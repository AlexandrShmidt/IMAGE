from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_base64 = models.TextField()  # Хранение base64 строки
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
