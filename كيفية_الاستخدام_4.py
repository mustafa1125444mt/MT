from MT.user import AminoUser
from MT.group import AminoGroup
from MT.category import AminoCategory
from MT.ban import AminoBan
from MT.invite_link import AminoInviteLink
from MT.media import AminoMedia
from MT.interactive_event import AminoInteractiveEvent

# إنشاء عميل Amino
user_client = AminoUser()

# تسجيل الدخول باستخدام البريد الإلكتروني وكلمة المرور
email = "your_email@example.com"
password = "your_password"
try:
    token = user_client.login_with_credentials(email, password)
    print(f"تم تسجيل الدخول بنجاح. التوكن: {token}")

    # إضافة عضو إلى فئة
    category_client = AminoCategory(user_client.base_url)
    add_member_response = category_client.add_member_to_category("group_id", "category_id", "user_id")
    print(add_member_response)

    # إنشاء رابط دعوة
    invite_link_client = AminoInviteLink(user_client.base_url)
    invite_response = invite_link_client.create_invite_link("group_id")
    print(invite_response)

    # تحميل صورة
    media_client = AminoMedia(user_client.base_url)
    upload_image_response = media_client.upload_image("path_to_image.jpg")
    print(upload_image_response)

    # بدء حدث تفاعلي
    event_client = AminoInteractiveEvent(user_client.base_url)
    create_event_response = event_client.start_interactive_event("group_id", "حدث جديد", "وصف الحدث")
    print(create_event_response)

except Exception as e