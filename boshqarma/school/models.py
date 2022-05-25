from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Region(models.Model):
    region_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200,null=True)
    admin = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.region_name

class School(models.Model):
    region = models.ForeignKey(Region,on_delete=models.CASCADE)
    type = models.CharField(max_length=255,null=True)
    school_number = models.IntegerField()
    school_name = models.CharField(max_length=200,null=True, blank=True)
    domain = models.CharField( max_length=100,null=True,blank=True, unique=True)
    admin = models.OneToOneField(User,related_name='school_admin', on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    video = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    b_r1 = models.ImageField(null=True,blank=True)
    b_c1 = models.ImageField(null=True,blank=True)
    b_c2 = models.ImageField(null=True,blank=True)
    b_c3 = models.ImageField(null=True,blank=True)
    m_h_h1 = models.ImageField(null=True,blank=True)
    m_h_h2 = models.ImageField(null=True,blank=True)
    m_h_h3 = models.ImageField(null=True,blank=True)
    m_h_h4 = models.ImageField(null=True,blank=True)
    m_h_h5 = models.ImageField(null=True,blank=True)
    m_h_navruz = models.ImageField(null=True,blank=True)
    m_h_mustaqillik = models.ImageField(null=True,blank=True)
    m_h_bitiruv = models.ImageField(null=True,blank=True)
    m_h_t = models.ImageField(null=True,blank=True)
    m_h_oshxona = models.ImageField(null=True,blank=True)
    m_h_musiqa = models.ImageField(null=True,blank=True)
    m_h_sport = models.ImageField(null=True,blank=True)
    foto = models.ImageField(null=True,blank=True)
    foto1 = models.ImageField(null=True,blank=True)
    foto2 = models.ImageField(null=True,blank=True)
    foto3 = models.ImageField(null=True,blank=True)
    foto4 = models.ImageField(null=True,blank=True)
    foto5 = models.ImageField(null=True,blank=True)
    foto6 = models.ImageField(null=True,blank=True)
    foto7 = models.ImageField(null=True,blank=True)
    q = models.ImageField(null=True,blank=True)
    m_h_axborot = models.ImageField(null=True,blank=True)
    m_h_xavfsizlik = models.ImageField(null=True,blank=True)
    m_h_tibbiyot = models.ImageField(null=True,blank=True)
    m_h_o_r = models.ImageField(null=True,blank=True)
    q_imtihon_r = models.ImageField(null=True,blank=True)

    m_h_tq = models.TextField(null=True,blank=True)
    m_h_t_t = models.TextField(null=True,blank=True)
    m_h_k_h = models.TextField(null=True,blank=True)
    m_h_k_t = models.TextField(null=True,blank=True)
    m_h_oshxona_t = models.TextField(null=True,blank=True)
    m_h_musiqa_t = models.TextField(null=True,blank=True)
    m_h_sport_t = models.TextField(null=True,blank=True)
    m_h_axborot_t = models.TextField(null=True,blank=True)
    m_h_xavfsizlik_t = models.TextField(null=True,blank=True)
    m_h_tibbiyot_t = models.TextField(null=True,blank=True)
    m_h_o = models.TextField(null=True,blank=True)
    m_h_o_t = models.TextField(null=True,blank=True)
    q_t = models.TextField(null=True,blank=True)
    q_talim = models.TextField(null=True,blank=True)
    q_bitiruv = models.TextField(null=True,blank=True)
    q_oquvchi = models.TextField(null=True,blank=True)
    q_j_online = models.TextField(null=True,blank=True)
    q_j_forma = models.TextField(null=True,blank=True)
    q_j_koz = models.TextField(null=True,blank=True)
    q_j_hujjat = models.TextField(null=True,blank=True)
    q_j_intervyu = models.TextField(null=True,blank=True)
    q_j_qaror = models.TextField(null=True,blank=True)
    q_imtihon_t = models.TextField(null=True,blank=True)
    q_oquv_yili = models.TextField(null=True,blank=True)
    q_muddat = models.TextField(null=True,blank=True)
    q_imtihon = models.TextField(null=True,blank=True)
    q_hujjat_t1 = models.TextField(null=True,blank=True)
    q_hujjat_t2 = models.TextField(null=True,blank=True)
    q_hujjat_t3 = models.TextField(null=True,blank=True)
    params = ArrayField(
        models.DecimalField(max_digits=9, decimal_places=6),
            size=2, null=True
    )


    @property
    def setname(self):
        self.school_name = f'{self.region.address} {self.region.region_name} {self.school_number} - maktab'
        if self.domain is None:
            self.domain = self.school_name
    def __str__(self):
        return f'{self.region.region_name} tumani {self.school_number} - maktab'

class Videos(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    videos = ArrayField(models.FileField(null=True, blank=True), size=120)

    def __str__(self):
        return f'{self.school.school_name}'

class Fotos(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    fotos = ArrayField(models.FileField(null=True, blank=True), size=120, null=True, blank=True)

    def __str__(self):
        return f'{self.school.school_name}'
# class Images(models.Model):
#     image =

class Spec(models.Model):
    name = models.CharField(max_length=255,null=True)
    def __str__(self):
        return self.name
class Staff(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    speciality = models.ManyToManyField(Spec,related_name='spec_id',swappable=False,null=True,blank=True)
    image = models.ImageField(null=True)
    full_name = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL,null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.user:
            return self.user.username
        else:
            return f'Staff {self.id}'
class AchievementByT(models.Model):
    speciality = models.ManyToManyField(Spec,related_name='speciality_id',swappable=False,null=True,blank=True)
    image = models.ImageField(null=True)
    full_name = models.CharField(max_length=100,null=True)
    position = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL,null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.user:
            return self.user.username
        else:
            return f'Staff {self.id}'

class New(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    published_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.title} - {self.school} - {self.published_time}"


    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Event(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    published_time = models.DateTimeField(auto_now_add=True,null=True)
    text = models.TextField(null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.title} - {self.school} - {self.address}"

    
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Course(models.Model):
    image = models.ImageField(null=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=True)
    mentor = models.ForeignKey(Staff,on_delete=models.SET_NULL,null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return f"{self.title} - {self.school} - {self.mentor}"

    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)
    spec = models.ForeignKey(Spec,on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return self.subject_name

class Excellent(models.Model):
 #   pupil = models.ForeignKey(Pupil,on_delete=models.CASCADE)
    #clas = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    clas = models.CharField(max_length=200, null=True, blank=True)
    full_name = models.CharField(max_length=255,null=True,blank=True)
    #pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    birth_day = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.school}"

class Achivement(models.Model):
    pupils = models.ManyToManyField('Excellent',blank=True)
    image = models.ImageField(null=True,blank=True)
    competition = models.CharField(max_length=255,null=True,blank=True)
    result = models.CharField(max_length=25,null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        verbose_name = 'Achievement by pupils'
        verbose_name_plural = 'Achievements by pupils'



