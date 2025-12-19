import os
from datetime import datetime
from zoneinfo import ZoneInfo
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from .state import AgentState
from ..services.perplexity import PerplexityService


class ResearcherAgent:
    """Agent responsible for gathering information via web search"""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            temperature=1.0
        )
        self.perplexity = PerplexityService()

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a research assistant. Your job is to:
1. Analyze the user's query
2. Determine what information needs to be searched
3. Format search queries effectively

Current date and time: {current_datetime}

Based on the user query, create a concise search query for web search.
If the query is time-sensitive, include relevant date/time information in the search query."""),
            ("user", "{query}")
        ])

    async def execute(self, state: AgentState) -> AgentState:
        """Execute the research step"""

        # Get current datetime in Japan timezone (JST)
        jst = ZoneInfo("Asia/Tokyo")
        current_datetime = datetime.now(jst).strftime("%Y年%m月%d日 %H時%M分%S秒")

        # Generate search query
        search_query_chain = self.prompt | self.llm
        search_query_response = await search_query_chain.ainvoke({
            "query": state["user_query"],
            "current_datetime": current_datetime
        })
        search_query = search_query_response.content

        # Execute web search using Perplexity
        search_result = await self.perplexity.search(search_query)

        # Update state
        state["research_data"] = search_result.get("content", "No data found")
        state["step_history"].append({
            "agent": "Researcher",
            "action": f"Searched: {search_query}",
            "result": f"Found {len(search_result.get('citations', []))} sources"
        })

        return state
