from .client import AminoClient

class AminoVoiceMessage(AminoClient):
    def send_voice_message(self, chat_id, voice_file):
        """إرسال رسالة صوتية في الدردشة"""
        data = {"voice_file": voice_file}
        return self.send_request("POST", f"/chats/{chat_id}/send_voice_message", data)

    def get_voice_messages(self, chat_id):
        """الحصول على الرسائل الصوتية في الدردشة"""
        return self.send_request("GET", f"/chats/{chat_id}/voice_messages")

    def delete_voice_message(self, chat_id, message_id):
        """حذف رسالة صوتية في الدردشة"""
        return self.send_request("DELETE", f"/chats/{chat_id}/voice_messages/{message_id}")