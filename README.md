# YouTube Video Downloader

This project is a simple web application built with Flask that allows users to download YouTube videos by providing the video URL. It utilizes the Pytube library to fetch and download the video.

## Features

- Users can input a YouTube video URL into a form.
- The application validates the URL and attempts to download the video.
- If successful, it provides a message confirming the download.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Pytube

You can install Flask and Pytube using pip:

```bash
pip install Flask
pip install pytube
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/youtube-downloader.git
```

2. Navigate to the project directory:

```bash
cd youtube-downloader
```

3. Run the Flask application:

```bash
python app.py
```

4. Open a web browser and go to http://localhost:5000 to access the application.

5. Enter a valid YouTube video URL into the input field and click the "Download" button.

6. Wait for the download to complete. Once finished, a success message will be displayed.

## File Structure

- `app.py`: Contains the Flask application code, including route definitions and request handling.
- `templates/index.html`: HTML template file for the user interface.
- `README.md`: Documentation file.
- `requirements.txt`: Lists the dependencies required for the project.

## Contributing

Contributions are welcome! If you have any ideas for improvement or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask: A lightweight WSGI web application framework in Python.
- Pytube: A simple, yet versatile library for downloading YouTube videos.

## Disclaimer

This project is for educational purposes only. Please respect the copyright policies of YouTube and use the downloaded videos responsibly.
