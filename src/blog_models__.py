from peewee import *

database = MySQLDatabase('today_if_ua', **{'password': 'root', 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        db_table = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(db_column='content_type_id', rel_model=DjangoContentType, to_field='id')
    name = CharField()

    class Meta:
        db_table = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(db_column='group_id', rel_model=AuthGroup, to_field='id')
    permission = ForeignKeyField(db_column='permission_id', rel_model=AuthPermission, to_field='id')

    class Meta:
        db_table = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(db_column='group_id', rel_model=AuthGroup, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(db_column='permission_id', rel_model=AuthPermission, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class CoreGategories(BaseModel):
    icon = CharField()
    slug = CharField(unique=True)
    title = CharField()

    class Meta:
        db_table = 'core_gategories'

class CoreEvent(BaseModel):
    category = ForeignKeyField(db_column='category_id', null=True, rel_model=CoreGategories, to_field='id')
    contact_number = CharField()
    description = TextField(null=True)
    event_day = DateField(null=True)
    event_time = TimeField(null=True)
    fb_href = CharField(null=True)
    latitude = CharField()
    location = CharField()
    location_false = CharField(null=True)
    longitude = CharField()
    photo = CharField(null=True)
    price = CharField()
    publish = DateField()
    slug = CharField(index=True)
    source = CharField()
    source_href = CharField()
    status = CharField()
    ticket = CharField()
    title = CharField()
    vk_href = CharField(null=True)

    class Meta:
        db_table = 'core_event'

class CorePartners(BaseModel):
    photo = CharField(null=True)
    source_href = CharField()
    title = CharField(null=True)

    class Meta:
        db_table = 'core_partners'

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(db_column='content_type_id', null=True, rel_model=DjangoContentType, to_field='id')
    object = TextField(db_column='object_id', null=True)
    object_repr = CharField()
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        db_table = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        db_table = 'django_session'

class ThumbnailKvstore(BaseModel):
    key = CharField(primary_key=True)
    value = TextField()

    class Meta:
        db_table = 'thumbnail_kvstore'

