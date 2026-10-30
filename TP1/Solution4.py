# Part B - a safe converter
def safe_int(text):
    """Turn text into an int: return None when it is not a number"""
    text = text.strip()
    if text.lstrip("-").isdigit():
        return int(text)
    

















