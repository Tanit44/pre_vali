from django.shortcuts import render, redirect
from django.contrib import messages
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

def bkk1_home(request):
    bkk1_all = Bkk1.objects.count()
    total_bkk1 = (f'{bkk1_all:,d}')
    bkk1001_all = Bkk1001.objects.count()
    total_bkk1001 = (f'{bkk1001_all:,d}')
    bkk1002_all = Bkk1002.objects.count()
    total_bkk1002 = (f'{bkk1002_all:,d}')
    bkk1003_all = Bkk1003.objects.count()
    total_bkk1003 = (f'{bkk1003_all:,d}')
    context = {
        'total_bkk1': total_bkk1,
        'total_bkk1001': total_bkk1001,
        'total_bkk1002': total_bkk1002,
        'total_bkk1003': total_bkk1003,
        }
    return render(request,"bkk1/bkk1_home.html", context)

# Server Side Print-out
class Bkk1sJsonView(BaseDatatableView):
    # Model specification
    model = Bkk1
    # Field specification
    columns = ['id', 'nId_person', 'cGender', 'cFname', 'nAge', 'cRoom', 'dDate', 'cPro', 'cRec', 'cSup', 'Reference_id']

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

# Sever Side Save/Edit
# bkk1001  
class MainViewBkk1001(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Bkk1001Form
    def get_context_data(self, **kwargs):
        context = super(MainViewBkk1001, self).get_context_data(**kwargs)
        context['header'] = 'หมิงซิน' # front to command back to display
        context['home'] = 'bkk1_home'
        context['form'] = 'bkk1001_form'
        context['s'] = 'Bkk1001s'
        context['id_room'] = 'bkk1001'
        return context


class Bkk1001sJsonView(BaseDatatableView):
    # model setting
    model = Bkk1001
    # columns setting
    columns = ['id', 'nId_person', 'cFname', 'cGender', 'nAge', 'cPro', 'dDate', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

class Bkk1001Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bkk1001
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class Bkk1001ViewSet(viewsets.ModelViewSet):
    serializer_class = Bkk1001Serializer
    queryset = Bkk1001.objects.all()

def bkk1001_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            last_id = Bkk1001.objects.all().last()
            last_nId_person = last_id.nId_person
            # print(last_nId_person)
            next_nId_person = int(last_id.nId_person) + 1
            # print(next_nId_person)
            form = Bkk1001Form()
            context = {
                'next_nId_person' : str(next_nId_person),
                'header' : 'หมิงซิน',
                'id_room' : 'bkk1001',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            bkk1001 = Bkk1001.objects.get(pk=id)
            # lunar calendar
            dDate = bkk1001.dDate
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
            bkk1001.cDate_dc = lunar2
            # print(d)
            form = Bkk1001Form(instance=bkk1001)
            context = {
                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'หมิงซิน',
                'id_room' : 'bkk1001',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/bkk1001_form')
            except TableAll.DoesNotExist: # For TableAll
                form = Bkk1001Form(request.POST)
                form.save()
                messages.success(request,"ได้เพิ่มผู้รับธรรมะ เข้าฐานข้อมูลกลางแล้ว")
                return redirect('/bkk1001_form')
        else:
            bkk1001 = Bkk1001.objects.get(pk=id)
            form = Bkk1001Form(request.POST,instance=bkk1001)
            form.save()
            return redirect('/bkk1001')

def bkk1001_delete(request, id):
    bkk1001 = Bkk1001.objects.get(pk=id)
    bkk1001.delete()
    return redirect('/bkk1001')

# bkk1002  
class MainViewBkk1002(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Bkk1002Form
    def get_context_data(self, **kwargs):
        context = super(MainViewBkk1002, self).get_context_data(**kwargs)
        context['header'] = 'หมิงฮุย' # front to command back to display
        context['form'] = 'bkk1002_form'
        context['s'] = 'Bkk1002s'
        context['id_room'] = 'bkk1002'
        return context

class Bkk1002sJsonView(BaseDatatableView):
    # model setting
    model = Bkk1002
    # columns setting
    columns = ['id', 'nId_person', 'cFname', 'cGender', 'nAge', 'cPro', 'dDate', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

class Bkk1002Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bkk1002
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class Bkk1002ViewSet(viewsets.ModelViewSet):
    serializer_class = Bkk1002Serializer
    queryset = Bkk1002.objects.all()


def bkk1002_form(request, id=0):
    # return render(request, "bkk1/bkk1001_form.html")
    if request.method == "GET":
        if id == 0:
            last_id = Bkk1002.objects.all().last()
            last_nId_person = last_id.nId_person
            # print(last_nId_person)
            next_nId_person = int(last_id.nId_person) + 1
            # print(next_nId_person)
            form = Bkk1002Form()
            context = {
                'next_nId_person' : str(next_nId_person),
                'header' : 'หมิงฮุย',
                'id_room' : 'bkk1002',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            bkk1002 = Bkk1002.objects.get(pk=id)
            # lunar calendar
            dDate = bkk1002.dDate
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
            bkk1002.cDate_dc = lunar2
            # print(d)
            form = Bkk1002Form(instance=bkk1002)
            context = {
                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'หมิงฮุย',
                'id_room' : 'bkk1002',
                'form': form,
            }
            # return render(request, "skw1_template/skw1001_form.html", context)
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/bkk1003_form')
            except TableAll.DoesNotExist: # For TableAll
                form = Bkk1002Form(request.POST)
                form.save()
                messages.success(request,"ได้เพิ่มผู้รับธรรมะ เข้าฐานข้อมูลกลางแล้ว")
                return redirect('/bkk1002_form')
        else:
            bkk1002 = Bkk1002.objects.get(pk=id)
            form = Bkk1002Form(request.POST,instance=bkk1002)
            form.save()
            return redirect('/bkk1002')

def bkk1002_delete(request, id):
    bkk1002 = Bkk1002.objects.get(pk=id)
    bkk1002.delete()
    return redirect('/bkk1002')



# bkk1003  
class MainViewBkk1003(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Bkk1003Form
    def get_context_data(self, **kwargs):
        context = super(MainViewBkk1003, self).get_context_data(**kwargs)
        context['header'] = 'ฉือเฉิง' # front to command back to display
        context['form'] = 'bkk1003_form'
        context['s'] = 'Bkk1003s'
        context['id_room'] = 'bkk1003'
        return context


class Bkk1003sJsonView(BaseDatatableView):
    # model setting
    model = Bkk1003
    # columns setting
    columns = ['id', 'nId_person', 'cFname', 'cGender', 'nAge', 'cPro', 'dDate', 'cRec', 'cSup', 'cAddress', 'cMtel', 'cHtel', 'cName']

    # Specify search method: Partial match
    def get_filter_method(self):
        return super().FILTER_ICONTAINS

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(cFname__istartswith=search) |
                Q(nId_person__istartswith=search)
            )
        return qs

class Bkk1003Serializer(serializers.ModelSerializer):
    class Meta:
        model = Bkk1003
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class Bkk1003ViewSet(viewsets.ModelViewSet):
    serializer_class = Bkk1003Serializer
    queryset = Bkk1003.objects.all()


def bkk1003_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            last_id = Bkk1003.objects.all().last()
            last_nId_person = last_id.nId_person
            # print(last_nId_person)
            next_nId_person = int(last_id.nId_person) + 1
            # print(next_nId_person)
            form = Bkk1003Form()
            context = {
                'next_nId_person' : str(next_nId_person),
                'header' : 'ฉือเฉิง',
                'id_room' : 'bkk1003',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            bkk1003 = Bkk1003.objects.get(pk=id)
            # lunar calendar
            dDate = bkk1003.dDate
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
            bkk1003.cDate_dc = lunar2
            # print(d)
            form = Bkk1003Form(instance=bkk1003)
            context = {
                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฉือเฉิง',
                'id_room' : 'bkk1003',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/bkk1003_form')
            except TableAll.DoesNotExist: # For TableAll
                form = Bkk1001Form(request.POST)
                form.save()
                messages.success(request,"ได้เพิ่มผู้รับธรรมะ เข้าฐานข้อมูลกลางแล้ว")
                return redirect('/bkk1003_form')
        else:
            bkk1003 = Bkk1003.objects.get(pk=id)
            form = Bkk1003Form(request.POST,instance=bkk1003)
            form.save()
            return redirect('/bkk1003')

def bkk1003_delete(request, id):
    bkk1003 = Bkk1003.objects.get(pk=id)
    bkk1003.delete()
    return redirect('/bkk1003')
