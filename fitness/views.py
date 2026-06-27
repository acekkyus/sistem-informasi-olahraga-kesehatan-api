from rest_framework import viewsets

from .models import (
    Activity,
    WorkoutProgram,
    DietPlan,
    HealthRecord,
    Reminder,
)

from .serializers import (
    ActivitySerializer,
    WorkoutProgramSerializer,
    DietPlanSerializer,
    HealthRecordSerializer,
    ReminderSerializer,
)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class WorkoutProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer


class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer


class HealthRecordViewSet(viewsets.ModelViewSet):
    queryset = HealthRecord.objects.all()
    serializer_class = HealthRecordSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer