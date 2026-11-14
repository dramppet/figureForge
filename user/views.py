
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Client
from .forms import ClientForm


class ItemList(ListView):
    model = Client
    template_name = 'user/item_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        qs = Client.objects.all()

        search = self.request.GET.get('q', '').strip()

        if search:
            qs = qs.filter(
                Q(name__icontains=search)
            )

        sort = self.request.GET.get('sort', '')
        allowed = ['pk', '-pk']

        if sort in allowed:
            qs = qs.order_by(sort)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Orders',
            section='user',
        )

        return ctx


class ItemDetail(DetailView):
    model = Client
    template_name = 'user/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Orders',
            section='user',
        )

        return ctx


class ItemCreate(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'user/item_form.html'
    success_url = reverse_lazy('user:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Add Order',
            section='user',
        )

        return ctx


class ItemUpdate(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'user/item_form.html'
    success_url = reverse_lazy('user:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Edit Order',
            section='user',
        )

        return ctx


class ItemDelete(DeleteView):
    model = Client
    template_name = 'user/item_confirm_delete.html'
    success_url = reverse_lazy('user:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Delete Order',
            section='user',
        )

        return ctx
