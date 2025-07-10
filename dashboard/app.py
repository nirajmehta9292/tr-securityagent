import streamlit as st
import json
import os

st.title("🛡️ Security Agent Log Monitor")

log_path = "../logs/security_logs.jsonl"
if os.path.exists(log_path):
    with open(log_path, 'r') as f:
        logs = [json.loads(line) for line in f]

    for entry in logs[::-1][:20]:
        st.markdown(f"**Timestamp:** {entry['timestamp']}")
        st.markdown(f"**Input:** {entry['input']}")
        st.json(entry['decision'])
        st.markdown("---")
else:
    st.warning("No logs found at 'logs/security_logs.jsonl'")
