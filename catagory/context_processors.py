from .models import Catagory


def product_links(request):
    links = Catagory.objects.all()
    return dict(links=links)
