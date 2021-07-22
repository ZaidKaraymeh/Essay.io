from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to = "profile_pics", editable = True, blank=True)
    # image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    # image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")

    # def __unicode__(self):
    #     return "{0}".format(self.image)

    # def save(self):
    #     if not self.image:
    #         return            

    #     super(Profile, self).save()
    #     image = Image.open(self.photo)
    #     (width, height) = image.size     
    #     size = ( 100, 100)
    #     image = image.resize(size, image.ANTIALIAS)
    #     image.save(self.photo.path)

    def __str__(self):
        return f"{self.user.username} Profile"



# class Student(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#     class Meta:
#         permissions = [("can_post_assignments", "Can post assignments")]

# class Instructor(Profile):
#     class Meta:
#         permissions = [("can_create_assignments", "Can create assignments")]