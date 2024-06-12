# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
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


class MyappArif(models.Model):
    id = models.BigAutoField(primary_key=True)
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'myapp_arif'


class MyappCity(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    population = models.IntegerField()
    literacy = models.DecimalField(max_digits=12, decimal_places=2)
    growth = models.DecimalField(max_digits=12, decimal_places=2)
    crime = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    education = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    health = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    job = models.CharField(db_column='Job', max_length=255, blank=True, null=True)  # Field name made lowercase.
    living_cost = models.DecimalField(db_column='Living_Cost', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pollution = models.DecimalField(db_column='Pollution', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    transportation = models.DecimalField(db_column='Transportation', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    job_rank = models.IntegerField(db_column='Job_rank', blank=True, null=True)  # Field name made lowercase.
    living_cost_rank = models.IntegerField(db_column='Living_Cost_rank', blank=True, null=True)  # Field name made lowercase.
    salary_rank = models.IntegerField(db_column='Salary_rank', blank=True, null=True)  # Field name made lowercase.
    transportation_rank = models.IntegerField(db_column='Transportation_rank', blank=True, null=True)  # Field name made lowercase.
    crime_rank = models.IntegerField(blank=True, null=True)
    education_rank = models.IntegerField(blank=True, null=True)
    growth_rank = models.IntegerField(blank=True, null=True)
    health_rank = models.IntegerField(blank=True, null=True)
    literacy_rank = models.IntegerField(blank=True, null=True)
    pollution_rank = models.IntegerField(blank=True, null=True)
    population_rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'myapp_city'

