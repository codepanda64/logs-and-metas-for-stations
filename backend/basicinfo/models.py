from django.db import models


class Network(models.Model):
    """定义台网信息"""

    code = models.CharField(max_length=50, unique=True, verbose_name="台网代码")
    name = models.CharField(max_length=50, blank=True, verbose_name="台网名称")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    remark = models.TextField(blank=True, verbose_name="备注")

    class Meta:
        """Meta definition for Network."""

        ordering = ("code",)

        verbose_name = "测震台网信息"
        verbose_name_plural = "测震台网信息"

    def __str__(self):
        """Unicode representation of Network."""
        return self.code

    def get_stations_count(self):
        """统计台网拥有的台站数"""
        return self.stations.count()


class Station(models.Model):
    """Model definition for Station."""

    """定义台站信息"""
    STATUS_TYPE = (
        ("selection", "勘选"),
        ("online", "在线"),
        ("suspend", "暂停"),
        ("offline", "下线"),
    )
    network = models.ForeignKey(
        "Network", on_delete=models.CASCADE, related_name="stations", verbose_name="台网"
    )
    code = models.CharField(max_length=50, verbose_name="台站代码")
    name = models.CharField(max_length=50, blank=True, verbose_name="台站名称")
    latitude = models.FloatField(default=0.0, verbose_name="纬度")
    longitude = models.FloatField(default=0.0, verbose_name="经度")
    altitude = models.FloatField(default=0.0, verbose_name="高程")
    status = models.CharField(
        max_length=50, choices=STATUS_TYPE, default="online", verbose_name="状态"
    )
    selection = models.DateField(blank=True, null=True, verbose_name="勘选时间")
    establish = models.DateField(blank=True, null=True, verbose_name="建台时间")
    removal = models.DateField(blank=True, null=True, verbose_name="撤台时间")
    remark = models.TextField(blank=True, verbose_name="备注")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Station."""

        unique_together = (("network", "code"),)
        ordering = (
            "network",
            "code",
        )
        verbose_name = "测震台站信息"
        verbose_name_plural = "测震台站信息"

    def __str__(self):
        """Unicode representation of Station."""
        return f"{self.network.code}-{self.code}"

    def get_count(self):
        """统计台网拥有的台站数"""
        return Station.objects.count()


class StationMoreInfo(models.Model):
    """
    台站其他信息
    """

    station = models.OneToOneField(
        "Station", on_delete=models.CASCADE, related_name="more_info"
    )
    geo_desciription = models.TextField(blank=True, verbose_name="位置描述")
    lithology_description = models.TextField(blank=True, verbose_name="岩性描述")
    other_info = models.TextField(blank=True, verbose_name="其他信息")

