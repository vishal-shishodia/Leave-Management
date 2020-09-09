from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.models import *
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
	if instance.is_manager:	
		Manager.objects.get_or_create(user=instance)
	else:
		Employee.objects.get_or_create(user=instance)
	

		
	
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
	if instance.is_manager:	
		instance.manager.save()
	else:
		instance.employee.save()
	


	
