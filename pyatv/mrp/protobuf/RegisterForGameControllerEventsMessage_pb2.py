# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyatv/mrp/protobuf/RegisterForGameControllerEventsMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pyatv.mrp.protobuf import ProtocolMessage_pb2 as pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyatv/mrp/protobuf/RegisterForGameControllerEventsMessage.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n?pyatv/mrp/protobuf/RegisterForGameControllerEventsMessage.proto\x1a(pyatv/mrp/protobuf/ProtocolMessage.proto\"@\n&RegisterForGameControllerEventsMessage\x12\x16\n\x0einputModeFlags\x18\x01 \x01(\x05:i\n&registerForGameControllerEventsMessage\x12\x10.ProtocolMessage\x18\x1b \x01(\x0b\x32\'.RegisterForGameControllerEventsMessage')
  ,
  dependencies=[pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.DESCRIPTOR,])


REGISTERFORGAMECONTROLLEREVENTSMESSAGE_FIELD_NUMBER = 27
registerForGameControllerEventsMessage = _descriptor.FieldDescriptor(
  name='registerForGameControllerEventsMessage', full_name='registerForGameControllerEventsMessage', index=0,
  number=27, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_REGISTERFORGAMECONTROLLEREVENTSMESSAGE = _descriptor.Descriptor(
  name='RegisterForGameControllerEventsMessage',
  full_name='RegisterForGameControllerEventsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputModeFlags', full_name='RegisterForGameControllerEventsMessage.inputModeFlags', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['RegisterForGameControllerEventsMessage'] = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE
DESCRIPTOR.extensions_by_name['registerForGameControllerEventsMessage'] = registerForGameControllerEventsMessage
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterForGameControllerEventsMessage = _reflection.GeneratedProtocolMessageType('RegisterForGameControllerEventsMessage', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE,
  __module__ = 'pyatv.mrp.protobuf.RegisterForGameControllerEventsMessage_pb2'
  # @@protoc_insertion_point(class_scope:RegisterForGameControllerEventsMessage)
  ))
_sym_db.RegisterMessage(RegisterForGameControllerEventsMessage)

registerForGameControllerEventsMessage.message_type = _REGISTERFORGAMECONTROLLEREVENTSMESSAGE
pyatv_dot_mrp_dot_protobuf_dot_ProtocolMessage__pb2.ProtocolMessage.RegisterExtension(registerForGameControllerEventsMessage)

# @@protoc_insertion_point(module_scope)