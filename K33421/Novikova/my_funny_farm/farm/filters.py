from django_filters import rest_framework as filters
from .models import *


class ChickenEggFilter(filters.FilterSet):
    egg_amount = filters.RangeFilter()
    ordering = filters.OrderingFilter(
        fields=(
            ('egg_amount', 'egg_amount'),
        ))

    class Meta:
        model = Chicken
        fields = ['egg_amount']
