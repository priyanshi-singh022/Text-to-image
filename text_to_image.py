from dotenv import load_dotenv
import os
import requests
# Load API key from .env
load_dotenv()
hf_token = os.getenv("HF_API_KEY")

if not hf_token:
    raise ValueError("⚠️ HF_API_KEY not found. Please set it in .env file")

# Hugging Face Stable Diffusion API
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {hf_token}"}

# Prompt from user
prompt = input("Prompt: ")

# Send request
response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

# Handle response
if response.status_code == 200:
    # Check if HuggingFace returned an image or JSON
    if response.headers.get("content-type") == "application/json":
        print("⚠️ Response:", response.json())  # e.g. model still loading
    else:
        output_file = "result.png"
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved as {output_file}")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
