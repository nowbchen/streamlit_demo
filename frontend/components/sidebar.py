import streamlit as st  
from streamlit_authenticator import StAuthenticator, UsernamePasswordHasher  
  
# 初始化一个Streamlit应用  
st.set_page_config(  
    page_title="Streamlit App with Authentication",  
    page_icon="::favicon::",  
    layout="wide",  
    initial_sidebar_state="expanded",  
)  
  
# 创建一个哈希器对象，用于存储和验证用户名和密码  
hasher = UsernamePasswordHasher()  
  
# 假设这是你的用户名和密码，实际使用中应该通过更安全的方式存储和验证  
USERNAME = "admin"  
PASSWORD = hasher.hash_password("my_secure_password")  
  
# 创建认证器对象  
authenticator = StAuthenticator(hasher)  
  
# 检查用户是否已登录  
if not authenticator.is_user_authenticated():  
    # 如果用户未登录，则显示登录表单  
    authenticator.login(USERNAME, PASSWORD)  
  
# 如果用户已登录，则显示应用程序内容  
else:  
    # 在这里编写你的应用程序逻辑  
    st.title("Welcome to the Secure Streamlit App!")  
    st.write("You are now authenticated and can access the app.")  
      
    # 示例：显示一些数据或进行其他操作  
    st.write("Here is some data:")  
    data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}  
    st.table(data)  
  
    # 提供一个注销按钮  
    if st.button("Logout"):  
        authenticator.logout()  
        st.stop()  
  
# 运行Streamlit应用  
if __name__ == "__main__":  
    st.run_script("app.py")