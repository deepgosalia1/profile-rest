from rest_framework.response import Response
from rest_framework.views import APIView
from profiles_api import serializers
from rest_framework import viewsets
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        an_apiview = ['1','2','3','4','5']
        return Response({'message':'Hello!', 'an_apiview':an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello "+name+" !"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=400
            )
    
    def put(self, request, pk = None):
        """For updating a particular object with the given key (pk)"""
        return Response({'method':'PUT'})
    
    def patch(self, request, pk = None):
        """For PARTIALLY updating a particular object with the given key (pk)"""
        return Response({'method':'PATCH'})
    
    def delete(self, request, pk = None):
        """For deleting a particular object with the given key (pk)"""
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test for API Viewsets"""

    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        a_viewset=[1,2,3,3,4,5]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello "+name+" !"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=400
            )
    
    def retrieve(self, request, pk = None):
        """For retrieving a particular object with the given key (pk) or an ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk = None):
        """For updating a particular object with the given key (pk)"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk = None):
        """For partially updating a particular object with the given key (pk)"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk = None):
        """For deleting a particular object with the given key (pk)"""
        return Response({'http_method':'DELETE'})

class UserprofileViewSet(viewsets.ModelViewSet):
    """CRUD on profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)