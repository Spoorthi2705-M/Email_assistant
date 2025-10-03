from dataclasses import dataclass
from typing import List

@dataclass
class AppSettings:
    whitelist: List[str]
    blacklist: List[str]
    max_summary_length: int
    auto_approve: bool
    custom_signature: str

# Default settings
default_settings = AppSettings(
    whitelist=[],
    blacklist=[],
    max_summary_length=130,
    auto_approve=False,
    custom_signature="Best regards,\nAuto-Responder Team"
)
