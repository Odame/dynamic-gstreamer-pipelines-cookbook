# -*- coding: utf-8 -*-


class BindingFlags:
    """"""
    DEFAULT = 0
    BIDIRECTIONAL = 1
    SYNC_CREATE = 2
    INVERT_BOOLEAN = 4


class ConnectFlags:
    """"""
    AFTER = 1
    SWAPPED = 2
PARAM_MASK = r"""255"""
PARAM_STATIC_STRINGS = r"""224"""
PARAM_USER_SHIFT = r"""8"""


class ParamFlags:
    """"""
    READABLE = 1
    WRITABLE = 2
    READWRITE = 3
    CONSTRUCT = 4
    CONSTRUCT_ONLY = 8
    LAX_VALIDATION = 16
    STATIC_NAME = 32
    PRIVATE = 32
    STATIC_NICK = 64
    STATIC_BLURB = 128
    EXPLICIT_NOTIFY = 1073741824
    DEPRECATED = 2147483648
SIGNAL_FLAGS_MASK = r"""511"""
SIGNAL_MATCH_MASK = r"""63"""


class SignalFlags:
    """"""
    RUN_FIRST = 1
    RUN_LAST = 2
    RUN_CLEANUP = 4
    NO_RECURSE = 8
    DETAILED = 16
    ACTION = 32
    NO_HOOKS = 64
    MUST_COLLECT = 128
    DEPRECATED = 256


class SignalMatchType:
    """"""
    ID = 1
    DETAIL = 2
    CLOSURE = 4
    FUNC = 8
    DATA = 16
    UNBLOCKED = 32
TYPE_FLAG_RESERVED_ID_BIT = r"""1"""
TYPE_FUNDAMENTAL_MAX = r"""255"""
TYPE_FUNDAMENTAL_SHIFT = r"""2"""
TYPE_RESERVED_BSE_FIRST = r"""32"""
TYPE_RESERVED_BSE_LAST = r"""48"""
TYPE_RESERVED_GLIB_FIRST = r"""22"""
TYPE_RESERVED_GLIB_LAST = r"""31"""
TYPE_RESERVED_USER_FIRST = r"""49"""


class TypeDebugFlags:
    """"""
    NONE = 0
    OBJECTS = 1
    SIGNALS = 2
    INSTANCE_COUNT = 4
    MASK = 7


class TypeFlags:
    """"""
    ABSTRACT = 16
    VALUE_ABSTRACT = 32


class TypeFundamentalFlags:
    """"""
    CLASSED = 1
    INSTANTIATABLE = 2
    DERIVABLE = 4
    DEEP_DERIVABLE = 8
VALUE_COLLECT_FORMAT_MAX_LENGTH = r"""8"""
VALUE_NOCOPY_CONTENTS = r"""134217728"""

def boxed_copy(boxed_type=None, src_boxed=None):
    """"""
    return object

def boxed_free(boxed_type=None, boxed=None):
    """"""
    return object

def boxed_type_register_static(name=None, boxed_copy=None, boxed_free=None):
    """"""
    return object

def cclosure_marshal_BOOLEAN__BOXED_BOXED(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_BOOLEAN__FLAGS(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_STRING__OBJECT_POINTER(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__BOOLEAN(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__BOXED(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__CHAR(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__DOUBLE(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__ENUM(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__FLAGS(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__FLOAT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__INT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__LONG(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__OBJECT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__PARAM(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__POINTER(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__STRING(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__UCHAR(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__UINT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__UINT_POINTER(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__ULONG(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__VARIANT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_VOID__VOID(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_marshal_generic(closure=None, return_gvalue=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
    """"""
    return object

def cclosure_new(callback_func=None, user_data=None, destroy_data=None):
    """"""
    return object

def cclosure_new_object(callback_func=None, object=None):
    """"""
    return object

def cclosure_new_object_swap(callback_func=None, object=None):
    """"""
    return object

def cclosure_new_swap(callback_func=None, user_data=None, destroy_data=None):
    """"""
    return object

def clear_object(object_ptr=None):
    """"""
    return object

def enum_complete_type_info(g_enum_type=None, info=None, const_values=None):
    """"""
    return object

def enum_get_value(enum_class=None, value=None):
    """"""
    return object

def enum_get_value_by_name(enum_class=None, name=None):
    """"""
    return object

def enum_get_value_by_nick(enum_class=None, nick=None):
    """"""
    return object

def enum_register_static(name=None, const_static_values=None):
    """"""
    return object

def enum_to_string(g_enum_type=None, value=None):
    """"""
    return object

def flags_complete_type_info(g_flags_type=None, info=None, const_values=None):
    """"""
    return object

def flags_get_first_value(flags_class=None, value=None):
    """"""
    return object

def flags_get_value_by_name(flags_class=None, name=None):
    """"""
    return object

def flags_get_value_by_nick(flags_class=None, nick=None):
    """"""
    return object

def flags_register_static(name=None, const_static_values=None):
    """"""
    return object

def flags_to_string(flags_type=None, value=None):
    """"""
    return object

def gtype_get_type():
    """"""
    return object

def param_spec_boolean(name=None, nick=None, blurb=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_boxed(name=None, nick=None, blurb=None, boxed_type=None, flags=None):
    """"""
    return object

def param_spec_char(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_double(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_enum(name=None, nick=None, blurb=None, enum_type=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_flags(name=None, nick=None, blurb=None, flags_type=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_float(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_gtype(name=None, nick=None, blurb=None, is_a_type=None, flags=None):
    """"""
    return object

def param_spec_int(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_int64(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_long(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_object(name=None, nick=None, blurb=None, object_type=None, flags=None):
    """"""
    return object

def param_spec_override(name=None, overridden=None):
    """"""
    return object

def param_spec_param(name=None, nick=None, blurb=None, param_type=None, flags=None):
    """"""
    return object

def param_spec_pointer(name=None, nick=None, blurb=None, flags=None):
    """"""
    return object

def param_spec_pool_new(type_prefixing=None):
    """"""
    return object

def param_spec_string(name=None, nick=None, blurb=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_uchar(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_uint(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_uint64(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_ulong(name=None, nick=None, blurb=None, minimum=None, maximum=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_unichar(name=None, nick=None, blurb=None, default_value=None, flags=None):
    """"""
    return object

def param_spec_value_array(name=None, nick=None, blurb=None, element_spec=None, flags=None):
    """"""
    return object

def param_spec_variant(name=None, nick=None, blurb=None, type=None, default_value=None, flags=None):
    """"""
    return object

def param_type_register_static(name=None, pspec_info=None):
    """"""
    return object

def param_value_convert(pspec=None, src_value=None, dest_value=None, strict_validation=None):
    """"""
    return object

def param_value_defaults(pspec=None, value=None):
    """"""
    return object

def param_value_set_default(pspec=None, value=None):
    """"""
    return object

def param_value_validate(pspec=None, value=None):
    """"""
    return object

def param_values_cmp(pspec=None, value1=None, value2=None):
    """"""
    return object

def pointer_type_register_static(name=None):
    """"""
    return object

def signal_accumulator_first_wins(ihint=None, return_accu=None, handler_return=None, dummy=None):
    """"""
    return object

def signal_accumulator_true_handled(ihint=None, return_accu=None, handler_return=None, dummy=None):
    """"""
    return object

def signal_add_emission_hook(signal_id=None, detail=None, hook_func=None, hook_data=None, data_destroy=None):
    """"""
    return object

def signal_chain_from_overridden(instance_and_params=None, return_value=None):
    """"""
    return object

def signal_chain_from_overridden_handler(instance=None, *args):
    """"""
    return object

def signal_connect_closure(instance=None, detailed_signal=None, closure=None, after=None):
    """"""
    return object

def signal_connect_closure_by_id(instance=None, signal_id=None, detail=None, closure=None, after=None):
    """"""
    return object

def signal_connect_data(instance=None, detailed_signal=None, c_handler=None, data=None, destroy_data=None, connect_flags=None):
    """"""
    return object

def signal_connect_object(instance=None, detailed_signal=None, c_handler=None, gobject=None, connect_flags=None):
    """"""
    return object

def signal_emit(instance=None, signal_id=None, detail=None, *args):
    """"""
    return object

def signal_emit_by_name(instance=None, detailed_signal=None, *args):
    """"""
    return object

def signal_emit_valist(instance=None, signal_id=None, detail=None, var_args=None):
    """"""
    return object

def signal_emitv(instance_and_params=None, signal_id=None, detail=None, return_value=None):
    """"""
    return object

def signal_get_invocation_hint(instance=None):
    """"""
    return object

def signal_handler_block(instance=None, handler_id=None):
    """"""
    return object

def signal_handler_disconnect(instance=None, handler_id=None):
    """"""
    return object

def signal_handler_find(instance=None, mask=None, signal_id=None, detail=None, closure=None, func=None, data=None):
    """"""
    return object

def signal_handler_is_connected(instance=None, handler_id=None):
    """"""
    return object

def signal_handler_unblock(instance=None, handler_id=None):
    """"""
    return object

def signal_handlers_block_matched(instance=None, mask=None, signal_id=None, detail=None, closure=None, func=None, data=None):
    """"""
    return object

def signal_handlers_destroy(instance=None):
    """"""
    return object

def signal_handlers_disconnect_matched(instance=None, mask=None, signal_id=None, detail=None, closure=None, func=None, data=None):
    """"""
    return object

def signal_handlers_unblock_matched(instance=None, mask=None, signal_id=None, detail=None, closure=None, func=None, data=None):
    """"""
    return object

def signal_has_handler_pending(instance=None, signal_id=None, detail=None, may_be_blocked=None):
    """"""
    return object

def signal_list_ids(itype=None, n_ids=None):
    """"""
    return object

def signal_lookup(name=None, itype=None):
    """"""
    return object

def signal_name(signal_id=None):
    """"""
    return object

def signal_new(signal_name=None, itype=None, signal_flags=None, class_offset=None, accumulator=None, accu_data=None, c_marshaller=None, return_type=None, n_params=None, *args):
    """"""
    return object

def signal_new_class_handler(signal_name=None, itype=None, signal_flags=None, class_handler=None, accumulator=None, accu_data=None, c_marshaller=None, return_type=None, n_params=None, *args):
    """"""
    return object

def signal_new_valist(signal_name=None, itype=None, signal_flags=None, class_closure=None, accumulator=None, accu_data=None, c_marshaller=None, return_type=None, n_params=None, args=None):
    """"""
    return object

def signal_newv(signal_name=None, itype=None, signal_flags=None, class_closure=None, accumulator=None, accu_data=None, c_marshaller=None, return_type=None, n_params=None, param_types=None):
    """"""
    return object

def signal_override_class_closure(signal_id=None, instance_type=None, class_closure=None):
    """"""
    return object

def signal_override_class_handler(signal_name=None, instance_type=None, class_handler=None):
    """"""
    return object

def signal_parse_name(detailed_signal=None, itype=None, signal_id_p=None, detail_p=None, force_detail_quark=None):
    """"""
    return object

def signal_query(signal_id=None, query=None):
    """"""
    return object

def signal_remove_emission_hook(signal_id=None, hook_id=None):
    """"""
    return object

def signal_set_va_marshaller(signal_id=None, instance_type=None, va_marshaller=None):
    """"""
    return object

def signal_stop_emission(instance=None, signal_id=None, detail=None):
    """"""
    return object

def signal_stop_emission_by_name(instance=None, detailed_signal=None):
    """"""
    return object

def signal_type_cclosure_new(itype=None, struct_offset=None):
    """"""
    return object

def source_set_closure(source=None, closure=None):
    """"""
    return object

def source_set_dummy_callback(source=None):
    """"""
    return object

def strdup_value_contents(value=None):
    """"""
    return object

def type_add_class_cache_func(cache_data=None, cache_func=None):
    """"""
    return object

def type_add_class_private(class_type=None, private_size=None):
    """"""
    return object

def type_add_instance_private(class_type=None, private_size=None):
    """"""
    return object

def type_add_interface_check(check_data=None, check_func=None):
    """"""
    return object

def type_add_interface_dynamic(instance_type=None, interface_type=None, plugin=None):
    """"""
    return object

def type_add_interface_static(instance_type=None, interface_type=None, info=None):
    """"""
    return object

def type_check_class_cast(g_class=None, is_a_type=None):
    """"""
    return object

def type_check_class_is_a(g_class=None, is_a_type=None):
    """"""
    return object

def type_check_instance(instance=None):
    """"""
    return object

def type_check_instance_cast(instance=None, iface_type=None):
    """"""
    return object

def type_check_instance_is_a(instance=None, iface_type=None):
    """"""
    return object

def type_check_instance_is_fundamentally_a(instance=None, fundamental_type=None):
    """"""
    return object

def type_check_is_value_type(type=None):
    """"""
    return object

def type_check_value(value=None):
    """"""
    return object

def type_check_value_holds(value=None, type=None):
    """"""
    return object

def type_children(type=None, n_children=None):
    """"""
    return object

def type_class_adjust_private_offset(g_class=None, private_size_or_offset=None):
    """"""
    return object

def type_class_peek(type=None):
    """"""
    return object

def type_class_peek_static(type=None):
    """"""
    return object

def type_class_ref(type=None):
    """"""
    return object

def type_create_instance(type=None):
    """"""
    return object

def type_default_interface_peek(g_type=None):
    """"""
    return object

def type_default_interface_ref(g_type=None):
    """"""
    return object

def type_default_interface_unref(g_iface=None):
    """"""
    return object

def type_depth(type=None):
    """"""
    return object

def type_ensure(type=None):
    """"""
    return object

def type_free_instance(instance=None):
    """"""
    return object

def type_from_name(name=None):
    """"""
    return object

def type_fundamental(type_id=None):
    """"""
    return object

def type_fundamental_next():
    """"""
    return object

def type_get_instance_count(type=None):
    """"""
    return object

def type_get_plugin(type=None):
    """"""
    return object

def type_get_qdata(type=None, quark=None):
    """"""
    return object

def type_get_type_registration_serial():
    """"""
    return object

def type_init():
    """"""
    return object

def type_init_with_debug_flags(debug_flags=None):
    """"""
    return object

def type_interface_add_prerequisite(interface_type=None, prerequisite_type=None):
    """"""
    return object

def type_interface_get_plugin(instance_type=None, interface_type=None):
    """"""
    return object

def type_interface_peek(instance_class=None, iface_type=None):
    """"""
    return object

def type_interface_prerequisites(interface_type=None, n_prerequisites=None):
    """"""
    return object

def type_interfaces(type=None, n_interfaces=None):
    """"""
    return object

def type_is_a(type=None, is_a_type=None):
    """"""
    return object

def type_name(type=None):
    """"""
    return object

def type_name_from_class(g_class=None):
    """"""
    return object

def type_name_from_instance(instance=None):
    """"""
    return object

def type_next_base(leaf_type=None, root_type=None):
    """"""
    return object

def type_parent(type=None):
    """"""
    return object

def type_qname(type=None):
    """"""
    return object

def type_query(type=None, query=None):
    """"""
    return object

def type_register_dynamic(parent_type=None, type_name=None, plugin=None, flags=None):
    """"""
    return object

def type_register_fundamental(type_id=None, type_name=None, info=None, finfo=None, flags=None):
    """"""
    return object

def type_register_static(parent_type=None, type_name=None, info=None, flags=None):
    """"""
    return object

def type_register_static_simple(parent_type=None, type_name=None, class_size=None, class_init=None, instance_size=None, instance_init=None, flags=None):
    """"""
    return object

def type_remove_class_cache_func(cache_data=None, cache_func=None):
    """"""
    return object

def type_remove_interface_check(check_data=None, check_func=None):
    """"""
    return object

def type_set_qdata(type=None, quark=None, data=None):
    """"""
    return object

def type_test_flags(type=None, flags=None):
    """"""
    return object

def type_value_table_peek(type=None):
    """"""
    return object

def value_register_transform_func(src_type=None, dest_type=None, transform_func=None):
    """"""
    return object

def value_type_compatible(src_type=None, dest_type=None):
    """"""
    return object

def value_type_transformable(src_type=None, dest_type=None):
    """"""
    return object


class CClosure():
    """"""
    @staticmethod
    def marshal_BOOLEAN__BOXED_BOXED(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_BOOLEAN__BOXED_BOXEDv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_BOOLEAN__FLAGS(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_BOOLEAN__FLAGSv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_STRING__OBJECT_POINTER(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_STRING__OBJECT_POINTERv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__BOOLEAN(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__BOOLEANv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__BOXED(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__BOXEDv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__CHAR(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__CHARv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__DOUBLE(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__DOUBLEv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__ENUM(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__ENUMv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__FLAGS(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__FLAGSv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__FLOAT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__FLOATv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__INT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__INTv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__LONG(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__LONGv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__OBJECT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__OBJECTv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__PARAM(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__PARAMv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__POINTER(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__POINTERv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__STRING(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__STRINGv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__UCHAR(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__UCHARv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__UINT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__UINT_POINTER(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__UINT_POINTERv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__UINTv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__ULONG(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__ULONGv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__VARIANT(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__VARIANTv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__VOID(closure=None, return_value=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_VOID__VOIDv(closure=None, return_value=None, instance=None, args=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def marshal_generic(closure=None, return_gvalue=None, n_param_values=None, param_values=None, invocation_hint=None, marshal_data=None):
        """"""
        return object
    @staticmethod
    def marshal_generic_va(closure=None, return_value=None, instance=None, args_list=None, marshal_data=None, n_params=None, param_types=None):
        """"""
        return object
    @staticmethod
    def new(callback_func=None, user_data=None, destroy_data=None):
        """"""
        return object
    @staticmethod
    def new_object(callback_func=None, object=None):
        """"""
        return object
    @staticmethod
    def new_object_swap(callback_func=None, object=None):
        """"""
        return object
    @staticmethod
    def new_swap(callback_func=None, user_data=None, destroy_data=None):
        """"""
        return object

    @property
    def closure(self):
        return object

    @property
    def callback(self):
        return object


class Closure():
    """"""
    @staticmethod
    def new_object(sizeof_closure=None, object=None):
        """"""
        return object
    @staticmethod
    def new_simple(sizeof_closure=None, data=None):
        """"""
        return object
    
    def add_finalize_notifier(self, notify_data=None, notify_func=None):
        """"""
        return object
    
    def add_invalidate_notifier(self, notify_data=None, notify_func=None):
        """"""
        return object
    
    def add_marshal_guards(self, pre_marshal_data=None, pre_marshal_notify=None, post_marshal_data=None, post_marshal_notify=None):
        """"""
        return object
    
    def invalidate(self):
        """"""
        return object
    
    def invoke(self, return_value=None, n_param_values=None, param_values=None, invocation_hint=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def remove_finalize_notifier(self, notify_data=None, notify_func=None):
        """"""
        return object
    
    def remove_invalidate_notifier(self, notify_data=None, notify_func=None):
        """"""
        return object
    
    def set_marshal(self, marshal=None):
        """"""
        return object
    
    def set_meta_marshal(self, marshal_data=None, meta_marshal=None):
        """"""
        return object
    
    def sink(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def meta_marshal_nouse(self):
        return object

    @property
    def n_guards(self):
        return object

    @property
    def n_fnotifiers(self):
        return object

    @property
    def n_inotifiers(self):
        return object

    @property
    def in_inotify(self):
        return object

    @property
    def floating(self):
        return object

    @property
    def derivative_flag(self):
        return object

    @property
    def in_marshal(self):
        return object

    @property
    def is_invalid(self):
        return object

    @property
    def marshal(self):
        return object

    @property
    def data(self):
        return object

    @property
    def notifiers(self):
        return object


class ClosureNotifyData():
    """"""

    @property
    def data(self):
        return object

    @property
    def notify(self):
        return object


class EnumClass():
    """"""

    @property
    def g_type_class(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def n_values(self):
        return object

    @property
    def values(self):
        return object


class EnumValue():
    """"""

    @property
    def value(self):
        return object

    @property
    def value_name(self):
        return object

    @property
    def value_nick(self):
        return object


class FlagsClass():
    """"""

    @property
    def g_type_class(self):
        return object

    @property
    def mask(self):
        return object

    @property
    def n_values(self):
        return object

    @property
    def values(self):
        return object


class FlagsValue():
    """"""

    @property
    def value(self):
        return object

    @property
    def value_name(self):
        return object

    @property
    def value_nick(self):
        return object


class InitiallyUnownedClass():
    """"""

    @property
    def g_type_class(self):
        return object

    @property
    def construct_properties(self):
        return object

    @property
    def constructor(self):
        return object

    @property
    def set_property(self):
        return object

    @property
    def get_property(self):
        return object

    @property
    def dispose(self):
        return object

    @property
    def finalize(self):
        return object

    @property
    def dispatch_properties_changed(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def constructed(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def pdummy(self):
        return object


class InterfaceInfo():
    """"""

    @property
    def interface_init(self):
        return object

    @property
    def interface_finalize(self):
        return object

    @property
    def interface_data(self):
        return object


class Object():
    """"""
    
    def __init__(self, object_type=None, first_property_name=None, *args):
        """"""
        return object
    @staticmethod
    def new(object_type=None, first_property_name=None, *args):
        """"""
        return object
    @staticmethod
    def new_valist(object_type=None, first_property_name=None, var_args=None):
        """"""
        return object
    @staticmethod
    def new_with_properties(object_type=None, n_properties=None, names=None, values=None):
        """"""
        return object
    @staticmethod
    def newv(object_type=None, n_parameters=None, parameters=None):
        """"""
        return object
    @staticmethod
    def compat_control(what=None, data=None):
        """"""
        return object
    @staticmethod
    def interface_find_property(g_iface=None, property_name=None):
        """"""
        return object
    @staticmethod
    def interface_install_property(g_iface=None, pspec=None):
        """"""
        return object
    @staticmethod
    def interface_list_properties(g_iface=None, n_properties_p=None):
        """"""
        return object
    
    def constructed(self):
        """"""
        return object
    
    def dispatch_properties_changed(self, n_pspecs=None, pspecs=None):
        """"""
        return object
    
    def dispose(self):
        """"""
        return object
    
    def finalize(self):
        """"""
        return object
    
    def get_property(self, property_id=None, value=None, pspec=None):
        """"""
        return object
    
    def notify(self, pspec=None):
        """"""
        return object
    
    def set_property(self, property_id=None, value=None, pspec=None):
        """"""
        return object
    
    def add_toggle_ref(self, notify=None, data=None):
        """"""
        return object
    
    def add_weak_pointer(self, weak_pointer_location=None):
        """"""
        return object
    
    def bind_property(self, source_property=None, target=None, target_property=None, flags=None):
        """"""
        return object
    
    def bind_property_full(self, source_property=None, target=None, target_property=None, flags=None, transform_to=None, transform_from=None, user_data=None, notify=None):
        """"""
        return object
    
    def bind_property_with_closures(self, source_property=None, target=None, target_property=None, flags=None, transform_to=None, transform_from=None):
        """"""
        return object
    
    def connect(self, signal_spec=None, *args):
        """"""
        return object
    
    def disconnect(self, signal_spec=None, *args):
        """"""
        return object
    
    def dup_data(self, key=None, dup_func=None, user_data=None):
        """"""
        return object
    
    def dup_qdata(self, quark=None, dup_func=None, user_data=None):
        """"""
        return object
    
    def force_floating(self):
        """"""
        return object
    
    def freeze_notify(self):
        """"""
        return object
    
    def get(self, first_property_name=None, *args):
        """"""
        return object
    
    def get_data(self, key=None):
        """"""
        return object
    
    def get_property(self, property_name=None, value=None):
        """"""
        return object
    
    def get_qdata(self, quark=None):
        """"""
        return object
    
    def get_valist(self, first_property_name=None, var_args=None):
        """"""
        return object
    
    def getv(self, n_properties=None, names=None, values=None):
        """"""
        return object
    
    def is_floating(self):
        """"""
        return object
    
    def notify(self, property_name=None):
        """"""
        return object
    
    def notify_by_pspec(self, pspec=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def ref_sink(self):
        """"""
        return object
    
    def remove_toggle_ref(self, notify=None, data=None):
        """"""
        return object
    
    def remove_weak_pointer(self, weak_pointer_location=None):
        """"""
        return object
    
    def replace_data(self, key=None, oldval=None, newval=None, destroy=None, old_destroy=None):
        """"""
        return object
    
    def replace_qdata(self, quark=None, oldval=None, newval=None, destroy=None, old_destroy=None):
        """"""
        return object
    
    def run_dispose(self):
        """"""
        return object
    
    def set(self, first_property_name=None, *args):
        """"""
        return object
    
    def set_data(self, key=None, data=None):
        """"""
        return object
    
    def set_data_full(self, key=None, data=None, destroy=None):
        """"""
        return object
    
    def set_property(self, property_name=None, value=None):
        """"""
        return object
    
    def set_qdata(self, quark=None, data=None):
        """"""
        return object
    
    def set_qdata_full(self, quark=None, data=None, destroy=None):
        """"""
        return object
    
    def set_valist(self, first_property_name=None, var_args=None):
        """"""
        return object
    
    def setv(self, n_properties=None, names=None, values=None):
        """"""
        return object
    
    def steal_data(self, key=None):
        """"""
        return object
    
    def steal_qdata(self, quark=None):
        """"""
        return object
    
    def thaw_notify(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def watch_closure(self, closure=None):
        """"""
        return object
    
    def weak_ref(self, notify=None, data=None):
        """"""
        return object
    
    def weak_unref(self, notify=None, data=None):
        """"""
        return object

    @property
    def g_type_instance(self):
        return object

    @property
    def ref_count(self):
        return object

    @property
    def qdata(self):
        return object


class ObjectClass():
    """"""
    
    def find_property(self, property_name=None):
        """"""
        return object
    
    def install_properties(self, n_pspecs=None, pspecs=None):
        """"""
        return object
    
    def install_property(self, property_id=None, pspec=None):
        """"""
        return object
    
    def list_properties(self, n_properties=None):
        """"""
        return object
    
    def override_property(self, property_id=None, name=None):
        """"""
        return object

    @property
    def g_type_class(self):
        return object

    @property
    def construct_properties(self):
        return object

    @property
    def constructor(self):
        return object

    @property
    def set_property(self):
        return object

    @property
    def get_property(self):
        return object

    @property
    def dispose(self):
        return object

    @property
    def finalize(self):
        return object

    @property
    def dispatch_properties_changed(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def constructed(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def pdummy(self):
        return object


class ObjectConstructParam():
    """"""

    @property
    def pspec(self):
        return object

    @property
    def value(self):
        return object


class ParamSpec():
    """"""
    @staticmethod
    def internal(param_type=None, name=None, nick=None, blurb=None, flags=None):
        """"""
        return object
    
    def finalize(self):
        """"""
        return object
    
    def value_set_default(self, value=None):
        """"""
        return object
    
    def value_validate(self, value=None):
        """"""
        return object
    
    def values_cmp(self, value1=None, value2=None):
        """"""
        return object
    
    def get_blurb(self):
        """"""
        return object
    
    def get_default_value(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_name_quark(self):
        """"""
        return object
    
    def get_nick(self):
        """"""
        return object
    
    def get_qdata(self, quark=None):
        """"""
        return object
    
    def get_redirect_target(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def ref_sink(self):
        """"""
        return object
    
    def set_qdata(self, quark=None, data=None):
        """"""
        return object
    
    def set_qdata_full(self, quark=None, data=None, destroy=None):
        """"""
        return object
    
    def sink(self):
        """"""
        return object
    
    def steal_qdata(self, quark=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def g_type_instance(self):
        return object

    @property
    def name(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def value_type(self):
        return object

    @property
    def owner_type(self):
        return object

    @property
    def _nick(self):
        return object

    @property
    def _blurb(self):
        return object

    @property
    def qdata(self):
        return object

    @property
    def ref_count(self):
        return object

    @property
    def param_id(self):
        return object


class ParamSpecBoolean(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecBoxed(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object


class ParamSpecChar(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecClass():
    """"""

    @property
    def g_type_class(self):
        return object

    @property
    def value_type(self):
        return object

    @property
    def finalize(self):
        return object

    @property
    def value_set_default(self):
        return object

    @property
    def value_validate(self):
        return object

    @property
    def values_cmp(self):
        return object

    @property
    def dummy(self):
        return object


class ParamSpecDouble(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object

    @property
    def epsilon(self):
        return object


class ParamSpecEnum(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def enum_class(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecFlags(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def flags_class(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecFloat(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object

    @property
    def epsilon(self):
        return object


class ParamSpecGType(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def is_a_type(self):
        return object


class ParamSpecInt(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecInt64(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecLong(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecObject(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object


class ParamSpecOverride(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def overridden(self):
        return object


class ParamSpecParam(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object


class ParamSpecPointer(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object


class ParamSpecPool():
    """"""
    
    def insert(self, pspec=None, owner_type=None):
        """"""
        return object
    
    def list(self, owner_type=None, n_pspecs_p=None):
        """"""
        return object
    
    def list_owned(self, owner_type=None):
        """"""
        return object
    
    def lookup(self, param_name=None, owner_type=None, walk_ancestors=None):
        """"""
        return object
    
    def remove(self, pspec=None):
        """"""
        return object
    @staticmethod
    def new(type_prefixing=None):
        """"""
        return object


class ParamSpecString(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def default_value(self):
        return object

    @property
    def cset_first(self):
        return object

    @property
    def cset_nth(self):
        return object

    @property
    def substitutor(self):
        return object

    @property
    def null_fold_if_empty(self):
        return object

    @property
    def ensure_non_null(self):
        return object


class ParamSpecTypeInfo():
    """"""

    @property
    def instance_size(self):
        return object

    @property
    def n_preallocs(self):
        return object

    @property
    def instance_init(self):
        return object

    @property
    def value_type(self):
        return object

    @property
    def finalize(self):
        return object

    @property
    def value_set_default(self):
        return object

    @property
    def value_validate(self):
        return object

    @property
    def values_cmp(self):
        return object


class ParamSpecUChar(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecUInt(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecUInt64(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecULong(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def minimum(self):
        return object

    @property
    def maximum(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecUnichar(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def default_value(self):
        return object


class ParamSpecValueArray(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def element_spec(self):
        return object

    @property
    def fixed_n_elements(self):
        return object


class ParamSpecVariant(ParamSpec):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def type(self):
        return object

    @property
    def default_value(self):
        return object

    @property
    def padding(self):
        return object


class Parameter():
    """"""

    @property
    def name(self):
        return object

    @property
    def value(self):
        return object


class SignalInvocationHint():
    """"""

    @property
    def signal_id(self):
        return object

    @property
    def detail(self):
        return object

    @property
    def run_type(self):
        return object


class SignalQuery():
    """"""

    @property
    def signal_id(self):
        return object

    @property
    def signal_name(self):
        return object

    @property
    def itype(self):
        return object

    @property
    def signal_flags(self):
        return object

    @property
    def return_type(self):
        return object

    @property
    def n_params(self):
        return object

    @property
    def param_types(self):
        return object


class TypeClass():
    """"""
    
    def add_private(self, private_size=None):
        """"""
        return object
    
    def get_instance_private_offset(self):
        """"""
        return object
    
    def get_private(self, private_type=None):
        """"""
        return object
    
    def peek_parent(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def unref_uncached(self):
        """"""
        return object
    @staticmethod
    def adjust_private_offset(g_class=None, private_size_or_offset=None):
        """"""
        return object
    @staticmethod
    def peek(type=None):
        """"""
        return object
    @staticmethod
    def peek_static(type=None):
        """"""
        return object
    @staticmethod
    def ref(type=None):
        """"""
        return object

    @property
    def g_type(self):
        return object


class TypeFundamentalInfo():
    """"""

    @property
    def type_flags(self):
        return object


class TypeInfo():
    """"""

    @property
    def class_size(self):
        return object

    @property
    def base_init(self):
        return object

    @property
    def base_finalize(self):
        return object

    @property
    def class_init(self):
        return object

    @property
    def class_finalize(self):
        return object

    @property
    def class_data(self):
        return object

    @property
    def instance_size(self):
        return object

    @property
    def n_preallocs(self):
        return object

    @property
    def instance_init(self):
        return object

    @property
    def value_table(self):
        return object


class TypeInstance():
    """"""
    
    def get_private(self, private_type=None):
        """"""
        return object

    @property
    def g_class(self):
        return object


class TypeInterface():
    """"""
    
    def peek_parent(self):
        """"""
        return object
    @staticmethod
    def add_prerequisite(interface_type=None, prerequisite_type=None):
        """"""
        return object
    @staticmethod
    def get_plugin(instance_type=None, interface_type=None):
        """"""
        return object
    @staticmethod
    def peek(instance_class=None, iface_type=None):
        """"""
        return object
    @staticmethod
    def prerequisites(interface_type=None, n_prerequisites=None):
        """"""
        return object

    @property
    def g_type(self):
        return object

    @property
    def g_instance_type(self):
        return object


class TypeModuleClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def load(self):
        return object

    @property
    def unload(self):
        return object

    @property
    def reserved1(self):
        return object

    @property
    def reserved2(self):
        return object

    @property
    def reserved3(self):
        return object

    @property
    def reserved4(self):
        return object


class TypePlugin():
    """"""
    
    def complete_interface_info(self, instance_type=None, interface_type=None, info=None):
        """"""
        return object
    
    def complete_type_info(self, g_type=None, info=None, value_table=None):
        """"""
        return object
    
    def unuse(self):
        """"""
        return object
    
    def use(self):
        """"""
        return object


class TypePluginClass():
    """"""

    @property
    def base_iface(self):
        return object

    @property
    def use_plugin(self):
        return object

    @property
    def unuse_plugin(self):
        return object

    @property
    def complete_type_info(self):
        return object

    @property
    def complete_interface_info(self):
        return object


class TypeQuery():
    """"""

    @property
    def type(self):
        return object

    @property
    def type_name(self):
        return object

    @property
    def class_size(self):
        return object

    @property
    def instance_size(self):
        return object


class TypeValueTable():
    """"""
    @staticmethod
    def peek(type=None):
        """"""
        return object

    @property
    def value_init(self):
        return object

    @property
    def value_free(self):
        return object

    @property
    def value_copy(self):
        return object

    @property
    def value_peek_pointer(self):
        return object

    @property
    def collect_format(self):
        return object

    @property
    def collect_value(self):
        return object

    @property
    def lcopy_format(self):
        return object

    @property
    def lcopy_value(self):
        return object


class Value():
    """"""
    
    def copy(self, dest_value=None):
        """"""
        return object
    
    def dup_boxed(self):
        """"""
        return object
    
    def dup_object(self):
        """"""
        return object
    
    def dup_param(self):
        """"""
        return object
    
    def dup_string(self):
        """"""
        return object
    
    def dup_variant(self):
        """"""
        return object
    
    def fits_pointer(self):
        """"""
        return object
    
    def get_boolean(self):
        """"""
        return object
    
    def get_boxed(self):
        """"""
        return object
    
    def get_char(self):
        """"""
        return object
    
    def get_double(self):
        """"""
        return object
    
    def get_enum(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_float(self):
        """"""
        return object
    
    def get_gtype(self):
        """"""
        return object
    
    def get_int(self):
        """"""
        return object
    
    def get_int64(self):
        """"""
        return object
    
    def get_long(self):
        """"""
        return object
    
    def get_object(self):
        """"""
        return object
    
    def get_param(self):
        """"""
        return object
    
    def get_pointer(self):
        """"""
        return object
    
    def get_schar(self):
        """"""
        return object
    
    def get_string(self):
        """"""
        return object
    
    def get_uchar(self):
        """"""
        return object
    
    def get_uint(self):
        """"""
        return object
    
    def get_uint64(self):
        """"""
        return object
    
    def get_ulong(self):
        """"""
        return object
    
    def get_variant(self):
        """"""
        return object
    
    def init(self, g_type=None):
        """"""
        return object
    
    def init_from_instance(self, instance=None):
        """"""
        return object
    
    def peek_pointer(self):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def set_boolean(self, v_boolean=None):
        """"""
        return object
    
    def set_boxed(self, v_boxed=None):
        """"""
        return object
    
    def set_boxed_take_ownership(self, v_boxed=None):
        """"""
        return object
    
    def set_char(self, v_char=None):
        """"""
        return object
    
    def set_double(self, v_double=None):
        """"""
        return object
    
    def set_enum(self, v_enum=None):
        """"""
        return object
    
    def set_flags(self, v_flags=None):
        """"""
        return object
    
    def set_float(self, v_float=None):
        """"""
        return object
    
    def set_gtype(self, v_gtype=None):
        """"""
        return object
    
    def set_instance(self, instance=None):
        """"""
        return object
    
    def set_int(self, v_int=None):
        """"""
        return object
    
    def set_int64(self, v_int64=None):
        """"""
        return object
    
    def set_long(self, v_long=None):
        """"""
        return object
    
    def set_object(self, v_object=None):
        """"""
        return object
    
    def set_object_take_ownership(self, v_object=None):
        """"""
        return object
    
    def set_param(self, param=None):
        """"""
        return object
    
    def set_param_take_ownership(self, param=None):
        """"""
        return object
    
    def set_pointer(self, v_pointer=None):
        """"""
        return object
    
    def set_schar(self, v_char=None):
        """"""
        return object
    
    def set_static_boxed(self, v_boxed=None):
        """"""
        return object
    
    def set_static_string(self, v_string=None):
        """"""
        return object
    
    def set_string(self, v_string=None):
        """"""
        return object
    
    def set_string_take_ownership(self, v_string=None):
        """"""
        return object
    
    def set_uchar(self, v_uchar=None):
        """"""
        return object
    
    def set_uint(self, v_uint=None):
        """"""
        return object
    
    def set_uint64(self, v_uint64=None):
        """"""
        return object
    
    def set_ulong(self, v_ulong=None):
        """"""
        return object
    
    def set_variant(self, variant=None):
        """"""
        return object
    
    def take_boxed(self, v_boxed=None):
        """"""
        return object
    
    def take_object(self, v_object=None):
        """"""
        return object
    
    def take_param(self, param=None):
        """"""
        return object
    
    def take_string(self, v_string=None):
        """"""
        return object
    
    def take_variant(self, variant=None):
        """"""
        return object
    
    def transform(self, dest_value=None):
        """"""
        return object
    
    def unset(self):
        """"""
        return object
    @staticmethod
    def register_transform_func(src_type=None, dest_type=None, transform_func=None):
        """"""
        return object
    @staticmethod
    def type_compatible(src_type=None, dest_type=None):
        """"""
        return object
    @staticmethod
    def type_transformable(src_type=None, dest_type=None):
        """"""
        return object

    @property
    def g_type(self):
        return object

    @property
    def data(self):
        return object


class ValueArray():
    """"""
    
    def __init__(self, n_prealloced=None):
        """"""
        return object
    @staticmethod
    def new(n_prealloced=None):
        """"""
        return object
    
    def append(self, value=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_nth(self, index_=None):
        """"""
        return object
    
    def insert(self, index_=None, value=None):
        """"""
        return object
    
    def prepend(self, value=None):
        """"""
        return object
    
    def remove(self, index_=None):
        """"""
        return object
    
    def sort(self, compare_func=None):
        """"""
        return object
    
    def sort_with_data(self, compare_func=None, user_data=None):
        """"""
        return object

    @property
    def n_values(self):
        return object

    @property
    def values(self):
        return object

    @property
    def n_prealloced(self):
        return object


class WeakRef():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def get(self):
        """"""
        return object
    
    def init(self, object=None):
        """"""
        return object
    
    def set(self, object=None):
        """"""
        return object


class Binding(Object):
    """"""
    
    def get_flags(self):
        """"""
        return object
    
    def get_source(self):
        """"""
        return object
    
    def get_source_property(self):
        """"""
        return object
    
    def get_target(self):
        """"""
        return object
    
    def get_target_property(self):
        """"""
        return object
    
    def unbind(self):
        """"""
        return object


class InitiallyUnowned(Object):
    """"""

    @property
    def g_type_instance(self):
        return object

    @property
    def ref_count(self):
        return object

    @property
    def qdata(self):
        return object


class TypeModule(Object, TypePlugin):
    """"""
    
    def load(self):
        """"""
        return object
    
    def unload(self):
        """"""
        return object
    
    def add_interface(self, instance_type=None, interface_type=None, interface_info=None):
        """"""
        return object
    
    def register_enum(self, name=None, const_static_values=None):
        """"""
        return object
    
    def register_flags(self, name=None, const_static_values=None):
        """"""
        return object
    
    def register_type(self, parent_type=None, type_name=None, type_info=None, flags=None):
        """"""
        return object
    
    def set_name(self, name=None):
        """"""
        return object
    
    def unuse(self):
        """"""
        return object
    
    def use(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def use_count(self):
        return object

    @property
    def type_infos(self):
        return object

    @property
    def interface_infos(self):
        return object

    @property
    def name(self):
        return object
