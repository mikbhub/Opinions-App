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
    customer = serializers.HyperlinkedRelatedField(
        view_name="collect_opinions:customer-detail",
        read_only=False,
        queryset=Customer.objects.all(),
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


# TODO: leave other serializers as they are and write separate serialize,
# view and named url just for POSTing new feedback.
class FeedbackCreateSerializer(serializers.ModelSerializer):

    customer = CustomerSerializer()

    class Meta:
        model = Feedback
        # TODO: define fields
        
        fields = [
            # 'customer_name',
            # 'customer_email',
            "customer",
            "source_type",
            "source_url",
            "date",
            "text",
        ]
    # TODO: implement explicit create() method
    def create(self, validated_data):
        print('Starting create()')
        print(f'Validated data: {validated_data}')
        customer = validated_data.pop('customer')
        email = customer['email']
        name = customer['name']
        return Feedback.objects.create_feedback_from_Form_or_Api(
            name=name,
            email=email,
            **validated_data
        )
        # raise NotImplementedError


# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer()

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'profile')

#     def create(self, validated_data):
#         profile_data = validated_data.pop('profile')
#         user = User.objects.create(**validated_data)
#         Profile.objects.create(user=user, **profile_data)
#         return user
