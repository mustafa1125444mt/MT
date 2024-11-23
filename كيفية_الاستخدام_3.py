from MT.user import AminoUser
from MT.group import AminoGroup
from MT.chat import AminoChat
from MT.member import AminoMember
from MT.poll import AminoPoll
from MT.announcement import AminoAnnouncement
from MT.voice_message import AminoVoiceMessage
from MT.public_profile import AminoPublicProfile

# إنشاء عميل Amino
user_client = AminoUser()

# تسجيل الدخول باستخدام البريد الإلكتروني وكلمة المرور
email = "your_email@example.com"
password = "your_password"
try:
    token = user_client.login_with_credentials(email, password)
    print(f"تم تسجيل الدخول بنجاح. التوكن: {token}")

    # إدارة الأعضاء
    member_client = AminoMember(user_client.base_url)
    add_member_response = member_client.add_member("group_id", "user_id")
    print(add_member_response)

    # إنشاء استطلاع
    poll_client = AminoPoll(user_client.base_url)
    create_poll_response = poll_client.create_poll("group_id", "ما رأيك في هذا؟", ["خيارات1", "خيارات2"])
    print(create_poll_response)

    # إنشاء إعلان
    announcement_client = AminoAnnouncement(user_client.base_url)
    create_announcement_response = announcement_client.create_announcement("group_id", "إعلان مهم", "تفاصيل الإعلان")
    print(create_announcement_response)

    # إرسال رسالة صوتية
    voice_message_client = AminoVoiceMessage(user_client.base_url)
    voice_response = voice_message_client.send_voice_message("chat_id", "path_to_voice_file")
    print(voice_response)

    # عرض الملف الشخصي العام
    public_profile_client = AminoPublicProfile(user_client.base_url)
    profile_response = public_profile_client.get_public_profile("user_id")
    print(profile_response)

except Exception as e:
    print(f"فشل تسجيل الدخول: {e}")