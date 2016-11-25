from django.db import models
#from multiselectfield import MultiSelectField

DOW = (('1', 'Sunday'),
      ('2', 'Monday'),
      ('3', 'Tuesday'),
      ('4', 'Wednesday'),
      ('5', 'Thursday'),
      ('6', 'Friday'),
      ('7', 'Saturday'))

class Course(models.Model):
    course_name = models.CharField(blank=False, null=False, max_length=250)
    course_slug = models.SlugField(unique=True)
    course_description = models.TextField(blank=False, null=False)
    course_start_time = models.TimeField(blank=False, null=False)
    course_end_time = models.TimeField(blank=False, null=False)
    #course_days_of_week = MultiSelectField(choices=DOW)
    course_days_of_week = models.CharField(max_length=1, choices=DOW)
    course_all_day = models.BooleanField(default=False)
    custom_start_date = models.DateField(blank=True, null=True)
    custom_end_date = models.DateField(blank=True, null=True)
    session_id = models.ForeignKey('Session')
    course_private = models.BooleanField(default=False)
    course_spaces = models.IntegerField(default=15)
    course_date_created = models.DateTimeField(blank=True, null=False, auto_now=True)
    course_date_modified = models.DateTimeField(blank=True, null=False, auto_now=True)
    course_instructor = models.ForeignKey('users.User')
    #course_image
    course_price = models.IntegerField(blank=True, null=True)
    location_id = models.ForeignKey('Location')
    course_category_id = models.ForeignKey('Category')
    recurs = models.BooleanField(default=True)
    recurs_interval = models.IntegerField(blank=True, null=True)
    recurs_times = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cm_courses'

    def __str__(self):
        return self.course_name

class Session(models.Model):
    session_name = models.CharField(blank=False, null=False, max_length=250)
    session_start_date = models.DateField(blank=False, null=False)
    session_end_date = models.DateField(blank=False, null=False)

    def __str__(self):
        return self.session_name

class Location(models.Model):
    location_name = models.CharField(blank=False, null=False, max_length=250)
    location_slug = models.CharField(max_length=100, blank=False, null=False)
    location_address = models.CharField(max_length=200, blank=False, null=False)
    location_city = models.CharField(max_length=200, blank=False, null=False)
    location_state = models.CharField(max_length=2, blank=False, null=False)
    location_postcode = models.CharField(max_length=10, blank=False, null=False)
    location_phone = models.CharField(max_length=15, blank=True, null=True)
    #google maps linkage
    #location_country = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'cm_locations'

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(blank=False, null=False, max_length=250)
    category_slug = models.CharField(max_length=100, blank=False, null=False)

    class Meta:
        db_table = 'cm_categories'
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name

class Spot(models.Model):
    course_id = models.ForeignKey('Course')
    spot_name = models.CharField(max_length=100, blank=False, null=False)
    spot_price = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    spot_start = models.DateTimeField(blank=True, null=True) #spots go on sale
    spot_end = models.DateTimeField(blank=True, null=True) #sales end

    class Meta:
        db_table = 'cm_spots'
'''
class Reservation(models.Model):
    #basically building a cart system here, look into existing carts for functionality
    #look at django-carton for this part
    course_id = models.ForeignKey('Course')
    person_id = models.BigIntegerField() #if signed in
    reservation_spaces = models.IntegerField()
    reservation_comment = models.TextField(blank=True, null=True)
    reservation_date = models.DateTimeField()
    reservation_status = models.IntegerField()
    reservation_total = models.DecimalField(max_digits=14, decimal_places=4)
    reservation_tax_rate = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    reservation_taxes = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    reservation_meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cm_reservations'


'''
