from django.test import TestCase
from .models import User, FamilyMember, Relationship

class FamilyTreeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="test@example.com")
        self.member1 = FamilyMember.objects.create(user=self.user, first_name="John", last_name="Doe")
        self.member2 = FamilyMember.objects.create(user=self.user, first_name="Jane", last_name="Doe")
        Relationship.objects.create(parent=self.member1, child=self.member2)

    def test_family_member_creation(self):
        self.assertEqual(FamilyMember.objects.count(), 2)
    
    def test_relationship_creation(self):
        self.assertEqual(Relationship.objects.count(), 1)

    def test_calculate_tree_height(self):
        from .views import calculate_tree_height
        height = calculate_tree_height(self.member1.id)
        self.assertEqual(height, 2)
