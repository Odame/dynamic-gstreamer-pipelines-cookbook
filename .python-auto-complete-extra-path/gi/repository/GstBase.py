# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import Gst
BASE_PARSE_FLAG_DRAINING = r"""2"""
BASE_PARSE_FLAG_LOST_SYNC = r"""1"""
BASE_TRANSFORM_SINK_NAME = r"""sink"""
BASE_TRANSFORM_SRC_NAME = r"""src"""


class BaseParseFrameFlags:
    """"""
    NONE = 0
    NEW_FRAME = 1
    NO_FRAME = 2
    CLIP = 4
    DROP = 8
    QUEUE = 16


class BaseSrcFlags:
    """"""
    STARTING = 16384
    STARTED = 32768
    LAST = 1048576


class CollectPadsStateFlags:
    """"""
    EOS = 1
    FLUSHING = 2
    NEW_SEGMENT = 4
    WAITING = 8
    LOCKED = 16

def bit_reader_new(data=None, size=None):
    """"""
    return object

def byte_reader_new(data=None, size=None):
    """"""
    return object

def byte_writer_new():
    """"""
    return object

def byte_writer_new_with_data(data=None, size=None, initialized=None):
    """"""
    return object

def byte_writer_new_with_size(size=None, fixed=None):
    """"""
    return object

def queue_array_new(initial_size=None):
    """"""
    return object

def queue_array_new_for_struct(struct_size=None, initial_size=None):
    """"""
    return object

def type_find_helper(src=None, size=None):
    """"""
    return object

def type_find_helper_for_buffer(obj=None, buf=None, prob=None):
    """"""
    return object

def type_find_helper_for_data(obj=None, data=None, size=None, prob=None):
    """"""
    return object

def type_find_helper_for_extension(obj=None, extension=None):
    """"""
    return object

def type_find_helper_get_range(obj=None, parent=None, func=None, size=None, extension=None, prob=None):
    """"""
    return object

def type_find_helper_get_range_full(obj=None, parent=None, func=None, size=None, extension=None, caps=None, prob=None):
    """"""
    return object


class Adapter(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def available(self):
        """"""
        return object
    
    def available_fast(self):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def copy(self, dest=None, offset=None, size=None):
        """"""
        return object
    
    def copy_bytes(self, offset=None, size=None):
        """"""
        return object
    
    def distance_from_discont(self):
        """"""
        return object
    
    def dts_at_discont(self):
        """"""
        return object
    
    def flush(self, flush=None):
        """"""
        return object
    
    def get_buffer(self, nbytes=None):
        """"""
        return object
    
    def get_buffer_fast(self, nbytes=None):
        """"""
        return object
    
    def get_buffer_list(self, nbytes=None):
        """"""
        return object
    
    def get_list(self, nbytes=None):
        """"""
        return object
    
    def map(self, size=None):
        """"""
        return object
    
    def masked_scan_uint32(self, mask=None, pattern=None, offset=None, size=None):
        """"""
        return object
    
    def masked_scan_uint32_peek(self, mask=None, pattern=None, offset=None, size=None, value=None):
        """"""
        return object
    
    def offset_at_discont(self):
        """"""
        return object
    
    def prev_dts(self, distance=None):
        """"""
        return object
    
    def prev_dts_at_offset(self, offset=None, distance=None):
        """"""
        return object
    
    def prev_offset(self, distance=None):
        """"""
        return object
    
    def prev_pts(self, distance=None):
        """"""
        return object
    
    def prev_pts_at_offset(self, offset=None, distance=None):
        """"""
        return object
    
    def pts_at_discont(self):
        """"""
        return object
    
    def push(self, buf=None):
        """"""
        return object
    
    def take(self, nbytes=None):
        """"""
        return object
    
    def take_buffer(self, nbytes=None):
        """"""
        return object
    
    def take_buffer_fast(self, nbytes=None):
        """"""
        return object
    
    def take_buffer_list(self, nbytes=None):
        """"""
        return object
    
    def take_list(self, nbytes=None):
        """"""
        return object
    
    def unmap(self):
        """"""
        return object


class AdapterClass():
    """"""


class Aggregator(Gst.Element):
    """"""
    
    def aggregate(self, timeout=None):
        """"""
        return object
    
    def clip(self, aggregator_pad=None, buf=None):
        """"""
        return object
    
    def create_new_pad(self, templ=None, req_name=None, caps=None):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def finish_buffer(self, buffer=None):
        """"""
        return object
    
    def fixate_src_caps(self, caps=None):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def get_next_time(self):
        """"""
        return object
    
    def negotiated_src_caps(self, caps=None):
        """"""
        return object
    
    def propose_allocation(self, pad=None, decide_query=None, query=None):
        """"""
        return object
    
    def sink_event(self, aggregator_pad=None, event=None):
        """"""
        return object
    
    def sink_query(self, aggregator_pad=None, query=None):
        """"""
        return object
    
    def src_activate(self, mode=None, active=None):
        """"""
        return object
    
    def src_event(self, event=None):
        """"""
        return object
    
    def src_query(self, query=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def update_src_caps(self, caps=None, ret=None):
        """"""
        return object
    
    def finish_buffer(self, buffer=None):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_buffer_pool(self):
        """"""
        return object
    
    def get_latency(self):
        """"""
        return object
    
    def set_latency(self, min_latency=None, max_latency=None):
        """"""
        return object
    
    def set_src_caps(self, caps=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def srcpad(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AggregatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def clip(self):
        return object

    @property
    def finish_buffer(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def sink_query(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def src_query(self):
        return object

    @property
    def src_activate(self):
        return object

    @property
    def aggregate(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def start(self):
        return object

    @property
    def get_next_time(self):
        return object

    @property
    def create_new_pad(self):
        return object

    @property
    def update_src_caps(self):
        return object

    @property
    def fixate_src_caps(self):
        return object

    @property
    def negotiated_src_caps(self):
        return object

    @property
    def decide_allocation(self):
        return object

    @property
    def propose_allocation(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AggregatorPad(Gst.Pad):
    """"""
    
    def flush(self, aggregator=None):
        """"""
        return object
    
    def skip_buffer(self, aggregator=None, buffer=None):
        """"""
        return object
    
    def drop_buffer(self):
        """"""
        return object
    
    def has_buffer(self):
        """"""
        return object
    
    def is_eos(self):
        """"""
        return object
    
    def peek_buffer(self):
        """"""
        return object
    
    def pop_buffer(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AggregatorPadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def skip_buffer(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AggregatorPadPrivate():
    """"""


class AggregatorPrivate():
    """"""


class BaseParse(Gst.Element):
    """"""
    
    def convert(self, src_format=None, src_value=None, dest_format=None, dest_value=None):
        """"""
        return object
    
    def detect(self, buffer=None):
        """"""
        return object
    
    def get_sink_caps(self, filter=None):
        """"""
        return object
    
    def handle_frame(self, frame=None, skipsize=None):
        """"""
        return object
    
    def pre_push_frame(self, frame=None):
        """"""
        return object
    
    def set_sink_caps(self, caps=None):
        """"""
        return object
    
    def sink_event(self, event=None):
        """"""
        return object
    
    def sink_query(self, query=None):
        """"""
        return object
    
    def src_event(self, event=None):
        """"""
        return object
    
    def src_query(self, query=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def add_index_entry(self, offset=None, ts=None, key=None, force=None):
        """"""
        return object
    
    def convert_default(self, src_format=None, src_value=None, dest_format=None, dest_value=None):
        """"""
        return object
    
    def drain(self):
        """"""
        return object
    
    def finish_frame(self, frame=None, size=None):
        """"""
        return object
    
    def merge_tags(self, tags=None, mode=None):
        """"""
        return object
    
    def push_frame(self, frame=None):
        """"""
        return object
    
    def set_average_bitrate(self, bitrate=None):
        """"""
        return object
    
    def set_duration(self, fmt=None, duration=None, interval=None):
        """"""
        return object
    
    def set_frame_rate(self, fps_num=None, fps_den=None, lead_in=None, lead_out=None):
        """"""
        return object
    
    def set_has_timing_info(self, has_timing=None):
        """"""
        return object
    
    def set_infer_ts(self, infer_ts=None):
        """"""
        return object
    
    def set_latency(self, min_latency=None, max_latency=None):
        """"""
        return object
    
    def set_min_frame_size(self, min_size=None):
        """"""
        return object
    
    def set_passthrough(self, passthrough=None):
        """"""
        return object
    
    def set_pts_interpolation(self, pts_interpolate=None):
        """"""
        return object
    
    def set_syncable(self, syncable=None):
        """"""
        return object
    
    def set_ts_at_offset(self, offset=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def sinkpad(self):
        return object

    @property
    def srcpad(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def _gst_reserved(self):
        return object

    @property
    def priv(self):
        return object


class BaseParseClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def set_sink_caps(self):
        return object

    @property
    def handle_frame(self):
        return object

    @property
    def pre_push_frame(self):
        return object

    @property
    def convert(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def get_sink_caps(self):
        return object

    @property
    def detect(self):
        return object

    @property
    def sink_query(self):
        return object

    @property
    def src_query(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseParseFrame():
    """"""
    
    def __init__(self, buffer=None, flags=None, overhead=None):
        """"""
        return object
    @staticmethod
    def new(buffer=None, flags=None, overhead=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object

    @property
    def buffer(self):
        return object

    @property
    def out_buffer(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def overhead(self):
        return object

    @property
    def size(self):
        return object

    @property
    def _gst_reserved_i(self):
        return object

    @property
    def _gst_reserved_p(self):
        return object

    @property
    def _private_flags(self):
        return object


class BaseParsePrivate():
    """"""


class BaseSink(Gst.Element):
    """"""
    
    def activate_pull(self, active=None):
        """"""
        return object
    
    def event(self, event=None):
        """"""
        return object
    
    def fixate(self, caps=None):
        """"""
        return object
    
    def get_caps(self, filter=None):
        """"""
        return object
    
    def get_times(self, buffer=None, start=None, end=None):
        """"""
        return object
    
    def prepare(self, buffer=None):
        """"""
        return object
    
    def prepare_list(self, buffer_list=None):
        """"""
        return object
    
    def preroll(self, buffer=None):
        """"""
        return object
    
    def propose_allocation(self, query=None):
        """"""
        return object
    
    def query(self, query=None):
        """"""
        return object
    
    def render(self, buffer=None):
        """"""
        return object
    
    def render_list(self, buffer_list=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def unlock(self):
        """"""
        return object
    
    def unlock_stop(self):
        """"""
        return object
    
    def wait_event(self, event=None):
        """"""
        return object
    
    def do_preroll(self, obj=None):
        """"""
        return object
    
    def get_blocksize(self):
        """"""
        return object
    
    def get_drop_out_of_segment(self):
        """"""
        return object
    
    def get_last_sample(self):
        """"""
        return object
    
    def get_latency(self):
        """"""
        return object
    
    def get_max_bitrate(self):
        """"""
        return object
    
    def get_max_lateness(self):
        """"""
        return object
    
    def get_render_delay(self):
        """"""
        return object
    
    def get_sync(self):
        """"""
        return object
    
    def get_throttle_time(self):
        """"""
        return object
    
    def get_ts_offset(self):
        """"""
        return object
    
    def is_async_enabled(self):
        """"""
        return object
    
    def is_last_sample_enabled(self):
        """"""
        return object
    
    def is_qos_enabled(self):
        """"""
        return object
    
    def query_latency(self, live=None, upstream_live=None, min_latency=None, max_latency=None):
        """"""
        return object
    
    def set_async_enabled(self, enabled=None):
        """"""
        return object
    
    def set_blocksize(self, blocksize=None):
        """"""
        return object
    
    def set_drop_out_of_segment(self, drop_out_of_segment=None):
        """"""
        return object
    
    def set_last_sample_enabled(self, enabled=None):
        """"""
        return object
    
    def set_max_bitrate(self, max_bitrate=None):
        """"""
        return object
    
    def set_max_lateness(self, max_lateness=None):
        """"""
        return object
    
    def set_qos_enabled(self, enabled=None):
        """"""
        return object
    
    def set_render_delay(self, delay=None):
        """"""
        return object
    
    def set_sync(self, sync=None):
        """"""
        return object
    
    def set_throttle_time(self, throttle=None):
        """"""
        return object
    
    def set_ts_offset(self, offset=None):
        """"""
        return object
    
    def wait(self, time=None, jitter=None):
        """"""
        return object
    
    def wait_clock(self, time=None, jitter=None):
        """"""
        return object
    
    def wait_preroll(self):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def sinkpad(self):
        return object

    @property
    def pad_mode(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def can_activate_pull(self):
        return object

    @property
    def can_activate_push(self):
        return object

    @property
    def preroll_lock(self):
        return object

    @property
    def preroll_cond(self):
        return object

    @property
    def eos(self):
        return object

    @property
    def need_preroll(self):
        return object

    @property
    def have_preroll(self):
        return object

    @property
    def playing_async(self):
        return object

    @property
    def have_newsegment(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def clock_id(self):
        return object

    @property
    def sync(self):
        return object

    @property
    def flushing(self):
        return object

    @property
    def running(self):
        return object

    @property
    def max_lateness(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseSinkClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_caps(self):
        return object

    @property
    def set_caps(self):
        return object

    @property
    def fixate(self):
        return object

    @property
    def activate_pull(self):
        return object

    @property
    def get_times(self):
        return object

    @property
    def propose_allocation(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def unlock(self):
        return object

    @property
    def unlock_stop(self):
        return object

    @property
    def query(self):
        return object

    @property
    def event(self):
        return object

    @property
    def wait_event(self):
        return object

    @property
    def prepare(self):
        return object

    @property
    def prepare_list(self):
        return object

    @property
    def preroll(self):
        return object

    @property
    def render(self):
        return object

    @property
    def render_list(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseSinkPrivate():
    """"""


class BaseSrc(Gst.Element):
    """"""
    
    def alloc(self, offset=None, size=None, buf=None):
        """"""
        return object
    
    def create(self, offset=None, size=None, buf=None):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def do_seek(self, segment=None):
        """"""
        return object
    
    def event(self, event=None):
        """"""
        return object
    
    def fill(self, offset=None, size=None, buf=None):
        """"""
        return object
    
    def fixate(self, caps=None):
        """"""
        return object
    
    def get_caps(self, filter=None):
        """"""
        return object
    
    def get_size(self, size=None):
        """"""
        return object
    
    def get_times(self, buffer=None, start=None, end=None):
        """"""
        return object
    
    def is_seekable(self):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def prepare_seek_segment(self, seek=None, segment=None):
        """"""
        return object
    
    def query(self, query=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def unlock(self):
        """"""
        return object
    
    def unlock_stop(self):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_blocksize(self):
        """"""
        return object
    
    def get_buffer_pool(self):
        """"""
        return object
    
    def get_do_timestamp(self):
        """"""
        return object
    
    def is_async(self):
        """"""
        return object
    
    def is_live(self):
        """"""
        return object
    
    def new_seamless_segment(self, start=None, stop=None, time=None):
        """"""
        return object
    
    def query_latency(self, live=None, min_latency=None, max_latency=None):
        """"""
        return object
    
    def set_async(self, async=None):
        """"""
        return object
    
    def set_automatic_eos(self, automatic_eos=None):
        """"""
        return object
    
    def set_blocksize(self, blocksize=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def set_do_timestamp(self, timestamp=None):
        """"""
        return object
    
    def set_dynamic_size(self, dynamic=None):
        """"""
        return object
    
    def set_format(self, format=None):
        """"""
        return object
    
    def set_live(self, live=None):
        """"""
        return object
    
    def start_complete(self, ret=None):
        """"""
        return object
    
    def start_wait(self):
        """"""
        return object
    
    def submit_buffer_list(self, buffer_list=None):
        """"""
        return object
    
    def wait_playing(self):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def srcpad(self):
        return object

    @property
    def live_lock(self):
        return object

    @property
    def live_cond(self):
        return object

    @property
    def is_live(self):
        return object

    @property
    def live_running(self):
        return object

    @property
    def blocksize(self):
        return object

    @property
    def can_activate_push(self):
        return object

    @property
    def random_access(self):
        return object

    @property
    def clock_id(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def need_newsegment(self):
        return object

    @property
    def num_buffers(self):
        return object

    @property
    def num_buffers_left(self):
        return object

    @property
    def typefind(self):
        return object

    @property
    def running(self):
        return object

    @property
    def pending_seek(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseSrcClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_caps(self):
        return object

    @property
    def negotiate(self):
        return object

    @property
    def fixate(self):
        return object

    @property
    def set_caps(self):
        return object

    @property
    def decide_allocation(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def get_times(self):
        return object

    @property
    def get_size(self):
        return object

    @property
    def is_seekable(self):
        return object

    @property
    def prepare_seek_segment(self):
        return object

    @property
    def do_seek(self):
        return object

    @property
    def unlock(self):
        return object

    @property
    def unlock_stop(self):
        return object

    @property
    def query(self):
        return object

    @property
    def event(self):
        return object

    @property
    def create(self):
        return object

    @property
    def alloc(self):
        return object

    @property
    def fill(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseSrcPrivate():
    """"""


class BaseTransform(Gst.Element):
    """"""
    
    def accept_caps(self, direction=None, caps=None):
        """"""
        return object
    
    def before_transform(self, buffer=None):
        """"""
        return object
    
    def copy_metadata(self, input=None, outbuf=None):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def filter_meta(self, query=None, api=None, params=None):
        """"""
        return object
    
    def fixate_caps(self, direction=None, caps=None, othercaps=None):
        """"""
        return object
    
    def generate_output(self, outbuf=None):
        """"""
        return object
    
    def get_unit_size(self, caps=None, size=None):
        """"""
        return object
    
    def prepare_output_buffer(self, input=None, outbuf=None):
        """"""
        return object
    
    def propose_allocation(self, decide_query=None, query=None):
        """"""
        return object
    
    def query(self, direction=None, query=None):
        """"""
        return object
    
    def set_caps(self, incaps=None, outcaps=None):
        """"""
        return object
    
    def sink_event(self, event=None):
        """"""
        return object
    
    def src_event(self, event=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def submit_input_buffer(self, is_discont=None, input=None):
        """"""
        return object
    
    def transform(self, inbuf=None, outbuf=None):
        """"""
        return object
    
    def transform_caps(self, direction=None, caps=None, filter=None):
        """"""
        return object
    
    def transform_ip(self, buf=None):
        """"""
        return object
    
    def transform_meta(self, outbuf=None, meta=None, inbuf=None):
        """"""
        return object
    
    def transform_size(self, direction=None, caps=None, size=None, othercaps=None, othersize=None):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_buffer_pool(self):
        """"""
        return object
    
    def is_in_place(self):
        """"""
        return object
    
    def is_passthrough(self):
        """"""
        return object
    
    def is_qos_enabled(self):
        """"""
        return object
    
    def reconfigure_sink(self):
        """"""
        return object
    
    def reconfigure_src(self):
        """"""
        return object
    
    def set_gap_aware(self, gap_aware=None):
        """"""
        return object
    
    def set_in_place(self, in_place=None):
        """"""
        return object
    
    def set_passthrough(self, passthrough=None):
        """"""
        return object
    
    def set_prefer_passthrough(self, prefer_passthrough=None):
        """"""
        return object
    
    def set_qos_enabled(self, enabled=None):
        """"""
        return object
    
    def update_qos(self, proportion=None, diff=None, timestamp=None):
        """"""
        return object
    
    def update_src_caps(self, updated_caps=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def sinkpad(self):
        return object

    @property
    def srcpad(self):
        return object

    @property
    def have_segment(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def queued_buf(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseTransformClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def passthrough_on_same_caps(self):
        return object

    @property
    def transform_ip_on_passthrough(self):
        return object

    @property
    def transform_caps(self):
        return object

    @property
    def fixate_caps(self):
        return object

    @property
    def accept_caps(self):
        return object

    @property
    def set_caps(self):
        return object

    @property
    def query(self):
        return object

    @property
    def decide_allocation(self):
        return object

    @property
    def filter_meta(self):
        return object

    @property
    def propose_allocation(self):
        return object

    @property
    def transform_size(self):
        return object

    @property
    def get_unit_size(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def prepare_output_buffer(self):
        return object

    @property
    def copy_metadata(self):
        return object

    @property
    def transform_meta(self):
        return object

    @property
    def before_transform(self):
        return object

    @property
    def transform(self):
        return object

    @property
    def transform_ip(self):
        return object

    @property
    def submit_input_buffer(self):
        return object

    @property
    def generate_output(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BaseTransformPrivate():
    """"""


class BitReader():
    """"""
    
    def free(self):
        """"""
        return object
    
    def get_bits_uint16(self, val=None, nbits=None):
        """"""
        return object
    
    def get_bits_uint32(self, val=None, nbits=None):
        """"""
        return object
    
    def get_bits_uint64(self, val=None, nbits=None):
        """"""
        return object
    
    def get_bits_uint8(self, val=None, nbits=None):
        """"""
        return object
    
    def get_pos(self):
        """"""
        return object
    
    def get_remaining(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def init(self, data=None, size=None):
        """"""
        return object
    
    def peek_bits_uint16(self, val=None, nbits=None):
        """"""
        return object
    
    def peek_bits_uint32(self, val=None, nbits=None):
        """"""
        return object
    
    def peek_bits_uint64(self, val=None, nbits=None):
        """"""
        return object
    
    def peek_bits_uint8(self, val=None, nbits=None):
        """"""
        return object
    
    def set_pos(self, pos=None):
        """"""
        return object
    
    def skip(self, nbits=None):
        """"""
        return object
    
    def skip_to_byte(self):
        """"""
        return object
    @staticmethod
    def new(data=None, size=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def size(self):
        return object

    @property
    def byte(self):
        return object

    @property
    def bit(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ByteReader():
    """"""
    
    def dup_data(self, size=None, val=None):
        """"""
        return object
    
    def dup_string_utf16(self, str=None):
        """"""
        return object
    
    def dup_string_utf32(self, str=None):
        """"""
        return object
    
    def dup_string_utf8(self, str=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_data(self, size=None, val=None):
        """"""
        return object
    
    def get_float32_be(self, val=None):
        """"""
        return object
    
    def get_float32_le(self, val=None):
        """"""
        return object
    
    def get_float64_be(self, val=None):
        """"""
        return object
    
    def get_float64_le(self, val=None):
        """"""
        return object
    
    def get_int16_be(self, val=None):
        """"""
        return object
    
    def get_int16_le(self, val=None):
        """"""
        return object
    
    def get_int24_be(self, val=None):
        """"""
        return object
    
    def get_int24_le(self, val=None):
        """"""
        return object
    
    def get_int32_be(self, val=None):
        """"""
        return object
    
    def get_int32_le(self, val=None):
        """"""
        return object
    
    def get_int64_be(self, val=None):
        """"""
        return object
    
    def get_int64_le(self, val=None):
        """"""
        return object
    
    def get_int8(self, val=None):
        """"""
        return object
    
    def get_pos(self):
        """"""
        return object
    
    def get_remaining(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def get_string_utf8(self, str=None):
        """"""
        return object
    
    def get_sub_reader(self, sub_reader=None, size=None):
        """"""
        return object
    
    def get_uint16_be(self, val=None):
        """"""
        return object
    
    def get_uint16_le(self, val=None):
        """"""
        return object
    
    def get_uint24_be(self, val=None):
        """"""
        return object
    
    def get_uint24_le(self, val=None):
        """"""
        return object
    
    def get_uint32_be(self, val=None):
        """"""
        return object
    
    def get_uint32_le(self, val=None):
        """"""
        return object
    
    def get_uint64_be(self, val=None):
        """"""
        return object
    
    def get_uint64_le(self, val=None):
        """"""
        return object
    
    def get_uint8(self, val=None):
        """"""
        return object
    
    def init(self, data=None, size=None):
        """"""
        return object
    
    def masked_scan_uint32(self, mask=None, pattern=None, offset=None, size=None):
        """"""
        return object
    
    def masked_scan_uint32_peek(self, mask=None, pattern=None, offset=None, size=None, value=None):
        """"""
        return object
    
    def peek_data(self, size=None, val=None):
        """"""
        return object
    
    def peek_float32_be(self, val=None):
        """"""
        return object
    
    def peek_float32_le(self, val=None):
        """"""
        return object
    
    def peek_float64_be(self, val=None):
        """"""
        return object
    
    def peek_float64_le(self, val=None):
        """"""
        return object
    
    def peek_int16_be(self, val=None):
        """"""
        return object
    
    def peek_int16_le(self, val=None):
        """"""
        return object
    
    def peek_int24_be(self, val=None):
        """"""
        return object
    
    def peek_int24_le(self, val=None):
        """"""
        return object
    
    def peek_int32_be(self, val=None):
        """"""
        return object
    
    def peek_int32_le(self, val=None):
        """"""
        return object
    
    def peek_int64_be(self, val=None):
        """"""
        return object
    
    def peek_int64_le(self, val=None):
        """"""
        return object
    
    def peek_int8(self, val=None):
        """"""
        return object
    
    def peek_string_utf8(self, str=None):
        """"""
        return object
    
    def peek_sub_reader(self, sub_reader=None, size=None):
        """"""
        return object
    
    def peek_uint16_be(self, val=None):
        """"""
        return object
    
    def peek_uint16_le(self, val=None):
        """"""
        return object
    
    def peek_uint24_be(self, val=None):
        """"""
        return object
    
    def peek_uint24_le(self, val=None):
        """"""
        return object
    
    def peek_uint32_be(self, val=None):
        """"""
        return object
    
    def peek_uint32_le(self, val=None):
        """"""
        return object
    
    def peek_uint64_be(self, val=None):
        """"""
        return object
    
    def peek_uint64_le(self, val=None):
        """"""
        return object
    
    def peek_uint8(self, val=None):
        """"""
        return object
    
    def set_pos(self, pos=None):
        """"""
        return object
    
    def skip(self, nbytes=None):
        """"""
        return object
    
    def skip_string_utf16(self):
        """"""
        return object
    
    def skip_string_utf32(self):
        """"""
        return object
    
    def skip_string_utf8(self):
        """"""
        return object
    @staticmethod
    def new(data=None, size=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def size(self):
        return object

    @property
    def byte(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ByteWriter():
    """"""
    
    def ensure_free_space(self, size=None):
        """"""
        return object
    
    def fill(self, value=None, size=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def free_and_get_buffer(self):
        """"""
        return object
    
    def free_and_get_data(self):
        """"""
        return object
    
    def get_remaining(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def init_with_data(self, data=None, size=None, initialized=None):
        """"""
        return object
    
    def init_with_size(self, size=None, fixed=None):
        """"""
        return object
    
    def put_buffer(self, buffer=None, offset=None, size=None):
        """"""
        return object
    
    def put_data(self, data=None, size=None):
        """"""
        return object
    
    def put_float32_be(self, val=None):
        """"""
        return object
    
    def put_float32_le(self, val=None):
        """"""
        return object
    
    def put_float64_be(self, val=None):
        """"""
        return object
    
    def put_float64_le(self, val=None):
        """"""
        return object
    
    def put_int16_be(self, val=None):
        """"""
        return object
    
    def put_int16_le(self, val=None):
        """"""
        return object
    
    def put_int24_be(self, val=None):
        """"""
        return object
    
    def put_int24_le(self, val=None):
        """"""
        return object
    
    def put_int32_be(self, val=None):
        """"""
        return object
    
    def put_int32_le(self, val=None):
        """"""
        return object
    
    def put_int64_be(self, val=None):
        """"""
        return object
    
    def put_int64_le(self, val=None):
        """"""
        return object
    
    def put_int8(self, val=None):
        """"""
        return object
    
    def put_string_utf16(self, data=None):
        """"""
        return object
    
    def put_string_utf32(self, data=None):
        """"""
        return object
    
    def put_string_utf8(self, data=None):
        """"""
        return object
    
    def put_uint16_be(self, val=None):
        """"""
        return object
    
    def put_uint16_le(self, val=None):
        """"""
        return object
    
    def put_uint24_be(self, val=None):
        """"""
        return object
    
    def put_uint24_le(self, val=None):
        """"""
        return object
    
    def put_uint32_be(self, val=None):
        """"""
        return object
    
    def put_uint32_le(self, val=None):
        """"""
        return object
    
    def put_uint64_be(self, val=None):
        """"""
        return object
    
    def put_uint64_le(self, val=None):
        """"""
        return object
    
    def put_uint8(self, val=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def reset_and_get_buffer(self):
        """"""
        return object
    
    def reset_and_get_data(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_with_data(data=None, size=None, initialized=None):
        """"""
        return object
    @staticmethod
    def new_with_size(size=None, fixed=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def alloc_size(self):
        return object

    @property
    def fixed(self):
        return object

    @property
    def owned(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class CollectData():
    """"""

    @property
    def collect(self):
        return object

    @property
    def pad(self):
        return object

    @property
    def buffer(self):
        return object

    @property
    def pos(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def state(self):
        return object

    @property
    def priv(self):
        return object


class CollectDataPrivate():
    """"""


class CollectPads(Gst.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def add_pad(self, pad=None, size=None, destroy_notify=None, lock=None):
        """"""
        return object
    
    def available(self):
        """"""
        return object
    
    def clip_running_time(self, cdata=None, buf=None, outbuf=None, user_data=None):
        """"""
        return object
    
    def event_default(self, data=None, event=None, discard=None):
        """"""
        return object
    
    def flush(self, data=None, size=None):
        """"""
        return object
    
    def peek(self, data=None):
        """"""
        return object
    
    def pop(self, data=None):
        """"""
        return object
    
    def query_default(self, data=None, query=None, discard=None):
        """"""
        return object
    
    def read_buffer(self, data=None, size=None):
        """"""
        return object
    
    def remove_pad(self, pad=None):
        """"""
        return object
    
    def set_buffer_function(self, func=None, user_data=None):
        """"""
        return object
    
    def set_clip_function(self, clipfunc=None, user_data=None):
        """"""
        return object
    
    def set_compare_function(self, func=None, user_data=None):
        """"""
        return object
    
    def set_event_function(self, func=None, user_data=None):
        """"""
        return object
    
    def set_flush_function(self, func=None, user_data=None):
        """"""
        return object
    
    def set_flushing(self, flushing=None):
        """"""
        return object
    
    def set_function(self, func=None, user_data=None):
        """"""
        return object
    
    def set_query_function(self, func=None, user_data=None):
        """"""
        return object
    
    def set_waiting(self, data=None, waiting=None):
        """"""
        return object
    
    def src_event_default(self, pad=None, event=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def take_buffer(self, data=None, size=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def data(self):
        return object

    @property
    def stream_lock(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class CollectPadsClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class CollectPadsPrivate():
    """"""


class DataQueue(GObject.Object):
    """"""
    
    def __init__(self, checkfull=None, fullcallback=None, emptycallback=None, checkdata=None):
        """"""
        return object
    @staticmethod
    def new(checkfull=None, fullcallback=None, emptycallback=None, checkdata=None):
        """"""
        return object
    
    def empty(self):
        """"""
        return object
    
    def full(self):
        """"""
        return object
    
    def drop_head(self, type=None):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def get_level(self, level=None):
        """"""
        return object
    
    def is_empty(self):
        """"""
        return object
    
    def is_full(self):
        """"""
        return object
    
    def limits_changed(self):
        """"""
        return object
    
    def peek(self, item=None):
        """"""
        return object
    
    def pop(self, item=None):
        """"""
        return object
    
    def push(self, item=None):
        """"""
        return object
    
    def push_force(self, item=None):
        """"""
        return object
    
    def set_flushing(self, flushing=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DataQueueClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def empty(self):
        return object

    @property
    def full(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DataQueueItem():
    """"""

    @property
    def object(self):
        return object

    @property
    def size(self):
        return object

    @property
    def duration(self):
        return object

    @property
    def visible(self):
        return object

    @property
    def destroy(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DataQueuePrivate():
    """"""


class DataQueueSize():
    """"""

    @property
    def visible(self):
        return object

    @property
    def bytes(self):
        return object

    @property
    def time(self):
        return object


class FlowCombiner():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def add_pad(self, pad=None):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def remove_pad(self, pad=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def update_flow(self, fret=None):
        """"""
        return object
    
    def update_pad_flow(self, pad=None, fret=None):
        """"""
        return object


class PushSrc(BaseSrc):
    """"""
    
    def alloc(self, buf=None):
        """"""
        return object
    
    def create(self, buf=None):
        """"""
        return object
    
    def fill(self, buf=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PushSrcClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def create(self):
        return object

    @property
    def alloc(self):
        return object

    @property
    def fill(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class QueueArray():
    """"""
    
    def drop_element(self, idx=None):
        """"""
        return object
    
    def drop_struct(self, idx=None, p_struct=None):
        """"""
        return object
    
    def find(self, func=None, data=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def is_empty(self):
        """"""
        return object
    
    def peek_head(self):
        """"""
        return object
    
    def peek_head_struct(self):
        """"""
        return object
    
    def peek_tail(self):
        """"""
        return object
    
    def peek_tail_struct(self):
        """"""
        return object
    
    def pop_head(self):
        """"""
        return object
    
    def pop_head_struct(self):
        """"""
        return object
    
    def pop_tail(self):
        """"""
        return object
    
    def pop_tail_struct(self):
        """"""
        return object
    
    def push_tail(self, data=None):
        """"""
        return object
    
    def push_tail_struct(self, p_struct=None):
        """"""
        return object
    @staticmethod
    def new(initial_size=None):
        """"""
        return object
    @staticmethod
    def new_for_struct(struct_size=None, initial_size=None):
        """"""
        return object
