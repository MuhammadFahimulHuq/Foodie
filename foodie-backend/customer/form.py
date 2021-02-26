from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
            'customer_password',
            'customer_address',
            'customer_email',
            'customer_phoneNo',
            'customer_accountCreated',
            'customer_profilePicture',
            'customer_dateOfBirth',
        ]


class RawCustomerForm(forms.Form):
    customer_name = forms.CharField(max_length=100, min_length=5)
    customer_password = forms.PasswordInput()
    customer_address = forms.Textarea(max_length=200)
    customer_email = forms.EmailField(max_length=62)
    customer_phoneNo = forms.CharField(max_length=20, min_length=10)
    customer_dateOfBirth = forms.DateField()
