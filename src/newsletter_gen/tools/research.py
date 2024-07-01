from crewai_tools import BaseTool
from exa_py import Exa
import os
from datetime import datetime

class SearchAndContents(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for the latest results. "
        "Results are only from the custom date range entered by the user. Uses the Exa API. This also returns the contents of the search results."
    )

    def _run(self, search_query: str, start_date: str) -> str:
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        # Validate and format the start_date
        try:
            start_published_date = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

        end_published_date = datetime.now().strftime("%Y-%m-%d")

        # Log the dates for debugging
        print(f"Searching from {start_published_date} to {end_published_date}")

        search_results = exa.search_and_contents(
            query=search_query,
            use_autoprompt=True,
            start_published_date=start_published_date,
            text={"include_html_tags": False, "max_characters": 8000},
        )

        return search_results


class FindSimilar(BaseTool):
    name: str = "Find Similar Tool"
    description: str = (
        "Searches for similar articles to a given article using the Exa API. Takes in a URL of the article."
    )

    def _run(self, article_url: str, start_date: str) -> str:
        # Validate and format the start_date
        try:
            start_published_date = datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

        end_published_date = datetime.now().strftime("%Y-%m-%d")

        # Log the dates for debugging
        print(f"Searching from {start_published_date} to {end_published_date}")

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        search_results = exa.find_similar_and_contents(
            url=article_url,
            start_published_date=start_published_date,
            text={"include_html_tags": False, "max_characters": 8000},
        )

        return search_results


class GetContents(BaseTool):
    name: str = "Get Contents Tool"
    description: str = (
        "Gets the contents of a specific article using the Exa API. "
        "Takes in the ID of the article in a list, like this: ['https://www.cnbc.com/2024/04/18/my-news-story']."
    )

    def _run(self, article_ids: list) -> str:
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        contents = exa.contents(ids=article_ids)
        return contents
