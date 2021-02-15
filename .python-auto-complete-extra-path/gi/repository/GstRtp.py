# -*- coding: utf-8 -*-
from gi.repository import Gst


class RTCPFBType:
    """"""
    FB_TYPE_INVALID = 0
    RTPFB_TYPE_NACK = 1
    RTPFB_TYPE_TMMBR = 3
    RTPFB_TYPE_TMMBN = 4
    RTPFB_TYPE_RTCP_SR_REQ = 5
    PSFB_TYPE_PLI = 1
    PSFB_TYPE_SLI = 2
    PSFB_TYPE_RPSI = 3
    PSFB_TYPE_AFB = 15
    PSFB_TYPE_FIR = 4
    PSFB_TYPE_TSTR = 5
    PSFB_TYPE_TSTN = 6
    PSFB_TYPE_VBCN = 7


class RTCPSDESType:
    """"""
    INVALID = -1
    END = 0
    CNAME = 1
    NAME = 2
    EMAIL = 3
    PHONE = 4
    LOC = 5
    TOOL = 6
    NOTE = 7
    PRIV = 8


class RTCPType:
    """"""
    INVALID = 0
    SR = 200
    RR = 201
    SDES = 202
    BYE = 203
    APP = 204
    RTPFB = 205
    PSFB = 206
    XR = 207
RTCP_MAX_BYE_SSRC_COUNT = r"""31"""
RTCP_MAX_RB_COUNT = r"""31"""
RTCP_MAX_SDES = r"""255"""
RTCP_MAX_SDES_ITEM_COUNT = r"""31"""
RTCP_REDUCED_SIZE_VALID_MASK = r"""57592"""
RTCP_VALID_MASK = r"""57598"""
RTCP_VALID_VALUE = r"""200"""
RTCP_VERSION = r"""2"""


class RTPBufferFlags:
    """"""
    RETRANSMISSION = 1048576
    REDUNDANT = 2097152
    LAST = 268435456


class RTPBufferMapFlags:
    """"""
    SKIP_PADDING = 65536
    LAST = 16777216


class RTPPayload:
    """"""
    PCMU = 0
    _1016 = 1
    G721 = 2
    GSM = 3
    G723 = 4
    DVI4_8000 = 5
    DVI4_16000 = 6
    LPC = 7
    PCMA = 8
    G722 = 9
    L16_STEREO = 10
    L16_MONO = 11
    QCELP = 12
    CN = 13
    MPA = 14
    G728 = 15
    DVI4_11025 = 16
    DVI4_22050 = 17
    G729 = 18
    CELLB = 25
    JPEG = 26
    NV = 28
    H261 = 31
    MPV = 32
    MP2T = 33
    H263 = 34


class RTPProfile:
    """"""
    UNKNOWN = 0
    AVP = 1
    SAVP = 2
    AVPF = 3
    SAVPF = 4
RTP_HDREXT_BASE = r"""urn:ietf:params:rtp-hdrext:"""
RTP_HDREXT_NTP_56 = r"""ntp-56"""
RTP_HDREXT_NTP_56_SIZE = r"""7"""
RTP_HDREXT_NTP_64 = r"""ntp-64"""
RTP_HDREXT_NTP_64_SIZE = r"""8"""
RTP_PAYLOAD_1016_STRING = r"""1"""
RTP_PAYLOAD_CELLB_STRING = r"""25"""
RTP_PAYLOAD_CN_STRING = r"""13"""
RTP_PAYLOAD_DVI4_11025_STRING = r"""16"""
RTP_PAYLOAD_DVI4_16000_STRING = r"""6"""
RTP_PAYLOAD_DVI4_22050_STRING = r"""17"""
RTP_PAYLOAD_DVI4_8000_STRING = r"""5"""
RTP_PAYLOAD_DYNAMIC_STRING = r"""[96, 127]"""
RTP_PAYLOAD_G721_STRING = r"""2"""
RTP_PAYLOAD_G722_STRING = r"""9"""
RTP_PAYLOAD_G723_53 = r"""17"""
RTP_PAYLOAD_G723_53_STRING = r"""17"""
RTP_PAYLOAD_G723_63 = r"""16"""
RTP_PAYLOAD_G723_63_STRING = r"""16"""
RTP_PAYLOAD_G723_STRING = r"""4"""
RTP_PAYLOAD_G728_STRING = r"""15"""
RTP_PAYLOAD_G729_STRING = r"""18"""
RTP_PAYLOAD_GSM_STRING = r"""3"""
RTP_PAYLOAD_H261_STRING = r"""31"""
RTP_PAYLOAD_H263_STRING = r"""34"""
RTP_PAYLOAD_JPEG_STRING = r"""26"""
RTP_PAYLOAD_L16_MONO_STRING = r"""11"""
RTP_PAYLOAD_L16_STEREO_STRING = r"""10"""
RTP_PAYLOAD_LPC_STRING = r"""7"""
RTP_PAYLOAD_MP2T_STRING = r"""33"""
RTP_PAYLOAD_MPA_STRING = r"""14"""
RTP_PAYLOAD_MPV_STRING = r"""32"""
RTP_PAYLOAD_NV_STRING = r"""28"""
RTP_PAYLOAD_PCMA_STRING = r"""8"""
RTP_PAYLOAD_PCMU_STRING = r"""0"""
RTP_PAYLOAD_QCELP_STRING = r"""12"""
RTP_PAYLOAD_TS41 = r"""19"""
RTP_PAYLOAD_TS41_STRING = r"""19"""
RTP_PAYLOAD_TS48 = r"""18"""
RTP_PAYLOAD_TS48_STRING = r"""18"""
RTP_VERSION = r"""2"""

def rtcp_buffer_map(buffer=None, flags=None, rtcp=None):
    """"""
    return object

def rtcp_buffer_new(mtu=None):
    """"""
    return object

def rtcp_buffer_new_copy_data(data=None, len=None):
    """"""
    return object

def rtcp_buffer_new_take_data(data=None, len=None):
    """"""
    return object

def rtcp_buffer_validate(buffer=None):
    """"""
    return object

def rtcp_buffer_validate_data(data=None, len=None):
    """"""
    return object

def rtcp_buffer_validate_data_reduced(data=None, len=None):
    """"""
    return object

def rtcp_buffer_validate_reduced(buffer=None):
    """"""
    return object

def rtcp_ntp_to_unix(ntptime=None):
    """"""
    return object

def rtcp_sdes_name_to_type(name=None):
    """"""
    return object

def rtcp_sdes_type_to_name(type=None):
    """"""
    return object

def rtcp_unix_to_ntp(unixtime=None):
    """"""
    return object

def rtp_buffer_allocate_data(buffer=None, payload_len=None, pad_len=None, csrc_count=None):
    """"""
    return object

def rtp_buffer_calc_header_len(csrc_count=None):
    """"""
    return object

def rtp_buffer_calc_packet_len(payload_len=None, pad_len=None, csrc_count=None):
    """"""
    return object

def rtp_buffer_calc_payload_len(packet_len=None, pad_len=None, csrc_count=None):
    """"""
    return object

def rtp_buffer_compare_seqnum(seqnum1=None, seqnum2=None):
    """"""
    return object

def rtp_buffer_default_clock_rate(payload_type=None):
    """"""
    return object

def rtp_buffer_ext_timestamp(exttimestamp=None, timestamp=None):
    """"""
    return object

def rtp_buffer_map(buffer=None, flags=None, rtp=None):
    """"""
    return object

def rtp_buffer_new_allocate(payload_len=None, pad_len=None, csrc_count=None):
    """"""
    return object

def rtp_buffer_new_allocate_len(packet_len=None, pad_len=None, csrc_count=None):
    """"""
    return object

def rtp_buffer_new_copy_data(data=None, len=None):
    """"""
    return object

def rtp_buffer_new_take_data(data=None, len=None):
    """"""
    return object

def rtp_hdrext_get_ntp_56(data=None, size=None, ntptime=None):
    """"""
    return object

def rtp_hdrext_get_ntp_64(data=None, size=None, ntptime=None):
    """"""
    return object

def rtp_hdrext_set_ntp_56(data=None, size=None, ntptime=None):
    """"""
    return object

def rtp_hdrext_set_ntp_64(data=None, size=None, ntptime=None):
    """"""
    return object

def rtp_payload_info_for_name(media=None, encoding_name=None):
    """"""
    return object

def rtp_payload_info_for_pt(payload_type=None):
    """"""
    return object


class RTCPBuffer():
    """"""
    
    def add_packet(self, type=None, packet=None):
        """"""
        return object
    
    def get_first_packet(self, packet=None):
        """"""
        return object
    
    def get_packet_count(self):
        """"""
        return object
    
    def unmap(self):
        """"""
        return object
    @staticmethod
    def map(buffer=None, flags=None, rtcp=None):
        """"""
        return object
    @staticmethod
    def new(mtu=None):
        """"""
        return object
    @staticmethod
    def new_copy_data(data=None, len=None):
        """"""
        return object
    @staticmethod
    def new_take_data(data=None, len=None):
        """"""
        return object
    @staticmethod
    def validate(buffer=None):
        """"""
        return object
    @staticmethod
    def validate_data(data=None, len=None):
        """"""
        return object
    @staticmethod
    def validate_data_reduced(data=None, len=None):
        """"""
        return object
    @staticmethod
    def validate_reduced(buffer=None):
        """"""
        return object

    @property
    def buffer(self):
        return object

    @property
    def map(self):
        return object


class RTCPPacket():
    """"""
    
    def add_profile_specific_ext(self, data=None, len=None):
        """"""
        return object
    
    def add_rb(self, ssrc=None, fractionlost=None, packetslost=None, exthighestseq=None, jitter=None, lsr=None, dlsr=None):
        """"""
        return object
    
    def app_get_data(self):
        """"""
        return object
    
    def app_get_data_length(self):
        """"""
        return object
    
    def app_get_name(self):
        """"""
        return object
    
    def app_get_ssrc(self):
        """"""
        return object
    
    def app_get_subtype(self):
        """"""
        return object
    
    def app_set_data_length(self, wordlen=None):
        """"""
        return object
    
    def app_set_name(self, name=None):
        """"""
        return object
    
    def app_set_ssrc(self, ssrc=None):
        """"""
        return object
    
    def app_set_subtype(self, subtype=None):
        """"""
        return object
    
    def bye_add_ssrc(self, ssrc=None):
        """"""
        return object
    
    def bye_add_ssrcs(self, ssrc=None, len=None):
        """"""
        return object
    
    def bye_get_nth_ssrc(self, nth=None):
        """"""
        return object
    
    def bye_get_reason(self):
        """"""
        return object
    
    def bye_get_reason_len(self):
        """"""
        return object
    
    def bye_get_ssrc_count(self):
        """"""
        return object
    
    def bye_set_reason(self, reason=None):
        """"""
        return object
    
    def copy_profile_specific_ext(self, data=None, len=None):
        """"""
        return object
    
    def fb_get_fci(self):
        """"""
        return object
    
    def fb_get_fci_length(self):
        """"""
        return object
    
    def fb_get_media_ssrc(self):
        """"""
        return object
    
    def fb_get_sender_ssrc(self):
        """"""
        return object
    
    def fb_get_type(self):
        """"""
        return object
    
    def fb_set_fci_length(self, wordlen=None):
        """"""
        return object
    
    def fb_set_media_ssrc(self, ssrc=None):
        """"""
        return object
    
    def fb_set_sender_ssrc(self, ssrc=None):
        """"""
        return object
    
    def fb_set_type(self, type=None):
        """"""
        return object
    
    def get_count(self):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def get_padding(self):
        """"""
        return object
    
    def get_profile_specific_ext(self, data=None, len=None):
        """"""
        return object
    
    def get_profile_specific_ext_length(self):
        """"""
        return object
    
    def get_rb(self, nth=None, ssrc=None, fractionlost=None, packetslost=None, exthighestseq=None, jitter=None, lsr=None, dlsr=None):
        """"""
        return object
    
    def get_rb_count(self):
        """"""
        return object
    
    def get_type(self):
        """"""
        return object
    
    def move_to_next(self):
        """"""
        return object
    
    def remove(self):
        """"""
        return object
    
    def rr_get_ssrc(self):
        """"""
        return object
    
    def rr_set_ssrc(self, ssrc=None):
        """"""
        return object
    
    def sdes_add_entry(self, type=None, len=None, data=None):
        """"""
        return object
    
    def sdes_add_item(self, ssrc=None):
        """"""
        return object
    
    def sdes_copy_entry(self, type=None, len=None, data=None):
        """"""
        return object
    
    def sdes_first_entry(self):
        """"""
        return object
    
    def sdes_first_item(self):
        """"""
        return object
    
    def sdes_get_entry(self, type=None, len=None, data=None):
        """"""
        return object
    
    def sdes_get_item_count(self):
        """"""
        return object
    
    def sdes_get_ssrc(self):
        """"""
        return object
    
    def sdes_next_entry(self):
        """"""
        return object
    
    def sdes_next_item(self):
        """"""
        return object
    
    def set_rb(self, nth=None, ssrc=None, fractionlost=None, packetslost=None, exthighestseq=None, jitter=None, lsr=None, dlsr=None):
        """"""
        return object
    
    def sr_get_sender_info(self, ssrc=None, ntptime=None, rtptime=None, packet_count=None, octet_count=None):
        """"""
        return object
    
    def sr_set_sender_info(self, ssrc=None, ntptime=None, rtptime=None, packet_count=None, octet_count=None):
        """"""
        return object

    @property
    def rtcp(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def padding(self):
        return object

    @property
    def count(self):
        return object

    @property
    def type(self):
        return object

    @property
    def length(self):
        return object

    @property
    def item_offset(self):
        return object

    @property
    def item_count(self):
        return object

    @property
    def entry_offset(self):
        return object


class RTPBaseAudioPayloadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTPBaseAudioPayloadPrivate():
    """"""


class RTPBaseDepayload(Gst.Element):
    """"""
    
    def handle_event(self, event=None):
        """"""
        return object
    
    def packet_lost(self, event=None):
        """"""
        return object
    
    def process(self, _in=None):
        """"""
        return object
    
    def process_rtp_packet(self, rtp_buffer=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def push(self, out_buf=None):
        """"""
        return object
    
    def push_list(self, out_list=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def sinkpad(self):
        return object

    @property
    def srcpad(self):
        return object

    @property
    def clock_rate(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def need_newsegment(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTPBaseDepayloadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def set_caps(self):
        return object

    @property
    def process(self):
        return object

    @property
    def packet_lost(self):
        return object

    @property
    def handle_event(self):
        return object

    @property
    def process_rtp_packet(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTPBaseDepayloadPrivate():
    """"""


class RTPBasePayload(Gst.Element):
    """"""
    
    def get_caps(self, pad=None, filter=None):
        """"""
        return object
    
    def handle_buffer(self, buffer=None):
        """"""
        return object
    
    def query(self, pad=None, query=None):
        """"""
        return object
    
    def set_caps(self, caps=None):
        """"""
        return object
    
    def sink_event(self, event=None):
        """"""
        return object
    
    def src_event(self, event=None):
        """"""
        return object
    
    def is_filled(self, size=None, duration=None):
        """"""
        return object
    
    def push(self, buffer=None):
        """"""
        return object
    
    def push_list(self, list=None):
        """"""
        return object
    
    def set_options(self, media=None, dynamic=None, encoding_name=None, clock_rate=None):
        """"""
        return object
    
    def set_outcaps(self, fieldname=None, *args):
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
    def ts_base(self):
        return object

    @property
    def seqnum_base(self):
        return object

    @property
    def media(self):
        return object

    @property
    def encoding_name(self):
        return object

    @property
    def dynamic(self):
        return object

    @property
    def clock_rate(self):
        return object

    @property
    def ts_offset(self):
        return object

    @property
    def timestamp(self):
        return object

    @property
    def seqnum_offset(self):
        return object

    @property
    def seqnum(self):
        return object

    @property
    def max_ptime(self):
        return object

    @property
    def pt(self):
        return object

    @property
    def ssrc(self):
        return object

    @property
    def current_ssrc(self):
        return object

    @property
    def mtu(self):
        return object

    @property
    def segment(self):
        return object

    @property
    def min_ptime(self):
        return object

    @property
    def ptime(self):
        return object

    @property
    def ptime_multiple(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTPBasePayloadClass():
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
    def handle_buffer(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def query(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTPBasePayloadPrivate():
    """"""


class RTPBuffer():
    """"""
    
    def add_extension_onebyte_header(self, id=None, data=None, size=None):
        """"""
        return object
    
    def add_extension_twobytes_header(self, appbits=None, id=None, data=None, size=None):
        """"""
        return object
    
    def get_csrc(self, idx=None):
        """"""
        return object
    
    def get_csrc_count(self):
        """"""
        return object
    
    def get_extension(self):
        """"""
        return object
    
    def get_extension_bytes(self, bits=None):
        """"""
        return object
    
    def get_extension_data(self, bits=None, data=None, wordlen=None):
        """"""
        return object
    
    def get_extension_onebyte_header(self, id=None, nth=None, data=None, size=None):
        """"""
        return object
    
    def get_extension_twobytes_header(self, appbits=None, id=None, nth=None, data=None, size=None):
        """"""
        return object
    
    def get_header_len(self):
        """"""
        return object
    
    def get_marker(self):
        """"""
        return object
    
    def get_packet_len(self):
        """"""
        return object
    
    def get_padding(self):
        """"""
        return object
    
    def get_payload(self):
        """"""
        return object
    
    def get_payload_buffer(self):
        """"""
        return object
    
    def get_payload_bytes(self):
        """"""
        return object
    
    def get_payload_len(self):
        """"""
        return object
    
    def get_payload_subbuffer(self, offset=None, len=None):
        """"""
        return object
    
    def get_payload_type(self):
        """"""
        return object
    
    def get_seq(self):
        """"""
        return object
    
    def get_ssrc(self):
        """"""
        return object
    
    def get_timestamp(self):
        """"""
        return object
    
    def get_version(self):
        """"""
        return object
    
    def pad_to(self, len=None):
        """"""
        return object
    
    def set_csrc(self, idx=None, csrc=None):
        """"""
        return object
    
    def set_extension(self, extension=None):
        """"""
        return object
    
    def set_extension_data(self, bits=None, length=None):
        """"""
        return object
    
    def set_marker(self, marker=None):
        """"""
        return object
    
    def set_packet_len(self, len=None):
        """"""
        return object
    
    def set_padding(self, padding=None):
        """"""
        return object
    
    def set_payload_type(self, payload_type=None):
        """"""
        return object
    
    def set_seq(self, seq=None):
        """"""
        return object
    
    def set_ssrc(self, ssrc=None):
        """"""
        return object
    
    def set_timestamp(self, timestamp=None):
        """"""
        return object
    
    def set_version(self, version=None):
        """"""
        return object
    
    def unmap(self):
        """"""
        return object
    @staticmethod
    def allocate_data(buffer=None, payload_len=None, pad_len=None, csrc_count=None):
        """"""
        return object
    @staticmethod
    def calc_header_len(csrc_count=None):
        """"""
        return object
    @staticmethod
    def calc_packet_len(payload_len=None, pad_len=None, csrc_count=None):
        """"""
        return object
    @staticmethod
    def calc_payload_len(packet_len=None, pad_len=None, csrc_count=None):
        """"""
        return object
    @staticmethod
    def compare_seqnum(seqnum1=None, seqnum2=None):
        """"""
        return object
    @staticmethod
    def default_clock_rate(payload_type=None):
        """"""
        return object
    @staticmethod
    def ext_timestamp(exttimestamp=None, timestamp=None):
        """"""
        return object
    @staticmethod
    def map(buffer=None, flags=None, rtp=None):
        """"""
        return object
    @staticmethod
    def new_allocate(payload_len=None, pad_len=None, csrc_count=None):
        """"""
        return object
    @staticmethod
    def new_allocate_len(packet_len=None, pad_len=None, csrc_count=None):
        """"""
        return object
    @staticmethod
    def new_copy_data(data=None, len=None):
        """"""
        return object
    @staticmethod
    def new_take_data(data=None, len=None):
        """"""
        return object

    @property
    def buffer(self):
        return object

    @property
    def state(self):
        return object

    @property
    def data(self):
        return object

    @property
    def size(self):
        return object

    @property
    def map(self):
        return object


class RTPPayloadInfo():
    """"""
    @staticmethod
    def for_name(media=None, encoding_name=None):
        """"""
        return object
    @staticmethod
    def for_pt(payload_type=None):
        """"""
        return object

    @property
    def payload_type(self):
        return object

    @property
    def media(self):
        return object

    @property
    def encoding_name(self):
        return object

    @property
    def clock_rate(self):
        return object

    @property
    def encoding_parameters(self):
        return object

    @property
    def bitrate(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTPBaseAudioPayload(RTPBasePayload):
    """"""
    
    def flush(self, payload_len=None, timestamp=None):
        """"""
        return object
    
    def get_adapter(self):
        """"""
        return object
    
    def push(self, data=None, payload_len=None, timestamp=None):
        """"""
        return object
    
    def set_frame_based(self):
        """"""
        return object
    
    def set_frame_options(self, frame_duration=None, frame_size=None):
        """"""
        return object
    
    def set_sample_based(self):
        """"""
        return object
    
    def set_sample_options(self, sample_size=None):
        """"""
        return object
    
    def set_samplebits_options(self, sample_size=None):
        """"""
        return object

    @property
    def payload(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def base_ts(self):
        return object

    @property
    def frame_size(self):
        return object

    @property
    def frame_duration(self):
        return object

    @property
    def sample_size(self):
        return object

    @property
    def _gst_reserved(self):
        return object
