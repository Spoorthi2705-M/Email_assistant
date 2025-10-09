# 📧 Email Auto-Responder Pro

An AI-powered email management system with **human-like draft replies**, **AI summarization**, and **manual approval** using **Python**, **Streamlit**, and **Hugging Face Transformers**.

---




## Features

Securely fetch unread emails via IMAP

Summarize long email content using Hugging Face transformer models

Draft human-like replies (customizable or auto-generated)

Auto-reply with summary included

Whitelist / blacklist filtering to avoid spam or loops

Manual approval before sending replies (optionally)

View reply history, logs, and status

Streamlit-based dashboard for ease of use
------


| File / Directory     | Purpose                                                   |
| -------------------- | --------------------------------------------------------- |
| `app.py`             | Main Streamlit application entry point                    |
| `config.py`          | Configuration settings (constants, email settings)        |
| `summarizer.py`      | Wrappers and utilities for text summarization             |
| `email_utils.py`     | Functions to fetch, parse, validate, reply to emails      |
| `filters.py`         | Functions for whitelist / blacklist / loop detection etc. |
| `draft_generator.py` | Logic for creating draft reply templates                  |
| `requirements.txt`   | Python dependencies                                       |
| `README.md`          | This README file                                          |


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
2. 
```bash
https://github.com/ankitha-km/email_assistant.git
cd email_assistant
```


2.Create a virtual environment & activate it
```bash
python3 -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate           # Windows
```       


3.Install dependencies
```bash
pip install -r requirements.txt
```


4.Run the Streamlit app
```bash
streamlit run app.py
```


## **How It Works (High-Level Flow)**

The user logs in via the Streamlit interface using email + app password.
The system connects to Gmail via IMAP and fetches unread messages.
It checks for automated or spam emails to avoid reply loops.
The email body is extracted (text or HTML converted to text).
A transformer-based summarization model generates a concise summary.
A draft reply is composed, embedding the summary.
The system sends the reply using SMTP and marks the email as “Seen.”
The dashboard shows which emails were processed, with details and success status.


 ## **Usage Tips & Configuration**

Use Streamlit’s sidebar to set check interval (seconds) and max emails per check
Turn on auto-check for periodic inbox scans
Consider adding your own blacklist / whitelist rules in filters.py
If encountering errors with large emails, increase summary truncation or fallback to manual reading















