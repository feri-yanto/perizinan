from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Accounts(AbstractUser):
   email = models.EmailField(_("email address"), unique=True)
   first_name = None
   last_name = None

   class Meta:
      db_table = 'accounts'
      verbose_name = 'account'
      verbose_name_plural = 'accounts'

class ProfileModels(models.Model):
   account = models.OneToOneField(verbose_name=_('account'), to=Accounts, on_delete=models.CASCADE, editable=False)
   first_name = models.CharField(verbose_name=_('first name'), max_length=100)
   last_name = models.CharField(verbose_name=_('last name'), max_length=100, null=True, blank=True)
   nip = models.PositiveBigIntegerField(verbose_name=('NIP'), unique=True)
   nik = models.PositiveBigIntegerField(verbose_name=_('NIK'), unique=True)
   pangkat_golongan = models.CharField(verbose_name='pangkat/golongan', max_length=20)
   position = models.CharField(verbose_name=_('position'), max_length=100)
   status = models.CharField(verbose_name=_('status'), max_length=10, choices=(
      ('PNS', 'PNS'),
      ('PPPK', 'P3K'),
      ('CPNS', 'CPNS'),
   ))
   place_of_birth = models.CharField(verbose_name=_('place of birth'), max_length=50)
   date_of_birth = models.DateField(verbose_name=_('date of birth'))
   gender = models.CharField(verbose_name=_('gender'), max_length=10, choices=(
      ('pria', 'laki-laki'),
      ('perempuan', 'perempuan'),
   ))
   religion = models.CharField(verbose_name=_('religion'), max_length=10, choices=(
      ('islam', 'ISLAM'),
      ('kristen', 'KRISTEN'),
      ('hindu', 'HINDU'),
      ('budha', 'BUDHA'),
      ('konghuchu', 'KONGHUCHU'),
   ))
   institution = models.CharField(verbose_name='institution', max_length=200)

   class Meta:
      db_table = 'account_profiles'
      verbose_name = 'profile'
      verbose_name_plural = 'profiles'

   def __str__(self):
      return f'{self.first_name} {self.last_name}'