import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user
    


class CustomUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=20)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class InterestCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=80, unique=True)
    category = models.ForeignKey(InterestCategory, on_delete=models.CASCADE, related_name="interests")

    def __str__(self):
        return self.name
    

class UserInterest(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'interest')

    def __str__(self):
        return f'{self.user} - {self.interest}'
    
#class BoatOwnerProfile():
    # custom_user: CustomUser
    # boat_model: string (required)
    # boat_name: string(optional)
    # boat_pes: number (required)
    # boat_location
    # crews_number (required)
    # needed
    # descriptions
    #...


#class CrewProfile():
    # custom_user: CustomUser
    # qualifications
    # description
    #...