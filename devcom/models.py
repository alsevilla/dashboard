from django.db import models

#facebook
class fb_page_info(models.Model):
    likes = models.IntegerField()
    followers = models.IntegerField()
    seeds = models.IntegerField()
    extensions = models.IntegerField()
    core = models.IntegerField()
    hybrid = models.IntegerField()
    pSeeds = models.IntegerField()
    pExtensions = models.IntegerField()
    pCore = models.IntegerField()
    pHybrid = models.IntegerField()

    allpost = models.IntegerField()
    reactions = models.IntegerField()
    comments = models.IntegerField()
    shares = models.IntegerField()
    reach = models.IntegerField()

    videos = models.IntegerField()
    vViews = models.IntegerField()
    vReactions = models.IntegerField()
    vComments = models.IntegerField()
    vShares = models.IntegerField()
    vReach = models.IntegerField()

    vSeeds = models.IntegerField()
    vExtensions = models.IntegerField()
    vCore = models.IntegerField()
    vHybrid = models.IntegerField()

    irri = models.IntegerField()
    da = models.IntegerField()
    ati = models.IntegerField()
    pcc = models.IntegerField()
    philmech = models.IntegerField()
    bpi = models.IntegerField()
    bar = models.IntegerField()

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    semester = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'fb_page_info'

class fb_post_data(models.Model):
    responseRate = models.IntegerField()
    messagesRecieve = models.IntegerField()

    topic1 = models.CharField(max_length=255)
    ntopic1 = models.IntegerField()
    topic2 = models.CharField(max_length=255)
    ntopic2 = models.IntegerField()
    topic3 = models.CharField(max_length=255)
    ntopic3 = models.IntegerField()
    topic4 = models.CharField(max_length=255)
    ntopic4 = models.IntegerField()
    topic5 = models.CharField(max_length=255)
    ntopic5 = models.IntegerField()

    occupation1 = models.CharField(max_length=255)
    noccupation1 = models.IntegerField()
    occupation2 = models.CharField(max_length=255)
    noccupation2 = models.IntegerField()
    occupation3 = models.CharField(max_length=255)
    noccupation3 = models.IntegerField()
    occupation4 = models.CharField(max_length=255)
    noccupation4 = models.IntegerField()
    occupation5 = models.CharField(max_length=255)
    noccupation5 = models.IntegerField()

    nSurvey = models.IntegerField()
    nSurveyYes1 = models.IntegerField()
    nSurveyNo1 = models.IntegerField()
    nSurveyYes2 = models.IntegerField()
    nSurveyNo2 = models.IntegerField()

    male = models.IntegerField()
    female = models.IntegerField()

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    semester = models.IntegerField()
    year = models.IntegerField()

    class Meta:
        db_table = 'fb_post_data'

#end Facebook
#philrice text Center
class ptc(models.Model):
    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    year = models.IntegerField()

    sms = models.IntegerField()
    smsWD = models.IntegerField()
    smsWE = models.IntegerField()
    dwntimeH = models.IntegerField()
    dwntimeM = models.IntegerField()
    texterOH = models.IntegerField()
    texterNOH = models.IntegerField()
    texterWD = models.IntegerField()
    texterWE = models.IntegerField()
    keywords = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()

    seedAvail = models.IntegerField()
    seedVar = models.IntegerField()
    landPrep = models.IntegerField()
    cropEsta = models.IntegerField()
    nutriMng = models.IntegerField()
    waterMng = models.IntegerField()
    pestMng = models.IntegerField()
    harvMng = models.IntegerField()
    genInfo = models.IntegerField()
    knowProd = models.IntegerField()
    machine = models.IntegerField()
    foodSci = models.IntegerField()
    training = models.IntegerField()
    palayamanan = models.IntegerField()
    philrice = models.IntegerField()
    otherAgency = models.IntegerField()
    greetings = models.IntegerField()
    thanks = models.IntegerField()
    registration = models.IntegerField()
    others = models.IntegerField()
    rcef = models.IntegerField()
    rcefSeed = models.IntegerField()
    rcefComp = models.IntegerField()
    rcefExt = models.IntegerField()
    rsbsa = models.IntegerField()
    website = models.IntegerField()

    OH1to5 = models.IntegerField()
    OH6to10 = models.IntegerField()
    OH11to15 = models.IntegerField()
    OH16to20 = models.IntegerField()
    OH21to25 = models.IntegerField()
    OH26to30 = models.IntegerField()
    OH31to1h = models.IntegerField()
    OH1hto2h = models.IntegerField()
    OH2hto4h = models.IntegerField()
    OH4hto8h = models.IntegerField()
    OH8hto12h = models.IntegerField()
    OH12hto24h = models.IntegerField()
    OH24to48h = models.IntegerField()
    OH48hplus = models.IntegerField()
    notRes = models.IntegerField()

    NOH1to5 = models.IntegerField()
    NOH6to10 = models.IntegerField()
    NOH11to15 = models.IntegerField()
    NOH16to20 = models.IntegerField()
    NOH21to25 = models.IntegerField()
    NOH26to30 = models.IntegerField()
    NOH31to1h = models.IntegerField()
    NOH1hto2h = models.IntegerField()
    NOH2hto4h = models.IntegerField()
    NOH4hto8h = models.IntegerField()
    NOH8hto12h = models.IntegerField()
    NOH12hto24h = models.IntegerField()
    NOH24to48h = models.IntegerField()
    NOH48hplus = models.IntegerField()
    NnotRes = models.IntegerField()

    WOH1to5 = models.IntegerField()
    WOH6to10 = models.IntegerField()
    WOH11to15 = models.IntegerField()
    WOH16to20 = models.IntegerField()
    WOH21to25 = models.IntegerField()
    WOH26to30 = models.IntegerField()
    WOH31to1h = models.IntegerField()
    WOH1hto2h = models.IntegerField()
    WOH2hto4h = models.IntegerField()
    WOH4hto8h = models.IntegerField()
    WOH8hto12h = models.IntegerField()
    WOH12hto24h = models.IntegerField()
    WOH24to48h = models.IntegerField()
    WOH48hplus = models.IntegerField()
    WnotRes = models.IntegerField()

    abra = models.IntegerField()
    agusanNorte = models.IntegerField()
    agusanSur = models.IntegerField()
    aklan = models.IntegerField()
    albay = models.IntegerField()
    antique = models.IntegerField()
    apayao = models.IntegerField()
    aurora = models.IntegerField()
    basilan = models.IntegerField()
    bataan = models.IntegerField()
    batanes = models.IntegerField()
    batangas = models.IntegerField()
    benguet = models.IntegerField()
    biliran = models.IntegerField()
    bohol = models.IntegerField()
    bukidnon = models.IntegerField()
    bulacan = models.IntegerField()
    cagayan = models.IntegerField()
    camarinesNorte = models.IntegerField()
    camarinesSur = models.IntegerField()
    camiguin = models.IntegerField()
    capiz = models.IntegerField()
    catanduanes = models.IntegerField()
    cavite = models.IntegerField()
    cebu = models.IntegerField()
    compostela = models.IntegerField()
    davaoNorte = models.IntegerField()
    davaoSur = models.IntegerField()
    davaoOriental = models.IntegerField()
    samarEast = models.IntegerField()
    guimaras = models.IntegerField()
    ifugao = models.IntegerField()
    ilocosNorte = models.IntegerField()
    ilocosSur = models.IntegerField()
    iloilo = models.IntegerField()
    isabela = models.IntegerField()
    kalinga = models.IntegerField()
    launion = models.IntegerField()
    laguna = models.IntegerField()
    lanaoNorte = models.IntegerField()
    lanaoSur = models.IntegerField()
    leyte = models.IntegerField()
    maguindanao = models.IntegerField()
    marinduque = models.IntegerField()
    masbate = models.IntegerField()
    manila = models.IntegerField()
    misamisOccidental = models.IntegerField()
    misamisOriental = models.IntegerField()
    mountainProvince = models.IntegerField()
    negrosOccidental = models.IntegerField()
    negrosOriental = models.IntegerField()
    cotabatoNorth = models.IntegerField()
    samarNorth = models.IntegerField()
    nuevaEcija = models.IntegerField()
    nuevaVizcaya = models.IntegerField()
    mindoroOccidental = models.IntegerField()
    mindoroOriental = models.IntegerField()
    palawan = models.IntegerField()
    pampanga = models.IntegerField()
    pangasinan = models.IntegerField()
    quezon = models.IntegerField()
    quirino = models.IntegerField()
    rizal = models.IntegerField()
    romblon = models.IntegerField()
    samar = models.IntegerField()
    sarangani = models.IntegerField()
    siquijor = models.IntegerField()
    sorsogon = models.IntegerField()
    cotabatoSouth = models.IntegerField()
    leyteSouth = models.IntegerField()
    sultanKudarat = models.IntegerField()
    sulu = models.IntegerField()
    surigaoNorte = models.IntegerField()
    surigaoSur = models.IntegerField()
    tarlac = models.IntegerField()
    tawitawi = models.IntegerField()
    zambales = models.IntegerField()
    zamboangaNorte = models.IntegerField()
    zamboangaSibugay = models.IntegerField()
    zamboangaSur = models.IntegerField()
    international = models.IntegerField()
    undetermined = models.IntegerField()

    class Meta:
        db_table = 'ptc'

#end philrice text center
#philrice Website
class pw(models.Model):
    CLASSIFICATION = (
    ('news','News'),
    ('features','Features'),
    ('photonews','Photo News'),
    )

    title = models.CharField(max_length = 255)
    topic = models.CharField(max_length = 255)
    classification = models.CharField(max_length = 60, null = True, choices=CLASSIFICATION)
    fascinated = models.IntegerField()
    amused = models.IntegerField()
    excited = models.IntegerField()
    angry = models.IntegerField()
    sad = models.IntegerField()
    bored = models.IntegerField()
    date = models.DateField()

    month = models.CharField(max_length = 60)
    year = models.IntegerField()
    class Meta:
        db_table = 'pw'
    #visitor
class pw_visitor(models.Model):
    visit = models.IntegerField()
    pageviews = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    nosex = models.IntegerField()
    syes = models.IntegerField()
    sno = models.IntegerField()

    organic = models.IntegerField()
    direct = models.IntegerField()
    social = models.IntegerField()
    referral = models.IntegerField()
    mobile = models.IntegerField()
    desktop = models.IntegerField()
    tablet = models.IntegerField()

    location1 = models.CharField(max_length = 100)
    nlocation1 = models.IntegerField()
    location2 = models.CharField(max_length = 100)
    nlocation2 = models.IntegerField()
    location3 = models.CharField(max_length = 100)
    nlocation3 = models.IntegerField()
    location4 = models.CharField(max_length = 100)
    nlocation4 = models.IntegerField()
    location5 = models.CharField(max_length = 100)
    nlocation5 = models.IntegerField()

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    year = models.IntegerField()

    class Meta:
        db_table = 'pw_visitor'
    #end visitor
#end philrice website
#pinoyrice
    #visitors
class pr_visitor(models.Model):
    visit = models.IntegerField()
    download = models.IntegerField()
    pageviews = models.IntegerField()

    male = models.IntegerField()
    female = models.IntegerField()
    nosex = models.IntegerField()
    syes = models.IntegerField()
    sno = models.IntegerField()
    age18to24 = models.IntegerField()
    age25to34 = models.IntegerField()
    age35to44 = models.IntegerField()
    age45to54 = models.IntegerField()
    age55to64 = models.IntegerField()
    age65above = models.IntegerField()
    noage = models.IntegerField()
    location1 = models.CharField(max_length = 60)
    nlocation1 = models.IntegerField()
    location2 = models.CharField(max_length = 60)
    nlocation2 = models.IntegerField()
    location3 = models.CharField(max_length = 60)
    nlocation3 = models.IntegerField()
    location4 = models.CharField(max_length = 60)
    nlocation4 = models.IntegerField()
    location5 = models.CharField(max_length = 60)
    nlocation5 = models.IntegerField()
    location6 = models.CharField(max_length = 60)
    nlocation6 = models.IntegerField()
    location7 = models.CharField(max_length = 60)
    nlocation7 = models.IntegerField()
    location8 = models.CharField(max_length = 60)
    nlocation8 = models.IntegerField()
    location9 = models.CharField(max_length = 60)
    nlocation9 = models.IntegerField()
    location10 = models.CharField(max_length = 60)
    nlocation10 = models.IntegerField()

    mobile = models.IntegerField()
    desktop = models.IntegerField()
    tablet = models.IntegerField()

    organic = models.IntegerField()
    direct = models.IntegerField()
    social = models.IntegerField()
    referral = models.IntegerField()

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    year = models.IntegerField()

    class Meta:
        db_table = 'pr_visitor'
    #end visitors
    #uploads
class pr_upload(models.Model):
    title = models.CharField(max_length = 255)

    TOPIC = (
    ('crop','Crop'),
    ('general info','Genera Info'),
    ('harvest','Harvest'),
    ('land','Land'),
    ('machine','Machine'),
    ('nutrient','Nutrient'),
    ('palayamanan','Palayamanan'),
    ('palaycheck','PalayCheck'),
    ('pest','Pest'),
    ('planting','Planting'),
    ('postharvest','Postharvest'),
    ('rcef','RCEF'),
    ('seed','Seed'),
    ('training','Training'),
    ('water','Water'),
    )
    topic = models.CharField(max_length = 60, null = True, choices=TOPIC)

    TYPE = (
    ('accordion','Accordion'),
    ('audio','Audio'),
    ('book','Book'),
    ('booklet','Booklet'),
    ('broadcast release','Broadcast Release'),
    ('data','Data'),
    ('handouts','Handouts'),
    ('infographics','Infographics'),
    ('ksl','KSL'),
    ('learning modules','Learning Modules'),
    ('magazine','Magazine'),
    ('poster','Poster'),
    ('powerpoint','Powerpoint'),
    ('rs4dm','RS4DM'),
    ('rtb','RTB'),
    ('technoguide','Technoguide'),
    ('video','Video')
    )

    type = models.CharField(max_length = 60, null = True, choices=TYPE)

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    year = models.IntegerField()
    class Meta:
        db_table = 'pr_upload'
    #end uploads
#end pinoyrice
#Radio
    #visitor
class radio_visitor(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    interviewee = models.CharField(max_length=255)

    SEX = (
    ('male','Male'),
    ('female','Female'),
    )

    sex = models.CharField(max_length=10, null = True, choices = SEX)
    station = models.CharField(max_length=50)
    location= models.CharField(max_length=255)
    frequency = models.CharField(max_length=10)
    time = models.TimeField()
    month = models.CharField(max_length=10)
    day = models.CharField(max_length=10)
    year = models.IntegerField()

    class Meta:
        db_table = 'radio_visitor'
    #end visitor
    #upload
class radio_upload(models.Model):
    title = models.CharField(max_length=255)
    respondents = models.IntegerField()
    syes = models.IntegerField()
    sno = models.IntegerField()

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    year = models.IntegerField()

    class Meta:
        db_table = 'radio_upload'
    #end upload
#end Radio
#kp

class kp_input(models.Model):
    TYPE = (
    ('Accordion','Accordion'),
    ('AR and Milestone','AR and Milestone'),
    ('Book','Book'),
    ('Brochure and Leaflets','Brochure and Leaflets'),
    ('Calendar','Calendar'),
    ('Comics','Comics'),
    ('Facebook Ads','Facebook Ads'),
    ('Flipchart','Flipchart'),
    ('Handouts','Handouts'),
    ('Infographics','Infographics'),
    ('Journal','Journal'),
    ('Magasin','Magasin'),
    ('Magazine','Magazine'),
    ('Manuals and Field Guides','Manuals and Field Guides'),
    ('Poster','Poster'),
    ('Q&A','Q&A'),
    ('R&D Highlights','R&D Highlights'),
    ('RS4DM','RS4DM'),
    ('Technoguide','Technoguide'),
    ('Technology Bulletin','Technology Bulletin'),
    )

    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    type = models.CharField(max_length = 100, null = True, choices = TYPE)
    manageby = models.CharField(max_length = 100)
    date_record = models.DateTimeField()
    datefortable = models.IntegerField()
    monthfortable = models.IntegerField()
    date_revised = models.DateTimeField(auto_now=True, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s  [%s]' % (self.title,self.type)

    class Meta:
        db_table = 'kp_input'

class kp_input_stock(models.Model):
    kp = models.ForeignKey(kp_input, on_delete=models.CASCADE)
    stocks = models.IntegerField()
    date_recorded = models.DateTimeField()
    printing_press = models.CharField(max_length=150, null=True)


    def __self__(self):
        return self.kp.title

    class Meta:
        db_table = 'kp_input_stock'

class kp_request(models.Model):
    OCCUPATION = (
    ('AEW','AEW'),
    ('Chef','Chef'),
    ('Dev Worker','Dev Worker'),
    ('Entrepreneur','Entrepreneur'),
    ('Farmers','Farmers'),
    ('Govt Employee','Govt Employee'),
    ('Govt Officials','Govt Offcials'),
    ('Media','Media'),
    ('OFW','OFW'),
    ('PhilRice Staff','PhilRice Staff'),
    ('Policymakers','Policymakers'),
    ('Private Company','Private Company'),
    ('Program Manager','Program Manager'),
    ('Researcher','Researcher'),
    ('Student','Student'),
    ('Teacher','Teacher'),
    ('Others','Others'),
    )

    purpose = models.CharField(max_length = 255)
    date = models.DateField()
    requester_name = models.CharField(max_length = 150)
    requester_division = models.CharField(max_length = 200)
    requester_contact = models.CharField(max_length = 20)
    distributer_name = models.CharField(max_length = 150)
    recipient_name = models.CharField(max_length = 150)
    recipient_occupation = models.CharField(max_length = 50, null = True, choices = OCCUPATION)
    recipient_male = models.IntegerField()
    recipient_female = models.IntegerField()
    recipient_province = models.CharField(max_length = 100)
    datefortable = models.IntegerField()
    monthfortable = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.date, self.requester_name)

    class Meta:
        db_table = 'kp_request'


class kp_distribute(models.Model):
    Request = models.ForeignKey(kp_request, on_delete=models.CASCADE, blank=True, null=True)
    Kp = models.ForeignKey(kp_input, on_delete=models.CASCADE, blank=True, null=True)
    Quantity = models.IntegerField()
    Month = models.IntegerField(blank=True, null=True)
    Year = models.IntegerField(blank=True, null=True)
    Date = models.DateField(blank=True, null=True)


    class Meta:
        db_table = 'kp_distribute'

#end kp
#partners
class partners(models.Model):
    partner = models.CharField(max_length=100)
    engagement = models.CharField(max_length=255)
    location = models.CharField(max_length=60)
    startDate = models.DateField()
    endDate = models.DateField()

    CLASSIFICATION = (
    ('media','Media'),
    ('NGO','Non Government Organization'),
    ('private','Private'),
    )
    classification = models.CharField(max_length = 60, null = True, choices=CLASSIFICATION)

    SCOPE = (
    ('national','National'),
    ('regional','Regional'),
    ('community','Community'),
    )
    scope = models.CharField(max_length = 60, null = True, choices=SCOPE)

    MONTH = (
    ('01','January'), ('02','February'),
    ('03','March'), ('04','April'),
    ('05','May'), ('06','June'),
    ('07','July'), ('08','August'),
    ('09','September'), ('10','October'),
    ('11','November'), ('12','December'),
    )

    month = models.CharField(max_length = 60, null = True, choices=MONTH)
    year = models.IntegerField()

    class Meta:
        db_table = 'partners'
#partners
#Intermediaries
class intermediaries(models.Model):

    class Meta:
        db_table = 'intermediaries'
#end Intermediaries
#DevCom
    #Program and Project
class progproj(models.Model):
    program = models.CharField(max_length=255)
    budget = models.CharField(max_length=50)
    datestart = models.DateField()
    dateend = models.DateField()
    duration = models.CharField(max_length=50)

    leader = models.CharField(max_length=50)
    staff = models.CharField(max_length=255)
    cowork = models.CharField(max_length=255)

    protocol = models.FileField(upload_to='protocol/')
    ar = models.FileField(upload_to='ar/')

    STATUS = (
    ('ongoing','Ongoing'),
    ('terminated','Terminated'),
    ('onhold','Onhold'),
    )

    QUARTER = (
    ('1st Quarter','1st Quarter'),
    ('2nd Quarter','2nd Quarter'),
    ('3rd Quarter','3rd Quarter'),
    ('4th Quarter','4th Quarter'),
    )
    status = models.CharField(max_length = 60, null = True, choices=STATUS)
    quarter = models.CharField(max_length = 60, null = True, choices=QUARTER)
    year = models.IntegerField()
    class Meta:
        db_table = 'progproj'
    #end Program and Project
    #Publication
class publication(models.Model):
    journal = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    volume = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    publisher = models.CharField(max_length = 100)
    datepublish = models.DateField()
    publishlocation = models.CharField(max_length = 255)
    dateconference = models.DateField()
    locationconference = models.CharField(max_length = 255)

    QUARTER = (
    ('1st Quarter','1st Quarter'),
    ('2nd Quarter','2nd Quarter'),
    ('3rd Quarter','3rd Quarter'),
    ('4th Quarter','4th Quarter'),
    )

    quarter = models.CharField(max_length = 60, null = True, choices=QUARTER)
    year = models.IntegerField()
    class Meta:
        db_table = 'publication'
    #end Publication
    #Awards
class awards(models.Model):
    CHOICES = (
    ('Individual','Individual'),
    ('Group','Group'),
    )

    title = models.CharField(max_length=255)
    type = models.CharField(max_length = 60, null = True, choices=CHOICES)
    awardee = models.CharField(max_length=100)
    sponsor = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    recieved = models.CharField(max_length=50)

    class Meta:
        db_table = 'awards'
    #end Awards
    #Staff
class staff(models.Model):
    lname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    mi = models.CharField(max_length=10)
    position = models.CharField(max_length=100)
    sdate = models.DateField()
    edate = models.DateField()
    WSTATUS = (
    ('permanent','Permanent'),
    ('contract','Service Contractor'),
    )
    wstatus = models.CharField(max_length=50, null = True, choices =WSTATUS)
    bday = models.DateField()
    SEX = (
    ('male','Male'),
    ('female','Female')
    )
    sex = models.CharField(max_length=10, null = True, choices =SEX)
    EDUCATION = (
    ('elementary','Elementary'),
    ('high school','High School'),
    ('college','College'),
    ('masters','Masters'),
    ('phd','PhD'),
    )
    education = models.CharField(max_length=20, null = True, choices =EDUCATION)
    adress = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    STATUS = (
    ('active','Active'),
    ('ongoing','Ongoing'),
    ('EOC','End of Contract'),
    )
    status = models.CharField(max_length=20, null = True, choices =STATUS)
    photo = models.ImageField(upload_to='staff/')
    class Meta:
        db_table = 'staff'
    #end Staff
#end DevCom
