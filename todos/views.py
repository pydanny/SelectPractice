from typing import Any, Dict

from django import forms
from django.views.generic import FormView

from .models import Todo


class TodoListForm(forms.Form):
    id_nums = forms.TypedChoiceField(choices=())

class TodoList(FormView):
    form_class = TodoListForm
    template_name = 'todos/templates/form.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['todos'] = Todo.objects.filter(is_selected=False)
        return ctx
