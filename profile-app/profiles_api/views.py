from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets

from profiles_api import serializers


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
