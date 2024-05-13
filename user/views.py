from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
from rest_framework import status, generics
from .models import Profile, Transaction, Identified, MoneyOutNetbo, MoneyOutBnb, Strength_bnb, Strength_netbo, Level_bnb, Level_netbo, Exchange
from drf_yasg.utils import swagger_auto_schema
from .serialazers import (
    ProfileSerializer, 
    ProfilesingupSerialazer, 
    ProfileLoginserialazer, 
    UpdateProfileSerializer, 
    ProfileRefeleshSerialazer,
    VerificationCodeserialazer,
    GMProfileserialazer, 
    UpdatePasswordSerializer, 
    Tranzaktionserialazer, 
    UpdateEmPsSerializer,
    MoneyOutBnbserialazer, 
    MoneyOutNetboserialazer,
    CreatMoneyOutNetboserialazer,
    CreatMoneyOutBnbserialazer, 
    IdentifiedSerializer, 
    exchangeserialazers,
    StrengthBnbSerialazer,
    StrengthNetboSerialazer,
    LevelBnbSerialazer,
    LevelNetboSerialazer,
    
)
import time, calendar
from django.db.models import Sum
import random, string
from datetime import datetime
from datetime import date, timedelta
from django.shortcuts import get_list_or_404, get_object_or_404


# gmail######
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

globals
code_lis = {}

def generate_random_string(length=10):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))

def send_email(subject, body, to_email):
    # Gmail pochtangiz va parolingizni kiriting
    gmail_user = 'netboxollc@gmail.com'
    gmail_password = "rfqdwyoszfrfoczl"

    # Xabar tayyorlash
    message = MIMEMultipart()
    message['From'] = gmail_user
    message['To'] = to_email
    message['Subject'] = subject

    # Xabarning matnini qo'shish
    message.attach(MIMEText(body, 'html'))

    # SMTP serveriga ulanish
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(gmail_user, gmail_password)

        # Xabarni yuborish
        server.sendmail(gmail_user, to_email, message.as_string())
#####


@swagger_auto_schema(method='PATCH', operation_description="Tiklamoqchi bo'lgan profilning ID sini kirting!")
@api_view(['PATCH'])
def send_otp(request, email):
    if request.method == 'PATCH':
        try:
            # Agar email bo'yicha profili topish mumkin bo'lsa
            profile = Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            try:
                # Agar email bo'yicha topilmagan bo'lsa, username bo'yicha izlash
                profile = Profile.objects.get(username=email)
            except Profile.DoesNotExist:
                # Agar username bo'yicha ham topilmagan bo'lsa, xato qaytarish
                return Response({'message': -2 }, status=status.HTTP_400_BAD_REQUEST)
        six_digit_number = generate_random_string()
        gmail = str(profile.email)
        massag =f"""
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    color: #333;
                }}
                .password-message {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #f4f4f4;
                    border-radius: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="password-message">
                <p>Password Recovery - MinerUP</p>
                <p>Your new login password: <strong>{six_digit_number}</strong></p>
                <p>After that, you can only log in with this password.</p>
                <p>If this is not you, please contact us immediately.</p>
            </div>
        </body>
        </html>
    """
        send_email("Password",massag, gmail)
        profile.password = six_digit_number
        profile.save()
        return Response({'message': 1 },status=status.HTTP_200_OK)
    else:
        return Response({'message': -1 },status=status.HTTP_400_BAD_REQUEST)
        
@swagger_auto_schema(method='PATCH', request_body=VerificationCodeserialazer, operation_description="Tiklamoqchi bo'lgan profilning ID sini kirting!")
@api_view(['PATCH'])
def confirmation_otp(request):
    if request.method == 'PATCH':
        code = request.data.get("code")
        if code in code_lis.keys():
            del code_lis[code]
            return Response({'message': 1 }, status=status.HTTP_200_OK)
        else:
            return Response({'message': -2 },status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({'message': -1 },status=status.HTTP_400_BAD_REQUEST)
    

    
@swagger_auto_schema(method='PATCH', request_body=UpdatePasswordSerializer, operation_description="Parolni o'zgartirish uchun so'rov")
@api_view(['PATCH'])
def update_password(request, email):
    profile = get_object_or_404(Profile, email=email)
    serializer = UpdatePasswordSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    new_password = serializer.validated_data['password']
    profile.password = new_password
    profile.save()
    return Response({'message': 1 }, status=status.HTTP_200_OK)
    
class UpdateProfileAPIView(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    queryset = Profile.objects.all()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        new_username = serializer.validated_data.get('username')
        if Profile.objects.filter(username=new_username).exclude(id=instance.id).exists():
            return Response({'message': -4}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        instance.refresh_from_db()
        return Response({'message': 1, "profile": ProfileSerializer(instance).data}, status=status.HTTP_200_OK)
    
@swagger_auto_schema(method='PATCH', request_body=UpdateEmPsSerializer, operation_description="Yangilamaoqchi bo'lgan Profilening ID sini kirting")
@api_view(['PATCH'])
def update_email_password(request, pk):
    profile = get_object_or_404(Profile, id=pk)
    data = UpdateEmPsSerializer(instance=profile, data=request.data)
    data.is_valid(raise_exception=True)
    new_email = data.validated_data.get('email')
    if Profile.objects.filter(email=new_email).exclude(id=pk).exists():
        return Response({'message': -4}, status=status.HTTP_400_BAD_REQUEST)
    data.save()
    profile.refresh_from_db()
    serializer = ProfileSerializer(profile)
    return Response({'message': 1, "profile": serializer.data}, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PATCH', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['PATCH'])
def verify_email(request, pk):
    if request.method == 'PATCH':
        try:
            profile = Profile.objects.get(id=pk)
        except:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        is_data = int(time.time())
        profile.is_verified = is_data
        profile.save()
        return Response({'message': 1}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='POST', request_body=ProfilesingupSerialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    email = request.data.get('email')
    # Profil ma'lumotlarini bir marta olish
    existing_profiles = Profile.objects.filter(username=username) | Profile.objects.filter(email=email)
    # Profil ma'lumotlarini tekshirish
    if existing_profiles.exists():
        return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
    serializer = ProfileSerializer(data=request.data)
    # Serializer ma'lumotlarini tekshirish
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 1, "profile": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile(request):
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile_id(request, pk):
    if request.method == 'GET':
        profile = Profile.objects.get(id=pk)
        serializer = ProfileSerializer(profile)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_profile_username(request, username):
    if request.method == 'GET':
        profile = Profile.objects.get(username=username)
        serializer = ProfileSerializer(profile)
        return Response({'message': 1,"profile":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='POST', request_body=ProfileLoginserialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        profile = Profile.objects.get(username=username)
    except:
        return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)   
    if profile.password == password:
        profile_serializer = ProfileSerializer(profile)
        return Response({'message': 1, "profile":profile_serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)

    
@swagger_auto_schema(method='DELETE', operation_description="O'chirmoqchi bo'lgan Profileni ID sini kirting")
@api_view(['DELETE'])
def delete_profile(request, pk):
    if request.method == 'DELETE':
        try:
            praduct = Profile.objects.get(id=pk)
        except:
            return Response({'message': -2 },status=status.HTTP_400_BAD_REQUEST)
        praduct.delete()
        return Response({'message':1},status=status.HTTP_200_OK)
    else:
        return Response({'message': -1 },status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(method='PATCH', request_body=ProfileRefeleshSerialazer, operation_description="Referal_link")
@api_view(['PATCH'])
def activate_referral_link(request, pk):
    if request.method == 'PATCH':
        referal = request.data.get('referal_link')
        try:
            frend = Profile.objects.get(referal_link=referal)
        except:
            return Response({'message': -2}, status=status.HTTP_400_BAD_REQUEST)
        profile = Profile.objects.get(id=pk)
        if frend.is_identified == True:
            link = frend.referal_link
            profile.friend_referal_link = link
            profile.save()
            return Response({'message': 1}, status=status.HTTP_200_OK)
        else:
            return Response({'message': -3}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    
    
@swagger_auto_schema(method='POST', operation_description="Ball berladigan profile ID sini kirting")
@api_view(['POST'])
def ad_reward_netbo(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    if profile.netbo_level != None:
        profile.balance_netbo += profile.netbo_level.netbo
        profile.save()
        return Response({'message': 1},status=status.HTTP_200_OK)
    else:
        try:
            level = Level_netbo.objects.get(level = 1)
        except:
            return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
        profile.balance_netbo += level.netbo
        profile.save()
        return Response({'message': 1},status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='POST', operation_description="Ball berladigan profile ID sini kirting")
@api_view(['POST'])
def ad_reward_bnb(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    if profile.bnb_level != None:
        profile.balance_bnb += profile.bnb_level.bnb
        profile.save()
        return Response({'message': 1},status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def balance_history(request, pk):
    current_timestamp = int(time.time())
    current_date = datetime.utcfromtimestamp(current_timestamp).date()

    dey_sum = 0
    days_in_month = calendar.monthrange(current_date.year, current_date.month)[1]
    moon_sum = [0] * days_in_month
    week_sum = [0] * 7
    profile = Profile.objects.get(id=pk)
    username_id = profile.id

    all_transactions = Transaction.objects.filter(user=username_id)

    # Kunlik tranzaksiyalar
    daily_transactions = all_transactions.filter(
        created_at__gte=current_timestamp - 86400,
        created_at__lt=current_timestamp
    )
    dey_sum = daily_transactions.aggregate(Sum('balance_netbo'))['balance_netbo__sum'] or 0

    # Haftalik tranzaksiyalar
    weekly_transactions = all_transactions.filter(
        created_at__gte=current_timestamp - (86400 * 7),
        created_at__lt=current_timestamp
    )
    week_sum = [0] * 7  # Reset week_sum
    for transaction in weekly_transactions:
        transaction_date = datetime.utcfromtimestamp(transaction.created_at).date()
        day_of_week = transaction_date.weekday()
        week_sum[day_of_week] += transaction.balance_netbo

    # Oylik tranzaksiyalar
    oylik_transactions = all_transactions.filter(
        created_at__gte=current_timestamp - (86400 * days_in_month),
        created_at__lt=current_timestamp
    )
    moon_sum = [0] * days_in_month  # Reset moon_sum
    for transaction in oylik_transactions:
        transaction_date = datetime.utcfromtimestamp(transaction.created_at).date()
        day_of_month = transaction_date.day - 1
        moon_sum[day_of_month] += transaction.balance_netbo

    return Response({'message': 1, 'daily': dey_sum, "weekly": week_sum, 'monthly': moon_sum}, status=status.HTTP_200_OK)
    
    

@swagger_auto_schema(method='POST', request_body=IdentifiedSerializer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def upload_image(request, pk):
    serializer = IdentifiedSerializer(data=request.data)
    if  serializer.is_valid():
        profile = Profile.objects.get(id=pk)
        profile.is_identified = None
        profile.save()
        serializer.save(user_id=pk)
        return Response({'message': 1, 'data': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_identified_id(request, pk):
    if request.method == 'GET':
        profile = Identified.objects.get(id=pk)
        serializer = IdentifiedSerializer(profile)
        return Response({'message': 1,"Identified":serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='POST', request_body=CreatMoneyOutNetboserialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def moneyout_netbo(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    stf = get_object_or_404(Strength_netbo, id = 1).money_out
    if stf == True and profile.netbo_out == True:
        taim = int(time.time())
        wallet_address = request.data.get('wallet_addres')
        balance_netboo = request.data.get('balance_netbo')
        data = {"wallet_addres":wallet_address, "user":profile.id, "balance_netbo":balance_netboo, "created_at":taim}
        ser = MoneyOutNetboserialazer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        profile.balance_netbo -= balance_netboo
        profile.save()
        return Response({'message': 1,"data":ser.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1,}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_moneyout_netbo_id(request, pk):
    if request.method == 'GET':
        moneyouts = MoneyOutNetbo.objects.filter(user=pk)
        serializer = MoneyOutNetboserialazer(moneyouts, many=True)
        return Response({'message': 1, "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='POST', request_body=CreatMoneyOutBnbserialazer, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def moneyout_bnb(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
    stf = get_object_or_404(Strength_bnb, id = 1).money_out
    if stf == True and profile.bnb_out == True:
        taim = int(time.time())
        wallet_address = request.data.get('wallet_addres')
        balance_bnb = request.data.get('balance_bnb')
        data = {"wallet_addres":wallet_address, "user":profile.id, "balance_bnb":balance_bnb, "created_at":taim}
        ser = MoneyOutNetboserialazer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        profile.balance_netbo -= balance_bnb
        profile.save()
        return Response({'message': 1,"data":ser.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1,}, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_moneyout_bnb_id(request, pk):
    if request.method == 'GET':
        moneyouts = MoneyOutBnb.objects.filter(user=pk)
        serializer = MoneyOutBnbserialazer(moneyouts, many=True)
        return Response({'message': 1, "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_level_bnb_id(request, pk):
    if request.method == 'GET':
        try:
            moneyouts = Level_bnb.objects.get(id=pk)
        except:
            return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LevelBnbSerialazer(moneyouts)
        return Response({'message': 1, "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_level_netbo_id(request, pk):
    if request.method == 'GET':
        try:
            moneyouts = Level_netbo.objects.get(id=pk)
        except:
            return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)
        serializer = LevelNetboSerialazer(moneyouts)
        return Response({'message': 1, "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'message': -1}, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_strength_netbo(request):
    strength = Strength_netbo.objects.get(id=1)
    serializer = StrengthNetboSerialazer(strength)
    return Response({'message': 1,"strength":serializer.data}, status=status.HTTP_200_OK)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def get_strength_bnb(request):
    strength = Strength_bnb.objects.get(id=1)
    serializer = StrengthBnbSerialazer(strength)
    return Response({'message': 1,"strength":serializer.data}, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PATCH',request_body=exchangeserialazers, operation_description="profile ID sini kirting")
@api_view(['PATCH'])
def exchange(request, pk):
    if request.method == 'PATCH':
        try:
            profile = Profile.objects.get(id=pk)
        except:
            return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)   
        bnb = request.data.get('bnb')
        balanc_bnb = profile.balance_bnb
        try:
            exchange = Exchange.objects.get(id = 1)
        except:
            return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)  
        if bnb <= balanc_bnb:
            profile.balance_bnb -= bnb
            profile.balance_netbo += (exchange.value * bnb)
            profile.save()
            return Response({'message': 1},status=status.HTTP_200_OK)
        else:
            return Response({'message': -2},status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': -1},status=status.HTTP_400_BAD_REQUEST)
