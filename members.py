from .client import AminoClient

class AminoMember(AminoClient):
    def add_member(self, group_id, user_id):
        """إضافة عضو جديد إلى المجموعة"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/add_member", data)

    def remove_member(self, group_id, user_id):
        """إزالة عضو من المجموعة"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/remove_member", data)

    def get_member_info(self, group_id, user_id):
        """الحصول على معلومات عضو في المجموعة"""
        return self.send_request("GET", f"/groups/{group_id}/members/{user_id}")

    def check_membership_status(self, group_id, user_id):
        """التحقق من حالة العضوية في مجموعة معينة"""
        return self.send_request("GET", f"/groups/{group_id}/members/{user_id}/status")