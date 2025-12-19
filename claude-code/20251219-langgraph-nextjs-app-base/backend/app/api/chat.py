import time
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from ..models import ChatRequest, ChatResponse, AgentStep, WorkflowInfo, AgentInfo
from ..agents import create_agent_graph

router = APIRouter()

# Initialize the agent graph
agent_graph = create_agent_graph()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Process a chat message through the multi-agent system

    Args:
        request: ChatRequest containing the user message

    Returns:
        ChatResponse with the final answer and agent execution steps
    """
    try:
        # Start timer
        start_time = time.time()

        # Initialize the state
        initial_state = {
            "user_query": request.message,
            "conversation_history": request.conversation_history,
            "needs_research": False,  # Will be determined by Router agent
            "messages": [],
            "research_data": "",
            "analysis_result": "",
            "final_answer": "",
            "step_history": []
        }

        # Run the agent graph
        result = await agent_graph.ainvoke(initial_state)

        # Calculate elapsed time
        elapsed_time = round(time.time() - start_time, 1)

        # Convert step history to AgentStep objects
        steps = [
            AgentStep(
                agent=step["agent"],
                action=step["action"],
                result=step.get("result")
            )
            for step in result["step_history"]
        ]

        return ChatResponse(
            response=result["final_answer"],
            steps=steps,
            elapsed_time=elapsed_time
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@router.get("/workflow/graph")
async def get_workflow_graph():
    """
    Get the LangGraph workflow visualization as PNG image

    Returns:
        PNG image showing the agent workflow structure
    """
    try:
        # Generate the graph visualization using LangGraph's built-in method
        png_data = agent_graph.get_graph().draw_mermaid_png()

        return Response(
            content=png_data,
            media_type="image/png",
            headers={
                "Cache-Control": "no-cache, no-store, must-revalidate",  # Always fetch fresh
                "Pragma": "no-cache",
                "Expires": "0",
                "Content-Disposition": "inline; filename=workflow.png"
            }
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate workflow graph: {str(e)}"
        )


@router.get("/workflow/info", response_model=WorkflowInfo)
async def get_workflow_info():
    """
    Get information about the agent workflow configuration

    Returns:
        WorkflowInfo containing agent descriptions and workflow structure
    """
    return WorkflowInfo(
        description="LangGraphによるマルチエージェントワークフロー。Routerが質問を判定し、必要に応じてWeb検索を実行します。",
        agents=[
            AgentInfo(
                name="Router",
                description="質問を分析し、Web検索の必要性を判定（最新情報が必要か、直接回答可能か）",
                order=1
            ),
            AgentInfo(
                name="Researcher",
                description="ユーザーの質問を分析し、Perplexity APIでWeb検索を実行（検索が必要な場合のみ）",
                order=2
            ),
            AgentInfo(
                name="Analyzer",
                description="収集された情報を分析し、重要な洞察を抽出（検索が実行された場合のみ）",
                order=3
            ),
            AgentInfo(
                name="Composer",
                description="分析結果または知識ベースから、ユーザーに分かりやすい回答を生成",
                order=4
            )
        ]
    )
