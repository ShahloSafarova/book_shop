from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Books(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  isbn = models.PositiveIntegerField(unique=True)
  image_book = models.ImageField(default='books_images/default_book_image.png', upload_to='media/books_images')
  price = models.DecimalField(max_digits=6, decimal_places=2)
  publisher = models.CharField(max_length=50, blank=True, null=True)
  create_at = models.DateField(auto_now_add=True)
  update_at = models.DateField(auto_now=True)
  
def __str__(self):
  return self.title


class Author(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  email = models.EmailField()
  description = models.TextField()
  
  def __str__(self):
    return self.name
  
class BookAuthor(models.Model):
  book = models.ForeignKey(Books, on_delete=models.CASCADE)
  author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default='deleted author')
  
  def __str__(self):
    return f'{self.book.title}, {self.author.name}'
  
  def get_info(self):
    return f'{self.book.title}, {self.author.name}'
  
class BookReview(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  book = models.ForeignKey(Books, on_delete=models.CASCADE)
  comment = models.TextField()
  star_given = models.PositiveIntegerField(default=0, validators=[
    MinValueValidator(1),
    MaxValueValidator(5)
  ])
  create_at = models.DateField(auto_now_add=True)
  update_at = models.DateField(auto_now=True)
  
  def __str__(self):
    return self.book.title