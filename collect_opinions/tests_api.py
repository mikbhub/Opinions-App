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
    endpoint = reverse('collect_opinions:feedback-create')

    fake = Factory.create()
    email = fake.safe_email()
    name = fake.name()

    def setUp(self):
        """
        Creates single customer instance in the database.
        """
        Customer.objects.create(
            email=self.email,
            name=self.name,
        )
        print(self.name, self.email)

    def test_create_new_feedback_customer_not_in_database(self):
        """
        Should create new `feedback` in the database and assign it
        to the `customer` identified by `email`.
        """
        fake = Factory.create()
        data = {
            "customer": {
                "email": fake.safe_email(),
                "name": fake.name()
            },
            "text": fake.text(),
            "source_type": "tests",
            "source_url": "test_url"
        }
        response = self.client.post(self.endpoint, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Feedback.objects.count(), 1)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.last(), Feedback.objects.get().customer)

    def test_create_new_feedback_customer_already_in_database(self):
        """
        Should create new `feedback` in the database,
        create new `customer` in the database and assign
        newly created `feedback` to the `customer`.
        """
        # reuses email and name for customer from setUp()
        fake = Factory.create()
        data = {
            "customer": {
                "email": self.email,
                "name": self.name
            },
            "text": fake.text(),
            "source_type": "tests",
            "source_url": "test_url"
        }
        response = self.client.post(self.endpoint, data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            msg=f"""
            Wrong response status! at {self.endpoint}.
            Response: {response.data}.
            email: {self.email}.
            name: {self.name}.
            """
        )
        self.assertEqual(Customer.objects.count(), 1, msg='Cusomer count does not match.')
        self.assertEqual(Feedback.objects.count(), 1, msg='Feedback count does not match.')
        self.assertEqual(Customer.objects.get(), Feedback.objects.get().customer)


class TestListFeebacks(APITestCase):
    """
    Test module for api/feedbacks/ endpoint.
    Ensure we can list all feedbacks from the database using this endpoint.
    """

    def setUp(self):
        """
        Create few sample feedbacks in the database.
        """
        fake = Factory.create()
        email1 = fake.safe_email()
        email2 = fake.safe_email()
        name1 = fake.name()
        name2 = fake.name()
        text1 = fake.text()
        text2 = fake.text()
        text3 = fake.text()

        Feedback.objects.create_feedback_from_Form_or_Api(
            email=email1,
            name=name1,
            text=text1,
            source_type='tests',
        )

        Feedback.objects.create_feedback_from_Form_or_Api(
            email=email2,
            name=name2,
            text=text2,
            source_type='tests',
        )

        Feedback.objects.create_feedback_from_Form_or_Api(
            email=email2,
            name=name2,
            text=text3,
            source_type='tests',
        )
    
    def test_list_all_feedbacks(self):
        """
        Shoud list all feedbacks from the database.
        """
        feedbacks_in_database = Feedback.objects.count()
        url = reverse('collect_opinions:feedbacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], feedbacks_in_database)
