# filters.py
import django_filters
from .models import Draft


class DraftModelFilter(django_filters.FilterSet):
    # 定义要用于搜索的字段和搜索类型
    title = django_filters.CharFilter(lookup_expr="icontains")
    content = django_filters.CharFilter(lookup_expr="icontains")
    author = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Draft
        fields = ["title", "content", "author", "description"]
