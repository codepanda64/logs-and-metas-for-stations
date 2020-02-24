from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Department(models.Model):
    """
    仪器实体所属部门
    """

    name = models.CharField(max_length=50, unique=True, verbose_name="部门名称")
    address = models.CharField(max_length=200, blank=True, verbose_name="地址")
    remark = models.TextField(blank=True, verbose_name="备注")

    class Meta:
        verbose_name = "部门"
        verbose_name_plural = "部门"

    def __str__(self):
        return self.name


class InstrumentCategory(MPTTModel):
    """
    设备仪器分类
    """

    name = models.CharField(max_length=50, unique=True, verbose_name="分类名称")
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="上级分类",
    )

    class Meta:
        verbose_name = "设备分类"
        verbose_name_plural = verbose_name

    class MPTTMeta:
        level_attr = "mptt_level"
        order_insertion_by = ("name",)

    def __str__(self):
        return self.name


class Instrument(models.Model):
    """
    设备仪器型号信息 
    有单独的序列号记录的设备的型号模型信息
    """

    name = models.CharField(max_length=100, verbose_name="设备名称")
    brand = models.CharField(max_length=50, blank=True, verbose_name="品牌")
    manufacturer = models.CharField(max_length=50, blank=True, verbose_name="厂商")
    category = TreeForeignKey(
        InstrumentCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="instruments",
        verbose_name="所属分类",
    )
    # 是否是特殊设备的模版，有单独序列号设备的模版
    is_model = models.BooleanField(default=False)
    param = models.CharField(max_length=200, blank=True, verbose_name="参数描述")
    total = models.PositiveIntegerField(default=1, verbose_name="总数")

    class Meta:
        verbose_name = "设备模型信息"
        verbose_name_plural = "设备模型信息"
        ordering = ("name",)
        unique_together = (
            "name",
            "param",
        )

    class MPTTMeta:
        level_attr = "mptt_level"
        order_insertion_by = ("name",)

    def __str__(self):
        return self.name if self.param == "" else f"{self.name}({self.param})"


class InstrumentEntity(models.Model):
    """
    测震设备实体
    """

    STATUS_TYPE = (
        ("online", "在线"),
        ("fault", "故障"),
        ("in_warehouse", "库存"),
        ("quarantine", "待检"),
        ("returned", "已归还"),
        ("unknow", "未知"),
    )
    sn = models.CharField(max_length=50, verbose_name="设备序号", unique=True)
    instrument_model = models.ForeignKey(
        "Instrument",
        related_name="instrument_entities",
        on_delete=models.CASCADE,
        limit_choices_to={"is_model": True},
        verbose_name="设备型号",
    )
    status = models.CharField(
        max_length=50, choices=STATUS_TYPE, default="in_warehouse", verbose_name="状态"
    )
    belong = models.ForeignKey(
        "Department", null=True, on_delete=models.SET_NULL, verbose_name="所属单位"
    )
    by_used = models.ForeignKey(
        "basicinfo.Station",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="seismic_instruments",
        verbose_name="使用台站",
    )

    class Meta:
        verbose_name = "测震设备实体"
        verbose_name_plural = "测震设备实体"
        ordering = ("sn",)

    class MPTTMeta:
        level_attr = "mptt_level"
        order_insertion_by = ("sn",)

    def __str__(self):
        return f"{self.sn} [{self.instrument_model}]"


class InstrumentItem(models.Model):
    station = models.ForeignKey("basicinfo.Station", on_delete=models.CASCADE)
    instrument = models.ForeignKey(
        "Instrument",
        on_delete=models.CASCADE,
        verbose_name="仪器型号",
        limit_choices_to={"is_model": False},
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="数量")

    class Meta:
        verbose_name = "仪器信息"
        verbose_name_plural = "仪器信息"

