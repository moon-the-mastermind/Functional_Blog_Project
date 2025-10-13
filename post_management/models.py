from django.db import models
from django.conf import settings
from django.utils.text import slugify
from .utils import generate_slug

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image= models.ImageField(upload_to="posts/")
    slug = models.SlugField(unique=True, blank=True)
    views = models.PositiveBigIntegerField(blank=True, default=0)
    
    # relationship
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True ,related_name="liked_posts")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "posts")
    category = models.ForeignKey(Category, blank= True, null=True, on_delete= models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = generate_slug(self.title) or "post"
            slug = base_slug
            num = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    body = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    commented_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user" )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments" )

    def __str__(self):
        return self.body[:50]
    





