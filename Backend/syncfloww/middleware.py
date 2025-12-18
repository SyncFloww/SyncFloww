import jwt
import requests
from django.conf import settings
from django.http import JsonResponse

# Use a default value or handle the setting properly
SUPABASE_URL = getattr(settings, 'SUPABASE_URL', '')
SUPABASE_JWKS_URL = f"{SUPABASE_URL}/auth/v1/certs"

_jwks_cache = None

def get_jwks():
    global _jwks_cache
    if not _jwks_cache and SUPABASE_URL: # Only try if URL is set
        try:
            _jwks_cache = requests.get(SUPABASE_JWKS_URL).json()
        except Exception:
            pass # Handle gracefully if offline/not configured
    return _jwks_cache


class SupabaseJWTMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth = request.headers.get("Authorization")

        if auth and auth.startswith("Bearer "):
            token = auth.split(" ")[1]
            try:
                # In development/offline without keys, we might want to skip or mock
                # For now, we attempt verification if we have keys
                jwks = get_jwks()
                if jwks:
                    payload = jwt.decode(
                        token,
                        jwks,
                        algorithms=["RS256"],
                        audience="authenticated",
                    )
                    request.supabase_user = payload
            except Exception:
                # For strict auth endpoints, DRF permissions will handle the 401 later if user is not authenticated
                # This middleware just attempts to attach info
                pass

        return self.get_response(request)
