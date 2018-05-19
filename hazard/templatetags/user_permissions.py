# Core Django imports
from django import template
from django.contrib.auth.models import Group

# Third-party app imports

# Realative imports of the 'app-name' package


register = template.Library()


@register.filter('has_group')
def has_group(user, group_name):
    print(group_name)
    db_groups = Group.objects.all()
    for group in db_groups:
        print(group)
    print(user)
    groups = user.groups.all().values_list('name', flat=True)
    print(groups)
    return True if group_name in groups else False