from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import random
User._meta.get_field('email').blank=True
User._meta.get_field('email')._unique=False

from django.core.validators import FileExtensionValidator
from cloudinary_storage.storage import VideoMediaCloudinaryStorage, MediaCloudinaryStorage, RawMediaCloudinaryStorage
#from cloudinary_storage.validators import validate_video


class Boshqarma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    domain = models.CharField(max_length=1000, null=True, blank=True)
    # nizom = models.FileField(null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(null=True, blank=True, max_length=100)
    telegram = models.CharField(null=True, blank=True, max_length=1000)
    instagram = models.CharField(null=True, blank=True, max_length=1000)
    facebook = models.CharField(null=True, blank=True, max_length=1000)
    twitter = models.CharField(null=True, blank=True, max_length=1000)
    youtube = models.CharField(null=True, blank=True, max_length=1000)
    youtube_videos = ArrayField(
        models.CharField(max_length=1000), size=100,null=True, blank=True
    )
    video1 = models.URLField(null=True, blank=True)
    video2 = models.URLField(null=True, blank=True)
    video2_text = models.CharField(max_length=1000, null=True, blank=True)
    video3 = models.URLField(null=True, blank=True)
    video3_text = models.CharField(max_length=1000, null=True, blank=True)
    text_p = models.TextField(null=True, blank=True)
    text_p_ism = models.CharField(max_length=1000, null=True, blank=True)
    image_p = models.ImageField(null=True, blank=True, upload_to="frontend_videos", storage=MediaCloudinaryStorage())
    text_afzallik_1 = models.CharField(max_length=1000, null=True, blank=True)
    text_afzallik_2 = models.CharField(max_length=1000, null=True, blank=True)
    text_afzallik_3 = models.CharField(max_length=1000, null=True, blank=True)
    text_afzallik_4 = models.CharField(max_length=1000, null=True, blank=True)
    params = ArrayField(
        models.DecimalField(max_digits=12, decimal_places=9), size=2,
    )
    fotos = ArrayField(
        models.CharField(max_length=1000), size=100,null=True, blank=True
    )
    manzil = models.CharField(max_length=500, null=True, blank=True)


    statistics_tuman_bulim = models.IntegerField(null=True, blank=True)
    statistics_maktab = models.IntegerField(null=True, blank=True)
    statistics_talim_tillari = models.IntegerField(null=True, blank=True)
    statistics_pupils = models.IntegerField(null=True, blank=True)
    statistics_teachers = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Boshqarma"
        verbose_name_plural = "Boshqarmalar"

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    full_name = models.CharField(max_length=180, null=True, blank=True)
    image_region = models.ImageField(default="default.jpg", upload_to="region_images", null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to="region_mudir_images", null=True, blank=True)
    video = models.URLField(null=True, blank=True)
    phone =  models.CharField(null=True, blank=True, max_length=100)
    telegram = models.CharField(null=True, blank=True, max_length=1000)
    instagram = models.CharField(null=True, blank=True, max_length=1000)
    facebook = models.CharField(null=True, blank=True, max_length=1000)
    email = models.CharField(null=True, blank=True, max_length=1000)
    youtube = models.CharField(null=True, blank=True, max_length=1000)
    domain = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name

class Foto_lavhalar(models.Model):
    foto_lavha = models.ImageField(upload_to="Boshqarma_images")

    def __str__(self):
        return f'{self.id}'
    
    @property
    def FotoURL(self):
        return self.foto_lavha.url

class Speciality(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.name

class Rahbariyat(models.Model):
    full_name = models.CharField(max_length=120)
    spec = models.ForeignKey(Speciality, on_delete=models.CASCADE, null=True, blank=True)
    qabul = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=70)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(default="default.jpg", upload_to="rahbariyat_images")


    class Meta:
        verbose_name = "Rahbariyat"
        verbose_name_plural = "Rahbariyat a'zolari"

    def __str__(self):
        return self.full_name

class News(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="news")
    date_added = models.DateField(null=True, blank=True)
    # boshqarma = models.ForeignKey(Boshqarma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

    def __str__(self):
        return f"{self.name}"

class Hujjatlar(models.Model):
    CHOICE_LEVEL = [
        (1, 1),
        (2, 2),
        (3, 3),
    ]
    title = models.CharField(max_length=3000)
    type = models.IntegerField(choices=CHOICE_LEVEL, default=1)
    link = models.URLField()

    def __str__(self):
        return self.title

class Events(models.Model):

    image = models.ImageField(null=True, upload_to="events_images")
    title = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    #published_time = models.DateField( null=True, blank=True)
    text = models.TextField(null=True)
    # boshqarma = models.ForeignKey(Boshqarma, on_delete=models.CASCADE, null=True)

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Murojaat(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=60)
    text = models.TextField()
    date_sent = models.DateField()
    seen = models.BooleanField(default=False)
    # boshqarma = models.ForeignKey(Boshqarma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Murojaat"
        verbose_name_plural = "Murojaatlar"

    def __str__(self):
        return self.name

def generation_code():
    code = ''
    for i in range(0, 6):
        code +=''.join(str(random.randint(0, 9)))
    if code == '':
        return generation_code()
    print("code: ", code)
    return code


class Verification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(default=generation_code, max_length=6)

    class Meta:
        verbose_name="Verification"
        verbose_name_plural = "Verifications"

    def __str__(self):
        return f"{self.user.username} - {self.code}"

class Presentations(models.Model):
    name =  models.CharField(max_length=520)
    file = models.FileField(upload_to="presentations")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Presentation"
        verbose_name_plural = "Presentations"


class Projects(models.Model):
    name =  models.CharField(max_length=520)
    file = models.FileField(upload_to="projects")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    download = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Project"
        verbose_name_plural = "Projects"

class Comments(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    comment = models.TextField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
    
    def __str__(self):
        return self.email
