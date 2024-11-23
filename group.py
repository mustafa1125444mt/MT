from .client import AminoClient

class AminoGroup(AminoClient):
    def create_group(self, name, description):
        data = {"name": name, "description": description}
        return self.send_request("POST", "/groups", data)

    def get_group_info(self, group_id):
        return self.send_request("GET", f"/groups/{group_id}")

    def search_groups(self, query):
        return self.send_request("GET", f"/groups/search?query={query}")

    def join_group(self, group_id):
        return self.send_request("POST", f"/groups/{group_id}/join")

    def leave_group(self, group_id):
        return self.send_request("POST", f"/groups/{group_id}/leave")