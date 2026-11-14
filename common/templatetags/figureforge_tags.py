from django import template
register = template.Library()
@register.filter
def short_label(value):
    return str(value)[:80]
