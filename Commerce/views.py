# import json
from itertools import chain

from allauth.account.views import SignupView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin

from .forms import ItemForm, RegistrationForm, EditItemForm
from .models import Item, User


def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class HomeView(ListView):
    template_name = 'home-page.html'
    paginate_by = 8
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        context['item'] = self.request.GET.get('name')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            item_results = Item.objects.search(query=query).filter(ordered=False)
            # combine querysets
            queryset_chain = chain(
                item_results
                # order_results,
                # orderitem_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Item.objects.filter(ordered=False).order_by('-pk')  # just an empty queryset as default


class GetClothes(ListView):
    template_name = 'home-page.html'
    paginate_by = 8
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            item_results = Item.objects.search(query=query).filter(category='C', ordered=False)
            # combine querysets
            queryset_chain = chain(
                item_results
                # order_results,
                # orderitem_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Item.objects.filter(category='C', ordered=False).order_by('-pk')


class GetFurniture(ListView):
    template_name = 'home-page.html'
    paginate_by = 8
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            item_results = Item.objects.search(query=query).filter(category='F', ordered=False)
            # combine querysets
            queryset_chain = chain(
                item_results
                # order_results,
                # orderitem_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Item.objects.filter(category='F', ordered=False).order_by('-pk')


class GetFoodstuff(ListView):
    template_name = 'home-page.html'
    paginate_by = 8
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            item_results = Item.objects.search(query=query).filter(category='Fd', ordered=False)
            # combine querysets
            queryset_chain = chain(
                item_results
                # order_results,
                # orderitem_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Item.objects.filter(category='Fd', ordered=False).order_by('-pk')


class GetElectronic(ListView):
    template_name = 'home-page.html'
    paginate_by = 8
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            item_results = Item.objects.search(query=query).filter(category='E', ordered=False)
            # combine querysets
            queryset_chain = chain(
                item_results
                # order_results,
                # orderitem_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Item.objects.filter(category='E', ordered=False).order_by('-pk')


class GetRental(ListView):
    template_name = 'home-page.html'
    paginate_by = 8
    count = 0
    category = 'R'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')

        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:
            item_results = Item.objects.search(query=query).filter(category='R', ordered=False)
            # combine querysets
            queryset_chain = chain(
                item_results
                # order_results,
                # orderitem_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Item.objects.filter(category='R', ordered=False).order_by('-pk')


class ItemDetailView(SingleObjectMixin, ListView):
    paginate_by = 8
    model = Item
    template_name = 'product-page.html'

    def get(self, requests, *args, **kwargs):
        self.object = self.get_object(queryset=Item.objects.all())
        return super().get(requests, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.object
        return context

    def get_queryset(self):
        return Item.objects.filter(ordered=False).order_by('-pk')


def view_seller(request, user):
    seller = User.objects.get(username=user)
    data = {
        'seller': seller
    }
    return render(request, 'user.html', data)


class UploadItem(LoginRequiredMixin, View):
    def get(self, request):
        form = ItemForm()
        args = {
            'form': form
        }
        return render(self.request, 'item_upload.html', args)

    def post(self, request):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(self.request, 'Your upload was successful')
            return redirect('commerce:home')

        else:
            form = ItemForm()

            messages.warning(self.request, 'Your upload was unsuccessful')
            return render(request, 'commerce:upload', {'form': form})


@login_required
def edit_item(request, slug):
    product_to_edit = get_object_or_404(Item, slug=slug)
    form = EditItemForm(instance=product_to_edit)

    if request.method == 'POST':
        form = EditItemForm(request.POST, instance=product_to_edit)

        if form.is_valid():
            form.save()
            messages.info(request, 'Product editing was successful')
            return redirect('commerce:my-account')
        else:
            form = EditItemForm(instance=product_to_edit)
            messages.warning(request, 'editing was unsuccessful')

    return render(request, 'item_edit.html', {'form': form, 'product': product_to_edit})


@login_required
def remove_item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    item.delete()
    messages.info(request, 'Product removed successfully')
    return redirect('commerce:my-account')


class UserSignUp(SignupView):
    template_name = 'account/signup.html'
    form_class = RegistrationForm
    redirect_field_name = 'next'
    view_name = 'account_signup'

    def get_context_data(self, **kwargs):
        ret = super(UserSignUp, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


class TransactionSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            item = Item.objects.filter(user=self.request.user)

            # print(data)
            data = {
                'product': item,
            }
            return render(self.request, 'my_account.html', data)

        except ObjectDoesNotExist:
            messages.warning(self.request, "you do not have an active order ")
            return redirect('/')
