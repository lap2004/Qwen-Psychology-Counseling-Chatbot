# 🧠 Qwen-Psychology-Counseling-Chatbot

An AI-powered chatbot for answering psychology-related questions, built with the Flan-T5 language model and fine-tuned using LoRA. The system combines Hugging Face Transformers with Streamlit for an interactive frontend.

## 📦 Features

- Fine-tuned **Qwen** model with **LoRA**
- Hugging Face integration via `.env` token
- Local inference and Streamlit-based UI
- Support for both training in Colab and deployment on local machine

## 🚀 Setup & Run

### 1. Environment Setup

- Dùng python version 3.11
- Nên dùng conda, setup environment qua câu lệnh: conda create -n myenv python=3.11
- Sau đó active enviroment qua câu lệnh: conda activate myenv
- Cài các thư viện cần thiết : pip install -r requirements.txt
### 2: Cấu hình Hugging Face

1. Tạo file `.env`
2. Truy cập Hugging Face để lấy token API của bạn
Options: Login khi chạy file Chatbot.ipynb trên colab và nhập token API
### 3: Chạy ứng dụng
Chạy file Qwen.ipynb Mở Terminal/Command Prompt, di chuyển vào thư mục src cd colab và chạy:
```python
python Qwen.ipynb
```
Run ứng dụng:
```python
streamlit run app.py
```
