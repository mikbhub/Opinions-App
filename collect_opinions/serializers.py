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

    customer_name = serializers.ReadOnlyField(source='customer.name')
    customer_email = serializers.ReadOnlyField(source='customer.email')
    customer = serializers.HyperlinkedRelatedField(
        view_name="collect_opinions:customer-detail",
        read_only=True,
        # queryset=Customer.objects.all(),
    )

    class Meta:
        model = Feedback
        fields = [
            'customer_name',
            'customer_email',
            "customer",
            "source_type",
            "source_url",
            "date",
            "text",
        ]


class CustomerRawSerializer(serializers.Serializer):
    """
    QuickFix to ommit email `unique` constraint on `customer`.
    """
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=True)


class FeedbackCreateSerializer(serializers.ModelSerializer):

    """
    A nested writtable serializer with explicit create() method.
    Takes care of customer creation if not already in the database.
    """

    customer = CustomerRawSerializer()

    class Meta:
        model = Feedback

        fields = [
            # 'customer_name',
            # 'customer_email',
            "customer",
            "source_type",
            "source_url",
            "date",
            "text",
        ]

    # explicit create() method
    def create(self, validated_data):
        customer = validated_data.pop('customer')
        email = customer['email']
        name = customer['name']
        return Feedback.objects.create_feedback_from_Form_or_Api(
            name=name,
            email=email,
            **validated_data,
        )
