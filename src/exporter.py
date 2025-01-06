import pandas as pd
from typing import Any, Dict, List


def save_as_txt(comments: List[Dict[str, Any]], filename: str) -> None:
    """Save comments to a TXT file."""
    with open(file=filename, mode="w", encoding="utf-8") as file:
        for comment in comments:
            file.write(
                f"_No.: {comment['_no_']}\nUser: {comment['user']}\nText: {comment['text']}\nDate: {comment['date']}\n\n"
            )


def save_as_csv(comments: List[Dict[str, Any]], filename: str) -> None:
    """Save comments to a CSV file."""
    df: pd.DataFrame = pd.DataFrame(data=comments)
    df.to_csv(path_or_buf=filename, index=False, encoding="utf-8")


def save_as_xlsx(comments: List[Dict[str, Any]], filename: str) -> None:
    """Save comments to an XLSX file."""
    df: pd.DataFrame = pd.DataFrame(data=comments)
    df.to_excel(excel_writer=filename, index=False, engine="openpyxl")


def save_as_json(comments: List[Dict[str, Any]], filename: str) -> None:
    """Save comments to a JSON file."""
    pd.DataFrame(data=comments).to_json(
        path_or_buf=filename, orient="records", force_ascii=False, indent=2
    )
