import streamlit as st

st.markdown("#### 1. TCE Exam Searching Engine")
st.write("https://apps4u.streamlit.app")

st.markdown(
    """
<style>
.link-block {
    margin-bottom: 14px;
}

.link-button {
    display: inline-block;
    padding: 12px 22px;
    margin: 6px 0;
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

/* Description text */
.link-desc {
    margin-left: 6px;
    font-size: 14px;
    color: #555555;
}
</style>

<div class="link-block">
    <a class="link-button btn-blue"
       href="https://apps4u.streamlit.app/Search:_Phonology_&_Morphology"
       target="_blank">
       📘 TCE Search (Phonetics & Phonology)
    </a>
    <div class="link-desc">
        Search past TCE questions related to phonetics, phonology, and morphology (updated from 2005~2026).
    </div>
</div>

<div class="link-block">
    <a class="link-button btn-green"
       href="https://apps4u.streamlit.app/Search:_Syntax_&_Semantics"
       target="_blank">
       📗 TCE Search (Syntax & Semantics)
    </a>
    <div class="link-desc">
        Explore TCE questions focusing on English grammar, syntax, semantics, and pragmatics (since 2026.12.30).
    </div>
</div>

""",
    unsafe_allow_html=True
)
