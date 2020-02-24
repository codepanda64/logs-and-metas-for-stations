from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from mptt.admin import MPTTModelAdmin
from mptt.admin import TreeRelatedFieldListFilter

from .models import (
    Department,
    Instrument,
    InstrumentCategory,
    InstrumentEntity,
)

admin.site.register(Department)
admin.site.register(InstrumentCategory, MPTTModelAdmin)


@admin.register(Instrument)
class InstrumentModelAdmin(admin.ModelAdmin):
    """Admin View for Station"""

    list_display = ("name", "param", "brand", "manufacturer", "category", "total")
    list_display_links = ("name",)
    list_filter = (("category", TreeRelatedFieldListFilter),)
    search_fields = (
        "name",
        "param",
        "brand",
        "manufacturer",
    )
    ordering = (
        "name",
        "manufacturer",
        "category",
    )


class InstrumentEntityCategoryFilter(admin.SimpleListFilter):
    title = "按仪器分类"

    parameter_name = "category"

    def lookups(self, request, model_admin):
        return (
            (2, "地震数据采集器"),
            (3, "地震仪"),
        )

    def queryset(self, request, queryset):
        if self.value() == "2":
            return queryset.filter(instrument_model__category=2)

        if self.value() == "3":
            return queryset.filter(instrument_model__category=3)


@admin.register(InstrumentEntity)
class InstrumentEntityAdmin(admin.ModelAdmin):
    """Admin View for InstrumentEntity"""

    list_display = (
        "sn",
        "instrument_model",
        "status",
        "belong",
    )
    list_display_links = ("sn",)
    list_filter = (
        InstrumentEntityCategoryFilter,
        "instrument_model",
        "status",
        "belong",
    )
    ordering = (
        "sn",
        "instrument_model",
    )
    list_editable = ("status",)
    search_fields = ("sn",)
