# import for authentication
from django.contrib.auth.models import User

# import for forms and models
from .models import Profile

# imports for api
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

model = Profile.objects.all()
auth = User.objects.all()

# custom class for permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


# view for getting all the profile
class Profiles(generics.ListAPIView):
    queryset = model
    serializer_class = ProfileSerializer


# view for getting a profile in detailed view
class SingleProfile(generics.RetrieveAPIView):
    queryset = model
    serializer_class = ProfileSerializer


# view for updating the profile if the the PUT request is done by the owner
class updateProfile(generics.RetrieveUpdateAPIView):
    queryset = model
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]


# view for registering a user
class Registering(viewsets.ModelViewSet):
    queryset = auth
    serializer_class = UserSerializer
