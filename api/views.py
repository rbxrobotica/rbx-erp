from rest_framework import viewsets, serializers
from rest_framework.response import Response
from crm.models import Lead, Origem
from .serializers import LeadSerializer, OrigemSerializer, LeadPostSerializer
import logging

logger = logging.getLogger(__name__)

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class OrigemViewSet(viewsets.ModelViewSet):
    queryset = Origem.objects.all()
    serializer_class = OrigemSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)  

        try:
            logger.debug(f"Request data: {request.data}")  # Log os dados da requisição
            origem, created = Origem.objects.get_or_create(nome=serializer.validated_data['origem'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            logger.error(f"Error creating Origem: {e}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

