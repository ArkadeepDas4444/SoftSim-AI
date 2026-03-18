from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from rag_utils import load_template
import os
from dotenv import load_dotenv

load_dotenv()

# Works for both local + cloud
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, max_tokens=1000)

# Business Analyst Agent
def business_analyst(requirement):

    template = load_template("user_story.txt")

    prompt = f"""
    You are a Business Analyst.

    Use the following template:

    {template}

    Fill it based on this requirement:

    {requirement}
    """

    return llm.invoke(prompt).content

# Design Agent
def design_agent(stories):

    template = load_template("design.txt")

    prompt = f"""
    You are a Software Architect.

    Use this template:

    {template}

    Based on user stories:

    {stories}
    """

    return llm.invoke(prompt).content

# Developer Agent
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

# Testing Agent
def testing_agent(code):

    template = load_template("test_case.txt")

    prompt = f"""
    You are a QA Tester.

    Use this template:

    {template}

    Generate test cases for:

    {code}
    """

    return llm.invoke(prompt).content

# Project Lead
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
        status_callback("🕵️ Tester generating test cases...")

    tests = testing_agent(code)

    return {
        "stories": stories,
        "design": design,
        "code": code,
        "tests": tests
    }