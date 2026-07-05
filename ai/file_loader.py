from pypdf import PdfReader
from docx import Document


def read_file(uploaded_file):
    filename = uploaded_file.name.lower()

    if filename.endswith(".pdf"):
        return _read_pdf(uploaded_file)
    elif filename.endswith(".docx"):
        return _read_docx(uploaded_file)
    elif filename.endswith(".txt"):
        return _read_txt(uploaded_file)
    else:
        raise ValueError(f"Unsupported file type: {filename}")


def _read_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
        text += "\n"
    return text.strip()


def _read_docx(uploaded_file):
    document = Document(uploaded_file)
    return "\n".join(p.text for p in document.paragraphs).strip()


def _read_txt(uploaded_file):
    return uploaded_file.read().decode("utf-8").strip()
