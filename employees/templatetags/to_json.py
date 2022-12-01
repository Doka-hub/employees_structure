from django import template
from django.core.serializers.json import DjangoJSONEncoder

import json


register = template.Library()


@register.filter(name='json_format')
def json_format(data):
    return json.dumps(data, cls=DjangoJSONEncoder)
