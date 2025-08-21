from functools import wraps
from django.http import JsonResponse
from volunteer_app.model.token import AdminToken

def admin_token_required(view_func):
	@wraps(view_func)
	def _wrapped_view(request, *args, **kwargs):
		token_key = request.headers.get('Authorization', '').replace('Bearer ', '')
		try:
			token = AdminToken.objects.get(key=token_key)
			if not token.is_valid():
				return JsonResponse({'error': 'Token expired'}, status=401)
			request.admin = token.admin
			return view_func(request, *args, **kwargs)
		except AdminToken.DoesNotExist:
			return JsonResponse({'error': 'Invalid token'}, status=401)
	return _wrapped_view