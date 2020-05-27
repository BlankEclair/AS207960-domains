from django.conf import settings
from django.urls import path, include
from .views import domain, hosts, contacts

urlpatterns = [
    path('', domain.domains, name='domains'),
    path('prices/', domain.domain_prices, name='domain_prices'),
    path('domains/new/', domain.domain_search, name='domain_search'),
    path('domains/register/<str:domain_name>/', domain.domain_register, name='domain_register'),
    path('domains/transfer/', domain.domain_transfer_query, name='domain_transfer_query'),
    path('domains/transfer/<str:domain_name>/', domain.domain_transfer, name='domain_transfer'),
    path('domains/<uuid:domain_id>/', domain.domain, name='domain'),
    path('domains/<uuid:domain_id>/delete/', domain.delete_domain, name='delete_domain'),
    path('domains/<uuid:domain_id>/restore/', domain.restore_domain, name='restore_domain'),
    path('domains/<uuid:domain_id>/renew/', domain.renew_domain, name='renew_domain'),
    path('domains/<uuid:domain_id>/update_contact/', domain.update_domain_contact, name='update_domain_contact'),
    path('domains/<uuid:domain_id>/add_host_obj/', domain.add_domain_host_obj, name='add_domain_host_obj'),
    path('domains/<uuid:domain_id>/add_host_addr/', domain.add_domain_host_addr, name='add_domain_host_addr'),
    path('domains/<uuid:domain_id>/add_ds_data/', domain.add_domain_ds_data, name='add_domain_ds_data'),
    path('domains/<uuid:domain_id>/add_dnskey_data/', domain.add_domain_dnskey_data, name='add_domain_dnskey_data'),
    path('domains/<uuid:domain_id>/delete_ds_data/', domain.delete_domain_ds_data, name='delete_domain_ds_data'),
    path('domains/<uuid:domain_id>/delete_dnskey_data/', domain.delete_domain_dnskey_data, name='delete_domain_dnskey_data'),
    path('domains/<uuid:domain_id>/delete_sec_dns/', domain.delete_domain_sec_dns, name='delete_domain_sec_dns'),
    path('domains/<uuid:domain_id>/del_host_obj/<str:host_name>/', domain.delete_domain_host_obj, name='delete_domain_host_obj'),
    path('domains/<uuid:domain_id>/block_transfer/', domain.domain_block_transfer, name='domain_block_transfer'),
    path('domains/<uuid:domain_id>/del_block_transfer/', domain.domain_del_block_transfer, name='domain_del_block_transfer'),
    path('domains/<uuid:domain_id>/regen_transfer_code/', domain.domain_regen_transfer_code, name='domain_regen_transfer_code'),
    path('hosts/', hosts.hosts, name='hosts'),
    path('hosts/<uuid:host_id>/', hosts.host, name='host'),
    path('hosts/<uuid:host_id>/delete/', hosts.host_delete, name='host_delete'),
    path('hosts/<str:registry_name>/create/<str:host>/', hosts.host_create, name='host_create'),
    path('contacts/', contacts.contacts, name='contacts'),
    path('contacts/new/', contacts.new_contact, name='new_contact'),
    path('contacts/<uuid:contact_id>/', contacts.edit_contact, name='edit_contact'),
    path('contacts/<uuid:contact_id>/delete/', contacts.delete_contact, name='delete_contact'),
    path('addresses/', contacts.addresses, name='addresses'),
    path('addresses/new/', contacts.new_address, name='new_address'),
    path('addresses/<uuid:address_id>/delete/', contacts.delete_address, name='delete_address'),
    path('addresses/<uuid:address_id>/', contacts.edit_address, name='edit_address'),
]

if settings.DEBUG:
    urlpatterns.append(path('api/', include('domains.api.urls')))
