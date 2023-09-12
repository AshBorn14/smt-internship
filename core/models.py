from django.db import models
import uuid


GENDER_CHOICES = [
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Prefer not to say")
]

STAGE_CHOICES = [
    ("Ideation", "Ideation"),
    ("Proof of Concept", "Proof of Concept"),
    ("Prototype Development", "Prototype Development"),
    ("MVP", "Minimum Viable Product (MVP)"),
    ("In Market", "In Market"),
    ("Product-Market-Fit", "Product-Market-Fit"),
    ("Growth", "Growth")
]

class Application(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    startup_name = models.CharField(max_length=150,)
    founder_name = models.CharField(max_length=100, help_text="<span class='form-text text-muted'><small>Please enter name without honorific such as Mr./Ms.</small></span>")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    qualifications = models.CharField(max_length=120)
    contact_number = models.BigIntegerField(help_text="<span class='form-text text-muted'><small>Please enter the number without +91</small></span>")
    email_id = models.EmailField(max_length=100, help_text="<span class='form-text text-muted'><small>This Email will be used for further communications</small></span>")
    institution_attended = models.CharField(max_length=120, blank=True, null=True)
    founders_experience = models.TextField(blank=True, null=True)
    product_name = models.CharField(max_length=120, blank=True, null=True)
    brief_description = models.TextField()
    incorporation_date = models.DateField(help_text="<span class='form-text text-muted'><small>Please enter date in yyyy-mm-dd format</small></span>")
    incorporation_certificate = models.FileField(upload_to="incorp_cert/", max_length=300, null=True, default=None, blank=True, help_text="<span class='form-text text-muted'><small>Please upload pdf file of size less than 200KB</small></span>")
    website = models.URLField(max_length=300, help_text="<span class='form-text text-muted'><small>Please enter your website full url</small></span>")
    address_of_company = models.TextField()
    company_sector = models.CharField(max_length=400)
    technology_area = models.CharField(max_length=300)
    company_stage = models.CharField(max_length=120, choices=STAGE_CHOICES)
    target_market = models.TextField()
    usp = models.TextField()
    revenue_streams = models.TextField(null=True,blank=True)
    pitchdeck = models.FileField(upload_to="pitchdeck/", max_length=300, null=True, default=None, blank=True, help_text="<span class='form-text text-muted'><small>Please upload pdf file of size less than 200KB</small></span>")
    isAccepted = models.BooleanField(default=False)
    isRejected = models.BooleanField(default=False)
    infoVerified = models.BooleanField(default=True)

