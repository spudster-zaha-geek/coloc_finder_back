from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from api.serializers import AnnonceSerializer, ConditionColocationSerializer
from rest_framework.permissions import IsAuthenticated
from api.models import ConditionColocation, Annonce

class CreateAnnonceAPIView(CreateAPIView):
    serializer_class = AnnonceSerializer
    permission_classes = (IsAuthenticated,)
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
class ListAnnonceAPIView(ListAPIView):
    serializer_class = AnnonceSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self):  
        return Annonce.objects.filter(owner=self.request.user)

class CreateConditionColocationView(CreateAPIView):
    serializer_class = ConditionColocationSerializer
    permission_classes = ()
    
class ListConditionColocationView(ListAPIView):
    serializer_class = ConditionColocationSerializer
    permission_classes = ()
    
    def get_queryset(self):  
        return ConditionColocation.objects.all()
    

class AnnoceDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnnonceSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    
    def get_queryset(self):  
        return Annonce.objects.filter(owner=self.request.user)