
from django.urls import path, re_path
from ecommerce.userapp import views as user_view


urlpatterns = [
    re_path(r'^profile/(?P<userid>\d+)/', user_view.userProfile , name='profile'),
    re_path(r'^user_edit_profile/(?P<userid>\d+)/', user_view.editUserProfile , name='user_edit_profile'),
    re_path(r'^my_profile/(?P<userid>\d+)/', user_view.deactivateProfile , name='my_profile'),
    re_path(r'^display_staff/', user_view.displayStaff, name='display_staff'),
    re_path(r'^display_customer/', user_view.displayCustomer, name='display_customer'),
    
    
]

