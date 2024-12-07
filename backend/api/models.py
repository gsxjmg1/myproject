from django.db import models


class HomePage(models.Model):
    page_name = models.CharField(max_length=100)
    home_image = models.URLField()


class Swiper(models.Model):
    swiper_image = models.URLField()


class DetailPage(models.Model):
    model_info = models.JSONField()
