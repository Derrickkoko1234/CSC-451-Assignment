import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize

# Download the 'punkt' tokenizer if not already downloaded
nltk.download('punkt')

# List of downloaded PDF file paths
pdf_paths = ["pdf1.pdf", "pdf2.pdf", "pdf3.pdf"]

# Iterate over each PDF file
for i, pdf_path in enumerate(pdf_paths):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Extract text from the PDF file
    text = ""
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    # Find the start and end index of the abstract
    abstract_start = text.find("ABSTRACT:")
    if "KEYWORDS:" in text[abstract_start:]:
        abstract_end = text.find("KEYWORDS:", abstract_start)
    else:
        abstract_end = text.find("I. INTRODUCTION", abstract_start)

    # Extract the abstract
    abstract = text[abstract_start + len("ABSTRACT:"):abstract_end].strip()

    # Count the number of sentences and words in the abstract
    sentences = sent_tokenize(abstract)
    num_sentences = len(sentences)
    num_words = sum(len(sent.split()) for sent in sentences)

    # Print observations
    print(f"PDF {i+1}:\nNumber of sentences in abstract: {num_sentences}\nNumber of words in abstract: {num_words}\n")
