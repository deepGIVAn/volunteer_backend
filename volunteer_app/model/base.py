from django.db import models
from volunteer_app.choices import *
import uuid
import csv
import random

def generate_4_digit_number_str():
	return f"{random.randint(0, 9999):04d}"

class ActiveManager(models.Manager):
	"""Manager that filters out deleted objects by default"""
	def get_queryset(self):
		return super().get_queryset().filter(isdeleted=False)


class AllObjectsManager(models.Manager):
	"""Manager that returns all objects including deleted ones"""
	def get_queryset(self):
		return super().get_queryset()

class Organisations(models.Model):
	id = models.CharField(max_length=36, default=uuid.uuid4, unique=True, primary_key=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	organisation_name = models.CharField(max_length=200, null=True, blank=True)
	regions_list = models.JSONField(default=list, null=True, blank=True)
	organisation_branch = models.CharField(max_length=200, null=True, blank=True)
	physical_address = models.TextField(null=True, blank=True)
	postal_address = models.TextField(null=True, blank=True)
	contact_name = models.CharField(max_length=200, null=True, blank=True)
	contact_phone = models.CharField(max_length=20, null=True, blank=True)
	contact_email = models.EmailField(max_length=100, null=True, blank=True)
	company_aim = models.TextField(null=True, blank=True)
	website = models.CharField(max_length=200, null=True, blank=True)
	volunteer_name = models.CharField(max_length=200, null=True, blank=True)
	volunteer_phone = models.CharField(max_length=20, null=True, blank=True)
	volunteer_email = models.EmailField(max_length=100, null=True, blank=True)
	time_role = models.CharField(max_length=100, null=True, blank=True)
	disability = models.BooleanField(null=True, blank=True, default=False)
	policies = models.BooleanField(null=True, blank=True, default=False)
	risk = models.BooleanField(null=True, blank=True, default=False)
	charity_number = models.CharField(max_length=20, null=True, blank=True)
	fee = models.CharField(max_length=20, null=True, blank=True)
	organisation_type_list = models.JSONField(default=list, null=True, blank=True)

	status = models.IntegerField(choices=ORGANISATION_STATUS, default=4)
	attachment = models.CharField(max_length=200, null=True, blank=True)

	added_date = models.DateTimeField(null=True, blank=True)
	deactivated_date = models.DateTimeField(null=True, blank=True)
	
	isdeleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# Custom managers
	objects = ActiveManager()  # Default manager excludes deleted objects
	all_objects = AllObjectsManager()  # Manager that includes all objects

	def __str__(self):
		return self.organisation_name

	@property
	def status_display(self):
		status_dict = dict(ORGANISATION_STATUS)
		return status_dict.get(self.status, "Unknown")

	@property
	def regions(self):
		from data import get_regions_list_full
		regions_data = get_regions_list_full()
		regions_dict = {str(region['seq']): region['region'] for region in regions_data}
		if not self.regions_list:
			return []
		return [regions_dict.get(str(region_id), "Unknown") for region_id in self.regions_list]

	@property
	def organisation_types(self):
		from data import get_services_list
		services_data = get_services_list()
		services_dict = {str(service['seq']): service['service'] for service in services_data}
		if not self.organisation_type_list:
			return []
		return [services_dict.get(str(service_id), "Unknown") for service_id in self.organisation_type_list]

class Volunteer(models.Model):
	id = models.CharField(max_length=36, default=uuid.uuid4, unique=True, primary_key=True)
	title = models.CharField(max_length=200, null=True, blank=True)
	first_name = models.CharField(max_length=100, null=True, blank=True)
	last_name = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True)
	street = models.CharField(max_length=200, null=True, blank=True)
	city = models.CharField(max_length=100, null=True, blank=True)
	post_code = models.CharField(max_length=20, null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	year_of_birth = models.IntegerField(null=True, blank=True)
	date_added = models.DateTimeField(null=True, blank=True)
	hours = models.CharField(max_length=20, null=True, blank=True)
	qualification = models.TextField(null=True, blank=True)
	work_experience = models.TextField(null=True, blank=True)
	skills = models.TextField(null=True, blank=True)
	health = models.TextField(null=True, blank=True)
	other_information = models.TextField(null=True, blank=True)
	notes = models.TextField(null=True, blank=True)
	languages = models.TextField(null=True, blank=True)
	type_of_work_list = models.JSONField(default=list, null=True, blank=True)
	region_of_placement_list = models.JSONField(default=list, null=True, blank=True)
	refer_from_list = models.JSONField(default=list, null=True, blank=True)
	days_list = models.JSONField(default=list, null=True, blank=True)
	time_list = models.JSONField(default=list, null=True, blank=True)
	labour_list = models.JSONField(default=list, null=True, blank=True)
	status = models.IntegerField(choices=VOLUNTEER_STATUS, default=3)
	color = models.IntegerField(choices=VOLUNTEER_COLOR, default=0)
	transport_list = models.JSONField(default=list, null=True, blank=True)
	review_date = models.DateTimeField(null=True, blank=True)
	gender = models.IntegerField(choices=GENDER, default=0)
	ethnic_origin_list = models.JSONField(default=list, null=True, blank=True)
	activities_list = models.JSONField(default=list, null=True, blank=True)
	activities_driving_list = models.JSONField(default=list, null=True, blank=True)

	activities_administration_list = models.JSONField(default=list, null=True, blank=True)
	activities_mantinance_list = models.JSONField(default=list, null=True, blank=True)
	activities_home_cares_list = models.JSONField(default=list, null=True, blank=True)
	activities_technology_list = models.JSONField(default=list, null=True, blank=True)
	activities_event_list = models.JSONField(default=list, null=True, blank=True)
	activities_hospitality_list = models.JSONField(default=list, null=True, blank=True)
	activities_support_list = models.JSONField(default=list, null=True, blank=True)

	activities_financial_list = models.JSONField(default=list, null=True, blank=True)
	activities_other_list = models.JSONField(default=list, null=True, blank=True)
	activities_sport_list = models.JSONField(default=list, null=True, blank=True)
	activities_group_list = models.JSONField(default=list, null=True, blank=True)

	isdeleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# Custom managers
	objects = ActiveManager()  # Default manager excludes deleted objects
	all_objects = AllObjectsManager()  # Manager that includes all objects

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Role(models.Model):
	id = models.CharField(max_length=36, default=uuid.uuid4, unique=True, primary_key=True)
	roleId = models.CharField(max_length=10, unique=True, null=True, blank=True)
	title = models.CharField(max_length=200)
	organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE)
	contact = models.TextField(null=True, blank=True)
	branch = models.CharField(max_length=200, null=True, blank=True)
	status = models.IntegerField(choices=ROLE_STATUS, default=1)
	vols_req = models.CharField(max_length=100, null=True, blank=True)
	reports = models.CharField(max_length=200, null=True, blank=True)
	email = models.EmailField(max_length=100, null=True, blank=True)
	date_added = models.DateTimeField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	results = models.TextField(null=True, blank=True)
	leagues_hours = models.TextField(null=True, blank=True)
	skills = models.TextField(null=True, blank=True)
	personality = models.TextField(null=True, blank=True)
	criminal = models.BooleanField(default=False)
	transport = models.BooleanField(default=False)
	wheelchair = models.BooleanField(default=False)
	toilet = models.BooleanField(default=False)
	stairs = models.BooleanField(default=False)
	home = models.BooleanField(default=False)
	oneoff = models.BooleanField(default=False)
	leagues_days = models.TextField(null=True, blank=True)
	start_date = models.DateTimeField(null=True, blank=True)
	end_date = models.DateTimeField(null=True, blank=True)
	training = models.TextField(null=True, blank=True)
	reimbursement = models.TextField(null=True, blank=True)
	reimbursement_other = models.TextField(null=True, blank=True)
	supervision = models.CharField(max_length=200, null=True, blank=True)
	other = models.TextField(null=True, blank=True)
	paid_job = models.BooleanField(default=False)
	notes = models.TextField(null=True, blank=True)
	filter_color = models.IntegerField(choices=VOLUNTEER_COLOR, default=0)
	youth = models.BooleanField(default=False)
	english = models.BooleanField(default=False)
	disability = models.BooleanField(default=False)
	mental = models.BooleanField(default=False)
	region_of_placement_list = models.JSONField(default=list, null=True, blank=True)
	days_list = models.JSONField(default=list, null=True, blank=True)
	time_list = models.JSONField(default=list, null=True, blank=True)
	activities_driving_list = models.JSONField(default=list, null=True, blank=True)
	activities_administration_list = models.JSONField(default=list, null=True, blank=True)
	activities_mantinance_list = models.JSONField(default=list, null=True, blank=True)
	activities_home_cares_list = models.JSONField(default=list, null=True, blank=True)
	activities_technology_list = models.JSONField(default=list, null=True, blank=True)
	activities_event_list = models.JSONField(default=list, null=True, blank=True)
	activities_hospitality_list = models.JSONField(default=list, null=True, blank=True)
	activities_support_list = models.JSONField(default=list, null=True, blank=True)
	activities_financial_list = models.JSONField(default=list, null=True, blank=True)
	activities_other_list = models.JSONField(default=list, null=True, blank=True)
	activities_sport_list = models.JSONField(default=list, null=True, blank=True)
	activities_group_list = models.JSONField(default=list, null=True, blank=True)
	attachments = models.CharField(max_length=200, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	isdeleted = models.BooleanField(default=False)
	deleted_at = models.DateTimeField(null=True, blank=True)

	# Custom managers
	objects = ActiveManager()  # Default manager excludes deleted objects
	all_objects = AllObjectsManager()  # Manager that includes all objects

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.roleId:
			# Try up to 10 times to avoid rare collisions
			for _ in range(10):
				candidate = generate_4_digit_number_str()
				if not Role.objects.filter(roleId=candidate).exists():
					self.roleId = candidate
					break
			else:
				raise ValueError("Could not generate a unique 4-digit roleId after 10 attempts.")
		super().save(*args, **kwargs)

	@property
	def status_display(self):
		status_dict = dict(ROLE_STATUS)
		return status_dict.get(self.status, "Unknown")

	@property
	def color_display(self):
		color_dict = dict(VOLUNTEER_COLOR)
		return color_dict.get(self.filter_color, "Unknown")

	@property
	def regions(self):
		from data import get_regions_list_full
		regions_data = get_regions_list_full()
		regions_dict = {str(region['seq']): region['region'] for region in regions_data}
		if not self.region_of_placement_list:
			return []
		return [regions_dict.get(str(region_id), "Unknown") for region_id in self.region_of_placement_list]

	@property
	def days(self):
		try:
			from data import get_days
			days_data = get_days()
			days_dict = {str(day['seq']): day['day'] for day in days_data}
			if not self.days_list:
				return []
			return [days_dict.get(str(day_id), "Unknown") for day_id in self.days_list]
		except:
			return []

	@property
	def times(self):
		try:
			from data import get_times
			times_data = get_times()
			times_dict = {str(time['seq']): time['time'] for time in times_data}
			if not self.time_list:
				return []
			return [times_dict.get(str(time_id), "Unknown") for time_id in self.time_list]
		except:
			return []

	def _get_activities(self, activity_type, activity_list):
		try:
			with open(f'data/activities_{activity_type}.csv', 'r') as file:
				reader = csv.DictReader(file)
				activities_dict = {str(row['seq']): row['activity'] for row in reader}
				if not activity_list:
					return []
				return [activities_dict.get(str(activity_id), "Unknown") for activity_id in activity_list]
		except:
			return []

	@property
	def activities_driving(self):
		return self._get_activities('driving', self.activities_driving_list)

	@property
	def activities_administration(self):
		return self._get_activities('administration', self.activities_administration_list)

	@property
	def activities_mantinance(self):
		return self._get_activities('mantinance', self.activities_mantinance_list)

	@property
	def activities_home_cares(self):
		return self._get_activities('home_cares', self.activities_home_cares_list)

	@property
	def activities_technology(self):
		return self._get_activities('technology', self.activities_technology_list)

	@property
	def activities_event(self):
		return self._get_activities('event', self.activities_event_list)

	@property
	def activities_hospitality(self):
		return self._get_activities('hospitality', self.activities_hospitality_list)

	@property
	def activities_support(self):
		return self._get_activities('support', self.activities_support_list)

	@property
	def activities_financial(self):
		return self._get_activities('financial', self.activities_financial_list)

	@property
	def activities_other(self):
		return self._get_activities('other', self.activities_other_list)

	@property
	def activities_sport(self):
		return self._get_activities('sport', self.activities_sport_list)

	@property
	def activities_group(self):
		return self._get_activities('group', self.activities_group_list)