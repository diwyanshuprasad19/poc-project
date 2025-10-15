from django.db import models
from datetime import datetime


class PatientKeyarMonitoringSession(models.Model):
    """
    Represents a hospital monitoring session for a patient (JFH).
    """
    patient_id = models.IntegerField()
    place_id = models.IntegerField(default=0)
    worker_id = models.IntegerField(default=0)
    name = models.CharField(max_length=100, blank=True, default="")
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"JFH Session {self.id} - Patient {self.patient_id}"


class PatientKeyarDataSet(models.Model):
    """
    Represents a processed dataset in a JFH session.
    """
    patient_id = models.IntegerField()
    monitoring_session = models.ForeignKey(
        PatientKeyarMonitoringSession, on_delete=models.CASCADE, related_name="datasets"
    )
    data_time = models.DateTimeField(default=datetime.now)
    doctor_interpretation = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, default="CREATED")

    def __str__(self):
        return f"JFH Dataset {self.id} - Patient {self.patient_id}"


class PatientKeyarDataSetParam(models.Model):
    """
    Represents parameter data linked to a JFH dataset.
    """
    dataset = models.ForeignKey(
        PatientKeyarDataSet, on_delete=models.CASCADE, related_name="params"
    )
    param_type = models.CharField(max_length=50)
    data_set = models.JSONField(default=dict)
    meta_data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.param_type} - Dataset {self.dataset_id}"


# ==============================
# 📱 JFM Monitoring (Consumer / App Side)
# ==============================
class KeyarMonitoringSession(models.Model):
    """
    Represents a user's monitoring session in the JFM app.
    """
    patient_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, default="")
    category = models.CharField(max_length=100, default="KEYAR_DATA")
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, default="STARTED")
    serial_number = models.CharField(max_length=100, blank=True, default="")

    def __str__(self):
        return f"JFM Session {self.id} - Patient {self.patient_id}"


class KeyarDataset(models.Model):
    """
    Represents dataset data for a JFM monitoring session.
    """
    keyar_monitoring_session = models.ForeignKey(
        KeyarMonitoringSession, on_delete=models.CASCADE, related_name="datasets"
    )
    data_time = models.DateTimeField(default=datetime.now)
    doctor_interpretation = models.TextField(blank=True, default="")
    status = models.CharField(max_length=50, default="STARTED")
    params_data = models.JSONField(default=dict)
    files = models.JSONField(default=list)  # replaced ArrayField for portability

    def __str__(self):
        return f"JFM Dataset {self.id} - Session {self.keyar_monitoring_session_id}"
