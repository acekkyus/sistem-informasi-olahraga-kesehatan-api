from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    ActivityViewSet,
    WorkoutProgramViewSet,
    DietPlanViewSet,
    HealthRecordViewSet,
    ReminderViewSet,
)

router = DefaultRouter()

router.register(r'activities', ActivityViewSet)
router.register(r'workout-programs', WorkoutProgramViewSet)
router.register(r'diet-plans', DietPlanViewSet)
router.register(r'health-records', HealthRecordViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]