---
title: My Sign Language Bot
emoji: 📊
colorFrom: pink
colorTo: blue
sdk: gradio
sdk_version: 5.42.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: This app uses a custom machine learning model to detect sign
---

Check out the configuration reference at https://silent-bridge-ai-sinhala.onrender.com/
"" 
# Silent Bridge Ai

> **Breaking communication barriers through real-time AI sign language translation in English and Sinhala.**

---

## About the Project
**Silent Bridge Ai** is an intelligent, web-based sign language translation platform built for the **Young Computer Scientist (YCS)** competition. The project bridges the communication gap between the hearing community and individuals who use sign language, offering seamless, real-time translations deployed across web applications for both English and Sinhala speakers.

By leveraging computer vision and deep learning directly inside a browser-based webcam stream, Silent Bridge Ai processes gestures instantly with high-frequency frame capture, translating sign language symbols into readable text dynamically.

---

## Important Note on Cloud Hosting (Render)
Both the English and Sinhala applications are hosted on **Render's free tier**. 
* **Cold Start Delay:** If the web applications have not been visited recently, Render puts the server to sleep to save resources. When you first open the live link, **it may take 50 seconds or more for the server to spin up and become active**. Please wait a moment for the initialization page to load!

---

## Key Features
* **Real-Time Translation Loop:** Optimized video frame processing pipeline running at maximum refresh frequency for zero-lag gesture recognition.
* **Bilingual Support (English & Sinhala):** Seamless integration between two dedicated platform instances allowing users to toggle languages effortlessly via an intuitive dropdown menu.
* **Multi-Camera Selection:** Automatically detects and lets users switch between available web devices (built-in webcams, external USB cameras, etc.).
* **Cross-Platform Navigation:** Built-in glassmorphism navigation links connecting directly to the main portfolio and corresponding language mirrors.

---

## Technology Stack

### Frontend
* **HTML5 & CSS3:** Modern, responsive UI featuring custom gradients, Google Fonts (`Orbitron`), and glassmorphism styling.
* **JavaScript (ES6+):** Manages webcam streams via `navigator.mediaDevices`, canvas frame extraction, and asynchronous backend communication (`fetch` API).

### Backend & AI / Machine Learning
* **Python / Flask:** Lightweight web server handling incoming image payloads and model inference endpoints (`/predict`).
* **Deep Learning / Computer Vision:** Custom-trained image classification models analyzing hand signs and returning predicted classes alongside confidence scores.

---

## Project Architecture

```text
Silent-Bridge-Ai/
│
├── app.py                  # Flask backend server & model prediction route
├── requirements.txt        # Python dependencies (Flask, torch, torchvision, etc.)
├── templates/
│   └── index.html          # Main interactive user interface (Webcam + UI)
└── README.md               # Project documentation
```

## How It Works (Technical Workflow)

1. **Webcam Initialization:** The browser requests permission to access the user's camera feed (`navigator.mediaDevices.getUserMedia`).
2. **Frame Capture & Optimization:** As video plays, a hidden HTML5 canvas captures frames at 224x224 pixels, compressing them into JPEG format (`0.8` quality) to reduce payload size and speed up network transmission.
3. **Inference Request:** Base64-encoded image data is dispatched asynchronously via a `POST` request to the Flask backend `/predict` endpoint.
4. **Result Rendering:** The AI model classifies the sign, returning the predicted class and confidence score, which instantly updates the UI text element.

---

## Live Deployments
* **English Platform:** [https://silent-bridge-ai.onrender.com/](https://silent-bridge-ai.onrender.com/) *(May take ~50s to wake up on first load)*
* **Sinhala Platform:** [https://silent-bridge-ai-sinhala.onrender.com/](https://silent-bridge-ai-sinhala.onrender.com/) *(May take ~50s to wake up on first load)*
* **Project Portfolio:** [Sign Language Bot Website](https://sign-language-bot.mystrikingly.com/)

---

* **Live Platform:** [Silent Bride Ai](https://sign-language-bot.mystrikingly.com/)

* **Project Resources & Documentation (Google Drive):** [Access Drive Folder](https://drive.google.com/drive/folders/1sIAd2QQba0OoaQ3N32dQoM4D28qOpFzw?usp=drive_link)

* **Project Showcase Video:** [Silent Bridge Ai | Video #01](https://youtu.be/WnqLWqmSwuE)

* **Concept Evolution & Previous Versions:**
  * [Coolest Project '25 | AI-Powered Sign Language Translator Robot](https://youtu.be/5ZqNzwZ9Rr0)
  * [Sign Language Translator Bot | #2](https://youtu.be/OyLwNhvlcZY)
---

## Local Installation & Setup Guide

If you want to run this project locally on your machine for testing or offline demonstrations during your YCS presentation, follow these step-by-step instructions:

### Prerequisites
Make sure you have the following installed on your computer:
* **Python** (Version 3.8 or higher recommended)
* **Git**
* A working **Webcam** (built-in or USB)

### Step 1: Clone the Repository
Open your terminal (Command Prompt, PowerShell, or Bash) and run:
```bash
git clone [https://github.com/your-username/silent-bridge-ai.git](https://github.com/your-username/silent-bridge-ai.git)
cd silent-bridge-ai
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
It is best practice to isolate your project dependencies using a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
Install all required Python libraries (Flask, PyTorch, torchvision, etc.) listed in the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Flask Application
Start the backend server by running:
```bash
python app.py
```

### Step 5: Open in Your Web Browser
Open your web browser (Chrome, Firefox, or Edge) and go to:
```text
[http://127.0.0.1:5000](http://127.0.0.1:5000)
```

---

## Developed For
**Young Computer Scientist (YCS)** Competition  
*Empowering accessibility and inclusion through artificial intelligence.*

**Developer:** Shawin James  
**Serial No:** GS3-458

* **Project Showcase Video:** [Silent Bridge Ai | Video #01](https://youtu.be/WnqLWqmSwuE)
