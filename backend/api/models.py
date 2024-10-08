from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    # The title of the note, limited to 100 characters
    title = models.CharField(max_length=100)
    
    # The main content of the note, can be of any length
    content = models.TextField()
    
    # Automatically set to the current date and time when the note is created
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Links the note to a User (author). If the user is deleted, all their notes will be deleted too.
    # 'related_name' allows us to access a user's notes via user.notes.all()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    
    def __str__(self):
        # Returns the title of the note when the object is printed
        # This is useful for representing the note in the Django admin interface
        return self.title
    
