import streamlit as st
import transformers
from transformers import pipeline
pipe = pipeline("text-classification")
st.title("Sentiment Analysis")
def create_message_box(message, bg_color, text_color):
    style = f"""
    <style>
    .message-box {{
        padding: 20px;
        border-radius: 10px;
        background-color: {bg_color};
        color: {text_color};
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    }}
    </style>
    """
    message_box = f'<div class="message-box">{message}</div>'
    st.write(style, unsafe_allow_html=True)
    st.write(message_box, unsafe_allow_html=True)
def main():
    bg_color = "#ffd699"  # Light orange
    text_color = "#333333"  # Dark gray
    st.header("Input Review:")
    user_input = st.text_input("")
    sentiment=pipe(user_input)
    first_item=sentiment[0]
    FinalSentiment = first_item.get('label', '')
    if FinalSentiment:
        st.header("Sentiment:")
        create_message_box(FinalSentiment, bg_color, text_color)


if __name__ == "__main__":
    main()