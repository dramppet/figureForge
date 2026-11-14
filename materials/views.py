
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Material
from .forms import MaterialForm


class ItemList(ListView):
    model = Material
    template_name = 'materials/item_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        qs = Material.objects.all()

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
            page_title='Materials',
            section='materials',
        )

        return ctx


class ItemDetail(DetailView):
    model = Material
    template_name = 'materials/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Materials',
            section='materials',
        )

        return ctx


class ItemCreate(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/item_form.html'
    success_url = reverse_lazy('materials:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Add Material',
            section='materials',
        )

        return ctx


class ItemUpdate(UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/item_form.html'
    success_url = reverse_lazy('materials:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Edit Material',
            section='materials',
        )

        return ctx


class ItemDelete(DeleteView):
    model = Material
    template_name = 'materials/item_confirm_delete.html'
    success_url = reverse_lazy('materials:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Delete Material',
            section='materials',
        )

        return ctx
