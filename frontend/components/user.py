import streamlit as st
import streamlit_authenticator as stauth
import yaml
 
# 从config.yaml加载用户数据
with open('config/config.yaml') as file:
    config = yaml.safe_load(file)
 
credentials = {
    'usernames': {
        config['usernames'][0]: {'name': config['names'][0], 'password': config['passwords'][0]},
        config['usernames'][1]: {'name': config['names'][1], 'password': config['passwords'][1]}
    }
}
 
authenticator = stauth.Authenticate(credentials, 'cookie_name', 'random_key', 30)
 
name, authentication_status, username = authenticator.login('Login', 'main')
 
if authentication_status:
    st.write(f'Welcome *{name}*')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')