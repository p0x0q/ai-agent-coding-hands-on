import os
from datetime import datetime
from zoneinfo import ZoneInfo
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from .state import AgentState


class ComposerAgent:
    """Agent responsible for composing the final response"""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            temperature=1.0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a skilled communicator. Your job is to:
1. Synthesize research findings and analysis (if available)
2. Create a clear, well-structured response
3. Ensure the answer directly addresses the user's question
4. Format the response in a user-friendly way
5. Use conversation history for context-aware responses

Current date and time: {current_datetime}

Conversation History:
{conversation_history}

When answering time-sensitive questions, always reference the current date/time.
Compose a comprehensive answer based on the analysis or your knowledge."""),
            ("user", """User Query: {query}

Analysis Result:
{analysis}

Compose a final answer:""")
        ])

    async def execute(self, state: AgentState) -> AgentState:
        """Execute the composition step"""

        # Get current datetime in Japan timezone (JST)
        jst = ZoneInfo("Asia/Tokyo")
        current_datetime = datetime.now(jst).strftime("%Y年%m月%d日 %H時%M分%S秒")

        # Format conversation history
        conversation_context = "\n".join([
            f"{msg['role']}: {msg['content']}"
            for msg in state.get("conversation_history", [])[-5:]  # Last 5 messages
        ]) if state.get("conversation_history") else "（会話履歴なし）"

        # If no research was done, provide empty analysis
        analysis = state.get("analysis_result", "検索不要のため、知識ベースから直接回答")

        chain = self.prompt | self.llm
        response = await chain.ainvoke({
            "query": state["user_query"],
            "analysis": analysis,
            "current_datetime": current_datetime,
            "conversation_history": conversation_context
        })

        # Update state
        state["final_answer"] = response.content
        state["step_history"].append({
            "agent": "Composer",
            "action": "Composed final answer",
            "result": "Answer ready"
        })

        return state
