from django import template

register = template.Library()

@register.filter
def get_sub(d, id):
    return d[id]
