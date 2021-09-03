# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: divider/v1/divider.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='divider/v1/divider.proto',
  package='distributedcalculator.divider.v1',
  syntax='proto3',
  serialized_options=_b('Z@github.com/sato-mh/distributed-calculator/api/divider/v1;divider'),
  serialized_pb=_b('\n\x18\x64ivider/v1/divider.proto\x12 distributedcalculator.divider.v1\x1a\x1cgoogle/api/annotations.proto\"N\n\nDivRequest\x12\x1f\n\x0boperand_one\x18\x01 \x01(\tR\noperandOne\x12\x1f\n\x0boperand_two\x18\x02 \x01(\tR\noperandTwo\"%\n\x0b\x44ivResponse\x12\x16\n\x06result\x18\x01 \x01(\tR\x06result2\x86\x01\n\x07\x44ivider\x12{\n\x03\x44iv\x12,.distributedcalculator.divider.v1.DivRequest\x1a-.distributedcalculator.divider.v1.DivResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/divider/div:\x01*BBZ@github.com/sato-mh/distributed-calculator/api/divider/v1;dividerb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_DIVREQUEST = _descriptor.Descriptor(
  name='DivRequest',
  full_name='distributedcalculator.divider.v1.DivRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operand_one', full_name='distributedcalculator.divider.v1.DivRequest.operand_one', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='operandOne', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operand_two', full_name='distributedcalculator.divider.v1.DivRequest.operand_two', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='operandTwo', file=DESCRIPTOR),
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
  serialized_start=92,
  serialized_end=170,
)


_DIVRESPONSE = _descriptor.Descriptor(
  name='DivResponse',
  full_name='distributedcalculator.divider.v1.DivResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='distributedcalculator.divider.v1.DivResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='result', file=DESCRIPTOR),
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
  serialized_start=172,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['DivRequest'] = _DIVREQUEST
DESCRIPTOR.message_types_by_name['DivResponse'] = _DIVRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DivRequest = _reflection.GeneratedProtocolMessageType('DivRequest', (_message.Message,), dict(
  DESCRIPTOR = _DIVREQUEST,
  __module__ = 'divider.v1.divider_pb2'
  # @@protoc_insertion_point(class_scope:distributedcalculator.divider.v1.DivRequest)
  ))
_sym_db.RegisterMessage(DivRequest)

DivResponse = _reflection.GeneratedProtocolMessageType('DivResponse', (_message.Message,), dict(
  DESCRIPTOR = _DIVRESPONSE,
  __module__ = 'divider.v1.divider_pb2'
  # @@protoc_insertion_point(class_scope:distributedcalculator.divider.v1.DivResponse)
  ))
_sym_db.RegisterMessage(DivResponse)


DESCRIPTOR._options = None

_DIVIDER = _descriptor.ServiceDescriptor(
  name='Divider',
  full_name='distributedcalculator.divider.v1.Divider',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=212,
  serialized_end=346,
  methods=[
  _descriptor.MethodDescriptor(
    name='Div',
    full_name='distributedcalculator.divider.v1.Divider.Div',
    index=0,
    containing_service=None,
    input_type=_DIVREQUEST,
    output_type=_DIVRESPONSE,
    serialized_options=_b('\202\323\344\223\002\021\"\014/divider/div:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_DIVIDER)

DESCRIPTOR.services_by_name['Divider'] = _DIVIDER

# @@protoc_insertion_point(module_scope)
