# 📧 Email Auto-Responder Pro

An AI-powered email management system with **human-like draft replies**, **AI summarization**, and **manual approval** using **Python**, **Streamlit**, and **Hugging Face Transformers**.

---




## Features

- ✅ Fetch unread emails from Gmail securely  
- 🤖 Summarize emails using AI (Transformers)  
- ✉️ Generate human-like draft replies automatically  
- 🛡️ Whitelist / Blacklist email filtering  
- 📝 Manual approval before sending replies  
- 📊 View sent email history and logs  
- ⚡ Streamlit-based interactive dashboard  

---
## Configuration

### 1. Enable IMAP in Gmail
1. Open Gmail → Settings (⚙️) → See all settings  
2. Go to **Forwarding and POP/IMAP** tab  
3. Enable **IMAP**  
4. Click **Save Changes**

### 2. Create a Gmail App Password
> Google no longer allows “less secure apps” to access Gmail directly. You need an **App Password**.

1. Go to your Google Account → Security  
2. Under **Signing in to Google**, select **App passwords**  
3. Select **Mail** as the app, and **Other (Custom name)** as device (e.g., `EmailBot`)  
4. Click **Generate** → Copy the 16-character password  
5. Use this password in the Streamlit app **instead of your normal Gmail password**

### 3. Enter Credentials in Streamlit
- Open the Streamlit app → Sidebar → Enter:  
  - Your Gmail address  
  - The **App Password** you just generated  

**⚠️ Your credentials are never stored permanently.**




## Installation

1. Clone the repository:
```bash
git clone https://github.com/ankitha-km/email_bot.git
cd email_b

python -m venv venv
venv\Scripts\activate 


pip install -r requirements.txt








