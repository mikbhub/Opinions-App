from pprint import pprint

from django.urls import reverse
from faker import Factory
from rest_framework import status
# from rest_framework.request import Request
from rest_framework.test import APIClient, APIRequestFactory, APITestCase

from .models import Customer, Feedback
from .serializers import CustomerSerializer, FeedbackCreateSerializer


class TestGetSingleCustomer(APITestCase):
    """ 
    Test module for GET single customer via API endpoint api/customers/
    """

    def setUp(self):
        """
        Creates sample customer using Faker
        """
        fake = Factory.create()
        self.customer1 = Customer.objects.create(
            name=fake.name(),
            email=fake.safe_email(),
        )

    def test_get_valid_single_customer(self):
        """
        Data of serialized customer should be the same as
        data obtained for the customer using api endpoint.
        """
        factory = APIRequestFactory()
        request = factory.get('/')
        response = self.client.get(reverse('collect_opinions:customer-detail', kwargs={'pk': self.customer1.pk}))
        customer1 = Customer.objects.get(pk=self.customer1.pk)
        serializer = CustomerSerializer(instance=customer1, context={'request': request})
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
    """
    Test module for creatin single customer using API endpoint api/customers/
    """

    fake = Factory.create()
    customer_data = {
        'name': fake.name(),
        'email': fake.safe_email(),
    }

    def test_create_customer(self):
        """
        Ensure we can create a new customer object.
        """
        url = reverse('collect_opinions:customers')
        self.assertEqual(url, '/collect_opinions/api/customers/')
        response = self.client.post(url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCreateAndGetSingleCustomer(APITestCase):
    """
    Test module for GET single customer API using endpoint api/customers/{pk}
    """
    fake = Factory.create()
    customer_data = {
        'name': fake.name(),
        'email': fake.safe_email(),
    }
    
    def setUp(self):
        """
        Creates new customer in the database using api endpoint.
        """
        url = reverse('collect_opinions:customers')
        self.assertEqual(url, '/collect_opinions/api/customers/')
        response = self.client.post(url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_created_customer(self):
        """
        Should get customer created in the `setUp` method
        """
        # check getting created customer with api
        factory = APIRequestFactory()
        url = reverse('collect_opinions:customer-detail', kwargs={'pk': 1})
        request = factory.get(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.customer_data.update({
            "customer_url": request.build_absolute_uri()
        })
        print('response.data:')
        pprint(response.data)
        print('customer_data:')
        pprint(self.customer_data)
        self.assertEqual(response.data, self.customer_data)


# TODO: write test for feedback creation, getting.
class TestCreateFeedback(APITestCase):
    """
    Test module for api/feedback/new endpoint
    """
    def setUp(self):
        """
        Creates single customer instance in the database.
        """
        raise NotImplementedError
    
    def test_create_new_feedback_customer_not_in_database(self):
        """
        Should create new `feedback` in the database and assign it
        to the `customer` identified by `email`.
        """
        raise NotImplementedError

    def test_create_new_feedback_customer_already_in_database(self):
        """
        Should create new `feedback` in the database,
        create new `customer` in the database and assign
        newly created `feedback` to the `customer`.
        """
        raise NotImplementedError


class TestListFeebacks(APITestCase):
    """
    Test module for api/feedbacks/ endpoint.
    Ensure we can list all feedbacks from the database using this endpoint.
    """
    
    def setUp(self):
        """
        Create few sample feedbacks in the database.
        """
        raise NotImplementedError
    
    def test_list_all_feedbacks(self):
        """
        Shoud list all feedbacks from the database.
        """
        raise NotImplementedError
