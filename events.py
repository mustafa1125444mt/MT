from .client import AminoClient

class AminoEvent(AminoClient):
    def create_event(self, group_id, event_title, event_description, event_date):
        """إنشاء حدث جديد في المجموعة"""
        data = {
            "title": event_title,
            "description": event_description,
            "event_date": event_date
        }
        return self.send_request("POST", f"/groups/{group_id}/events", data)

    def get_events(self, group_id):
        """الحصول على قائمة بالأحداث القادمة في المجموعة"""
        return self.send_request("GET", f"/groups/{group_id}/events")

    def delete_event(self, group_id, event_id):
        """حذف حدث معين في المجموعة"""
        return self.send_request("DELETE", f"/groups/{group_id}/events/{event_id}")