from django.db import models
import uuid, random, string

def generate_random_string(length=7):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))



class Level_netbo(models.Model):
    level = models.IntegerField(default=0)
    netbo = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.level)


class Level_bnb(models.Model):
    level = models.IntegerField(default=0)
    bnb = models.FloatField(default=0)
    price = models.FloatField(default=0)

    def __str__(self) -> str:
        return str(self.level)

class Profile(models.Model):
    email = models.EmailField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    name = models.CharField(max_length=200, blank=True, null=True)
    surname = models.CharField(max_length=250, blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    referal_link = models.CharField(max_length=8, default=generate_random_string, unique=True, editable=False)
    number_people = models.IntegerField(default=0)
    balance_netbo = models.FloatField(default=0.0)
    wallet_id_netbo = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    netbo_out = models.BooleanField(default=True)
    netbo_level = models.ForeignKey(Level_netbo, null=True, blank=True, on_delete=models.SET_NULL)
    balance_bnb = models.FloatField(default=0.0)
    wallet_id_bnb = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    bnb_out = models.BooleanField(default=True)
    bnb_level = models.ForeignKey(Level_bnb, null=True, blank=True, on_delete=models.SET_NULL)
    is_identified = models.BooleanField(default=False,null=True, blank=True)
    is_verified = models.IntegerField(null=True, blank=True)
    friend_referal_link = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.username


class Transaction(models.Model):
    balance_netbo = models.FloatField(default=0.0)
    balance_bnb = models.FloatField(default=0.0)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.IntegerField()


class Identified(models.Model):
    fullname = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    birthday = models.CharField(max_length=250)
    serial_document = models.CharField(max_length=255)
    id_image = models.ImageField(upload_to='identified/')
    address_image = models.ImageField(upload_to='identified/')
    selfie_image = models.ImageField(upload_to='identified/')
    is_identified = models.BooleanField(null=True, blank=True)


class MoneyOutNetbo(models.Model):
    wallet_addres = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    balance_netbo = models.FloatField(default=0.0)
    is_identified = models.BooleanField(null=True, blank=True)
    created_at = models.IntegerField()

class MoneyOutBnb(models.Model):
    wallet_addres = models.CharField(max_length=200)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    balance_bnb = models.FloatField(default=0.0)
    is_identified = models.BooleanField(null=True, blank=True)
    created_at = models.IntegerField()

    

class Strength_netbo(models.Model):
    referal_netbo = models.FloatField(default=0)
    max_out = models.FloatField(default=0, null=True, blank=True)
    min_out = models.FloatField(default=0, null=True, blank=True)
    commission = models.FloatField(default=0, null=True, blank=True)
    level_netbo = models.ManyToManyField(Level_netbo)
    taim = models.IntegerField(default=0)
    money_out = models.BooleanField(default=True)


class Strength_bnb(models.Model):
    referal_bnb = models.FloatField(default=0)
    max_out = models.FloatField(default=0, null=True, blank=True)
    min_out = models.FloatField(default=0, null=True, blank=True)
    commission = models.FloatField(default=0, null=True, blank=True)
    level_bnb = models.ManyToManyField(Level_bnb)
    taim = models.IntegerField(default=0)
    money_out = models.BooleanField(default=True)


class Exchange(models.Model):
    value = models.FloatField()


    

