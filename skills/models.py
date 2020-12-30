from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Skill(MPTTModel):
    name = models.TextField(_("name"), max_length=50, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("skill_detail", kwargs={"pk": self.pk})
