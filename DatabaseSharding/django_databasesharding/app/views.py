from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import SaleOrder
from app.serializers import SaleOrderSerializer

class SaleOrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        # Deserialize the incoming data
        serializer = SaleOrderSerializer(data=request.data)
        
        # If data is valid, save the order
        if serializer.is_valid():
            # Save the order to the correct shard
            serializer.save()  # No need to pass 'using' here, it's handled by the serializer's create method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
