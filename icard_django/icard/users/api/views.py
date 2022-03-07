from rest_framework.viewsets import ModelViewSet
# Para que los usuarios no propietario obtengan sus propios datos
from rest_framework.views import APIView
# Permisos de IsAdminUser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from users.models import User
from users.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    # Quienes van a utilizar el servicio del API user que solo son los adminitradores
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    # El queryset es que modelo va a utilizar
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

    # Creación de la clases para los usuarios no propietarios el usuario obtendra solo sus propios datos
    class UserView(APIView):
        permission_classes = [IsAuthenticated]

        def get(self, request):
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
