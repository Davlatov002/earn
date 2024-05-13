from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('get-profile/', views.get_profile, name='get-profile'),
    path('login/', views.login, name='login'),
    path('get-profile-id/<str:pk>/', views.get_profile_id, name='get-profile-id'),
    path('get-profile-username/<str:username>/', views.get_profile_username, name='get-profile-username'),
    path('update-profile/<str:pk>/', views.UpdateProfileAPIView.as_view(), name='update-profile'),
    path('update-email-password/<str:pk>/', views.update_email_password, name='update-email-password'),
    path('delete-profile/<str:pk>/', views.delete_profile, name='delete-profile'),
    path('activate-referral-link/<str:pk>/', views.activate_referral_link, name='activate-referral-link'),
    path('ad-reward-netbo/<str:pk>/', views.ad_reward_netbo, name='ad-reward-netbo'),
    path('ad-reward-bnb/<str:pk>/', views.ad_reward_bnb, name='ad-reward-bnb'),
    path('confirmation-otp/', views.confirmation_otp, name='confirmation-otp'),
    path('update-password/<str:email>/', views.update_password, name='update-password'),
    path('exchange/<str:pk>/', views.exchange, name='exchange'),
    path('send-otp/', views.send_otp, name='send-otp'),
    path('verify-email/<str:pk>/', views.verify_email, name='verify-email'),
    path('balance-history/<str:pk>/', views.balance_history, name='balance-history'),
    path('get-identified-id/<str:pk>/', views.get_identified_id, name='get-identified-id'),
    path('creat-identified/<str:pk>/', views.upload_image, name='creat-identified'),
    path("get-moneyout-netbo-id/<str:pk>/", views.get_moneyout_netbo_id, name='get-moneyout-netbo-id'),
    path("get-moneyout-bnb-id/<str:pk>/", views.get_moneyout_bnb_id, name='get-moneyout-bnb-id'),
    path("moneyout-netbo/<str:pk>/", views.moneyout_netbo, name='moneyout-netbo'),
    path("moneyout-bnb/<str:pk>/", views.moneyout_bnb, name='moneyout-bnb'),
    path("recovery-password/<str:email>/", views.send_otp, name='recovery-password'),

    path('get-strength-bnb/', views.get_strength_bnb, name='get-strength-bnb'),
    path('get-strength-netbo/', views.get_strength_netbo, name='get-strength-netbo'),

] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)