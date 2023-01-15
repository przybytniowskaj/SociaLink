from django.test import TestCase

from core.models import *

class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username='kotek', email='kotek@gmail.com', password='kot123')
        self.user1.save()
        self.profil1 = Profile.objects.create(
            user = self.user1,
            id_user = 1,
            name= 'Kasia',
            surname= 'Kot',
            email = 'kotek@gmail.com',
        )
        self.profil1.save()
        self.post1 = Post.objects.create(user = 'kotek', description='')
        self.post1.save()
        self.like1 = LikePost.objects.create(post_id=self.post1.id, username='kotek')
        self.like1.save()
        self.followers1 = Followers.objects.create(follower='ja', user='kotek')
        self.followers1.save()
        self.comment1 = Comment.objects.create(post_id = self.post1.id, username='kotek', text='blabla')
        self.comment1.save()

    def test__str__post(self):
        self.assertEquals(str(self.post1), self.post1.user)

    def test__str__profile(self):
        self.assertEquals(str(self.profil1), 'kotek')

    def test__str__likePost(self):
        self.assertEquals(str(self.like1), 'kotek')
    
    def test__str__follow(self):
        self.assertEquals(str(self.followers1), 'kotek')

    def test__str__comment(self):
        self.assertEquals(str(self.comment1), 'kotek')
        
