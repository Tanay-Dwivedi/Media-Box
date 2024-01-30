import streamlit as sl
import os
from pytube import YouTube

sl.set_page_config(page_title="Media Box", page_icon="📱")

sl.title("Youtube Video Downloader")

with sl.form("Enter the Youtube video URL", clear_on_submit=False):
    inp_url = sl.text_input("video URL")
    video_resolution = sl.selectbox(
        "Select video resolution",
        options=["1080p", "720p", "480p", "360p", "240p", "144p"],
    )
    submit_btn = sl.form_submit_button("Download")

if submit_btn:
    sl.write("button pressed")
    try:
        yt = YouTube(inp_url)
        video_stream = yt.streams.filter(res=video_resolution).first()

        count = 1
        while os.path.exists(
            os.path.join(
                os.path.expanduser("~"), "Downloads", f"{yt.title} ({count}).mp4"
            )
        ):
            count += 1

        video_stream.download(
            output_path=os.path.join(
                os.path.expanduser("~"), "Downloads", f"{yt.title} ({count}).mp4"
            )
        )
        sl.success(f"Video Downloaded. See your Downloads folder.")
    except:
        sl.error("Enter the correct URL.")
        sl.error("Choose the correct available video resolution.")
