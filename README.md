# 🧠 Qwen-Psychology-Counseling-Chatbot

An AI-powered chatbot for answering psychology-related questions, built with the Flan-T5 language model and fine-tuned using LoRA. The system combines Hugging Face Transformers with Streamlit for an interactive frontend.

## 📦 Features

- Fine-tuned **Qwen** model with **LoRA**
- Hugging Face integration via `.env` token
- Local inference and Streamlit-based UI
- Support for both training in Colab and deployment on local machine

## 🚀 Setup & Run

### 1. Environment Setup

```bash
conda create -n myenv python=3.11
conda activate myenv
pip install -r requirements.txt
streamlit run app.py
