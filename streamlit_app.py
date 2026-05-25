import streamlit as st
from pathlib import Path
from app.answer import answer_question

st.set_page_config(page_title="Compliance RAG", layout="wide")

top_left, top_right = st.columns([6, 1])

with top_right:
    program_choice = st.selectbox(
        "Program",
        ["all", "aliro", "matter", "bluetooth"],
        index=1,
        label_visibility="collapsed",
    )

logo_path = Path("assets/company_logo.png")
if logo_path.exists():
    st.image(str(logo_path), width=180)

st.title("Allion L3M")
st.caption("Ask Allion Compliance AI any technical question.")

# Session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "last_question" not in st.session_state:
    st.session_state["last_question"] = ""

if "last_items" not in st.session_state:
    st.session_state["last_items"] = []

# Show chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
question = st.chat_input("Ask a technical question...")

if question:
    program = None if program_choice == "all" else program_choice

    st.session_state["messages"].append(
        {"role": "user", "content": question}
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = answer_question(
                question,
                detail_mode="normal",
                program=program,
                chat_history=st.session_state["messages"][-6:],
            )

        if isinstance(result, dict):
            answer = result.get("answer", "")
            items = result.get("items", [])
        else:
            answer = str(result)
            items = []

        st.write(answer)

    st.session_state["messages"].append(
        {"role": "assistant", "content": answer}
    )

    st.session_state["last_question"] = question
    st.session_state["last_items"] = items

# Follow-up buttons
col1, col2 = st.columns([1, 1])

with col1:
    more_clicked = st.button(
        "Tell me more",
        use_container_width=True,
        disabled=not st.session_state["last_items"],
    )

with col2:
    wider_clicked = st.button(
        "Search wider",
        use_container_width=True,
        disabled=not st.session_state["last_question"],
    )

if more_clicked:
    with st.spinner("Going deeper..."):
        result = answer_question(
            st.session_state["last_question"],
            detail_mode="deep",
            preloaded_items=st.session_state["last_items"],
        )

    if isinstance(result, dict):
        answer = result.get("answer", "")
    else:
        answer = str(result)

    st.session_state["messages"].append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()

if wider_clicked:
    with st.spinner("Searching wider..."):
        result = answer_question(
            st.session_state["last_question"],
            detail_mode="wide",
            preloaded_items=None,
        )

    if isinstance(result, dict):
        answer = result.get("answer", "")
        st.session_state["last_items"] = result.get("items", [])
    else:
        answer = str(result)
        st.session_state["last_items"] = []

    st.session_state["messages"].append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()