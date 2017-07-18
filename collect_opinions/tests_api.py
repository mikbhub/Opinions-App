from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from .models import Customer
# from myproject.apps.core.models import Account

class CustomerTests(APITestCase):
    def test_create_customer(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('collect_opinions:customers')
        self.assertEqual(url, '/collect_opinions/api/customers/')
        data = {
            # "customer_url": "http://127.0.0.1:8110/collect_opinions/api/customers/1",
            "email": "albergiza@mail.com",
            "name": "Albert Giza"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # url = reverse('collect_opinions:customer-detail', kwargs={'pk': 1})
        # response = self.client.get(url)
        # # data = {'name': 'DabApps'}
        # # response = self.client.get('/users/4/')
        # self.assertEqual(response.data, {
        #     "customer_url": "http://127.0.0.1:8110/collect_opinions/api/customers/1",
        #     "email": "albergiza@mail.com",
        #     "name": "Albert Giza"
        # }
        # )
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')


        # response = self.client.get('/users/4/')
# self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})
