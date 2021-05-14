# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=100)
    classification = models.CharField(max_length=100)
    fascinated = models.IntegerField()
    amused = models.IntegerField()
    excited = models.IntegerField()
    angry = models.IntegerField()
    sad = models.IntegerField()
    bored = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    year = models.IntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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


class Awards(models.Model):
    title = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    receive = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'awards'


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


class Dropdown(models.Model):
    id = models.AutoField()
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dropdown'


class Facebook(models.Model):
    fid = models.AutoField(primary_key=True)
    post = models.IntegerField()
    responserate = models.CharField(db_column='responseRate', max_length=255)  # Field name made lowercase.
    likes = models.IntegerField()
    followers = models.IntegerField()
    shares = models.IntegerField()
    reactions = models.IntegerField()
    comments = models.IntegerField()
    toptopics = models.TextField(db_column='topTopics')  # Field name made lowercase.
    yes = models.IntegerField()
    no = models.IntegerField()
    date = models.DateField()
    asofdate = models.DateField(db_column='asOfDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facebook'


class FbLikefollowAge(models.Model):
    fbid = models.IntegerField()
    age13to17 = models.IntegerField()
    age18to24 = models.IntegerField()
    age25to34 = models.IntegerField()
    age35to44 = models.IntegerField()
    age45to54 = models.IntegerField()
    age55to64 = models.IntegerField()
    age65 = models.IntegerField()
    agetype = models.IntegerField(db_column='ageType')  # Field name made lowercase.
    like_follow = models.IntegerField()
    type = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fb_likefollow_age'


class FbPostcomment(models.Model):
    fid = models.IntegerField()
    seed = models.IntegerField()
    land = models.IntegerField()
    crop = models.IntegerField()
    nutrient = models.IntegerField()
    water = models.IntegerField()
    pest = models.IntegerField()
    harvest = models.IntegerField()
    machine = models.IntegerField()
    food = models.IntegerField()
    program = models.IntegerField()
    arts = models.IntegerField()
    people = models.IntegerField()
    service = models.IntegerField()
    cognitive = models.IntegerField()
    attitudal = models.IntegerField()
    behavioral = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fb_postcomment'


class FbPostdata(models.Model):
    fid = models.IntegerField()
    seed = models.IntegerField()
    land = models.IntegerField()
    crop = models.IntegerField()
    nutrient = models.IntegerField()
    water = models.IntegerField()
    pest = models.IntegerField()
    harvest = models.IntegerField()
    machine = models.IntegerField()
    food = models.IntegerField()
    program = models.IntegerField()
    arts = models.IntegerField()
    people = models.IntegerField()
    service = models.IntegerField()
    photo = models.IntegerField()
    video = models.IntegerField()
    meme = models.IntegerField()
    news = models.IntegerField()
    radio = models.IntegerField()
    feature = models.IntegerField()
    share = models.IntegerField()
    reaction = models.IntegerField()
    comment = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fb_postdata'


class FbPrivatemessage(models.Model):
    fid = models.IntegerField()
    seedavailability = models.IntegerField(db_column='seedAvailability')  # Field name made lowercase.
    seedvariery = models.IntegerField(db_column='seedVariery')  # Field name made lowercase.
    land = models.IntegerField()
    crop = models.IntegerField()
    nutrient = models.IntegerField()
    water = models.IntegerField()
    pest = models.IntegerField()
    harvest = models.IntegerField()
    generalinfo = models.IntegerField(db_column='generalInfo')  # Field name made lowercase.
    kp = models.IntegerField()
    machine = models.IntegerField()
    food = models.IntegerField()
    training = models.IntegerField()
    palayaman = models.IntegerField()
    otheragency = models.IntegerField(db_column='otherAgency')  # Field name made lowercase.
    others = models.IntegerField()
    responserate = models.IntegerField(db_column='responseRate')  # Field name made lowercase.
    studentresearcher = models.IntegerField(db_column='studentResearcher')  # Field name made lowercase.
    farmer = models.IntegerField()
    aew = models.IntegerField()
    otheroccupation = models.IntegerField(db_column='otherOccupation')  # Field name made lowercase.
    male = models.IntegerField()
    female = models.IntegerField()
    age13 = models.IntegerField()
    age18 = models.IntegerField()
    age25 = models.IntegerField()
    age35 = models.IntegerField()
    age45 = models.IntegerField()
    age55 = models.IntegerField()
    age65 = models.IntegerField()
    yes = models.IntegerField()
    no = models.IntegerField()
    asked1 = models.CharField(max_length=255)
    asked2 = models.CharField(max_length=255)
    asked3 = models.CharField(max_length=255)
    asked4 = models.CharField(max_length=255)
    asked5 = models.CharField(max_length=255)
    askedfreq1 = models.IntegerField(db_column='askedFreq1')  # Field name made lowercase.
    askedfreq2 = models.IntegerField(db_column='askedFreq2')  # Field name made lowercase.
    askedfreq3 = models.IntegerField(db_column='askedFreq3')  # Field name made lowercase.
    askedfreq4 = models.IntegerField(db_column='askedFreq4')  # Field name made lowercase.
    askedfreq5 = models.IntegerField(db_column='askedFreq5')  # Field name made lowercase.
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fb_privatemessage'


class FbVersus(models.Model):
    fbid = models.IntegerField()
    da = models.IntegerField()
    ati = models.IntegerField()
    pcc = models.IntegerField()
    philmech = models.IntegerField()
    bpi = models.IntegerField()
    bar = models.IntegerField()
    period = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fb_versus'


class FbfollowersLocation(models.Model):
    fid = models.IntegerField()
    location = models.CharField(max_length=255)
    number = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fbfollowers_location'


class FblikesLocation(models.Model):
    fid = models.IntegerField()
    location = models.CharField(max_length=255)
    number = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fblikes_location'


class Kp(models.Model):
    kp_id = models.AutoField(primary_key=True)
    produced = models.IntegerField()
    quarter = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kp'


class KpPublication(models.Model):
    numberofpublication = models.IntegerField(db_column='numberOfPublication')  # Field name made lowercase.
    type = models.IntegerField()
    title = models.IntegerField()
    supplier = models.IntegerField()
    copyproduced = models.IntegerField(db_column='copyProduced')  # Field name made lowercase.
    copydistributed = models.IntegerField(db_column='copyDistributed')  # Field name made lowercase.
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kp_publication'


class KpType(models.Model):
    accordion = models.IntegerField()
    book = models.IntegerField()
    booklet = models.IntegerField()
    brochure = models.IntegerField()
    calendar = models.IntegerField()
    catalog = models.IntegerField()
    infographics = models.IntegerField()
    komiks = models.IntegerField()
    handouts = models.IntegerField()
    magasin = models.IntegerField()
    magazine = models.IntegerField()
    milestones = models.IntegerField()
    newsletter = models.IntegerField()
    palaycheck = models.IntegerField()
    poster = models.IntegerField()
    qa = models.IntegerField()
    rs4dm = models.IntegerField()
    rtb = models.IntegerField()
    leaflet = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    distribute = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'kp_type'


class Partners(models.Model):
    partner = models.CharField(max_length=255)
    classification = models.CharField(max_length=255)
    engagement = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    scope = models.CharField(max_length=255)
    period = models.IntegerField()
    year = models.IntegerField()
    date = models.DateField()
    day = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'partners'


class PrkbLocation(models.Model):
    location = models.CharField(max_length=255)
    number = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prkb_location'


class PrkbUpload(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    date = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prkb_upload'


class PrkbVisitor(models.Model):
    visit = models.IntegerField()
    age18to24 = models.IntegerField()
    age25to34 = models.IntegerField()
    age35to44 = models.IntegerField()
    age45to54 = models.IntegerField()
    age55to64 = models.IntegerField()
    age65 = models.IntegerField()
    malevisitor = models.IntegerField(db_column='maleVisitor')  # Field name made lowercase.
    femalevisitor = models.IntegerField(db_column='femaleVisitor')  # Field name made lowercase.
    yes = models.IntegerField()
    no = models.IntegerField()
    download = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prkb_visitor'


class Ptc(models.Model):
    ptcid = models.AutoField(primary_key=True)
    totalregistered = models.IntegerField(db_column='totalRegistered')  # Field name made lowercase.
    malenewusers = models.IntegerField(db_column='maleNewUsers')  # Field name made lowercase.
    femalenewusers = models.IntegerField(db_column='femaleNewUsers')  # Field name made lowercase.
    category = models.TextField()
    location = models.TextField()
    toptopics = models.TextField(db_column='topTopics')  # Field name made lowercase.
    responserate = models.CharField(db_column='responseRate', max_length=255)  # Field name made lowercase.
    yes = models.IntegerField()
    textmale = models.IntegerField(db_column='textMale')  # Field name made lowercase.
    textfemale = models.IntegerField(db_column='textFemale')  # Field name made lowercase.
    nowdate = models.DateField()
    asofdate = models.DateField(db_column='asOfDate')  # Field name made lowercase.
    no = models.IntegerField()
    year = models.IntegerField()
    period = models.IntegerField()
    answered = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ptc'


class RadioBroadcastrelease(models.Model):
    topic = models.CharField(max_length=255)
    frequency = models.CharField(max_length=255)
    yes = models.IntegerField()
    no = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radio_broadcastrelease'


class RadioSegment(models.Model):
    topic = models.CharField(max_length=255)
    interviewee = models.CharField(max_length=255)
    radiostation = models.CharField(db_column='radioStation', max_length=255)  # Field name made lowercase.
    frequency = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'radio_segment'


class Staff(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    datestarted = models.DateField(db_column='dateStarted')  # Field name made lowercase.
    status = models.CharField(max_length=255)
    birthdate = models.DateField()
    sex = models.CharField(max_length=20)
    education = models.CharField(max_length=255)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'staff'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    desigbantion = models.CharField(max_length=255)
    privilege = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    image = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class Website(models.Model):
    wid = models.AutoField(primary_key=True)
    visit = models.IntegerField()
    pickuprate = models.IntegerField(db_column='pickupRate')  # Field name made lowercase.
    male = models.IntegerField()
    female = models.IntegerField()
    yes = models.IntegerField()
    no = models.IntegerField()
    location = models.TextField()
    year = models.IntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website'


class WebsiteLcoation(models.Model):
    wlid = models.AutoField(primary_key=True)
    wid = models.IntegerField()
    location = models.CharField(max_length=255)
    number = models.IntegerField()
    period = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website_lcoation'
