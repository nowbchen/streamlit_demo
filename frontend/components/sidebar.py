import streamlit as st
import streamlit_authenticator as stauth

# 用户数据
usernames = ['user1', 'user2']
passwords = stauth.Hasher(['password1', 'password2']).generate()  # 生成哈希加密的密码
names = ['User One', 'User Two']

# 创建用户鉴权对象，明确参数名称避免冲突
authenticator = stauth.Authenticate(
    names=names,
    usernames=usernames,
    passwords=passwords,
    cookie_name='cookie_name',
    key='signature_key',
    cookie_expiry_days=30  # 指定 cookie 过期时间
)

# 创建用户登录表单
name, authentication_status = authenticator.login('Login', 'main')

if authentication_status:
    st.success(f'Welcome {name}!')
    # 用户登录成功后展示的内容

elif authentication_status is False:
    st.error('Username/password is incorrect')

elif authentication_status is None:
    st.warning('Please enter your username and password')

# 允许用户登出
authenticator.logout('Logout', 'main')
