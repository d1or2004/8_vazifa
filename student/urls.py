from django.urls import path
from .views import StudentView, LendingWive,UserRigisterView,LoginView

urlpatterns = [
    path('student/', StudentView.as_view(), name='student'),
    path('', LendingWive.as_view(), name='landing'),
    path('auth/register/', UserRigisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
]
