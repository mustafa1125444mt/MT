from .client import AminoClient

class AminoPoll(AminoClient):
    def create_poll(self, group_id, question, options):
        """إنشاء استطلاع داخل المجموعة"""
        data = {
            "question": question,
            "options": options
        }
        return self.send_request("POST", f"/groups/{group_id}/polls", data)

    def get_poll_results(self, group_id, poll_id):
        """الحصول على نتائج استطلاع معين"""
        return self.send_request("GET", f"/groups/{group_id}/polls/{poll_id}/results")

    def vote_in_poll(self, group_id, poll_id, option_id):
        """التصويت في استطلاع معين"""
        data = {"option_id": option_id}
        return self.send_request("POST", f"/groups/{group_id}/polls/{poll_id}/vote", data)

    def delete_poll(self, group_id, poll_id):
        """حذف استطلاع معين"""
        return self.send_request("DELETE", f"/groups/{group_id}/polls/{poll_id}")