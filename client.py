import requests

class AminoClient:
    def __init__(self, base_url="https://api.aminoapps.com"):
        self.base_url = base_url
        self.headers = {}

    def send_request(self, method, endpoint, data=None):
        """إرسال طلب HTTP إلى الـ API"""
        url = f"{self.base_url}{endpoint}"
        if method == "GET":
            response = requests.get(url, headers=self.headers)
        elif method == "POST":
            response = requests.post(url, json=data, headers=self.headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=self.headers)
        elif method == "DELETE":
            response = requests.delete(url, headers=self.headers)
        return response.json()

    def authenticate(self, token):
        """استخدام التوكن للمصادقة"""
        self.headers['Authorization'] = token

    def login(self, email, password):
        """تسجيل الدخول باستخدام البريد الإلكتروني وكلمة المرور"""
        login_url = f"{self.base_url}/login"
        data = {
            "email": email,
            "password": password
        }
        response = requests.post(login_url, json=data)
        if response.status_code == 200:
            # إذا تم التسجيل بنجاح، نحتفظ بالتوكن الذي تم إرجاعه
            token = response.json().get("authToken")
            self.authenticate(token)
            return token
        else:
            # إذا فشل تسجيل الدخول، نرجع رسالة خطأ
            raise Exception("Login failed. Check your credentials.")