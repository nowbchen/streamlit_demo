# Streamlit 用户鉴权系统

## 项目概述

这是一个基于 Streamlit 和 `streamlit-authenticator` 的用户鉴权系统，旨在为用户提供安全的登录和退出功能。该项目通过哈希加密的方式存储用户密码，并支持 cookie 过期机制，确保用户能够安全登录并访问特定内容。

## 功能说明

1. **用户登录**：
   - 系统为用户提供了一个简单的登录表单，用户可以通过用户名和密码进行登录。
   - 支持哈希加密存储密码，保证密码的安全性。

2. **鉴权机制**：
   - 通过 `streamlit-authenticator` 实现用户的登录状态管理。
   - 使用 cookie 机制保存用户的登录状态，cookie 的过期时间为 30 天。

3. **用户权限控制**：
   - 登录成功后，可以根据用户的角色或权限，展示不同的内容（可以根据需求进一步扩展）。

4. **登出功能**：
   - 提供用户的登出按钮，支持退出后自动清除用户的 cookie。

## 文件结构

- `frontend/components/sidebar.py`：主要功能模块，处理用户登录、鉴权和登出逻辑。
- `requirements.txt`：列出了项目运行所需的依赖库。

## 安装指南

1. 克隆或下载项目代码：
   ```bash
   git clone https://your-repository-url
   cd your-project-directory
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 运行项目：
   ```bash
   streamlit run frontend/components/sidebar.py
   ```

## 使用说明

1. **登录**：
   - 打开项目后，用户将看到一个登录表单。
   - 输入预先设置的用户名和密码（例如：`user1` 和 `password1`）即可登录。

2. **错误提示**：
   - 如果用户名或密码不正确，系统会提示错误信息。
   - 如果没有输入用户名或密码，系统会发出警告。

3. **登出**：
   - 用户可以通过点击“Logout”按钮退出登录，登录状态会被清除。

## 技术细节

- **Streamlit**: 用于构建交互式 web 应用，帮助用户创建登录界面和展示内容。
- **Streamlit Authenticator**: 用于管理用户的登录状态，支持密码加密和 cookie 管理。
- **密码加密**: 在 `frontend/components/sidebar.py` 中使用 `stauth.Hasher` 对密码进行哈希加密，确保密码安全存储。

## 未来改进

- 增加用户角色和权限管理，控制不同用户可以访问的内容。
- 增强密码加密算法，进一步提高系统的安全性。
- 集成数据库以存储用户信息，而不是直接在代码中写入用户名和密码。

## 依赖项

请确保在你的环境中安装以下依赖项：

