# YouTube Comment Downloader

A Python tool to download comments from YouTube videos and export them to multiple formats (TXT, CSV, XLSX, JSON).

## Features

- Download comments from a YouTube video.
- Export comments to TXT, CSV, XLSX, and JSON formats.
- Handles invalid characters in filenames.

## Requirements

- Python 3.7+
- YouTube Data API v3 key

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/youtube-comment-downloader.git
   cd youtube-comment-downloader
   ```

2. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your YouTube API key:

   ```env
   YOUTUBE_API_KEY=your_api_key_here
   ```

## Usage

Run the script with the YouTube video URL and an optional output directory:

```sh
python main.py "https://www.youtube.com/watch?v=Ju6_DpfPEeI" --output "output_directory"
```

### Arguments

- `url`: The YouTube video URL.
- `--output`: (Optional) The base directory to save exported files. Default is `output`.

## Example

```sh
python main.py "https://www.youtube.com/watch?v=Ju6_DpfPEeI" --output "comments"
```

This will download the comments from the specified YouTube video and save them in the `comments` directory.

## License

This project is licensed under the MIT License.
