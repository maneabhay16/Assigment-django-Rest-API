from .models import Blog, Category
from .serializer import BlogSerializer, CategorySerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import  generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class CategoryListCreateView(generics.ListCreateAPIView):
   
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   permission_classes = [IsAdminOrReadOnly]
   
   
   
   def list(self, request, *args, **kwargs):
         queryset = self.get_queryset()
         serializer = CategorySerializer(queryset, many=True, context={'request': request})
         if queryset.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
         else:
            return Response({'Message': 'No Category Found'}, status.HTTP_404_NOT_FOUND)
         

class CategorydetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   liikup_field = 'id'
   permission_classes = [IsAdminOrReadOnly]
   
   def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      
      if instance:
         return Response(serializer.data, status=status.HTTP_200_OK)
      
      else : 
         return Response({'Message': 'No Blog Found'}, status = status.HTTP_404_NOT_FOUND)
      


class BlogListCreateView(generics.ListCreateAPIView):
   queryset = Blog.objects.filter(is_public = True)
   serializer_class = BlogSerializer
   permission_classes = [IsAuthenticatedOrReadOnly]
   
   def list(self,request, *args, **kwargs):
      queryset = self.get_queryset()
      serializer = BlogSerializer(queryset, many=True, context={'request': request})
      if queryset.exists():
         return Response(serializer.data, status=status.HTTP_200_OK)
      else:
         return Response({'Message': 'No blogs found'}, status=status.HTTP_204_NO_CONTENT)
      
   
   def create(self, request, *args, **kwargs):
      serializer = BlogSerializer(data=request.data, context={'request': request})
      serializer.is_valid(raise_exception=True)
      serializer.save(author=self.request.user)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   
      

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
   queryset = Blog.objects.filter(is_public = True)
   serializer_class = BlogSerializer
   liikup_field = 'id'
   permission_classes = [IsOwnerOrReadOnly]
   
   
   def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      
      if instance:
         return Response(serializer.data, status=status.HTTP_200_OK)
      
      else : 
         return Response({'Message': 'No Blog Found'}, status = status.HTTP_404_NOT_FOUND)
 
      
      
      


   

   
      
        


