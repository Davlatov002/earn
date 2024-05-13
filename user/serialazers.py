from rest_framework import serializers
from .models import Profile, Transaction, Identified, MoneyOutNetbo, MoneyOutBnb, Strength, Level
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}  # Parolni faqat yozish uchun qo'shimcha ma'lumot qilib belgilang
        }


class ProfilesingupSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password']

class Tranzaktionserialazer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['user', 'balance_netbo', 'balance_bnb', 'created_at']

class ProfileRefeleshSerialazer(serializers.Serializer):
    referal_link = serializers.CharField()

class ProfileLoginserialazer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

class VerificationCodeserialazer(serializers.Serializer):
    code = serializers.CharField()
    
class UpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField()

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'name', 'surname', 'profile_image']

    def update(self, instance, validated_data):
        # Update each field individually
        instance.username = validated_data.get('username', instance.username)
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()

        return instance
    
class UpdateEmPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['email', 'password']

    def update(self, instance, validated_data):
        # Update each field individually
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
                                                                
        return instance

class GMProfileserialazer(serializers.Serializer):
    email = serializers.EmailField()

class IdentifiedSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Identified
        fields = '__all__'

class CreatMoneyOutNetboserialazer(serializers.Serializer):
    wallet_addres = serializers.CharField()
    balance_netbo = serializers.FloatField()

class CreatMoneyOutBnbserialazer(serializers.Serializer):
    wallet_addres = serializers.CharField()
    balance_bnb = serializers.FloatField()

class MoneyOutNetboserialazer(serializers.ModelSerializer):
    class Meta:
        model = MoneyOutNetbo
        fields = '__all__'

class MoneyOutBnbserialazer(serializers.ModelSerializer):
    class Meta:
        model = MoneyOutBnb
        fields = '__all__'

class IdentifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Identified
        fields = fields = ["fullname", "birthday", "serial_document", "id_image", "address_image", "selfie_image"]

class LevelSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = [
            'level',
            'bnb',
            'netbo', 
            'price',
            ]




class StrengthSerialazer(serializers.ModelSerializer):
    level = LevelSerialazer(many=True, read_only=True)

    class Meta:
        model = Strength
        fields = [
            'exchange',
            'referal_netbo', 
            'referal_bnb', 
            'default_netbo',
            'bnb_max_out',
            'bnb_min_out',  
            'bnb_commission', 
            'netbo_max_out',
            'netbo_min_out',  
            'netbo_commission', 
            'level', 
            'taim',
            'money_out',
            ]



class exchangeserialazers(serializers.Serializer):
    bnb = serializers.FloatField()