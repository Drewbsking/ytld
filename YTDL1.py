
import yt_dlp

url = "https://www.youtube.com/watch?v=vXoX3CyXtv4"  # Replace with actual URL

ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])