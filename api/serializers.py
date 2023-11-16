from rest_framework import serializers
from .models import BookModels, BlogPostSubscription
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModels
        fields = '__all__'


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
    )
    password = serializers.CharField(
        label="Password",
    )

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                error = 'Error: This templates and password is not available'
                raise serializers.ValidationError(error, code='authorization')
        else:
            error = 'User and password must be entered !'
            raise serializers.ValidationError(error, code='authorization')
        data['templates'] = user
        return data


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSubscription
        fields = '__all__'


class FilterList(serializers.ModelSerializer):
    class Meta:
        model = BookModels
        fields = ['id', 'title', 'category', 'iso']


class Subscribe(serializers.ModelSerializer):
    class Meta:
        model = BlogPostSubscription
        fields = '__all__'
