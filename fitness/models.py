from django.db import models


class Activity(models.Model):
    nama_aktivitas = models.CharField(max_length=100)
    durasi = models.PositiveIntegerField(help_text="Durasi dalam menit")
    kalori_terbakar = models.PositiveIntegerField()
    tanggal = models.DateField()

    def __str__(self):
        return self.nama_aktivitas


class WorkoutProgram(models.Model):
    nama_program = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    durasi_minggu = models.PositiveIntegerField()
    deskripsi = models.TextField()

    def __str__(self):
        return self.nama_program


class DietPlan(models.Model):
    menu = models.CharField(max_length=100)
    kalori = models.PositiveIntegerField()
    protein = models.FloatField()
    karbohidrat = models.FloatField()
    lemak = models.FloatField()
    tanggal = models.DateField()

    def __str__(self):
        return self.menu


class HealthRecord(models.Model):
    berat_badan = models.FloatField()
    tinggi_badan = models.FloatField()
    detak_jantung = models.PositiveIntegerField()
    tekanan_darah = models.CharField(max_length=30)
    tanggal = models.DateField()

    def __str__(self):
        return f"Record {self.id}"


class Reminder(models.Model):
    judul = models.CharField(max_length=100)
    waktu = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.judul

# Create your models here.
