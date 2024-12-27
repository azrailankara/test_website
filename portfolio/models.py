from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome ikon kodu (örn: fab fa-python)", blank=True, null=True)
    icon_image = models.ImageField(upload_to='skills/', blank=True, null=True, help_text="Özel ikon resmi")
    level = models.IntegerField(default=80, help_text="Yetenek seviyesi (0-100)")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(Skill)
    order = models.IntegerField(default=0, help_text="Sıralama için kullanılır")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    logo = models.ImageField(upload_to='companies/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.position} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, help_text="Genel Akademik Not Ortalaması (GANO)")
    logo = models.ImageField(upload_to='education/', null=True, blank=True)
    
    def __str__(self):
        return f"{self.degree} in {self.field} from {self.institution}"
    
    class Meta:
        ordering = ['-start_date']

class About(models.Model):
    title = models.CharField(max_length=200, default="Android Developer")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    cv_file = models.FileField(upload_to='cv/', blank=True)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField(blank=True)
    
    def __str__(self):
        return "Hakkımda"
    
    class Meta:
        verbose_name_plural = "About"
