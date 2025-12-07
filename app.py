from transformers import pipeline
import gradio as gr

# Load the summarization model
model = pipeline("summarization")

def summarize_text(text):
    # Summarize the input text
    result = model(text, max_length=100, min_length=20, do_sample=False)
    return result[0]['summary_text']

# Create Gradio Interface
interface = gr.Interface(
    fn=summarize_text,
    inputs=gr.Textbox(lines=8, label="Enter text to summarize"),
    outputs=gr.Textbox(label="Summary", lines=8),
    title="Text Summarizer",
    description="Enter long text and get a short summary using HuggingFace Transformers."
)

interface.launch()
