from django.core.mail import send_mail
from rest_framework import generics, permissions
from rest_framework import filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from .models import BookModels, BlogPostSubscription, Profile
from .serializers import BookSerializer, BlogPostSerializer, FilterList, LoginSerializer, SignupSerializer, Subscribe
from Book_Store.settings import EMAIL_HOST_USER

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = BookModels.objects.filter(is_available=True)
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllBookList(generics.ListAPIView):
    queryset = BookModels.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class AddBook(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookDetail(generics.RetrieveAPIView):
    queryset = BookModels.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class BookDelete(generics.DestroyAPIView):
    queryset = BookModels.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class BookUpdate(generics.UpdateAPIView):
    queryset = BookModels.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class User_Blog_Search(generics.ListAPIView):
    queryset = BookModels.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs['username']
        return BookModels.objects.filter(user__username=user)


class SortedBookList(generics.ListAPIView):
    queryset = BookModels.objects.all()
    serializer_class = FilterList
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['title', 'category', 'iso', 'about_book', 'published']
    search_fields = ['category']


class SignUp(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
                                     context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['templates']
        login(request, user)
        return Response('You Login Successfully')


class Subscribes(APIView):
    queryset = BlogPostSubscription.objects.all()
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = Subscribe(data=request.data)
        response = Subscribe(data=request.data.get('email'))
        Email = str(response.initial_data)
        to_mail = [Email]
        send_mail('Blog Post Admin',
                  'Assalomu alaykum xurmatli mijoz, siz bizni blog postlarimizga obuna bo’ldingiz va tez orada biz '
                  'sizga eng yaxshi postlarimizni yuboramiz',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=to_mail,
                  fail_silently=False
                  )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)