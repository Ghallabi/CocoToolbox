import streamlit as st

# from src.main_ui import MainUI


home_page = st.Page("pages/home.py", title="Home", icon="🏠")
tools_page = st.Page("pages/tools.py", title="Tools", icon="🪛")
analysis_page = st.Page("pages/analysis.py", title="Analysis", icon="🔍")


pg = st.navigation([home_page, tools_page, analysis_page])
st.set_page_config(
    page_title="COCO-ML-TOOLBOX",
    page_icon=":rocket",
)
pg.run()
