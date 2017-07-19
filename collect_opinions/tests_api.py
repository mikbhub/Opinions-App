from pprint import pprint

from django.urls import reverse
from rest_framework import status
# from rest_framework.request import Request
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from .models import Customer, Feedback
from .serializers import CustomerSerializer, FeedbackSerializer


# from myproject.apps.core.models import Account

# class CustomerTests(APITestCase):
#     def test_create_customer(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('collect_opinions:customers')
#         self.assertEqual(url, '/collect_opinions/api/customers/')
#         data = {
#             # "customer_url": "http://127.0.0.1:8110/collect_opinions/api/customers/1",
#             "email": "albergiza@mail.com",
#             "name": "Albert Giza"
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         url = reverse('collect_opinions:customer-detail', kwargs={'pk': 1})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # # data = {'name': 'DabApps'}
#         # # response = self.client.get('/users/4/')
#         self.assertEqual(response.data, {
#             "customer_url": "http://127.0.0.1:8110/collect_opinions/api/customers/1",
#             "email": "albergiza@mail.com",
#             "name": "Albert Giza",
#         }
#         )
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), 1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')


        # response = self.client.get('/users/4/')
# self.assertEqual(response.data, {'id': 4, 'username': 'lauren'})


class TestGetSingleCustomer(APITestCase):
    """ Test module for GET single customer API """

    def setUp(self):
        self.customer1 = Customer.objects.create(
            name="Albert Giza",
            email="albergiza@mail.com",
        )

    def test_get_valid_single_customer(self):
        factory = APIRequestFactory()
        request = factory.get('/')
        # client = APIClient()
        response = self.client.get(reverse('collect_opinions:customer-detail', kwargs={'pk': self.customer1.pk}))
        customer1 = Customer.objects.get(pk=self.customer1.pk)
        serializer = CustomerSerializer(instance=customer1, context={'request': request})
        # self.assertTrue(serializer.is_valid())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print('response.data:')
        pprint(response.data)
        print('serializer.data:')
        pprint(serializer.data)
        self.assertEqual(response.data, serializer.data)

    def test_get_invalid_single_customer(self):
        response = self.client.get(reverse('collect_opinions:customer-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class TestCreateSingleCustomer(APITestCase):
    """ Test module for creatin single customer using API """

    # def setUp(self):
    #     self.customer1 = Customer.objects.create(
    #         name="Albert Giza",
    #         email="albergiza@mail.com",
    #     )


    def test_create_customer(self):
        """
        Ensure we can create a new customer object.
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

    # def test_get_valid_single_customer(self):
    #     factory = APIRequestFactory()
    #     request = factory.get('/')
    #     # client = APIClient()
    #     response = self.client.get(reverse('collect_opinions:customer-detail', kwargs={'pk': self.customer1.pk}))
    #     customer1 = Customer.objects.get(pk=self.customer1.pk)
    #     serializer = CustomerSerializer(instance=customer1, context={'request': request})
    #     # self.assertTrue(serializer.is_valid())
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data, serializer.data)

    # def test_get_invalid_single_customer(self):
    #     response = self.client.get(reverse('collect_opinions:customer-detail', kwargs={'pk': 30}))
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

