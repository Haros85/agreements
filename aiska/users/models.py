from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    SEX = (
        ('male', 'Мужчина'),
        ('female', 'Женщина'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    sex = models.CharField(max_length=10, choices=SEX, verbose_name="Пол")

    class Meta:
        verbose_name = u"Профиль"
        verbose_name_plural = u"Профили"

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()