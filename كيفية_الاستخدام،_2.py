from MT.user import AminoUser
from MT.group import AminoGroup
from MT.chat import AminoChat
from MT.post import AminoPost
from MT.private_message import AminoPrivateMessage
from MT.permissions import AminoPermissions
from MT.event import AminoEvent

# إنشاء عميل Amino
user_client = AminoUser()

# تسجيل الدخول باستخدام البريد الإلكتروني وكلمة المرور
email = "your_email@example.com"
password = "your_password"
try:
    token = user_client.login_with_credentials(email, password)
    print(f"تم تسجيل الدخول بنجاح. التوكن: {token}")

    # التفاعل مع المنشورات
    post_client = AminoPost(user_client.base_url)
    post_response = post_client.create_post("group_id", "هذا منشور جديد!")
    print(post_response)

    # إرسال رسالة خاصة
    pm_client = AminoPrivateMessage(user_client.base_url)
    pm_response = pm_client.send_private_message("user_id", "مرحبًا، كيف حالك؟")
    print(pm_response)

    # إدارة صلاحيات المستخدمين
    permissions_client = AminoPermissions(user_client.base_url)
    promote_response = permissions_client.promote_to_admin("group_id", "user_id")
    print(promote_response)

    # إنشاء حدث
    event_client = AminoEvent(user_client.base_url)
    event_response = event_client.create_event("group_id", "حدث جديد", "تفاصيل الحدث", "2024-12-31")
    print(event_response)

except Exception as e:
    print(f"فشل تسجيل الدخول: {e}")