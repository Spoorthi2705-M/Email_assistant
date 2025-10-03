import re

def is_valid_email(email_str: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email_str) is not None

def is_automated_email(msg) -> bool:
    automated_headers = [
        'auto-submitted', 'x-auto-response-suppress', 
        'precedence', 'x-autoreply', 'list-unsubscribe'
    ]
    for header in automated_headers:
        if msg.get(header):
            return True

    subject = msg.get("Subject", "").lower()
    auto_patterns = [
        'out of office', 'automatic reply', 'auto-reply', 
        'vacation', 'away from office', 'ooo', 'autoreply'
    ]
    return any(pattern in subject for pattern in auto_patterns)

def check_email_filters(email_address: str, settings) -> tuple[bool, str]:
    domain = email_address.split('@')[-1] if '@' in email_address else ''

    for blocked in settings.blacklist:
        if blocked in email_address or blocked in domain:
            return False, f"Blocked by blacklist: {blocked}"

    if settings.whitelist:
        for allowed in settings.whitelist:
            if allowed in email_address or allowed in domain:
                return True, "Approved by whitelist"
        return False, "Not in whitelist"

    return True, "Passed filters"
