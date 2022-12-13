from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, User_form, Profile_form
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect



# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def userProfile(request, userid):

    my_profile = Profile.objects.all().filter(user_id=userid)
    return render(request, 'userapp/profile.html', {'profile_details':my_profile})


@login_required
@transaction.atomic
def editUserProfile(request, userid):
    if request.method == "POST":
        user = get_object_or_404(User, id=userid)
        user_form = User_form(request.POST, instance=user)
        profile_form = Profile_form(request.POST or None, request.FILES or None, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            if profile_form.cleaned_data ["staff"]:
                user.is_staff = True
                user.save()
                
            else:
                user.is_staff = False
                user.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponsePermanentRedirect(reverse("profile", args=(userid)))
        
        else:
            messages.error(request, ('Please correct the error below'))
            return HttpResponsePermanentRedirect(reverse('edit_profile', args=(userid, )))


    else:
        user = get_object_or_404(User, id=userid)
        user_form = User_form(instance=user)
        profile_form = Profile_form(instance=user.profile)
        return render(request, 'userapp/edit_profile_form.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


@login_required
def deactivateProfile(request, userid):
    myprofile = User.objects.get(id=userid)
    if myprofile.is_active == True:
        User.objects.only("is_active").filter(id=userid).update("is_active=False")
        Profile.objects.only("status").filter(id=userid).update("is_active=False")
    else:
        User.objects.only("is_active").filter(id=userid).update("is_active=False")
        Profile.objects.only("status").filter(id=userid).update(status="Active")

    return HttpResponsePermanentRedirect(reverse("profile", args=(userid,)))


@login_required
def displayStaff(request):
    allStaff = User.objects.all().filter(is_staff=True)
    return render(request, "userapp/display_staff.html", {"allstaff": allStaff})

@login_required
def displayCustomer(request):
    allCustomer = User.objects.all().filter(is_staff=False)
    return render(request, "userapp/display_customer.html", {"allcustomer": allCustomer})


    