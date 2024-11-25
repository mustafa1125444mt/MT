from .client import AminoClient

class AminoBan(AminoClient):
    def ban_user(self, group_id, user_id, reason=""):
        """حظر مستخدم من المجموعة مع تحديد سبب الحظر"""
        data = {"user_id": user_id, "reason": reason}
        return self.send_request("POST", f"/groups/{group_id}/ban", data)

    def unban_user(self, group_id, user_id):
        """رفع الحظر عن مستخدم معين"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/unban", data)

    def check_user_ban_status(self, group_id, user_id):
        """التحقق من حالة الحظر لمستخدم معين داخل المجموعة"""
        return self.send_request("GET", f"/groups/{group_id}/bans/{user_id}")