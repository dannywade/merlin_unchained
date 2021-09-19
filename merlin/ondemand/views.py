from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.db.models import Q
from merlin.models import Devices
import os

# On DEMAND VIEWS
def button(request):
    return render(request, 'OnDemand/ondemand.html')

def get_all_all_ondemand(request):
    os.system('pyats run job populate_db_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_acl_all_ondemand(request):
    os.system('pyats run job learn_acl_all_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_arp_all_ondemand(request):
    os.system('pyats run job learn_arp_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_bgp_all_ondemand(request):
    os.system('pyats run job learn_bgp_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_vlan_all_ondemand(request):
    os.system('pyats run job learn_vlan_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def learn_vrf_all_ondemand(request):
    os.system('pyats run job learn_vrf_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def show_inventory_all_ondemand(request):
    os.system('pyats run job show_inventory_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def show_ip_int_brief_all_ondemand(request):
    os.system('pyats run job show_ip_int_brief_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

def show_version_all_ondemand(request):
    os.system('pyats run job show_version_job.py')
    return render(request, 'OnDemand/ondemand_result.html')

class OnDemandResult(ListView):
    template_name = 'OnDemand/ondemand_result.html'    