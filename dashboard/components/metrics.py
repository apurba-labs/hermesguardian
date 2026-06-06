import streamlit as st


def render_metrics():

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Integrity Score",
            "95"
        )

    with col2:
        st.metric(
            "Active Incidents",
            "1"
        )

    with col3:
        st.metric(
            "Investigations",
            "1"
        )