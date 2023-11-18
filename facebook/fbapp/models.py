from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save,pre_save
# from django.dispatch import receiver
import  uuid

class feeds(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    feed_id=models.AutoField(unique=True ,primary_key=True)
    image=models.ImageField(upload_to='feed', max_length=None,default="")
    desc=models.CharField(max_length=100)
    date_feeded=models.DateField(auto_now=False, auto_now_add=False, blank=True,null=True )
    
    def __str__(self):
        return str(self.feed_id)

class like_msg(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="like")
    feed_id=models.CharField(default=uuid.uuid4,max_length=1000)
    liked=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
    

class comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    feed_id=models.ForeignKey(feeds,on_delete=models.CASCADE,related_name="com")
    comment_id=models.AutoField(unique=True ,primary_key=True)
    text=models.CharField(max_length=500)
    date_cmt=models.DateTimeField(auto_now_add=True, blank=True,null=True )


    def __str__(self):
        return str(self.feed_id)

















































































# class profile(models.Model):
#     user=models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
#     dob=models.DateField(auto_now_add=True)
#     gender=models.CharField(default='custom' ,max_length=50)
#     ph=models.IntegerField()

#     def __str__(self):
#         return self.user
    
# # @receiver(post_save, sender=User)
# # def create_profile(sender, instance=, created, **kwargs):
# #     if created:
# #         profile.objects.create(user=instance)
# #         print("Profile created!")

# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         profile.objects.create(user=instance)

# post_save.connect(create_user_profile, sender=User)

# @receiver(post_save, sender=User) 
# def save_profile(sender, instance, **kwargs):
#         instance.profile.save()


# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if not created:
#         print("Custom user updated!")

# @receiver(post_save, sender=User)
# def update_profile(sender, instance, created, **kwargs):
#     if not created:
#         instance.profile.save()
#         print("Profile updated!")