from itertools import chain
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from core.models import Followers, Post, Profile, LikePost, Comment
from django.core.mail import EmailMessage
from django.conf import settings

@login_required(login_url='sign')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all().order_by('created_at')
    comments = Comment.objects.all()
    return render(request, 'index.html', {'user_profile': user_profile, 'posts' : posts, 'comments' : comments})

@login_required(login_url='sign')
def setting(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST" :
        if request.FILES.get('profile_img') == None:
            image = user_profile.profile_img
            bio = request.POST['bio']
            location = request.POST['location']
            phone = request.POST['phone']

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.phone = phone
            user_profile.save()
        else:
            image = request.FILES.get('profile_img')
            bio = request.POST['bio']
            location = request.POST['location']
            phone = request.POST['phone']

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.phone = phone
            user_profile.save()
        return redirect("/")
    return render(request,'settings.html', {'user_profile': user_profile})

def sign(request):
    return render(request, 'sign.html')

def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('signup')
        else:
            html = "Dear " + name + ", <br><br> Thank you for creating a new user account with our service. "
            html += "Your account has been successfully created and is now ready for use. <br>"
            html += "<br> Thank you for choosing our service. <br> If you have any questions or need assistance, "
            html += "please don't hesitate to contact us. <br><br> Sincerely,<br> SociaLink"
            msg = EmailMessage('User Creation Confirmation', html, settings.EMAIL_HOST_USER, [email,])
            msg.content_subtype = "html"
            msg.send()
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name,last_name=surname)
            user.save()
            user_login = auth.authenticate(username=username, password=password)
            auth.login(request, user_login)
            user_model = User.objects.get(username=username)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, name=name, surname=surname, email=email)
            new_profile.save()
            return redirect('setting')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Login or Password is incorrect.")
            return redirect('signin')
    else:
        return render(request, 'signin.html')

@login_required(login_url='sign')
def logout(request):
    auth.logout(request)
    return redirect('sign')

@login_required(login_url='sign')
def create_post(request):
    if request.method == "POST":
        user=request.user.username
        image=request.FILES.get("image_upload")
        description = request.POST['description']
        new_post = Post.objects.create(user=user, image= image, description=description)
        new_post.save()
        return redirect("/")
    else:
        return redirect("/")

@login_required(login_url='sign')
def like_post(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)
    like_filter = LikePost.objects.filter(post_id=post_id, username=username).first()
    if like_filter:
        like_filter.delete()
        post.no_of_likes -=1
        post.save()
        return redirect("/")
    else:
        new_like = LikePost.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes += 1
        post.save()
        return redirect("/")

@login_required(login_url='sign')
def post_delete(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('/')

@login_required(login_url='sign')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    no_post = len(user_posts)
    user_logged = Profile.objects.get(user=request.user)
    follower = request.user.username
    user = pk

    if Followers.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'
    followers = len(Followers.objects.filter(user=pk))
    following = len(Followers.objects.filter(follower=pk))
        
    return render(request, 'profile.html', {'user_object' : user_object,
    'user_profile': user_profile, 'user_posts': user_posts, 'no_post':no_post,
     'user_logged' : user_logged, 'button_text' : button_text, 'followers': followers,
      'following' : following})

@login_required(login_url='sign')
def follow(request):
    if request.method == "POST":
        follower = request.POST['follower']
        user = request.POST['user']

        if Followers.objects.filter(follower=follower, user=user).first():
            Followers.objects.filter(follower=follower, user=user).delete()
            return redirect('/profile/' + user)
        else:
            new_follow = Followers.objects.create(follower=follower, user=user)
            new_follow.save()
            return redirect('/profile/' + user)
    else:
        return redirect("/")

def comment(request):
    username = request.user.username
    post_id = request.GET.get('post_id')
    if request.method == "POST":
        text = request.POST['text']
        new_comment = Comment.objects.create(post_id=post_id, username=username, text = text)
        new_comment.save()
        return redirect('/')
    else:
        return redirect('/')

@login_required(login_url='sign')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        search = request.POST['username']
        username_object = User.objects.filter(username__icontains=search)

        username_profile = []
        username_profile_list = []

        for users in username_object:
            username_profile.append(users.id)

        for ids in username_profile:
            profile_lists = Profile.objects.filter(id_user=ids)
            username_profile_list.append(profile_lists)
        
        
        username_profile_list = list(chain(*username_profile_list))
    return render(request, 'search.html', {'username' : search,'user_profile': user_profile, 'username_profile_list': username_profile_list})