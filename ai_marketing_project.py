import streamlit as st
import os
import urllib.parse
from groq import Groq

# Screen ka Design aur Title
st.set_page_config(page_title="AI Marketing Agency", page_icon="🚀")
st.title("🚀 AI Marketing Agency-in-a-Box")
st.write("Apne brand ke liye marketing copy aur images generate karein!")

# Sidebar mein API key
st.sidebar.header("⚙️ Settings")
api_key = st.sidebar.text_input("Enter Groq API Key", type="password")

# User se details lene ke boxes
brand_name = st.text_input("Brand Name", "DigiCrome AI")
tone = st.text_input("Brand Tone", "professional, innovative, and friendly")
product = st.text_area("Product Brief", "AI Marketing Agency-in-a-Box for Small businesses")

# Generate Button
if st.button("✨ Generate Marketing Package"):
    if not api_key:
        st.error("⚠️ Please enter your Groq API Key in the left sidebar!")
    else:
        with st.spinner("AI aapka content aur images bana raha hai... ⏳"):
            try:
                # 1. Text Generate Karna (Groq API)
                client = Groq(api_key=api_key)
                prompt = f"You are a Copywriter for {brand_name}. Tone: {tone}. Write a short Instagram Caption and LinkedIn Post for: {product}."
                
                chat = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="qwen/qwen3.8-27b",
                    max_tokens=800
                )
                
                st.success("🎉 Package Ready!")
                st.subheader("📝 Generated Copy")
                st.write(chat.choices[0].message.content)
                
                # 2. Image Generate Karna (Pollinations AI)
                st.subheader("🖼️ Generated Visuals")
                safe_prompt = urllib.parse.quote(f"A modern workspace with laptop showing marketing analytics, {tone} style, high resolution")
                image_url = f"https://image.pollinations.ai/prompt/{safe_prompt}?width=800&height=400&nologo=true"
                
                st.image(image_url, caption="Campaign Image")
                
            except Exception as e:
                st.error(f"Error: {e}")
