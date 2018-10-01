# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acceptip(models.Model):
    ip = models.TextField()

    class Meta:
        managed = False
        db_table = 'acceptip'


class Accounts(models.Model):
    name = models.CharField(unique=True, max_length=64)
    password = models.CharField(max_length=128)
    number_2ndpassword = models.CharField(db_column='2ndpassword', max_length=134, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    using2ndpassword = models.IntegerField()
    loggedin = models.PositiveIntegerField()
    lastlogin = models.DateTimeField(blank=True, null=True)
    createdat = models.DateTimeField()
    banned = models.IntegerField()
    banreason = models.TextField(blank=True, null=True)
    gm = models.IntegerField()
    email = models.TextField(blank=True, null=True)
    macs = models.TextField(blank=True, null=True)
    tempban = models.DateTimeField()
    greason = models.PositiveIntegerField(blank=True, null=True)
    nxcash = models.IntegerField(db_column='nxCash', blank=True, null=True)  # Field name made lowercase.
    mpoints = models.IntegerField(db_column='mPoints', blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField()
    sessionip = models.CharField(db_column='SessionIP', max_length=64, blank=True, null=True)  # Field name made lowercase.
    ip = models.TextField(blank=True, null=True)
    pin = models.PositiveIntegerField()
    vpoints = models.IntegerField(blank=True, null=True)
    idcode1 = models.IntegerField()
    idcode2 = models.IntegerField()
    lastconnect = models.CharField(max_length=10)
    realcash = models.PositiveIntegerField(blank=True, null=True)
    aimkind = models.IntegerField()
    promote = models.PositiveIntegerField(blank=True, null=True)
    chrslot = models.PositiveIntegerField()
    checkmeso = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class Acheck(models.Model):
    cid = models.PositiveIntegerField()
    keya = models.CharField(max_length=80)
    value = models.CharField(max_length=80)
    day = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'acheck'


class Alliances(models.Model):
    notice = models.CharField(max_length=101)
    name = models.CharField(max_length=45)
    guild1 = models.IntegerField()
    guild2 = models.IntegerField()
    guild3 = models.IntegerField()
    guild4 = models.IntegerField()
    guild5 = models.IntegerField()
    rank1 = models.CharField(max_length=45)
    rank2 = models.CharField(max_length=45)
    rank3 = models.CharField(max_length=45)
    rank4 = models.CharField(max_length=45)
    rank5 = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'alliances'


class Android(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    itemid = models.IntegerField()
    hair = models.IntegerField()
    face = models.IntegerField()
    name = models.CharField(max_length=20)
    uniqueid = models.IntegerField()
    skincolor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'android'


class Attendcheck(models.Model):
    accid = models.PositiveIntegerField()
    weekly_check = models.PositiveIntegerField()
    returnattend = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'attendcheck'


class Auctionequipment(models.Model):
    inventoryequipmentid = models.AutoField(primary_key=True)
    inventoryitemid = models.PositiveIntegerField()
    upgradeslots = models.IntegerField()
    level = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    int = models.IntegerField()
    luk = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    watk = models.IntegerField()
    matk = models.IntegerField()
    wdef = models.IntegerField()
    mdef = models.IntegerField()
    acc = models.IntegerField()
    avoid = models.IntegerField()
    hands = models.IntegerField()
    speed = models.IntegerField()
    jump = models.IntegerField()
    vicioushammer = models.IntegerField(db_column='ViciousHammer')  # Field name made lowercase.
    itemlevel = models.IntegerField(db_column='itemLevel')  # Field name made lowercase.
    itemexp = models.IntegerField(db_column='itemEXP')  # Field name made lowercase.
    durability = models.IntegerField()
    enhance = models.SmallIntegerField()
    state = models.IntegerField()
    lines = models.IntegerField()
    potential1 = models.IntegerField()
    potential2 = models.IntegerField()
    potential3 = models.IntegerField()
    potential4 = models.IntegerField()
    potential5 = models.IntegerField()
    potential6 = models.IntegerField()
    anvil = models.IntegerField()
    hpr = models.SmallIntegerField(db_column='hpR')  # Field name made lowercase.
    mpr = models.SmallIntegerField(db_column='mpR')  # Field name made lowercase.
    potential7 = models.IntegerField()
    fire = models.IntegerField()
    downlevel = models.IntegerField()
    bossdmg = models.IntegerField()
    alldmgp = models.IntegerField()
    allstatp = models.IntegerField()
    ignorewdef = models.IntegerField(db_column='IgnoreWdef')  # Field name made lowercase.
    soulname = models.IntegerField()
    soulenchanter = models.IntegerField()
    soulpotential = models.IntegerField()
    soulskill = models.IntegerField()
    starforce = models.IntegerField()
    itemtrace = models.IntegerField()
    firestat = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'auctionequipment'


class Auctionitems(models.Model):
    inventoryitemid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    characterid = models.IntegerField(blank=True, null=True)
    accountid = models.IntegerField()
    packageid = models.IntegerField(db_column='packageId')  # Field name made lowercase.
    itemid = models.IntegerField()
    inventorytype = models.IntegerField()
    position = models.IntegerField()
    quantity = models.IntegerField()
    owner = models.TextField(blank=True, null=True)
    gm_log = models.TextField(db_column='GM_Log', blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.IntegerField()
    flag = models.IntegerField()
    expiredate = models.BigIntegerField()
    giftfrom = models.CharField(db_column='giftFrom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iscash = models.IntegerField(db_column='isCash')  # Field name made lowercase.
    ispet = models.IntegerField(db_column='isPet')  # Field name made lowercase.
    isandroid = models.IntegerField(db_column='isAndroid')  # Field name made lowercase.
    issale = models.IntegerField()
    bid = models.BigIntegerField(blank=True, null=True)
    meso = models.BigIntegerField()
    expired = models.BigIntegerField()
    bargain = models.IntegerField()
    ownername = models.CharField(max_length=45)
    buyer = models.IntegerField(blank=True, null=True)
    buytime = models.BigIntegerField()
    starttime = models.BigIntegerField()
    inventoryid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auctionitems'


class Auctions(models.Model):
    characterid = models.IntegerField(primary_key=True)
    bid = models.IntegerField()
    inventoryid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auctions'


class AuthServerLogin(models.Model):
    loginserverid = models.AutoField(primary_key=True)
    key = models.CharField(max_length=40)
    world = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_server_login'


class Banksystem(models.Model):
    name = models.TextField()
    money = models.BigIntegerField()
    date = models.TextField()
    time = models.BigIntegerField()
    try_field = models.PositiveIntegerField(db_column='try')  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'banksystem'


class BbsReplies(models.Model):
    replyid = models.AutoField(primary_key=True)
    threadid = models.PositiveIntegerField()
    postercid = models.PositiveIntegerField()
    timestamp = models.BigIntegerField()
    content = models.CharField(max_length=26)

    class Meta:
        managed = False
        db_table = 'bbs_replies'


class BbsThreads(models.Model):
    threadid = models.AutoField(primary_key=True)
    postercid = models.PositiveIntegerField()
    name = models.CharField(max_length=26)
    timestamp = models.BigIntegerField()
    icon = models.PositiveSmallIntegerField()
    replycount = models.PositiveSmallIntegerField()
    startpost = models.TextField()
    guildid = models.PositiveIntegerField()
    localthreadid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bbs_threads'


class Boom(models.Model):
    status = models.TextField(blank=True, null=True)
    gun = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boom'


class Boomboom(models.Model):
    create = models.TextField(blank=True, null=True)
    gun = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boomboom'


class BossTotalRank(models.Model):
    name = models.CharField(max_length=45)
    boss = models.IntegerField()
    bgin = models.CharField(max_length=45)
    ends = models.CharField(max_length=45)
    time = models.IntegerField()
    pmem = models.CharField(max_length=45)
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'boss_total_rank'


class Bosscooltime(models.Model):
    channel = models.IntegerField()
    map = models.IntegerField()
    time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'bosscooltime'


class Bosslog(models.Model):
    bosslogid = models.AutoField(primary_key=True)
    characterid = models.PositiveIntegerField()
    bossid = models.CharField(max_length=20)
    lastattempt = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bosslog'


class Bossraidtime(models.Model):
    bgin = models.CharField(max_length=45)
    ends = models.CharField(max_length=45)
    name = models.CharField(max_length=45)
    diff = models.CharField(max_length=45)
    time = models.IntegerField()
    rate = models.IntegerField()
    pmem = models.CharField(max_length=45)
    size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bossraidtime'


class Bossremain(models.Model):
    charid = models.PositiveIntegerField()
    bossid = models.PositiveIntegerField()
    remain = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'bossremain'


class Buddies(models.Model):
    characterid = models.IntegerField()
    buddyid = models.IntegerField()
    pending = models.IntegerField()
    groupname = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'buddies'


class Burningfield(models.Model):
    number = models.AutoField(primary_key=True)
    burningmapid = models.IntegerField(db_column='burningMapId')  # Field name made lowercase.
    burningexprate = models.IntegerField(db_column='burningExpRate')  # Field name made lowercase.
    burningchannel = models.IntegerField(db_column='burningChannel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'burningfield'


class CharacterCards(models.Model):
    accid = models.IntegerField()
    worldid = models.IntegerField()
    characterid = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_cards'


class Charactercard(models.Model):
    accountid = models.IntegerField(primary_key=True)
    cardid = models.IntegerField()
    position = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'charactercard'


class Characters(models.Model):
    accountid = models.IntegerField()
    name = models.CharField(max_length=13)
    level = models.IntegerField()
    exp = models.BigIntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    luk = models.IntegerField()
    int = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    maxhp = models.IntegerField()
    maxmp = models.IntegerField()
    meso = models.BigIntegerField()
    hpapused = models.IntegerField(db_column='hpApUsed')  # Field name made lowercase.
    mpapused = models.IntegerField(db_column='mpApUsed')  # Field name made lowercase.
    job = models.IntegerField()
    skincolor = models.IntegerField()
    skincolor2 = models.IntegerField()
    gender = models.IntegerField()
    gender2 = models.IntegerField()
    fame = models.IntegerField()
    hair = models.PositiveIntegerField()
    hair2 = models.IntegerField()
    face = models.IntegerField()
    face2 = models.IntegerField()
    wp = models.IntegerField()
    askguildid = models.IntegerField()
    ap = models.IntegerField()
    map = models.IntegerField()
    spawnpoint = models.IntegerField()
    gm = models.IntegerField()
    party = models.IntegerField()
    buddycapacity = models.IntegerField(db_column='buddyCapacity')  # Field name made lowercase.
    createdate = models.DateTimeField()
    rank = models.PositiveIntegerField()
    rankmove = models.IntegerField(db_column='rankMove')  # Field name made lowercase.
    worldrank = models.PositiveIntegerField(db_column='worldRank')  # Field name made lowercase.
    worldrankmove = models.IntegerField(db_column='worldRankMove')  # Field name made lowercase.
    guildid = models.PositiveIntegerField()
    guildrank = models.PositiveIntegerField()
    alliancerank = models.PositiveIntegerField(db_column='allianceRank')  # Field name made lowercase.
    messengerid = models.PositiveIntegerField()
    messengerposition = models.PositiveIntegerField()
    monsterbookcover = models.PositiveIntegerField()
    subcategory = models.IntegerField(blank=True, null=True)
    reborns = models.PositiveIntegerField()
    sp = models.CharField(max_length=255)
    ambition = models.IntegerField()
    insight = models.IntegerField()
    willpower = models.IntegerField()
    diligence = models.IntegerField()
    empathy = models.IntegerField()
    charm = models.IntegerField()
    innerexp = models.PositiveIntegerField(db_column='innerExp')  # Field name made lowercase.
    innerlevel = models.PositiveIntegerField(db_column='innerLevel')  # Field name made lowercase.
    artifactpoints = models.IntegerField(db_column='artifactPoints')  # Field name made lowercase.
    morphgage = models.IntegerField(db_column='morphGage')  # Field name made lowercase.
    firstprofession = models.IntegerField(db_column='firstProfession')  # Field name made lowercase.
    secondprofession = models.IntegerField(db_column='secondProfession')  # Field name made lowercase.
    firstprofessionlevel = models.IntegerField(db_column='firstProfessionLevel')  # Field name made lowercase.
    secondprofessionlevel = models.IntegerField(db_column='secondProfessionLevel')  # Field name made lowercase.
    firstprofessionexp = models.IntegerField(db_column='firstProfessionExp')  # Field name made lowercase.
    secondprofessionexp = models.IntegerField(db_column='secondProfessionExp')  # Field name made lowercase.
    fatigue = models.IntegerField()
    last_command_time = models.BigIntegerField()
    pet_id = models.CharField(max_length=60)
    pet_loot = models.IntegerField()
    pet_mp = models.IntegerField()
    pet_hp = models.IntegerField()
    rankpoint = models.IntegerField()
    gp = models.IntegerField()
    soul = models.IntegerField()
    chatban = models.CharField(max_length=45)
    betaclothes = models.IntegerField()
    burning = models.IntegerField()
    loginpoint = models.IntegerField()
    damageskinslot = models.IntegerField(blank=True, null=True)
    savedamageskin = models.CharField(db_column='saveDamageSkin', max_length=250, blank=True, null=True)  # Field name made lowercase.
    nmixbasehaircolor = models.IntegerField(db_column='nMixBaseHairColor', blank=True, null=True)  # Field name made lowercase.
    nmixaddhaircolor = models.IntegerField(db_column='nMixAddHairColor', blank=True, null=True)  # Field name made lowercase.
    nmixhairbaseprob = models.IntegerField(db_column='nMixHairBaseProb', blank=True, null=True)  # Field name made lowercase.
    damage = models.BigIntegerField(blank=True, null=True)
    guildpoint = models.BigIntegerField(db_column='guildPoint', blank=True, null=True)  # Field name made lowercase.
    guildigp = models.IntegerField(db_column='guildIGP', blank=True, null=True)  # Field name made lowercase.
    itcafetime = models.IntegerField(blank=True, null=True)
    hope = models.CharField(max_length=45)
    damagehit = models.PositiveIntegerField()
    subjobcode = models.IntegerField(blank=True, null=True)
    subjoblevel = models.IntegerField(blank=True, null=True)
    subjobexp = models.BigIntegerField(blank=True, null=True)
    subjobname = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'characters'


class Code(models.Model):
    chrid = models.IntegerField()
    item = models.IntegerField()
    qua = models.IntegerField()
    code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code'


class Color(models.Model):
    cid = models.PositiveIntegerField()
    color = models.IntegerField()
    selection = models.TextField()

    class Meta:
        managed = False
        db_table = 'color'


class Coupon(models.Model):
    number = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    item = models.TextField(blank=True, null=True)
    itemn = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupon'


class Damagerank(models.Model):
    cid = models.PositiveIntegerField()
    name = models.CharField(max_length=45)
    damage = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'damagerank'


class DropData(models.Model):
    id = models.BigAutoField(primary_key=True)
    dropperid = models.IntegerField()
    itemid = models.IntegerField()
    minimum_quantity = models.IntegerField()
    maximum_quantity = models.IntegerField()
    questid = models.IntegerField()
    chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drop_data'


class DropDataGlobal(models.Model):
    id = models.BigAutoField(primary_key=True)
    continent = models.IntegerField()
    droptype = models.IntegerField(db_column='dropType')  # Field name made lowercase.
    itemid = models.IntegerField()
    minimum_quantity = models.IntegerField()
    maximum_quantity = models.IntegerField()
    questid = models.IntegerField()
    chance = models.IntegerField()
    comments = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drop_data_global'


class DropDataVana(models.Model):
    id = models.BigAutoField(primary_key=True)
    dropperid = models.IntegerField()
    flags = models.CharField(max_length=8)
    itemid = models.IntegerField()
    minimum_quantity = models.IntegerField()
    maximum_quantity = models.IntegerField()
    questid = models.IntegerField()
    chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drop_data_vana'


class Dueypackages(models.Model):
    packageid = models.AutoField(db_column='PackageId', primary_key=True)  # Field name made lowercase.
    recieverid = models.IntegerField(db_column='RecieverId')  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=13)  # Field name made lowercase.
    mesos = models.PositiveIntegerField(db_column='Mesos', blank=True, null=True)  # Field name made lowercase.
    timestamp = models.BigIntegerField(db_column='TimeStamp', blank=True, null=True)  # Field name made lowercase.
    checked = models.PositiveIntegerField(db_column='Checked', blank=True, null=True)  # Field name made lowercase.
    type = models.PositiveIntegerField(db_column='Type')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dueypackages'


class Eventstats(models.Model):
    eventstatid = models.AutoField(primary_key=True)
    event = models.CharField(max_length=30)
    instance = models.CharField(max_length=30)
    characterid = models.IntegerField()
    channel = models.IntegerField()
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eventstats'


class Extendedslots(models.Model):
    index = models.IntegerField()
    characterid = models.IntegerField()
    uniqueid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'extendedslots'


class Famelog(models.Model):
    famelogid = models.AutoField(primary_key=True)
    characterid = models.IntegerField()
    characterid_to = models.IntegerField()
    when = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'famelog'


class Fireitem(models.Model):
    value = models.AutoField(primary_key=True)
    uniqueid = models.IntegerField()
    mdef = models.IntegerField()
    mp = models.IntegerField()
    hp = models.IntegerField()
    wdef = models.IntegerField()
    speed = models.IntegerField()
    jump = models.IntegerField()
    fire = models.IntegerField()
    hands = models.IntegerField()
    avoid = models.IntegerField()
    acc = models.IntegerField()
    watk = models.IntegerField()
    matk = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    field_int = models.IntegerField(db_column='_int')  # Field renamed because it started with '_'.
    luk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fireitem'


class Force(models.Model):
    forceid = models.AutoField(primary_key=True)
    point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'force'


class Forcemap(models.Model):
    mapid = models.IntegerField()
    mobcount = models.IntegerField()
    force = models.IntegerField()
    channel = models.IntegerField()
    time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'forcemap'


class Futurehope(models.Model):
    cid = models.PositiveIntegerField()
    hope = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'futurehope'


class GamePollReply(models.Model):
    accountid = models.PositiveIntegerField(db_column='AccountId')  # Field name made lowercase.
    selectans = models.PositiveIntegerField(db_column='SelectAns')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'game_poll_reply'


class Guilds(models.Model):
    guildid = models.AutoField(primary_key=True)
    leader = models.PositiveIntegerField()
    gp = models.PositiveIntegerField(db_column='GP')  # Field name made lowercase.
    logo = models.PositiveIntegerField(blank=True, null=True)
    logocolor = models.PositiveSmallIntegerField(db_column='logoColor')  # Field name made lowercase.
    name = models.CharField(max_length=45)
    rank1title = models.CharField(max_length=45)
    rank2title = models.CharField(max_length=45)
    rank3title = models.CharField(max_length=45)
    rank4title = models.CharField(max_length=45)
    rank5title = models.CharField(max_length=45)
    capacity = models.PositiveIntegerField()
    logobg = models.PositiveIntegerField(db_column='logoBG', blank=True, null=True)  # Field name made lowercase.
    logobgcolor = models.PositiveSmallIntegerField(db_column='logoBGColor')  # Field name made lowercase.
    notice = models.CharField(max_length=101, blank=True, null=True)
    signature = models.IntegerField()
    alliance = models.PositiveIntegerField()
    guildlevel = models.PositiveIntegerField(db_column='guildLevel')  # Field name made lowercase.
    hoorexp = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guilds'


class Guildsills(models.Model):
    gid = models.AutoField(primary_key=True)
    skillid = models.PositiveIntegerField()
    time = models.BigIntegerField()
    buyer = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'guildsills'


class Guildskills(models.Model):
    guildid = models.PositiveIntegerField(blank=True, null=True)
    skillid = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.BigIntegerField(blank=True, null=True)
    purchaser = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'guildskills'


class Hardban(models.Model):
    serial = models.TextField()

    class Meta:
        managed = False
        db_table = 'hardban'


class Hiredmerch(models.Model):
    packageid = models.AutoField(db_column='PackageId', primary_key=True)  # Field name made lowercase.
    characterid = models.PositiveIntegerField(blank=True, null=True)
    accountid = models.PositiveIntegerField(blank=True, null=True)
    mesos = models.PositiveIntegerField(db_column='Mesos', blank=True, null=True)  # Field name made lowercase.
    time = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hiredmerch'


class Hiredmerchantsaveitems(models.Model):
    id = models.IntegerField(primary_key=True)
    merchid = models.IntegerField()
    uniqueid = models.IntegerField()
    bundle = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hiredmerchantsaveitems'


class Hiredmerchantsaves(models.Model):
    id = models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=100)
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    ownername = models.CharField(db_column='ownerName', max_length=30)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerId')  # Field name made lowercase.
    owneraccid = models.IntegerField(db_column='ownerAccid')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    map = models.IntegerField()
    channel = models.IntegerField()
    start = models.BigIntegerField()
    meso = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hiredmerchantsaves'


class Hns(models.Model):
    cid = models.IntegerField()
    win = models.IntegerField()
    lose = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hns'


class Htsquads(models.Model):
    channel = models.PositiveIntegerField()
    leaderid = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    members = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'htsquads'


class InnerAbilitySkills(models.Model):
    player_id = models.IntegerField()
    skill_id = models.IntegerField()
    skill_level = models.IntegerField()
    max_level = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inner_ability_skills'


class Invensave(models.Model):
    charid = models.PositiveIntegerField()
    upgradeslots = models.IntegerField()
    level = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    int = models.IntegerField()
    luk = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    watk = models.IntegerField()
    matk = models.IntegerField()
    wdef = models.IntegerField()
    mdef = models.IntegerField()
    acc = models.IntegerField()
    avoid = models.IntegerField()
    hands = models.IntegerField()
    speed = models.IntegerField()
    jump = models.IntegerField()
    vicioushammer = models.IntegerField(db_column='ViciousHammer')  # Field name made lowercase.
    itemlevel = models.IntegerField(db_column='itemLevel')  # Field name made lowercase.
    itemexp = models.IntegerField(db_column='itemEXP')  # Field name made lowercase.
    durability = models.IntegerField()
    enhance = models.SmallIntegerField()
    state = models.IntegerField()
    lines = models.IntegerField()
    potential1 = models.IntegerField()
    potential2 = models.IntegerField()
    potential3 = models.IntegerField()
    potential4 = models.IntegerField()
    potential5 = models.IntegerField()
    potential6 = models.IntegerField()
    anvil = models.IntegerField()
    hpr = models.SmallIntegerField(db_column='hpR')  # Field name made lowercase.
    mpr = models.SmallIntegerField(db_column='mpR')  # Field name made lowercase.
    potential7 = models.IntegerField()
    fire = models.IntegerField()
    downlevel = models.IntegerField()
    bossdmg = models.IntegerField()
    alldmgp = models.IntegerField()
    allstatp = models.IntegerField()
    ignorewdef = models.IntegerField(db_column='IgnoreWdef')  # Field name made lowercase.
    soulname = models.IntegerField()
    soulenchanter = models.IntegerField()
    soulpotential = models.IntegerField()
    soulskill = models.IntegerField()
    starforce = models.IntegerField()
    itemtrace = models.IntegerField()
    firestat = models.CharField(max_length=128)
    itemid = models.IntegerField()
    confirm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invensave'


class Invensave2(models.Model):
    charid = models.IntegerField()
    itemid = models.IntegerField()
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    confirm = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invensave2'


class Inventoryequipment(models.Model):
    inventoryequipmentid = models.AutoField(primary_key=True)
    inventoryitemid = models.PositiveIntegerField()
    upgradeslots = models.IntegerField()
    level = models.IntegerField()
    str = models.IntegerField()
    dex = models.IntegerField()
    int = models.IntegerField()
    luk = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    watk = models.IntegerField()
    matk = models.IntegerField()
    wdef = models.IntegerField()
    mdef = models.IntegerField()
    acc = models.IntegerField()
    avoid = models.IntegerField()
    hands = models.IntegerField()
    speed = models.IntegerField()
    jump = models.IntegerField()
    vicioushammer = models.IntegerField(db_column='ViciousHammer')  # Field name made lowercase.
    itemlevel = models.IntegerField(db_column='itemLevel')  # Field name made lowercase.
    itemexp = models.IntegerField(db_column='itemEXP')  # Field name made lowercase.
    durability = models.IntegerField()
    enhance = models.SmallIntegerField()
    state = models.IntegerField()
    lines = models.IntegerField()
    potential1 = models.IntegerField()
    potential2 = models.IntegerField()
    potential3 = models.IntegerField()
    potential4 = models.IntegerField()
    potential5 = models.IntegerField()
    potential6 = models.IntegerField()
    anvil = models.IntegerField()
    hpr = models.SmallIntegerField(db_column='hpR')  # Field name made lowercase.
    mpr = models.SmallIntegerField(db_column='mpR')  # Field name made lowercase.
    potential7 = models.IntegerField()
    fire = models.IntegerField()
    downlevel = models.IntegerField()
    bossdmg = models.IntegerField()
    alldmgp = models.IntegerField()
    allstatp = models.IntegerField()
    ignorewdef = models.IntegerField(db_column='IgnoreWdef')  # Field name made lowercase.
    soulname = models.IntegerField()
    soulenchanter = models.IntegerField()
    soulpotential = models.IntegerField()
    soulskill = models.IntegerField()
    starforce = models.IntegerField()
    itemtrace = models.IntegerField()
    firestat = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'inventoryequipment'


class Inventoryitems(models.Model):
    inventoryitemid = models.AutoField(primary_key=True)
    type = models.IntegerField()
    characterid = models.IntegerField(blank=True, null=True)
    accountid = models.IntegerField()
    packageid = models.IntegerField(db_column='packageId')  # Field name made lowercase.
    itemid = models.IntegerField()
    inventorytype = models.IntegerField()
    position = models.IntegerField()
    quantity = models.IntegerField()
    owner = models.TextField(blank=True, null=True)
    gm_log = models.TextField(db_column='GM_Log', blank=True, null=True)  # Field name made lowercase.
    uniqueid = models.IntegerField()
    flag = models.IntegerField()
    expiredate = models.BigIntegerField()
    giftfrom = models.CharField(db_column='giftFrom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    iscash = models.IntegerField(db_column='isCash')  # Field name made lowercase.
    ispet = models.IntegerField(db_column='isPet')  # Field name made lowercase.
    isandroid = models.IntegerField(db_column='isAndroid')  # Field name made lowercase.
    issale = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventoryitems'


class Inventorylog(models.Model):
    inventorylogid = models.AutoField(primary_key=True)
    inventoryitemid = models.PositiveIntegerField()
    msg = models.TextField()

    class Meta:
        managed = False
        db_table = 'inventorylog'


class Inventoryslot(models.Model):
    characterid = models.PositiveIntegerField(blank=True, null=True)
    equip = models.PositiveIntegerField(blank=True, null=True)
    use = models.PositiveIntegerField(blank=True, null=True)
    setup = models.PositiveIntegerField(blank=True, null=True)
    etc = models.PositiveIntegerField(blank=True, null=True)
    cash = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventoryslot'


class Ipbans(models.Model):
    ipbanid = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ipbans'


class Itempot(models.Model):
    cid = models.IntegerField()
    lifeid = models.IntegerField()
    slot = models.IntegerField()
    level = models.IntegerField()
    status = models.IntegerField()
    fullness = models.IntegerField()
    closeness = models.IntegerField()
    starttime = models.BigIntegerField()
    sleeptime = models.BigIntegerField()
    inccloseleft = models.IntegerField(db_column='incCloseLeft')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itempot'


class Keymap(models.Model):
    characterid = models.IntegerField()
    key = models.IntegerField()
    type = models.IntegerField()
    action = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'keymap'


class Keyvalue(models.Model):
    cid = models.IntegerField()
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'keyvalue'


class Keyvalue2(models.Model):
    cid = models.IntegerField()
    key = models.CharField(max_length=100)
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'keyvalue2'


class Learnexp(models.Model):
    accid = models.IntegerField()
    exp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'learnexp'


class LinkSkill(models.Model):
    skillid = models.PositiveIntegerField()
    skilllevel = models.PositiveIntegerField(db_column='skillLevel')  # Field name made lowercase.
    link_cid = models.PositiveIntegerField()
    cid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'link_skill'


class Macbans(models.Model):
    macbanid = models.AutoField(primary_key=True)
    mac = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'macbans'


class Macfilters(models.Model):
    macfilterid = models.AutoField(primary_key=True)
    filter = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'macfilters'


class Marri(models.Model):
    cid = models.IntegerField()
    pid = models.IntegerField()
    time = models.BigIntegerField()
    pname = models.CharField(max_length=50)
    ringid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'marri'


class Medalranking(models.Model):
    cid = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'medalranking'


class Memo(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    title = models.TextField()
    date = models.CharField(max_length=64, blank=True, null=True)
    memo = models.TextField()
    reply = models.TextField()

    class Meta:
        managed = False
        db_table = 'memo'


class Monsterbook(models.Model):
    charid = models.PositiveIntegerField()
    cardid = models.PositiveIntegerField()
    level = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monsterbook'


class Mountdata(models.Model):
    characterid = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(db_column='Level')  # Field name made lowercase.
    exp = models.PositiveIntegerField(db_column='Exp')  # Field name made lowercase.
    fatigue = models.PositiveIntegerField(db_column='Fatigue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mountdata'


class Mulung(models.Model):
    name = models.CharField(max_length=50)
    time = models.BigIntegerField()
    timestring = models.CharField(db_column='timeString', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mulung'


class Mulungdojo(models.Model):
    charid = models.IntegerField()
    stage = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mulungdojo'


class Notes(models.Model):
    to = models.CharField(max_length=13)
    from_field = models.CharField(db_column='from', max_length=13)  # Field renamed because it was a Python reserved word.
    message = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'notes'


class Nxcode(models.Model):
    code = models.CharField(primary_key=True, max_length=15)
    valid = models.IntegerField()
    user = models.CharField(max_length=13, blank=True, null=True)
    type = models.IntegerField()
    item = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nxcode'


class Parttime(models.Model):
    cid = models.PositiveIntegerField()
    job = models.PositiveIntegerField()
    starttime = models.BigIntegerField()
    reward = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'parttime'


class Party(models.Model):
    name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    recom = models.IntegerField(blank=True, null=True)
    recomp = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'party'


class Pets(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=13, blank=True, null=True)
    level = models.PositiveIntegerField()
    closeness = models.PositiveIntegerField()
    fullness = models.PositiveIntegerField()
    pet_skill = models.CharField(max_length=70)
    expiredate = models.BigIntegerField()
    pet_buff = models.IntegerField()
    color = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pets'


class Playernpcs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=13)
    hair = models.IntegerField()
    face = models.IntegerField()
    skin = models.IntegerField()
    dir = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    map = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'playernpcs'


class PlayernpcsEquip(models.Model):
    npcid = models.IntegerField()
    equipid = models.IntegerField()
    equippos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'playernpcs_equip'


class Questactions(models.Model):
    questactionid = models.AutoField(primary_key=True)
    questid = models.IntegerField()
    status = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'questactions'


class Questinfo(models.Model):
    questinfoid = models.AutoField(primary_key=True)
    characterid = models.IntegerField()
    quest = models.IntegerField()
    data = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questinfo'


class Questrequirements(models.Model):
    questrequirementid = models.AutoField(primary_key=True)
    questid = models.IntegerField()
    status = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'questrequirements'


class Queststatus(models.Model):
    queststatusid = models.AutoField(primary_key=True)
    characterid = models.IntegerField()
    quest = models.IntegerField()
    status = models.IntegerField()
    time = models.IntegerField()
    forfeited = models.IntegerField()
    customdata = models.CharField(db_column='customData', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'queststatus'


class Queststatusmobs(models.Model):
    queststatusmobid = models.AutoField(primary_key=True)
    queststatusid = models.PositiveIntegerField()
    mob = models.IntegerField()
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'queststatusmobs'


class Quickslot(models.Model):
    cid = models.IntegerField()
    index = models.IntegerField()
    key = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'quickslot'


class Raed(models.Model):
    name = models.TextField()
    ran = models.TextField()
    countta = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'raed'


class Reactordrops(models.Model):
    reactordropid = models.AutoField(primary_key=True)
    reactorid = models.IntegerField()
    itemid = models.IntegerField()
    chance = models.IntegerField()
    questid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reactordrops'


class Receivedaccount(models.Model):
    accid = models.IntegerField()
    itemid = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receivedaccount'


class RecomLog(models.Model):
    name = models.TextField(blank=True, null=True)
    recom = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recom_log'


class Reports(models.Model):
    reporttime = models.DateTimeField()
    reporterid = models.IntegerField()
    victimid = models.IntegerField()
    reason = models.IntegerField()
    chatlog = models.TextField()
    status = models.TextField()

    class Meta:
        managed = False
        db_table = 'reports'


class Rewardsaves(models.Model):
    cid = models.IntegerField()
    itemid = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rewardsaves'


class Rings(models.Model):
    ringid = models.IntegerField(db_column='ringId')  # Field name made lowercase.
    itemid = models.IntegerField()
    partnerchrid = models.IntegerField(db_column='partnerChrId')  # Field name made lowercase.
    partnername = models.CharField(db_column='partnerName', max_length=255)  # Field name made lowercase.
    partnerringid = models.IntegerField(db_column='partnerRingId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rings'


class Savedlocations(models.Model):
    characterid = models.IntegerField()
    locationtype = models.IntegerField()
    map = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'savedlocations'


class Send(models.Model):
    name = models.TextField(blank=True, null=True)
    itemid = models.TextField(blank=True, null=True)
    itemop = models.TextField(blank=True, null=True)
    name2 = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    itime = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'send'


class Serialbans(models.Model):
    serial = models.TextField()

    class Meta:
        managed = False
        db_table = 'serialbans'


class Shopitems(models.Model):
    shopitemid = models.AutoField(primary_key=True)
    shopid = models.PositiveIntegerField()
    itemid = models.IntegerField()
    price = models.IntegerField()
    position = models.IntegerField()
    pricequantity = models.IntegerField()
    tab = models.IntegerField(db_column='Tab')  # Field name made lowercase.
    quantity = models.IntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shopitems'


class Shops(models.Model):
    shopid = models.AutoField(primary_key=True)
    npcid = models.IntegerField(blank=True, null=True)
    usage = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'shops'


class Skillmacros(models.Model):
    characterid = models.IntegerField()
    position = models.IntegerField()
    skill1 = models.IntegerField()
    skill2 = models.IntegerField()
    skill3 = models.IntegerField()
    name = models.CharField(max_length=13, blank=True, null=True)
    shout = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'skillmacros'


class Skills(models.Model):
    skillid = models.IntegerField()
    characterid = models.IntegerField()
    skilllevel = models.IntegerField()
    masterlevel = models.IntegerField()
    expiration = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'skills'


class SkillsCooldowns(models.Model):
    charid = models.IntegerField()
    skillid = models.IntegerField(db_column='SkillID')  # Field name made lowercase.
    length = models.BigIntegerField()
    starttime = models.BigIntegerField(db_column='StartTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'skills_cooldowns'


class Spawn(models.Model):
    lifeid = models.IntegerField()
    rx0 = models.IntegerField()
    rx1 = models.IntegerField()
    cy = models.IntegerField()
    fh = models.IntegerField()
    type = models.CharField(max_length=11)
    dir = models.IntegerField()
    mapid = models.IntegerField()
    mobtime = models.IntegerField(db_column='mobTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spawn'


class SpawnsProfession(models.Model):
    idd = models.IntegerField()
    f = models.IntegerField()
    fh = models.IntegerField()
    type = models.CharField(max_length=1)
    cy = models.IntegerField()
    rx0 = models.IntegerField()
    rx1 = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    mobtime = models.IntegerField(blank=True, null=True)
    mid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spawns_profession'


class Steelskills(models.Model):
    cid = models.IntegerField()
    skillid = models.IntegerField()
    skilllevel = models.IntegerField()
    index = models.IntegerField()
    slot = models.IntegerField()
    equipped = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'steelskills'


class Storages(models.Model):
    storageid = models.AutoField(primary_key=True)
    accountid = models.IntegerField()
    slots = models.IntegerField()
    meso = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'storages'


class TradeCm(models.Model):
    chr_name = models.TextField(blank=True, null=True)
    from_name = models.TextField(blank=True, null=True)
    cash = models.IntegerField(blank=True, null=True)
    meso = models.TextField(blank=True, null=True)
    confirm = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trade_cm'


class Trocklocations(models.Model):
    trockid = models.AutoField(primary_key=True)
    characterid = models.IntegerField(blank=True, null=True)
    mapid = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trocklocations'


class WebsiteEvents(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=16)
    date = models.CharField(max_length=32)
    type = models.CharField(max_length=100)
    status = models.CharField(max_length=32)
    content = models.TextField()
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website_events'


class WebsiteNews(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=16)
    date = models.CharField(max_length=32)
    type = models.CharField(max_length=50)
    content = models.TextField()
    views = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'website_news'


class Wishlist(models.Model):
    characterid = models.IntegerField()
    sn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wishlist'
