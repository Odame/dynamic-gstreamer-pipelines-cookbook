# -*- coding: utf-8 -*-


class MIKEYCacheType:
    """"""
    NONE = 0
    ALWAYS = 1
    FOR_CSB = 2


class MIKEYEncAlg:
    """"""
    NULL = 0
    AES_CM_128 = 1
    AES_KW_128 = 2


class MIKEYKVType:
    """"""
    NULL = 0
    SPI = 1
    INTERVAL = 2


class MIKEYKeyDataType:
    """"""
    TGK = 0
    TEK = 2


class MIKEYMacAlg:
    """"""
    NULL = 0
    HMAC_SHA_1_160 = 1


class MIKEYMapType:
    """"""
    MIKEY_MAP_TYPE_SRTP = 0


class MIKEYPRFFunc:
    """"""
    MIKEY_PRF_MIKEY_1 = 0


class MIKEYPayloadType:
    """"""
    LAST = 0
    KEMAC = 1
    PKE = 2
    DH = 3
    SIGN = 4
    T = 5
    ID = 6
    CERT = 7
    CHASH = 8
    V = 9
    SP = 10
    RAND = 11
    ERR = 12
    KEY_DATA = 20
    GEN_EXT = 21


class MIKEYSecProto:
    """"""
    MIKEY_SEC_PROTO_SRTP = 0


class MIKEYSecSRTP:
    """"""
    ENC_ALG = 0
    ENC_KEY_LEN = 1
    AUTH_ALG = 2
    AUTH_KEY_LEN = 3
    SALT_KEY_LEN = 4
    PRF = 5
    KEY_DERIV_RATE = 6
    SRTP_ENC = 7
    SRTCP_ENC = 8
    FEC_ORDER = 9
    SRTP_AUTH = 10
    AUTH_TAG_LEN = 11
    SRTP_PREFIX_LEN = 12


class MIKEYTSType:
    """"""
    NTP_UTC = 0
    NTP = 1
    COUNTER = 2


class MIKEYType:
    """"""
    INVALID = -1
    PSK_INIT = 0
    PSK_VERIFY = 1
    PK_INIT = 2
    PK_VERIFY = 3
    DH_INIT = 4
    DH_RESP = 5
    ERROR = 6
MIKEY_VERSION = r"""1"""


class SDPResult:
    """"""
    OK = 0
    EINVAL = -1
SDP_BWTYPE_AS = r"""AS"""
SDP_BWTYPE_CT = r"""CT"""
SDP_BWTYPE_EXT_PREFIX = r"""X-"""
SDP_BWTYPE_RR = r"""RR"""
SDP_BWTYPE_RS = r"""RS"""
SDP_BWTYPE_TIAS = r"""TIAS"""

def sdp_address_is_multicast(nettype=None, addrtype=None, addr=None):
    """"""
    return object

def sdp_make_keymgmt(uri=None, base64=None):
    """"""
    return object

def sdp_media_new(media=None):
    """"""
    return object

def sdp_media_set_media_from_caps(caps=None, media=None):
    """"""
    return object

def sdp_message_as_uri(scheme=None, msg=None):
    """"""
    return object

def sdp_message_new(msg=None):
    """"""
    return object

def sdp_message_parse_buffer(data=None, size=None, msg=None):
    """"""
    return object

def sdp_message_parse_uri(uri=None, msg=None):
    """"""
    return object


class MIKEYDecryptInfo():
    """"""


class MIKEYEncryptInfo():
    """"""


class MIKEYMapSRTP():
    """"""

    @property
    def policy(self):
        return object

    @property
    def ssrc(self):
        return object

    @property
    def roc(self):
        return object


class MIKEYMessage():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_from_bytes(bytes=None, info=None):
        """"""
        return object
    @staticmethod
    def new_from_caps(caps=None):
        """"""
        return object
    @staticmethod
    def new_from_data(data=None, size=None, info=None):
        """"""
        return object
    
    def add_cs_srtp(self, policy=None, ssrc=None, roc=None):
        """"""
        return object
    
    def add_payload(self, payload=None):
        """"""
        return object
    
    def add_pke(self, C=None, data_len=None, data=None):
        """"""
        return object
    
    def add_rand(self, len=None, rand=None):
        """"""
        return object
    
    def add_rand_len(self, len=None):
        """"""
        return object
    
    def add_t(self, type=None, ts_value=None):
        """"""
        return object
    
    def add_t_now_ntp_utc(self):
        """"""
        return object
    
    def base64_encode(self):
        """"""
        return object
    
    def find_payload(self, type=None, nth=None):
        """"""
        return object
    
    def get_cs_srtp(self, idx=None):
        """"""
        return object
    
    def get_n_cs(self):
        """"""
        return object
    
    def get_n_payloads(self):
        """"""
        return object
    
    def get_payload(self, idx=None):
        """"""
        return object
    
    def insert_cs_srtp(self, idx=None, map=None):
        """"""
        return object
    
    def insert_payload(self, idx=None, payload=None):
        """"""
        return object
    
    def remove_cs_srtp(self, idx=None):
        """"""
        return object
    
    def remove_payload(self, idx=None):
        """"""
        return object
    
    def replace_cs_srtp(self, idx=None, map=None):
        """"""
        return object
    
    def replace_payload(self, idx=None, payload=None):
        """"""
        return object
    
    def set_info(self, version=None, type=None, V=None, prf_func=None, CSB_id=None, map_type=None):
        """"""
        return object
    
    def to_bytes(self, info=None):
        """"""
        return object
    
    def to_caps(self, caps=None):
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def version(self):
        return object

    @property
    def type(self):
        return object

    @property
    def V(self):
        return object

    @property
    def prf_func(self):
        return object

    @property
    def CSB_id(self):
        return object

    @property
    def map_type(self):
        return object

    @property
    def map_info(self):
        return object

    @property
    def payloads(self):
        return object


class MIKEYPayload():
    """"""
    
    def __init__(self, type=None):
        """"""
        return object
    @staticmethod
    def new(type=None):
        """"""
        return object
    
    def kemac_add_sub(self, newpay=None):
        """"""
        return object
    
    def kemac_get_n_sub(self):
        """"""
        return object
    
    def kemac_get_sub(self, idx=None):
        """"""
        return object
    
    def kemac_remove_sub(self, idx=None):
        """"""
        return object
    
    def kemac_set(self, enc_alg=None, mac_alg=None):
        """"""
        return object
    
    def key_data_set_interval(self, vf_len=None, vf_data=None, vt_len=None, vt_data=None):
        """"""
        return object
    
    def key_data_set_key(self, key_type=None, key_len=None, key_data=None):
        """"""
        return object
    
    def key_data_set_salt(self, salt_len=None, salt_data=None):
        """"""
        return object
    
    def key_data_set_spi(self, spi_len=None, spi_data=None):
        """"""
        return object
    
    def pke_set(self, C=None, data_len=None, data=None):
        """"""
        return object
    
    def rand_set(self, len=None, rand=None):
        """"""
        return object
    
    def sp_add_param(self, type=None, len=None, val=None):
        """"""
        return object
    
    def sp_get_n_params(self):
        """"""
        return object
    
    def sp_get_param(self, idx=None):
        """"""
        return object
    
    def sp_remove_param(self, idx=None):
        """"""
        return object
    
    def sp_set(self, policy=None, proto=None):
        """"""
        return object
    
    def t_set(self, type=None, ts_value=None):
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def type(self):
        return object

    @property
    def len(self):
        return object


class MIKEYPayloadKEMAC():
    """"""

    @property
    def pt(self):
        return object

    @property
    def enc_alg(self):
        return object

    @property
    def mac_alg(self):
        return object

    @property
    def subpayloads(self):
        return object


class MIKEYPayloadKeyData():
    """"""

    @property
    def pt(self):
        return object

    @property
    def key_type(self):
        return object

    @property
    def key_len(self):
        return object

    @property
    def key_data(self):
        return object

    @property
    def salt_len(self):
        return object

    @property
    def salt_data(self):
        return object

    @property
    def kv_type(self):
        return object

    @property
    def kv_len(self):
        return object

    @property
    def kv_data(self):
        return object


class MIKEYPayloadPKE():
    """"""

    @property
    def pt(self):
        return object

    @property
    def C(self):
        return object

    @property
    def data_len(self):
        return object

    @property
    def data(self):
        return object


class MIKEYPayloadRAND():
    """"""

    @property
    def pt(self):
        return object

    @property
    def len(self):
        return object

    @property
    def rand(self):
        return object


class MIKEYPayloadSP():
    """"""

    @property
    def pt(self):
        return object

    @property
    def policy(self):
        return object

    @property
    def proto(self):
        return object

    @property
    def params(self):
        return object


class MIKEYPayloadSPParam():
    """"""

    @property
    def type(self):
        return object

    @property
    def len(self):
        return object

    @property
    def val(self):
        return object


class MIKEYPayloadT():
    """"""

    @property
    def pt(self):
        return object

    @property
    def type(self):
        return object

    @property
    def ts_value(self):
        return object


class SDPAttribute():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def set(self, key=None, value=None):
        """"""
        return object

    @property
    def key(self):
        return object

    @property
    def value(self):
        return object


class SDPBandwidth():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def set(self, bwtype=None, bandwidth=None):
        """"""
        return object

    @property
    def bwtype(self):
        return object

    @property
    def bandwidth(self):
        return object


class SDPConnection():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def set(self, nettype=None, addrtype=None, address=None, ttl=None, addr_number=None):
        """"""
        return object

    @property
    def nettype(self):
        return object

    @property
    def addrtype(self):
        return object

    @property
    def address(self):
        return object

    @property
    def ttl(self):
        return object

    @property
    def addr_number(self):
        return object


class SDPKey():
    """"""

    @property
    def type(self):
        return object

    @property
    def data(self):
        return object


class SDPMedia():
    """"""
    
    def add_attribute(self, key=None, value=None):
        """"""
        return object
    
    def add_bandwidth(self, bwtype=None, bandwidth=None):
        """"""
        return object
    
    def add_connection(self, nettype=None, addrtype=None, address=None, ttl=None, addr_number=None):
        """"""
        return object
    
    def add_format(self, format=None):
        """"""
        return object
    
    def as_text(self):
        """"""
        return object
    
    def attributes_len(self):
        """"""
        return object
    
    def attributes_to_caps(self, caps=None):
        """"""
        return object
    
    def bandwidths_len(self):
        """"""
        return object
    
    def connections_len(self):
        """"""
        return object
    
    def copy(self, copy=None):
        """"""
        return object
    
    def formats_len(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_attribute(self, idx=None):
        """"""
        return object
    
    def get_attribute_val(self, key=None):
        """"""
        return object
    
    def get_attribute_val_n(self, key=None, nth=None):
        """"""
        return object
    
    def get_bandwidth(self, idx=None):
        """"""
        return object
    
    def get_caps_from_media(self, pt=None):
        """"""
        return object
    
    def get_connection(self, idx=None):
        """"""
        return object
    
    def get_format(self, idx=None):
        """"""
        return object
    
    def get_information(self):
        """"""
        return object
    
    def get_key(self):
        """"""
        return object
    
    def get_media(self):
        """"""
        return object
    
    def get_num_ports(self):
        """"""
        return object
    
    def get_port(self):
        """"""
        return object
    
    def get_proto(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def insert_attribute(self, idx=None, attr=None):
        """"""
        return object
    
    def insert_bandwidth(self, idx=None, bw=None):
        """"""
        return object
    
    def insert_connection(self, idx=None, conn=None):
        """"""
        return object
    
    def insert_format(self, idx=None, format=None):
        """"""
        return object
    
    def parse_keymgmt(self, mikey=None):
        """"""
        return object
    
    def remove_attribute(self, idx=None):
        """"""
        return object
    
    def remove_bandwidth(self, idx=None):
        """"""
        return object
    
    def remove_connection(self, idx=None):
        """"""
        return object
    
    def remove_format(self, idx=None):
        """"""
        return object
    
    def replace_attribute(self, idx=None, attr=None):
        """"""
        return object
    
    def replace_bandwidth(self, idx=None, bw=None):
        """"""
        return object
    
    def replace_connection(self, idx=None, conn=None):
        """"""
        return object
    
    def replace_format(self, idx=None, format=None):
        """"""
        return object
    
    def set_information(self, information=None):
        """"""
        return object
    
    def set_key(self, type=None, data=None):
        """"""
        return object
    
    def set_media(self, med=None):
        """"""
        return object
    
    def set_port_info(self, port=None, num_ports=None):
        """"""
        return object
    
    def set_proto(self, proto=None):
        """"""
        return object
    
    def uninit(self):
        """"""
        return object
    @staticmethod
    def new(media=None):
        """"""
        return object
    @staticmethod
    def set_media_from_caps(caps=None, media=None):
        """"""
        return object

    @property
    def media(self):
        return object

    @property
    def port(self):
        return object

    @property
    def num_ports(self):
        return object

    @property
    def proto(self):
        return object

    @property
    def fmts(self):
        return object

    @property
    def information(self):
        return object

    @property
    def connections(self):
        return object

    @property
    def bandwidths(self):
        return object

    @property
    def key(self):
        return object

    @property
    def attributes(self):
        return object


class SDPMessage():
    """"""
    
    def add_attribute(self, key=None, value=None):
        """"""
        return object
    
    def add_bandwidth(self, bwtype=None, bandwidth=None):
        """"""
        return object
    
    def add_email(self, email=None):
        """"""
        return object
    
    def add_media(self, media=None):
        """"""
        return object
    
    def add_phone(self, phone=None):
        """"""
        return object
    
    def add_time(self, start=None, stop=None, repeat=None):
        """"""
        return object
    
    def add_zone(self, adj_time=None, typed_time=None):
        """"""
        return object
    
    def as_text(self):
        """"""
        return object
    
    def attributes_len(self):
        """"""
        return object
    
    def attributes_to_caps(self, caps=None):
        """"""
        return object
    
    def bandwidths_len(self):
        """"""
        return object
    
    def copy(self, copy=None):
        """"""
        return object
    
    def dump(self):
        """"""
        return object
    
    def emails_len(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_attribute(self, idx=None):
        """"""
        return object
    
    def get_attribute_val(self, key=None):
        """"""
        return object
    
    def get_attribute_val_n(self, key=None, nth=None):
        """"""
        return object
    
    def get_bandwidth(self, idx=None):
        """"""
        return object
    
    def get_connection(self):
        """"""
        return object
    
    def get_email(self, idx=None):
        """"""
        return object
    
    def get_information(self):
        """"""
        return object
    
    def get_key(self):
        """"""
        return object
    
    def get_media(self, idx=None):
        """"""
        return object
    
    def get_origin(self):
        """"""
        return object
    
    def get_phone(self, idx=None):
        """"""
        return object
    
    def get_session_name(self):
        """"""
        return object
    
    def get_time(self, idx=None):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_version(self):
        """"""
        return object
    
    def get_zone(self, idx=None):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def insert_attribute(self, idx=None, attr=None):
        """"""
        return object
    
    def insert_bandwidth(self, idx=None, bw=None):
        """"""
        return object
    
    def insert_email(self, idx=None, email=None):
        """"""
        return object
    
    def insert_phone(self, idx=None, phone=None):
        """"""
        return object
    
    def insert_time(self, idx=None, t=None):
        """"""
        return object
    
    def insert_zone(self, idx=None, zone=None):
        """"""
        return object
    
    def medias_len(self):
        """"""
        return object
    
    def parse_keymgmt(self, mikey=None):
        """"""
        return object
    
    def phones_len(self):
        """"""
        return object
    
    def remove_attribute(self, idx=None):
        """"""
        return object
    
    def remove_bandwidth(self, idx=None):
        """"""
        return object
    
    def remove_email(self, idx=None):
        """"""
        return object
    
    def remove_phone(self, idx=None):
        """"""
        return object
    
    def remove_time(self, idx=None):
        """"""
        return object
    
    def remove_zone(self, idx=None):
        """"""
        return object
    
    def replace_attribute(self, idx=None, attr=None):
        """"""
        return object
    
    def replace_bandwidth(self, idx=None, bw=None):
        """"""
        return object
    
    def replace_email(self, idx=None, email=None):
        """"""
        return object
    
    def replace_phone(self, idx=None, phone=None):
        """"""
        return object
    
    def replace_time(self, idx=None, t=None):
        """"""
        return object
    
    def replace_zone(self, idx=None, zone=None):
        """"""
        return object
    
    def set_connection(self, nettype=None, addrtype=None, address=None, ttl=None, addr_number=None):
        """"""
        return object
    
    def set_information(self, information=None):
        """"""
        return object
    
    def set_key(self, type=None, data=None):
        """"""
        return object
    
    def set_origin(self, username=None, sess_id=None, sess_version=None, nettype=None, addrtype=None, addr=None):
        """"""
        return object
    
    def set_session_name(self, session_name=None):
        """"""
        return object
    
    def set_uri(self, uri=None):
        """"""
        return object
    
    def set_version(self, version=None):
        """"""
        return object
    
    def times_len(self):
        """"""
        return object
    
    def uninit(self):
        """"""
        return object
    
    def zones_len(self):
        """"""
        return object
    @staticmethod
    def as_uri(scheme=None, msg=None):
        """"""
        return object
    @staticmethod
    def new(msg=None):
        """"""
        return object
    @staticmethod
    def parse_buffer(data=None, size=None, msg=None):
        """"""
        return object
    @staticmethod
    def parse_uri(uri=None, msg=None):
        """"""
        return object

    @property
    def version(self):
        return object

    @property
    def origin(self):
        return object

    @property
    def session_name(self):
        return object

    @property
    def information(self):
        return object

    @property
    def uri(self):
        return object

    @property
    def emails(self):
        return object

    @property
    def phones(self):
        return object

    @property
    def connection(self):
        return object

    @property
    def bandwidths(self):
        return object

    @property
    def times(self):
        return object

    @property
    def zones(self):
        return object

    @property
    def key(self):
        return object

    @property
    def attributes(self):
        return object

    @property
    def medias(self):
        return object


class SDPOrigin():
    """"""

    @property
    def username(self):
        return object

    @property
    def sess_id(self):
        return object

    @property
    def sess_version(self):
        return object

    @property
    def nettype(self):
        return object

    @property
    def addrtype(self):
        return object

    @property
    def addr(self):
        return object


class SDPTime():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def set(self, start=None, stop=None, repeat=None):
        """"""
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def repeat(self):
        return object


class SDPZone():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def set(self, adj_time=None, typed_time=None):
        """"""
        return object

    @property
    def time(self):
        return object

    @property
    def typed_time(self):
        return object
