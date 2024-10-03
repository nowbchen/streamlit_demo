import streamlit as st
import streamlit_authenticator as stauth

# 定义用户和密码
usernames = ['user1', 'user2']
passwords = ['password1', 'password2']
names = ['User One', 'User Two']

# 创建一个用户鉴权对象
authenticator = stauth.Authenticate(names, usernames, passwords, 'cookie_name', 'signature_key', cookie_expiry_days=30)

# 创建用户登录表单
name, authentication_status = authenticator.login('Login', 'main')

if authentication_status:
    st.success(f'Welcome {name}!')
    # 这里可以放置用户登陆后的内容
    # ...

elif authentication_status is False:
    st.error('Username/password is incorrect')

# 允许用户登出
authenticator.logout('Logout', 'main')
