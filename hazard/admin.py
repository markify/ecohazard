from django.contrib import admin
from .models import HazardReport, HazardReportComment


# This populate Eco Hazard's Admin Page (/admin) when logged in with Hazard Report and Hazard comment
# Able to delete Hazard reports and comment in the admin section (admin role to delete inappropriate post functionality)

admin.site.register(HazardReport)
admin.site.register(HazardReportComment)
