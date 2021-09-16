from django.shortcuts import render
from django.http import HttpResponse
from .models import LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion
import os
import csv

# HTML VIEWS #
def learn_acl_all(request):
    acl_list = LearnACL.objects.all()
    context = {'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_all.html', context)

def learn_acl_year_archive(request, year):
    acl_list = LearnACL.objects.filter(timestamp__year=year)
    context = {'year': year, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_year_archive.html', context)

def learn_acl_month_archive(request, year, month):
    acl_list = LearnACL.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_month_archive.html', context)

def learn_acl_day_archive(request, year, month, day):
    acl_list = LearnACL.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_day_archive.html', context)

def learn_acl_os_archive(request, os):
    acl_list = LearnACL.objects.filter(os=os)
    context = {'os': os, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_os_archive.html', context)

def learn_acl_alias_archive(request, os, pyats_alias):
    acl_list = LearnACL.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'acl_list': acl_list}
    return render(request, 'HTML/LearnACL/learn_acl_alias_archive.html', context)

def learn_arp_all(request):
    arp_list = LearnARP.objects.all()
    context = {'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_all.html', context)

def learn_arp_year_archive(request, year):
    arp_list = LearnARP.objects.filter(timestamp__year=year)
    context = {'year': year, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_year_archive.html', context)

def learn_arp_month_archive(request, year, month):
    arp_list = LearnARP.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_month_archive.html', context)

def learn_arp_day_archive(request, year, month, day):
    arp_list = LearnARP.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_day_archive.html', context)

def learn_arp_os_archive(request, os):
    arp_list = LearnARP.objects.filter(os=os)
    context = {'os': os, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_os_archive.html', context)

def learn_arp_alias_archive(request, os, pyats_alias):
    arp_list = LearnARP.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'arp_list': arp_list}
    return render(request, 'HTML/LearnARP/learn_arp_alias_archive.html', context)

def learn_arp_statistics_all(request):
    arp_statistics_list = LearnARPStatistics.objects.all()
    context = {'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_all.html', context)

def learn_arp_statistics_year_archive(request, year):
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp__year=year)
    context = {'year': year, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_year_archive.html', context)

def learn_arp_statistics_month_archive(request, year, month):
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_month_archive.html', context)

def learn_arp_statistics_day_archive(request, year, month, day):
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_day_archive.html', context)

def learn_arp_statistics_os_archive(request, os):
    arp_statistics_list = LearnARPStatistics.objects.filter(os=os)
    context = {'os': os, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_os_archive.html', context)

def learn_arp_statistics_alias_archive(request, os, pyats_alias):
    arp_statistics_list = LearnARPStatistics.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'arp_statistics_list': arp_statistics_list}
    return render(request, 'HTML/LearnARPStatistics/learn_arp_statistics_alias_archive.html', context)    

def learn_vlan_all(request):
    v_list = LearnVLAN.objects.all()
    context = {'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_all.html', context)

def learn_vlan_year_archive(request, year):
    v_list = LearnVLAN.objects.filter(timestamp__year=year)
    context = {'year': year, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_year_archive.html', context)

def learn_vlan_month_archive(request, year, month):
    v_list = LearnVLAN.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_month_archive.html', context)

def learn_vlan_day_archive(request, year, month, day):
    v_list = LearnVLAN.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_day_archive.html', context)

def learn_vlan_os_archive(request, os):
    v_list = LearnVLAN.objects.filter(os=os)
    context = {'os': os, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_os_archive.html', context)

def learn_vlan_alias_archive(request, os, pyats_alias):
    v_list = LearnVLAN.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'vlan_list': v_list}
    return render(request, 'HTML/LearnVLAN/learn_vlan_alias_archive.html', context)

def learn_vrf_all(request):
    v_list = LearnVRF.objects.all()
    context = {'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_all.html', context)

def learn_vrf_year_archive(request, year):
    v_list = LearnVRF.objects.filter(timestamp__year=year)
    context = {'year': year, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_year_archive.html', context)

def learn_vrf_month_archive(request, year, month):
    v_list = LearnVRF.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_month_archive.html', context)

def learn_vrf_day_archive(request, year, month, day):
    v_list = LearnVRF.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_day_archive.html', context)

def learn_vrf_os_archive(request, os):
    v_list = LearnVRF.objects.filter(os=os)
    context = {'os': os, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_os_archive.html', context)

def learn_vrf_alias_archive(request, os, pyats_alias):
    v_list = LearnVRF.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'vrf_list': v_list}
    return render(request, 'HTML/LearnVRF/learn_vrf_alias_archive.html', context)    

def show_inventory_all(request):
    inventory_list = ShowInventory.objects.all()
    context = {'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_all.html', context)

def show_inventory_year_archive(request, year):
    inventory_list = ShowInventory.objects.filter(timestamp__year=year)
    context = {'year': year, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_year_archive.html', context)

def show_inventory_month_archive(request, year, month):
    inventory_list = ShowInventory.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_month_archive.html', context)

def show_inventory_day_archive(request, year, month, day):
    inventory_list = ShowInventory.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_day_archive.html', context)

def show_inventory_os_archive(request, os):
    inventory_list = ShowInventory.objects.filter(os=os)
    context = {'os': os, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_os_archive.html', context)

def show_inventory_alias_archive(request, os, pyats_alias):
    inventory_list = ShowInventory.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'inventory_list': inventory_list}
    return render(request, 'HTML/ShowInventory/show_inventory_alias_archive.html', context)

def show_ip_int_brief_all(request):
    interface_list = ShowIPIntBrief.objects.all()
    context = {'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_all.html', context)

def show_ip_int_brief_year_archive(request, year):
    interface_list = ShowIPIntBrief.objects.filter(timestamp__year=year)
    context = {'year': year, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_year_archive.html', context)

def show_ip_int_brief_month_archive(request, year, month):
    interface_list = ShowIPIntBrief.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_month_archive.html', context)

def show_ip_int_brief_day_archive(request, year, month, day):
    interface_list = ShowIPIntBrief.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_day_archive.html', context)

def show_ip_int_brief_os_archive(request, os):
    interface_list = ShowIPIntBrief.objects.filter(os=os)
    context = {'os': os, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_os_archive.html', context)

def show_ip_int_brief_alias_archive(request, os, pyats_alias):
    interface_list = ShowIPIntBrief.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'interface_list': interface_list}
    return render(request, 'HTML/ShowIPInterfaceBrief/show_ip_int_brief_alias_archive.html', context)

def show_version_all(request):
    v_list = ShowVersion.objects.all()
    context = {'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_all.html', context)

def show_version_year_archive(request, year):
    v_list = ShowVersion.objects.filter(timestamp__year=year)
    context = {'year': year, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_year_archive.html', context)

def show_version_month_archive(request, year, month):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month)
    context = {'year': year, 'month': month, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_month_archive.html', context)

def show_version_day_archive(request, year, month, day):
    v_list = ShowVersion.objects.filter(timestamp__year=year,timestamp__month=month,timestamp__day=day)
    context = {'year': year, 'month': month, 'day': day, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_day_archive.html', context)

def show_version_os_archive(request, os):
    v_list = ShowVersion.objects.filter(os=os)
    context = {'os': os, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_os_archive.html', context)

def show_version_alias_archive(request, os, pyats_alias):
    v_list = ShowVersion.objects.filter(pyats_alias=pyats_alias, os=os)
    context = {'os': os, 'pyats_alias': pyats_alias, 'version_list': v_list}
    return render(request, 'HTML/ShowVersion/show_version_alias_archive.html', context)

# CSV VIEWS
def csv_page(request):
    return render(request, 'CSV/csv.html')    

def all_csv_download(request):
    return render(request, 'CSV/csv.html')  

def learn_acl_csv(request):
    return render(request, 'CSV/LearnACL/learn_acl_csv.html')

def learn_acl_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_acl_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Access Control List','Access Control Entry','Permission','Logging','Source Network','Destination Network','Layer 3 Protocol','Layer 4 Protocol','Operator','Port','Timestamp'])
    acls = LearnACL.objects.all().values_list('pyats_alias','acl', 'ace', 'permission', 'logging', 'source_network', 'destination_network', 'l3_protocol', 'l4_protocol', 'operator', 'port', 'timestamp')
    for acl in acls:
        writer.writerow(acl)
    return response

def learn_acl_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_acl_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Access Control List','Access Control Entry','Permission','Logging','Source Network','Destination Network','Layer 3 Protocol','Layer 4 Protocol','Operator','Port','Timestamp'])
    latest_timestamp = LearnACL.objects.latest('timestamp')
    acls = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','acl', 'ace', 'permission', 'logging', 'source_network', 'destination_network', 'l3_protocol', 'l4_protocol', 'operator', 'port', 'timestamp')
    for acl in acls:
        writer.writerow(acl)
    return response

def learn_arp_csv(request):
    return render(request, 'CSV/LearnARP/learn_arp_csv.html')

def learn_arp_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Neighbor IP','Neighbor MAC','Origin','Local Proxy','Proxy','Timestamp'])
    interfaces = LearnARP.objects.all().values_list('pyats_alias', 'interface', 'neighbor_ip', 'neighbor_mac', 'origin', 'local_proxy', 'proxy','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def learn_arp_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Neighbor IP','Neighbor MAC','Origin','Local Proxy','Proxy','Timestamp'])
    latest_timestamp = LearnARP.objects.latest('timestamp')
    interfaces = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias', 'interface', 'neighbor_ip', 'neighbor_mac', 'origin', 'local_proxy', 'proxy','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def learn_arp_statistics_csv(request):
    return render(request, 'CSV/LearnARP/learn_arp_csv.html')

def learn_arp_statistics_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_statistics_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Total Entries','Input Drops','Input Replies','Input Requests','Incomplete Requests','Output Replies','Output Requests','Timestamp'])
    statistics = LearnARPStatistics.objects.all().values_list('pyats_alias','entries_total','in_drops','in_replies_pkts','in_requests_pkts','incomplete_total','out_replies_pkts','out_requests_pkts','timestamp')
    for stat in statistics:
        writer.writerow(stat)
    return response

def learn_arp_statistics_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_arp_statistics_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Total Entries','Input Drops','Input Replies','Input Requests','Incomplete Requests','Output Replies','Output Requests','Timestamp'])
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    statistics = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','entries_total','in_drops','in_replies_pkts','in_requests_pkts','incomplete_total','out_replies_pkts','out_requests_pkts','timestamp')
    for stat in statistics:
        writer.writerow(statistics)
    return response

def learn_vlan_csv(request):
    return render(request, 'CSV/LearnVLAN/learn_vlan_csv.html')

def learn_vlan_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vlan_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VLAN','Interfaces','Mode','Name','Shutdown','State','Timestamp'])
    vlans = LearnVLAN.objects.all().values_list('pyats_alias','vlan','interfaces','mode','name','shutdown','state','timestamp')
    for vlan in vlans:
        writer.writerow(vlan)
    return response

def learn_vlan_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vlan_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VLAN','Interfaces','Mode','Name','Shutdown','State','Timestamp'])
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlans = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','vlan','interfaces','mode','name','shutdown','state','timestamp')
    for vlan in vlans:
        writer.writerow(vlan)
    return response

def learn_vrf_csv(request):
    return render(request, 'CSV/LearnVRF/learn_vrf_csv.html')    

def learn_vrf_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vrf_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VRF','Address Family IPv4','Address Family IPv6','Route Distinguisher','Timestamp'])
    vrfs = LearnVRF.objects.all().values_list('pyats_alias','vrf','address_family_ipv4','address_family_ipv6','route_distinguisher','timestamp')
    for vrf in vrfs:
        writer.writerow(vrf)
    return response

def learn_vrf_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="learn_vrf_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','VRF','Address Family IPv4','Address Family IPv6','Route Distinguisher','Timestamp'])
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrfs = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','vrf','address_family_ipv4','address_family_ipv6','route_distinguisher','timestamp')
    for vrf in vrfs:
        writer.writerow(vrf)
    return response

def show_inventory_csv(request):
    return render(request, 'CSV/ShowInventory/show_inventory_csv.html')    

def show_inventory_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_inventory_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Part','Description','Part ID','Serial Number','Timestamp'])
    inventory = ShowInventory.objects.all().values_list('pyats_alias','part','description','pid','serial_number','timestamp')
    for part in inventory:
        writer.writerow(part)
    return response

def show_inventory_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_inventory_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Part','Description','Part ID','Serial Number','Timestamp'])
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','part','description','pid','serial_number','timestamp')
    for part in inventory:
        writer.writerow(part)
    return response

def show_ip_int_brief_csv(request):
    return render(request, 'CSV/ShowIPInterfaceBrief/show_ip_int_brief.html')    

def show_ip_int_brief_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_ip_interface_brief_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Interface Status','IP Address','Timestamp'])
    interfaces = ShowIPIntBrief.objects.all().values_list('pyats_alias','interface','interface_status','ip_address','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def show_ip_int_brief_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_ip_interface_brief_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Interface','Interface Status','IP Address','Timestamp'])
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    interfaces = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','interface','interface_status','ip_address','timestamp')
    for interface in interfaces:
        writer.writerow(interface)
    return response

def show_version_csv(request):
    return render(request, 'CSV/ShowVersion/show_version_csv.html')    

def show_version_csv_download(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_version_all.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Bootflash','Chassis','CPU','Device Name','Memory','Model','Processor Board ID','RP','Slots','Days Up','Hours Up','Minutes Up','Seconds Up','Name','OS','Last Reload Reason','System Compile Time','Image File','Version','Chassis Serial Number','Compiled By','Current Config Register','Image ID','Label','License Leven','License Type','Non Volative Memory','Physical Memory','Next Reload License Level','Platform','Processor Type','Return to ROM by','Router Type','Uptime','Uptime this CP','Version (Short)','XE Version','Timestamp'])
    versions = ShowVersion.objects.all().values_list('pyats_alias','bootflash','chassis','cpu','device_name','memory','model','processor_board_id','rp','slots','days','hours','minutes','seconds','name','os','reason','system_compile_time','system_image_file','system_version','chassis_sn','compiled_by','curr_config_register','image_id','image_type','label','license_level','license_type','non_volatile','physical','next_reload_license_level','platform','processor_type','returned_to_rom_by','rom','rtr_type','uptime','uptime_this_cp','version_short','xe_version','timestamp')
    for version in versions:
        writer.writerow(version)
    return response

def show_version_csv_download_latest(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="show_version_latest.csv'
    writer = csv.writer(response)
    writer.writerow(['pyATS Alias','Bootflash','Chassis','CPU','Device Name','Memory','Model','Processor Board ID','RP','Slots','Days Up','Hours Up','Minutes Up','Seconds Up','Name','OS','Last Reload Reason','System Compile Time','Image File','Version','Chassis Serial Number','Compiled By','Current Config Register','Image ID','Label','License Leven','License Type','Non Volative Memory','Physical Memory','Next Reload License Level','Platform','Processor Type','Return to ROM by','Router Type','Uptime','Uptime this CP','Version (Short)','XE Version','Timestamp'])
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    versions = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp).values_list('pyats_alias','bootflash','chassis','cpu','device_name','memory','model','processor_board_id','rp','slots','days','hours','minutes','seconds','name','os','reason','system_compile_time','system_image_file','system_version','chassis_sn','compiled_by','curr_config_register','image_id','image_type','label','license_level','license_type','non_volatile','physical','next_reload_license_level','platform','processor_type','returned_to_rom_by','rom','rtr_type','uptime','uptime_this_cp','version_short','xe_version','timestamp')
    for version in versions:
        writer.writerow(version)
    return response

# On DEMAND VIEWS

def button(request):
    return render(request, 'OnDemand/ondemand.html')

def get_all_ondemand(request):
    os.system('pyats run job populate_db_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/get_all_result.html')

def learn_acl_ondemand(request):
    os.system('pyats run job learn_acl_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_acl_result.html')

def learn_arp_ondemand(request):
    os.system('pyats run job learn_arp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_arp_result.html')

def learn_bgp_ondemand(request):
    os.system('pyats run job learn_bgp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_bgp_result.html')

def learn_vlan_ondemand(request):
    os.system('pyats run job learn_vlan_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_vlan_result.html')

def learn_vrf_ondemand(request):
    os.system('pyats run job learn_vrf_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/learn_vrf_result.html')

def show_inventory_ondemand(request):
    os.system('pyats run job show_inventory_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/show_inventory_result.html')

def show_ip_int_brief_ondemand(request):
    os.system('pyats run job show_ip_int_brief_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/show_ip_int_brief_result.html')

def show_version_ondemand(request):
    os.system('pyats run job show_version_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    return render(request, 'OnDemand/show_version_result.html')

# Latest
def latest(request):
    return render(request, 'Latest/latest.html')

def all_latest(request):
    acl_latest_timestamp = LearnACL.objects.latest('timestamp')
    acl_list = LearnACL.objects.filter(timestamp=acl_latest_timestamp.timestamp)
    arp_latest_timestamp = LearnARP.objects.latest('timestamp')
    arp_list = LearnARP.objects.filter(timestamp=arp_latest_timestamp.timestamp)
    arp_statistics_latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp=arp_statistics_latest_timestamp.timestamp)
    bgp_latest_timestamp = LearnBGP.objects.latest('timestamp')
    bgp_list = LearnBGP.objects.filter(timestamp=bgp_latest_timestamp.timestamp)
    vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
    vlan_list = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp)
    vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
    vrf_list = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp)
    inventory_latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=inventory_latest_timestamp.timestamp)
    ip_int_brief_latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    ip_int_brief_list = ShowIPIntBrief.objects.filter(timestamp=ip_int_brief_latest_timestamp.timestamp)    
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    version_list = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp)       
    context = {'acl_list': acl_list, 'arp_list': arp_list, 'arp_statistics_list': arp_statistics_list, 'bgp_list': bgp_list, 'vlan_list': vlan_list,'vrf_list': vrf_list,'version_list': version_list,'ip_int_brief_list': ip_int_brief_list,'inventory_list': inventory_list}
    return render(request, 'Latest/All/all_latest.html', context)

def learn_acl_latest(request):
    latest_timestamp = LearnACL.objects.latest('timestamp')
    acl_list = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'acl_list': acl_list}
    return render(request, 'Latest/LearnACL/learn_acl_latest.html', context)

def learn_arp_latest(request):
    latest_timestamp = LearnARP.objects.latest('timestamp')
    arp_list = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'arp_list': arp_list}
    return render(request, 'Latest/LearnARP/learn_arp_latest.html', context)

def learn_arp_statistics_latest(request):
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    arp_statistics_list = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'arp_statistics_list': arp_statistics_list}
    return render(request, 'Latest/LearnARPStatistics/learn_arp_statistics_latest.html', context)    

def learn_bgp_latest(request):
    latest_timestamp = LearnBGP.objects.latest('timestamp')
    bgp_list = LearnBGP.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'bgp_list': bgp_list}
    return render(request, 'Latest/LearnBGP/learn_bgp_latest.html', context)

def learn_vlan_latest(request):
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    v_list = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'vlan_list': v_list}
    return render(request, 'Latest/LearnVLAN/learn_vlan_latest.html', context)

def learn_vrf_latest(request):
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    v_list = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'vrf_list': v_list}
    return render(request, 'Latest/LearnVRF/learn_vrf_latest.html', context)

def show_inventory_latest(request):
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    inventory_list = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'inventory_list': inventory_list}
    return render(request, 'Latest/ShowInventory/show_inventory_latest.html', context)

def show_ip_int_brief_latest(request):
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    interface_list = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'interface_list': interface_list}
    return render(request, 'Latest/ShowIPInterfaceBrief/show_ip_int_brief_latest.html', context)

def show_version_latest(request):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    v_list = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp)
    context = {'version_list': v_list}
    return render(request, 'Latest/ShowVersion/show_version_latest.html', context)

# Changes 

def changes(request):
    return render(request, 'Changes/changes.html')

def all_changes(request):
    acl_latest_timestamp = LearnACL.objects.latest('timestamp')
    current_acls = LearnACL.objects.filter(timestamp=acl_latest_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    arp_latest_timestamp = LearnARP.objects.latest('timestamp')
    current_arp = LearnARP.objects.filter(timestamp=arp_latest_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    arp_stats_latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    current_arp_statistics = LearnARPStatistics.objects.filter(timestamp=arp_stats_latest_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")    
    bgp_latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    current_bgp_instances = LearnBGPInstances.objects.filter(timestamp=bgp_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    bgp_route_latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    current_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_route_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    bgp_table_latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    current_bgp_table = LearnBGPTables.objects.filter(timestamp=bgp_table_latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')    
    vlan_latest_timestamp = LearnVLAN.objects.latest('timestamp')
    current_vlans = LearnVLAN.objects.filter(timestamp=vlan_latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vrf_latest_timestamp = LearnVRF.objects.latest('timestamp')
    current_vrfs = LearnVRF.objects.filter(timestamp=vrf_latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    version_latest_timestamp = ShowVersion.objects.latest('timestamp')
    current_version = ShowVersion.objects.filter(timestamp=version_latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    os.system('pyats run job populate_db_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    acl_new_timestamp = LearnACL.objects.latest('timestamp')
    latest_acls = LearnACL.objects.filter(timestamp=acl_new_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    arp_new_timestamp = LearnARP.objects.latest('timestamp')
    latest_arp = LearnARP.objects.filter(timestamp=arp_new_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    arp_stats_new_timestamp = LearnARPStatistics.objects.latest('timestamp')
    latest_arp_statistics = LearnARPStatistics.objects.filter(timestamp=arp_stats_new_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
    bgp_new_timestamp = LearnBGPInstances.objects.latest('timestamp')
    latest_bgp_instances = LearnBGPInstances.objects.filter(timestamp=bgp_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    bgp_route_new_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    latest_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=bgp_route_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    bgp_table_new_timestamp = LearnBGPTables.objects.latest('timestamp')
    latest_bgp_table = LearnBGPTables.objects.filter(timestamp=bgp_table_new_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')    
    vlan_new_timestamp = LearnVLAN.objects.latest('timestamp')
    latest_vlans = LearnVLAN.objects.filter(timestamp=vlan_new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vrf_new_timestamp = LearnVRF.objects.latest('timestamp')
    latest_vrfs = LearnVRF.objects.filter(timestamp=vrf_new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    version_new_timestamp = ShowVersion.objects.latest('timestamp')
    latest_version = ShowVersion.objects.filter(timestamp=version_new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")    
    acl_removals = current_acls.difference(latest_acls)
    acl_additions = latest_acls.difference(current_acls)
    arp_removals = current_arp.difference(latest_arp)
    arp_additions = latest_arp.difference(current_arp)
    arp_statistics_removals = current_arp_statistics.difference(latest_arp_statistics)
    arp_statistics_additions = latest_arp_statistics.difference(current_arp_statistics)
    bgp_removals = current_bgp.difference(latest_bgp)
    bgp_additions = latest_bgp.difference(current_bgp)
    bgp_route_removals = current_bgp_route.difference(latest_bgp_route)
    bgp_route_additions = latest_bgp_route.difference(current_bgp_route)
    bgp_table_removals = current_bgp_table.difference(latest_bgp_table)
    bgp_table_additions = latest_bgp_table.difference(current_bgp_table)
    vlan_removals = current_vlans.difference(latest_vlans)
    vlan_additions = latest_vlans.difference(current_vlans)
    vrf_removals = current_vrfs.difference(latest_vrfs)
    vrf_additions = latest_vrfs.difference(current_vrfs)
    version_removals = current_version.difference(latest_version)
    version_additions = latest_version.difference(current_version)       
    return render(request, 'Changes/all_changes.html', {'acl_removals': acl_removals,'acl_additions': acl_additions, 'arp_removals': arp_removals,'arp_additions': arp_additions, 'arp_statistics_removals': arp_statistics_removals,'arp_statistics_additions': arp_statistics_additions, 'bgp_instances_removals': bgp_instances_removals,'bgp_instances_additions': bgp_instances_additions, 'bgp_route_removals': bgp_route_removals,'bgp_route_additions': bgp_route_additions, 'vlan_removals': vlan_removals, 'vlan_additions': vlan_additions, 'vlan_latest_timestamp': vlan_latest_timestamp.timestamp, 'vlan_new_timestamp': vlan_new_timestamp.timestamp, 'vrf_removals': vrf_removals, 'vrf_additions': vrf_additions, 'vrf_latest_timestamp': vrf_latest_timestamp.timestamp, 'vrf_new_timestamp': vrf_new_timestamp.timestamp, 'version_removals': version_removals, 'version_additions': version_additions, 'version_latest_timestamp': version_latest_timestamp.timestamp, 'version_new_timestamp': version_new_timestamp.timestamp})

def learn_acl_changes(request):
    latest_timestamp = LearnACL.objects.latest('timestamp')
    current_acls = LearnACL.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    os.system('pyats run job learn_vlan_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnACL.objects.latest('timestamp')
    latest_acls = LearnACL.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "acl", "ace", "permission", "logging", "source_network", "destination_network", "l3_protocol", "l4_protocol", "operator", "port")
    acl_removals = current_acls.difference(latest_acls)
    acl_additions = latest_acls.difference(current_acls)
    return render(request, 'Changes/learn_acl_changes.html', {'acl_removals': acl_removals,'acl_additions': acl_additions})

def learn_arp_changes(request):
    latest_timestamp = LearnARP.objects.latest('timestamp')
    current_arp = LearnARP.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    os.system('pyats run job learn_arp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnARP.objects.latest('timestamp')
    latest_arp = LearnARP.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "interface", "neighbor_ip", "neighbor_mac", "origin", "local_proxy", "proxy")
    arp_removals = current_arp.difference(latest_arp)
    arp_additions = latest_arp.difference(current_arp)
    return render(request, 'Changes/learn_arp_changes.html', {'arp_removals': arp_removals,'arp_additions': arp_additions})

def learn_arp_statistics_changes(request):
    latest_timestamp = LearnARPStatistics.objects.latest('timestamp')
    current_arp_statistics = LearnARPStatistics.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
    os.system('pyats run job learn_arp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnARPStatistics.objects.latest('timestamp')
    latest_arp_statistics = LearnARPStatistics.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "entries_total", "in_drops", "incomplete_total")
    arp_statistics_removals = current_arp_statistics.difference(latest_arp_statistics)
    arp_statistics_additions = latest_arp_statistics.difference(current_arp_statistics)
    return render(request, 'Changes/learn_arp_statistics_changes.html', {'arp_statistics_removals': arp_statistics_removals,'arp_statistics_additions': arp_statistics_additions})

def learn_bgp_instances_changes(request):
    latest_timestamp = LearnBGPInstances.objects.latest('timestamp')
    current_bgp_instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    os.system('pyats run job learn_bgp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnBGPInstances.objects.latest('timestamp')
    latest_bgp_instances = LearnBGPInstances.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'last_reset', 'reset_reason')
    bgp_instances_removals = current_bgp_instances.difference(latest_bgp_instances)
    bgp_instances_additions = latest_bgp_instances.difference(current_bgp_instances)
    return render(request, 'Changes/learn_bgp_instances_changes.html', {'bgp_instances_removals': bgp_instances_removals,'bgp_instances_additions': bgp_instances_additions})

def learn_bgp_route_changes(request):
    latest_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    current_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    os.system('pyats run job learn_bgp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnBGPRoutesPerPeer.objects.latest('timestamp')
    latest_bgp_route = LearnBGPRoutesPerPeer.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as')
    bgp_route_removals = current_bgp_route.difference(latest_bgp_route)
    bgp_route_additions = latest_bgp_route.difference(current_bgp_route)
    return render(request, 'Changes/learn_bgp_route_changes.html', {'bgp_route_removals': bgp_route_removals,'bgp_route_additions': bgp_route_additions})

def learn_bgp_table_changes(request):
    latest_timestamp = LearnBGPTables.objects.latest('timestamp')
    current_bgp_table = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')
    os.system('pyats run job learn_bgp_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnBGPTables.objects.latest('timestamp')
    latest_bgp_table = LearnBGPTables.objects.filter(timestamp=latest_timestamp.timestamp).values('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight')
    bgp_table_removals = current_bgp_table.difference(latest_bgp_table)
    bgp_table_additions = latest_bgp_table.difference(current_bgp_table)
    return render(request, 'Changes/learn_bgp_table_changes.html', {'bgp_table_removals': bgp_table_removals,'bgp_table_additions': bgp_table_additions})

def learn_vlan_changes(request):
    latest_timestamp = LearnVLAN.objects.latest('timestamp')
    current_vlans = LearnVLAN.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    os.system('pyats run job learn_vlan_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnVLAN.objects.latest('timestamp')
    latest_vlans = LearnVLAN.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vlan", "interfaces", "mode", "name", "shutdown", "state")
    vlan_removals = current_vlans.difference(latest_vlans)
    vlan_additions = latest_vlans.difference(current_vlans)
    return render(request, 'Changes/learn_vlan_changes.html', {'vlan_removals': vlan_removals,'vlan_additions': vlan_additions})

def learn_vrf_changes(request):
    latest_timestamp = LearnVRF.objects.latest('timestamp')
    current_vrfs = LearnVRF.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    os.system('pyats run job learn_vrf_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = LearnVRF.objects.latest('timestamp')
    latest_vrfs = LearnVRF.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias", "os", "vrf", "address_family_ipv4", "address_family_ipv6", "route_distinguisher")
    vrf_removals = current_vrfs.difference(latest_vrfs)
    vrf_additions = latest_vrfs.difference(current_vrfs)
    return render(request, 'Changes/learn_vrf_changes.html', {'vrf_removals': vrf_removals,'vrf_additions': vrf_additions})

def show_inventory_changes(request):
    latest_timestamp = ShowInventory.objects.latest('timestamp')
    current_inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","part","description","pid","serial_number")
    os.system('pyats run job show_inventory_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = ShowInventory.objects.latest('timestamp')
    latest_inventory = ShowInventory.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","part","description","pid","serial_number")
    inventory_removals = current_inventory.difference(latest_inventory)
    inventory_additions = latest_inventory.difference(current_inventory)
    return render(request, 'Changes/show_inventory_changes.html', {'inventory_removals': inventory_removals,'inventory_additions': inventory_additions})

def show_ip_int_brief_changes(request):
    latest_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    current_interfaces = ShowIPIntBrief.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","os","interface","interface_status","ip_address")
    os.system('pyats run job show_ip_int_brief_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = ShowIPIntBrief.objects.latest('timestamp')
    latest_interfaces = ShowIPIntBrief.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","os","interface","interface_status","ip_address")
    interface_removals = current_interfaces.difference(latest_interfaces)
    interface_additions = latest_interfaces.difference(current_interfaces)
    return render(request, 'Changes/show_ip_int_brief_changes.html', {'interface_removals': interface_removals,'interface_additions': interface_additions})

def show_version_changes(request):
    latest_timestamp = ShowVersion.objects.latest('timestamp')
    current_version = ShowVersion.objects.filter(timestamp=latest_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    os.system('pyats run job learn_vrf_job.py --testbed-file testbed/testbed_DevNet_Nexus9k_Sandbox.yaml')
    new_timestamp = ShowVersion.objects.latest('timestamp')
    latest_version = ShowVersion.objects.filter(timestamp=new_timestamp.timestamp).values("pyats_alias","bootflash","chassis","cpu","device_name","memory","model","processor_board_id","rp","slots","name","os","reason","system_compile_time","system_image_file","system_version","chassis_sn","compiled_by","curr_config_register","image_id","image_type","label","license_level","license_type","non_volatile","physical","next_reload_license_level","platform","processor_type","returned_to_rom_by","rom","rtr_type","version_short","xe_version")
    version_removals = current_version.difference(latest_version)
    version_additions = latest_version.difference(current_version)
    return render(request, 'Changes/show_version_changes.html', {'version_removals': version_removals,'version_additions': version_additions})