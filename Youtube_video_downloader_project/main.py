from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    if request.method == 'POST':
        video_url = request.form['video_url']
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download('./downloads/')
            print ("Video Downloaded Successfully ")
            return "Video downloaded successfully!"
        except Exception as e:
            return "Error: " + str(e)

if __name__ == '__main__':
    app.run(debug=True)
