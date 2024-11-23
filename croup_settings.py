from .client import AminoClient

class AminoGroupSettings(AminoClient):
    def update_group_name(self, group_id, new_name):
        """تحديث اسم المجموعة"""
        data = {"name": new_name}
        return self.send_request("PUT", f"/groups/{group_id}/settings", data)

    def update_group_description(self, group_id, new_description):
        """تحديث وصف المجموعة"""
        data = {"description": new_description}
        return self.send_request("PUT", f"/groups/{group_id}/settings", data)

    def update_group_avatar(self, group_id, avatar_url):
        """تحديث صورة المجموعة"""
        data = {"avatar_url": avatar_url}
        return self.send_request("PUT", f"/groups/{group_id}/settings", data)

    def update_group_tags(self, group_id, tags):
        """تحديث الوسوم (Tags) الخاصة بالمجموعة"""
        data = {"tags": tags}
        return self.send_request("PUT", f"/groups/{group_id}/settings", data)

    def set_group_visibility(self, group_id, visibility):
        """تحديد مدى ظهور المجموعة (عام أو خاص)"""
        data = {"visibility": visibility}
        return self.send_request("PUT", f"/groups/{group_id}/settings", data)