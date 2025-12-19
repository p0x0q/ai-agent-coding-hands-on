import os
import httpx
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)


class PerplexityService:
    """Perplexity API service for web search"""

    def __init__(self):
        self.api_key = os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY is not set")

        self.base_url = "https://api.perplexity.ai"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def search(self, query: str) -> Dict[str, Any]:
        """
        Execute a web search using Perplexity API

        Args:
            query: Search query string

        Returns:
            Dictionary containing search results
        """
        logger.info(f"[Perplexity API] Executing search for query: {query}")

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": "sonar-pro",
                        "messages": [
                            {
                                "role": "user",
                                "content": query
                            }
                        ]
                    },
                    timeout=60.0
                )
                response.raise_for_status()
                data = response.json()

                logger.info(f"[Perplexity API] Search successful. Citations: {len(data.get('citations', []))}")

                return {
                    "success": True,
                    "content": data["choices"][0]["message"]["content"],
                    "citations": data.get("citations", [])
                }
            except httpx.HTTPStatusError as e:
                error_detail = e.response.text
                logger.error(f"[Perplexity API] Search failed: {str(e)}")
                logger.error(f"[Perplexity API] Error detail: {error_detail}")
                return {
                    "success": False,
                    "error": str(e),
                    "content": "Web search failed"
                }
            except httpx.HTTPError as e:
                logger.error(f"[Perplexity API] Search failed: {str(e)}")
                return {
                    "success": False,
                    "error": str(e),
                    "content": "Web search failed"
                }
