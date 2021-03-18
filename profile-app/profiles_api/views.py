from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers, models, permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API features"""
        an_api_view = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
        ]

        return Response(
            {
                'message': 'hello!',
                'an_api_view': an_api_view
            }
        )

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}!'
            return Response(
                {
                    'message': message
                }
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_view_set = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
        ]

        return Response(
            {
                'message': 'Hello!',
                'a_view_set': a_view_set
            }
        )

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response(
                {
                    'message': message
                }
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response(
            {
                'http_method': 'GET',
                'pk': pk
            }
        )

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response(
            {
                'http_method': 'PUT',
                'pk': pk
            }
        )

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response(
            {
                'http_method': 'PATCH',
                'pk': pk
            }
        )

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response(
            {
                'http_method': 'DELETE',
                'pk': pk
            }
        )


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
