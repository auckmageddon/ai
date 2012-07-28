from tastypie.resources import ModelResource
from faqs.models import FAQ

class FAQResource(ModelResource):
    class Meta:
        queryset = FAQ.objects.all()
        resource_name = 'FAQ'
