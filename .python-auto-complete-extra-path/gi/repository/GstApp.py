# -*- coding: utf-8 -*-
from gi.repository import Gst
from gi.repository import GstBase


class AppStreamType:
    """"""
    STREAM = 0
    SEEKABLE = 1
    RANDOM_ACCESS = 2


class AppSink(GstBase.BaseSink, Gst.URIHandler):
    """"""
    
    def eos(self):
        """"""
        return object
    
    def new_preroll(self):
        """"""
        return object
    
    def new_sample(self):
        """"""
        return object
    
    def pull_preroll(self):
        """"""
        return object
    
    def pull_sample(self):
        """"""
        return object
    
    def try_pull_preroll(self, timeout=None):
        """"""
        return object
    
    def try_pull_sample(self, timeout=None):
        """"""
        return object
    
    def get_buffer_list_support(self):
        """"""
        return object
    
    def get_caps(self):
        """"""
        return object
    
    def get_drop(self):
        """"""
        return object
    
    def get_emit_signals(self):
        """"""
        return object
    
    def get_max_buffers(self):
        """"""
        return object
    
    def get_wait_on_eos(self):
        """"""
        return object
    
    def is_eos(self):
        """"""
        return object
    
    def pull_preroll(self):
        """"""
        return object
    
    def pull_sample(self):
        """"""
        return object
    
    def set_buffer_list_support(self, enable_lists=None):
        """"""
        return object
    
    def set_callbacks(self, callbacks=None, user_data=None, notify=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def set_drop(self, drop=None):
        """"""
        return object
    
    def set_emit_signals(self, emit=None):
        """"""
        return object
    
    def set_max_buffers(self, max=None):
        """"""
        return object
    
    def set_wait_on_eos(self, wait=None):
        """"""
        return object
    
    def try_pull_preroll(self, timeout=None):
        """"""
        return object
    
    def try_pull_sample(self, timeout=None):
        """"""
        return object

    @property
    def basesink(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AppSinkCallbacks():
    """"""

    @property
    def eos(self):
        return object

    @property
    def new_preroll(self):
        return object

    @property
    def new_sample(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AppSinkClass():
    """"""

    @property
    def basesink_class(self):
        return object

    @property
    def eos(self):
        return object

    @property
    def new_preroll(self):
        return object

    @property
    def new_sample(self):
        return object

    @property
    def pull_preroll(self):
        return object

    @property
    def pull_sample(self):
        return object

    @property
    def try_pull_preroll(self):
        return object

    @property
    def try_pull_sample(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AppSinkPrivate():
    """"""


class AppSrc(GstBase.BaseSrc, Gst.URIHandler):
    """"""
    
    def end_of_stream(self):
        """"""
        return object
    
    def enough_data(self):
        """"""
        return object
    
    def need_data(self, length=None):
        """"""
        return object
    
    def push_buffer(self, buffer=None):
        """"""
        return object
    
    def push_buffer_list(self, buffer_list=None):
        """"""
        return object
    
    def push_sample(self, sample=None):
        """"""
        return object
    
    def seek_data(self, offset=None):
        """"""
        return object
    
    def end_of_stream(self):
        """"""
        return object
    
    def get_caps(self):
        """"""
        return object
    
    def get_current_level_bytes(self):
        """"""
        return object
    
    def get_duration(self):
        """"""
        return object
    
    def get_emit_signals(self):
        """"""
        return object
    
    def get_latency(self, min=None, max=None):
        """"""
        return object
    
    def get_max_bytes(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def get_stream_type(self):
        """"""
        return object
    
    def push_buffer(self, buffer=None):
        """"""
        return object
    
    def push_buffer_list(self, buffer_list=None):
        """"""
        return object
    
    def push_sample(self, sample=None):
        """"""
        return object
    
    def set_callbacks(self, callbacks=None, user_data=None, notify=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def set_duration(self, duration=None):
        """"""
        return object
    
    def set_emit_signals(self, emit=None):
        """"""
        return object
    
    def set_latency(self, min=None, max=None):
        """"""
        return object
    
    def set_max_bytes(self, max=None):
        """"""
        return object
    
    def set_size(self, size=None):
        """"""
        return object
    
    def set_stream_type(self, type=None):
        """"""
        return object

    @property
    def basesrc(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AppSrcCallbacks():
    """"""

    @property
    def need_data(self):
        return object

    @property
    def enough_data(self):
        return object

    @property
    def seek_data(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AppSrcClass():
    """"""

    @property
    def basesrc_class(self):
        return object

    @property
    def need_data(self):
        return object

    @property
    def enough_data(self):
        return object

    @property
    def seek_data(self):
        return object

    @property
    def push_buffer(self):
        return object

    @property
    def end_of_stream(self):
        return object

    @property
    def push_sample(self):
        return object

    @property
    def push_buffer_list(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AppSrcPrivate():
    """"""
