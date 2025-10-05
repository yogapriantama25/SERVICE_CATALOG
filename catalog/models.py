from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Kategori")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori"
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="services",
        verbose_name="Kategori"
    )
    name = models.CharField(max_length=200, verbose_name="Nama Layanan")
    description = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Deskripsi",
        help_text="Penjelasan singkat layanan"
    )
    users = models.CharField(
        max_length=255, 
        verbose_name="Pengguna",
        help_text="Target pengguna layanan (Dosen, Mahasiswa, Staf, dsb.)"
    )
    request_method = models.CharField(
        max_length=255, 
        verbose_name="Cara Request",
        help_text="Jalur untuk request (Helpdesk IT, Portal Helpdesk, Website PMB, dll.)"
    )
    sla = models.CharField(
        max_length=255, 
        verbose_name="SLA",
        help_text="Respon & waktu penyelesaian (Respon 30 menit, selesai 1 jam, dll.)"
    )
    pic = models.CharField(
        max_length=100, 
        verbose_name="PIC",
        help_text="Tim penanggung jawab (Tim Infrastruktur, Tim Aplikasi, Tim Support, dll.)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktif")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Layanan"
        verbose_name_plural = "Layanan"
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"
