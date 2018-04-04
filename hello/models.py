# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.timezone import now


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EasyMapsAddress(models.Model):
    address = models.CharField(unique=True, max_length=255)
    computed_address = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    geocode_error = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'easy_maps_address'


class HazardReportAttachments(models.Model):
    id = models.BigAutoField(primary_key=True)
    report = models.ForeignKey('HazardReports', models.DO_NOTHING)
    attachment_name = models.CharField(max_length=100)
    attachment_path = models.CharField(max_length=100)
    user = models.ForeignKey('User', models.DO_NOTHING)
    created_at = models.DateTimeField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'hazard_report_attachments'


class HazardReportHistory(models.Model):
    report = models.ForeignKey('HazardReports', models.DO_NOTHING)
    description = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hazard_report_history'


class HazardReports(models.Model):
    id = models.BigAutoField(primary_key=True)
    creator = models.ForeignKey('User', models.DO_NOTHING)
    hazard_type = models.ForeignKey('HazardTypes', models.DO_NOTHING, db_column='hazard_type')
    description = models.TextField()
    created_at = models.DateTimeField(default=now, blank=True)
    status = models.IntegerField()
    assigned_to = models.ForeignKey('User', models.DO_NOTHING, db_column='assigned_to')
    priority = models.IntegerField()
    address_id = models.CharField(max_length=45, blank=True, null=True)
    street = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'hazard_reports'


class HazardTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'hazard_types'


class HelloGreeting(models.Model):
    when = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hello_greeting'


class HelloPointofinterest(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=42)

    class Meta:
        managed = False
        db_table = 'hello_pointofinterest'


class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    user_type = models.ForeignKey('UserTypes', models.DO_NOTHING, db_column='user_type')

    class Meta:
        managed = False
        db_table = 'user'


class UserTypes(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'user_types'
