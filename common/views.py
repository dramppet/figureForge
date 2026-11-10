from django.views.generic import TemplateView
from django.shortcuts import render

from figures.models import Figure
from manufacturers.models import Manufacturer
from reviews.models import Review


class IndexView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['latest'] = (
            Figure.objects
            .select_related('manufacturers')
            .order_by('-pk')[:6]
        )

        context['figure_count'] = Figure.objects.count()
        context['manufacture_count'] = Manufacturer.objects.count()
        context['review_count'] = Review.objects.count()

        return context

def page_not_found(request, exception):
    return render(request,'404.html',status=404)

