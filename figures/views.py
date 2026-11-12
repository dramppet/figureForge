
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Figure
from .forms import FigureForm, FigureDeleteForm


class ItemList(ListView):
    model = Figure
    template_name = 'figures/item_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        qs = (
            Figure.objects
            .select_related('manufacturers')
            .prefetch_related('materials')
        )

        search = self.request.GET.get(
            'q', ''
        ).strip()

        if search:
            qs = qs.filter(
                Q(title__icontains=search)
                | Q(character_name__icontains=search)
            )

        sort = self.request.GET.get(
            'sort', ''
        )

        allowed = [
            'title',
            '-title',
            'base_price',
            '-base_price',
            '-pk',
        ]

        if sort in allowed:
            qs = qs.order_by(sort)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Figures',
            section='figures',
        )

        return ctx


class ItemDetail(DetailView):
    model = Figure
    template_name = 'figures/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Figure Details',
            section='figures',
        )

        return ctx


class ItemCreate(CreateView):
    model = Figure
    form_class = FigureForm
    template_name = 'figures/item_form.html'
    success_url = reverse_lazy('figures:list')

    extra_context = {
        'page_title': 'Add Figure',
        'section': 'figures',
    }


class ItemUpdate(UpdateView):
    model = Figure
    form_class = FigureForm
    template_name = 'figures/item_form.html'
    success_url = reverse_lazy('figures:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_title'] = 'Edit Figure'
        context['section'] = 'figures'

        return context

    def form_invalid(self, form):
        print("EDIT FORM ERRORS:", form.errors.as_json())
        return super().form_invalid(form)




class ItemDelete(DeleteView):
    model = Figure
    template_name = 'figures/item_confirm_delete.html'
    success_url = reverse_lazy('figures:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page_title'] = 'Delete Figure'
        context['section'] = 'figures'

        context['figure_form'] = FigureDeleteForm(
            instance=self.object
        )

        return context

