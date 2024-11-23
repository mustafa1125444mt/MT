from .client import AminoClient

class AminoComment(AminoClient):
    def get_comments(self, post_id):
        """الحصول على تعليقات منشور معين"""
        return self.send_request("GET", f"/posts/{post_id}/comments")

    def delete_comment(self, post_id, comment_id):
        """حذف تعليق معين على منشور"""
        return self.send_request("DELETE", f"/posts/{post_id}/comments/{comment_id}")