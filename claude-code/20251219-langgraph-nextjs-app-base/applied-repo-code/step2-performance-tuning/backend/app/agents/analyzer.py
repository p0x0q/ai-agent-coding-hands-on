import os
from datetime import datetime
from zoneinfo import ZoneInfo
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from .state import AgentState


class AnalyzerAgent:
    """Agent responsible for analyzing collected information"""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            temperature=1.0
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """You are an analytical expert. Your job is to:
1. Review the research data provided
2. Extract key insights and patterns
3. Identify relevant information for answering the user's question
4. Organize findings in a structured way

Current date and time: {current_datetime}

Analyze the research data and provide key insights."""),
            ("user", """User Query: {query}

Research Data:
{research_data}

Provide your analysis:""")
        ])

    async def execute(self, state: AgentState) -> AgentState:
        """Execute the analysis step"""

        # Get current datetime in Japan timezone (JST)
        jst = ZoneInfo("Asia/Tokyo")
        current_datetime = datetime.now(jst).strftime("%Y年%m月%d日 %H時%M分%S秒")

        chain = self.prompt | self.llm
        response = await chain.ainvoke({
            "query": state["user_query"],
            "research_data": state["research_data"],
            "current_datetime": current_datetime
        })

        # Update state
        state["analysis_result"] = response.content
        state["step_history"].append({
            "agent": "Analyzer",
            "action": "Analyzed research data",
            "result": "Extracted key insights"
        })

        return state
