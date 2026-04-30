import streamlit as st
from app.answer import answer_question

# Change this import to match your project

st.set_page_config(page_title="Bluetooth RAG", layout="wide")
st.title("Compliance RAG")
st.caption("Ask a Bluetooth qualification or technical question.")

question = st.text_area("Question", height=120, placeholder="e.g. Does changing antenna require requalification?")

if st.button("Ask", type="primary"):
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        with st.spinner("Thinking..."):
            result = answer_question(question)

        # Flexible handling in case your function returns string or dict
        if isinstance(result, dict):
            answer = result.get("answer", "")
            citations = result.get("citations", "")
        else:
            answer = str(result)
            citations = ""

        st.subheader("Answer")
        st.write(answer)

        if citations:
            st.subheader("Citations")
            st.code(citations)