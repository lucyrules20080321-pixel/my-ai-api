from fastapi import FastAPI
import google.generativeai as genai
import os

app = FastAPI()

# 自动从系统读取你的秘密通行证
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_KEY)
model = 
genai.GenerativeModel('models/gemini-1.5-flash')
@app.get("/")
def home():
    return {"message": "我的手机手搓API已上线！"}

@app.get("/chat")
def chat(q: str):
    response = model.generate_content(q)
    return {"ai_answer": response.text}
