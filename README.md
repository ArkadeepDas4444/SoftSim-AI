# 🤖 SoftSim AI

### An AI-Powered Virtual Development Pod

SoftSim AI is a multi-agent AI system that simulates a real-world software development team.
It automates the entire software development lifecycle — from requirement analysis to code generation and testing — using Large Language Models (LLMs).

---

## 🚀 Features

* 🧑‍💼 **Business Analyst Agent**
  Converts high-level requirements into structured user stories

* 🏗️ **Design Agent**
  Generates system architecture and design documents

* 👨‍💻 **Developer Agent**
  Writes clean Python code based on design

* 🧪 **Testing Agent**
  Creates test cases for generated code

* 🧑‍✈️ **Project Lead Agent**
  Orchestrates the entire workflow and tracks progress

* 📊 **Live Progress Updates**
  Real-time status updates in the UI during execution

* 🖥️ **Interactive Dashboard**
  Built using Streamlit for easy interaction

---

## 🧠 Architecture

```
User Requirement
        ↓
Project Lead Agent
        ↓
Business Analyst → User Stories
        ↓
Design Agent → System Design
        ↓
Developer Agent → Code
        ↓
Testing Agent → Test Cases
```

---

## 🛠️ Tech Stack

* Python
* LangChain
* Groq LLM API (Llama 3)
* Streamlit
* python-dotenv

---

## 📁 Project Structure

```
SoftSim-AI/
│
├── app.py          # Streamlit UI
├── agents.py       # AI agents & workflow
├── requirements.txt
├── .env            # API keys (not included)
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

### 3. Add your API key

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

### 4. Run the application

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

* User Stories
* System Design
* Python Code
* Test Cases

---

## 🧩 Code Highlights

* Multi-agent architecture implemented using LangChain
* Central orchestration via `project_lead()` 
* Live UI updates using Streamlit status callbacks 

---

## 🎯 Key Concepts Demonstrated

* Multi-Agent AI Systems
* Prompt Engineering
* LLM Orchestration
* Software Development Lifecycle Automation
* Real-time UI feedback

---

## 🔒 Security Note

* API keys are stored in `.env` and are **not committed** to the repository
* `.gitignore` is used to exclude sensitive files

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

* Groq for free LLM API
* LangChain for agent orchestration
* Streamlit for UI framework

---

## 📌 Future Improvements

* Add RAG for template retrieval
* Implement code execution & validation
* Add agent memory and chat logs
* Integrate GitHub for version control simulation

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
