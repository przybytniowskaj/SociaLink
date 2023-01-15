from django.test import SimpleTestCase
from django.urls import resolve, reverse
from core.views import *


class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)
    
    def test_sign_url_resolved(self):
        url = reverse('sign')
        self.assertEquals(resolve(url).func, sign)
    
    def test_signup_url_resolved(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func, signup)

    def test_signin_url_resolved(self):
        url = reverse('signin')
        self.assertEquals(resolve(url).func, signin)

    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logout)

    def test_setting_url_resolved(self):
        url = reverse('setting')
        self.assertEquals(resolve(url).func, setting)

    def test_like_post_url_resolved(self):
        url = reverse('like_post')
        self.assertEquals(resolve(url).func, like_post)

    def test_create_post_url_resolved(self):
        url = reverse('create_post')
        self.assertEquals(resolve(url).func, create_post)

    def test_follow_url_resolved(self):
        url = reverse('follow')
        self.assertEquals(resolve(url).func, follow)

    def test_comment_url_resolved(self):
        url = reverse('comment')
        self.assertEquals(resolve(url).func, comment)
    
    def test_post_delete_url_resolved(self):
        url = reverse('post_delete')
        self.assertEquals(resolve(url).func, post_delete)

    def test_search_url_resolved(self):
        url = reverse('search')
        self.assertEquals(resolve(url).func, search)
    
    def test_profile_url_resolved(self):
        url = reverse('profile', args=['przybytniowska'])
        self.assertEquals(resolve(url).func, profile)
