import streamlit as st
from agents import project_lead

st.set_page_config(page_title="SoftSim AI", page_icon="🤖")

st.title("🤖 SoftSim AI")
st.caption("An AI-Powered Virtual Development Pod")
st.write("Simulate a software development team using AI agents.")
st.sidebar.success("System Status: Online")
status_box = st.empty()

def update_status(message):
    status_box.info(message)

# Input requirement
requirement = st.text_area(
    "Enter Business Requirement",
    placeholder="Example: Build a simple blog platform where users can create posts and comments."
)

if st.button("Start Development 🚀"):

    if requirement.strip() == "":
        st.warning("Please enter a requirement first!")
    else:
        result = project_lead(requirement, status_callback=update_status)
        status_box.success("✅ Development completed!")
        st.divider()

        st.subheader("👲 Project Leader (to Business Analyst):")
        st.write("**Create user stories from the high-level business requirements.**")
        st.subheader("🧑‍💼 Business Analyst:")
        st.write(result["stories"])
        st.divider()

        st.subheader("👲 Project Leader (to Designer):")
        st.write("**Create the design of the software.**")
        st.subheader("🧑‍✈️ Designer:")
        st.write(result["design"])
        st.divider()

        st.subheader("👲 Project Leader (to Developer):")
        st.write("**Generate the code of the software based on the user stories and design.**")
        st.subheader("👨‍💻 Developer:")
        st.code(result["code"], language="python")
        st.divider()

        st.subheader("👲 Project Leader (to Tester):")
        st.write("**Create test cases and execute those on the code created.**")
        st.subheader("🕵️ Tester:")
        st.write(result["tests"])