from .models import Event, Participant, Category
from django import forms

class StyledFormMixin:
    """Form fields এ premium glassmorphism styling add করার জন্য Mixin।"""
    default_classes = "w-full px-5 py-3 rounded-xl border bg-slate-900  text-slate-200 shadow-sm placeholder-slate-500"

    def apply_styled_widgets(self):
        for field_name, field in self.fields.items():
            label_text = field.label if field.label else field_name.replace('_', ' ').capitalize()

            if isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class': 'mt-2 space-y-2 text-gray-700'
                })
            else:
                existing_classes = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = f"{self.default_classes} {existing_classes}".strip()

                if isinstance(field.widget, (forms.TextInput, forms.EmailInput, forms.Textarea)):
                    field.widget.attrs.update({
                        'placeholder': f"Enter {label_text.lower()}..."
                    })

                if isinstance(field.widget, forms.Textarea):
                    field.widget.attrs.update({
                        'rows': 4,
                        'class': f"{self.default_classes} resize-none"
                    })

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()

class EventForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'time', 'location', 'category']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Select date...'
                }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'placeholder': 'Select time...'
            }),
        }

class ParticipantForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'email', 'event']
        widgets = {
            
            'event': forms.CheckboxSelectMultiple(),
        }
        

class CategoryForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter category name...'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Write a short description...',
                'rows': 4
            }),
        }
