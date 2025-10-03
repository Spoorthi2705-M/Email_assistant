def create_reply_draft(from_email, subject, original_body, signature, human_like=True):
    """Create either human-like or summarized draft"""
    if human_like:
        draft = f"""Hi {from_email.split('@')[0]},

Thanks for reaching out regarding "{subject}".  
I’ve read your message and will get back to you soon.

{signature}
"""
    else:
        draft = f"""Hello,

📝 Summary of your message:
{original_body[:200]}

We will respond personally within 24-48 hours.

{signature}

--- Note: Automated response"""
    return draft
