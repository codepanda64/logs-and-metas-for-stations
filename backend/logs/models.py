from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .fields import OrderField


class ManageLog(models.Model):
    """
    台站管理日志
    """

    station = models.ForeignKey(
        "basicinfo.Station", on_delete=models.CASCADE, verbose_name="管理的台站"
    )
    station_state = models.BooleanField(default=True, verbose_name="查台时运行状态")
    is_restore = models.BooleanField(default=True, verbose_name="是否恢复正常")

    manage_time = models.DateTimeField(verbose_name="管理台站的时间")

    order = OrderField(for_fields=["station", "manage_time.year"], blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.order}. {self.manage_time}"


class Record(models.Model):
    manage_log = models.ForeignKey("ManageLog", on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            "model__in": (
                "ChangedLocation",
                "ChangedSeismicInstrument",
                "ChangedDisk",
                "ManualCollectedData",
            )
        },
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey("content_type", "object_id")

    order = OrderField(blank=True, for_fields=["manage_log"])

    class Meta:
        ordering = ["order"]


class BaseRecordItem(models.Model):
    station = models.ForeignKey(
        "basicinfo.Station",
        on_delete=models.CASCADE,
        related_name="%(class)s_related",
        verbose_name="所属台站",
    )
    changed = models.DateTimeField()
    is_last = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ChangedLocation(BaseRecordItem):
    """
    台站位置变更记录
    """

    latitude = models.FloatField(default=0.0, verbose_name="纬度")
    longitude = models.FloatField(default=0.0, verbose_name="经度")
    altitude = models.FloatField(default=0.0, verbose_name="高程")


class ChangedSeismicInstrument(BaseRecordItem):
    """
    台站测震仪器变更记录
    """

    seismic_instruments = models.ManyToManyField(
        "instruments.SeismicInstrumentEntity",
        related_name="by_used_histories",
        verbose_name="更换测震仪器记录",
    )


class ChangedOtherInstrument(BaseRecordItem):
    """
    其它设备变更记录
    """

    instruments = models.ManyToManyField(
        "instruments.InstrumentModel",
        limit_choices_to={"has_sn": False},
        related_name="by_used_histories",
        verbose_name="更换仪器记录",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="数量")


class ChangedDisk(BaseRecordItem):
    """
    台站数据存储卡变更记录
    """

    disk1_size = models.FloatField(default=0.0, verbose_name="卡1")
    disk2_size = models.FloatField(default=0.0, verbose_name="卡2")


class ManualCollectedData(BaseRecordItem):
    """
    台站数据回收记录
    """

    disk1_used = models.FloatField(default=0.0, verbose_name="卡1")
    disk2_used = models.FloatField(default=0.0, verbose_name="卡2")

