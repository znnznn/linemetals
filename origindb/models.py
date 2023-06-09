# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arinv(models.Model):
    arinv_guid = models.CharField(db_column='ARINV_GUID', primary_key=True, max_length=36)
    recno5 = models.IntegerField(db_column='RECNO5')
    id = models.CharField(db_column='ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(db_column='NAME', max_length=86, db_collation='SQL_Latin1_General_CP1_CI_AS')
    address1 = models.CharField(db_column='ADDRESS1', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')
    address2 = models.CharField(db_column='ADDRESS2', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')
    city = models.CharField(db_column='CITY', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    state = models.CharField(db_column='STATE', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')
    zip = models.CharField(db_column='ZIP', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS')
    invoice = models.CharField(db_column='INVOICE', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descr = models.CharField(db_column='DESCR', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    inv_date = models.DateField(db_column='INV_DATE', blank=True, null=True)
    due_date = models.DateField(db_column='DUE_DATE', blank=True, null=True)
    dis_date = models.DateField(db_column='DIS_DATE', blank=True, null=True)
    iddiscount = models.CharField(db_column='IDDISCOUNT', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    idcharge = models.CharField(db_column='IDCHARGE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    discoun = models.CharField(db_column='DISCOUN', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')
    charge = models.CharField(db_column='CHARGE', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')
    terms = models.CharField(db_column='TERMS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')
    in_level = models.CharField(db_column='IN_LEVEL', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    po_no = models.CharField(db_column='PO_NO', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    salesman = models.CharField(db_column='SALESMAN', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ship_via = models.CharField(db_column='SHIP_VIA', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    e_date = models.DateField(db_column='E_DATE', blank=True, null=True)
    discount = models.DecimalField(db_column='DISCOUNT', max_digits=14, decimal_places=2)
    overdue = models.DecimalField(db_column='OVERDUE', max_digits=14, decimal_places=2)
    freight = models.DecimalField(db_column='FREIGHT', max_digits=14, decimal_places=2)
    tax = models.DecimalField(db_column='TAX', max_digits=14, decimal_places=2)
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=14, decimal_places=2)
    total = models.DecimalField(db_column='TOTAL', max_digits=14, decimal_places=2)
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')
    total_paid = models.DecimalField(db_column='TOTAL_PAID', max_digits=14, decimal_places=2)
    total_w = models.DecimalField(db_column='TOTAL_W', max_digits=14, decimal_places=2)
    balance = models.DecimalField(db_column='BALANCE', max_digits=14, decimal_places=2)
    check_no = models.CharField(db_column='CHECK_NO', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    check_date = models.DateField(db_column='CHECK_DATE', blank=True, null=True)
    c_id = models.CharField(db_column='C_ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_name = models.CharField(db_column='C_NAME', max_length=86, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_address1 = models.CharField(db_column='C_ADDRESS1', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_address2 = models.CharField(db_column='C_ADDRESS2', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_city = models.CharField(db_column='C_CITY', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_state = models.CharField(db_column='C_STATE', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_zip = models.CharField(db_column='C_ZIP', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(db_column='EMAIL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    billing_co = models.CharField(db_column='BILLING_CO', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ship_date = models.DateField(db_column='SHIP_DATE', blank=True, null=True)
    frght_amt = models.CharField(db_column='FRGHT_AMT', max_length=90, db_collation='SQL_Latin1_General_CP1_CI_AS')
    frght_type = models.CharField(db_column='FRGHT_TYPE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    user_name = models.CharField(db_column='USER_NAME', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    was_proc = models.BooleanField(db_column='WAS_PROC')
    memo = models.TextField(db_column='MEMO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    signature = models.BinaryField(db_column='SIGNATURE', blank=True, null=True)
    country = models.CharField(db_column='COUNTRY', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_country = models.CharField(db_column='C_COUNTRY', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    close_date = models.DateField(db_column='CLOSE_DATE', blank=True, null=True)
    so_tax = models.DecimalField(db_column='SO_TAX', max_digits=14, decimal_places=2)
    man_tax = models.BooleanField(db_column='MAN_TAX')
    orig_inv = models.CharField(db_column='ORIG_INV', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    orig_aid = models.CharField(db_column='ORIG_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    print_time = models.CharField(db_column='PRINT_TIME', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_fr_order = models.BooleanField(db_column='C_FR_ORDER')
    crea_date = models.DateField(db_column='CREA_DATE', blank=True, null=True)
    crea_time = models.CharField(db_column='CREA_TIME', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    proc_date = models.DateField(db_column='PROC_DATE', blank=True, null=True)
    proc_time = models.CharField(db_column='PROC_TIME', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ar_trade = models.CharField(db_column='AR_TRADE', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    freight_gl = models.CharField(db_column='FREIGHT_GL', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    finance = models.CharField(db_column='FINANCE', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cust_disc = models.CharField(db_column='CUST_DISC', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    down_pay = models.CharField(db_column='DOWN_PAY', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    def_dept = models.CharField(db_column='DEF_DEPT', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')
    warehouse = models.CharField(db_column='WAREHOUSE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    autoid = models.CharField(db_column='AUTOID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    csend_date = models.DateField(db_column='CSEND_DATE', blank=True, null=True)
    csend_time = models.CharField(db_column='CSEND_TIME', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS')
    csend_mes = models.TextField(db_column='CSEND_MES', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    c_rate = models.DecimalField(db_column='C_RATE', max_digits=15, decimal_places=5)
    curr_id = models.CharField(db_column='CURR_ID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')
    copied = models.BooleanField(db_column='COPIED')
    prevord = models.CharField(db_column='PREVORD', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    trim = models.BooleanField(db_column='TRIM')
    metal = models.BooleanField(db_column='METAL')
    div_aid = models.CharField(db_column='DIV_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    authorized = models.DecimalField(db_column='AUTHORIZED', max_digits=14, decimal_places=2)
    web_sale = models.BooleanField(db_column='WEB_SALE')
    phone = models.CharField(db_column='PHONE', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    web_aid = models.CharField(db_column='WEB_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cf_email = models.CharField(db_column='CF_EMAIL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cf_sent = models.BooleanField(db_column='CF_SENT')
    rollexdt = models.DateField(db_column='ROLLEXDT', blank=True, null=True)
    rollprocdt = models.DateField(db_column='ROLLPROCDT', blank=True, null=True)
    c_email = models.CharField(db_column='C_EMAIL', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_phone = models.CharField(db_column='C_PHONE', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_print = models.CharField(db_column='LAST_PRINT', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    handling = models.DecimalField(db_column='HANDLING', max_digits=14, decimal_places=2)
    freightexp = models.TextField(db_column='FREIGHTEXP', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ly_pts_got = models.DecimalField(db_column='LY_PTS_GOT', max_digits=14, decimal_places=2)
    to_b_sent = models.BooleanField(db_column='TO_B_SENT')
    internalnt = models.TextField(db_column='INTERNALNT', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    out_city = models.BooleanField(db_column='OUT_CITY')
    c_tax = models.DecimalField(db_column='C_TAX', max_digits=14, decimal_places=2)
    c_manual = models.BooleanField(db_column='C_MANUAL')
    arpw_id = models.CharField(db_column='ARPW_ID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    comis_paid = models.BooleanField(db_column='COMIS_PAID')
    job_id = models.CharField(db_column='JOB_ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    num_bill = models.CharField(db_column='NUM_BILL', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')
    use_jobret = models.BooleanField(db_column='USE_JOBRET')
    from_tandm = models.BooleanField(db_column='FROM_TANDM')
    subilnoret = models.DecimalField(db_column='SUBILNORET', max_digits=14, decimal_places=2)
    arqtaidsrc = models.CharField(db_column='ARQTAIDSRC', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    usetaxed = models.BooleanField(db_column='USETAXED')
    cntct_aid = models.CharField(db_column='CNTCT_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ccntct_aid = models.CharField(db_column='CCNTCT_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    man_usetax = models.BooleanField(db_column='MAN_USETAX')
    externalid = models.CharField(db_column='EXTERNALID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    p_rounddif = models.DecimalField(db_column='P_ROUNDDIF', max_digits=14, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ARINV'


class Arinvdet(models.Model):
    arinvdet_guid = models.CharField(db_column='ARINVDET_GUID', primary_key=True, max_length=36)
    recno5 = models.IntegerField(db_column='RECNO5')
    invoice = models.CharField(db_column='INVOICE', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    id = models.CharField(db_column='ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    doc_type = models.CharField(db_column='DOC_TYPE', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')
    doc_aid = models.CharField(db_column='DOC_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    inv_date = models.DateField(db_column='INV_DATE', blank=True, null=True)
    quan = models.DecimalField(db_column='QUAN', max_digits=22, decimal_places=6)
    ship = models.DecimalField(db_column='SHIP', max_digits=22, decimal_places=6)
    m_quan = models.DecimalField(db_column='M_QUAN', max_digits=22, decimal_places=6)
    orig_quan = models.DecimalField(db_column='ORIG_QUAN', max_digits=22, decimal_places=6)
    inven = models.CharField(db_column='INVEN', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_type = models.DecimalField(db_column='C_TYPE', max_digits=2, decimal_places=0)
    unit_meas = models.CharField(db_column='UNIT_MEAS', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descr = models.TextField(db_column='DESCR', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    unit = models.DecimalField(db_column='UNIT', max_digits=22, decimal_places=6)
    price = models.DecimalField(db_column='PRICE', max_digits=14, decimal_places=2)
    so_amount = models.DecimalField(db_column='SO_AMOUNT', max_digits=14, decimal_places=2)
    discount = models.DecimalField(db_column='DISCOUNT', max_digits=14, decimal_places=2)
    sodiscount = models.DecimalField(db_column='SODISCOUNT', max_digits=14, decimal_places=2)
    timestamp = models.CharField(db_column='TIMESTAMP', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    par_time = models.CharField(db_column='PAR_TIME', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    gpar_time = models.CharField(db_column='GPAR_TIME', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    status = models.DecimalField(db_column='STATUS', max_digits=1, decimal_places=0)
    u_cost = models.DecimalField(db_column='U_COST', max_digits=18, decimal_places=4)
    costs = models.DecimalField(db_column='COSTS', max_digits=14, decimal_places=2)
    tax_group = models.CharField(db_column='TAX_GROUP', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    exm_overid = models.CharField(db_column='EXM_OVERID', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ship_date = models.DateField(db_column='SHIP_DATE', blank=True, null=True)
    weight = models.DecimalField(db_column='WEIGHT', max_digits=14, decimal_places=2)
    print = models.BooleanField(db_column='PRINT')
    ap_partime = models.CharField(db_column='AP_PARTIME', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    print_quan = models.BooleanField(db_column='PRINT_QUAN')
    print_uom = models.BooleanField(db_column='PRINT_UOM')
    account = models.CharField(db_column='ACCOUNT', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    warehouse = models.CharField(db_column='WAREHOUSE', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    autoid = models.CharField(db_column='AUTOID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pcm_type = models.DecimalField(db_column='PCM_TYPE', max_digits=1, decimal_places=0)
    pcm_perc = models.DecimalField(db_column='PCM_PERC', max_digits=8, decimal_places=2)
    mto = models.BooleanField(db_column='MTO')
    mto_d_sync = models.BooleanField(db_column='MTO_D_SYNC')
    drop_ven = models.CharField(db_column='DROP_VEN', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    drop_part = models.CharField(db_column='DROP_PART', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    drop_aid = models.CharField(db_column='DROP_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    purc_meth = models.DecimalField(db_column='PURC_METH', max_digits=1, decimal_places=0)
    c_price = models.DecimalField(db_column='C_PRICE', max_digits=22, decimal_places=6)
    c_unit = models.DecimalField(db_column='C_UNIT', max_digits=22, decimal_places=6)
    fxline = models.BooleanField(db_column='FXLINE')
    c_formula = models.TextField(db_column='C_FORMULA', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    width = models.CharField(db_column='WIDTH', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')
    widthd = models.DecimalField(db_column='WIDTHD', max_digits=22, decimal_places=6)
    height = models.CharField(db_column='HEIGHT', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')
    heightd = models.DecimalField(db_column='HEIGHTD', max_digits=22, decimal_places=6)
    dem = models.CharField(db_column='DEM', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')
    demd = models.DecimalField(db_column='DEMD', max_digits=22, decimal_places=6)
    manual_p = models.BooleanField(db_column='MANUAL_P')
    manual_c = models.BooleanField(db_column='MANUAL_C')
    round = models.DecimalField(db_column='ROUND', max_digits=13, decimal_places=5)
    comment = models.CharField(db_column='COMMENT', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ea_quan = models.DecimalField(db_column='EA_QUAN', max_digits=21, decimal_places=6)
    r_ea_quan = models.DecimalField(db_column='R_EA_QUAN', max_digits=21, decimal_places=6)
    report_n = models.CharField(db_column='REPORT_N', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    random_w = models.BooleanField(db_column='RANDOM_W')
    random_h = models.BooleanField(db_column='RANDOM_H')
    item_num = models.CharField(db_column='ITEM_NUM', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    feet = models.DecimalField(db_column='FEET', max_digits=9, decimal_places=0)
    inchesd = models.DecimalField(db_column='INCHESD', max_digits=18, decimal_places=6)
    inches = models.CharField(db_column='INCHES', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_mfg = models.DecimalField(db_column='C_MFG', max_digits=14, decimal_places=2)
    r_serial = models.CharField(db_column='R_SERIAL', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    su_autoid = models.CharField(db_column='SU_AUTOID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    trade_in = models.BooleanField(db_column='TRADE_IN')
    in_level = models.CharField(db_column='IN_LEVEL', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    job_id = models.CharField(db_column='JOB_ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jobstg_id = models.CharField(db_column='JOBSTG_ID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    aia = models.CharField(db_column='AIA', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    retn_type = models.CharField(db_column='RETN_TYPE', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')
    retn_perc = models.DecimalField(db_column='RETN_PERC', max_digits=8, decimal_places=2)
    int_note = models.TextField(db_column='INT_NOTE', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    tax_expl = models.TextField(db_column='TAX_EXPL', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    on_site = models.DecimalField(db_column='ON_SITE', max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ARINVDET'


class Inprodtype(models.Model):
    inprodtype_guid = models.CharField(db_column='INPRODTYPE_GUID', primary_key=True, max_length=36)
    recno5 = models.IntegerField(db_column='RECNO5', unique=True)
    prod_type = models.CharField(db_column='PROD_TYPE', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ar_aid = models.CharField(db_column='AR_AID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    autoid = models.CharField(db_column='AUTOID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'INPRODTYPE'
        app_label = "origindb"
        verbose_name = 'inprodtype'


class Inventry(models.Model):
    inventry_guid = models.CharField(db_column='INVENTRY_GUID', primary_key=True, max_length=36)
    recno5 = models.IntegerField(db_column='RECNO5')
    id = models.CharField(db_column='ID', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    tree_id = models.CharField(db_column='TREE_ID', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')
    upc = models.CharField(db_column='UPC', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    type = models.CharField(db_column='TYPE', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    c_type = models.DecimalField(db_column='C_TYPE', max_digits=2, decimal_places=0)
    descr_1 = models.CharField(db_column='DESCR_1', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descr_1prn = models.BooleanField(db_column='DESCR_1PRN')
    descr_1prp = models.BooleanField(db_column='DESCR_1PRP')
    descr_2 = models.CharField(db_column='DESCR_2', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descr_2prn = models.BooleanField(db_column='DESCR_2PRN')
    descr_2prp = models.BooleanField(db_column='DESCR_2PRP')
    descr_3 = models.TextField(db_column='DESCR_3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    descr_3prn = models.BooleanField(db_column='DESCR_3PRN')
    descr_3prp = models.BooleanField(db_column='DESCR_3PRP')
    markup = models.CharField(db_column='MARKUP', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')
    markup_id = models.CharField(db_column='MARKUP_ID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    base = models.DecimalField(db_column='BASE', max_digits=14, decimal_places=2)
    cost = models.DecimalField(db_column='COST', max_digits=18, decimal_places=4)
    tax_group = models.CharField(db_column='TAX_GROUP', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    weight = models.DecimalField(db_column='WEIGHT', max_digits=14, decimal_places=2)
    date = models.DateField(db_column='DATE', blank=True, null=True)
    quan2order = models.DecimalField(db_column='QUAN2ORDER', max_digits=14, decimal_places=2)
    count = models.DecimalField(db_column='COUNT', max_digits=22, decimal_places=6)
    location = models.CharField(db_column='LOCATION', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    min_inven = models.DecimalField(db_column='MIN_INVEN', max_digits=14, decimal_places=2)
    max_inven = models.DecimalField(db_column='MAX_INVEN', max_digits=14, decimal_places=2)
    order_amt = models.DecimalField(db_column='ORDER_AMT', max_digits=14, decimal_places=2)
    pri_vendor = models.CharField(db_column='PRI_VENDOR', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    pur_o = models.DecimalField(db_column='PUR_O', max_digits=22, decimal_places=6)
    pur_s = models.DecimalField(db_column='PUR_S', max_digits=22, decimal_places=6)
    sales_o = models.DecimalField(db_column='SALES_O', max_digits=22, decimal_places=6)
    sales_s = models.DecimalField(db_column='SALES_S', max_digits=22, decimal_places=6)
    m_in_o = models.DecimalField(db_column='M_IN_O', max_digits=22, decimal_places=6)
    m_in_s = models.DecimalField(db_column='M_IN_S', max_digits=22, decimal_places=6)
    m_out_o = models.DecimalField(db_column='M_OUT_O', max_digits=22, decimal_places=6)
    m_out_s = models.DecimalField(db_column='M_OUT_S', max_digits=22, decimal_places=6)
    job_out_o = models.DecimalField(db_column='JOB_OUT_O', max_digits=22, decimal_places=6)
    job_out_s = models.DecimalField(db_column='JOB_OUT_S', max_digits=22, decimal_places=6)
    each_unit = models.CharField(db_column='EACH_UNIT', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    int_quan = models.BooleanField(db_column='INT_QUAN')
    def_unit = models.CharField(db_column='DEF_UNIT', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_chk_u = models.CharField(db_column='LAST_CHK_U', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_chk_d = models.DateField(db_column='LAST_CHK_D', blank=True, null=True)
    last_chk_t = models.CharField(db_column='LAST_CHK_T', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS')
    auto_cost = models.BooleanField(db_column='AUTO_COST')
    memo = models.TextField(db_column='MEMO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    mfg = models.CharField(db_column='MFG', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    mfg_part = models.CharField(db_column='MFG_PART', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    web = models.TextField(db_column='WEB', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    est_hours = models.DecimalField(db_column='EST_HOURS', max_digits=14, decimal_places=2)
    def_work = models.CharField(db_column='DEF_WORK', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    perc_adj = models.DecimalField(db_column='PERC_ADJ', max_digits=9, decimal_places=2)
    perc_adj_c = models.DecimalField(db_column='PERC_ADJ_C', max_digits=1, decimal_places=0)
    pur_memo = models.TextField(db_column='PUR_MEMO', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    sale_class = models.CharField(db_column='SALE_CLASS', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    updatecost = models.BooleanField(db_column='UPDATECOST')
    updvencost = models.BooleanField(db_column='UPDVENCOST')
    ins_acc = models.DecimalField(db_column='INS_ACC', max_digits=1, decimal_places=0)
    returndays = models.CharField(db_column='RETURNDAYS', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    sale_acc = models.CharField(db_column='SALE_ACC', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    use_pl_gl = models.BooleanField(db_column='USE_PL_GL')
    pur_acc = models.CharField(db_column='PUR_ACC', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    adjust = models.CharField(db_column='ADJUST', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')
    asset = models.CharField(db_column='ASSET', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    use_itemgl = models.BooleanField(db_column='USE_ITEMGL')
    mfg_cost = models.CharField(db_column='MFG_COST', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    autoid = models.CharField(db_column='AUTOID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    fixed_cost = models.BooleanField(db_column='FIXED_COST')
    adj_inven = models.CharField(db_column='ADJ_INVEN', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    autoserial = models.BooleanField(db_column='AUTOSERIAL')  # Field name made lowercase.
    weigh_it = models.BooleanField(db_column='WEIGH_IT')
    def_type = models.CharField(db_column='DEF_TYPE', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ent_task = models.BooleanField(db_column='ENT_TASK')
    purc_meth = models.DecimalField(db_column='PURC_METH', max_digits=1, decimal_places=0)
    pur_ssed = models.BooleanField(db_column='PUR_SSED')
    s_cust_i = models.CharField(db_column='S_CUST_I', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    d_width = models.DecimalField(db_column='D_WIDTH', max_digits=16, decimal_places=4)
    d_height = models.DecimalField(db_column='D_HEIGHT', max_digits=16, decimal_places=4)
    d_dem = models.DecimalField(db_column='D_DEM', max_digits=16, decimal_places=4)
    width = models.DecimalField(db_column='WIDTH', max_digits=16, decimal_places=4)
    width_r = models.BooleanField(db_column='WIDTH_R')
    height = models.DecimalField(db_column='HEIGHT', max_digits=16, decimal_places=4)
    height_r = models.BooleanField(db_column='HEIGHT_R')
    dem = models.DecimalField(db_column='DEM', max_digits=16, decimal_places=4)
    dem_r = models.BooleanField(db_column='DEM_R')
    waste_p = models.DecimalField(db_column='WASTE_P', max_digits=12, decimal_places=4)
    item_num = models.BooleanField(db_column='ITEM_NUM')
    d_replace = models.BooleanField(db_column='D_REPLACE')
    trade_in = models.BooleanField(db_column='TRADE_IN')
    trade_acc = models.CharField(db_column='TRADE_ACC', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS')
    su_autoid = models.CharField(db_column='SU_AUTOID', max_length=16, db_collation='SQL_Latin1_General_CP1_CI_AS')
    show_stock = models.CharField(db_column='SHOW_STOCK', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    ostk_msg = models.CharField(db_column='OSTK_MSG', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS')
    hide_wwprc = models.BooleanField(db_column='HIDE_WWPRC')
    web_descr1 = models.CharField(db_column='WEB_DESCR1', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS')
    web_descr2 = models.TextField(db_column='WEB_DESCR2', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    web_descr3 = models.TextField(db_column='WEB_DESCR3', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    comp_tpl = models.CharField(db_column='COMP_TPL', max_length=48, db_collation='SQL_Latin1_General_CP1_CI_AS')
    comp_descr = models.CharField(db_column='COMP_DESCR', max_length=48, db_collation='SQL_Latin1_General_CP1_CI_AS')
    template = models.CharField(db_column='TEMPLATE', max_length=48, db_collation='SQL_Latin1_General_CP1_CI_AS')
    descr1copy = models.BooleanField(db_column='DESCR1COPY')
    descr2copy = models.BooleanField(db_column='DESCR2COPY')
    descr3copy = models.BooleanField(db_column='DESCR3COPY')
    seasonal = models.CharField(db_column='SEASONAL', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    show_web = models.BooleanField(db_column='SHOW_WEB')
    acc_label = models.CharField(db_column='ACC_LABEL', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    showserial = models.BooleanField(db_column='SHOWSERIAL')
    perc_adj_n = models.DecimalField(db_column='PERC_ADJ_N', max_digits=2, decimal_places=0)  # Field name made lowercase.
    rol_fnprod = models.BooleanField(db_column='ROL_FNPROD')
    rol_rwmtrl = models.BooleanField(db_column='ROL_RWMTRL')
    rol_gauge = models.DecimalField(db_column='ROL_GAUGE', max_digits=2, decimal_places=0)
    rol_thick = models.DecimalField(db_column='ROL_THICK', max_digits=12, decimal_places=4)
    rol_color = models.CharField(db_column='ROL_COLOR', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')
    rol_dense = models.DecimalField(db_column='ROL_DENSE', max_digits=10, decimal_places=3)
    rol_width = models.DecimalField(db_column='ROL_WIDTH', max_digits=12, decimal_places=4)
    rol_fnexdt = models.DateField(db_column='ROL_FNEXDT', blank=True, null=True)
    rol_rwexdt = models.DateField(db_column='ROL_RWEXDT', blank=True, null=True)
    lotselopt = models.CharField(db_column='LOTSELOPT', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS')
    show_lots = models.BooleanField(db_column='SHOW_LOTS')
    inactive = models.BooleanField(db_column='INACTIVE')
    notqtysell = models.BooleanField(db_column='NOTQTYSELL')
    no_search = models.BooleanField(db_column='NO_SEARCH')
    rol_profil = models.CharField(db_column='ROL_PROFIL', max_length=24, db_collation='SQL_Latin1_General_CP1_CI_AS')
    value = models.DecimalField(db_column='VALUE', max_digits=14, decimal_places=2)
    comp_flatv = models.BooleanField(db_column='COMP_FLATV')
    jobstg_id = models.CharField(db_column='JOBSTG_ID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS')
    cto_prompt = models.DecimalField(db_column='CTO_PROMPT', max_digits=1, decimal_places=0)
    tree_path = models.CharField(db_column='TREE_PATH', max_length=60, db_collation='SQL_Latin1_General_CP1_CI_AS')
    int_note = models.TextField(db_column='INT_NOTE', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    upc2 = models.CharField(db_column='UPC2', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    upc3 = models.CharField(db_column='UPC3', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS')
    def_to_ser = models.BooleanField(db_column='DEF_TO_SER')
    def_to_pri = models.BooleanField(db_column='DEF_TO_PRI')
    usetaxelig = models.BooleanField(db_column='USETAXELIG')
    usetax_acc = models.CharField(db_column='USETAX_ACC', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS')
    externalid = models.CharField(db_column='EXTERNALID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS')
    jc_offset = models.BooleanField(db_column='JC_OFFSET')
    isshortcut = models.BooleanField(db_column='ISSHORTCUT')
    av_in_off = models.DecimalField(db_column='AV_IN_OFF', max_digits=22, decimal_places=6)
    av_out_off = models.DecimalField(db_column='AV_OUT_OFF', max_digits=22, decimal_places=6)
    oh_in_off = models.DecimalField(db_column='OH_IN_OFF', max_digits=22, decimal_places=6)
    oh_out_off = models.DecimalField(db_column='OH_OUT_OFF', max_digits=22, decimal_places=6)
    no_in_off = models.DecimalField(db_column='NO_IN_OFF', max_digits=22, decimal_places=6)
    no_out_off = models.DecimalField(db_column='NO_OUT_OFF', max_digits=22, decimal_places=6)
    prod_type = models.CharField(db_column='PROD_TYPE', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'INVENTRY'
