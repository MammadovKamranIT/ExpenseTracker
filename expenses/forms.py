from django import forms
from.models import Expense

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Имя',
        max_length=100,
        min_length=1,
        widget=forms.TextInput(attrs={'placeholder':'Enter your name'})
    )
    email = forms.EmailField(
        label='Почта',
        widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))

    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={'placeholder':'Enter your message', 'rows':'5'}),
    )


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title','payment_type', 'category', 'amount']

        labels = {

            'title': "Title",
            'payment type': "Payment type",
            'category': "Category",
            'amount': "Amount"
        }




        widgets = {

        "title": forms.TextInput(),
        'category':forms.Select(), 
        'payment_type':forms.Select(),
        'amount': forms.NumberInput()
                                                                                   
        }




 

def clean_title(self):
    title = self.cleaned_data['title'].strip()
    if title.lower().startswith('test'):
        raise forms.ValidationError("Title should not start with 'test'")
    return title