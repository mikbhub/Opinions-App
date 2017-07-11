from collect_opinions.models import Feedback, Customer
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    customer_url = serializers.HyperlinkedIdentityField(view_name="collect_opinions:customer-detail")
    class Meta:
        model = Customer
        # fields = '__all__'
        fields = (
            "name",
            "email",
            'customer_url',
        )


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    # customer = serializers.StringRelatedField(many=False)
    customer_name = serializers.ReadOnlyField(source='customer.name')
    customer_email = serializers.ReadOnlyField(source='customer.email')
    customer = serializers.HyperlinkedRelatedField(view_name="collect_opinions:customer-detail", read_only=True)

    class Meta:
        model = Feedback
        fields = [
            'customer_name',
            'customer_email',
            "customer",
            "source",
            "date",
            "text",
        ]
