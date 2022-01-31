"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views, AdminViews, Bkk1Views, Skw1Views
from django.views.generic.base import TemplateView

urlpatterns = [
    #API
    path('api/all_tablelist', views.All_TableList),
    #Admin
    path('admin/', admin.site.urls),
    path('', views.ShowLoginPage,name="show_login"),
    path('doLogin', views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"), 
    path("add_user_type/", AdminViews.add_user_type, name="add_user_type"),     
    path("add_staff/", AdminViews.add_staff, name="add_staff"),       
    path('staff', AdminViews.MainViewStaff.as_view(),name="staff"),
    path('api/Staffs', AdminViews.StaffsJsonView.as_view(), name='StaffsJsonView'),
    path('delete/staff/<int:id>/', AdminViews.staff_delete,name="staff_delete"),
    # Server-Side admin
    path('admin_home', AdminViews.admin_home,name="admin_home"),
    path('tableall', TemplateView.as_view(template_name='layouts/tableall.html'), name='tableall'),
    path('tablealls', AdminViews.TableAllsJsonView.as_view(), name='TableAllsJson'),    
    path('tableall_form', AdminViews.tableall_form,name="tableall_form"),
    path('tableall/<int:id>/', AdminViews.tableall_form,name="tableall_update"), # View Only Can't Edit/Add
    path('print', AdminViews.PrintView.as_view(), name='print'),
    # Server-Side bkk1
    path('bkk1_home', Bkk1Views.bkk1_home,name="bkk1_home"),
    path('bkk1', TemplateView.as_view(template_name='layouts/tableall.html'), name='bkk1'),
    path('bkk1s', Bkk1Views.Bkk1sJsonView.as_view(), name='Bkk1sJson'),
    # bkk1001
    path('bkk1001', Bkk1Views.MainViewBkk1001.as_view(), name='bkk1001'),
    path('api/Bkk1001s', Bkk1Views.Bkk1001sJsonView.as_view(), name='Bkk1001sJson'),
    path('bkk1001_form', Bkk1Views.bkk1001_form,name="bkk1001_form"),
    path('bkk1001/<int:id>/', Bkk1Views.bkk1001_form,name="bkk1001_update"),
    path('delete/bkk1001/<int:id>/', Bkk1Views.bkk1001_delete,name="bkk1001_delete"),
    # bkk1002
    path('bkk1002', Bkk1Views.MainViewBkk1002.as_view(), name='bkk1002'),
    path('api/Bkk1002s', Bkk1Views.Bkk1002sJsonView.as_view(), name='Bkk1002sJson'),
    path('bkk1002_form', Bkk1Views.bkk1002_form,name="bkk1002_form"),
    path('bkk1002/<int:id>/', Bkk1Views.bkk1002_form,name="bkk1002_update"),
    path('delete/bkk1002/<int:id>/', Bkk1Views.bkk1002_delete,name="bkk1002_delete"),
    # bkk1003
    path('bkk1003', Bkk1Views.MainViewBkk1003.as_view(), name='bkk1003'),
    path('api/Bkk1003s', Bkk1Views.Bkk1003sJsonView.as_view(), name='Bkk1003sJson'),
    path('bkk1003_form', Bkk1Views.bkk1003_form,name="bkk1003_form"),
    path('bkk1003/<int:id>/', Bkk1Views.bkk1003_form,name="bkk1003_update"),
    path('delete/bkk1003/<int:id>/', Bkk1Views.bkk1001_delete,name="bkk1003_delete"),    
    # Server-Side skw1
    path('skw1_home', Skw1Views.skw1_home,name="skw1_home"),
    path('skw1', TemplateView.as_view(template_name='layouts/tableall.html'), name='skw1'),
    path('skw1s', Skw1Views.Skw1sJsonView.as_view(), name='Skw1sJson'),
    # skw1001
    path('skw1001', Skw1Views.MainViewSkw1001.as_view(), name='skw1001'),
    path('api/Skw1001s', Skw1Views.Skw1001sJsonView.as_view(), name='Skw1001sJson'),
    path('skw1001_form', Skw1Views.skw1001_form,name="skw1001_form"),
    path('skw1001/<int:id>/', Skw1Views.skw1001_form,name="skw1001_update"),
    path('delete/skw1001/<int:id>/', Skw1Views.skw1001_delete,name="skw1001_delete"),
    # skw1002
    path('skw1002', Skw1Views.MainViewSkw1002.as_view(), name='skw1002'),
    path('api/Skw1002s', Skw1Views.Skw1002sJsonView.as_view(), name='Skw1002sJson'),
    path('skw1002_form', Skw1Views.skw1002_form,name="skw1002_form"),
    path('skw1002/<int:id>/', Skw1Views.skw1002_form,name="skw1002_update"),
    path('delete/skw1002/<int:id>/', Skw1Views.skw1002_delete,name="skw1002_delete"),
    # skw1003
    path('skw1003', Skw1Views.MainViewSkw1003.as_view(), name='skw1003'),
    path('api/Skw1003s', Skw1Views.Skw1003sJsonView.as_view(), name='Skw1003sJson'),
    path('skw1003_form', Skw1Views.skw1003_form,name="skw1003_form"),
    path('skw1003/<int:id>/', Skw1Views.skw1003_form,name="skw1003_update"),
    path('delete/skw1003/<int:id>/', Skw1Views.skw1003_delete,name="skw1003_delete"),

]
