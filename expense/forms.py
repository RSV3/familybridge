from django import forms
from expense.models import Expense, Contribution

class AddExpenseForm(forms.ModelForm):

  class Meta:
    model = Expense

  def __init__(self, *args, **kwargs):
    super(AddExpenseForm, self).__init__(*args, **kwargs)

    signup_field_width = 370

    self.fields['date'].widget.attrs['class'] = 'form-control'
    #self.fields['first_name'].widget.attrs['style'] = 'width:%dpx;' % (signup_field_width/2)
    self.fields['date'].widget.attrs['placeholder'] = 'MM/DD/YYYY'
    self.fields['date'].widget.attrs['type'] = 'date'
    self.fields['amount'].widget.attrs['class'] = 'form-control'
    #self.fields['last_name'].widget.attrs['style'] = 'width:%dpx;' % (signup_field_width/2)
    self.fields['amount'].widget.attrs['placeholder'] = 'Amount'
    self.fields['title'].widget.attrs['class'] = 'form-control'
    #self.fields['email'].widget.attrs['style'] = 'width:%dpx;' % signup_field_width
    self.fields['title'].widget.attrs['placeholder'] = 'Title'

    self.fields['description'].widget.attrs['class'] = 'form-control'
    #self.fields['password1'].widget.attrs['style'] = 'width:%dpx;' % signup_field_width
    self.fields['description'].widget.attrs['placeholder'] = 'Description'
    self.fields['category'].widget.attrs['class'] = 'form-control'
    #self.fields['password2'].widget.attrs['style'] = 'width:%dpx;' % signup_field_width
    self.fields['category'].widget.attrs['placeholder'] = 'Category'


PERCENTAGE_CHOICES = (
  (0, '------'),
  (10, '10%'),
  (20, '20%'),
  (30, '30%'),
  (40, '40%'),
  (50, '50%'),
  (60, '60%'),
  (70, '70%'),
  (80, '80%'),
  (90, '90%'),
  (100, '100%'),
)

class ContributeForm(forms.ModelForm):

  class Meta:
    model = Contribution


class AddContributorForm(forms.ModelForm):

  percentage = forms.ChoiceField(widget=forms.Select, choices=PERCENTAGE_CHOICES)

  class Meta:
    model = Contribution
    fields = ['contributor', 'percentage']

  def __init__(self, *args, **kwargs):
    super(AddContributorForm, self).__init__(*args, **kwargs)

    self.fields['contributor'].widget.attrs['class'] = 'form-control'
    self.fields['percentage'].widget.attrs['class'] = 'form-control'
