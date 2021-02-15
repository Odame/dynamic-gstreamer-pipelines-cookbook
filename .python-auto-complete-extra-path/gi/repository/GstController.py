# -*- coding: utf-8 -*-
from gi.repository import Gst


class InterpolationMode:
    """"""
    NONE = 0
    LINEAR = 1
    CUBIC = 2
    CUBIC_MONOTONIC = 3


class LFOWaveform:
    """"""
    SINE = 0
    SQUARE = 1
    SAW = 2
    REVERSE_SAW = 3
    TRIANGLE = 4

def timed_value_control_invalidate_cache(self):
    """"""
    return object


class ARGBControlBinding(Gst.ControlBinding):
    """"""
    
    def __init__(self, object=None, property_name=None, cs_a=None, cs_r=None, cs_g=None, cs_b=None):
        """"""
        return object
    @staticmethod
    def new(object=None, property_name=None, cs_a=None, cs_r=None, cs_g=None, cs_b=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def cs_a(self):
        return object

    @property
    def cs_r(self):
        return object

    @property
    def cs_g(self):
        return object

    @property
    def cs_b(self):
        return object

    @property
    def cur_value(self):
        return object

    @property
    def last_value(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ARGBControlBindingClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ControlPoint():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object

    @property
    def timestamp(self):
        return object

    @property
    def value(self):
        return object


class DirectControlBinding(Gst.ControlBinding):
    """"""
    
    def __init__(self, object=None, property_name=None, cs=None):
        """"""
        return object
    @staticmethod
    def new(object=None, property_name=None, cs=None):
        """"""
        return object
    @staticmethod
    def new_absolute(object=None, property_name=None, cs=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def cs(self):
        return object

    @property
    def cur_value(self):
        return object

    @property
    def last_value(self):
        return object

    @property
    def byte_size(self):
        return object

    @property
    def convert_value(self):
        return object

    @property
    def convert_g_value(self):
        return object


class DirectControlBindingClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class InterpolationControlSourceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class InterpolationControlSourcePrivate():
    """"""


class LFOControlSource(Gst.ControlSource):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class LFOControlSourceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class LFOControlSourcePrivate():
    """"""


class ProxyControlBinding(Gst.ControlBinding):
    """"""
    
    def __init__(self, object=None, property_name=None, ref_object=None, ref_property_name=None):
        """"""
        return object
    @staticmethod
    def new(object=None, property_name=None, ref_object=None, ref_property_name=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def ref_object(self):
        return object

    @property
    def property_name(self):
        return object

    @property
    def _padding(self):
        return object


class ProxyControlBindingClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class TimedValueControlSource(Gst.ControlSource):
    """"""
    
    def find_control_point_iter(self, timestamp=None):
        """"""
        return object
    
    def get_all(self):
        """"""
        return object
    
    def get_count(self):
        """"""
        return object
    
    def set(self, timestamp=None, value=None):
        """"""
        return object
    
    def set_from_list(self, timedvalues=None):
        """"""
        return object
    
    def unset(self, timestamp=None):
        """"""
        return object
    
    def unset_all(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def values(self):
        return object

    @property
    def nvalues(self):
        return object

    @property
    def valid_cache(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TimedValueControlSourceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TimedValueControlSourcePrivate():
    """"""


class TriggerControlSource(TimedValueControlSource):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TriggerControlSourceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TriggerControlSourcePrivate():
    """"""


class InterpolationControlSource(TimedValueControlSource):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object
