from rest_framework import viewsets
from ..models.user import User
from ..serializers.user import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user = self.request.query_params.get('user', None)
        return queryset.filter(username=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)