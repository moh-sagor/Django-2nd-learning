from django import template

register = template.Library()

# @register.filter
def my_filters(value , arg):
    return value + " "+ arg


register.filter('custom_filters', my_filters)

