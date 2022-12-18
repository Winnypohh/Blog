from django.test import TestCase
from myblog.models import Post


class TestAppModels(TestCase):

    def test_model_str(self):

        title = Post.objects.create(title="Django Testing")
        content = Post.objects.create(content="Test")
        self.assertEqual(str(title), "Django Testing")
