from typing import TypedDict, List, Dict, Annotated
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """State shared across all agents in the graph"""

    # User input
    user_query: str

    # Conversation history (for context-aware responses)
    conversation_history: List[Dict[str, str]]

    # Flag to determine if web search is needed
    needs_research: bool

    # Messages history
    messages: Annotated[List[Dict], add_messages]

    # Research data from Researcher Agent
    research_data: str

    # Analysis result from Analyzer Agent
    analysis_result: str

    # Final answer from Composer Agent
    final_answer: str

    # Execution history for tracking agent steps
    step_history: List[Dict[str, str]]
