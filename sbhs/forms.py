from django import forms

class userForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class eventForm(forms.Form):
    event_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput()
    )
    event_start_date = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget()
    )
    event_end_date = forms.DateField(
        required=True,
        widget=forms.SelectDateWidget()
    )
    timeSlot = forms.ChoiceField(
        required=True,
        choices=[
            ('', 'Select a time slot'),
            ('9AM-1PM', '9 AM - 1 PM'),
            ('1PM-5PM', '1 PM - 5 PM'),
            ('9AM-5PM', 'Full Day')
        ],
        widget=forms.Select()
    )
    event_description = forms.CharField(
        required=True,
        widget=forms.Textarea()
    )
    event_hall = forms.ChoiceField(
        required=True,
        choices=[
            ('', 'Select a hall'),
            ('Ramegowda', 'Ramegowda Seminar Hall'),
            ('Training', 'Training Hall')
        ],
        widget=forms.Select()
    )
