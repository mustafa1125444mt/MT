from MT.user import AminoUser
from MT.group import AminoGroup
from MT.chat import AminoChat

# إنشاء عميل Amino
user_client = AminoUser()

# تسجيل الدخول باستخدام البريد الإلكتروني وكلمة المرور
email = "mustafafaleh8787@gmail.com"
password = "MT12345678"
try:
    token = user_client.login_with_credentials(email, password)
    print(f"تم تسجيل الدخول بنجاح. التوكن: {token}")
    
    # الآن يمكنك التفاعل مع API باستخدام التوكن
    # التفاعل مع المجموعات
    group_client = AminoGroup(user_client.base_url)
    group_info = group_client.search_groups("Gaming")
    print(group_info)

    # إرسال رسالة في الدردشة
    chat_client = AminoChat(user_client.base_url)
    chat_response = chat_client.send_message("chat_id", "مرحبًا")
    print(chat_response)

except Exception as e:
    print(f"فشل تسجيل الدخول: {e}")