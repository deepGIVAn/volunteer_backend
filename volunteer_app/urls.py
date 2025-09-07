from django.urls import path
from volunteer_app.views import auth_view, base_view, organisation_view, role_view, volunteer_view

app_name = "volunteer_app"

urlpatterns = [
	path('admin/login', auth_view.admin_login, name="admin_login"),
	path('admin/info/', auth_view.get_admin_info, name="admin_info"),
	path('admin/logout/', auth_view.admin_logout, name="admin_logout"),

	path('get-preset/<str:type>/', base_view.get_preset, name="get_preset"),

	path('admin/create-organisation/', organisation_view.create_organisation, name="create_organisation"),
	path('admin/get-all-organisations/', organisation_view.get_all_organisations, name="get_all_organisations"),
	path('admin/get-organisation/<str:id>/', organisation_view.get_organisation, name="get_organisation"),
	path('admin/delete-organisation/<str:id>/', organisation_view.delete_organisation, name="delete_organisation"),
	path('admin/update-organisation/<str:id>/', organisation_view.update_organisation, name="update_organisation"),
	
	path('admin/create-role/', role_view.create_role, name="create_role"),
	path('admin/get-all-roles/', role_view.get_all_roles, name="get_all_roles"),
	path('admin/get-role/<str:id>/', role_view.get_role, name="get_role"),
	path('admin/delete-role/<str:id>/', role_view.delete_role, name="delete_role"),
	path('admin/update-role/<str:id>/', role_view.update_role, name="update_role"),

	path('admin/create-volunteer/', volunteer_view.create_volunteer, name="create_volunteer"),
	path('admin/get-all-volunteers/', volunteer_view.get_all_volunteers, name="get_all_volunteers"),
	path('admin/get-volunteer/<str:id>/', volunteer_view.get_volunteer, name="get_volunteer"),
	path('admin/delete-volunteer/<str:id>/', volunteer_view.delete_volunteer, name="delete_volunteer"),
	path('admin/update-volunteer/<str:id>/', volunteer_view.update_volunteer, name="update_volunteer"),

	path('admin/create-staff/', auth_view.create_staff, name="create_staff"),
	path('admin/get-all-staff/', auth_view.get_all_staff, name="get_all_staff"),
	path('admin/delete-staff/<str:id>/', auth_view.delete_staff, name="delete_staff"),
	path('admin/update-staff/<str:id>/', auth_view.update_staff, name="update_staff"),
]
