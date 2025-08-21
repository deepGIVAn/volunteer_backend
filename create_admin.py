
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'volunteer_project.settings')
django.setup()

from volunteer_app.model.admin import Admin, AdminPermissions
from django.contrib.auth.hashers import make_password

def create_admin():
    email = 'admin@volunteercentral.nz'
    password = '123456'
    name = 'admin'
    if not Admin.objects.filter(email=email).exists():
        hashed_password = make_password(password)
        admin = Admin.objects.create(
            name=name,
            email=email,
            password=hashed_password,
            status=True,
            role=1
        )
        AdminPermissions.objects.create(admin=admin, permission=1, permission_status=True)
        print('Admin and AdminPermissions created.')
    else:
        print('Admin already exists.')

if __name__ == '__main__':
    create_admin()
