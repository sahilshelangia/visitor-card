from django.shortcuts import render,redirect
from visitor.models import visitor_detail
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone
from django.urls import reverse
from datetime import datetime,timedelta
from django.http import HttpResponse
from django.views.generic import View
from utils import render_to_pdf #created in step 4
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from visitor.forms import VisitorDetailForm
@login_required
def index(request):
	return render(request,'visitor/index.html')


@login_required
def register(request):
	if request.method=="POST":
		id=request.POST['id']
		name=request.POST['name']
		name_2=request.POST['name_2']
		address=request.POST['address']
		id_no=request.POST['id_no']
		gender=request.POST['gender']
		if id_no=="":
			id_no="N/A"
		id_type=request.POST['id_type']
		if id_type=="":
			id_type="N/A"
		mob=request.POST['mob']
		if mob=="":
			mob="N/A"
		email=request.POST['email']
		if email=="":
			email="N/A"
		veh=request.POST['veh']
		if veh=="":
			veh="N/A"
		purpose=request.POST['purpose']
		dest=request.POST['dest']
		pic=request.POST['pic']
		expected_out_time=request.POST['expected_out_time']
		print("out time: ",expected_out_time)
		print(expected_out_time)
		ff="%m/%d/%Y %I:%M %p"
		expected_out_time = datetime.strptime(str(expected_out_time), ff)
		if id:
			obj=visitor_detail(id=id,name=name,name_2=name_2,gender=gender,address=address,id_no=id_no,id_type=id_type,mob=mob,email=email,veh=veh,purpose=purpose,dest=dest,pic=pic,expected_out_time=expected_out_time)
		else:
			obj=visitor_detail(name=name,name_2=name_2,gender=gender,address=address,id_no=id_no,id_type=id_type,mob=mob,email=email,veh=veh,purpose=purpose,dest=dest,pic=pic,expected_out_time=expected_out_time)
		print("This is the object ",obj)
		obj.save()
		# if email!="N/A":
		# 	subject, from_email, to = 'Visitor Details at ABV IIITM', 'surjeetsingh41097@gmail.com', email
		# 	text_content = 'This is Visitor ID Card information.'
		# 	html_content = """<h3>Welcome to IIITM, your visiting ID is """+ str(obj.id)+""".</h3>"""+	"""	<table>
		# 	<tr>
		# 		<th colspan="2">Your personal details:</th>
		# 	</tr>
		# 	<tr>
		# 		<td>Name: </td>
		# 		<td>"""+str(obj.name)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>S/D/W/O: </td>
		# 		<td>"""+str(obj.name_2)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Address: </td>
		# 		<td>"""+str(obj.address)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>ID Type: </td>
		# 		<td>"""+str(obj.id_no)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Mobile: </td>
		# 		<td>"""+str(obj.mob)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Email ID: </td>
		# 		<td>"""+str(obj.email)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Vechile No.: </td>
		# 		<td>"""+str(obj.veh)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Purpose: </td>
		# 		<td>"""+str(obj.purpose)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Destination: </td>
		# 		<td>"""+str(obj.dest)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Check In Time: </td>
		# 		<td>"""+str(obj.time_in)+"""</td>
		# 	</tr>
		# 	<tr>
		# 		<td>Expected Out Time: </td>
		# 		<td>"""+str(obj.expected_out_time)+"""</td>
		# 	</tr>
		# </table>"""
		# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		# 	msg.attach_alternative(html_content, "text/html")
		# 	msg.send()
		return redirect('visitor:checkedin_list')
		#call reminder mail function
		# notify_user(obj.id)

	form=VisitorDetailForm()
	context={'form':form}
	return render(request,'visitor/new.html',context=context)



@login_required
def update(request,id):
	obj=visitor_detail.objects.get(id=id)
	instance=visitor_detail.objects.all().get(id=id)
	if instance.email=="N/A":
		instance.email=""
	form=VisitorDetailForm(instance=instance)
	# print("Here it is")
	# print(form['expected_out_time'].value)
	obj.expected_out_time=datetime.strptime(str(obj.expected_out_time)[:18],"%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y %I:%M %p")
	# print(form['expected_out_time'].value)
	# instance.delete()
	context={'form':form,'ID':id,'obj':obj}
	return render(request,'visitor/new.html',context=context)

def re_entry(request,id):
	obj=visitor_detail.objects.get(id=id)
	instance=visitor_detail.objects.all().get(id=id)
	if instance.email=="N/A":
		instance.email=""
	form=VisitorDetailForm(instance=instance)
	# print("Here it is")
	# print(form['expected_out_time'].value)
	obj.expected_out_time=datetime.strptime(str(obj.expected_out_time)[:18],"%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y %I:%M %p")
	# print(form['expected_out_time'].value)
	# instance.delete()
	context={'form':form,'obj':obj}
	return render(request,'visitor/new.html',context=context)
	# print("original id: ",id)
	# obj=visitor_detail.objects.get(id=id)
	# instance=visitor_detail.objects.all().get(id=id)
	# foo = visitor_detail()
	# # foo.save()
	# print("Foo id: ",id)

	# # print("This is foo", foo)
	# pk=foo.id
	# foo=obj
	# foo.id=pk
	# print("Foo saved",id)
	# id=pk
	# foo.status_in=True
	# if instance.email=="N/A":
	# 	instance.email=""
	# form=VisitorDetailForm(instance=instance)
	# # print("Here it is")
	# # print(form['expected_out_time'].value)
	# obj.expected_out_time=datetime.strptime(str(obj.expected_out_time)[:18],"%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y %I:%M %p")
	# # print(form['expected_out_time'].value)
	# # instance.delete()
	# print("foo id",id)
	# context={'form':form,'ID':id,'obj':foo}
	# return render(request,'visitor/new.html',context=context)

	# obj_old=visitor_detail.objects.get(id=id)
	# obj=visitor_detail.objects.create()
	# id=obj.id
	# obj=obj_old
	# obj.status_in=True

	# instance=visitor_detail.objects.all().get(id=id)
	# if instance.email=="N/A":
	# 	instance.email=""
	# form=VisitorDetailForm(instance=instance)

	# obj.expected_out_time=datetime.strptime(str(obj.expected_out_time)[:18],"%Y-%m-%d %H:%M:%S").strftime("%m/%d/%Y %I:%M %p")
	# context={'form':form,'ID':id,'obj':obj}
	# return render(request,'visitor/new.html',context=context)


@login_required
def list_view(request):
	names=''
	id_no=''
	mob_no=''
	time_in=''
	time_out=''
	context={}
	if request.method=='POST':
		names=request.POST['name']
		id_no=request.POST['id_no']
		mob_no=request.POST['mob_no']
		ff="%m/%d/%Y %I:%M %p"
		time_in=request.POST['time_in']
		time_in=datetime.strptime(str(time_in), ff)
		time_out=request.POST['time_out']
		time_out=datetime.strptime(str(time_out), ff)

		visitors=visitor_detail.objects.filter(status_in=False).\
		filter(name__icontains=names).filter(id_no__icontains=id_no).\
		filter(mob__icontains=mob_no).filter(time_in__gte=time_in).\
		filter(time_out__lte=time_out).order_by('-time_in')
		context={'visitors':visitors}
	else:
		visitors=visitor_detail.objects.filter(status_in=False).order_by('-time_in')
		context={'visitors':visitors}
	return render(request,'visitor/list.html',context=context)

@login_required
def detail(request,pk):
	visitor=visitor_detail.objects.get(id=pk)
	context={'visitor':visitor}
	return render(request,'visitor/detail.html',context=context)

@login_required
def checkedin_list(request):
	names=''
	id_no=''
	mob_no=''
	time_in=''
	time_out=''
	context={}
	if request.method=='POST':
		names=request.POST['name']
		id_no=request.POST['id_no']
		mob_no=request.POST['mob_no']
		ff="%m/%d/%Y %I:%M %p"

		time_in=request.POST['time_in']
		time_in=datetime.strptime(str(time_in), ff)
		time_out=request.POST['time_out']
		time_out=datetime.strptime(str(time_out), ff)
		visitors=visitor_detail.objects.filter(status_in=True).filter(name__icontains=names).filter(id_no__icontains=id_no).filter(mob__icontains=mob_no).filter(time_in__gte=time_in).filter(time_out__lte=time_out).order_by('-time_in')
		context={'visitors':visitors}
	else:
		# .filter(time_in__gte=datetime.today()-timedelta(days=2))
		visitors=visitor_detail.objects.filter(status_in=True).order_by('-time_in')
		context={'visitors':visitors}
	return render(request,'visitor/checkedin_list.html',context=context)
	
@login_required
def check_out(request,pk):
	visitor=visitor_detail.objects.get(id=pk)
	visitor.time_out=datetime.now()
	visitor.status_in=False
	visitor.save()
	# if visitor.email!="N/A":
	# 	subject, from_email, to = 'Visitor Details at ABV IIITM', 'surjeetsingh41097@gmail.com', visitor.email
	# 	text_content = 'This is Visitor ID Card information.'
	# 	html_content = """<h3>Thanks for Visiting ABV IIITM.</h3>"""+	"""	<table>
	# 	<tr>
	# 		<th colspan="2">Your personal details:</th>
	# 	</tr>
	# 	<tr>
	# 		<td>Name: </td>
	# 		<td>"""+str(visitor.name)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>S/D/W/O: </td>
	# 		<td>"""+str(visitor.name_2)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Address: </td>
	# 		<td>"""+str(visitor.address)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>ID Type: </td>
	# 		<td>"""+str(visitor.id_no)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Mobile: </td>
	# 		<td>"""+str(visitor.mob)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Email ID: </td>
	# 		<td>"""+str(visitor.email)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Vechile No.: </td>
	# 		<td>"""+str(visitor.veh)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Purpose: </td>
	# 		<td>"""+str(visitor.purpose)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Destination: </td>
	# 		<td>"""+str(visitor.dest)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Check In Time: </td>
	# 		<td>"""+str(visitor.time_in)+"""</td>
	# 	</tr>
	# 	<tr>
	# 		<td>Check Out Time: </td>
	# 		<td>"""+str(visitor.time_out)+"""</td>
	# 	</tr>
	# </table>"""
	# 	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	# 	msg.attach_alternative(html_content, "text/html")
	# 	msg.send()
	context={'visitor':visitor}
	return render(request,'visitor/detail.html',context=context)

class GeneratePdf(View,LoginRequiredMixin):
	def get(self, request, *args, **kwargs):
		primary=self.kwargs['pk']
		visitor=visitor_detail.objects.get(pk=primary)
		data={'visitor':visitor}
		pdf = render_to_pdf('visitor/card.html', data)
		return HttpResponse(pdf, content_type='application/pdf')