from django.conf import settings
from django.urls import path, include
from .views import domain, hosts, contacts, admin, gchat_bot

urlpatterns = [
    path('', domain.index, name='index'),
    path('prices/', domain.domain_prices, name='domain_prices'),
    path('prices/query/', domain.domain_price_query, name='domain_price_query'),
    path('domains/', domain.domains, name='domains'),
    path('domains/new/', domain.domain_search, name='domain_search'),
    path('domains/new/<str:domain_name>/success/', domain.domain_search_success, name='domain_search_success'),
    path('domains/register/<str:domain_name>/', domain.domain_register, name='domain_register'),
    path('domains/transfer/', domain.domain_transfer_query, name='domain_transfer_query'),
    path('domains/transfer/<str:domain_name>/', domain.domain_transfer, name='domain_transfer'),
    path('domains/register_confirm/<uuid:order_id>/', domain.domain_register_confirm, name='domain_register_confirm'),
    path('domains/transfer_confirm/<uuid:order_id>/', domain.domain_transfer_confirm, name='domain_transfer_confirm'),
    path('domains/restore_confirm/<uuid:order_id>/', domain.restore_domain_confirm, name='restore_domain_confirm'),
    path('domains/renew_confirm/<uuid:order_id>', domain.renew_domain_confirm, name='renew_domain_confirm'),
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
    path('hosts/create/<str:host_name>/', hosts.host_create, name='host_create'),
    path('contacts/', contacts.contacts, name='contacts'),
    path('contacts/setup/', contacts.setup_contacts, name='setup_contacts'),
    path('contacts/new/', contacts.new_contact, name='new_contact'),
    path('contacts/<uuid:contact_id>/', contacts.edit_contact, name='edit_contact'),
    path('contacts/<uuid:contact_id>/delete/', contacts.delete_contact, name='delete_contact'),
    path('addresses/', contacts.addresses, name='addresses'),
    path('addresses/new/', contacts.new_address, name='new_address'),
    path('addresses/<uuid:address_id>/delete/', contacts.delete_address, name='delete_address'),
    path('addresses/<uuid:address_id>/', contacts.edit_address, name='edit_address'),
    path('api/', include('domains.api.urls')),
    path('gchat_bot/webhook/', gchat_bot.webhook),
    path('gchat_bot/link/<uuid:state_id>', gchat_bot.link_account, name='gchat_account_link'),
    path('epp_client/', admin.index, name='admin_index'),
    path('epp_client/domain_info/', admin.domain_info, name='admin_domain_info'),
    path('epp_client/contact_info/', admin.contact_info, name='admin_contact_info'),
    path('epp_client/contact_get_id/', admin.get_contact_id, name='admin_get_contact_id'),
    path('epp_client/domain_transfer_info/', admin.domain_transfer_info, name='admin_domain_transfer_info'),
    path('epp_client/domain_transfer_request/', admin.domain_transfer_request, name='admin_domain_transfer_request'),
    path('epp_client/balance/<str:registry_name>/', admin.balance, name='admin_balance'),
    path('epp_client/nominet_tags/', admin.nominet_tags, name='admin_nominet_tags'),
]
