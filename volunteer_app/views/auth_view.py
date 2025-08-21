import secrets
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from volunteer_app.model.admin import Admin, AdminPermissions
from volunteer_app.model.token import AdminToken
from django.contrib.auth.hashers import check_password
from volunteer_app.decorators import admin_token_required

@api_view(['POST'])
@permission_classes([AllowAny])
def admin_login(request):
	email = request.data.get('email')
	password = request.data.get('password')
	try:
		admin = Admin.objects.get(email=email, status=True)
		if check_password(password, admin.password):
			# Generate new token
			token_key = secrets.token_hex(20)
			AdminToken.objects.filter(admin=admin).delete()  # Remove old tokens
			token = AdminToken.objects.create(admin=admin, key=token_key)
			permissions = list(AdminPermissions.objects.filter(admin=admin, permission_status=True).values_list('permission', flat=True))
			return Response({
				'token': token.key,
				'admin_id': admin.id,
				'name': admin.name,
				'email': admin.email,
				'role': admin.role,
				'permissions': permissions,
				'status': admin.status,
			})
		else:
			return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
	except Admin.DoesNotExist:
		return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@permission_classes([AllowAny])
@admin_token_required
def get_admin_info(request):
	admin = request.admin
	permissions = list(AdminPermissions.objects.filter(admin=admin, permission_status=True).values_list('permission', flat=True))
	return Response({
		'admin_id': admin.id,
		'name': admin.name,
		'email': admin.email,
		'role': admin.role,
		'permissions': permissions,
		'status': admin.status,
	})
