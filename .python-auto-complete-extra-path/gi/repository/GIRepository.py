# -*- coding: utf-8 -*-
from gi.repository import GObject


class ArrayType:
    """"""
    C = 0
    ARRAY = 1
    PTR_ARRAY = 2
    BYTE_ARRAY = 3


class Direction:
    """"""
    IN = 0
    OUT = 1
    INOUT = 2


class FieldInfoFlags:
    """"""
    READABLE = 1
    WRITABLE = 2


class FunctionInfoFlags:
    """"""
    IS_METHOD = 1
    IS_CONSTRUCTOR = 2
    IS_GETTER = 4
    IS_SETTER = 8
    WRAPS_VFUNC = 16
    THROWS = 32


class InfoType:
    """"""
    INVALID = 0
    FUNCTION = 1
    CALLBACK = 2
    STRUCT = 3
    BOXED = 4
    ENUM = 5
    FLAGS = 6
    OBJECT = 7
    INTERFACE = 8
    CONSTANT = 9
    INVALID_0 = 10
    UNION = 11
    VALUE = 12
    SIGNAL = 13
    VFUNC = 14
    PROPERTY = 15
    FIELD = 16
    ARG = 17
    TYPE = 18
    UNRESOLVED = 19


class RepositoryError:
    """"""
    TYPELIB_NOT_FOUND = 0
    NAMESPACE_MISMATCH = 1
    NAMESPACE_VERSION_CONFLICT = 2
    LIBRARY_NOT_FOUND = 3


class RepositoryLoadFlags:
    """"""
    IREPOSITORY_LOAD_FLAG_LAZY = 1


class ScopeType:
    """"""
    INVALID = 0
    CALL = 1
    ASYNC = 2
    NOTIFIED = 3


class Transfer:
    """"""
    NOTHING = 0
    CONTAINER = 1
    EVERYTHING = 2


class TypeTag:
    """"""
    VOID = 0
    BOOLEAN = 1
    INT8 = 2
    UINT8 = 3
    INT16 = 4
    UINT16 = 5
    INT32 = 6
    UINT32 = 7
    INT64 = 8
    UINT64 = 9
    FLOAT = 10
    DOUBLE = 11
    GTYPE = 12
    UTF8 = 13
    FILENAME = 14
    ARRAY = 15
    INTERFACE = 16
    GLIST = 17
    GSLIST = 18
    GHASH = 19
    ERROR = 20
    UNICHAR = 21


class VFuncInfoFlags:
    """"""
    MUST_CHAIN_UP = 1
    MUST_OVERRIDE = 2
    MUST_NOT_OVERRIDE = 4
    THROWS = 8

def arg_info_get_closure(info=None):
    """"""
    return object

def arg_info_get_destroy(info=None):
    """"""
    return object

def arg_info_get_direction(info=None):
    """"""
    return object

def arg_info_get_ownership_transfer(info=None):
    """"""
    return object

def arg_info_get_scope(info=None):
    """"""
    return object

def arg_info_get_type(info=None):
    """"""
    return object

def arg_info_is_caller_allocates(info=None):
    """"""
    return object

def arg_info_is_optional(info=None):
    """"""
    return object

def arg_info_is_return_value(info=None):
    """"""
    return object

def arg_info_is_skip(info=None):
    """"""
    return object

def arg_info_load_type(info=None, type=None):
    """"""
    return object

def arg_info_may_be_null(info=None):
    """"""
    return object

def callable_info_can_throw_gerror(info=None):
    """"""
    return object

def callable_info_get_arg(info=None, n=None):
    """"""
    return object

def callable_info_get_caller_owns(info=None):
    """"""
    return object

def callable_info_get_instance_ownership_transfer(info=None):
    """"""
    return object

def callable_info_get_n_args(info=None):
    """"""
    return object

def callable_info_get_return_attribute(info=None, name=None):
    """"""
    return object

def callable_info_get_return_type(info=None):
    """"""
    return object

def callable_info_invoke(info=None, function=None, in_args=None, n_in_args=None, out_args=None, n_out_args=None, return_value=None, is_method=None, throws=None):
    """"""
    return object

def callable_info_is_method(info=None):
    """"""
    return object

def callable_info_iterate_return_attributes(info=None, iterator=None, name=None, value=None):
    """"""
    return object

def callable_info_load_arg(info=None, n=None, arg=None):
    """"""
    return object

def callable_info_load_return_type(info=None, type=None):
    """"""
    return object

def callable_info_may_return_null(info=None):
    """"""
    return object

def callable_info_skip_return(info=None):
    """"""
    return object

def constant_info_free_value(info=None, value=None):
    """"""
    return object

def constant_info_get_type(info=None):
    """"""
    return object

def constant_info_get_value(info=None, value=None):
    """"""
    return object

def enum_info_get_error_domain(info=None):
    """"""
    return object

def enum_info_get_method(info=None, n=None):
    """"""
    return object

def enum_info_get_n_methods(info=None):
    """"""
    return object

def enum_info_get_n_values(info=None):
    """"""
    return object

def enum_info_get_storage_type(info=None):
    """"""
    return object

def enum_info_get_value(info=None, n=None):
    """"""
    return object

def field_info_get_field(field_info=None, mem=None, value=None):
    """"""
    return object

def field_info_get_flags(info=None):
    """"""
    return object

def field_info_get_offset(info=None):
    """"""
    return object

def field_info_get_size(info=None):
    """"""
    return object

def field_info_get_type(info=None):
    """"""
    return object

def field_info_set_field(field_info=None, mem=None, value=None):
    """"""
    return object

def function_info_get_flags(info=None):
    """"""
    return object

def function_info_get_property(info=None):
    """"""
    return object

def function_info_get_symbol(info=None):
    """"""
    return object

def function_info_get_vfunc(info=None):
    """"""
    return object

def function_info_invoke(info=None, in_args=None, n_in_args=None, out_args=None, n_out_args=None, return_value=None):
    """"""
    return object

def info_new(type=None, container=None, typelib=None, offset=None):
    """"""
    return object

def info_type_to_string(type=None):
    """"""
    return object

def interface_info_find_method(info=None, name=None):
    """"""
    return object

def interface_info_find_signal(info=None, name=None):
    """"""
    return object

def interface_info_find_vfunc(info=None, name=None):
    """"""
    return object

def interface_info_get_constant(info=None, n=None):
    """"""
    return object

def interface_info_get_iface_struct(info=None):
    """"""
    return object

def interface_info_get_method(info=None, n=None):
    """"""
    return object

def interface_info_get_n_constants(info=None):
    """"""
    return object

def interface_info_get_n_methods(info=None):
    """"""
    return object

def interface_info_get_n_prerequisites(info=None):
    """"""
    return object

def interface_info_get_n_properties(info=None):
    """"""
    return object

def interface_info_get_n_signals(info=None):
    """"""
    return object

def interface_info_get_n_vfuncs(info=None):
    """"""
    return object

def interface_info_get_prerequisite(info=None, n=None):
    """"""
    return object

def interface_info_get_property(info=None, n=None):
    """"""
    return object

def interface_info_get_signal(info=None, n=None):
    """"""
    return object

def interface_info_get_vfunc(info=None, n=None):
    """"""
    return object

def invoke_error_quark():
    """"""
    return object


class nvokeError:
    """"""
    FAILED = 0
    SYMBOL_NOT_FOUND = 1
    ARGUMENT_MISMATCH = 2

def object_info_find_method(info=None, name=None):
    """"""
    return object

def object_info_find_method_using_interfaces(info=None, name=None, implementor=None):
    """"""
    return object

def object_info_find_signal(info=None, name=None):
    """"""
    return object

def object_info_find_vfunc(info=None, name=None):
    """"""
    return object

def object_info_find_vfunc_using_interfaces(info=None, name=None, implementor=None):
    """"""
    return object

def object_info_get_abstract(info=None):
    """"""
    return object

def object_info_get_class_struct(info=None):
    """"""
    return object

def object_info_get_constant(info=None, n=None):
    """"""
    return object

def object_info_get_field(info=None, n=None):
    """"""
    return object

def object_info_get_fundamental(info=None):
    """"""
    return object

def object_info_get_get_value_function(info=None):
    """"""
    return object

def object_info_get_get_value_function_pointer(info=None):
    """"""
    return object

def object_info_get_interface(info=None, n=None):
    """"""
    return object

def object_info_get_method(info=None, n=None):
    """"""
    return object

def object_info_get_n_constants(info=None):
    """"""
    return object

def object_info_get_n_fields(info=None):
    """"""
    return object

def object_info_get_n_interfaces(info=None):
    """"""
    return object

def object_info_get_n_methods(info=None):
    """"""
    return object

def object_info_get_n_properties(info=None):
    """"""
    return object

def object_info_get_n_signals(info=None):
    """"""
    return object

def object_info_get_n_vfuncs(info=None):
    """"""
    return object

def object_info_get_parent(info=None):
    """"""
    return object

def object_info_get_property(info=None, n=None):
    """"""
    return object

def object_info_get_ref_function(info=None):
    """"""
    return object

def object_info_get_ref_function_pointer(info=None):
    """"""
    return object

def object_info_get_set_value_function(info=None):
    """"""
    return object

def object_info_get_set_value_function_pointer(info=None):
    """"""
    return object

def object_info_get_signal(info=None, n=None):
    """"""
    return object

def object_info_get_type_init(info=None):
    """"""
    return object

def object_info_get_type_name(info=None):
    """"""
    return object

def object_info_get_unref_function(info=None):
    """"""
    return object

def object_info_get_unref_function_pointer(info=None):
    """"""
    return object

def object_info_get_vfunc(info=None, n=None):
    """"""
    return object

def property_info_get_flags(info=None):
    """"""
    return object

def property_info_get_ownership_transfer(info=None):
    """"""
    return object

def property_info_get_type(info=None):
    """"""
    return object

def registered_type_info_get_g_type(info=None):
    """"""
    return object

def registered_type_info_get_type_init(info=None):
    """"""
    return object

def registered_type_info_get_type_name(info=None):
    """"""
    return object

def signal_info_get_class_closure(info=None):
    """"""
    return object

def signal_info_get_flags(info=None):
    """"""
    return object

def signal_info_true_stops_emit(info=None):
    """"""
    return object

def struct_info_find_field(info=None, name=None):
    """"""
    return object

def struct_info_find_method(info=None, name=None):
    """"""
    return object

def struct_info_get_alignment(info=None):
    """"""
    return object

def struct_info_get_field(info=None, n=None):
    """"""
    return object

def struct_info_get_method(info=None, n=None):
    """"""
    return object

def struct_info_get_n_fields(info=None):
    """"""
    return object

def struct_info_get_n_methods(info=None):
    """"""
    return object

def struct_info_get_size(info=None):
    """"""
    return object

def struct_info_is_foreign(info=None):
    """"""
    return object

def struct_info_is_gtype_struct(info=None):
    """"""
    return object

def type_info_get_array_fixed_size(info=None):
    """"""
    return object

def type_info_get_array_length(info=None):
    """"""
    return object

def type_info_get_array_type(info=None):
    """"""
    return object

def type_info_get_interface(info=None):
    """"""
    return object

def type_info_get_param_type(info=None, n=None):
    """"""
    return object

def type_info_get_tag(info=None):
    """"""
    return object

def type_info_is_pointer(info=None):
    """"""
    return object

def type_info_is_zero_terminated(info=None):
    """"""
    return object

def type_tag_to_string(type=None):
    """"""
    return object

def union_info_find_method(info=None, name=None):
    """"""
    return object

def union_info_get_alignment(info=None):
    """"""
    return object

def union_info_get_discriminator(info=None, n=None):
    """"""
    return object

def union_info_get_discriminator_offset(info=None):
    """"""
    return object

def union_info_get_discriminator_type(info=None):
    """"""
    return object

def union_info_get_field(info=None, n=None):
    """"""
    return object

def union_info_get_method(info=None, n=None):
    """"""
    return object

def union_info_get_n_fields(info=None):
    """"""
    return object

def union_info_get_n_methods(info=None):
    """"""
    return object

def union_info_get_size(info=None):
    """"""
    return object

def union_info_is_discriminated(info=None):
    """"""
    return object

def value_info_get_value(info=None):
    """"""
    return object

def vfunc_info_get_address(info=None, implementor_gtype=None):
    """"""
    return object

def vfunc_info_get_flags(info=None):
    """"""
    return object

def vfunc_info_get_invoker(info=None):
    """"""
    return object

def vfunc_info_get_offset(info=None):
    """"""
    return object

def vfunc_info_get_signal(info=None):
    """"""
    return object

def vfunc_info_invoke(info=None, implementor=None, in_args=None, n_in_args=None, out_args=None, n_out_args=None, return_value=None):
    """"""
    return object


class AttributeIter():
    """"""

    @property
    def data(self):
        return object

    @property
    def data2(self):
        return object

    @property
    def data3(self):
        return object

    @property
    def data4(self):
        return object


class BaseInfo():
    """"""
    
    def equal(self, info2=None):
        """"""
        return object
    
    def get_attribute(self, name=None):
        """"""
        return object
    
    def get_container(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_namespace(self):
        """"""
        return object
    
    def get_type(self):
        """"""
        return object
    
    def get_typelib(self):
        """"""
        return object
    
    def is_deprecated(self):
        """"""
        return object
    
    def iterate_attributes(self, iterator=None, name=None, value=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def dummy1(self):
        return object

    @property
    def dummy2(self):
        return object

    @property
    def dummy3(self):
        return object

    @property
    def dummy4(self):
        return object

    @property
    def dummy5(self):
        return object

    @property
    def dummy6(self):
        return object

    @property
    def dummy7(self):
        return object

    @property
    def padding(self):
        return object


class Repository(GObject.Object):
    """"""
    @staticmethod
    def dump(arg=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    @staticmethod
    def get_default():
        """"""
        return object
    @staticmethod
    def get_option_group():
        """"""
        return object
    @staticmethod
    def get_search_path():
        """"""
        return object
    @staticmethod
    def prepend_library_path(directory=None):
        """"""
        return object
    @staticmethod
    def prepend_search_path(directory=None):
        """"""
        return object
    
    def enumerate_versions(self, namespace_=None):
        """"""
        return object
    
    def find_by_error_domain(self, domain=None):
        """"""
        return object
    
    def find_by_gtype(self, gtype=None):
        """"""
        return object
    
    def find_by_name(self, namespace_=None, name=None):
        """"""
        return object
    
    def get_c_prefix(self, namespace_=None):
        """"""
        return object
    
    def get_dependencies(self, namespace_=None):
        """"""
        return object
    
    def get_immediate_dependencies(self, namespace_=None):
        """"""
        return object
    
    def get_info(self, namespace_=None, index=None):
        """"""
        return object
    
    def get_loaded_namespaces(self):
        """"""
        return object
    
    def get_n_infos(self, namespace_=None):
        """"""
        return object
    
    def get_shared_library(self, namespace_=None):
        """"""
        return object
    
    def get_typelib_path(self, namespace_=None):
        """"""
        return object
    
    def get_version(self, namespace_=None):
        """"""
        return object
    
    def is_registered(self, namespace_=None, version=None):
        """"""
        return object
    
    def load_typelib(self, typelib=None, flags=None):
        """"""
        return object
    
    def require(self, namespace_=None, version=None, flags=None):
        """"""
        return object
    
    def require_private(self, typelib_dir=None, namespace_=None, version=None, flags=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object


class RepositoryClass():
    """"""

    @property
    def parent(self):
        return object


class RepositoryPrivate():
    """"""


class Typelib():
    """"""
    
    def free(self):
        """"""
        return object
    
    def get_namespace(self):
        """"""
        return object
    
    def symbol(self, symbol_name=None, symbol=None):
        """"""
        return object
    @staticmethod
    def new_from_const_memory(memory=None, len=None):
        """"""
        return object
    @staticmethod
    def new_from_mapped_file(mfile=None):
        """"""
        return object
    @staticmethod
    def new_from_memory(memory=None, len=None):
        """"""
        return object


class UnresolvedInfo():
    """"""
