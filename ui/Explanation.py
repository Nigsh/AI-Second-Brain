import streamlit as st

def show_biomedical():
    st.header(" Biomedical Explainer")

    topic = st.text_input(
        "Biomedical Topic",
        placeholder="Example: MRI, ECG, EEG..."
    )

    if st.button("Explain Topic"):
        st.info("🚧 Biomedical AI will be connected here.")
        