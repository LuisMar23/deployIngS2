from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from ..serializers import BranchOfficeSerializer
from ...models import BranchOffice


class BranchOfficeViewSet(viewsets.ModelViewSet):
    serializer_class = BranchOfficeSerializer
    queryset = BranchOfficeSerializer.Meta.model.objects.all()

    view_permissions = {
        'create,list,destroy,update':{'admin': True, 'contador':True}
    }

    def list(self, request):
        sede_serializer = BranchOfficeSerializer(BranchOffice.objects.all(), many=True)
        return Response(sede_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        estado = int(request.query_params.get('accion'))
        sede = get_object_or_404(BranchOffice, id=pk)
        sede.is_active = estado
        sede.save()
        return Response({'estado': estado}, status=status.HTTP_200_OK)
