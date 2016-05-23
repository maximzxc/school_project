import django_filters
import django_select2

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Reset

from core.models import (
    User,
    Message,
)


class UserChoiceField(django_select2.AutoModelSelect2Field):
    queryset = User.objects.all()
    search_fields = []


class MessageChoiceField(django_select2.AutoModelSelect2Field):
    queryset = Message.objects.all()
    search_fields = []


class UserChoiceFilter(django_filters.Filter):
    field_class = UserChoiceField


class MessageChoiceFilter(django_filters.Filter):
    field_class = MessageChoiceField


# Have to call it clearly to help django_select2 register fields
UserChoiceField()
MessageChoiceField()
