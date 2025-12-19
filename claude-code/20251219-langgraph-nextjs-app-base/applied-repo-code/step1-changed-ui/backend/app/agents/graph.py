from langgraph.graph import StateGraph, END
from .state import AgentState
from .router import RouterAgent
from .researcher import ResearcherAgent
from .analyzer import AnalyzerAgent
from .composer import ComposerAgent


def route_after_router(state: AgentState) -> str:
    """Determine the next node based on research necessity"""
    if state.get("needs_research", False):
        return "researcher"
    else:
        return "composer"


def create_agent_graph():
    """Create and configure the LangGraph agent workflow"""

    # Initialize agents
    router = RouterAgent()
    researcher = ResearcherAgent()
    analyzer = AnalyzerAgent()
    composer = ComposerAgent()

    # Create the graph
    workflow = StateGraph(AgentState)

    # Add nodes for each agent
    workflow.add_node("router", router.execute)
    workflow.add_node("researcher", researcher.execute)
    workflow.add_node("analyzer", analyzer.execute)
    workflow.add_node("composer", composer.execute)

    # Define the workflow edges
    workflow.set_entry_point("router")

    # Conditional edge: route to researcher or composer based on needs_research flag
    workflow.add_conditional_edges(
        "router",
        route_after_router,
        {
            "researcher": "researcher",
            "composer": "composer"
        }
    )

    # Research path: researcher -> analyzer -> composer
    workflow.add_edge("researcher", "analyzer")
    workflow.add_edge("analyzer", "composer")

    # Both paths end at composer
    workflow.add_edge("composer", END)

    # Compile the graph
    app = workflow.compile()

    return app
