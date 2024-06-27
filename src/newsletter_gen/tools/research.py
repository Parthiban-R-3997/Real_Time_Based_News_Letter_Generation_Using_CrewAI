from crewai_tools import BaseTool
from exa_py import Exa
import os
from datetime import datetime, timedelta
import requests

class SearchAndContents(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for results within a specified date range. Uses the Exa API. This also returns the contents of the search results."
    )

    def _run(self, search_query: str, start_datetime: datetime, end_datetime: datetime) -> str:
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))
        
        try:
            search_results = exa.search_and_contents(
                query=search_query,
                use_autoprompt=True,
                start_published_date=start_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
                end_published_date=end_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
                text={"include_html_tags": False, "max_characters": 8000},
            )
            return search_results
        except requests.RequestException as e:
            return f"An error occurred while searching: {str(e)}"

class FindSimilar(BaseTool):
    name: str = "Find Similar Tool"
    description: str = (
        "Searches for similar articles to a given article within a specified date range using the Exa API. Takes in a URL of the article."
    )

    def _run(self, article_url: str, start_datetime: datetime, end_datetime: datetime) -> str:
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        try:
            search_results = exa.find_similar(
                url=article_url, 
                start_published_date=start_datetime.strftime("%Y-%m-%dT%H:%M:%S"),
                end_published_date=end_datetime.strftime("%Y-%m-%dT%H:%M:%S")
            )
            return search_results
        except requests.RequestException as e:
            return f"An error occurred while finding similar articles: {str(e)}"

class GetContents(BaseTool):
    name: str = "Get Contents Tool"
    description: str = "Gets the contents of specific articles using the Exa API. Takes in a list of article IDs."
    
    def _run(self, article_ids: list, start_datetime: datetime = None, end_datetime: datetime = None) -> str:
        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        try:
            contents = exa.get_contents(article_ids)
            
            # If date filtering is supported, you could implement it here
            # This is a placeholder and might not be directly supported by the API
            if start_datetime and end_datetime:
                filtered_contents = [
                    content for content in contents 
                    if start_datetime <= datetime.fromisoformat(content['published_date']) <= end_datetime
                ]
                return filtered_contents
            
            return contents
        except requests.RequestException as e:
            return f"An error occurred while getting contents: {str(e)}"