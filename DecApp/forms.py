from django import forms

from DecApp.models import Work_Details



class DateInput(forms.DateInput):
    input_type = 'date'
class Work_Form(forms.ModelForm):
    Date = forms.DateField(widget=DateInput)
    Finished_date = forms.DateField(widget=DateInput)
    Delivery_Date = forms.DateField(widget=DateInput)
    class Meta:
        model = Work_Details
        fields = "__all__"
