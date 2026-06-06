import streamlit as st


def render_incident(incident):

    st.subheader("Integrity Incident")

    st.error(
        f"""
Incident ID: {incident['incident_id']}

Title: {incident['title']}

Status: {incident['status']}
"""
    )