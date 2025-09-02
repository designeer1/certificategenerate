from django.db import models
from django.utils import timezone

TEMPLATE_TYPES = [('landscape','Landscape'),('portrait','Portrait')]

class Template(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    file = models.ImageField(upload_to='templates/')
    course = models.CharField(max_length=120)
    template_type = models.CharField(max_length=20, choices=TEMPLATE_TYPES)

    def __str__(self):
        return f"{self.name} ({self.course})"

class Student(models.Model):
    sno = models.AutoField(primary_key=True)
    hallticket = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=120)
    course = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    template = models.ForeignKey(Template, null=True, blank=True, on_delete=models.SET_NULL)
    # last generated certificate for quick access
    last_certificate = models.FileField(upload_to='certificates/', blank=True)

    def __str__(self):
        return f"{self.hallticket} - {self.name}"

class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
    file = models.FileField(upload_to='certificates/')
    created_at = models.DateTimeField(default=timezone.now)

class SendLog(models.Model):
    STATUS = [('SUCCESS','SUCCESS'), ('ERROR','ERROR')]
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    recipient_email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS)
    error_reason = models.TextField(blank=True)
    sent_at = models.DateTimeField(default=timezone.now)
    resend_count = models.PositiveIntegerField(default=0)
    download_count = models.PositiveIntegerField(default=0)
    attachment = models.FileField(upload_to='sent_attachments/', blank=True)

    def __str__(self):
        return f"{self.recipient_email} - {self.status} - {self.sent_at:%Y-%m-%d %H:%M}"
