from django_dynamic_fixture import G
from django_dynamic_fixture import F
from test_plus.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse

from django.contrib.auth.models import User
from api.models import Task


# Create your tests here.
class LoginTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.data_auth = {
            'password': 'password',
            'username': 'test',
        }
        self.user = User.objects.create_user(
            email='test@example.com',
            first_name='test',
            last_name='edw',
            **self.data_auth,
        )

    def test_get_token(self):
        response = self.client.post(
            reverse('login'),
            data=self.data_auth,
        )
        self.assertTrue('token' in response.json())


class TaskTestCase(TestCase):
    def setUp(self):
        self.data_auth = {
            'password': 'password',
            'username': 'test',
        }
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            first_name='test',
            last_name='edw',
            **self.data_auth,
        )

        self.token = self.client.post(
            reverse('login'),
            data=self.data_auth,
        ).json()['token']

        self.task_description = 'test_description'
        self.task = G(Task, user=self.user, description=self.task_description)
        self.task_other = G(Task, user=F(), description=self.task_description)

        self.url_task_list = reverse('api:task-list')
        self.url_detail_task = reverse('api:task-detail', args=[self.task.id])

    def test_unauthorized(self):
        response = self.client.get(
            self.url_task_list,
        )
        self.assert_http_401_unauthorized(response)

    def test_task_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

        response = self.client.get(
            self.url_task_list,
        )
        response_json = response.json()
        self.assertTrue(self.task_description in str(response_json))

        # todo test only task for this user
        print(response_json)

    def test_task_detail_unauthorized(self):
        response = self.client.get(
            self.url_detail_task,
        )
        self.assert_http_401_unauthorized(response)

    def test_task_detail(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

        response = self.client.get(
            self.url_detail_task,
        )
        response_json = response.json()
        self.assertTrue(self.task_description == response_json['description'])
