
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Review
from .forms import ReviewForm


class ItemList(ListView):
    model = Review
    template_name = 'reviews/item_list.html'
    context_object_name = 'items'
    paginate_by = 12

    def get_queryset(self):
        qs = Review.objects.all()

        search = self.request.GET.get('q', '').strip()

        if search:
            qs = qs.filter(
                Q(author_name__icontains=search) |
                Q(comment__icontains=search)
            )

        sort = self.request.GET.get('sort', '')
        allowed = ['pk', '-pk']

        if sort in allowed:
            qs = qs.order_by(sort)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Reviews',
            section='reviews',
        )

        return ctx


class ItemDetail(DetailView):
    model = Review
    template_name = 'reviews/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Reviews',
            section='reviews',
        )

        return ctx


class ItemCreate(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/item_form.html'
    success_url = reverse_lazy('reviews:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Add Review',
            section='reviews',
        )

        return ctx


class ItemUpdate(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/item_form.html'
    success_url = reverse_lazy('reviews:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Edit Review',
            section='reviews',
        )

        return ctx


class ItemDelete(DeleteView):
    model = Review
    template_name = 'reviews/item_confirm_delete.html'
    success_url = reverse_lazy('reviews:list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx.update(
            page_title='Delete Review',
            section='reviews',
        )

        return ctx
