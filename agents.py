from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, max_tokens=2000)

# -----------------------------
# Business Analyst Agent
# -----------------------------
ba_prompt = ChatPromptTemplate.from_template("""
You are a Business Analyst.

Convert the requirement into user stories.

Requirement:
{requirement}

Format:
User Story
Acceptance Criteria
Priority
""")

def business_analyst(requirement):
    chain = ba_prompt | llm
    return chain.invoke({"requirement": requirement}).content


# -----------------------------
# Design Agent
# -----------------------------
design_prompt = ChatPromptTemplate.from_template("""
You are a software architect.

Create a system design from the following user stories.

User Stories:
{stories}

Output:
Architecture
Components
Database Schema
""")

def design_agent(stories):
    chain = design_prompt | llm
    return chain.invoke({"stories": stories}).content


# -----------------------------
# Developer Agent
# -----------------------------
dev_prompt = ChatPromptTemplate.from_template("""
You are a senior Python developer.

Write clean, working Python code based on this design.

Design:
{design}

Return ONLY the Python code without explanation.
""")

def developer_agent(design):
    chain = dev_prompt | llm
    return chain.invoke({"design": design}).content


# -----------------------------
# Testing Agent
# -----------------------------
test_prompt = ChatPromptTemplate.from_template("""
You are a QA tester.

Generate test cases for the following code.

Code:
{code}

Format:
Test Case
Input
Expected Output
""")

def testing_agent(code):
    chain = test_prompt | llm
    return chain.invoke({"code": code}).content


# -----------------------------
# Project Lead
# -----------------------------
def project_lead(requirement, status_callback=None):

    if status_callback:
        status_callback("🧑‍💼 Business Analyst generating user stories...")

    stories = business_analyst(requirement)

    if status_callback:
        status_callback("🧑‍✈️ Architect designing system...")

    design = design_agent(stories)

    if status_callback:
        status_callback("👨‍💻 Developer writing code...")

    code = developer_agent(design)

    if status_callback:
        status_callback("🧪 Tester generating test cases...")

    tests = testing_agent(code)

    if status_callback:
        status_callback("✅ Development completed!")

    return {
        "stories": stories,
        "design": design,
        "code": code,
        "tests": tests
    }