from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.

# This class handles both listing and creating Note objects
# Specify the serializer class to use for Note objects
# Ensure that only authenticated users can access this view
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # Get the currently authenticated user
    # Return only the notes authored by the current user
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    # Check if the serializer data is valid
    # Save the new note, setting the author to the current user
    # If the data is invalid, print the errors (for debugging purposes)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# This class handles user creation (registration)
# # Use all User objects as the queryset
# # Specify the serializer class to use for User objects
# # Allow any user (authenticated or not) to access this view
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
