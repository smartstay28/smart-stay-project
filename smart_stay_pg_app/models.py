from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Admin(models.Model):
    # Fields (columns) are defined as class attributes
    
    name = models.CharField(max_length=100, verbose_name="Admin Name")

    admin_id = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Admin ID / Username"
    )

    email = models.EmailField(
        unique=True,
        verbose_name="Email Address"
    )

    password = models.CharField(
        max_length=128,           # long enough for hashed passwords
        verbose_name="Password (hashed)"
    )

    contact_number = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Contact Number"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Is Active"
    )

    def __str__(self):
        return f"{self.name} ({self.admin_id})"

    def set_password(self, raw_password):
        """Use this to set password - never set it directly!"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Use this to verify password during login"""
        return check_password(raw_password, self.password)

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Admins"
        ordering = ['name']

class UserInfo(models.Model):
    user_id = models.AutoField(
        primary_key=True
    )

    user_name = models.CharField(
        max_length=100,
        null=False,
        verbose_name="User Name"
    )

    contact_no = models.CharField(
        max_length=15,
        null=False,
        verbose_name="Contact Number"
    )

    email = models.EmailField(
        unique=True,
        null=False,
        verbose_name="Email Address"
    )

    user_password = models.CharField(
        max_length=128,
        null=False,
        verbose_name="Password (hashed)"
    )

    id_number = models.IntegerField(
        unique=True,
        null=False,
        verbose_name="ID Number"
    )

    def __str__(self):
        return f"{self.user_name} ({self.user_id})"

    def set_password(self, raw_password):
        self.user_password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.user_password)

    class Meta:
        db_table = "user_info"
        verbose_name = "User Info"
        verbose_name_plural = "User Info"
    
class PaymentInfo(models.Model):
    payment_id = models.AutoField(
        primary_key=True
    )

    payment_type = models.CharField(
        max_length=50,
        null=False,
        verbose_name="Payment Type"
    )

    payment_date = models.DateField(
        null=False,
        verbose_name="Payment Date"
    )

    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='payments'
    )

    def __str__(self):
        return f"Payment {self.payment_id} - {self.payment_type}"

    class Meta:
        db_table = "payment_info"
        verbose_name = "Payment Info"
        verbose_name_plural = "Payment Info"

class FeedbackInfo(models.Model):
    feedback_id = models.AutoField(
        primary_key=True
    )

    feedback_date = models.DateField(
        null=False,
        verbose_name="Feedback Date"
    )

    feedback_desc = models.TextField(
        null=False,
        verbose_name="Feedback Description"
    )

    rating = models.IntegerField(
        null=False,
        verbose_name="Rating"
    )

    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='feedbacks'
    )

    def __str__(self):
        return f"Feedback {self.feedback_id} - Rating {self.rating}"

    class Meta:
        db_table = "feedback_info"
        verbose_name = "Feedback Info"
        verbose_name_plural = "Feedback Info"

class NotificationInfo(models.Model):
    notifi_id = models.AutoField(
        primary_key=True
    )

    service_name = models.CharField(
        max_length=80,
        null=False,
        verbose_name="Service Name"
    )

    end_time = models.TimeField(
        null=False,
        verbose_name="End Time"
    )

    description = models.CharField(
        max_length=255,
        null=False,
        verbose_name="Description"
    )

    def __str__(self):
        return f"{self.service_name} - {self.end_time}"

    class Meta:
        db_table = "notification_info"
        verbose_name = "Notification Info"
        verbose_name_plural = "Notification Info"

class RoomInfo(models.Model):
    room_id = models.AutoField(
        primary_key=True
    )

    room_type = models.CharField(
        max_length=50,
        null=False,
        verbose_name="Room Type"
    )

    room_floor = models.IntegerField(
        null=False,
        verbose_name="Room Floor"
    )

    capacity = models.IntegerField(
        null=False,
        verbose_name="Capacity"
    )

    available_room = models.IntegerField(
        null=False,
        verbose_name="Available Rooms"
    )

    def __str__(self):
        return f"{self.room_type} (Floor {self.room_floor})"

    class Meta:
        db_table = "room_info"
        verbose_name = "Room Info"
        verbose_name_plural = "Room Info"

class RoomBookingInfo(models.Model):
    booking_id = models.AutoField(
        primary_key=True
    )

    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='bookings'
    )

    room = models.ForeignKey(
        'RoomInfo',
        on_delete=models.CASCADE,
        db_column='room_id',
        related_name='bookings'
    )

    booking_date = models.DateField(
        null=False,
        verbose_name="Booking Date"
    )

    def __str__(self):
        return f"Booking {self.booking_id} - User {self.user.user_name} - Room {self.room.room_type}"

    class Meta:
        db_table = "room_booking_info"
        verbose_name = "Room Booking Info"
        verbose_name_plural = "Room Booking Info"

class VehicalInfo(models.Model):
    vehical_id = models.AutoField(
        primary_key=True
    )

    vehical_type = models.CharField(
        max_length=50,
        null=False,
        verbose_name="Vehical Type"
    )

    vehical_number = models.CharField(
        max_length=20,
        null=False,
        unique=True,
        verbose_name="Vehical Number"
    )

    rto_number = models.CharField(
        max_length=20,
        null=False,
        unique=True,
        verbose_name="RTO Number"
    )

    def __str__(self):
        return f"{self.vehical_type} - {self.vehical_number}"

    class Meta:
        db_table = "vehical_info"
        verbose_name = "Vehical Info"
        verbose_name_plural = "Vehical Info"

class VehicalBookingInfo(models.Model):
    booking_id = models.AutoField(
        primary_key=True
    )

    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='vehical_bookings'
    )

    vehical = models.ForeignKey(
        'VehicalInfo',
        on_delete=models.CASCADE,
        db_column='vehical_id',
        related_name='vehical_bookings'
    )

    booking_date = models.DateField(
        null=False,
        verbose_name="Booking Date"
    )

    pickup_date = models.DateTimeField(
        null=False,
        verbose_name="Pickup Date & Time"
    )

    return_time = models.DateTimeField(
        null=False,
        verbose_name="Return Date & Time"
    )

    def __str__(self):
        return f"Vehical Booking {self.booking_id} - {self.vehical.vehical_number}"

    class Meta:
        db_table = "vehical_booking_info"
        verbose_name = "Vehical Booking Info"
        verbose_name_plural = "Vehical Booking Info"

class ComplaintInfo(models.Model):
    complaint_id = models.AutoField(
        primary_key=True,
        verbose_name="Complaint ID"
    )

    user = models.ForeignKey(
        'UserInfo',
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='complaints',
        verbose_name="User"
    )

    message = models.TextField(
        null=False,
        verbose_name="Complaint Message"
    )

    date = models.DateField(
        null=False,
        verbose_name="Date"
    )

    def __str__(self):
        return f"Complaint {self.complaint_id} by {self.user.user_name}"

    class Meta:
        db_table = "complaint_info"
        verbose_name = "Complaint Info"
        verbose_name_plural = "Complaint Info"