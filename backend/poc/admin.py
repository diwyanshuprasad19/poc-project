from django.contrib import admin
from .models import (
    PatientKeyarMonitoringSession,
    PatientKeyarDataSet,
    PatientKeyarDataSetParam,
    KeyarMonitoringSession,
    KeyarDataset,
)


@admin.register(PatientKeyarMonitoringSession)
class PatientKeyarMonitoringSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "patient_id", "place_id", "start_time", "end_time", "is_complete")
    list_filter = ("is_complete",)
    search_fields = ("patient_id", "name")


@admin.register(PatientKeyarDataSet)
class PatientKeyarDataSetAdmin(admin.ModelAdmin):
    list_display = ("id", "patient_id", "monitoring_session", "data_time", "status")
    list_filter = ("status",)
    search_fields = ("patient_id", "monitoring_session__id")


@admin.register(PatientKeyarDataSetParam)
class PatientKeyarDataSetParamAdmin(admin.ModelAdmin):
    list_display = ("id", "dataset", "param_type")
    search_fields = ("param_type", "dataset__id")


@admin.register(KeyarMonitoringSession)
class KeyarMonitoringSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "patient_id", "name", "start_time", "end_time", "status")
    list_filter = ("status",)
    search_fields = ("patient_id", "name", "serial_number")


@admin.register(KeyarDataset)
class KeyarDatasetAdmin(admin.ModelAdmin):
    list_display = ("id", "keyar_monitoring_session", "data_time", "status")
    list_filter = ("status",)
    search_fields = ("keyar_monitoring_session__id",)
