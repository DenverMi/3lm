import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

import streamlit as st

from app.answer import answer_question

st.set_page_config(page_title="Compliance RAG", layout="wide")
CONVERSATION_LOG_PATH = Path("storage/conversations.jsonl")
CORRECTION_LOG_PATH = Path("storage/corrections.jsonl")
NOTE_LOG_PATH = Path("storage/notes.jsonl")

def log_conversation_event(event: dict) -> None:
    CONVERSATION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with CONVERSATION_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

def log_correction_event(event: dict) -> None:
    CORRECTION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with CORRECTION_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

def log_note_event(event: dict) -> None:
    NOTE_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with NOTE_LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")

top_left, top_right = st.columns([5, 2])

with top_right:
    program_choice = st.selectbox(
        "Program",
        ["all", "aliro", "matter", "bluetooth"],
        index=1,
        label_visibility="collapsed",
    )

    new_chat_clicked = st.button(
        "New chat",
        use_container_width=True,
    )

logo_path = Path("assets/company_logo.png")
if logo_path.exists():
    st.image(str(logo_path), width=180)

st.title("Allion L3M")
st.caption("Ask Allion Compliance AI any technical question.")

# Session state
if "conversation_id" not in st.session_state:
    st.session_state["conversation_id"] = str(uuid.uuid4())

if "conversation_title" not in st.session_state:
    st.session_state["conversation_title"] = ""

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "last_question" not in st.session_state:
    st.session_state["last_question"] = ""

if "last_items" not in st.session_state:
    st.session_state["last_items"] = []

if new_chat_clicked:
    st.session_state["conversation_id"] = str(uuid.uuid4())
    st.session_state["conversation_title"] = ""
    st.session_state["messages"] = []
    st.session_state["last_question"] = ""
    st.session_state["last_items"] = []
    st.rerun()    

# Show chat history
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
question = st.chat_input("Ask a technical question...")

if question:
    program = None if program_choice == "all" else program_choice

    if question.strip().lower().startswith("/correction:"):
        correction_text = question.strip()[len("/correction:"):].strip()

        previous_user_question = ""
        previous_assistant_answer = ""

        for message in reversed(st.session_state["messages"]):
            if message.get("role") == "assistant" and not previous_assistant_answer:
                previous_assistant_answer = message.get("content", "")
            elif message.get("role") == "user" and not previous_user_question:
                previous_user_question = message.get("content", "")

            if previous_user_question and previous_assistant_answer:
                break

        log_correction_event(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "correction_id": str(uuid.uuid4()),
                "conversation_id": st.session_state["conversation_id"],
                "conversation_title": st.session_state["conversation_title"],
                "program": program_choice,
                "correction": correction_text,
                "status": "unreviewed",
                "source": "user_command",
                "previous_user_question": previous_user_question,
                "previous_assistant_answer": previous_assistant_answer,
            }
        )

        st.session_state["messages"].append(
            {"role": "user", "content": question}
        )
        st.session_state["messages"].append(
            {
                "role": "assistant",
                "content": "Correction saved for review. It will not affect answers until approved and ingested.",
            }
        )

        st.rerun()

    if not st.session_state["conversation_title"]:
        st.session_state["conversation_title"] = question[:120]

    st.session_state["messages"].append(
        {"role": "user", "content": question}
    )
    
    log_conversation_event(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "conversation_id": st.session_state["conversation_id"],
            "conversation_title": st.session_state["conversation_title"],
            "role": "user",
            "content": question,
            "program": program_choice,
            "event_type": "message",
        }
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

    log_conversation_event(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "conversation_id": st.session_state["conversation_id"],
            "role": "assistant",
            "content": answer,
            "program": program_choice,
            "event_type": "message",
            "conversation_title": st.session_state["conversation_title"],
            "source_count": len(items),
        }
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

    log_conversation_event(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "conversation_id": st.session_state["conversation_id"],
            "role": "assistant",
            "content": answer,
            "program": program_choice,
            "event_type": "tell_me_more",
            "conversation_title": st.session_state["conversation_title"],
        }
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

    log_conversation_event(
        {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "conversation_id": st.session_state["conversation_id"],
            "role": "assistant",
            "content": answer,
            "program": program_choice,
            "event_type": "search_wider",
            "conversation_title": st.session_state["conversation_title"],
            "source_count": len(st.session_state["last_items"]),
        }
    )

    st.rerun()