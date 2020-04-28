from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404

from shopping_cart.models import Order
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            user_type = form.cleaned_data.get('user_type')
            buyer = Group.objects.get(name='Buyer')
            seller = Group.objects.get(name='Seller')

            if user_type == 'buyer':
                user.groups.add(buyer)
            else:
                user.groups.add(seller)

            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to login')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'user/profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'user/password_change.html', {'form': form})


@login_required
def my_orders(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Order.objects.filter(is_ordered=True, owner=my_user_profile)
    order_list = Order.objects.filter(is_ordered=True)
    my_user = Profile.objects.filter(user=request.user)
    context = {
        'my_orders': my_orders,
        'my_user': my_user,
        'order_list': order_list
    }

    return render(request, "order.html", context)
