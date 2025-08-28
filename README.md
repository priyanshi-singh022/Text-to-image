# Text-to-Image Generator (Python)

Generate images from text prompts using Hugging Face's Stable Diffusion API.

---

## Features

- Generate high-quality images from descriptive text prompts
- Saves generated images locally as `result.png`
- Easy to set up using a `.env` file for your API key
- Beginner-friendly and ready to run

---

## Demo
![prompt](Images/ss.png)
![result](Images/result.png)

---

## Technologies Used

- Python 3.7+
- `requests` for HTTP requests
- `python-dotenv` for environment variable management
- Hugging Face Stable Diffusion API

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/text-to-image.git
cd text-to-image
```
2. **Install dependencies:**
```bash
pip install requests python-dotenv
```
3. **Create a .env file in the project root and add your Hugging Face API key:**
```bash
HF_API_KEY=your_api_key_here
```
---

## How It Works
- The script loads your API key from .env
- You enter a descriptive text prompt
- The script sends your prompt to Hugging Face's Stable Diffusion API
- The API generates an image and saves it as result.png
