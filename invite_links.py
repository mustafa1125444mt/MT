from .client import AminoClient

class AminoInviteLink(AminoClient):
    def create_invite_link(self, group_id, expire_time=86400):
        """إنشاء رابط دعوة جديد للمجموعة مع تحديد فترة انتهاء الرابط"""
        data = {"expire_time": expire_time}
        return self.send_request("POST", f"/groups/{group_id}/invite_links", data)

    def get_invite_links(self, group_id):
        """الحصول على جميع روابط الدعوة للمجموعة"""
        return self.send_request("GET", f"/groups/{group_id}/invite_links")

    def delete_invite_link(self, group_id, link_id):
        """حذف رابط دعوة معين للمجموعة"""
        return self.send_request("DELETE", f"/groups/{group_id}/invite_links/{link_id}")