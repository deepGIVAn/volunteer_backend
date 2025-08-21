from django.db import models
from django.utils import timezone
from volunteer_app.model.admin import Admin

class AdminToken(models.Model):
	admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
	key = models.CharField(max_length=40, unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def is_valid(self):
		return timezone.now() - self.created < timezone.timedelta(days=1)