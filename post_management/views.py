from django.shortcuts import render, redirect, get_object_or_404
from . forms import CreatePostForm, CategoryFrom, TagsForm, CommentForm
from django.contrib.auth.decorators import login_required
from authsystem import models as authmodel
from django.db.models import Count
from django.http import JsonResponse
from . import models

# Create your views here.


@login_required
def create_tags(request):
    if request.method == "POST":
        form = TagsForm(request.POST)
        if form.is_valid():
            form.save()
            form = TagsForm()
        else:
            return JsonResponse({"alert" : form.errors})
    else:
        form = TagsForm()

    get_tags = models.Tag.objects.all()

    print(get_tags)
    return render(request, "create_tag.html", {"form": form, "tags" : get_tags} )


@login_required
def create_post(request):
    if request.method == "POST":
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            form.save_m2m()
            return redirect("post_details", slug = post.slug )

        else:
            return JsonResponse({
                "error" : form.errors
            })
    else:
        form = CreatePostForm()
    

    return render(request, "create_post.html", {"form": form})


def view_post(request):

    posts = models.Post.objects.select_related("created_by", "category").prefetch_related("tags").all().order_by("-created_by")
    post_data = []
    for post in posts:
        post_data.append(
            {
                "title" : post.title,
                "body" : post.body,
                "image" : post.image.url if post.image else None,
                "slug" : post.slug,
                "created_by" : post.created_by.first_name,
                "category" : post.category.name if post.category else None,
                "tags" : [tag.name for tag in post.tags.all()], 
                "created_at" : post.created_at,
                "updated_at" : post.updated_at,
                "views" : post.views
            }
        )
    popular_post = models.Post.objects.order_by("-views")[:3]
        
    # category view section

    categorylist= models.Category.objects.annotate(post_count = Count("posts"))
    categoryinfo = []
    for category in categorylist:
        categoryinfo.append(

            {   "id" : category.id,
                "name" : category.name,
                "slug" : category.slug,
                "post_count" : category.post_count,
            }
        )

    return render(request, "view_post.html", {"posts" : post_data, "categories" : categoryinfo, "popular_post" : popular_post})

@login_required
def post_details(request, slug):

    # get post
    post = get_object_or_404(models.Post.objects.select_related("created_by", "created_by__profile", "category").prefetch_related("tags", "liked_by"), slug=slug)
    try:
        bio = post.created_by.profile.bio
    except authmodel.UserProfile.DoesNotExist:
        bio = None
    # set post details
    post_data = {
                
                "title" : post.title,
                "body" : post.body,
                "image" : post.image.url if post.image else None,
                "slug" : post.slug,
                "created_by" : {
                    "id" : post.created_by.id,
                    "name" : f"{post.created_by.first_name} {post.created_by.last_name}",
                    "username" : post.created_by.username,
                    "bio" : bio ,
                },
                "category" : post.category.name if post.category else None,
                "tags" : [tag.name for tag in post.tags.all()], 
                "created_at" : post.created_at,
                "updated_at" : post.updated_at,
                "views" : post.views,
            }
    post.views +=1
    post.save()

    if post.liked_by.filter(id = request.user.id):
        is_liked = True
    else:
        is_liked = False


    # related post==> category
    related_posts = models.Post.objects.filter(category = post.category).exclude(id = post.id)
    related_post_data = []
    for post in related_posts:

        related_post_data.append(
            {
                "title" : post.title,
                "body" : post.body,
                "image" : post.image.url if post.image else None,
                "slug" : post.slug,
                "created_by" : post.created_by.first_name,
                "category" : post.category.name if post.category else None,
                "tags" : [tag.name for tag in post.tags.all()], 
                "created_at" : post.created_at,
                "updated_at" : post.updated_at,
            }
        )
    # create comments

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commented_by = request.user
            comment.post = post
            comment.save()
            form = CommentForm()
            return redirect("post_details", slug = post.slug)
        else:
            return JsonResponse({"alert" : form.errors})
    else:
        form = CommentForm()
    
    
    # get and set comments
    comments_obj = post.comments.all().select_related("commented_by")
    comments_data = []
    for comment in comments_obj:
        comments_data.append(
            {
                "id" : comment.id,
                "body" : comment.body,
                "commented_at" : comment.commented_at,
                "updated_at" : comment.updated_at,
                "commented_by" : comment.commented_by,
            }
        )


    # data passing 
    context = {
        "form" : form,
        "post_data" : post_data,
        "liked" : is_liked,
        "related_post_data" : related_post_data,
        "comments" : comments_data,
        "slug" : slug,
    
    }

    return render(request, "post_details.html", context)

    

@login_required
def post_category_filter(request, slug):

    category = models.Category.objects.get(slug = slug)
    posts = models.Post.objects.filter(category = category)

    post_data = []
    for post in posts:
        post_data.append(
            {
                "title" : post.title,
                "body" : post.body,
                "image" : post.image.url if post.image else None,
                "slug" : post.slug,
                "created_by" : post.created_by.first_name,
                "category" : post.category.name if post.category else None,
                "tags" : [tag.name for tag in post.tags.all()], 
                "created_at" : post.created_at,
                "updated_at" : post.updated_at,
            }
        )
    categorylist= models.Category.objects.annotate(post_count = Count("posts"))
    categoryinfo = []
    for category in categorylist:
        categoryinfo.append(

            {   "id" : category.id,
                "name" : category.name,
                "slug" : category.slug,
                "post_count" : category.post_count,
            }
        )

        

    return render(request, "view_post.html", {"category" : category, "posts" : post_data, "categories" : categoryinfo} )

@login_required
def view_category(request):

    if request.method == "POST":
        form = CategoryFrom(request.POST)
        if form.is_valid():
            form.save()
            form = CategoryFrom()
        else:
            return JsonResponse({"alert" : form.errors})
    else:
        form = CategoryFrom()

    get_category= models.Category.objects.all()
    categoryinfo = []
    for category in get_category:
        categoryinfo.append(

            {   "id" : category.id,
                "name" : category.name,
                "slug" : category.slug,
            }
        )
    return render(request, "category_view_form.html", {"form" : form , "categories" : categoryinfo})

@login_required
def edit_comment(request, pk, slug):
    comment = get_object_or_404(models.Comment, id = pk)
    post = get_object_or_404(models.Post, slug = slug)

    if request.user != comment.commented_by:
        return JsonResponse({"alert" : "You're not allow to edit this comment"}, status = 403)
    else:
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect("post_details", slug = comment.post.slug)
            else:
                return JsonResponse({"alert" : form.errors}, status = 400)
        else:

            form = CommentForm()

        return render(request, "edit_comment.html", {"form" : form, "post" : post})
    
def about(request):

    return render(request, "about.html")

def contact(request):

    return render(request, "contact_me.html")
    

def edit_post(request, slug):

    get_post = models.Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=get_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect("post_details", slug = get_post.slug)
        else:
            return JsonResponse({"alert": form.errors})
    else:
        form = CreatePostForm(instance=get_post)

    context = {
        "form" : form,
        "post" : get_post
    }
    
    return render(request, "edit_post.html", context)
            
def delete_post(request, slug):
    get_post = get_object_or_404(models.Post.objects.select_related("created_by"), slug = slug)

    if request.method == 'POST':
        get_post.delete()
        return redirect("view_post")
    context = {
        "post" : get_post
    }
    return render(request, "confirm_delete.html", context)



            

def liked_post(request, slug):
    post = models.Post.objects.get(slug = slug)

    if post.liked_by.filter(id = request.user.id).exists():
        post.liked_by.remove(request.user.id)
    else:
        post.liked_by.add(request.user.id)
        
    return redirect("post_details", slug=post.slug)
