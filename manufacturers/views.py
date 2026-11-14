
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Manufacturer
from .forms import ManufacturerForm


class ItemList(ListView):
    model = Manufacturer
    template_name = 'manufacturers/item_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        qs = Manufacturer.objects.all()

        search = self.request.GET.get('q', '').strip()

        if search:
            qs = qs.filter(
                Q(name__icontains=search)
            )

        sort = self.request.GET.get('sort', '')
        allowed = ['name', '-name']

        if sort in allowed:
            qs = qs.order_by(sort)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Manufacturers',
            section='manufacturers',
        )

        return ctx


class ItemDetail(DetailView):
    model = Manufacturer
    template_name = 'manufacturers/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Manufacturers',
            section='manufacturers',
        )

        return ctx


class ItemCreate(CreateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturers/item_form.html'
    success_url = reverse_lazy('manufacturers:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Add Manufacturer',
            section='manufacturers',
        )

        return ctx


class ItemUpdate(UpdateView):
    model = Manufacturer
    form_class = ManufacturerForm
    template_name = 'manufacturers/item_form.html'
    success_url = reverse_lazy('manufacturers:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Edit Manufacturer',
            section='manufacturers',
        )

        return ctx


class ItemDelete(DeleteView):
    model = Manufacturer
    template_name = 'manufacturers/item_confirm_delete.html'
    success_url = reverse_lazy('manufacturers:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Delete Manufacturer',
            section='manufacturers',
        )

        return ctx
