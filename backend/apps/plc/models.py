from django.db import models


class PLC(models.Model):

    MANUFACTURERS = [
        ("Mitsubishi", "Mitsubishi"),
    ]

    SERIES = [
        ("iQ-R", "iQ-R"),
    ]

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    manufacturer = models.CharField(
        max_length=50,
        choices=MANUFACTURERS,
        default="Mitsubishi",
    )

    series = models.CharField(
        max_length=50,
        choices=SERIES,
        default="iQ-R",
    )

    ip_address = models.GenericIPAddressField()

    port = models.PositiveIntegerField(
        default=1025,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        db_table = "plcs"
        ordering = ["name"]

    def __str__(self):
        return self.name



class PLCTag(models.Model):

    DATA_TYPE_CHOICES = [
        ("BOOL", "BOOL"),
        ("INT", "INT"),
        ("REAL", "REAL"),
        ("FLOAT", "FLOAT"),
        ("STRING", "STRING"),
        ("WORD", "WORD"),
        ("DWORD", "DWORD"),
    ]


    plc = models.ForeignKey(
        PLC,
        on_delete=models.CASCADE,
        related_name="tags",
    )

    name = models.CharField(
        max_length=100,
    )

    address = models.CharField(
        max_length=50,
    )

    data_type = models.CharField(
        max_length=20,
        choices=DATA_TYPE_CHOICES,
    )

    on_color = models.CharField(
    max_length=20,
    default="#22C55E",
    )

    off_color = models.CharField(
        max_length=20,
        default="#6B7280",
    )

    low_color = models.CharField(
        max_length=20,
        default="#22C55E",
    )

    medium_color = models.CharField(
        max_length=20,
        default="#FACC15",
    )

    high_color = models.CharField(
        max_length=20,
        default="#EF4444",
    )

    unit = models.CharField(
        max_length=20,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    is_writable = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:
        db_table = "plc_tags"
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["plc", "address"],
                name="unique_plc_address",
            )
        ]


    def __str__(self):
        return f"{self.plc.name} - {self.name}"



# =====================================================
# PLC TAG RUNTIME VALUE
# =====================================================

class PLCTagValue(models.Model):

    tag = models.OneToOneField(
        PLCTag,
        on_delete=models.CASCADE,
        related_name="current_value",
    )


    value = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )


    quality = models.CharField(
        max_length=50,
        default="GOOD",
    )


    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        db_table = "plc_tag_values"



    def __str__(self):

        return f"{self.tag.name}: {self.value}"



# =====================================================
# PLC OPERATION AUDIT LOG
# =====================================================

class PLCOperationLog(models.Model):

    OPERATION_CHOICES = [
        ("READ", "READ"),
        ("WRITE", "WRITE"),
    ]


    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="plc_operations",
    )


    plc = models.ForeignKey(
        PLC,
        on_delete=models.CASCADE,
        related_name="operation_logs",
    )


    tag = models.ForeignKey(
        PLCTag,
        on_delete=models.CASCADE,
        related_name="operation_logs",
    )


    operation = models.CharField(
        max_length=20,
        choices=OPERATION_CHOICES,
    )


    old_value = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )


    new_value = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
    )


    class Meta:

        db_table = "plc_operation_logs"

        ordering = [
            "-created_at"
        ]


    def __str__(self):

        return (
            f"{self.operation} "
            f"{self.tag.name}"
        )


