import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 Welcome to My Streamlit App")

# Sidebar
st.sidebar.header("Navigation")

name = st.sidebar.text_input("Enter your name")

# Main content
st.header("Hello!")

if name:
    st.success(f"Welcome, {name}!")
else:
    st.info("Please enter your name in the sidebar.")

st.write("---")

# Age
age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    value=18
)

# Checkbox
agree = st.checkbox("I agree")

if agree:
    st.write(f"You are {age} years old.")

# File upload
st.subheader("📁 Upload a File")

uploaded_file = st.file_uploader(
    "Choose a file",
    type=["csv", "txt", "pdf", "jpg", "png"]
)

if uploaded_file:
    st.success("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)

# Button
if st.button("Click Me"):
    st.success("Thank You 🎉")