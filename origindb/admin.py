from django.contrib import admin

from origindb.models import Arinv, Arinvdet, Inprodtype, Inventry

# from linemetals.origindb.models import Arinv, Arinvdet, Inprodtype, Inventry

admin.site.register(Arinv)
admin.site.register(Arinvdet)
admin.site.register(Inprodtype)
admin.site.register(Inventry)
