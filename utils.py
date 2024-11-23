import json

def save_to_file(data: dict, filename: str):
    """حفظ البيانات إلى ملف"""
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_from_file(filename: str) -> dict:
    """تحميل البيانات من ملف"""
    with open(filename, 'r') as file:
        return json.load(file)

def is_valid_email(email: str) -> bool:
    """التحقق من صحة البريد الإلكتروني"""
    import re
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None