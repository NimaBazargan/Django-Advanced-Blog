from django_filters import rest_framework as filters
from blog.models import Post


class PostFilter(filters.FilterSet):
    min_time = filters.DateFilter(field_name="published_date", lookup_expr="gte")
    max_time = filters.DateFilter(field_name="published_date", lookup_expr="lte")

    class Meta:
        model = Post
        fields = ["category", "title"]
