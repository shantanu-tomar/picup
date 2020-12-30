from django.db import models


UPLOAD_FOLDER = 'uploads'


class Image(models.Model):
    image = models.ImageField(upload_to=UPLOAD_FOLDER)
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def get_image_name(self):
        return self.image.name.replace(f"{UPLOAD_FOLDER}/", '')
