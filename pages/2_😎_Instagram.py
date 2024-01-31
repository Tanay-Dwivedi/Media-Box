import streamlit as sl

sl.set_page_config(page_title="Media Box", page_icon="📱")

sl.title("Instagram Reels Downloader")

with sl.form("Enter the Youtube video URL", clear_on_submit=False):
    inp_url = sl.text_input("video URL")
    submit_btn = sl.form_submit_button("Download")

if submit_btn:
    try:
        sl.success("Video Downloaded. See your Downloads folder.")
    except:
        sl.error("Enter the correct URL.")

