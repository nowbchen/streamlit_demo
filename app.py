import streamlit as st
from frontend.components.sidebar import render_sidebar
from frontend.components.user import authenticator

# 创建用户登录表单
name, authentication_status = authenticator.login('Login', 'main')

# 检查登录状态并处理相应的响应
if authentication_status is True:
    st.success(f'Welcome {name}!')
    # 渲染侧边栏并获取当前选择的页面
    page = render_sidebar()

    # 根据选择的页面显示内容
    if page == "Home":
        st.title("Welcome to the Home Page")
        st.write("This is the main content of the home page.")
    elif page == "User Profile":
        st.title(f"{name}'s Profile")
        st.write(f"This is the profile page for {name}.")
    elif page == "Visualization":
        from backend.visualization import show_visualization
        st.title("Data Visualization")
        show_visualization()

    # 允许用户登出
    authenticator.logout('Logout', 'sidebar')

elif authentication_status is False:
    st.error('Username/password is incorrect')
else:
    st.warning('Please enter your username and password')