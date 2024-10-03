import streamlit_authenticator as stauth

# 用户数据
usernames = ['user1', 'user2']
passwords = ['password1', 'password2']
names = ['User One', 'User Two']

# 生成哈希加密的密码
hashed_passwords = stauth.Hasher(passwords).hash()

# 创建用户鉴权对象
authenticator = stauth.Authenticate(
    names=names,
    usernames=usernames,
    passwords=hashed_passwords,
    cookie_name='cookie_name',
    key='signature_key',
    cookie_expiry_days=30  # 指定 cookie 过期时间
)

