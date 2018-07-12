from django.views.generic import TemplateView
from main.models import Category


class HomePage(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        covers = [
            {
                'url': 'covers/cover1.jpg',
                'text': {
                    'title': "",
                    'description': ""
                }
            },
            {
                'url': 'covers/cover2.jpg',
                'text': {

                }
            },
            {
                'url': 'covers/cover3.jpg',
                'text': {

                }
            }
        ]

        categories = Category.objects.all()[:10]

        context['categories'] = categories
        context['covers'] = covers
        context['home'] = True

        return context
