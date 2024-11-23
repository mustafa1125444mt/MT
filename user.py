from .client import AminoClient

class AminoUser(AminoClient):
    def get_user_info(self, user_id):
        return self.send_request("GET", f"/users/{user_id}")

    def update_profile(self, name, bio, avatar_url):
        data = {"name": name, "bio": bio, "avatar_url": avatar_url}
        return self.send_request("PUT", "/users/me", data)

    def change_avatar(self, avatar_url):
        data = {"avatar_url": avatar_url}
        return self.send_request("PUT", "/users/me/avatar", data)

    def search_users(self, query):
        return self.send_request("GET", f"/users/search?query={query}")
    
    def login_with_credentials(self, email, password):
        """تسجيل الدخول باستخدام البريد الإلكتروني وكلمة المرور"""
        token = self.login(email, password)
        return token