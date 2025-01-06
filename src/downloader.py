import os
import re
from typing import Any, Dict, List, Optional

from .exporter import save_as_txt, save_as_csv, save_as_xlsx, save_as_json
from .youtube_api import fetch_comments, get_video_title


def sanitize_filename(filename: str) -> str:
    """Sanitize the filename by removing invalid characters."""
    return re.sub(pattern=r'[<>:"/\\|?*]', repl="", string=filename)


def download_comments(video_url: str, output_dir: str) -> None:
    """
    Download YouTube comments and export them to multiple formats.

    Args:
        video_url (str): YouTube video URL.
        output_dir (str): Base directory to save exported files.
    """
    video_id: str = video_url.split(sep="v=")[-1]
    video_title: Optional[str] = get_video_title(video_id=video_id)
    comments: List[Dict[str, Any]] = fetch_comments(video_id=video_id)

    if video_title and comments:
        sanitized_title: str = sanitize_filename(filename=video_title)
        formatted_output_dir: str = os.path.join(output_dir, sanitized_title)
        os.makedirs(name=formatted_output_dir, exist_ok=True)

        save_as_txt(
            comments=comments,
            filename=f"{formatted_output_dir}/comments.txt",
        )
        save_as_csv(
            comments=comments,
            filename=f"{formatted_output_dir}/comments.csv",
        )
        save_as_xlsx(
            comments=comments,
            filename=f"{formatted_output_dir}/comments.xlsx",
        )
        save_as_json(
            comments=comments,
            filename=f"{formatted_output_dir}/comments.json",
        )
    elif not video_title:
        print(f"Failed to retrieve video title for {video_url}. Skipping download.")
    elif not comments:
        print(f"No comments found for {video_url}.")
