# -*- coding: utf-8 -*-
from gi.repository import Gst

def buffer_straw_get_buffer(bin=None, pad=None):
    """"""
    return object

def buffer_straw_start_pipeline(bin=None, pad=None):
    """"""
    return object

def buffer_straw_stop_pipeline(bin=None, pad=None):
    """"""
    return object

def check_abi_list(list=None, have_abi_sizes=None):
    """"""
    return object

def check_add_log_filter(log=None, log_level=None, regex=None, func=None, user_data=None, destroy_data=None):
    """"""
    return object

def check_buffer_data(buffer=None, data=None, size=None):
    """"""
    return object

def check_caps_equal(caps1=None, caps2=None):
    """"""
    return object

def check_chain_func(pad=None, parent=None, buffer=None):
    """"""
    return object

def check_clear_log_filter():
    """"""
    return object

def check_drop_buffers():
    """"""
    return object

def check_element_push_buffer(element_name=None, buffer_in=None, caps_in=None, buffer_out=None, caps_out=None):
    """"""
    return object

def check_element_push_buffer_list(element_name=None, buffer_in=None, caps_in=None, buffer_out=None, caps_out=None, last_flow_return=None):
    """"""
    return object

def check_init(argc=None, argv=None):
    """"""
    return object

def check_message_error(message=None, type=None, domain=None, code=None):
    """"""
    return object

def check_object_destroyed_on_unref(object_to_unref=None):
    """"""
    return object

def check_objects_destroyed_on_unref(object_to_unref=None, first_object=None, *args):
    """"""
    return object

def check_remove_log_filter(filter=None):
    """"""
    return object

def check_run_suite(suite=None, name=None, fname=None):
    """"""
    return object

def check_setup_element(factory=None):
    """"""
    return object

def check_setup_events(srcpad=None, element=None, caps=None, format=None):
    """"""
    return object

def check_setup_events_with_stream_id(srcpad=None, element=None, caps=None, format=None, stream_id=None):
    """"""
    return object

def check_setup_sink_pad(element=None, tmpl=None):
    """"""
    return object

def check_setup_sink_pad_by_name(element=None, tmpl=None, name=None):
    """"""
    return object

def check_setup_sink_pad_by_name_from_template(element=None, tmpl=None, name=None):
    """"""
    return object

def check_setup_sink_pad_from_template(element=None, tmpl=None):
    """"""
    return object

def check_setup_src_pad(element=None, tmpl=None):
    """"""
    return object

def check_setup_src_pad_by_name(element=None, tmpl=None, name=None):
    """"""
    return object

def check_setup_src_pad_by_name_from_template(element=None, tmpl=None, name=None):
    """"""
    return object

def check_setup_src_pad_from_template(element=None, tmpl=None):
    """"""
    return object

def check_teardown_element(element=None):
    """"""
    return object

def check_teardown_pad_by_name(element=None, name=None):
    """"""
    return object

def check_teardown_sink_pad(element=None):
    """"""
    return object

def check_teardown_src_pad(element=None):
    """"""
    return object

def consistency_checker_add_pad(consist=None, pad=None):
    """"""
    return object

def consistency_checker_free(consist=None):
    """"""
    return object

def consistency_checker_new(pad=None):
    """"""
    return object

def consistency_checker_reset(consist=None):
    """"""
    return object

def harness_new(element_name=None):
    """"""
    return object

def harness_new_empty():
    """"""
    return object

def harness_new_full(element=None, hsrc=None, element_sinkpad_name=None, hsink=None, element_srcpad_name=None):
    """"""
    return object

def harness_new_parse(launchline=None):
    """"""
    return object

def harness_new_with_element(element=None, element_sinkpad_name=None, element_srcpad_name=None):
    """"""
    return object

def harness_new_with_padnames(element_name=None, element_sinkpad_name=None, element_srcpad_name=None):
    """"""
    return object

def harness_new_with_templates(element_name=None, hsrc=None, hsink=None):
    """"""
    return object

def harness_stress_thread_stop(t=None):
    """"""
    return object


class CheckABIStruct():
    """"""

    @property
    def name(self):
        return object

    @property
    def size(self):
        return object

    @property
    def abi_size(self):
        return object


class CheckLogFilter():
    """"""


class Harness():
    """"""
    
    def add_element_full(self, element=None, hsrc=None, element_sinkpad_name=None, hsink=None, element_srcpad_name=None):
        """"""
        return object
    
    def add_element_sink_pad(self, sinkpad=None):
        """"""
        return object
    
    def add_element_src_pad(self, srcpad=None):
        """"""
        return object
    
    def add_parse(self, launchline=None):
        """"""
        return object
    
    def add_probe(self, element_name=None, pad_name=None, mask=None, callback=None, user_data=None, destroy_data=None):
        """"""
        return object
    
    def add_sink(self, sink_element_name=None):
        """"""
        return object
    
    def add_sink_harness(self, sink_harness=None):
        """"""
        return object
    
    def add_sink_parse(self, launchline=None):
        """"""
        return object
    
    def add_src(self, src_element_name=None, has_clock_wait=None):
        """"""
        return object
    
    def add_src_harness(self, src_harness=None, has_clock_wait=None):
        """"""
        return object
    
    def add_src_parse(self, launchline=None, has_clock_wait=None):
        """"""
        return object
    
    def buffers_in_queue(self):
        """"""
        return object
    
    def buffers_received(self):
        """"""
        return object
    
    def crank_multiple_clock_waits(self, waits=None):
        """"""
        return object
    
    def crank_single_clock_wait(self):
        """"""
        return object
    
    def create_buffer(self, size=None):
        """"""
        return object
    
    def dump_to_file(self, filename=None):
        """"""
        return object
    
    def events_in_queue(self):
        """"""
        return object
    
    def events_received(self):
        """"""
        return object
    
    def find_element(self, element_name=None):
        """"""
        return object
    
    def get(self, element_name=None, first_property_name=None, *args):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_last_pushed_timestamp(self):
        """"""
        return object
    
    def get_testclock(self):
        """"""
        return object
    
    def play(self):
        """"""
        return object
    
    def pull(self):
        """"""
        return object
    
    def pull_event(self):
        """"""
        return object
    
    def pull_upstream_event(self):
        """"""
        return object
    
    def push(self, buffer=None):
        """"""
        return object
    
    def push_and_pull(self, buffer=None):
        """"""
        return object
    
    def push_event(self, event=None):
        """"""
        return object
    
    def push_from_src(self):
        """"""
        return object
    
    def push_to_sink(self):
        """"""
        return object
    
    def push_upstream_event(self, event=None):
        """"""
        return object
    
    def query_latency(self):
        """"""
        return object
    
    def set(self, element_name=None, first_property_name=None, *args):
        """"""
        return object
    
    def set_blocking_push_mode(self):
        """"""
        return object
    
    def set_caps(self, _in=None, out=None):
        """"""
        return object
    
    def set_caps_str(self, _in=None, out=None):
        """"""
        return object
    
    def set_drop_buffers(self, drop_buffers=None):
        """"""
        return object
    
    def set_forwarding(self, forwarding=None):
        """"""
        return object
    
    def set_propose_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def set_sink_caps(self, caps=None):
        """"""
        return object
    
    def set_sink_caps_str(self, str=None):
        """"""
        return object
    
    def set_src_caps(self, caps=None):
        """"""
        return object
    
    def set_src_caps_str(self, str=None):
        """"""
        return object
    
    def set_time(self, time=None):
        """"""
        return object
    
    def set_upstream_latency(self, latency=None):
        """"""
        return object
    
    def sink_push_many(self, pushes=None):
        """"""
        return object
    
    def src_crank_and_push_many(self, cranks=None, pushes=None):
        """"""
        return object
    
    def src_push_event(self):
        """"""
        return object
    
    def stress_custom_start(self, init=None, callback=None, data=None, sleep=None):
        """"""
        return object
    
    def stress_property_start_full(self, name=None, value=None, sleep=None):
        """"""
        return object
    
    def stress_push_buffer_start_full(self, caps=None, segment=None, buf=None, sleep=None):
        """"""
        return object
    
    def stress_push_buffer_with_cb_start_full(self, caps=None, segment=None, func=None, data=None, notify=None, sleep=None):
        """"""
        return object
    
    def stress_push_event_start_full(self, event=None, sleep=None):
        """"""
        return object
    
    def stress_push_event_with_cb_start_full(self, func=None, data=None, notify=None, sleep=None):
        """"""
        return object
    
    def stress_push_upstream_event_start_full(self, event=None, sleep=None):
        """"""
        return object
    
    def stress_push_upstream_event_with_cb_start_full(self, func=None, data=None, notify=None, sleep=None):
        """"""
        return object
    
    def stress_requestpad_start_full(self, templ=None, name=None, caps=None, release=None, sleep=None):
        """"""
        return object
    
    def stress_statechange_start_full(self, sleep=None):
        """"""
        return object
    
    def take_all_data(self, size=None):
        """"""
        return object
    
    def take_all_data_as_buffer(self):
        """"""
        return object
    
    def take_all_data_as_bytes(self):
        """"""
        return object
    
    def teardown(self):
        """"""
        return object
    
    def try_pull(self):
        """"""
        return object
    
    def try_pull_event(self):
        """"""
        return object
    
    def try_pull_upstream_event(self):
        """"""
        return object
    
    def upstream_events_in_queue(self):
        """"""
        return object
    
    def upstream_events_received(self):
        """"""
        return object
    
    def use_systemclock(self):
        """"""
        return object
    
    def use_testclock(self):
        """"""
        return object
    
    def wait_for_clock_id_waits(self, waits=None, timeout=None):
        """"""
        return object
    @staticmethod
    def new(element_name=None):
        """"""
        return object
    @staticmethod
    def new_empty():
        """"""
        return object
    @staticmethod
    def new_full(element=None, hsrc=None, element_sinkpad_name=None, hsink=None, element_srcpad_name=None):
        """"""
        return object
    @staticmethod
    def new_parse(launchline=None):
        """"""
        return object
    @staticmethod
    def new_with_element(element=None, element_sinkpad_name=None, element_srcpad_name=None):
        """"""
        return object
    @staticmethod
    def new_with_padnames(element_name=None, element_sinkpad_name=None, element_srcpad_name=None):
        """"""
        return object
    @staticmethod
    def new_with_templates(element_name=None, hsrc=None, hsink=None):
        """"""
        return object
    @staticmethod
    def stress_thread_stop(t=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def srcpad(self):
        return object

    @property
    def sinkpad(self):
        return object

    @property
    def src_harness(self):
        return object

    @property
    def sink_harness(self):
        return object

    @property
    def priv(self):
        return object


class HarnessPrivate():
    """"""


class HarnessThread():
    """"""


class StreamConsistency():
    """"""


class TestClock(Gst.Clock):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_with_start_time(start_time=None):
        """"""
        return object
    @staticmethod
    def id_list_get_latest_time(pending_list=None):
        """"""
        return object
    
    def advance_time(self, delta=None):
        """"""
        return object
    
    def crank(self):
        """"""
        return object
    
    def get_next_entry_time(self):
        """"""
        return object
    
    def has_id(self, id=None):
        """"""
        return object
    
    def peek_id_count(self):
        """"""
        return object
    
    def peek_next_pending_id(self, pending_id=None):
        """"""
        return object
    
    def process_id_list(self, pending_list=None):
        """"""
        return object
    
    def process_next_clock_id(self):
        """"""
        return object
    
    def set_time(self, new_time=None):
        """"""
        return object
    
    def wait_for_multiple_pending_ids(self, count=None, pending_list=None):
        """"""
        return object
    
    def wait_for_next_pending_id(self, pending_id=None):
        """"""
        return object
    
    def wait_for_pending_id_count(self, count=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object


class TestClockClass():
    """"""

    @property
    def parent_class(self):
        return object


class TestClockPrivate():
    """"""
