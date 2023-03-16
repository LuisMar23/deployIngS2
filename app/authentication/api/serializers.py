from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass
