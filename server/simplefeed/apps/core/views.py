from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, ListView
)

from pure_pagination.mixins import PaginationMixin
from braces.views import OrderableListMixin
from enhanced_cbv.views import ListFilteredView
from allauth.account.utils import complete_signup
from allauth.account.app_settings import EMAIL_VERIFICATION

from .decorators import ForbiddenUser

from .forms import LoginForm
from .forms import SignUpUserForm

from core.models import (
    User,
    Message,
)


def register(request):
    signup_form_user = SignUpUserForm(prefix="user", request=request)

    redirect_url = '/'
    redirect_url = request.GET.get('next') or redirect_url

    if request.method == 'POST' and 'signup_user_form' in request.POST:
        signup_form_user = SignUpUserForm(
            request.POST,
            prefix="user",
            request=request)

        if signup_form_user.is_valid():
            user = signup_form_user.save(request)
            return complete_signup(
                request,
                user,
                EMAIL_VERIFICATION,
                redirect_url)

    return render(request, "register.html", {
        "signup_form_user": signup_form_user,
    })
