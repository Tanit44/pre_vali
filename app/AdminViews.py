from django.shortcuts import render, redirect
from app.models import *
from .forms import *
from django.db.models import Q

from datetime import datetime
from lunarcalendar import Converter, Solar, Lunar, DateNotExist

from django.views.generic import FormView
# from django_datatables_view.base_datatable_view import BaseDatatableView
from rest_framework import serializers
from rest_framework import viewsets

from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView


def admin_home(request):
    total_all = TableAll.objects.count()
    total_all = (f'{total_all:,d}')
    total_bkk1 = Bkk1.objects.count()
    total_bkk1 = (f'{total_bkk1:,d}')
    total_skw1 = Skw1.objects.count()
    total_skw1 = (f'{total_skw1:,d}')
    context = {
        'total_all': total_all,
        'total_bkk1': total_bkk1,
        'total_skw1': total_skw1,
    }
    return render(request,"admin/admin_home.html", context)

def add_user_type(request):
    msg     = None
    success = False
    if request.method == "POST":
        form = AddusertypeForm(request.POST)
        if form.is_valid():
            form.save()
            msg     = 'User Type Created'
            success = True

        else:
            msg = 'Form is not valid'    
    else:
        form = AddusertypeForm()

    return render(request, "admin/add_user_type.html", {"form": form, "msg" : msg, "success" : success })

def add_staff(request):
    usertypes=UserType.objects.all()
    msg     = None
    success = False

    if request.method == "POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user_type=request.POST.get("user_type")
        try:
            form=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=user_type)
            form.save()

            msg     = 'Add Staff created'
            success = True
        except:
            msg = 'Form is not valid'    
    else:
        form = StaffForm()

    return render(request, "admin/add_staff.html", {"form": form, "msg" : msg, "success" : success, "usertypes":usertypes})

# Web API that provides data to DataTables
# django-datatables-view
# https://pypi.org/project/django-datatables-view/
class TableAllsJsonView(BaseDatatableView):
    # Model specification
    model = TableAll
    # Field specification
    columns = ['id', 'nId_person', 'cGender', 'cFname', 'nAge', 'cRoom', 'dDate', 'cPro', 'cRec', 'cSup']

    # Specify search method: Partial match
    # def get_filter_method(self):
    #     return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
            # use parameters passed in GET request to filter queryset

            # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs


# Base class for printing / Excel / CSV output
class BaseReportView(generic.ListView):
    model = TableAll

    # Get selected data
    def get_queryset(self):
        id_list = self.request.GET['id_list'].split('_')
        # result = Item.objects.filter(id__in=id_list)
        result = TableAll.objects.filter(id__in=id_list)
        return result


# Print screen display
class PrintView(BaseReportView):
    # template_name = 'sample/print.html'
    template_name = 'admin/print.html'

# staff_list    
class MainViewStaff(FormView):
    template_name = 'admin/staff.html'
    form_class = StaffForm
    def get_context_data(self, **kwargs):
        context = super(MainViewStaff, self).get_context_data(**kwargs)
        context['s'] = 'Staffs' # front to command back to display
        context['home'] = 'admin_home'
        context['form'] = 'add_staff'
        context['id_room'] = 'staff'
        return context

class StaffsJsonView(BaseDatatableView):
    # model setting
    model = CustomUser
    # columns setting
    columns = ['id', 'username','first_name','last_name', 'email', 'user_type', 'password']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
            # use parameters passed in GET request to filter queryset

            # simple example:
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = CustomUser.objects.all()


def staff_delete(request, id):
    staff = CustomUser.objects.get(pk=id)
    staff.delete()
    return redirect('/staff')


def tableall_form(request, id=0):    
    tableall = TableAll.objects.get(pk=id)
    # lunar calendar
    dDate = tableall.dDate
    sdDate = str(dDate)
    sdDate_obj = datetime.strptime(sdDate, '%Y-%m-%d') 
    year = int(sdDate_obj.strftime('%Y'))
    month = int(sdDate_obj.strftime('%m'))
    dd = int(sdDate_obj.strftime('%d'))
    solar = Solar(year, month, dd)
    solar1 = solar.to_date()
    # print(solar1)
    # print(dDate)
    lunar = Converter.Solar2Lunar(solar)
    lunar1 = str(datetime(lunar.year, lunar.month, lunar.day))[:-9]
    ldDate_obj = datetime.strptime(lunar1, '%Y-%m-%d')
    lunar2 = ldDate_obj.strftime('%Y.%m.%d')
    # print(ldDate_obj.strftime('%Y.%m.%d'))
    # print(lunar2)
    tableall.cDate_dc = lunar2
    # print(d)
    form = TableAllForm(instance=tableall)
    context = {
        'dDate' : dDate,
        'lunar1' : str(lunar1), #'%Y-%m-%d'
        'lunar2' : str(lunar2), #'%Y.%m.%d'
        'form': form,
    }
    return render(request, "layouts/tableall_form.html", context) 
    
def add_user_type(request):
    msg     = None
    success = False
    if request.method == "POST":
        form = AddusertypeForm(request.POST)
        if form.is_valid():
            form.save()
            msg     = 'User Type Created'
            success = True
            
            # return redirect("/add_user_type/")

        else:
            msg = 'Form is not valid'    
    else:
        form = AddusertypeForm()

    return render(request, "admin/add_user_type.html", {"form": form, "msg" : msg, "success" : success })