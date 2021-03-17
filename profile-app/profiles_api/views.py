from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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
