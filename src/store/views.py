from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Store
from products.models import Product
# from products.views import search


def home(request):
    context = {
        'stores': Store.objects.all(),
    }

    return render(request, 'store/home.html', context)


class StoreListView(ListView):
    model = Store
    template_name = 'store/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'stores'


class StoreDetailView(DetailView):
    model = Store


class StoreCreateView(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['restaurant_name', 'description', 'restaurant_address', 'restaurant_address_2', 'mobile',
              'email', 'city', 'state']
    success_url = '/'  # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class StoreUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Store
    fields = ['restaurant_name', 'description', 'restaurant_address', 'restaurant_address_2', 'mobile',
              'email', 'city', 'state']
    success_url = '/'  # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    # uncomment when owner is added in models.py
    def test_func(self):
        store = self.get_object()
        if self.request.user == store.owner:
            return True
        return False


class StoreDeleteView(LoginRequiredMixin, DeleteView):
    model = Store
    success_url = '/'  # navigate to home page after creating a new store.

    # uncomment when owner is added in models.py
    def test_func(self):
        store = self.get_object()
        if self.request.user == store.owner:
            return True
        return False


def about(request):
    return render(request, 'store/about.html')  # {'title': 'About'}

# trial


# class IndexView(DetailView):
#     model = Store
#     template_name = 'lst.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(IndexView, self).get_context_data(*args, **kwargs)
#         context['id'] = Store.objects.all()
#         return context
class IndexView(DetailView):
    model = Store

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id'] = Product.objects.all()
        return context
