"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___DomainStatus = DomainStatus
class _DomainStatus(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DomainStatus.V], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    ClientDeleteProhibited = DomainStatus.V(0)
    ClientHold = DomainStatus.V(1)
    ClientRenewProhibited = DomainStatus.V(2)
    ClientTransferProhibited = DomainStatus.V(3)
    ClientUpdateProhibited = DomainStatus.V(4)
    Inactive = DomainStatus.V(5)
    Ok = DomainStatus.V(6)
    PendingCreate = DomainStatus.V(7)
    PendingDelete = DomainStatus.V(8)
    PendingRenew = DomainStatus.V(9)
    PendingTransfer = DomainStatus.V(10)
    PendingUpdate = DomainStatus.V(11)
    ServerDeleteProhibited = DomainStatus.V(12)
    ServerHold = DomainStatus.V(13)
    ServerRenewProhibited = DomainStatus.V(14)
    ServerTransferProhibited = DomainStatus.V(15)
    ServerUpdateProhibited = DomainStatus.V(16)
class DomainStatus(metaclass=_DomainStatus):
    V = typing.NewType('V', builtins.int)
ClientDeleteProhibited = DomainStatus.V(0)
ClientHold = DomainStatus.V(1)
ClientRenewProhibited = DomainStatus.V(2)
ClientTransferProhibited = DomainStatus.V(3)
ClientUpdateProhibited = DomainStatus.V(4)
Inactive = DomainStatus.V(5)
Ok = DomainStatus.V(6)
PendingCreate = DomainStatus.V(7)
PendingDelete = DomainStatus.V(8)
PendingRenew = DomainStatus.V(9)
PendingTransfer = DomainStatus.V(10)
PendingUpdate = DomainStatus.V(11)
ServerDeleteProhibited = DomainStatus.V(12)
ServerHold = DomainStatus.V(13)
ServerRenewProhibited = DomainStatus.V(14)
ServerTransferProhibited = DomainStatus.V(15)
ServerUpdateProhibited = DomainStatus.V(16)
