from django import template

# ============================================================================ #
from project.apps.common.models import CommonInfo


register = template.Library()


@register.simple_tag(name="common_info")
def common_info():
    setting = CommonInfo.objects.filter(status="True").first()
    return setting
