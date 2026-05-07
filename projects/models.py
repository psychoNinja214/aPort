from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=7, default='#00ff88', help_text='Hex color for the tag')

    class Meta:
        verbose_name_plural = 'Technologies'
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('live', 'Live'),
        ('wip', 'Work in Progress'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=300, help_text='Short one-liner description')
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='live')
    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text='Lower = shown first')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title
