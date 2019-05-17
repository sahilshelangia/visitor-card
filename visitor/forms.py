from django import forms
from visitor.models import visitor_detail

class VisitorDetailForm(forms.ModelForm):
	class Meta():
		model=visitor_detail
		fields='__all__'
		widgets={
		'name': forms.TextInput(attrs={'name':"name",'class':"form-control",'placeholder':"Name of Visitor",'required':"required"}),
		'gender': forms.Select(attrs={'name':"name_2",'class':"form-control",'placeholder':"Father's/Husband's Name",'required':"required"}),		
		'name_2':forms.TextInput(attrs={'name':"name",'class':"form-control",'placeholder':"Name of Visitor",'required':"required"}),
		'address':forms.TextInput(attrs={'name':"address",'class':"form-control",'required':"required",'placeholder':"Address"}),
		'id_no':forms.TextInput(attrs={'name':"id_no",'class':"form-control" ,'placeholder':"ID number"}),
		'id_type':forms.TextInput(attrs={'name':"id_type",'class':"form-control",'placeholder':"ID Type"}),
		'mob':forms.TextInput(attrs={ 'name':"mob",'class':"form-control",'id':"datepicker2",'placeholder':"Mobile"}),
		'email':forms.EmailInput(attrs={'name':"email",'class':"form-control",'id':"datepicker2",'placeholder':"Email"}),
		'veh':forms.TextInput(attrs={'name':"veh",'class':"form-control",'placeholder':"Vehicle Number"}),
		'purpose':forms.TextInput(attrs={'name':"purpose", 'class':"form-control",'required':"required", 'placeholder':"Purpose of Visit"}),
		'dest':forms.TextInput(attrs={'name':"dest",'class':"form-control",'required':"required",'id':"datepicker",'placeholder':"Destination"}),
		'expected_out_time': forms.TextInput(attrs={ 'class':"form-control datepick" ,'name':"expected_out_time" ,'id':"frmSaveOffice_startdt", 'placeholder':"Valid Upto",'required':"required"}),
		}