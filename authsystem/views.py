from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from . forms import SignUpForm, LoginForm, UserInProfile, ProfileForm
from . models import CustomUser, UserProfile
from post_management.models import Post, Category
from django.db.models import Count
from django.core.management import call_command


def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migration applied")

def home(request):

    # featured projects
    posts = Post.objects.all().order_by("-created_at")[:6]

    if request.user.is_authenticated:
        user_obj = request.user
        user_post = Post.objects.filter(created_by=user_obj).order_by("-created_at")
    else:
        user_obj = None
        user_post = Post.objects.none()  # Empty queryset

    categorylist= Category.objects.annotate(post_count = Count("posts"))
    categoryinfo = []
    for category in categorylist:
        categoryinfo.append({
            "id": category.id,
            "name": category.name,
            "slug": category.slug,
            "post_count": category.post_count,
        })

    context = {
        "posts": posts,
        "user_post": user_post,
        "categories": categoryinfo
    }
    return render(request, "home.html", context)


def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return JsonResponse({"message" : "success"})
        else:
            return JsonResponse({"alert" : form.errors})
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form" : form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username = username, password = password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return JsonResponse({"alert": "user is not exists"})
            
        else:
            return JsonResponse({"alert": "Invalid username or password "})
    else:
        form = LoginForm()
    return render(request, "login.html", {"form" : form})
            
@login_required
def user_logout(request):
    logout(request)
    return redirect("user_login")

@login_required
def view_profile(request, pk):

    get_profile_data = UserProfile.objects.select_related("user")
    user_obj = get_object_or_404(CustomUser, id = pk )
    user_profile = get_object_or_404(UserProfile, user = user_obj)

    user_data= []
    
    for data in get_profile_data:
        user_data.append({
            "user" : data.user,
        })
    
    user_post = Post.objects.filter(created_by = user_obj).order_by("-created_at")


    return render(request, "view_profile.html", {"user_data": user_data, "profile_user" : user_obj, "profile" : user_profile, "user_posts" : user_post})

@login_required
def edit_profile(request):
    try:
        profile_instance = request.user.profile
    except UserProfile.DoesNotExist:
        profile_instance = None

    if request.method == "POST":

        user_data_form = UserInProfile(request.POST, request.FILES, instance = request.user)
        profile_data_form = ProfileForm(request.POST, instance= profile_instance)

        if user_data_form.is_valid() and profile_data_form.is_valid():
            user_data_form.save()

            # return redirect("view_profile", request.user.id)
        
            if not profile_instance:
                profile_obj = profile_data_form.save(commit=False)
                profile_obj.user = request.user
                profile_obj.save()
            else:
                profile_data_form.save()
           
            return JsonResponse({"message": "success"})
        else:
              
            
            return JsonResponse({
                "user-error" :  user_data_form.errors if user_data_form.errors else  "No error",
                "profile-error" : profile_data_form.errors if profile_data_form.errors else "No error",

            })
    else:
        user_data_form = UserInProfile(instance = request.user)
        profile_data_form = ProfileForm(instance= profile_instance)

    return render(request, "edit_profile_info.html" ,{"user_form": user_data_form, "profile_form": profile_data_form} )