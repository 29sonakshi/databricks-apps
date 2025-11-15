import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Hello World App",
    page_icon="👋",
    layout="centered"
)

# Main title
st.title("Hello World! 👋")

# Additional content
st.write("Welcome to your first Databricks Streamlit app!")

# Optional: Add some interactive elements
if st.button("Click me!"):
    st.balloons()
    st.success("Hello from Databricks Streamlit!")

