from django import template

register = template.Library()
@register.filter
def get_reward(reward, level):
    LEVLE_NAME = [f"{reward}-basic", f"{reward}-intermediate", f"{reward}-advanced"]
    if 10 >= level:
        return LEVLE_NAME[0]
    if 20 >= level:
        return LEVLE_NAME[1]
    return LEVLE_NAME[2]