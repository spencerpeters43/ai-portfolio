from django.db import models
from django.urls import reverse


class Project(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('chatbot', 'Chatbot'),
        ('workflow', 'Workflow'),
        ('code', 'Code / Script'),
        ('video', 'Video'),
        ('web_app', 'Web Application'),
    ]

    # Core identity
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    summary = models.CharField(max_length=300, help_text="One-sentence summary shown on the projects grid.")
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)

    # Rich detail fields — enter one item per line for list rendering in templates
    business_problem = models.TextField()
    tools_used = models.TextField(help_text="One tool per line.")
    key_features = models.TextField(help_text="One feature per line.")
    my_role = models.TextField()
    biggest_challenge = models.TextField()
    what_i_learned = models.TextField()

    # Media — all optional
    screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    video_url = models.URLField(blank=True, help_text="YouTube or Vimeo URL for iframe embed.")
    downloadable_file = models.FileField(upload_to='downloads/', blank=True, null=True)

    # Optional links
    github_link = models.URLField(blank=True)
    live_demo_link = models.URLField(blank=True)

    # Display control
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})

    def tools_list(self):
        return [t.strip() for t in self.tools_used.splitlines() if t.strip()]

    def features_list(self):
        return [f.strip() for f in self.key_features.splitlines() if f.strip()]


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, help_text="e.g. Technical Skills, Soft Skills")

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.subject} — {self.name} ({self.timestamp:%Y-%m-%d})"
