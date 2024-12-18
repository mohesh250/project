import streamlit as st
from datetime import timedelta

st.title("Upload and View Text or Video Files")
uploaded_file = st.file_uploader("Choose a file", type=["txt", "mp4", "mov", "avi", "mkv", "flv"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    if file_type == "text/plain":
        file_content = uploaded_file.read().decode("utf-8")
        st.subheader("Text File Content:")
        st.text_area("File Content", file_content, height=300)
    elif file_type.startswith("video"):
        st.subheader("Video File:")

        # Video file upload display
        st.video(uploaded_file)

        # Optional: add a timestamp input to let users jump to a specific part of the video
        st.subheader("Jump to a Specific Time in the Video:")

        # Provide a time input box for the user to jump to a time in HH:MM:SS format
        video_time = st.text_input("Enter time in HH:MM:SS format", "00:00:00")

        try:
            # Parse the time string into seconds
            time_parts = video_time.split(":")
            if len(time_parts) == 3:
                hours, minutes, seconds = map(int, time_parts)
                total_seconds = timedelta(hours=hours, minutes=minutes, seconds=seconds).total_seconds()

                # Display a message to inform the user if the time input is valid
                st.write(f"Jumping to {video_time} ({total_seconds} seconds)...")

                # Play video from the specific timestamp (this feature needs to be handled in a frontend environment
                # or by using a more sophisticated tool, Streamlit itself doesn't allow jumping to a specific time in its video player)
                st.video(uploaded_file, start_time=int(total_seconds))
            else:
                st.error("Invalid time format! Please use HH:MM:SS.")
        except ValueError:
            st.error("Invalid time input! Make sure you use a valid HH:MM:SS format.")
    else:
        st.error("Unsupported file type!")
