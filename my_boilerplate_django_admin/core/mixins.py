from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.db import models
from django.forms import Select, Textarea, TextInput
from django.utils import timezone
from django_currentuser.middleware import get_current_user
from reversion.admin import VersionAdmin


class MultiFieldSortableChangeList(ChangeList):
    def get_ordering(self, request, queryset):
        ORDER_VAR = admin.views.main.ORDER_VAR
        params = self.params
        ordering = list(
            self.model_admin.get_ordering(request) or self._get_default_ordering()
        )

        if ORDER_VAR in params:
            ordering = []
            order_params = params[ORDER_VAR].split(".")
            for p in order_params:
                try:
                    none, pfx, idx = p.rpartition("-")
                    field_name = self.list_display[int(idx)]
                    order_fields = self.get_ordering_field(field_name)

                    if type(order_fields) == str:
                        order_fields = [order_fields]

                    for order_field in order_fields:
                        if order_field:
                            ordering.append(pfx + order_field)
                except (IndexError, ValueError):
                    continue

        ordering.extend(queryset.query.order_by)

        pk_name = self.lookup_opts.pk.name
        if not (set(ordering) & set(["pk", "-pk", pk_name, "-" + pk_name])):
            ordering.append("-pk")

        return ordering


class BaseModel(models.Model):
    criado_em = models.DateTimeField(blank=True, null=True)
    criado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_criado_por",
        blank=True,
        null=True,
        default=get_current_user(),
    )
    modificado_em = models.DateTimeField(blank=True, null=True)
    modificado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="%(class)s_modificado_por",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.criado_por or not self.criado_em:
            self.criado_por = get_current_user()
            self.criado_em = timezone.now()
        else:
            self.modificado_por = get_current_user()
            self.modificado_em = timezone.now()
        super(BaseModel, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None
        )


class AuditoriaAdmin(VersionAdmin):
    readonly_fields = (
        "criado_em",
        "criado_por",
        "modificado_em",
        "modificado_por",
    )


class AuditoriaAdminInline(admin.TabularInline):
    readonly_fields = (
        "criado_em",
        "criado_por",
        "modificado_em",
        "modificado_por",
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 8, "cols": 40})},
        models.ForeignKey: {"widget": Select(attrs={"style": "max-width: 150px"})},
        models.CharField: {"widget": TextInput(attrs={"style": "max-width: 150px"})},
    }


class AuditoriaAdminStackedInlineInline(admin.StackedInline):
    readonly_fields = (
        "criado_em",
        "criado_por",
        "modificado_em",
        "modificado_por",
    )
