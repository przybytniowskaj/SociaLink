from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from core.models import *
from django.contrib.auth.models import auth
from django.core.files.uploadedfile import SimpleUploadedFile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.sign_url = reverse('sign')
        self.signup_url = reverse('signup')
        self.signin_url = reverse('signin')
        self.logout_url = reverse('logout')
        self.search_url = reverse('search')
        self.comment_url = reverse('comment')
        self.user = User.objects.create_user(username='kotek', password='kot123')
        self.user.save()
        self.user1 = User.objects.get(username='kotek')
        self.user_profile = Profile.objects.create(user=self.user1, id_user=1, email='kotek@gmail.com', name = 'Kasia', surname='Kot')
        self.post = Post.objects.create(user=self.user1, image=SimpleUploadedFile("file.txt", b"file_content"), description='Test Post')
        self.comment = Comment.objects.create(post_id=self.post.id, username=self.user1.username, text='Test comment.')
        self.image = open("static/images/background.jpg", 'rb')
        self.follower = User.objects.create_user(username='follower', password='password')

    def test_sign_get(self):
        response = self.client.get(self.sign_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sign.html')

    def test_signup_post(self):
        data = {
            'id_user' : 3,
            'name': 'k2',
            'surname': 'Kot2',
            'username' : 'kotek2',
            'email' : 'kotek2@gmail.com',
            'password' : 'kotek1223'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertEquals(Profile.objects.get(name='k2').surname, 'Kot2')
    
    def test_signup_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)

    def test_signin_post(self):
        data = {
            'username' : 'kotek',
            'password' : 'kotek123'
        }
        response = self.client.post(self.signin_url, data)
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)

    def test_index_view_with_logged_in_user(self):
        self.client.login(username='kotek', password='kot123')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user_profile'], self.user_profile)
        self.assertIn(self.comment, response.context['comments'])

    def test_index_view_with_logged_out_user(self):
        response = self.client.get(reverse('index'))
        self.assertRedirects(response, '/sign?next=/')

    def test_create_post(self):
        self.client.login(username='kotek', password='kot123')
        response = self.client.post(reverse('create_post'), {'description': 'post', 'image_upload': self.image})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(Post.objects.count(), 2)
    
    def test_like_post(self):
        self.client.login(username='kotek', password='kot123')
        response = self.client.get(reverse('like_post'), {'post_id': self.post.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(LikePost.objects.count(), 1)
        self.assertEqual(LikePost.objects.first().username, 'kotek')
        self.assertEqual(Post.objects.first().no_of_likes, 1)
        
        response = self.client.get(reverse('like_post'), {'post_id': self.post.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(LikePost.objects.count(), 0)
        self.assertEqual(Post.objects.first().no_of_likes, 0)

    def test_delete_post(self):
        self.client.login(username='kotek', password='kot123')
        response = self.client.get(reverse('post_delete'), {'post_id': self.post.id})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/')
        self.assertEqual(Post.objects.count(), 0)

    def test_follow(self):
        self.client.login(username='kotek', password='kot123')
        response = self.client.post(reverse('follow'), {'user': 'kotek', 'follower': 'follower'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/profile/kotek')
        self.assertEqual(Followers.objects.count(), 1)
        self.assertEqual(Followers.objects.first().follower, 'follower')
        self.assertEqual(Followers.objects.first().user, 'kotek')
        
        response = self.client.post(reverse('follow'), {'user': 'kotek', 'follower': 'follower'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/profile/kotek')
        self.assertEqual(Followers.objects.count(), 0)