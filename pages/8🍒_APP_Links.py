import streamlit as st

st.markdown("#### 1. TCE Exam Searching Engine")
st.write("https://apps4u.streamlit.app")

st.markdown(
    """
<style>
.link-button {
    display: inline-block;
    padding: 12px 22px;
    margin: 6px 10px 6px 0;
    font-size: 16px;
    font-weight: 600;
    text-decoration: none;
    border-radius: 8px;
    transition: background-color 0.2s ease;
}

/* Force white text in all states */
.link-button,
.link-button:visited,
.link-button:active {
    color: white !important;
}

/* Button colors */
.btn-blue { background-color: #1f77b4; }
.btn-green { background-color: #2ca02c; }
.btn-orange { background-color: #ff7f0e; }

/* Hover: yellow background, black text */
.link-button:hover {
    background-color: #FFD700;
    color: black !important;
}
</style>



<a class="link-button btn-blue" href="https://apps4u.streamlit.app/Search:_Phonology_&_Morphology" target="_blank">
📘 TCE Search (Phonetics & Phonology)
</a><br>

<a class="link-button btn-green" href="https://apps4u.streamlit.app/Search:_Syntax_&_Semantics" target="_blank">
📗 TCE Search (Syntax & Semantics)
</a>

""",
    unsafe_allow_html=True
)
