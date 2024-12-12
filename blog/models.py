from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from colorfield.fields import ColorField
from cloudinary.models import CloudinaryField
from markdownx.models import MarkdownxField

class PostCategory(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    color = ColorField(default="#000")  # For displaying category as a badge

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField(blank=True, help_text="A short summary of the post", max_length=100)
    content = MarkdownxField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(PostCategory, related_name="posts")
    tags = models.CharField(max_length=500, blank=True, help_text="Comma-separated tags (e.g., Django,Python,Web)")
    feature_image = CloudinaryField("image", blank=True, null=True, overwrite=True, resource_type="image", folder="blog-feature-images")
    meta_title = models.CharField(max_length=60, blank=True, help_text="Custom title for SEO (max 60 characters)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="Custom description for SEO (max 160 characters)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        # Automatically generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.title)
        # Auto-generate meta_title if not provided
        if not self.meta_title:
            self.meta_title = self.title[:60]
        # Auto-generate meta_description if not provided
        if not self.meta_description:
            self.meta_description = (self.content[:157] + "...") if len(self.content) > 157 else self.content
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
