from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User, UserProfile


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the user profile if not exist
            UserProfile.objects.create(user=instance)
            print('Profile was not exist ')
        print('user is updated')

# post_save.connect(post_save_create_profile_receiver, sender=User)
