# app.py
import streamlit as st
from rag_pipeline import search_query
from utils import normalize_query

st.set_page_config(page_title="IPL Result AI", layout="centered")
st.title("🏏 IPL Result AI")
st.markdown("Ask a question about IPL matches (e.g. 'Who won the match between CSK and MI in 2019?'):")

query = st.text_input("Enter your question")

if query:
    result = search_query(query)

    st.markdown("### 📌 Match Details")
    st.markdown(f"""
    **Match ID:** {result.get('Match ID', 'N/A')}  
    **Teams:** {result.get('Teams', 'N/A')}  
    **Winner:** {result.get('Winner', 'N/A')}  
    **Player of Match:** {result.get('Player of Match', 'N/A')}  
    **Venue:** {result.get('Venue', 'N/A')}  
    **City:** {result.get('City', 'N/A')}  
    **Season:** {result.get('Season', 'N/A')}
    """)
else:
    st.error("No match found.")
