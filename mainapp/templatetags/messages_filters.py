from django import template

register = template.Library()

@register.filter(name='get_day_or_night_from_score')
def get_day_or_night_from_score(value):
    if value > 0.5:
        return "DAY"
    else:
        return "NIGHT"

