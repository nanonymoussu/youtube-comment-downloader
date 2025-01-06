import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from typing import Any, Dict, List, Optional

load_dotenv()

api_key: str | None = os.getenv(key="YOUTUBE_API_KEY")
if not api_key:
    raise ValueError("YouTube API key not found in `.env` file.")

youtube: Any = build(serviceName="youtube", version="v3", developerKey=api_key)


def get_video_title(video_id: str) -> Optional[str]:
    """
    Get the title of a YouTube video.

    Args:
        video_id (str): YouTube video ID.

    Returns:
        str: YouTube video title, or None if video not found.
    """
    try:
        request: Any = youtube.videos().list(part="snippet", id=video_id)
        response: Dict[str, Any] = request.execute()

        if response.get("items"):
            return response["items"][0]["snippet"]["title"]
        return None  # video not found
    except HttpError as error:
        print(f"An HTTP error occurred: {error}")
        return None
    except KeyError as error:
        print(f"A key error occurred: {error}. Possibly malformed API response.")
        return None
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None


def fetch_comments(video_id: str) -> List[Dict[str, Any]]:
    """
    Fetch comments from a YouTube video.

    Args:
        video_id (str): YouTube video ID.

    Returns:
        List[Dict[str, str]]: List of comments with number, user, text and date.
    """
    try:
        request: Any = youtube.commentThreads().list(
            part="snippet", videoId=video_id, maxResults=100
        )

        comments: List[Dict[str, Any]] = []
        while request:
            response: Dict[str, Any] = request.execute()
            for item in response.get("items", []):
                snippet: Any = item["snippet"]["topLevelComment"]["snippet"]
                comments.append(
                    {
                        # "_no_": len(comments) + 1,
                        "user": snippet["authorDisplayName"],
                        "text": snippet["textOriginal"],
                        "date": snippet["updatedAt"],
                    }
                )
            request = youtube.commentThreads().list_next(request, response)

        comments.sort(key=lambda x: x["date"])
        for index, comment in enumerate(iterable=comments):
            comment["_no_"] = index + 1

        return comments
    except HttpError as error:
        print(f"An HTTP error occurred: {error}")
        return []
    except KeyError as error:
        print(f"A key error occurred: {error}. Possibly malformed API response.")
        return []
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return []
