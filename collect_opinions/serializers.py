from collect_opinions.models import Feedback, Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "name",
            "email"
        )


class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    customer = serializers.StringRelatedField(many=False)

    class Meta:
        model = Feedback
        fields = (
            "customer",
            "source",
            "date",
            "text",
        )
