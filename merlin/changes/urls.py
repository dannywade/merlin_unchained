from django.urls import path
from . import views
from .views import ChangesResultAll, ChangesResultEoX_PID, ChangesResultEoX_SN, ChangesResultEoX_SW, ChangesResultACL, ChangesResultARP, ChangesResultARPStatistics, ChangesResultBGPInstance, ChangesResultBGPRoute, ChangesResultBGPTable, ChangesResultConfig, ChangesResultInterface, ChangesResultPlatform, ChangesResultPlatformSlots, ChangesResultPlatformVirtual, ChangesResultVLAN, ChangesResultVRF, ChangesResultNMAP, ChangesResultPSIRT, ChangesResultRecommended, ChangesResultSerial2Contract, ChangesResultInventory, ChangesResultIPInterfaceBrief, ChangesResultVersion

urlpatterns = [
    path('Changes/', views.changes),
    path('Changes/all_changes/', views.all_changes, name="all_changes"),
    path('Changes/eox_pid_changes/', views.eox_pid_changes, name="eox_pid_changes"),
    path('Changes/eox_sn_changes/', views.eox_sn_changes, name="eox_sn_changes"),
    path('Changes/eox_sw_changes/', views.eox_sw_changes, name="eox_sw_changes"),
    path('Changes/learn_acl_changes/', views.learn_acl_changes, name="learn_acl_changes"),
    path('Changes/learn_arp_changes/', views.learn_arp_changes, name="learn_arp_changes"),
    path('Changes/learn_arp_statistics_changes/', views.learn_arp_statistics_changes, name="learn_arp_statistics_changes"),
    path('Changes/learn_bgp_instances_changes/', views.learn_bgp_instances_changes, name="learn_bgp_instances_changes"),
    path('Changes/learn_bgp_route_changes/', views.learn_bgp_route_changes, name="learn_bgp_route_changes"),
    path('Changes/learn_bgp_table_changes/', views.learn_bgp_table_changes, name="learn_bgp_table_changes"),
    path('Changes/learn_config_changes/', views.learn_config_changes, name="learn_config_changes"),
    path('Changes/learn_interface_changes/', views.learn_interface_changes, name="learn_interface_changes"),
    path('Changes/learn_platform_changes/', views.learn_platform_changes, name="learn_platform_changes"),
    path('Changes/learn_platform_slots_changes/', views.learn_platform_slots_changes, name="learn_platform_slots_changes"),
    path('Changes/learn_platform_virtual_changes/', views.learn_platform_virtual_changes, name="learn_platform_virtual_changes"),
    path('Changes/learn_vlan_changes/', views.learn_vlan_changes, name="learn_vlan_changes"),
    path('Changes/learn_vrf_changes/', views.learn_vrf_changes, name="learn_vrf_changes"),
    path('Changes/nmap_changes/', views.nmap_changes, name="nmap_changes"),
    path('Changes/psirt_changes/', views.psirt_changes, name="psirt_changes"),
    path('Changes/recommended_changes/', views.recommended_changes, name="recommended_changes"),
    path('Changes/serial2contract_changes/', views.serial2contract_changes, name="_changes"),
    path('Changes/show_inventory_changes/', views.show_inventory_changes, name="show_inventory_changes"),
    path('Changes/show_ip_int_brief_changes/', views.show_ip_int_brief_changes, name="show_ip_int_brief_changes"),
    path('Changes/show_version_changes/', views.show_version_changes, name="show_version_changes"),
    path('Changes/all_changes_filter/', ChangesResultAll.as_view(), name="get_all_changes_filter"),
    path('Changes/eox_pid_changes_filter/', ChangesResultEoX_PID.as_view(), name="eox_pid_changes_filter"),
    path('Changes/eox_sn_changes_filter/', ChangesResultEoX_SN.as_view(), name="eox_sn_changes_filter"),
    path('Changes/eox_sw_changes_filter/', ChangesResultEoX_SW.as_view(), name="eox_sw_changes_filter"),
    path('Changes/learn_acl_changes_filter/', ChangesResultACL.as_view(), name="learn_acl_changes_filter"),
    path('Changes/learn_arp_changes_filter/', ChangesResultARP.as_view(), name="learn_arp_changes_filter"),
    path('Changes/learn_arp_statistics_changes_filter/', ChangesResultARPStatistics.as_view(), name="learn_arp_statistics_changes_filter"),
    path('Changes/learn_bgp_instance_changes_filter/', ChangesResultBGPInstance.as_view(), name="learn_bgp_instance_changes_filter"),
    path('Changes/learn_bgp_route_changes_filter/', ChangesResultBGPRoute.as_view(), name="learn_bgp_route_changes_filter"),
    path('Changes/learn_bgp_table_changes_filter/', ChangesResultBGPTable.as_view(), name="learn_bgp_table_changes_filter"),
    path('Changes/learn_config_changes_filter/', ChangesResultConfig.as_view(), name="learn_config_changes_filter"),
    path('Changes/learn_interface_changes_filter/', ChangesResultInterface.as_view(), name="learn_interface_changes_filter"),
    path('Changes/learn_platform_changes_filter/', ChangesResultPlatform.as_view(), name="learn_platform_changes_filter"),
    path('Changes/learn_platform_slots_changes_filter/', ChangesResultPlatformSlots.as_view(), name="learn_platform_slots_changes_filter"),
    path('Changes/learn_platform_virtual_changes_filter/', ChangesResultPlatformVirtual.as_view(), name="learn_platform_virtual_changes_filter"),
    path('Changes/learn_vlan_changes_filter/', ChangesResultVLAN.as_view(), name="learn_vlan_changes_filter"),
    path('Changes/learn_vrf_changes_filter/', ChangesResultVRF.as_view(), name="learn_vrf_changes_filter"),
    path('Changes/nmap_changes_filter/', ChangesResultNMAP.as_view(), name="nmap_changes_filter"),
    path('Changes/psirt_changes_filter/', ChangesResultPSIRT.as_view(), name="psirt_changes_filter"),
    path('Changes/recommended_changes_filter/', ChangesResultRecommended.as_view(), name="recommended_changes_filter"),
    path('Changes/serial2contract_changes_filter/', ChangesResultSerial2Contract.as_view(), name="serial2contract_changes_filter"),
    path('Changes/show_inventory_changes_filter/', ChangesResultInventory.as_view(), name="show_inventory_changes_filter"),
    path('Changes/show_ip_int_brief_changes_filter/', ChangesResultIPInterfaceBrief.as_view(), name="show_ip_int_brief_changes_filter"),
    path('Changes/show_version_changes_filter/', ChangesResultVersion.as_view(), name="show_version_changes_filter"),
]