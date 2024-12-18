import streamlit as st

# Title of the Streamlit app
st.title("Upload and View Text or Video Files")

# File uploader widget allows multiple files to be uploaded
uploaded_files = st.file_uploader("Choose files", type=["txt", "mp4", "mov", "avi", "mkv", "flv"],
                                  accept_multiple_files=True)

# Initialize lists to hold text and video files
text_files = []
video_files = []

# Process uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_type = uploaded_file.type

        # If the file is a text file
        if file_type == "text/plain":
            text_files.append(uploaded_file)

        # If the file is a video file
        elif file_type.startswith("video"):
            video_files.append(uploaded_file)

    # Add a search bar to filter files
    search_query = st.text_input("Search for a file", "")

    # Filter text files based on the search query
    filtered_text_files = [file for file in text_files if search_query.lower() in file.name.lower()]

    # Filter video files based on the search query
    filtered_video_files = [file for file in video_files if search_query.lower() in file.name.lower()]

    # Show filtered text files and their contents
    if filtered_text_files:
        st.subheader("Text Files Content:")
        for text_file in filtered_text_files:
            file_content = text_file.read().decode("utf-8")
            st.text_area(f"Content of {text_file.name}", file_content, height=300)
    else:
        st.write("No text files found matching your search.")

    # Show filtered video files and allow video selection
    if filtered_video_files:
        st.subheader("Video Files:")

        # Create a dropdown to select a video
        video_file_names = [file.name for file in filtered_video_files]
        selected_video = st.selectbox("Select a video to play", video_file_names)

        # Display the selected video
        for video_file in filtered_video_files:
            if video_file.name == selected_video:
                st.video(video_file)
    else:
        st.write("No video files found matching your search.")
