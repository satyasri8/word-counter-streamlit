import streamlit as st

# App title
st.set_page_config(page_title="Word Counter App", page_icon="📝")
st.title("📝 Word Counter Application")
st.write("Count words, characters, and sentences from text or a file.")

# Option selection
option = st.radio("Choose input method:", ("Upload a text file", "Enter text manually"))

text_content = ""

# File upload option
if option == "Upload a text file":
    uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

    if uploaded_file is not None:
        try:
            text_content = uploaded_file.read().decode("utf-8")
        except Exception:
            st.error("Error reading the file. Please upload a valid text file.")

# Manual text input option
else:
    text_content = st.text_area("Enter your text here:", height=200)

# Process text
if st.button("🔍 Analyze Text"):
    if text_content.strip() == "":
        st.warning("Please provide some text to analyze.")
    else:
        words = text_content.split()
        sentences = text_content.count(".") + text_content.count("!") + text_content.count("?")
        characters = len(text_content)

        st.success("Analysis Completed ✅")
        st.write("### 📊 Results")
        st.write(f"**Total Words:** {len(words)}")
        st.write(f"**Total Characters:** {characters}")
        st.write(f"**Total Sentences:** {sentences}")
