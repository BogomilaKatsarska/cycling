from django.template import Library

from cycling.cyclist.models import Cyclist

register = Library()


@register.simple_tag(name='cyclist_info')
def show_cyclist_info(cyclist: Cyclist):
    return f'Hello, I am {cyclist.first_name} {cyclist.last_name}.'


@register.simple_tag(name='sample_tag')
def sample_tag(*args, **kwargs):
    return ', '.join(str(x) for x in list(args) + list(kwargs.items()))


# check takes_context=True
@register.inclusion_tag('tags/nav.html', name='app_nav')
def generate_nav(*args):
    context = {
        'url_names': args,
    }
    return context
