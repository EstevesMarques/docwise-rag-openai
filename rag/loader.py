from pathlib import Path
from typing import List
from PyPDF2 import PdfReader
from config import DATA_DIR

def load_pdfs(data_dir: Path = DATA_DIR) -> List[str]:
    texts = []
    for pdf_file in data_dir.glob("*.pdf"):
        print(f"Lendo {pdf_file}...")
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        texts.append(text)
    return texts
