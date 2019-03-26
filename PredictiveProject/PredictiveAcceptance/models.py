# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete
#   
#   ` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.db import connection


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class LookupValues(models.Model):
    lookup_code = models.CharField(primary_key=True, max_length=10)
    lookup_type = models.CharField(unique=True, max_length=50)
    lookup_value = models.CharField(unique=True, max_length=50)
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lookup_values'

    def __str__(self):
        return u'{0}'.format(self.lookup_code)

 

def userId():
  with connection.cursor() as cursor:
    cursor.execute("""SELECT nextval('predictive_users_seq')""")
    return cursor.fetchone()[0]

def get_userType():
    return UserTypes.objects.get(user_type = "Student")

class PredictiveUsers(models.Model):
    user_id = models.IntegerField(primary_key=True, default=userId)
    username = models.CharField(unique=True, max_length=20)
    firstname = models.CharField(max_length=30)
    middlename = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    email_address = models.CharField(unique=True, max_length=100)
    user_type_id = models.ForeignKey('UserTypes', db_column='user_type_id' ,default=lambda: get_userType(),on_delete = models.CASCADE)    
    #user_type = models.ForeignKey('UserTypes', db_column='user_type' ,default= 1)
    created_on = models.DateTimeField(auto_now = True)

    class Meta:
        managed = False
        db_table = 'predictive_users'


class StudentProfiles(models.Model):
    user = models.ForeignKey(PredictiveUsers, models.DO_NOTHING, primary_key=True)
    grescore = models.IntegerField()
    englishtest = models.DecimalField(max_digits=2, decimal_places=1)
    undergradcgpa = models.DecimalField(max_digits=2, decimal_places=1)
    workex_months = models.IntegerField()
    research_skills = models.IntegerField()
    created_on = models.DateTimeField(auto_now = True)

    class Meta:
        managed = False
        db_table = 'student_profiles'


class UniversityNames(models.Model):
    university_code = models.CharField(primary_key=True, max_length=10)
    university_name = models.CharField(unique=True, max_length=50)
    created_on = models.DateTimeField(auto_now = True)

    class Meta:
        managed = False
        db_table = 'university_names'

    def __str__(self):
     return u'{0}'.format(self.university_name)


class UniversitySampleData(models.Model):
    sample_data = models.AutoField(primary_key=True)
    university_code = models.ForeignKey(UniversityNames, models.DO_NOTHING, db_column='university_code')
    grescore = models.IntegerField()
    englishtest = models.IntegerField()
    undergradcgpa = models.IntegerField()
    workex_months = models.IntegerField()
    research_skills = models.IntegerField()
    acceptancepercentage = models.IntegerField()
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'university_sample_data'

    def __str__(self):
      return '%s' %(self.university_code)




class UniversitySummaries(models.Model):
    university_code = models.ForeignKey(UniversityNames, models.DO_NOTHING, db_column='university_code', primary_key=True)
    avg_grescore = models.IntegerField()
    avg_eng_score = models.DecimalField(max_digits=2, decimal_places=1)
    avg_undergradcgpa = models.DecimalField(max_digits=2, decimal_places=1)
    avg_workex_months = models.IntegerField()
    avg_research_skills = models.IntegerField()
    avg_acceptancepercentage = models.IntegerField()
    created_on = models.DateTimeField(auto_now = True)

    class Meta:
        managed = False
        db_table = 'university_summaries'


class UserTypes(models.Model):
    user_type_id = models.IntegerField(primary_key=True)
    user_type = models.CharField(unique=True, max_length=20)
    created_on = models.DateTimeField(auto_now = True)

    def __str__(self):
     return u'{0}'.format(self.user_type)

    class Meta:
        managed = False
        db_table = 'user_types'


class UniversityAcceptanceRates(models.Model):
    student_user = models.ForeignKey(PredictiveUsers, models.DO_NOTHING, primary_key=True)
    uor_accep_rate = models.IntegerField(blank=True, null=True)
    uoa_accep_rate = models.IntegerField(blank=True, null=True)
    ubc_accep_rate = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now = True)

    class Meta:
        managed = False
        db_table = 'university_acceptance_rates'