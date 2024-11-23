from .client import AminoClient

class AminoPermissions(AminoClient):
    def promote_to_admin(self, group_id, user_id):
        """ترقية مستخدم إلى مشرف في المجموعة"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/promote", data)

    def demote_from_admin(self, group_id, user_id):
        """خفض رتبة مستخدم من مشرف إلى عضو عادي"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/demote", data)

    def ban_user(self, group_id, user_id):
        """حظر مستخدم من المجموعة"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/ban", data)

    def unban_user(self, group_id, user_id):
        """رفع الحظر عن مستخدم في المجموعة"""
        data = {"user_id": user_id}
        return self.send_request("POST", f"/groups/{group_id}/unban", data)