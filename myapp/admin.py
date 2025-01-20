from django.contrib import admin
from . models import Login,District,Area,User,Meterreader,Assign_meter_reader,Notification,Usage,Userupload,Complaint,Payment,Public,Bank

# Register your models here.
admin.site.register(Login)
admin.site.register(District)
admin.site.register(Area)
admin.site.register(User)
admin.site.register(Meterreader)
admin.site.register(Assign_meter_reader)
admin.site.register(Notification)
admin.site.register(Usage)
admin.site.register(Userupload)
admin.site.register(Complaint)
admin.site.register(Payment)
admin.site.register(Public)
admin.site.register(Bank)