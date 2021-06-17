# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: domain_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='domain_common.proto',
  package='epp.domain',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x64omain_common.proto\x12\nepp.domain*\x86\x03\n\x0c\x44omainStatus\x12\x1a\n\x16\x43lientDeleteProhibited\x10\x00\x12\x0e\n\nClientHold\x10\x01\x12\x19\n\x15\x43lientRenewProhibited\x10\x02\x12\x1c\n\x18\x43lientTransferProhibited\x10\x03\x12\x1a\n\x16\x43lientUpdateProhibited\x10\x04\x12\x0c\n\x08Inactive\x10\x05\x12\x06\n\x02Ok\x10\x06\x12\x11\n\rPendingCreate\x10\x07\x12\x11\n\rPendingDelete\x10\x08\x12\x10\n\x0cPendingRenew\x10\t\x12\x13\n\x0fPendingTransfer\x10\n\x12\x11\n\rPendingUpdate\x10\x0b\x12\x1a\n\x16ServerDeleteProhibited\x10\x0c\x12\x0e\n\nServerHold\x10\r\x12\x19\n\x15ServerRenewProhibited\x10\x0e\x12\x1c\n\x18ServerTransferProhibited\x10\x0f\x12\x1a\n\x16ServerUpdateProhibited\x10\x10\x62\x06proto3'
)

_DOMAINSTATUS = _descriptor.EnumDescriptor(
  name='DomainStatus',
  full_name='epp.domain.DomainStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ClientDeleteProhibited', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ClientHold', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ClientRenewProhibited', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ClientTransferProhibited', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ClientUpdateProhibited', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Inactive', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Ok', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PendingCreate', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PendingDelete', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PendingRenew', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PendingTransfer', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PendingUpdate', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ServerDeleteProhibited', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ServerHold', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ServerRenewProhibited', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ServerTransferProhibited', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ServerUpdateProhibited', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=36,
  serialized_end=426,
)
_sym_db.RegisterEnumDescriptor(_DOMAINSTATUS)

DomainStatus = enum_type_wrapper.EnumTypeWrapper(_DOMAINSTATUS)
ClientDeleteProhibited = 0
ClientHold = 1
ClientRenewProhibited = 2
ClientTransferProhibited = 3
ClientUpdateProhibited = 4
Inactive = 5
Ok = 6
PendingCreate = 7
PendingDelete = 8
PendingRenew = 9
PendingTransfer = 10
PendingUpdate = 11
ServerDeleteProhibited = 12
ServerHold = 13
ServerRenewProhibited = 14
ServerTransferProhibited = 15
ServerUpdateProhibited = 16


DESCRIPTOR.enum_types_by_name['DomainStatus'] = _DOMAINSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
