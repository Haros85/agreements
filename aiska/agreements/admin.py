from django.contrib import admin
from .models import Foiv, Department, Type, Agreements, Additional, Protocol


class FoivAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "short")
    search_fields = ("title",)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)


class AgreementsAdmin(admin.ModelAdmin):
    list_display = ("pk", "foiv_id", "title", "number", "reg_date", "inv_number", "subject", "display_dept", "note", "file")
    search_fields = ("title",)


class AdditionalAdmin(admin.ModelAdmin):
    list_display = ("pk", "agr_id", "title", "number", "reg_date", "inv_number", "subject", "display_dept", "note", "file")
    search_fields = ("title",)


class TypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "type_protocol")
    search_fields = ("type_protocol",)


class ProtocolAdmin(admin.ModelAdmin):
    list_display = ("pk", "agr_id", "title", "number", "reg_date", "inv_number", "type_id", "from_mvd", "for_mvd", "note", "file")
    search_fields = ("title",)


admin.site.register(Foiv, FoivAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Agreements, AgreementsAdmin)
admin.site.register(Additional, AdditionalAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Protocol, ProtocolAdmin)
