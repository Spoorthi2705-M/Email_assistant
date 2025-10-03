import streamlit as st
from transformers import pipeline
import logging

@st.cache_resource
def load_summarizer():
    try:
        return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def summarize_text(text: str, summarizer, max_length: int = 130) -> str:
    if not text or len(text.strip()) < 50:
        return "Email too short to summarize."
    try:
        input_text = text[:1024]
        summary_list = summarizer(
            input_text,
            max_length=max_length,
            min_length=30,
            do_sample=False,
            truncation=True
        )
        if summary_list and len(summary_list) > 0:
            return summary_list[0]['summary_text']
        return "Could not generate summary."
    except Exception as e:
        logging.error(f"Summarization error: {e}")
        return "Summary unavailable - please review original email."
