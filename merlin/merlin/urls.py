"""merlin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('search.urls')),
    path('OnDemand/', views.button),
    path('OnDemand/get_all_result/', views.get_all_ondemand, name="get_all"),
    path('OnDemand/learn_acl_result/', views.learn_acl_ondemand, name="learn_acl"),
    path('OnDemand/learn_vlan_result/', views.learn_vlan_ondemand, name="learn_vlan"),
    path('OnDemand/learn_vrf_result/', views.learn_vrf_ondemand, name="learn_vrf"),
    path('OnDemand/show_inventory_result/', views.show_inventory_ondemand, name="show_inventory"),
    path('OnDemand/show_ip_int_brief_result/', views.show_ip_int_brief_ondemand, name="show_ip_int_brief"),
    path('OnDemand/show_version_result/', views.show_version_ondemand, name="show_version"),
    path('Changes/', views.changes),
    path('Changes/all_changes/', views.all_changes, name="all_changes"),
    path('Changes/learn_acl_changes/', views.learn_acl_changes, name="learn_acl_changes"),
    path('Changes/learn_vlan_changes/', views.learn_vlan_changes, name="learn_vlan_changes"),
    path('Changes/learn_vrf_changes/', views.learn_vrf_changes, name="learn_vrf_changes"),
    path('Changes/show_inventory_changes/', views.show_inventory_changes, name="show_inventory_changes"),
    path('Changes/show_ip_int_brief_changes/', views.show_ip_int_brief_changes, name="show_ip_int_brief_changes"),
    path('Changes/show_version_changes/', views.show_version_changes, name="show_version_changes"),
    path('API/', include('merlin_api.urls')),
    path('Latest/', views.latest),
    path('Latest/All/', views.all_latest),
    path('Latest/LearnVLAN/', views.learn_vlan_latest),
    path('Latest/LearnVRF/', views.learn_vrf_latest),
    path('Latest/ShowInventory/', views.show_inventory_latest),
    path('Latest/ShowIPInterfaceBrief/', views.show_ip_int_brief_latest),
    path('Latest/ShowVersion/', views.show_version_latest),
    path('CSV/', views.csv_page),
    path('CSV/download', views.learn_vlan_csv_download, name='learn_vlan_csv'),
    path('CSV/download', views.learn_vrf_csv_download, name='learn_vrf_csv'),
    path('CSV/download', views.show_inventory_csv_download, name='show_inventory_csv'),
    path('CSV/download', views.show_ip_int_brief_csv_download, name='show_ip_int_brief_csv'),
    path('CSV/download', views.show_version_csv_download, name='show_version_csv'),
    path('CSV/latest', views.learn_vlan_csv_download_latest, name='learn_vlan_csv_latest'),
    path('CSV/LearnVLAN/', views.learn_vlan_csv),
    path('CSV/LearnVLAN/download', views.learn_vlan_csv_download, name='learn_vlan_csv'),
    path('CSV/LearnVLAN/latest', views.learn_vlan_csv_download_latest, name='learn_vlan_csv_latest'),
    path('CSV/LearnVRF/', views.learn_vrf_csv),
    path('CSV/LearnVRF/download', views.learn_vrf_csv_download, name='learn_vrf_csv'),
    path('CSV/LearnVRF/latest', views.learn_vrf_csv_download_latest, name='learn_vrf_csv_latest'),
    path('CSV/ShowInventory/', views.show_inventory_csv),
    path('CSV/ShowInventory/download', views.show_inventory_csv_download, name='show_inventory_csv'),
    path('CSV/ShowInventory/latest', views.show_inventory_csv_download_latest, name='show_inventory_csv_latest'),
    path('CSV/ShowIPInterfaceBrief/', views.show_ip_int_brief_csv),
    path('CSV/ShowIPInterfaceBrief/download', views.show_ip_int_brief_csv_download, name='show_ip_int_brief_csv'),
    path('CSV/ShowIPInterfaceBrief/latest', views.show_ip_int_brief_csv_download_latest, name='show_ip_int_brief_csv_latest'),
    path('CSV/ShowVersion/', views.show_version_csv),
    path('CSV/ShowVersion/download', views.show_version_csv_download, name='show_version_csv'),
    path('CSV/ShowVersion/latest', views.show_version_csv_download_latest, name='show_version_csv_latest'),
    path('LearnVLAN/<int:year>/', views.learn_vlan_year_archive),
    path('LearnVLAN/<int:year>/<int:month>/', views.learn_vlan_month_archive),
    path('LearnVLAN/<int:year>/<int:month>/<int:day>/', views.learn_vlan_day_archive),
    path('LearnVLAN/<str:os>/', views.learn_vlan_os_archive),
    path('LearnVLAN/<str:os>/<str:pyats_alias>/', views.learn_vlan_alias_archive),
    path('LearnVRF/<int:year>/', views.learn_vrf_year_archive),
    path('LearnVRF/<int:year>/<int:month>/', views.learn_vrf_month_archive),
    path('LearnVRF/<int:year>/<int:month>/<int:day>/', views.learn_vrf_day_archive),
    path('LearnVRF/<str:os>/', views.learn_vrf_os_archive),
    path('LearnVRF/<str:os>/<str:pyats_alias>/', views.learn_vrf_alias_archive),
    path('ShowInventory/<int:year>/', views.show_inventory_year_archive),
    path('ShowInventory/<int:year>/<int:month>/', views.show_inventory_month_archive),
    path('ShowInventory/<int:year>/<int:month>/<int:day>/', views.show_inventory_day_archive),
    path('ShowInventory/<str:os>/', views.show_inventory_os_archive),
    path('ShowInventory/<str:os>/<str:pyats_alias>/', views.show_inventory_alias_archive),
    path('ShowIPInterfaceBrief/<int:year>/', views.show_ip_int_brief_year_archive),
    path('ShowIPInterfaceBrief/<int:year>/<int:month>/', views.show_ip_int_brief_month_archive),
    path('ShowIPInterfaceBrief/<int:year>/<int:month>/<int:day>/', views.show_ip_int_brief_day_archive),
    path('ShowIPInterfaceBrief/<str:os>/', views.show_ip_int_brief_os_archive),
    path('ShowIPInterfaceBrief/<str:os>/<str:pyats_alias>/', views.show_ip_int_brief_alias_archive),    
    path('ShowVersion/<int:year>/', views.show_version_year_archive),
    path('ShowVersion/<int:year>/<int:month>/', views.show_version_month_archive),
    path('ShowVersion/<int:year>/<int:month>/<int:day>/', views.show_version_day_archive),
    path('ShowVersion/<str:os>/', views.show_version_os_archive),
    path('ShowVersion/<str:os>/<str:pyats_alias>/', views.show_version_alias_archive),
]