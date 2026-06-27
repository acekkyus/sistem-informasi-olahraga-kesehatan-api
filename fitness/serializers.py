from rest_framework import serializers
from .models import (
    Activity,
    WorkoutProgram,
    DietPlan,
    HealthRecord,
    Reminder,
)


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = '__all__'


class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = '__all__'


class HealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthRecord
        fields = '__all__'


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'