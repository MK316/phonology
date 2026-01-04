import streamlit as st

st.write("Google sheet")


import streamlit as st

st.set_page_config(page_title="3 Tabs Example", layout="wide")

st.title("📌 Study Group Page")

tab1, tab2, tab3 = st.tabs(["🟦 Google Sheet", "🟩 TBA", "🟥 TBA"])

with tab1:
    st.markdown("### 📄 Shared Google Sheets for your study activities")

    st.link_button(
        label="📊 Open Google Sheet",
        url="https://docs.google.com/spreadsheets/d/11i6x_e7TDOpIdWqkmUzVnBKuHWkrjR24m_drYaRN7XI/edit?usp=sharing",
    )


with tab2:
    st.header("Tab 2")
    st.write("To be announced")
    st.slider("Tab 2 slider", 0, 100, 50, key="t2_slider")

with tab3:
    st.header("Tab 3")
    st.write("TBA")
    if st.button("Tab 3 button", key="t3_btn"):
        st.success("버튼을 눌렀습니다!")
