# Generated by Django 4.2.1 on 2023-06-10 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arinv',
            fields=[
                ('arinv_guid', models.CharField(db_column='ARINV_GUID', max_length=36, primary_key=True, serialize=False)),
                ('recno5', models.IntegerField(db_column='RECNO5')),
                ('id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ID', max_length=10)),
                ('name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='NAME', max_length=86)),
                ('address1', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ADDRESS1', max_length=35)),
                ('address2', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ADDRESS2', max_length=35)),
                ('city', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CITY', max_length=30)),
                ('state', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='STATE', max_length=3)),
                ('zip', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ZIP', max_length=11)),
                ('invoice', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INVOICE', max_length=15)),
                ('descr', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DESCR', max_length=50)),
                ('inv_date', models.DateField(blank=True, db_column='INV_DATE', null=True)),
                ('due_date', models.DateField(blank=True, db_column='DUE_DATE', null=True)),
                ('dis_date', models.DateField(blank=True, db_column='DIS_DATE', null=True)),
                ('iddiscount', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='IDDISCOUNT', max_length=10)),
                ('idcharge', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='IDCHARGE', max_length=10)),
                ('discoun', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DISCOUN', max_length=60)),
                ('charge', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CHARGE', max_length=60)),
                ('terms', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TERMS', max_length=1)),
                ('in_level', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='IN_LEVEL', max_length=15)),
                ('po_no', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PO_NO', max_length=20)),
                ('salesman', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SALESMAN', max_length=20)),
                ('ship_via', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SHIP_VIA', max_length=25)),
                ('e_date', models.DateField(blank=True, db_column='E_DATE', null=True)),
                ('discount', models.DecimalField(db_column='DISCOUNT', decimal_places=2, max_digits=14)),
                ('overdue', models.DecimalField(db_column='OVERDUE', decimal_places=2, max_digits=14)),
                ('freight', models.DecimalField(db_column='FREIGHT', decimal_places=2, max_digits=14)),
                ('tax', models.DecimalField(db_column='TAX', decimal_places=2, max_digits=14)),
                ('subtotal', models.DecimalField(db_column='SUBTOTAL', decimal_places=2, max_digits=14)),
                ('total', models.DecimalField(db_column='TOTAL', decimal_places=2, max_digits=14)),
                ('status', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='STATUS', max_length=1)),
                ('total_paid', models.DecimalField(db_column='TOTAL_PAID', decimal_places=2, max_digits=14)),
                ('total_w', models.DecimalField(db_column='TOTAL_W', decimal_places=2, max_digits=14)),
                ('balance', models.DecimalField(db_column='BALANCE', decimal_places=2, max_digits=14)),
                ('check_no', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CHECK_NO', max_length=15)),
                ('check_date', models.DateField(blank=True, db_column='CHECK_DATE', null=True)),
                ('c_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_ID', max_length=10)),
                ('c_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_NAME', max_length=86)),
                ('c_address1', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_ADDRESS1', max_length=35)),
                ('c_address2', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_ADDRESS2', max_length=35)),
                ('c_city', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_CITY', max_length=30)),
                ('c_state', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_STATE', max_length=3)),
                ('c_zip', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_ZIP', max_length=11)),
                ('email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='EMAIL', max_length=50)),
                ('billing_co', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='BILLING_CO', max_length=40)),
                ('ship_date', models.DateField(blank=True, db_column='SHIP_DATE', null=True)),
                ('frght_amt', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FRGHT_AMT', max_length=90)),
                ('frght_type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FRGHT_TYPE', max_length=10)),
                ('user_name', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='USER_NAME', max_length=20)),
                ('was_proc', models.BooleanField(db_column='WAS_PROC')),
                ('memo', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MEMO', null=True)),
                ('signature', models.BinaryField(blank=True, db_column='SIGNATURE', max_length='max', null=True)),
                ('country', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='COUNTRY', max_length=25)),
                ('c_country', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_COUNTRY', max_length=25)),
                ('close_date', models.DateField(blank=True, db_column='CLOSE_DATE', null=True)),
                ('so_tax', models.DecimalField(db_column='SO_TAX', decimal_places=2, max_digits=14)),
                ('man_tax', models.BooleanField(db_column='MAN_TAX')),
                ('orig_inv', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ORIG_INV', max_length=15)),
                ('orig_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ORIG_AID', max_length=16)),
                ('print_time', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PRINT_TIME', max_length=14)),
                ('c_fr_order', models.BooleanField(db_column='C_FR_ORDER')),
                ('crea_date', models.DateField(blank=True, db_column='CREA_DATE', null=True)),
                ('crea_time', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CREA_TIME', max_length=8)),
                ('proc_date', models.DateField(blank=True, db_column='PROC_DATE', null=True)),
                ('proc_time', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PROC_TIME', max_length=8)),
                ('ar_trade', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AR_TRADE', max_length=9)),
                ('freight_gl', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FREIGHT_GL', max_length=9)),
                ('finance', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FINANCE', max_length=9)),
                ('cust_disc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CUST_DISC', max_length=9)),
                ('down_pay', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DOWN_PAY', max_length=9)),
                ('def_dept', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DEF_DEPT', max_length=3)),
                ('warehouse', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WAREHOUSE', max_length=10)),
                ('autoid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AUTOID', max_length=16)),
                ('csend_date', models.DateField(blank=True, db_column='CSEND_DATE', null=True)),
                ('csend_time', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CSEND_TIME', max_length=4)),
                ('csend_mes', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CSEND_MES', null=True)),
                ('c_rate', models.DecimalField(db_column='C_RATE', decimal_places=5, max_digits=15)),
                ('curr_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CURR_ID', max_length=5)),
                ('copied', models.BooleanField(db_column='COPIED')),
                ('prevord', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PREVORD', max_length=15)),
                ('trim', models.BooleanField(db_column='TRIM')),
                ('metal', models.BooleanField(db_column='METAL')),
                ('div_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DIV_AID', max_length=16)),
                ('authorized', models.DecimalField(db_column='AUTHORIZED', decimal_places=2, max_digits=14)),
                ('web_sale', models.BooleanField(db_column='WEB_SALE')),
                ('phone', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PHONE', max_length=25)),
                ('web_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WEB_AID', max_length=16)),
                ('cf_email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CF_EMAIL', max_length=50)),
                ('cf_sent', models.BooleanField(db_column='CF_SENT')),
                ('rollexdt', models.DateField(blank=True, db_column='ROLLEXDT', null=True)),
                ('rollprocdt', models.DateField(blank=True, db_column='ROLLPROCDT', null=True)),
                ('c_email', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_EMAIL', max_length=50)),
                ('c_phone', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_PHONE', max_length=25)),
                ('last_print', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='LAST_PRINT', max_length=100)),
                ('handling', models.DecimalField(db_column='HANDLING', decimal_places=2, max_digits=14)),
                ('freightexp', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='FREIGHTEXP', null=True)),
                ('ly_pts_got', models.DecimalField(db_column='LY_PTS_GOT', decimal_places=2, max_digits=14)),
                ('to_b_sent', models.BooleanField(db_column='TO_B_SENT')),
                ('internalnt', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INTERNALNT', null=True)),
                ('out_city', models.BooleanField(db_column='OUT_CITY')),
                ('c_tax', models.DecimalField(db_column='C_TAX', decimal_places=2, max_digits=14)),
                ('c_manual', models.BooleanField(db_column='C_MANUAL')),
                ('arpw_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ARPW_ID', max_length=20)),
                ('comis_paid', models.BooleanField(db_column='COMIS_PAID')),
                ('job_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='JOB_ID', max_length=10)),
                ('num_bill', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='NUM_BILL', max_length=5)),
                ('use_jobret', models.BooleanField(db_column='USE_JOBRET')),
                ('from_tandm', models.BooleanField(db_column='FROM_TANDM')),
                ('subilnoret', models.DecimalField(db_column='SUBILNORET', decimal_places=2, max_digits=14)),
                ('arqtaidsrc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ARQTAIDSRC', max_length=16)),
                ('usetaxed', models.BooleanField(db_column='USETAXED')),
                ('cntct_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CNTCT_AID', max_length=16)),
                ('ccntct_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='CCNTCT_AID', max_length=16)),
                ('man_usetax', models.BooleanField(db_column='MAN_USETAX')),
                ('externalid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='EXTERNALID', max_length=50)),
                ('p_rounddif', models.DecimalField(db_column='P_ROUNDDIF', decimal_places=2, max_digits=14)),
            ],
            options={
                'db_table': 'ARINV',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Arinvdet',
            fields=[
                ('arinvdet_guid', models.CharField(db_column='ARINVDET_GUID', max_length=36, primary_key=True, serialize=False)),
                ('recno5', models.IntegerField(db_column='RECNO5')),
                ('invoice', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INVOICE', max_length=15)),
                ('id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ID', max_length=10)),
                ('doc_type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DOC_TYPE', max_length=1)),
                ('doc_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DOC_AID', max_length=16)),
                ('inv_date', models.DateField(blank=True, db_column='INV_DATE', null=True)),
                ('quan', models.DecimalField(db_column='QUAN', decimal_places=6, max_digits=22)),
                ('ship', models.DecimalField(db_column='SHIP', decimal_places=6, max_digits=22)),
                ('m_quan', models.DecimalField(db_column='M_QUAN', decimal_places=6, max_digits=22)),
                ('orig_quan', models.DecimalField(db_column='ORIG_QUAN', decimal_places=6, max_digits=22)),
                ('inven', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INVEN', max_length=24)),
                ('c_type', models.DecimalField(db_column='C_TYPE', decimal_places=0, max_digits=2)),
                ('unit_meas', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='UNIT_MEAS', max_length=10)),
                ('descr', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DESCR', null=True)),
                ('unit', models.DecimalField(db_column='UNIT', decimal_places=6, max_digits=22)),
                ('price', models.DecimalField(db_column='PRICE', decimal_places=2, max_digits=14)),
                ('so_amount', models.DecimalField(db_column='SO_AMOUNT', decimal_places=2, max_digits=14)),
                ('discount', models.DecimalField(db_column='DISCOUNT', decimal_places=2, max_digits=14)),
                ('sodiscount', models.DecimalField(db_column='SODISCOUNT', decimal_places=2, max_digits=14)),
                ('timestamp', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TIMESTAMP', max_length=10)),
                ('par_time', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PAR_TIME', max_length=10)),
                ('gpar_time', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='GPAR_TIME', max_length=10)),
                ('status', models.DecimalField(db_column='STATUS', decimal_places=0, max_digits=1)),
                ('u_cost', models.DecimalField(db_column='U_COST', decimal_places=4, max_digits=18)),
                ('costs', models.DecimalField(db_column='COSTS', decimal_places=2, max_digits=14)),
                ('tax_group', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TAX_GROUP', max_length=20)),
                ('exm_overid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='EXM_OVERID', max_length=1)),
                ('ship_date', models.DateField(blank=True, db_column='SHIP_DATE', null=True)),
                ('weight', models.DecimalField(db_column='WEIGHT', decimal_places=2, max_digits=14)),
                ('print', models.BooleanField(db_column='PRINT')),
                ('ap_partime', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AP_PARTIME', max_length=10)),
                ('print_quan', models.BooleanField(db_column='PRINT_QUAN')),
                ('print_uom', models.BooleanField(db_column='PRINT_UOM')),
                ('account', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ACCOUNT', max_length=9)),
                ('warehouse', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WAREHOUSE', max_length=10)),
                ('autoid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AUTOID', max_length=16)),
                ('pcm_type', models.DecimalField(db_column='PCM_TYPE', decimal_places=0, max_digits=1)),
                ('pcm_perc', models.DecimalField(db_column='PCM_PERC', decimal_places=2, max_digits=8)),
                ('mto', models.BooleanField(db_column='MTO')),
                ('mto_d_sync', models.BooleanField(db_column='MTO_D_SYNC')),
                ('drop_ven', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DROP_VEN', max_length=10)),
                ('drop_part', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DROP_PART', max_length=24)),
                ('drop_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DROP_AID', max_length=16)),
                ('purc_meth', models.DecimalField(db_column='PURC_METH', decimal_places=0, max_digits=1)),
                ('c_price', models.DecimalField(db_column='C_PRICE', decimal_places=6, max_digits=22)),
                ('c_unit', models.DecimalField(db_column='C_UNIT', decimal_places=6, max_digits=22)),
                ('fxline', models.BooleanField(db_column='FXLINE')),
                ('c_formula', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='C_FORMULA', null=True)),
                ('width', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WIDTH', max_length=12)),
                ('widthd', models.DecimalField(db_column='WIDTHD', decimal_places=6, max_digits=22)),
                ('height', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='HEIGHT', max_length=12)),
                ('heightd', models.DecimalField(db_column='HEIGHTD', decimal_places=6, max_digits=22)),
                ('dem', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DEM', max_length=12)),
                ('demd', models.DecimalField(db_column='DEMD', decimal_places=6, max_digits=22)),
                ('manual_p', models.BooleanField(db_column='MANUAL_P')),
                ('manual_c', models.BooleanField(db_column='MANUAL_C')),
                ('round', models.DecimalField(db_column='ROUND', decimal_places=5, max_digits=13)),
                ('comment', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='COMMENT', max_length=50)),
                ('ea_quan', models.DecimalField(db_column='EA_QUAN', decimal_places=6, max_digits=21)),
                ('r_ea_quan', models.DecimalField(db_column='R_EA_QUAN', decimal_places=6, max_digits=21)),
                ('report_n', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='REPORT_N', max_length=20)),
                ('random_w', models.BooleanField(db_column='RANDOM_W')),
                ('random_h', models.BooleanField(db_column='RANDOM_H')),
                ('item_num', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ITEM_NUM', max_length=20)),
                ('feet', models.DecimalField(db_column='FEET', decimal_places=0, max_digits=9)),
                ('inchesd', models.DecimalField(db_column='INCHESD', decimal_places=6, max_digits=18)),
                ('inches', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INCHES', max_length=12)),
                ('c_mfg', models.DecimalField(db_column='C_MFG', decimal_places=2, max_digits=14)),
                ('r_serial', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='R_SERIAL', max_length=24)),
                ('su_autoid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SU_AUTOID', max_length=16)),
                ('trade_in', models.BooleanField(db_column='TRADE_IN')),
                ('in_level', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='IN_LEVEL', max_length=15)),
                ('job_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='JOB_ID', max_length=10)),
                ('jobstg_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='JOBSTG_ID', max_length=15)),
                ('aia', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AIA', max_length=10)),
                ('retn_type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='RETN_TYPE', max_length=1)),
                ('retn_perc', models.DecimalField(db_column='RETN_PERC', decimal_places=2, max_digits=8)),
                ('int_note', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INT_NOTE', null=True)),
                ('tax_expl', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TAX_EXPL', null=True)),
                ('on_site', models.DecimalField(db_column='ON_SITE', decimal_places=2, max_digits=12)),
            ],
            options={
                'db_table': 'ARINVDET',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inprodtype',
            fields=[
                ('inprodtype_guid', models.CharField(db_column='INPRODTYPE_GUID', max_length=36, primary_key=True, serialize=False)),
                ('recno5', models.IntegerField(db_column='RECNO5', unique=True)),
                ('prod_type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PROD_TYPE', max_length=20)),
                ('ar_aid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AR_AID', max_length=16)),
                ('autoid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AUTOID', max_length=16)),
            ],
            options={
                'verbose_name': 'inprodtype',
                'db_table': 'INPRODTYPE',
                'managed': False,
                "app_label": "origindb"
            },
        ),
        migrations.CreateModel(
            name='Inventry',
            fields=[
                ('inventry_guid', models.CharField(db_column='INVENTRY_GUID', max_length=36, primary_key=True, serialize=False)),
                ('recno5', models.IntegerField(db_column='RECNO5')),
                ('id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ID', max_length=24)),
                ('tree_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TREE_ID', max_length=5)),
                ('upc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='UPC', max_length=25)),
                ('type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TYPE', max_length=20)),
                ('c_type', models.DecimalField(db_column='C_TYPE', decimal_places=0, max_digits=2)),
                ('descr_1', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DESCR_1', max_length=80)),
                ('descr_1prn', models.BooleanField(db_column='DESCR_1PRN')),
                ('descr_1prp', models.BooleanField(db_column='DESCR_1PRP')),
                ('descr_2', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DESCR_2', max_length=80)),
                ('descr_2prn', models.BooleanField(db_column='DESCR_2PRN')),
                ('descr_2prp', models.BooleanField(db_column='DESCR_2PRP')),
                ('descr_3', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DESCR_3', null=True)),
                ('descr_3prn', models.BooleanField(db_column='DESCR_3PRN')),
                ('descr_3prp', models.BooleanField(db_column='DESCR_3PRP')),
                ('markup', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MARKUP', max_length=60)),
                ('markup_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MARKUP_ID', max_length=10)),
                ('base', models.DecimalField(db_column='BASE', decimal_places=2, max_digits=14)),
                ('cost', models.DecimalField(db_column='COST', decimal_places=4, max_digits=18)),
                ('tax_group', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TAX_GROUP', max_length=20)),
                ('weight', models.DecimalField(db_column='WEIGHT', decimal_places=2, max_digits=14)),
                ('date', models.DateField(blank=True, db_column='DATE', null=True)),
                ('quan2order', models.DecimalField(db_column='QUAN2ORDER', decimal_places=2, max_digits=14)),
                ('count', models.DecimalField(db_column='COUNT', decimal_places=6, max_digits=22)),
                ('location', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='LOCATION', max_length=200)),
                ('min_inven', models.DecimalField(db_column='MIN_INVEN', decimal_places=2, max_digits=14)),
                ('max_inven', models.DecimalField(db_column='MAX_INVEN', decimal_places=2, max_digits=14)),
                ('order_amt', models.DecimalField(db_column='ORDER_AMT', decimal_places=2, max_digits=14)),
                ('pri_vendor', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PRI_VENDOR', max_length=10)),
                ('pur_o', models.DecimalField(db_column='PUR_O', decimal_places=6, max_digits=22)),
                ('pur_s', models.DecimalField(db_column='PUR_S', decimal_places=6, max_digits=22)),
                ('sales_o', models.DecimalField(db_column='SALES_O', decimal_places=6, max_digits=22)),
                ('sales_s', models.DecimalField(db_column='SALES_S', decimal_places=6, max_digits=22)),
                ('m_in_o', models.DecimalField(db_column='M_IN_O', decimal_places=6, max_digits=22)),
                ('m_in_s', models.DecimalField(db_column='M_IN_S', decimal_places=6, max_digits=22)),
                ('m_out_o', models.DecimalField(db_column='M_OUT_O', decimal_places=6, max_digits=22)),
                ('m_out_s', models.DecimalField(db_column='M_OUT_S', decimal_places=6, max_digits=22)),
                ('job_out_o', models.DecimalField(db_column='JOB_OUT_O', decimal_places=6, max_digits=22)),
                ('job_out_s', models.DecimalField(db_column='JOB_OUT_S', decimal_places=6, max_digits=22)),
                ('each_unit', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='EACH_UNIT', max_length=10)),
                ('int_quan', models.BooleanField(db_column='INT_QUAN')),
                ('def_unit', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DEF_UNIT', max_length=10)),
                ('last_chk_u', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='LAST_CHK_U', max_length=20)),
                ('last_chk_d', models.DateField(blank=True, db_column='LAST_CHK_D', null=True)),
                ('last_chk_t', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='LAST_CHK_T', max_length=8)),
                ('auto_cost', models.BooleanField(db_column='AUTO_COST')),
                ('memo', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MEMO', null=True)),
                ('mfg', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MFG', max_length=10)),
                ('mfg_part', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MFG_PART', max_length=24)),
                ('web', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WEB', null=True)),
                ('est_hours', models.DecimalField(db_column='EST_HOURS', decimal_places=2, max_digits=14)),
                ('def_work', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DEF_WORK', max_length=10)),
                ('perc_adj', models.DecimalField(db_column='PERC_ADJ', decimal_places=2, max_digits=9)),
                ('perc_adj_c', models.DecimalField(db_column='PERC_ADJ_C', decimal_places=0, max_digits=1)),
                ('pur_memo', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PUR_MEMO', null=True)),
                ('sale_class', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SALE_CLASS', max_length=15)),
                ('updatecost', models.BooleanField(db_column='UPDATECOST')),
                ('updvencost', models.BooleanField(db_column='UPDVENCOST')),
                ('ins_acc', models.DecimalField(db_column='INS_ACC', decimal_places=0, max_digits=1)),
                ('returndays', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='RETURNDAYS', max_length=16)),
                ('sale_acc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SALE_ACC', max_length=9)),
                ('use_pl_gl', models.BooleanField(db_column='USE_PL_GL')),
                ('pur_acc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PUR_ACC', max_length=9)),
                ('adjust', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ADJUST', max_length=5)),
                ('asset', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ASSET', max_length=9)),
                ('use_itemgl', models.BooleanField(db_column='USE_ITEMGL')),
                ('mfg_cost', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='MFG_COST', max_length=9)),
                ('autoid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='AUTOID', max_length=16)),
                ('fixed_cost', models.BooleanField(db_column='FIXED_COST')),
                ('adj_inven', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ADJ_INVEN', max_length=24)),
                ('autoserial', models.BooleanField(db_column='AUTOSERIAL')),
                ('weigh_it', models.BooleanField(db_column='WEIGH_IT')),
                ('def_type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='DEF_TYPE', max_length=35)),
                ('ent_task', models.BooleanField(db_column='ENT_TASK')),
                ('purc_meth', models.DecimalField(db_column='PURC_METH', decimal_places=0, max_digits=1)),
                ('pur_ssed', models.BooleanField(db_column='PUR_SSED')),
                ('s_cust_i', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='S_CUST_I', max_length=24)),
                ('d_width', models.DecimalField(db_column='D_WIDTH', decimal_places=4, max_digits=16)),
                ('d_height', models.DecimalField(db_column='D_HEIGHT', decimal_places=4, max_digits=16)),
                ('d_dem', models.DecimalField(db_column='D_DEM', decimal_places=4, max_digits=16)),
                ('width', models.DecimalField(db_column='WIDTH', decimal_places=4, max_digits=16)),
                ('width_r', models.BooleanField(db_column='WIDTH_R')),
                ('height', models.DecimalField(db_column='HEIGHT', decimal_places=4, max_digits=16)),
                ('height_r', models.BooleanField(db_column='HEIGHT_R')),
                ('dem', models.DecimalField(db_column='DEM', decimal_places=4, max_digits=16)),
                ('dem_r', models.BooleanField(db_column='DEM_R')),
                ('waste_p', models.DecimalField(db_column='WASTE_P', decimal_places=4, max_digits=12)),
                ('item_num', models.BooleanField(db_column='ITEM_NUM')),
                ('d_replace', models.BooleanField(db_column='D_REPLACE')),
                ('trade_in', models.BooleanField(db_column='TRADE_IN')),
                ('trade_acc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TRADE_ACC', max_length=9)),
                ('su_autoid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SU_AUTOID', max_length=16)),
                ('show_stock', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SHOW_STOCK', max_length=25)),
                ('ostk_msg', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='OSTK_MSG', max_length=250)),
                ('hide_wwprc', models.BooleanField(db_column='HIDE_WWPRC')),
                ('web_descr1', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WEB_DESCR1', max_length=80)),
                ('web_descr2', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WEB_DESCR2', null=True)),
                ('web_descr3', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='WEB_DESCR3', null=True)),
                ('comp_tpl', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='COMP_TPL', max_length=48)),
                ('comp_descr', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='COMP_DESCR', max_length=48)),
                ('template', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TEMPLATE', max_length=48)),
                ('descr1copy', models.BooleanField(db_column='DESCR1COPY')),
                ('descr2copy', models.BooleanField(db_column='DESCR2COPY')),
                ('descr3copy', models.BooleanField(db_column='DESCR3COPY')),
                ('seasonal', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='SEASONAL', max_length=20)),
                ('show_web', models.BooleanField(db_column='SHOW_WEB')),
                ('acc_label', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ACC_LABEL', max_length=200)),
                ('showserial', models.BooleanField(db_column='SHOWSERIAL')),
                ('perc_adj_n', models.DecimalField(db_column='PERC_ADJ_N', decimal_places=0, max_digits=2)),
                ('rol_fnprod', models.BooleanField(db_column='ROL_FNPROD')),
                ('rol_rwmtrl', models.BooleanField(db_column='ROL_RWMTRL')),
                ('rol_gauge', models.DecimalField(db_column='ROL_GAUGE', decimal_places=0, max_digits=2)),
                ('rol_thick', models.DecimalField(db_column='ROL_THICK', decimal_places=4, max_digits=12)),
                ('rol_color', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ROL_COLOR', max_length=20)),
                ('rol_dense', models.DecimalField(db_column='ROL_DENSE', decimal_places=3, max_digits=10)),
                ('rol_width', models.DecimalField(db_column='ROL_WIDTH', decimal_places=4, max_digits=12)),
                ('rol_fnexdt', models.DateField(blank=True, db_column='ROL_FNEXDT', null=True)),
                ('rol_rwexdt', models.DateField(blank=True, db_column='ROL_RWEXDT', null=True)),
                ('lotselopt', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='LOTSELOPT', max_length=10)),
                ('show_lots', models.BooleanField(db_column='SHOW_LOTS')),
                ('inactive', models.BooleanField(db_column='INACTIVE')),
                ('notqtysell', models.BooleanField(db_column='NOTQTYSELL')),
                ('no_search', models.BooleanField(db_column='NO_SEARCH')),
                ('rol_profil', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='ROL_PROFIL', max_length=24)),
                ('value', models.DecimalField(db_column='VALUE', decimal_places=2, max_digits=14)),
                ('comp_flatv', models.BooleanField(db_column='COMP_FLATV')),
                ('jobstg_id', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='JOBSTG_ID', max_length=15)),
                ('cto_prompt', models.DecimalField(db_column='CTO_PROMPT', decimal_places=0, max_digits=1)),
                ('tree_path', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='TREE_PATH', max_length=60)),
                ('int_note', models.TextField(blank=True, db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='INT_NOTE', null=True)),
                ('upc2', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='UPC2', max_length=25)),
                ('upc3', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='UPC3', max_length=25)),
                ('def_to_ser', models.BooleanField(db_column='DEF_TO_SER')),
                ('def_to_pri', models.BooleanField(db_column='DEF_TO_PRI')),
                ('usetaxelig', models.BooleanField(db_column='USETAXELIG')),
                ('usetax_acc', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='USETAX_ACC', max_length=5)),
                ('externalid', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='EXTERNALID', max_length=50)),
                ('jc_offset', models.BooleanField(db_column='JC_OFFSET')),
                ('isshortcut', models.BooleanField(db_column='ISSHORTCUT')),
                ('av_in_off', models.DecimalField(db_column='AV_IN_OFF', decimal_places=6, max_digits=22)),
                ('av_out_off', models.DecimalField(db_column='AV_OUT_OFF', decimal_places=6, max_digits=22)),
                ('oh_in_off', models.DecimalField(db_column='OH_IN_OFF', decimal_places=6, max_digits=22)),
                ('oh_out_off', models.DecimalField(db_column='OH_OUT_OFF', decimal_places=6, max_digits=22)),
                ('no_in_off', models.DecimalField(db_column='NO_IN_OFF', decimal_places=6, max_digits=22)),
                ('no_out_off', models.DecimalField(db_column='NO_OUT_OFF', decimal_places=6, max_digits=22)),
                ('prod_type', models.CharField(db_collation='SQL_Latin1_General_CP1_CI_AS', db_column='PROD_TYPE', max_length=20)),
            ],
            options={
                'db_table': 'INVENTRY',
                'managed': False,
            },
        ),
    ]
