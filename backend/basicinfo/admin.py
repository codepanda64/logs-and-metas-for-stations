from django.contrib import admin

from .models import Network, Station
from instruments.models import InstrumentItem, SeismicInstrumentEntity
from .forms import StationForm

admin.site.site_header = "台站运维日志管理系统"
admin.site.site_title = "台站运维日志管理系统"
admin.site.index_title = "欢迎使用台站运维日志管理系统"


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Admin View for Network"""

    list_display = (
        "code",
        "name",
    )
    list_display_links = ("code",)
    ordering = ("code",)
    prepopulated_fields = {"slug": ("code",)}


class InstrumentItemInline(admin.TabularInline):
    model = InstrumentItem


# class SeismicInstrumentEntityInline(admin.TabularInline):
#     model = SeismicInstrumentEntity


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    """Admin View for Station"""

    form = StationForm
