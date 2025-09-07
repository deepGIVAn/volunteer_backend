import secrets
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from volunteer_app.model.admin import Admin, AdminPermissions
from volunteer_app.model.token import AdminToken
from django.contrib.auth.hashers import check_password, make_password
from volunteer_app.decorators import admin_token_required, super_admin_required
from volunteer_app.serializers import AdminSerializer

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
@admin_token_required
def get_admin_info(request):
	admin = request.admin
	permissions = list(AdminPermissions.objects.filter(admin=admin, permission_status=True).values_list('permission', flat=True))
	return Response({
		'success': True,
		'admin_id': admin.id,
		'name': admin.name,
		'email': admin.email,
		'role': admin.role,
		'permissions': permissions,
		'status': admin.status,
	})

@api_view(['POST'])
@admin_token_required
def admin_logout(request):
	admin = request.admin
	token_key = request.headers.get('Authorization', '').replace('Bearer ', '')
	AdminToken.objects.filter(admin=admin, key=token_key).delete()
	return Response({'success': True, 'message': 'Logged out successfully.'})

@api_view(['POST'])
@admin_token_required
@super_admin_required
def create_staff(request):
	try:
		data = {
			'name': request.data.get('name', None),
			'email': request.data.get('email', None),
			'password': request.data.get('password', None),
			# 'role': request.data.get('role', 2),  # Default to Staff
			'role': 2,
			'status': request.data.get('status', False),
		}
		if data['password']:
			data['password'] = make_password(data['password'])
		staff = Admin.objects.create(**{k: v for k, v in data.items() if v is not None})
		serialized_staff = AdminSerializer(staff)
		return Response(serialized_staff.data, status=201)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)

@api_view(['GET'])
@admin_token_required
@super_admin_required
def get_all_staff(request):
	try:
		staff_members = Admin.objects.filter(role=2)
		serialized_staff = AdminSerializer(staff_members, many=True)
		return Response(serialized_staff.data, status=200)
	except Exception as e:
		# print(e)
		return Response([], status=400)

@api_view(['DELETE'])
@admin_token_required
@super_admin_required
def delete_staff(request, id):
	try:
		staff = Admin.objects.get(id=id, role=2)
		staff.delete()
		return Response({"success": True, "message": "Staff member deleted successfully."}, status=204)
	except Admin.DoesNotExist:
		return Response({"error": "Staff member not found"}, status=404)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)

@api_view(['POST'])
@admin_token_required
@super_admin_required
def update_staff(request, id):
	try:
		pass
		staff = Admin.objects.get(id=id, role=2)
		data = {
			'name': request.data.get('name', staff.name),
			'email': request.data.get('email', staff.email),
			'password': request.data.get('password', None),
			'status': request.data.get('status', staff.status),
		}
		if data['password']:
			data['password'] = make_password(data['password'])
		else:
			data.pop('password')
		for key, value in data.items():
			setattr(staff, key, value)
		staff.save()
		serialized_staff = AdminSerializer(staff)
		return Response(serialized_staff.data, status=200)
	except Admin.DoesNotExist:
		return Response({"error": "Staff member not found"}, status=404)
	except Exception as e:
		# print(e)
		return Response({"error": str(e)}, status=400)