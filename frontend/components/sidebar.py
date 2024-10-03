import streamlit as st

def render_sidebar():
    """渲染侧边栏，并返回当前选择的页面"""
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a Page", ["Home", "User Profile", "Visualization"])
    return page
