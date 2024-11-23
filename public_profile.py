from .client import AminoClient

class AminoPublicProfile(AminoClient):
    def get_public_profile(self, user_id):
        """الحصول على الملف الشخصي العام لمستخدم معين"""
        return self.send_request("GET", f"/users/{user_id}/public_profile")

    def update_public_profile(self, name, bio, avatar_url):
        """تحديث الملف الشخصي العام"""
        data = {"name": name, "bio": bio, "avatar_url": avatar_url}
        return self.send_request("PUT", "/users/me/public_profile", data)