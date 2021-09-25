from typing import Any, Dict

from django import forms
from django.views.generic import FormView

from .models import Todo


class TodoListForm(forms.Form):
    id_nums = forms.TypedChoiceField(choices=())

    def __init__(self, todos, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Need to do this as choices
        todo_choices = [(x.id, x.id) for x in todos]
        self.fields['id_nums'].choices = todo_choices


class TodoList(FormView):
    form_class = TodoListForm
    template_name = 'todos/templates/form.html'

    def form_valid(self, form):
        print(form.clean_data)
        return super.form_valid(form)

    def get_queryset(self):
        return Todo.objects.filter(is_selected=False)

    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['todos'] = self.get_queryset()
        return kwargs

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['todos'] = self.get_queryset()
        return ctx
