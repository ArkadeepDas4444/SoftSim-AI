# 🤖 SoftSim AI

### An AI-Powered Virtual Development Pod with RAG-Enhanced Multi-Agent System

**SoftSim AI** is a multi-agent AI system that simulates a real-world software development team.
It automates the entire Software Development Lifecycle (SDLC) — from requirement analysis to code generation and testing — using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

---

## 🚀 Features

* **Business Analyst Agent**:
  Converts high-level requirements into structured user stories using RAG templates

* **Design Agent**:
  Generates system architecture and design documents using predefined templates

* **Developer Agent**:
  Writes clean Python code based on generated design

* **Testing Agent**:
  Creates structured test cases using RAG-based templates

* **Project Lead Agent**:
  Orchestrates the complete workflow across all agents

* **Live Progress Updates**:
  Real-time execution tracking in the UI

* **Interactive Dashboard**:
  Built using Streamlit

* **RAG-based Template Retrieval**:
  Dynamically loads structured templates for consistent outputs

---

## 🧠 System Architecture

### Workflow

```
User Requirement
        ↓
Project Lead Agent (Orchestrator)
        ↓
Business Analyst → User Stories
        ↓
Design Agent → System Design
        ↓
Developer Agent → Python Code
        ↓
Testing Agent → Test Cases
```

---

## 🧩 RAG Integration (Template-Based Retrieval)

SoftSim AI uses a lightweight Retrieval-Augmented Generation (RAG) approach.

Instead of generating outputs blindly, agents retrieve structured templates and fill them using LLMs.

### 🔍 How it Works:

* Templates are stored locally:

  * `user_story.txt`
  * `design.txt`
  * `test_case.txt`

* Templates are dynamically loaded using:

```python
load_template(template_name)
```

* Each agent uses retrieved templates to ensure:

  * Structured output
  * Consistency
  * Better controllability

#### Example:

* Business Analyst → retrieves *user story template*
* Design Agent → retrieves *architecture template*
* Testing Agent → retrieves *test case template*

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM Framework:** LangChain
* **LLM API:** Groq (LLaMA 3)
* **RAG Layer:** File-based template retrieval
* **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
SoftSim-AI/
│
├── app.py               # Streamlit UI
├── agents.py            # AI agents & orchestration
├── rag_utils.py         # Template retrieval (RAG)
├── templates/
│   ├── user_story.txt
│   ├── design.txt
│   └── test_case.txt
│
├── requirements.txt
├── .env
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/ArkadeepDas4444/SoftSim-AI.git
cd SoftSim-AI
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Add API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 💡 Example Input

```
Build a blog platform where users can create accounts,
write posts, and comment on posts.
```

---

## 📊 Output

The system generates:

* 📋 User Stories
* 🏗️ System Design
* 💻 Python Code
* 🧪 Test Cases

---

## 🔄 Agent Workflow & Orchestration

The **Project Lead Agent** manages execution flow:

1. Calls Business Analyst → generates user stories
2. Passes output to Design Agent
3. Sends design to Developer Agent
4. Sends code to Testing Agent

Each step is executed sequentially with status updates in the UI.

---

## 🧩 Code Highlights

* Multi-agent orchestration using LangChain
* Template-based RAG system for structured generation
* Modular agent design
* Real-time UI updates using Streamlit

---

## 🎯 Key Concepts Demonstrated

* Multi-Agent AI Systems
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* LLM Orchestration
* Software Development Lifecycle Automation
* Human workflow simulation using AI

---

## 🔒 Security Note

* API keys stored securely using `.env`
* `.gitignore` prevents exposure of sensitive data

---

## 🚀 Future Improvements

* Replace file-based RAG with vector database (FAISS / Chroma)
* Add code execution & validation
* Add agent memory and chat history
* Integrate GitHub for version control simulation
* Enable parallel agent execution

---

## 📜 License

This project is licensed under the **MIT License**

---

## 🙌 Acknowledgements

* Groq for LLM API
* LangChain for orchestration
* Streamlit for UI

---

## ⭐ Support

If you like this project, give it a star⭐ on GitHub!
