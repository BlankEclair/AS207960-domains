# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='billing.proto',
  package='billing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rbilling.proto\x12\x07\x62illing\x1a\x1egoogle/protobuf/wrappers.proto\"\x8b\x01\n\x0e\x42illingRequest\x12;\n\x10\x63onvert_currency\x18\x01 \x01(\x0b\x32\x1f.billing.ConvertCurrencyRequestH\x00\x12\x31\n\x0b\x63harge_user\x18\x02 \x01(\x0b\x32\x1a.billing.ChargeUserRequestH\x00\x42\t\n\x07message\"\xee\x01\n\x16\x43onvertCurrencyRequest\x12\x15\n\rfrom_currency\x18\x01 \x01(\t\x12\x13\n\x0bto_currency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12.\n\x08username\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tremote_ip\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x63ountry_selection\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"h\n\x17\x43onvertCurrencyResponse\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\x12\x16\n\x0e\x61mount_inc_vat\x18\x01 \x01(\x03\x12\x0f\n\x07taxable\x18\x02 \x01(\x08\x12\x14\n\x0cused_country\x18\x04 \x01(\t\"\xe2\x01\n\x11\x43hargeUserRequest\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x03\x12\n\n\x02id\x18\x02 \x01(\t\x12\x12\n\ndescriptor\x18\x03 \x01(\t\x12\x12\n\ncan_reject\x18\x04 \x01(\x08\x12\x13\n\x0boff_session\x18\x05 \x01(\x08\x12\x0f\n\x07user_id\x18\x06 \x01(\t\x12\x30\n\nreturn_uri\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bnotif_queue\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xcf\x01\n\x12\x43hargeUserResponse\x12\x17\n\x0f\x63harge_state_id\x18\x01 \x01(\t\x12\x38\n\x06result\x18\x02 \x01(\x0e\x32(.billing.ChargeUserResponse.ChargeResult\x12\x11\n\x07message\x18\x03 \x01(\tH\x00\x12\x16\n\x0credirect_uri\x18\x04 \x01(\tH\x00\"3\n\x0c\x43hargeResult\x12\x0b\n\x07SUCCESS\x10\x00\x12\x08\n\x04\x46\x41IL\x10\x01\x12\x0c\n\x08REDIRECT\x10\x02\x42\x06\n\x04\x64\x61ta\"\x80\x02\n\x17\x43hargeStateNotification\x12\x11\n\tcharge_id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\t\x12;\n\x05state\x18\x03 \x01(\x0e\x32,.billing.ChargeStateNotification.ChargeState\x12\x30\n\nlast_error\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"R\n\x0b\x43hargeState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nPROCESSING\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\r\n\tCOMPLETED\x10\x04\"\xcf\x01\n\x18SubscriptionNotification\x12\x17\n\x0fsubscription_id\x18\x01 \x01(\t\x12\x42\n\x05state\x18\x02 \x01(\x0e\x32\x33.billing.SubscriptionNotification.SubscriptionState\"V\n\x11SubscriptionState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0c\n\x08PAST_DUE\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x12\r\n\tCANCELLED\x10\x04\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])



_CHARGEUSERRESPONSE_CHARGERESULT = _descriptor.EnumDescriptor(
  name='ChargeResult',
  full_name='billing.ChargeUserResponse.ChargeResult',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REDIRECT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=925,
  serialized_end=976,
)
_sym_db.RegisterEnumDescriptor(_CHARGEUSERRESPONSE_CHARGERESULT)

_CHARGESTATENOTIFICATION_CHARGESTATE = _descriptor.EnumDescriptor(
  name='ChargeState',
  full_name='billing.ChargeStateNotification.ChargeState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1161,
  serialized_end=1243,
)
_sym_db.RegisterEnumDescriptor(_CHARGESTATENOTIFICATION_CHARGESTATE)

_SUBSCRIPTIONNOTIFICATION_SUBSCRIPTIONSTATE = _descriptor.EnumDescriptor(
  name='SubscriptionState',
  full_name='billing.SubscriptionNotification.SubscriptionState',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAST_DUE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CANCELLED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1367,
  serialized_end=1453,
)
_sym_db.RegisterEnumDescriptor(_SUBSCRIPTIONNOTIFICATION_SUBSCRIPTIONSTATE)


_BILLINGREQUEST = _descriptor.Descriptor(
  name='BillingRequest',
  full_name='billing.BillingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='convert_currency', full_name='billing.BillingRequest.convert_currency', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='charge_user', full_name='billing.BillingRequest.charge_user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='message', full_name='billing.BillingRequest.message',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=59,
  serialized_end=198,
)


_CONVERTCURRENCYREQUEST = _descriptor.Descriptor(
  name='ConvertCurrencyRequest',
  full_name='billing.ConvertCurrencyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_currency', full_name='billing.ConvertCurrencyRequest.from_currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='to_currency', full_name='billing.ConvertCurrencyRequest.to_currency', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount', full_name='billing.ConvertCurrencyRequest.amount', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='billing.ConvertCurrencyRequest.username', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='remote_ip', full_name='billing.ConvertCurrencyRequest.remote_ip', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='country_selection', full_name='billing.ConvertCurrencyRequest.country_selection', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=201,
  serialized_end=439,
)


_CONVERTCURRENCYRESPONSE = _descriptor.Descriptor(
  name='ConvertCurrencyResponse',
  full_name='billing.ConvertCurrencyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='billing.ConvertCurrencyResponse.amount', index=0,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount_inc_vat', full_name='billing.ConvertCurrencyResponse.amount_inc_vat', index=1,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='taxable', full_name='billing.ConvertCurrencyResponse.taxable', index=2,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='used_country', full_name='billing.ConvertCurrencyResponse.used_country', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=545,
)


_CHARGEUSERREQUEST = _descriptor.Descriptor(
  name='ChargeUserRequest',
  full_name='billing.ChargeUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='billing.ChargeUserRequest.amount', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='billing.ChargeUserRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='billing.ChargeUserRequest.descriptor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='can_reject', full_name='billing.ChargeUserRequest.can_reject', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='off_session', full_name='billing.ChargeUserRequest.off_session', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='billing.ChargeUserRequest.user_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='return_uri', full_name='billing.ChargeUserRequest.return_uri', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='notif_queue', full_name='billing.ChargeUserRequest.notif_queue', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=774,
)


_CHARGEUSERRESPONSE = _descriptor.Descriptor(
  name='ChargeUserResponse',
  full_name='billing.ChargeUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='charge_state_id', full_name='billing.ChargeUserResponse.charge_state_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='billing.ChargeUserResponse.result', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='billing.ChargeUserResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redirect_uri', full_name='billing.ChargeUserResponse.redirect_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHARGEUSERRESPONSE_CHARGERESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='billing.ChargeUserResponse.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=777,
  serialized_end=984,
)


_CHARGESTATENOTIFICATION = _descriptor.Descriptor(
  name='ChargeStateNotification',
  full_name='billing.ChargeStateNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='charge_id', full_name='billing.ChargeStateNotification.charge_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='account', full_name='billing.ChargeStateNotification.account', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='billing.ChargeStateNotification.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_error', full_name='billing.ChargeStateNotification.last_error', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHARGESTATENOTIFICATION_CHARGESTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=987,
  serialized_end=1243,
)


_SUBSCRIPTIONNOTIFICATION = _descriptor.Descriptor(
  name='SubscriptionNotification',
  full_name='billing.SubscriptionNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='subscription_id', full_name='billing.SubscriptionNotification.subscription_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='billing.SubscriptionNotification.state', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SUBSCRIPTIONNOTIFICATION_SUBSCRIPTIONSTATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1246,
  serialized_end=1453,
)

_BILLINGREQUEST.fields_by_name['convert_currency'].message_type = _CONVERTCURRENCYREQUEST
_BILLINGREQUEST.fields_by_name['charge_user'].message_type = _CHARGEUSERREQUEST
_BILLINGREQUEST.oneofs_by_name['message'].fields.append(
  _BILLINGREQUEST.fields_by_name['convert_currency'])
_BILLINGREQUEST.fields_by_name['convert_currency'].containing_oneof = _BILLINGREQUEST.oneofs_by_name['message']
_BILLINGREQUEST.oneofs_by_name['message'].fields.append(
  _BILLINGREQUEST.fields_by_name['charge_user'])
_BILLINGREQUEST.fields_by_name['charge_user'].containing_oneof = _BILLINGREQUEST.oneofs_by_name['message']
_CONVERTCURRENCYREQUEST.fields_by_name['username'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CONVERTCURRENCYREQUEST.fields_by_name['remote_ip'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CONVERTCURRENCYREQUEST.fields_by_name['country_selection'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CHARGEUSERREQUEST.fields_by_name['return_uri'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CHARGEUSERREQUEST.fields_by_name['notif_queue'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CHARGEUSERRESPONSE.fields_by_name['result'].enum_type = _CHARGEUSERRESPONSE_CHARGERESULT
_CHARGEUSERRESPONSE_CHARGERESULT.containing_type = _CHARGEUSERRESPONSE
_CHARGEUSERRESPONSE.oneofs_by_name['data'].fields.append(
  _CHARGEUSERRESPONSE.fields_by_name['message'])
_CHARGEUSERRESPONSE.fields_by_name['message'].containing_oneof = _CHARGEUSERRESPONSE.oneofs_by_name['data']
_CHARGEUSERRESPONSE.oneofs_by_name['data'].fields.append(
  _CHARGEUSERRESPONSE.fields_by_name['redirect_uri'])
_CHARGEUSERRESPONSE.fields_by_name['redirect_uri'].containing_oneof = _CHARGEUSERRESPONSE.oneofs_by_name['data']
_CHARGESTATENOTIFICATION.fields_by_name['state'].enum_type = _CHARGESTATENOTIFICATION_CHARGESTATE
_CHARGESTATENOTIFICATION.fields_by_name['last_error'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_CHARGESTATENOTIFICATION_CHARGESTATE.containing_type = _CHARGESTATENOTIFICATION
_SUBSCRIPTIONNOTIFICATION.fields_by_name['state'].enum_type = _SUBSCRIPTIONNOTIFICATION_SUBSCRIPTIONSTATE
_SUBSCRIPTIONNOTIFICATION_SUBSCRIPTIONSTATE.containing_type = _SUBSCRIPTIONNOTIFICATION
DESCRIPTOR.message_types_by_name['BillingRequest'] = _BILLINGREQUEST
DESCRIPTOR.message_types_by_name['ConvertCurrencyRequest'] = _CONVERTCURRENCYREQUEST
DESCRIPTOR.message_types_by_name['ConvertCurrencyResponse'] = _CONVERTCURRENCYRESPONSE
DESCRIPTOR.message_types_by_name['ChargeUserRequest'] = _CHARGEUSERREQUEST
DESCRIPTOR.message_types_by_name['ChargeUserResponse'] = _CHARGEUSERRESPONSE
DESCRIPTOR.message_types_by_name['ChargeStateNotification'] = _CHARGESTATENOTIFICATION
DESCRIPTOR.message_types_by_name['SubscriptionNotification'] = _SUBSCRIPTIONNOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BillingRequest = _reflection.GeneratedProtocolMessageType('BillingRequest', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGREQUEST,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.BillingRequest)
  })
_sym_db.RegisterMessage(BillingRequest)

ConvertCurrencyRequest = _reflection.GeneratedProtocolMessageType('ConvertCurrencyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONVERTCURRENCYREQUEST,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.ConvertCurrencyRequest)
  })
_sym_db.RegisterMessage(ConvertCurrencyRequest)

ConvertCurrencyResponse = _reflection.GeneratedProtocolMessageType('ConvertCurrencyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONVERTCURRENCYRESPONSE,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.ConvertCurrencyResponse)
  })
_sym_db.RegisterMessage(ConvertCurrencyResponse)

ChargeUserRequest = _reflection.GeneratedProtocolMessageType('ChargeUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CHARGEUSERREQUEST,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.ChargeUserRequest)
  })
_sym_db.RegisterMessage(ChargeUserRequest)

ChargeUserResponse = _reflection.GeneratedProtocolMessageType('ChargeUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHARGEUSERRESPONSE,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.ChargeUserResponse)
  })
_sym_db.RegisterMessage(ChargeUserResponse)

ChargeStateNotification = _reflection.GeneratedProtocolMessageType('ChargeStateNotification', (_message.Message,), {
  'DESCRIPTOR' : _CHARGESTATENOTIFICATION,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.ChargeStateNotification)
  })
_sym_db.RegisterMessage(ChargeStateNotification)

SubscriptionNotification = _reflection.GeneratedProtocolMessageType('SubscriptionNotification', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIPTIONNOTIFICATION,
  '__module__' : 'billing_pb2'
  # @@protoc_insertion_point(class_scope:billing.SubscriptionNotification)
  })
_sym_db.RegisterMessage(SubscriptionNotification)


# @@protoc_insertion_point(module_scope)
