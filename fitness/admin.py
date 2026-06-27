from django.contrib import admin

from .models import (
    Activity,
    WorkoutProgram,
    DietPlan,
    HealthRecord,
    Reminder,
)

admin.site.register(Activity)
admin.site.register(WorkoutProgram)
admin.site.register(DietPlan)
admin.site.register(HealthRecord)
admin.site.register(Reminder)