# AI-Powered Customer Support & Sales Chatbot (Full-Stack)

A full-stack chatbot application designed for e-commerce stores. The system integrates a local Large Language Model (LLM) to assist customers in two modes: recommending products from an inventory database (Sales Mode) and providing answers regarding store policies and claims (Customer Service Mode) using Retrieval-Augmented Generation (RAG) concepts.

---

## 👥 Team & Contributions

This project was built as a collaborative effort. The responsibilities were divided as follows:

### 🤖 AI, RAG & Dataset Development (My Contributions)
I was responsible for the AI core, context routing logic, and database/dataset preparation:
* **Local LLM Integration:** Connected and managed a local **Qwen2.5:7b** model running via **Ollama**.
* **Intent Classification:** Implemented zero-shot prompting to classify user intents dynamically into `SALES` (product queries) or `SERVICE` (support queries).
* **Context Injection (RAG):** Designed the dynamic context retrieval mechanism. Based on the classified intent, the system dynamically queries the dataset and injects relevant context (product catalog or shop policy documents) to ensure 100% factual accuracy and prevent AI hallucinations.
* **Dataset Engineering:** Curated, cleaned, and structured the knowledge base and catalog into structured JSON formats (`service_config.json`, `category_1000_shorter.json`).
* **Prompt Optimization:** Configured system instructions and model parameters (temperature, token limits) to control the response tone and output consistency in Thai.

### 💻 Backend & Frontend Development (Teammates' Contributions)
My teammates developed the application structure and user interface:
* **Backend Development (FastAPI):** Set up the Python FastAPI server, defined Pydantic request/response schemas, and configured CORS middleware for secure integration.
* **Frontend Development (Angular 21):** Developed a single-page application using Angular 21, including a Landing Page, Product Showcase, and Interactive Chat UI styled with Tailwind CSS v4.
* **API Integration:** Implemented the Angular HttpClient service to communicate seamlessly with the FastAPI backend.

---

## 🛠️ Technology Stack

* **Frontend:** Angular 21 (TypeScript), Tailwind CSS v4, RxJS
* **Backend:** FastAPI (Python 3.8+), Uvicorn, Pydantic, Requests
* **AI Core:** Ollama (Qwen2.5:7b)

---

## 🚀 Getting Started

### 1. AI & Backend Setup
Make sure you have [Ollama](https://ollama.com/) installed and running.

1. **Pull the LLM:**
   ```bash
   ollama pull qwen2.5:7b
   ```
2. **Navigate to backend and set up Virtual Environment:**
   ```bash
   cd backend
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run FastAPI Server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The backend will start at `http://localhost:8000`.

### 2. Frontend Setup
Make sure you have [Node.js](https://nodejs.org/) installed.

1. **Navigate to frontend and install dependencies:**
   ```bash
   cd frontend
   npm install
   ```
2. **Run Angular Dev Server:**
   ```bash
   npm run start
   ```
   Open your browser and navigate to `http://localhost:4200`.
