"""Injection defense for untrusted search/fetch content."""

from __future__ import annotations

import re

ZERO_WIDTH_RE = re.compile(chr(92) + "u200b-" + chr(92) + "u200f" + chr(92) + "ufeff")
TAG_CHARS_RE = re.compile("[" + chr(0xE0000) + "-" + chr(0xE007F) + "]")
SUSPICIOUS_PATTERNS = [
    re.compile(r"ignore (all|previous|earlier) instructions", re.IGNORECASE),
    re.compile(r"system prompt", re.IGNORECASE),
    re.compile(r"disregard .* instructions", re.IGNORECASE),
    re.compile(r"new instructions", re.IGNORECASE),
    re.compile(r"base64[, :][A-Za-z0-9+/=]{40,}"),
]

def sanitize(text):
    warnings = []
    out = ZERO_WIDTH_RE.sub("", text)
    out = TAG_CHARS_RE.sub("", out)
    if out != text:
        warnings.append("stripped_invisible_characters")
    for pat in SUSPICIOUS_PATTERNS:
        if pat.search(out):
            warnings.append("pattern_match:" + pat.pattern)
    return out, warnings

def wrap(source, text):
    from datetime import datetime, timezone
    ts = datetime.now(timezone.utc).isoformat()
    return "<untrusted_content source=\"" + source + "\" retrieved_at=\"" + ts + "\">\n" + text + "\n</untrusted_content>"