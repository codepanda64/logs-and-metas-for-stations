from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .fields import OrderField


class ManageLog(models.Model):
    """
    台站维护管理日志
    """

    station = models.ForeignKey(
        "basicinfo.Station", on_delete=models.CASCADE, verbose_name="管理的台站"
    )
    before_state = models.BooleanField(default=True, verbose_name="查台时运行状态")
    after_state = models.BooleanField(default=True, verbose_name="是否恢复正常")
    managed_date = models.DateField(verbose_name="台站管理日期")

    arrived_at = models.TimeField(blank=True, null=True, verbose_name="到达台站时间")
    left_at = models.TimeField(blank=True, null=True, verbose_name="离开台站时间")

    description = models.TextField(blank=True, verbose_name="维护描述")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (
            "station",
            "managed_date",
        )
        ordering = (
            "station",
            "managed_date",
        )

    def __str__(self):
        return f"{self.station} {self.managed_date}"


class StatusCheck(models.Model):
    """
    查台时状态检查
    """

    GOOD = "good"
    DISCONTINUOUS = "discontinuous"
    MALFUNCTION = "malfunction"
    OTHER = "other"

    STATUS_TYPE_ITEM = (
        ("good", "工作正常/数据可用"),
        ("discontinuous", "工作不连续/数据不连续"),
        ("malfunction", "设备故障/数据不可用"),
        ("other", "其它情况"),
    )

    manage_log = models.ForeignKey(
        "ManageLog",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_related",
    )
    input_voltage = models.FloatField(default=0.0, verbose_name="输入电压")
    backup_voltage = models.FloatField(default=0.0, verbose_name="备份电压")
    gps_lock_satellite = models.PositiveIntegerField(default=0, verbose_name="GPS锁定星数")
    calibration_signal = models.BooleanField(default=True, verbose_name="标定信号是否正常")
    dist_status = models.BooleanField(default=True, verbose_name="存储卡状态")
    status = models.CharField(
        max_length=50, choices=STATUS_TYPE_ITEM, default=GOOD, verbose_name="台站总体状态"
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BeforeStatusCheck(StatusCheck):
    pass


class AfterStatusCheck(StatusCheck):
    pass


class Record(models.Model):
    """
    关联:ManageLog
    针对不同的维护方式:
        LocationRecord: 台站位置变更记录
        InstrumentEntityRecord: 台站专业仪器变更记录
        CommmonInstrumentRecord: 台站通用设备变更记录
        InsertDiskRecord: 台站存储卡变更记录
        CollectedDataRecord: 台站回收数据记录
    """

    manage_log = models.ForeignKey(
        "ManageLog", on_delete=models.CASCADE, related_name="records"
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={
            "model__in": (
                "LocationRecordItem",
                "InstrumentEntityRecordItem",
                "CommmonInstrumentRecordItem",
                "InsertDiskRecordItem",
                "CollectedDataRecordItem",
            )
        },
    )
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey("content_type", "object_id")

    order = OrderField(blank=True, for_fields=["manage_log"])

    class Meta:
        ordering = ["order"]


class BaseRecordItem(models.Model):
    """
    所有操作记录的基类
    """

    station = models.ForeignKey(
        "basicinfo.Station",
        on_delete=models.CASCADE,
        related_name="%(class)s_related",
        verbose_name="所属台站",
    )
    changed_at = models.DateTimeField()
    is_last = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LocationRecordItem(BaseRecordItem):
    """
    台站位置变更记录记录
    """

    latitude = models.FloatField(default=0.0, verbose_name="纬度")
    longitude = models.FloatField(default=0.0, verbose_name="经度")
    altitude = models.FloatField(default=0.0, verbose_name="高程")
    geo_desciription = models.TextField(blank=True, verbose_name="位置描述")
    lithology_description = models.TextField(blank=True, verbose_name="岩性描述")
    other_info = models.TextField(blank=True, verbose_name="其他信息")


class InstrumentEntityRecordItem(BaseRecordItem):
    """
    专业有序列号的设备变更记录
    """

    instrument_entity = models.ForeignKey(
        "instruments.InstrumentEntity",
        on_delete=models.CASCADE,
        related_name="by_used_histories",
        verbose_name="更换测震仪器记录",
    )


class CommmonInstrumentRecordItem(BaseRecordItem):
    """
    通用设备变更记录
    """

    instrument = models.ForeignKey(
        "instruments.Instrument",
        on_delete=models.CASCADE,
        limit_choices_to={"is_model": False},
        related_name="by_used_histories",
        verbose_name="更换仪器记录",
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="数量")


class InsertDiskRecordItem(BaseRecordItem):
    """
    台站数据存储卡变更记录
    """

    disk1_size = models.FloatField(default=0.0, verbose_name="卡1")
    disk2_size = models.FloatField(default=0.0, verbose_name="卡2")


class CollectedDataRecordItem(BaseRecordItem):
    """
    台站数据回收记录
    """

    disk1_used = models.FloatField(default=0.0, verbose_name="卡1")
    disk2_used = models.FloatField(default=0.0, verbose_name="卡2")

