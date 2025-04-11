import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch

# Tên thư mục chứa adapter model
ADAPTER_PATH = "./lap_qwen-mental-health-finetuned"

# Load model & tokenizer
@st.cache_resource
def load_model():
    # Load thông tin adapter
    config = PeftConfig.from_pretrained(ADAPTER_PATH)

    # Load base model (từ HuggingFace hoặc local)
    base_model = AutoModelForCausalLM.from_pretrained(
        config.base_model_name_or_path,
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto"
    )

    # Áp dụng adapter vào base model
    model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
    tokenizer = AutoTokenizer.from_pretrained(config.base_model_name_or_path)

    model.eval()
    return tokenizer, model

# Giao diện Streamlit
st.set_page_config(page_title="Chatbot Tâm lý (Adapter)", layout="centered")
st.title("🧠 Chatbot Tư vấn Tâm lý")

with st.spinner("🔧 Đang tải mô hình..."):
    tokenizer, model = load_model()

user_input = st.text_area("💬 Nhập câu hỏi của bạn:", height=100)

if st.button("🧠 Trả lời"):
    if not user_input.strip():
        st.warning("⛔ Vui lòng nhập câu hỏi.")
    else:
        with st.spinner("🤖 Đang sinh phản hồi..."):
            prompt = f"<|user|>\n{user_input.strip()}\n<|assistant|>\n"
            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

            with torch.no_grad():
                output = model.generate(
                    **inputs,
                    max_new_tokens=512,
                    temperature=0.7,
                    top_p=0.9,
                    do_sample=True,
                    pad_token_id=tokenizer.eos_token_id
                )

            decoded = tokenizer.decode(output[0], skip_special_tokens=True)
            response = decoded.split("<|assistant|>")[-1].strip()
            st.success(response)
