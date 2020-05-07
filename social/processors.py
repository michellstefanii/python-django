from .models import Link

def ctx_social(request):
    ctx_lib = {}
    links = Link.objects.all()
    for link in links:
        ctx_lib[link.key] = link.url
    return ctx_lib