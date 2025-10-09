from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from rest_framework import status, mixins, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from .filters import PostFilter

# @api_view(["GET","POST"])
# @permission_classes([IsAuthenticated])
# def post_list_view(request):
#     if request.method == "GET":
#         posts = Post.objects.filter(status=True)
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# class PostListView(APIView):
#     """
#     Getting a list of posts and create a new post
#     """
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     def get(self,request):
#         """
#         Retrieving a list of posts
#         """
#         posts = Post.objects.filter(status=True)
#         serializer = self.serializer_class(posts,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         """
#         Create a new post
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

# class PostListView(GenericAPIView):
#     permission_classes = ([IsAuthenticated])
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)
#     def get(self,request):
#         """
#         Retrieving a list of posts
#         """
#         queryset = self.get_queryset()
#         serializer = self.serializer_class(queryset,many=True)
#         return Response(serializer.data)
#     def post(self,request):
#         """
#         Create a new post
#         """
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


"""class PostListView(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    permission_classes = ([IsAuthenticated])
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)"""

'''class PostListView(ListCreateAPIView):
    """
    Getting a list of posts and create a new post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)'''


# @api_view(["GET","PUT","DELETE"])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_detail_view(request,id):
#     """
#     Showing detail of desire post and edit that and delete
#     """
# try:
# post = get_object_or_404(Post,id=id)
# if request.method == "GET":
#     serializer = PostSerializer(post)
#     return Response(serializer.data)
# elif request.method == "PUT":
#     serializer = PostSerializer(post, data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)
# elif request.method == "DELETE":
#     post.delete()
#     return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)
# except Post.DoesNotExist:
#     return Response({'detail':'post does not exist'},status=status.HTTP_404_NOT_FOUND)

'''class PostDetailView(APIView):
    """
    Showing detail of desire post and edit that and delete
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self,request,id):
        """
        Retrieving the post data
        """
        post = get_object_or_404(Post,id=id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self,request,id):
        """
        Editing the post data
        """
        post = get_object_or_404(Post,id=id)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,id):
        """
        Deleting the post object
        """
        post = get_object_or_404(Post,id=id)
        post.delete()
        return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)'''


"""class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)"""


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = {'author':["exact"],'category':["exact","in"]}
    search_fields = ["=title", "content", "author__user__email"]
    ordering_fields = ["published_date"]
    pagination_class = DefaultPagination
    filterset_class = PostFilter

    # @action(detail=False,methods=['get'])
    # def get_ok(self,request):
    #     return Response({'detail':'ok'})

    # def list(self,request):
    #     serializer = self.serializer_class(self.queryset, many=True)
    #     return Response(serializer.data)

    # def create(self,request):
    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def retrieve(self,request,pk=None):
    #     post = get_object_or_404(self.queryset,id=pk)
    #     serializer = self.serializer_class(post)
    #     return Response(serializer.data)

    # def update(self,request,pk=None):
    #     post = get_object_or_404(self.queryset,id=pk)
    #     serializer = self.serializer_class(post, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def partial_update(self,request,pk=None):
    #     post = get_object_or_404(self.queryset,id=pk)
    #     serializer = self.serializer_class(post, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def destroy(self,request,pk=None):
    #     post = get_object_or_404(self.queryset,id=pk)
    #     post.delete()
    #     return Response({'detail':'item removed successfully'},status=status.HTTP_204_NO_CONTENT)


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
