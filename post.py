from .client import AminoClient

class AminoPost(AminoClient):
    def create_post(self, group_id, content):
        """إنشاء منشور جديد في مجموعة معينة"""
        data = {"content": content}
        return self.send_request("POST", f"/groups/{group_id}/post", data)

    def get_post_info(self, post_id):
        """الحصول على معلومات منشور معين"""
        return self.send_request("GET", f"/posts/{post_id}")

    def like_post(self, post_id):
        """الإعجاب بمنشور معين"""
        return self.send_request("POST", f"/posts/{post_id}/like")

    def comment_on_post(self, post_id, comment):
        """التعليق على منشور معين"""
        data = {"content": comment}
        return self.send_request("POST", f"/posts/{post_id}/comment", data)

    def delete_post(self, post_id):
        """حذف منشور معين"""
        return self.send_request("DELETE", f"/posts/{post_id}")