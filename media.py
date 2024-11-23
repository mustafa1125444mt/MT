from .client import AminoClient

class AminoMedia(AminoClient):
    def upload_image(self, file_path):
        """رفع صورة إلى الخادم لاستخدامها في الملف الشخصي أو في المجموعة"""
        with open(file_path, "rb") as file:
            image_data = file.read()
        return self.send_request("POST", "/media/upload/image", image_data)

    def upload_video(self, file_path):
        """رفع فيديو إلى الخادم لاستخدامه في الرسائل أو المنشورات"""
        with open(file_path, "rb") as file:
            video_data = file.read()
        return self.send_request("POST", "/media/upload/video", video_data)