import streamlit as st

st.markdown(
    """
<style>
.link-button {
    display: inline-block;
    padding: 12px 20px;
    margin: 6px 10px 6px 0;
    font-size: 16px;
    font-weight: 600;
    color: white;
    text-decoration: none;
    border-radius: 8px;
}
.btn-blue { background-color: #1f77b4; }
.btn-green { background-color: #2ca02c; }
.btn-orange { background-color: #ff7f0e; }

.link-button:hover {
    opacity: 0.85;
}
</style>

<a class="link-button btn-blue" href="https://apps4u.streamlit.app/Search:_Phonology_&_Morphology" target="_blank">
📘 TCE Search (Phonetics & Phonology)
</a>

<a class="link-button btn-green" href="https://apps4u.streamlit.app/Search:_Syntax_&_Semantics" target="_blank">
📗 TCE Search (Syntax & Semantics)
</a>

""",
    unsafe_allow_html=True
)
