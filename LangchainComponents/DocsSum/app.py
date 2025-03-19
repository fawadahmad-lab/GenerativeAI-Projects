from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import streamlit as st
import PyPDF2
import pandas as pd
from PIL import Image
import pytesseract

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

# Streamlit UI
st.header("📄 Document Summary Generator")

# File uploader
file = st.file_uploader("Choose a file", type=["csv", "txt", "pdf", "png", "jpg"])

# Define the prompt template inline
prompt_template = PromptTemplate(
    input_variables=["document_text"],
    template="""
    You are an AI assistant that provides concise and informative summaries.
    Given the following document text, generate a summary that captures the key points.

    Document Text:
    {document_text}

    Summary:
    """
)

def process_file(file):
    """Extracts text content from different file types."""
    if file is None:
        return None  

    file_type = file.type

    try:
        # Process CSV file
        if file_type == "text/csv":
            df = pd.read_csv(file)
            return df.to_string()

        # Process TXT file
        elif file_type == "text/plain":
            return file.read().decode("utf-8").strip()

        # Process PDF file
        elif file_type == "application/pdf":
            text = ""
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text.strip() if text else None  

        # Process Images with OCR
        elif file_type in ["image/png", "image/jpeg"]:
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
            return text.strip() if text else None  

        else:
            return None  
    except Exception as e:
        st.error(f"⚠️ Error processing file: {e}")
        return None

if st.button('Submit'):
    extracted_text = process_file(file)

    if extracted_text:
        st.success("✅ Successfully extracted text!")
        st.text_area("Extracted Text Preview:", extracted_text, height=200)

        # Ensure correct input key for the model
        input_data = {"document_text": extracted_text}  

        try:
            chain = prompt_template | model
            result = chain.invoke(input_data)
            st.write("### 📌 Summary:")
            st.write(result.content)
        except Exception as e:
            st.error(f"⚠️ Error calling AI model: {e}")
    else:
        st.error("⚠️ No valid text found in the uploaded document. Please try another file.")
