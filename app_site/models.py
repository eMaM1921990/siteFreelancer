from __future__ import unicode_literals


# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

MANAGED=False
class AccountType(models.Model):
    # id = models.IntegerField(unique=True)
    type = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'Account_type'
        managed=MANAGED

    def __str__(self):
        return self.type

class Languages(models.Model):
    # id = models.IntegerField(unique=True)
    language = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'Languages'
        managed=MANAGED

    def __str__(self):
        return self.language



class Users(models.Model):
    # id = models.IntegerField(unique=True)
    username = models.CharField(unique=True, max_length=180, blank=True)
    first_name = models.CharField(max_length=180, blank=True)
    facebook_id = models.IntegerField(unique=True, null=True, blank=True)
    email = models.CharField(unique=True, max_length=180, blank=True)
    password = models.CharField(max_length=180, blank=True)
    account_type = models.ForeignKey(AccountType, null=True, db_column='account_type', blank=True)
    date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=135, blank=True)
    country = models.CharField(max_length=135, blank=True)
    language = models.ForeignKey(Languages, null=True, db_column='language', blank=True)
    image = models.CharField(max_length=180, blank=True)
    cover = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)
    skills = models.CharField(max_length=250, blank=True)
    title = models.CharField(max_length=180, blank=True)
    address = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=250, blank=True)
    zip_code = models.CharField(max_length=180, blank=True, db_column='zip')
    status=models.CharField(max_length=180,default='Active')

    class Meta:
        db_table = u'Users'
        managed=MANAGED

    def __str__(self):
        return self.username


class Messages(models.Model):
    from_user = models.ForeignKey(Users, null=True, db_column='from', blank=True, related_name="user_from") # Field renamed because it was a Python reserved word.
    to_user = models.ForeignKey(Users, null=True, db_column='to', blank=True , related_name="user_to")
    message = models.CharField(max_length=500, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'Messages'
        managed=MANAGED


class AccountUpdates(models.Model):
    # id = models.IntegerField(unique=True)
    user = models.ForeignKey(Users, null=True, blank=True)
    old_type = models.ForeignKey(AccountType, null=True, db_column='old_type', blank=True , related_name="type_old")
    new_type = models.ForeignKey(AccountType, null=True, db_column='new_type', blank=True , related_name="type_new")
    old_email = models.CharField(max_length=135, blank=True )
    new_email = models.CharField(max_length=135, blank=True)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'Account_updates'
        managed=MANAGED


class UsersActivity(models.Model):
    # id = models.IntegerField(unique=True)
    user = models.ForeignKey(Users, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'Users_activity'
        managed=MANAGED


class Categories(models.Model):
    # id = models.IntegerField(unique=True)
    category = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'Categories'
        managed=MANAGED

    def __str__(self):
        return self.category



class MembershipType(models.Model):
    # id = models.IntegerField(unique=True)
    type = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'Membership_type'
        managed=MANAGED

    def __str__(self):
        return self.type

class Membership(models.Model):
    # id = models.IntegerField(unique=True)
    membership_type = models.ForeignKey(MembershipType, null=True, db_column='membership_type', blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(Users, null=True, blank=True)
    class Meta:
        db_table = u'Membership'
        managed=MANAGED

    def __str__(self):
        return self.user.username



class PasswordReset(models.Model):
    # id = models.IntegerField(unique=True)
    username = models.CharField(max_length=180, blank=True)
    email = models.CharField(max_length=135, blank=True)
    password = models.CharField(max_length=135, blank=True)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'Password_reset'
        managed=MANAGED

class PaymentRequests(models.Model):
    # id = models.IntegerField(unique=True)
    made_by = models.CharField(max_length=135, blank=True)
    in_favor_of = models.CharField(max_length=135, blank=True)
    teensie_name = models.CharField(max_length=135, blank=True)
    amount = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'Payment_requests'
        managed=MANAGED

class ProfileUpdates(models.Model):
    # id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=135, blank=True)
    last_name = models.CharField(max_length=135, blank=True)
    language = models.ForeignKey(Languages, null=True, db_column='language', blank=True)
    city = models.CharField(max_length=135, blank=True)
    country = models.CharField(max_length=135, blank=True)
    date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(Users, null=True, blank=True)
    class Meta:
        db_table = u'Profile_updates'
        managed=MANAGED








class TeensiesPosted(models.Model):
    # id = models.IntegerField(unique=True)

    teensie_name = models.CharField(max_length=180, blank=True)
    status = models.CharField(max_length=60, blank=True)
    timeframe = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Categories, null=True, db_column='category', blank=True)
    user = models.ForeignKey(Users, null=True, db_column='user', blank=True)
    description = models.CharField(max_length=500, blank=True)
    skills = models.CharField(max_length=100, blank=True)
    ordered = models.IntegerField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True, default=0.0)
    featured = models.CharField(max_length=135, blank=True)

    class Meta:
        db_table = u'Teensies_posted'
        managed=MANAGED

    def __str__(self):
        return self.teensie_name


class TeensiesDeleted(models.Model):
    teensie = models.ForeignKey(TeensiesPosted, null=True, db_column='teensie', blank=True)
    date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = u'Teensies_deleted'
        managed=MANAGED


class TeensiesCancelled(models.Model):
    user = models.ForeignKey(Users, null=True, db_column='user', blank=True)
    teensie = models.ForeignKey(TeensiesPosted, null=True, db_column='teensie', blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'Teensies_cancelled'
        managed=MANAGED

    def __str__(self):
        return self.teensie.teensie_name


class TeensiesFeatured(models.Model):
    user = models.ForeignKey(Users, null=True, db_column='user', blank=True)
    teensie = models.ForeignKey(TeensiesPosted, null=True, db_column='teensie', blank=True)
    date = models.DateField(null=True, blank=True)
    days = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = u'Teensies_featured'
        managed=MANAGED

    def __str__(self):
        return self.teensie.teensie_name


class Disputes(models.Model):
    user = models.ForeignKey(Users, null=True, db_column='user', blank=True , related_name="user_disp")
    payment = models.CharField(max_length=180, blank=True)
    date = models.DateField(null=True, blank=True)
    teensie = models.ForeignKey(TeensiesPosted, null=True, db_column='teensie', blank=True)
    winner = models.ForeignKey(Users, null=True, db_column='winner', blank=True , related_name="winner_disp")
    class Meta:
        db_table = u'Disputes'
        managed=MANAGED



class TeensiesOrdered(models.Model):
    user = models.ForeignKey(Users, null=True, db_column='user', blank=True)
    teensie = models.ForeignKey(TeensiesPosted, null=True, db_column='teensie', blank=True)
    date = models.DateField(null=True, blank=True)
    released = models.CharField(max_length=135, blank=True)
    review = models.CharField(max_length=255, blank=True, default="" )
    class Meta:
        db_table = u'Teensies_ordered'
        managed=MANAGED

    def __str__(self):
        return self.teensie.teensie_name


class WithdrawalRequests(models.Model):
    user = models.ForeignKey(Users, null=True, db_column='user', blank=True)
    email = models.CharField(max_length=300, blank=True)
    amount = models.FloatField(null=True, blank=True)
    date = models.CharField(max_length=135, blank=True)
    status = models.CharField(max_length=135, blank=True)
    class Meta:
        db_table = u'Withdrawal_requests'
        managed=MANAGED

# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=240)
#     class Meta:
#         db_table = u'auth_group'
#
# class DjangoContentType(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=300)
#     app_label = models.CharField(unique=True, max_length=254)
#     model = models.CharField(unique=True, max_length=254)
#     class Meta:
#         db_table = u'django_content_type'
#
# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=150)
#     content_type = models.ForeignKey(DjangoContentType)
#     codename = models.CharField(unique=True, max_length=254)
#     class Meta:
#         db_table = u'auth_permission'
#
# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     group = models.ForeignKey(AuthGroup)
#     permission = models.ForeignKey(AuthPermission)
#     class Meta:
#         db_table = u'auth_group_permissions'
#
#
# class AuthUser(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(unique=True, max_length=90)
#     first_name = models.CharField(max_length=90)
#     last_name = models.CharField(max_length=90)
#     email = models.CharField(max_length=225)
#     password = models.CharField(max_length=384)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     is_superuser = models.IntegerField()
#     last_login = models.DateTimeField()
#     date_joined = models.DateTimeField()
#     class Meta:
#         db_table = u'auth_user'
#
# class AuthMessage(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     message = models.TextField()
#     class Meta:
#         db_table = u'auth_message'
#
#
#
#
# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     group = models.ForeignKey(AuthGroup)
#     class Meta:
#         db_table = u'auth_user_groups'
#
# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)
#     user = models.ForeignKey(AuthUser)
#     permission = models.ForeignKey(AuthPermission)
#     class Meta:
#         db_table = u'auth_user_user_permissions'
#
# class DjangoAdminLog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     action_time = models.DateTimeField()
#     user = models.ForeignKey(AuthUser)
#     content_type = models.ForeignKey(DjangoContentType, null=True, blank=True)
#     object_id = models.TextField(blank=True)
#     object_repr = models.CharField(max_length=600)
#     action_flag = models.IntegerField()
#     change_message = models.TextField()
#     class Meta:
#         db_table = u'django_admin_log'
#
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(max_length=120, primary_key=True)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#     class Meta:
#         db_table = u'django_session'
#
# class DjangoSite(models.Model):
#     id = models.IntegerField(primary_key=True)
#     domain = models.CharField(max_length=300)
#     name = models.CharField(max_length=150)
#     class Meta:
#         db_table = u'django_site'

