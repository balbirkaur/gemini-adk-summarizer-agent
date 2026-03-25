# 🚀 Gemini ADK Summarizer Agent

---

## 📌 Problem Statement

Build and deploy a single AI agent using ADK and Gemini that is hosted on Cloud Run and performs one clearly defined task.
The agent must be callable via an HTTP endpoint and return a valid response for a given input.

This project focuses on **agent structure, API design, and deployment**, not complex business logic.

---

## 🎯 Solution Overview

This project implements a **Text Summarization AI Agent** using:

- Google Gemini (via Vertex AI)
- FastAPI (for HTTP endpoint)
- Cloud Run (for serverless deployment)

The agent accepts input text and returns a concise summary.

---

## ⚙️ Features

- ✅ AI-powered text summarization
- ✅ REST API endpoint (`/summarize`)
- ✅ Serverless deployment on Cloud Run
- ✅ Gemini model integration
- ✅ Swagger UI for testing

---

## 🏗️ Tech Stack

- Python 3.11
- FastAPI
- Google Gemini (Vertex AI)
- Docker
- Google Cloud Run

---

## 📂 Project Structure

```text
gemini-adk-summarizer-agent/
│
├── app/
│   ├── main.py        # API routes
│   ├── agent.py       # AI agent logic
│
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## 🌐 Live API

Cloud Run URL:
https://adk-agent-573620545233.asia-south1.run.app

Swagger UI:
https://adk-agent-573620545233.asia-south1.run.app/docs

---

## 🧪 API Usage

### Endpoint

POST `/summarize`

### Request

```json
{
  "text": "Artificial Intelligence is transforming industries by automating processes and improving efficiency."
}
```

### Response

```json
{
  "summary": "AI is transforming industries by automating processes and improving efficiency."
}
```

---

## 🔄 How It Works

1. User sends text input via API
2. FastAPI receives request
3. Agent processes input using Gemini model
4. Model generates summary
5. API returns response

---

## 🛠️ Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/gemini-adk-summarizer-agent.git
cd gemini-adk-summarizer-agent
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Authenticate with Google Cloud

```bash
gcloud auth application-default login
```

### 5. Run Locally

```bash
uvicorn app.main:app --reload
```

---

## ☁️ Deployment

### Build Image

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/adk-agent
```

### Deploy to Cloud Run

```bash
gcloud run deploy adk-agent \
--image gcr.io/YOUR_PROJECT_ID/adk-agent \
--region asia-south1 \
--allow-unauthenticated
```

---

## 🔐 Authentication

Uses **Google Cloud Application Default Credentials (ADC)**
No API key required.

---

## 🎯 Use Cases

- Text summarization
- Content simplification
- AI-powered backend APIs
- NLP preprocessing

---

## 📌 Notes

- Fully serverless architecture
- Uses Google Gemini via Vertex AI
- Designed for simplicity and scalability

---

## 👩‍💻 Author

Developed as part of an AI agent deployment project using Gemini and Cloud Run.

---
