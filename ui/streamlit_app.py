import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import streamlit as st

from agents.classifier import classify_query
from agents.action_planner import plan_action
from retrieval.retriever import retrieve
from agents.reasoner import generate_answer



st.set_page_config(page_title="Enterprise Assistant", layout="wide")
st.title("Enterprise AI Assistant Dashboard")


if "history" not in st.session_state:
    st.session_state.history = []

if "last_action" not in st.session_state:
    st.session_state.last_action = None


st.sidebar.title("Target Domain")
domain = st.sidebar.radio(
    "Choose Domain",
    ["IT Service Desk", "HR Operations", "Developer Support"]
)


query = st.text_input(
    "Enter your request",
    placeholder="e.g. My VPN is not working, raise a ticket"
)
submit = st.button("Submit")


if submit and query:
 
    intent = classify_query(query)

    st.session_state.history.append({
        "type": "INTENT",
        "content": intent
    })


    if intent == "action":
        action = plan_action(f"[{domain}] {query}")

        st.session_state.last_action = action
        st.session_state.history.append({
            "type": "ACTION_PLANNED",
            "content": action
        })


    else:
        docs = retrieve(query, "embeddings/faiss_index")
        answer = generate_answer(query, docs)

        st.session_state.history.append({
            "type": "ANSWER",
            "content": answer
        })


if st.session_state.last_action:
    st.subheader("🛠 Planned Action (Mock)")

    st.json(st.session_state.last_action)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Execute Action"):
            st.success("Action executed successfully (mock).")

            st.session_state.history.append({
                "type": "ACTION_EXECUTED",
                "content": st.session_state.last_action
            })

            st.session_state.last_action = None

    with col2:
        if st.button("Cancel Action"):
            st.warning("Action cancelled.")
            st.session_state.last_action = None



st.markdown("---")
st.subheader("📊 Agent Decision Trace")

for step in reversed(st.session_state.history):
    if step["type"] == "INTENT":
        st.info(f" Classified as **{step['content']}**")

    elif step["type"] == "ACTION_PLANNED":
        st.warning("🛠 Action Planned")
        st.json(step["content"])

    elif step["type"] == "ACTION_EXECUTED":
        st.success("Action Executed")
        st.json(step["content"])

    elif step["type"] == "ANSWER":
        st.write("📄 Answer")
        st.write(step["content"])

#    if submit and query:
#         action = plan_action(query)

#         if action.get("action") != "none" and "name" in action:
 #            st.subheader("🛠 Triggered Enterprise Action")
  #           st.json(action)
#         else:
#             docs = retrieve(query, "embeddings/faiss_index")
#             answer = generate_answer(query, docs)
#             st.subheader("📄 Answer (with Citations)")
#             st.write(answer)

