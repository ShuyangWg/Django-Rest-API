from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'gives you',
            'is mapped to urls',
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})
        
