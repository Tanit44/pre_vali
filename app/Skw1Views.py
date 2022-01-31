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
# Create your views here.
def skw1_home(request):
    skw1_all = Skw1.objects.count()
    total_skw1 = (f'{skw1_all:,d}')
    skw1001_all = Skw1001.objects.count()
    total_skw1001 = (f'{skw1001_all:,d}')
    skw1002_all = Skw1002.objects.count()
    total_skw1002 = (f'{skw1002_all:,d}')
    skw1003_all = Skw1003.objects.count()
    total_skw1003 = (f'{skw1003_all:,d}')
    context = {
        'total_skw1': total_skw1,
        'total_skw1001': total_skw1001,
        'total_skw1002': total_skw1002,
        'total_skw1003': total_skw1003,
        }
    return render(request,"skw1/skw1_home.html", context)

# Server Side Print-out
class Skw1sJsonView(BaseDatatableView):
    # Model specification
    model = Skw1
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
# skw1001  
class MainViewSkw1001(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw1001Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw1001, self).get_context_data(**kwargs)
        context['header'] = 'ฝ่าเซิ่ง' # front to command back to display
        context['home'] = 'skw1_home'
        context['form'] = 'skw1001_form'
        context['s'] = 'Skw1001s'
        context['id_room'] = 'skw1001'
        return context


class Skw1001sJsonView(BaseDatatableView):
    # model setting
    model = Skw1001
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

class Skw1001Serializer(serializers.ModelSerializer):
    class Meta:
        model = Skw1001
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class Skw1001ViewSet(viewsets.ModelViewSet):
    serializer_class = Skw1001Serializer
    queryset = Skw1001.objects.all()


def skw1001_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw1001.objects.all().last()
            last_nId_person = last_id.nId_person
            # print(last_nId_person)
            next_nId_person = int(last_id.nId_person) + 1
            # print(next_nId_person)
            form = Skw1001Form()
            context = {
                'next_nId_person' : str(next_nId_person),
                'header' : 'ฝ่าเซิ่ง',
                'id_room' : 'skw1001',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw1001 = Skw1001.objects.get(pk=id)
            # lunar calendar
            dDate = skw1001.dDate
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
            skw1001.cDate_dc = lunar2
            # print(d)
            form = Skw1001Form(instance=skw1001)
            context = {
                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฝ่าเซิ่ง',
                'id_room' : 'skw1001',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw1001_form')
            except TableAll.DoesNotExist: # For TableAll
                form = Skw1001Form(request.POST)
                form.save()
                messages.success(request,"ได้เพิ่มผู้รับธรรมะ เข้าฐานข้อมูลกลางแล้ว")
                return redirect('/skw1001_form')
        else:
            skw1001 = Skw1001.objects.get(pk=id)
            form = Skw1001Form(request.POST,instance=skw1001)
            form.save()
            return redirect('/skw1001')

def skw1001_delete(request, id):
    skw1001 = Skw1001.objects.get(pk=id)
    skw1001.delete()
    return redirect('/skw1001')


# skw1002  
class MainViewSkw1002(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw1002Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw1002, self).get_context_data(**kwargs)
        context['header'] = 'ฉืออี' # front to command back to display
        context['home'] = 'skw1_home'
        context['form'] = 'skw1002_form'
        context['s'] = 'Skw1002s'
        context['id_room'] = 'skw1002'
        return context


class Skw1002sJsonView(BaseDatatableView):
    # model setting
    model = Skw1002
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

class Skw1002Serializer(serializers.ModelSerializer):
    class Meta:
        model = Skw1002
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class Skw1002ViewSet(viewsets.ModelViewSet):
    serializer_class = Skw1002Serializer
    queryset = Skw1002.objects.all()


def skw1002_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw1002.objects.all().last()
            last_nId_person = last_id.nId_person
            # print(last_nId_person)
            next_nId_person = int(last_id.nId_person) + 1
            # print(next_nId_person)
            form = Skw1002Form()
            context = {
                'next_nId_person' : str(next_nId_person),
                'header' : 'ฉืออี',
                'id_room' : 'skw1002',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw1002 = Skw1002.objects.get(pk=id)
            # lunar calendar
            dDate = skw1002.dDate
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
            skw1002.cDate_dc = lunar2
            # print(d)
            form = Skw1002Form(instance=skw1002)
            context = {
                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฉืออี',
                'id_room' : 'skw1002',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw1002_form')
            except TableAll.DoesNotExist: # For TableAll
                form = Skw1002Form(request.POST)
                form.save()
                messages.success(request,"ได้เพิ่มผู้รับธรรมะ เข้าฐานข้อมูลกลางแล้ว")
                return redirect('/skw1002_form')
        else:
            skw1002 = Skw1002.objects.get(pk=id)
            form = Skw1002Form(request.POST,instance=skw1002)
            form.save()
            return redirect('/skw1002')

def skw1002_delete(request, id):
    skw1002 = Skw1002.objects.get(pk=id)
    skw1002.delete()
    return redirect('/skw1002')


# skw1003  
class MainViewSkw1003(FormView):
    template_name = 'layouts/zone_n.html'
    form_class = Skw1003Form
    def get_context_data(self, **kwargs):
        context = super(MainViewSkw1003, self).get_context_data(**kwargs)
        context['header'] = 'ฉือจิ้ง' # front to command back to display
        context['home'] = 'skw1_home'
        context['form'] = 'skw1003_form'
        context['s'] = 'Skw1003s'
        context['id_room'] = 'skw1003'
        return context


class Skw1003sJsonView(BaseDatatableView):
    # model setting
    model = Skw1003
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

class Skw1003Serializer(serializers.ModelSerializer):
    class Meta:
        model = Skw1003
        fields = '__all__'
        # fields = ('id', 'nId_person', 'cFname')


class Skw1003ViewSet(viewsets.ModelViewSet):
    serializer_class = Skw1003Serializer
    queryset = Skw1003.objects.all()


def skw1003_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            last_id = Skw1003.objects.all().last()
            last_nId_person = last_id.nId_person
            # print(last_nId_person)
            next_nId_person = int(last_id.nId_person) + 1
            # print(next_nId_person)
            form = Skw1003Form()
            context = {
                'next_nId_person' : str(next_nId_person),
                'header' : 'ฉือจิ้ง',
                'id_room' : 'skw1003',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
        else:
            skw1003 = Skw1003.objects.get(pk=id)
            # lunar calendar
            dDate = skw1003.dDate
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
            skw1003.cDate_dc = lunar2
            # print(d)
            form = Skw1003Form(instance=skw1003)
            context = {
                'dDate' : dDate,
                'lunar1' : str(lunar1), #'%Y-%m-%d'
                'lunar2' : str(lunar2), #'%Y.%m.%d'
                'header' : 'ฉือจิ้ง',
                'id_room' : 'skw1003',
                'form': form,
            }
            return render(request, "layouts/zone_n_form.html", context)
    else:
        if id == 0:
            try:
                user_exists = TableAll.objects.get(cFname=request.POST['cFname']) # For TableAll
                # user_exists = Bkk1001.objects.get(cFname=request.POST['cFname']) # For Bkk1001
                messages.error(request,"ผู้รับธรรมะท่านนี้ รับธรรมะแล้ว !!!")
                return redirect('/skw1003_form')
            except TableAll.DoesNotExist: # For TableAll
                form = Skw1003Form(request.POST)
                form.save()
                messages.success(request,"ได้เพิ่มผู้รับธรรมะ เข้าฐานข้อมูลกลางแล้ว")
                return redirect('/skw1003_form')
        else:
            skw1003 = Skw1003.objects.get(pk=id)
            form = Skw1003Form(request.POST,instance=skw1003)
            form.save()
            return redirect('/skw1003')

def skw1003_delete(request, id):
    skw1003 = Skw1003.objects.get(pk=id)
    skw1003.delete()
    return redirect('/skw1003')