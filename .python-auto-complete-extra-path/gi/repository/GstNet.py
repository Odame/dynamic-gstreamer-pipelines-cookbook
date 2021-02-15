# -*- coding: utf-8 -*-
from gi.repository import Gst
from gi.repository import Gio
NET_TIME_PACKET_SIZE = r"""16"""
PTP_CLOCK_ID_NONE = r"""18446744073709551615"""
PTP_STATISTICS_BEST_MASTER_CLOCK_SELECTED = r"""GstPtpStatisticsBestMasterClockSelected"""
PTP_STATISTICS_NEW_DOMAIN_FOUND = r"""GstPtpStatisticsNewDomainFound"""
PTP_STATISTICS_PATH_DELAY_MEASURED = r"""GstPtpStatisticsPathDelayMeasured"""
PTP_STATISTICS_TIME_UPDATED = r"""GstPtpStatisticsTimeUpdated"""

def buffer_add_net_address_meta(buffer=None, addr=None):
    """"""
    return object

def buffer_add_net_control_message_meta(buffer=None, message=None):
    """"""
    return object

def buffer_get_net_address_meta(buffer=None):
    """"""
    return object

def net_address_meta_api_get_type():
    """"""
    return object

def net_address_meta_get_info():
    """"""
    return object

def net_control_message_meta_api_get_type():
    """"""
    return object

def net_control_message_meta_get_info():
    """"""
    return object

def net_time_packet_receive(socket=None, src_address=None):
    """"""
    return object

def ptp_deinit():
    """"""
    return object

def ptp_init(clock_id=None, interfaces=None):
    """"""
    return object

def ptp_is_initialized():
    """"""
    return object

def ptp_is_supported():
    """"""
    return object

def ptp_statistics_callback_add(callback=None, user_data=None, destroy_data=None):
    """"""
    return object

def ptp_statistics_callback_remove(id=None):
    """"""
    return object


class NetAddressMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def addr(self):
        return object


class NetClientClock(Gst.SystemClock):
    """"""
    
    def __init__(self, name=None, remote_address=None, remote_port=None, base_time=None):
        """"""
        return object
    @staticmethod
    def new(name=None, remote_address=None, remote_port=None, base_time=None):
        """"""
        return object

    @property
    def clock(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class NetClientClockClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class NetClientClockPrivate():
    """"""


class NetControlMessageMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def message(self):
        return object


class NetTimePacket():
    """"""
    
    def __init__(self, buffer=None):
        """"""
        return object
    @staticmethod
    def new(buffer=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def send(self, socket=None, dest_address=None):
        """"""
        return object
    
    def serialize(self):
        """"""
        return object
    @staticmethod
    def receive(socket=None, src_address=None):
        """"""
        return object

    @property
    def local_time(self):
        return object

    @property
    def remote_time(self):
        return object


class NetTimeProvider(Gst.Object, Gio.Initable):
    """"""
    
    def __init__(self, clock=None, address=None, port=None):
        """"""
        return object
    @staticmethod
    def new(clock=None, address=None, port=None):
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


class NetTimeProviderClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class NetTimeProviderPrivate():
    """"""


class NtpClock(NetClientClock):
    """"""
    
    def __init__(self, name=None, remote_address=None, remote_port=None, base_time=None):
        """"""
        return object
    @staticmethod
    def new(name=None, remote_address=None, remote_port=None, base_time=None):
        """"""
        return object

    @property
    def clock(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class NtpClockClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PtpClock(Gst.SystemClock):
    """"""
    
    def __init__(self, name=None, domain=None):
        """"""
        return object
    @staticmethod
    def new(name=None, domain=None):
        """"""
        return object

    @property
    def clock(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PtpClockClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PtpClockPrivate():
    """"""
