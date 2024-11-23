from .client import AminoClient

class AminoAnnouncement(AminoClient):
    def create_announcement(self, group_id, title, message):
        """إنشاء إعلان داخل المجموعة"""
        data = {
            "title": title,
            "message": message
        }
        return self.send_request("POST", f"/groups/{group_id}/announcements", data)

    def get_announcements(self, group_id):
        """الحصول على قائمة بالإعلانات داخل المجموعة"""
        return self.send_request("GET", f"/groups/{group_id}/announcements")

    def delete_announcement(self, group_id, announcement_id):
        """حذف إعلان معين داخل المجموعة"""
        return self.send_request("DELETE", f"/groups/{group_id}/announcements/{announcement_id}")