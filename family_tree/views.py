from rest_framework import viewsets
from .models import User, FamilyMember, Relationship
from .serializers import UserSerializer, FamilyMemberSerializer, RelationshipSerializer
from django.db.models import Q

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class RelationshipViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

def calculate_tree_height(member_id):
    def get_height(member):
        children = Relationship.objects.filter(parent=member)
        if not children:
            return 1
        return 1 + max(get_height(child.child) for child in children)
    
    root_member = FamilyMember.objects.get(pk=member_id)
    return get_height(root_member)
