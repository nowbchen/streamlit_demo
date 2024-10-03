import streamlit as st
import streamlit_authenticator as stauth

# 用户数据
usernames = ['user1', 'user2']
passwords = stauth.Hasher(['password1', 'password2']).generate()  # 只生成一次哈希
names = ['User One', 'User Two']

# 创建用户鉴权对象，明确传递参数名称
authenticator = stauth.Authenticate(
    names=names,
    usernames=usernames,
    passwords=passwords,
    cookie_name='cookie_name',
    key='signature_key',
    cookie_expiry_days=30  # 传递 cookie_expiry_days
)

# 创建用户登录表单
name, authentication_status = authenticator.login('Login', 'main')

if authentication_status:
    st.success(f'Welcome {name}!')
    # 登录后展示内容
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')

# 用户登出
authenticator.logout('Logout', 'main')
