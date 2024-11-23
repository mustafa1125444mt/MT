from .client import AminoClient

class AminoPrivateMessage(AminoClient):
    def send_private_message(self, user_id, message):
        """إرسال رسالة خاصة إلى مستخدم معين"""
        data = {"message": message}
        return self.send_request("POST", f"/users/{user_id}/messages", data)

    def get_private_messages(self, user_id):
        """الحصول على الرسائل الخاصة من مستخدم معين"""
        return self.send_request("GET", f"/users/{user_id}/messages")

    def delete_private_message(self, user_id, message_id):
        """حذف رسالة خاصة معينة"""
        return self.send_request("DELETE", f"/users/{user_id}/messages/{message_id}")