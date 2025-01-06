import os
import argparse

from src.downloader import download_comments


def main() -> None:
    parser = argparse.ArgumentParser(description="Download YouTube comments.")
    parser.add_argument("url", type=str, help="YouTube video URL")
    parser.add_argument("--output", type=str, default="output", help="Base directory")

    args: argparse.Namespace = parser.parse_args()
    os.makedirs(name=args.output, exist_ok=True)

    download_comments(video_url=args.url, output_dir=args.output)
    print(f"Comments downloaded and saved in `{args.output}/`")


if __name__ == "__main__":
    main()
