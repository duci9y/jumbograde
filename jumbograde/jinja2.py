from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage

def environment(**options):
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
    #     'url': reverse,
    #     'compile': compile_static,
    #     'serialize_item': serialize_item,
    #     'markdownify': markdownify,
    #     'visible_pages': visible_pages,
    })
    return env
