import streamlit as st
from pathlib import Path
from app.answer import answer_question

st.set_page_config(page_title="Compliance RAG", layout="wide")

logo_path = Path("assets/company_logo.png")
if logo_path.exists():
    st.image(str(logo_path), width=180)

st.title("Compliance 3LM")
st.caption("Ask Allion experts any technical question.")

if "last_question" not in st.session_state:
    st.session_state["last_question"] = ""
if "last_items" not in st.session_state:
    st.session_state["last_items"] = []
if "last_answer" not in st.session_state:
    st.session_state["last_answer"] = ""

question = st.text_area(
    "Question",
    height=120,
    placeholder="e.g. Does changing antenna require requalification?",
)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    ask_clicked = st.button("Ask", type="primary", use_container_width=True)

with col2:
    more_clicked = st.button(
        "Tell me more",
        use_container_width=True,
        disabled=not st.session_state["last_items"],
    )

with col3:
    wider_clicked = st.button(
        "Search wider",
        use_container_width=True,
        disabled=not st.session_state["last_question"],
    )

if ask_clicked:
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        with st.spinner("Thinking..."):
            result = answer_question(
                question,
                detail_mode="normal",
            )

        if isinstance(result, dict):
            st.session_state["last_question"] = question
            st.session_state["last_items"] = result.get("items", [])
            st.session_state["last_answer"] = result.get("answer", "")
            st.rerun()
        else:
            st.session_state["last_question"] = question
            st.session_state["last_items"] = []
            st.session_state["last_answer"] = str(result)
            st.rerun()

if more_clicked:
    if not st.session_state["last_question"] or not st.session_state["last_items"]:
        st.warning("Ask something first.")
    else:
        with st.spinner("Going deeper..."):
            result = answer_question(
                st.session_state["last_question"],
                detail_mode="deep",
                preloaded_items=st.session_state["last_items"],
            )

        if isinstance(result, dict):
            st.session_state["last_answer"] = result.get("answer", "")
        else:
            st.session_state["last_answer"] = str(result)

        st.rerun()

if wider_clicked:
    if not st.session_state["last_question"]:
        st.warning("Ask something first.")
    else:
        with st.spinner("Searching wider..."):
            result = answer_question(
                st.session_state["last_question"],
                detail_mode="wide",
                preloaded_items=None,
            )

        if isinstance(result, dict):
            st.session_state["last_items"] = result.get("items", [])
            st.session_state["last_answer"] = result.get("answer", "")
        else:
            st.session_state["last_items"] = []
            st.session_state["last_answer"] = str(result)

        st.rerun()

if st.session_state["last_answer"]:
    st.subheader("Answer")
    st.write(st.session_state["last_answer"])