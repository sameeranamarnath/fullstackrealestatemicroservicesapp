from django.urls import path


from .views import HouseViewSet
from .views import CheckerView

urlpatterns=[

path('houses',HouseViewSet.as_view({
    'get':'list',
    'put':'create'
})),

path('houses/<str:pk>',HouseViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'delete': 'destroy'
    })),

path('checker', CheckerView.as_view())
  
]




