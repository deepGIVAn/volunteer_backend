from django.db import models
from volunteer_app.choices import *
import uuid
import csv

class Admin(models.Model):
	id = models.CharField(max_length=36, default=uuid.uuid4, unique=True, primary_key=True)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	status = models.BooleanField(default=False)
	role = models.IntegerField(choices=ADMIN_ROLE, default=2)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	@property
	def get_status_display(self):
		return "Active" if self.status else "Inactive"

	def __str__(self):
		return self.name

class AdminPermissions(models.Model):
	admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
	permission = models.IntegerField(choices=ADMIN_PERMISSIONS, default=0)
	permission_status = models.BooleanField(default=False)

	@property
	def permission_name(self):
		return dict(ADMIN_PERMISSIONS).get(self.permission, "Unknown")

	@property
	def get_permission_status_display(self):
		return "Active" if self.permission_status else "Inactive"

	def __str__(self):
		return self.admin.name

class Comments(models.Model):
	id = models.CharField(max_length=36, default=uuid.uuid4, unique=True, primary_key=True)
	admin = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True, blank=True)
	comment_belongs_to = models.CharField(max_length=36)
	comment = models.TextField(null=True, blank=True)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.comment
