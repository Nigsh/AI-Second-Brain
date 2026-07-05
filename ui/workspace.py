import streamlit as st
from ai.router import process
from ai.file_loader import read_file

def show_workspace():
    st.title("🧠 AI Second Brain Workspace")

    task = st.selectbox(
        "Choose Workflow",
        [
            "flashcards",
            "summary",
            "biomedical",
            "project",
            "organize",
            "research",
            "journal"
        ]
    )

    text_input = st.text_area(
        "Paste text OR use file upload below",
        height=200
    )

    uploaded_file = st.file_uploader(
        "Upload file (PDF / DOCX / TXT)",
        type=["pdf", "docx", "txt"]
    )

    col1, col2 = st.columns(2)

    show_output = col1.checkbox("Show output", value=True)

    if st.button("🚀 Process"):
        text = ""

        # If file uploaded → convert to text
        if uploaded_file is not None:
            text = read_file(uploaded_file)
        else:
            text = text_input

        if not text.strip():
            st.warning("Please provide input text or file")
            return

        with st.spinner("AI is processing..."):
            result = process(task, text)

        st.success("Done!")

        if show_output:
            st.markdown("### 🧠 Output")
            st.write(result)