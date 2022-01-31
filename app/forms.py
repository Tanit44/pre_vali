from django import forms
from .models import *
import bootstrap_datepicker_plus as datetimepicker

class TableAllForm(forms.ModelForm):
    class Meta:
        model = TableAll
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }
    def __init__(self, *args, **kwargs):
        super(TableAllForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AddusertypeForm(forms.ModelForm):
    class Meta:
        model = UserType
        fields = ('id', 'user_type_name')

    def __init__(self, *args, **kwargs):
        super(AddusertypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class StaffForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput() 
        }

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Bkk1001Form(forms.ModelForm):
    class Meta:
        model = Bkk1001
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(Bkk1001Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'หมิงซิน'

class Bkk1002Form(forms.ModelForm):
    class Meta:
        model = Bkk1002
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(Bkk1002Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'หมิงฮุย'

class Bkk1003Form(forms.ModelForm):
    class Meta:
        model = Bkk1003
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(Bkk1003Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ฉือเฉิง'

class Skw1001Form(forms.ModelForm):
    class Meta:
        model = Skw1001
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(Skw1001Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ฝ่าเซิง'

class Skw1002Form(forms.ModelForm):
    class Meta:
        model = Skw1002
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(Skw1002Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ฉืออี'

class Skw1003Form(forms.ModelForm):
    class Meta:
        model = Skw1003
        fields = '__all__'
        # fields = ('id', 'cFname', 'nId_person', 'cGender', 'nAge', 'cLevel', 'cEdu', 'cCareer', 'cRoom', 'cPro', 'dDate', 'cDate_dc', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName')
        widgets = {
            'dDate': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                     'locale': 'th',
                     'dayViewHeaderFormat': 'YYYY(ค.ศ) MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(Skw1003Form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['cRoom'].initial = 'ฉือจิ้ง'
