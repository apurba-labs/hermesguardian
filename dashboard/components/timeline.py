import streamlit as st


def render_timeline(events):

    st.subheader("Investigation Timeline")

    for event in events:

        st.markdown(
            f"""
**{event['time']}**

🟢 {event['agent']}

{event['action']}
---
"""
        )