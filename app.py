import streamlit as st
from config import default_settings
from email_utils import fetch_unread_emails, send_email_with_draft, mark_email_as_read
from summarizer import load_summarizer
from draft_generator import create_reply_draft
from filters import is_valid_email, check_email_filters, is_automated_email
from datetime import datetime
import time

st.set_page_config(page_title="Email Auto-Responder Pro", page_icon="📧", layout="wide")

# Session State
if 'pending_emails' not in st.session_state: st.session_state.pending_emails = []
if 'sent_emails' not in st.session_state: st.session_state.sent_emails = []
if 'settings' not in st.session_state: st.session_state.settings = default_settings
if 'email_stats' not in st.session_state: st.session_state.email_stats = {'processed':0,'sent':0,'failed':0,'skipped':0}

st.title("📧 Email Auto-Responder Pro (Human-like Replies)")

# Sidebar for credentials & settings
with st.sidebar:
    st.header("⚙️ Configuration")
    email_user = st.text_input("Gmail Address")
    email_pass = st.text_input("App Password", type="password")
    st.session_state.settings.max_summary_length = st.slider("Summary Length",50,200,130)
    st.session_state.settings.custom_signature = st.text_area("Email Signature",value=st.session_state.settings.custom_signature,height=100)

# Tabs
tab1, tab2, tab3 = st.tabs(["📥 Fetch Emails","✉️ Pending Drafts","📤 Sent Emails"])

with tab1:
    if st.button("🔍 Check for New Emails"):
        summarizer = load_summarizer()
        new_emails = fetch_unread_emails(email_user,email_pass,summarizer,st.session_state.settings)
        st.session_state.pending_emails.extend(new_emails)
        st.success(f"Fetched {len(new_emails)} new emails")

with tab2:
    if not st.session_state.pending_emails:
        st.info("No pending emails")
    else:
        for idx, email_data in enumerate(st.session_state.pending_emails):
            msg = email_data['msg']
            from_email = email.utils.parseaddr(msg["From"])[1]
            subject = msg.get("Subject","No Subject")
            body = msg.get_payload(decode=True).decode(errors="ignore") if not msg.is_multipart() else "[Multipart email]"
            draft = create_reply_draft(from_email,subject,body,st.session_state.settings.custom_signature,human_like=True)
            with st.expander(f"From: {from_email} | Subject: {subject}",expanded=True):
                st.text_area("Email Body", value=body[:500]+"..." if len(body)>500 else body,height=150,disabled=True)
                edited_draft = st.text_area("Draft Reply",value=draft,height=200,key=f"draft_{idx}")
                col1,col2 = st.columns(2)
                with col1:
                    if st.button("✅ Send",key=f"send_{idx}"):
                        success,msg = send_email_with_draft(email_user,email_pass,from_email,subject,edited_draft)
                        if success: mark_email_as_read(email_user,email_pass,email_data['id'])
                        st.session_state.sent_emails.append({'to':from_email,'subject':subject,'body':edited_draft,'status':'success'})
                        st.success("Email sent")
                        st.session_state.pending_emails.pop(idx)
                        st.experimental_rerun()
                with col2:
                    if st.button("🗑️ Skip",key=f"skip_{idx}"):
                        mark_email_as_read(email_user,email_pass,email_data['id'])
                        st.session_state.pending_emails.pop(idx)
                        st.info("Skipped")
                        st.experimental_rerun()

with tab3:
    if not st.session_state.sent_emails:
        st.info("No emails sent yet")
    else:
        for email_sent in reversed(st.session_state.sent_emails):
            with st.expander(f"To: {email_sent['to']} | Status: {email_sent['status']}"):
                st.text_area("Message",value=email_sent['body'],height=200,disabled=True)
