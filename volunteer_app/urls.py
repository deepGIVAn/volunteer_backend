from django.urls import path
from volunteer_app.views import auth_view

app_name = "volunteer_app"

urlpatterns = [
	path('admin/login/', auth_view.admin_login, name="admin_login"),
	path('admin/info/', auth_view.get_admin_info, name="admin_info"),
]
