import streamlit as sl

sl.set_page_config(
    page_title="Media Box",
    page_icon="📱"
)

sl.title("Mp4 to Mp3 converter")

with sl.form("Upload the video", clear_on_submit=False):
    inp_url = sl.file_uploader("Upload file")
    submit_btn = sl.form_submit_button("Convert to mp3")

if submit_btn:
    try:
        sl.success("Audio Downloaded. See your Downloads folder.")
    except:
        sl.error("Enter the correct file.")

