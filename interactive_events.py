from .client import AminoClient

class AminoInteractiveEvent(AminoClient):
    def start_interactive_event(self, group_id, event_title, event_description):
        """بدء حدث تفاعلي داخل المجموعة"""
        data = {"title": event_title, "description": event_description}
        return self.send_request("POST", f"/groups/{group_id}/interactive_events", data)

    def get_interactive_events(self, group_id):
        """الحصول على جميع الأحداث التفاعلية في المجموعة"""
        return self.send_request("GET", f"/groups/{group_id}/interactive_events")

    def interact_with_event(self, group_id, event_id, reaction):
        """التفاعل مع حدث تفاعلي (رد فعل مثل "أعجبني" أو "موافق")"""
        data = {"reaction": reaction}
        return self.send_request("POST", f"/groups/{group_id}/interactive_events/{event_id}/reaction", data)