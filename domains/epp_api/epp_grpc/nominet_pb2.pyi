"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import common_pb2
import contact_pb2
import domain_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class HandshakeAcceptRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REGISTRY_NAME_FIELD_NUMBER: builtins.int
    CASE_ID_FIELD_NUMBER: builtins.int
    REGISTRANT_FIELD_NUMBER: builtins.int
    registry_name: typing.Text = ...
    case_id: typing.Text = ...

    @property
    def registrant(self) -> google.protobuf.wrappers_pb2.StringValue: ...

    def __init__(self,
        *,
        registry_name : typing.Text = ...,
        case_id : typing.Text = ...,
        registrant : typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"registrant",b"registrant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"case_id",b"case_id",u"registrant",b"registrant",u"registry_name",b"registry_name"]) -> None: ...
global___HandshakeAcceptRequest = HandshakeAcceptRequest

class HandshakeRejectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REGISTRY_NAME_FIELD_NUMBER: builtins.int
    CASE_ID_FIELD_NUMBER: builtins.int
    registry_name: typing.Text = ...
    case_id: typing.Text = ...

    def __init__(self,
        *,
        registry_name : typing.Text = ...,
        case_id : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"case_id",b"case_id",u"registry_name",b"registry_name"]) -> None: ...
global___HandshakeRejectRequest = HandshakeRejectRequest

class HandshakeReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CASE_ID_FIELD_NUMBER: builtins.int
    DOMAINS_FIELD_NUMBER: builtins.int
    CMD_RESP_FIELD_NUMBER: builtins.int
    case_id: typing.Text = ...
    domains: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    @property
    def cmd_resp(self) -> common_pb2.CommandResponse: ...

    def __init__(self,
        *,
        case_id : typing.Text = ...,
        domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        cmd_resp : typing.Optional[common_pb2.CommandResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cmd_resp",b"cmd_resp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"case_id",b"case_id",u"cmd_resp",b"cmd_resp",u"domains",b"domains"]) -> None: ...
global___HandshakeReply = HandshakeReply

class ReleaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REGISTRY_NAME_FIELD_NUMBER: builtins.int
    REGISTRAR_TAG_FIELD_NUMBER: builtins.int
    DOMAIN_FIELD_NUMBER: builtins.int
    REGISTRANT_FIELD_NUMBER: builtins.int
    registry_name: typing.Text = ...
    registrar_tag: typing.Text = ...
    domain: typing.Text = ...
    registrant: typing.Text = ...

    def __init__(self,
        *,
        registry_name : typing.Text = ...,
        registrar_tag : typing.Text = ...,
        domain : typing.Text = ...,
        registrant : typing.Text = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"domain",b"domain",u"object",b"object",u"registrant",b"registrant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"domain",b"domain",u"object",b"object",u"registrant",b"registrant",u"registrar_tag",b"registrar_tag",u"registry_name",b"registry_name"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal[u"object",b"object"]) -> typing_extensions.Literal["domain","registrant"]: ...
global___ReleaseRequest = ReleaseRequest

class ReleaseReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PENDING_FIELD_NUMBER: builtins.int
    MESSAGE_FIELD_NUMBER: builtins.int
    CMD_RESP_FIELD_NUMBER: builtins.int
    pending: builtins.bool = ...

    @property
    def message(self) -> google.protobuf.wrappers_pb2.StringValue: ...

    @property
    def cmd_resp(self) -> common_pb2.CommandResponse: ...

    def __init__(self,
        *,
        pending : builtins.bool = ...,
        message : typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        cmd_resp : typing.Optional[common_pb2.CommandResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cmd_resp",b"cmd_resp",u"message",b"message"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cmd_resp",b"cmd_resp",u"message",b"message",u"pending",b"pending"]) -> None: ...
global___ReleaseReply = ReleaseReply

class NominetTagListReply(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Tag(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        TAG_FIELD_NUMBER: builtins.int
        NAME_FIELD_NUMBER: builtins.int
        TRADING_NAME_FIELD_NUMBER: builtins.int
        HANDSHAKE_FIELD_NUMBER: builtins.int
        tag: typing.Text = ...
        name: typing.Text = ...
        handshake: builtins.bool = ...

        @property
        def trading_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...

        def __init__(self,
            *,
            tag : typing.Text = ...,
            name : typing.Text = ...,
            trading_name : typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
            handshake : builtins.bool = ...,
            ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal[u"trading_name",b"trading_name"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal[u"handshake",b"handshake",u"name",b"name",u"tag",b"tag",u"trading_name",b"trading_name"]) -> None: ...

    TAGS_FIELD_NUMBER: builtins.int
    CMD_RESP_FIELD_NUMBER: builtins.int

    @property
    def tags(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___NominetTagListReply.Tag]: ...

    @property
    def cmd_resp(self) -> common_pb2.CommandResponse: ...

    def __init__(self,
        *,
        tags : typing.Optional[typing.Iterable[global___NominetTagListReply.Tag]] = ...,
        cmd_resp : typing.Optional[common_pb2.CommandResponse] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cmd_resp",b"cmd_resp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cmd_resp",b"cmd_resp",u"tags",b"tags"]) -> None: ...
global___NominetTagListReply = NominetTagListReply

class DomainCancel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    ORIGINATOR_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    originator: typing.Text = ...

    def __init__(self,
        *,
        name : typing.Text = ...,
        originator : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"name",b"name",u"originator",b"originator"]) -> None: ...
global___DomainCancel = DomainCancel

class DomainRelease(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    ACCOUNT_MOVED_FIELD_NUMBER: builtins.int
    FROM_FIELD_NUMBER: builtins.int
    REGISTRAR_TAG_FIELD_NUMBER: builtins.int
    DOMAINS_FIELD_NUMBER: builtins.int
    account_id: typing.Text = ...
    account_moved: builtins.bool = ...
    registrar_tag: typing.Text = ...
    domains: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    def __init__(self,
        *,
        account_id : typing.Text = ...,
        account_moved : builtins.bool = ...,
        registrar_tag : typing.Text = ...,
        domains : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"account_id",b"account_id",u"account_moved",b"account_moved",u"domains",b"domains",u"from",b"from",u"registrar_tag",b"registrar_tag"]) -> None: ...
global___DomainRelease = DomainRelease

class DomainRegistrarChange(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ORIGINATOR_FIELD_NUMBER: builtins.int
    REGISTRAR_TAG_FIELD_NUMBER: builtins.int
    CASE_ID_FIELD_NUMBER: builtins.int
    DOMAINS_FIELD_NUMBER: builtins.int
    CONTACT_FIELD_NUMBER: builtins.int
    originator: typing.Text = ...
    registrar_tag: typing.Text = ...

    @property
    def case_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...

    @property
    def domains(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[domain_pb2.DomainInfoReply]: ...

    @property
    def contact(self) -> contact_pb2.ContactInfoReply: ...

    def __init__(self,
        *,
        originator : typing.Text = ...,
        registrar_tag : typing.Text = ...,
        case_id : typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        domains : typing.Optional[typing.Iterable[domain_pb2.DomainInfoReply]] = ...,
        contact : typing.Optional[contact_pb2.ContactInfoReply] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"case_id",b"case_id",u"contact",b"contact"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"case_id",b"case_id",u"contact",b"contact",u"domains",b"domains",u"originator",b"originator",u"registrar_tag",b"registrar_tag"]) -> None: ...
global___DomainRegistrarChange = DomainRegistrarChange

class HostCancel(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    HOST_OBJECTS_FIELD_NUMBER: builtins.int
    DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    host_objects: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...
    domain_names: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    def __init__(self,
        *,
        host_objects : typing.Optional[typing.Iterable[typing.Text]] = ...,
        domain_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"domain_names",b"domain_names",u"host_objects",b"host_objects"]) -> None: ...
global___HostCancel = HostCancel

class Process(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _ProcessStage(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ProcessStage.V], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        Initial = Process.ProcessStage.V(0)
        Updated = Process.ProcessStage.V(1)
    class ProcessStage(metaclass=_ProcessStage):
        V = typing.NewType('V', builtins.int)
    Initial = Process.ProcessStage.V(0)
    Updated = Process.ProcessStage.V(1)

    STAGE_FIELD_NUMBER: builtins.int
    CONTACT_FIELD_NUMBER: builtins.int
    PROCESS_TYPE_FIELD_NUMBER: builtins.int
    SUSPEND_DATE_FIELD_NUMBER: builtins.int
    CANCEL_DATE_FIELD_NUMBER: builtins.int
    DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    stage: global___Process.ProcessStage.V = ...
    process_type: typing.Text = ...
    domain_names: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    @property
    def contact(self) -> contact_pb2.ContactInfoReply: ...

    @property
    def suspend_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...

    @property
    def cancel_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...

    def __init__(self,
        *,
        stage : global___Process.ProcessStage.V = ...,
        contact : typing.Optional[contact_pb2.ContactInfoReply] = ...,
        process_type : typing.Text = ...,
        suspend_date : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        cancel_date : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        domain_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cancel_date",b"cancel_date",u"contact",b"contact",u"suspend_date",b"suspend_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cancel_date",b"cancel_date",u"contact",b"contact",u"domain_names",b"domain_names",u"process_type",b"process_type",u"stage",b"stage",u"suspend_date",b"suspend_date"]) -> None: ...
global___Process = Process

class Suspend(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    REASON_FIELD_NUMBER: builtins.int
    CANCEL_DATE_FIELD_NUMBER: builtins.int
    DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    reason: typing.Text = ...
    domain_names: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    @property
    def cancel_date(self) -> google.protobuf.timestamp_pb2.Timestamp: ...

    def __init__(self,
        *,
        reason : typing.Text = ...,
        cancel_date : typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        domain_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"cancel_date",b"cancel_date"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"cancel_date",b"cancel_date",u"domain_names",b"domain_names",u"reason",b"reason"]) -> None: ...
global___Suspend = Suspend

class DomainFail(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    DOMAIN_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    domain: typing.Text = ...
    reason: typing.Text = ...

    def __init__(self,
        *,
        domain : typing.Text = ...,
        reason : typing.Text = ...,
        ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"domain",b"domain",u"reason",b"reason"]) -> None: ...
global___DomainFail = DomainFail

class RegistrantTransfer(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    ORIGINATOR_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    OLD_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    CASE_ID_FIELD_NUMBER: builtins.int
    DOMAIN_NAMES_FIELD_NUMBER: builtins.int
    CONTACT_FIELD_NUMBER: builtins.int
    originator: typing.Text = ...
    account_id: typing.Text = ...
    old_account_id: typing.Text = ...
    domain_names: google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text] = ...

    @property
    def case_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...

    @property
    def contact(self) -> contact_pb2.ContactInfoReply: ...

    def __init__(self,
        *,
        originator : typing.Text = ...,
        account_id : typing.Text = ...,
        old_account_id : typing.Text = ...,
        case_id : typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        domain_names : typing.Optional[typing.Iterable[typing.Text]] = ...,
        contact : typing.Optional[contact_pb2.ContactInfoReply] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"case_id",b"case_id",u"contact",b"contact"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"account_id",b"account_id",u"case_id",b"case_id",u"contact",b"contact",u"domain_names",b"domain_names",u"old_account_id",b"old_account_id",u"originator",b"originator"]) -> None: ...
global___RegistrantTransfer = RegistrantTransfer
