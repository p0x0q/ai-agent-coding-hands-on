import os
from datetime import datetime
from zoneinfo import ZoneInfo
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from .state import AgentState


class RouterAgent:
    """Agent responsible for determining if web search is needed"""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            temperature=1.0  # Required for this model
        )

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", """あなたは質問の分類エキスパートです。ユーザーの質問を分析し、リアルタイムのWeb検索が必要かどうかを判定してください。

現在の日時: {current_datetime}

【Web検索が必要なケース】
- 最新のニュース、天気、株価などのリアルタイム情報
- 現在の日時が重要な質問（「今日は何日？」「今何時？」など）
- 最近の出来事や最新データが必要な質問
- 特定の場所の現在の状況（営業時間、混雑状況など）

【Web検索が不要なケース】
- 一般的な知識や概念の説明
- 挨拶や雑談
- 過去の会話の続きや文脈に基づく質問
- 計算や論理的推論のみで答えられる質問
- すでに会話履歴に情報がある質問

会話履歴:
{conversation_history}

判定は "RESEARCH_NEEDED" または "DIRECT_ANSWER" のいずれかで答えてください。
理由も簡潔に説明してください。"""),
            ("user", "{query}")
        ])

    async def execute(self, state: AgentState) -> AgentState:
        """Determine if web search is needed"""

        # Get current datetime in Japan timezone (JST)
        jst = ZoneInfo("Asia/Tokyo")
        current_datetime = datetime.now(jst).strftime("%Y年%m月%d日 %H時%M分%S秒")

        # Format conversation history for prompt
        conversation_context = "\n".join([
            f"{msg['role']}: {msg['content']}"
            for msg in state.get("conversation_history", [])[-5:]  # Last 5 messages
        ]) if state.get("conversation_history") else "（会話履歴なし）"

        # Make routing decision
        chain = self.prompt | self.llm
        response = await chain.ainvoke({
            "query": state["user_query"],
            "current_datetime": current_datetime,
            "conversation_history": conversation_context
        })

        # Parse the decision
        decision_text = response.content.upper()
        needs_research = "RESEARCH_NEEDED" in decision_text

        # Update state
        state["needs_research"] = needs_research
        state["step_history"].append({
            "agent": "Router",
            "action": f"判定: {'Web検索が必要' if needs_research else '直接回答可能'}",
            "result": response.content
        })

        return state
