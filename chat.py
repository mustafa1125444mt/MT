from .client import AminoClient

class AminoChat(AminoClient):
    def send_message(self, chat_id, message):
        data = {"message": message}
        return self.send_request("POST", f"/chats/{chat_id}/send_message", data)

    def get_chat_messages(self, chat_id):
        return self.send_request("GET", f"/chats/{chat_id}/messages")

    def delete_message(self, chat_id, message_id):
        return self.send_request("DELETE", f"/chats/{chat_id}/messages/{message_id}")

    def get_chat_info(self, chat_id):
        return self.send_request("GET", f"/chats/{chat_id}")