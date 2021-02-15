# -*- coding: utf-8 -*-


class RTSPAuthMethod:
    """"""
    NONE = 0
    BASIC = 1
    DIGEST = 2


class RTSPEvent:
    """"""
    READ = 1
    WRITE = 2


class RTSPFamily:
    """"""
    NONE = 0
    INET = 1
    INET6 = 2


class RTSPHeaderField:
    """"""
    INVALID = 0
    ACCEPT = 1
    ACCEPT_ENCODING = 2
    ACCEPT_LANGUAGE = 3
    ALLOW = 4
    AUTHORIZATION = 5
    BANDWIDTH = 6
    BLOCKSIZE = 7
    CACHE_CONTROL = 8
    CONFERENCE = 9
    CONNECTION = 10
    CONTENT_BASE = 11
    CONTENT_ENCODING = 12
    CONTENT_LANGUAGE = 13
    CONTENT_LENGTH = 14
    CONTENT_LOCATION = 15
    CONTENT_TYPE = 16
    CSEQ = 17
    DATE = 18
    EXPIRES = 19
    FROM = 20
    IF_MODIFIED_SINCE = 21
    LAST_MODIFIED = 22
    PROXY_AUTHENTICATE = 23
    PROXY_REQUIRE = 24
    PUBLIC = 25
    RANGE = 26
    REFERER = 27
    REQUIRE = 28
    RETRY_AFTER = 29
    RTP_INFO = 30
    SCALE = 31
    SESSION = 32
    SERVER = 33
    SPEED = 34
    TRANSPORT = 35
    UNSUPPORTED = 36
    USER_AGENT = 37
    VIA = 38
    WWW_AUTHENTICATE = 39
    CLIENT_CHALLENGE = 40
    REAL_CHALLENGE1 = 41
    REAL_CHALLENGE2 = 42
    REAL_CHALLENGE3 = 43
    SUBSCRIBE = 44
    ALERT = 45
    CLIENT_ID = 46
    COMPANY_ID = 47
    GUID = 48
    REGION_DATA = 49
    MAX_ASM_WIDTH = 50
    LANGUAGE = 51
    PLAYER_START_TIME = 52
    LOCATION = 53
    ETAG = 54
    IF_MATCH = 55
    ACCEPT_CHARSET = 56
    SUPPORTED = 57
    VARY = 58
    X_ACCELERATE_STREAMING = 59
    X_ACCEPT_AUTHENT = 60
    X_ACCEPT_PROXY_AUTHENT = 61
    X_BROADCAST_ID = 62
    X_BURST_STREAMING = 63
    X_NOTICE = 64
    X_PLAYER_LAG_TIME = 65
    X_PLAYLIST = 66
    X_PLAYLIST_CHANGE_NOTICE = 67
    X_PLAYLIST_GEN_ID = 68
    X_PLAYLIST_SEEK_ID = 69
    X_PROXY_CLIENT_AGENT = 70
    X_PROXY_CLIENT_VERB = 71
    X_RECEDING_PLAYLISTCHANGE = 72
    X_RTP_INFO = 73
    X_STARTUPPROFILE = 74
    TIMESTAMP = 75
    AUTHENTICATION_INFO = 76
    HOST = 77
    PRAGMA = 78
    X_SERVER_IP_ADDRESS = 79
    X_SESSIONCOOKIE = 80
    RTCP_INTERVAL = 81
    KEYMGMT = 82
    PIPELINED_REQUESTS = 83
    MEDIA_PROPERTIES = 84
    SEEK_STYLE = 85
    ACCEPT_RANGES = 86
    LAST = 87


class RTSPLowerTrans:
    """"""
    UNKNOWN = 0
    UDP = 1
    UDP_MCAST = 2
    TCP = 4
    HTTP = 16
    TLS = 32


class RTSPMethod:
    """"""
    INVALID = 0
    DESCRIBE = 1
    ANNOUNCE = 2
    GET_PARAMETER = 4
    OPTIONS = 8
    PAUSE = 16
    PLAY = 32
    RECORD = 64
    REDIRECT = 128
    SETUP = 256
    SET_PARAMETER = 512
    TEARDOWN = 1024
    GET = 2048
    POST = 4096


class RTSPMsgType:
    """"""
    INVALID = 0
    REQUEST = 1
    RESPONSE = 2
    HTTP_REQUEST = 3
    HTTP_RESPONSE = 4
    DATA = 5


class RTSPProfile:
    """"""
    UNKNOWN = 0
    AVP = 1
    SAVP = 2
    AVPF = 4
    SAVPF = 8


class RTSPRangeUnit:
    """"""
    SMPTE = 0
    SMPTE_30_DROP = 1
    SMPTE_25 = 2
    NPT = 3
    CLOCK = 4


class RTSPResult:
    """"""
    OK = 0
    ERROR = -1
    EINVAL = -2
    EINTR = -3
    ENOMEM = -4
    ERESOLV = -5
    ENOTIMPL = -6
    ESYS = -7
    EPARSE = -8
    EWSASTART = -9
    EWSAVERSION = -10
    EEOF = -11
    ENET = -12
    ENOTIP = -13
    ETIMEOUT = -14
    ETGET = -15
    ETPOST = -16
    ELAST = -17


class RTSPState:
    """"""
    INVALID = 0
    INIT = 1
    READY = 2
    SEEKING = 3
    PLAYING = 4
    RECORDING = 5


class RTSPStatusCode:
    """"""
    INVALID = 0
    CONTINUE = 100
    OK = 200
    CREATED = 201
    LOW_ON_STORAGE = 250
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    MOVE_TEMPORARILY = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTH_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_URI_TOO_LARGE = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    PARAMETER_NOT_UNDERSTOOD = 451
    CONFERENCE_NOT_FOUND = 452
    NOT_ENOUGH_BANDWIDTH = 453
    SESSION_NOT_FOUND = 454
    METHOD_NOT_VALID_IN_THIS_STATE = 455
    HEADER_FIELD_NOT_VALID_FOR_RESOURCE = 456
    INVALID_RANGE = 457
    PARAMETER_IS_READONLY = 458
    AGGREGATE_OPERATION_NOT_ALLOWED = 459
    ONLY_AGGREGATE_OPERATION_ALLOWED = 460
    UNSUPPORTED_TRANSPORT = 461
    DESTINATION_UNREACHABLE = 462
    KEY_MANAGEMENT_FAILURE = 463
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    RTSP_VERSION_NOT_SUPPORTED = 505
    OPTION_NOT_SUPPORTED = 551


class RTSPTimeType:
    """"""
    SECONDS = 0
    NOW = 1
    END = 2
    FRAMES = 3
    UTC = 4


class RTSPTransMode:
    """"""
    UNKNOWN = 0
    RTP = 1
    RDT = 2


class RTSPVersion:
    """"""
    INVALID = 0
    _1_0 = 16
    _1_1 = 17
    _2_0 = 32
RTSP_DEFAULT_PORT = r"""554"""

def rtsp_auth_credentials_free(credentials=None):
    """"""
    return object

def rtsp_connection_accept(socket=None, conn=None, cancellable=None):
    """"""
    return object

def rtsp_connection_create(url=None, conn=None):
    """"""
    return object

def rtsp_connection_create_from_socket(socket=None, ip=None, port=None, initial_buffer=None, conn=None):
    """"""
    return object

def rtsp_find_header_field(header=None):
    """"""
    return object

def rtsp_find_method(method=None):
    """"""
    return object

def rtsp_generate_digest_auth_response(algorithm=None, method=None, realm=None, username=None, password=None, uri=None, nonce=None):
    """"""
    return object

def rtsp_header_allow_multiple(field=None):
    """"""
    return object

def rtsp_header_as_text(field=None):
    """"""
    return object

def rtsp_message_new(msg=None):
    """"""
    return object

def rtsp_message_new_data(msg=None, channel=None):
    """"""
    return object

def rtsp_message_new_request(msg=None, method=None, uri=None):
    """"""
    return object

def rtsp_message_new_response(msg=None, code=None, reason=None, request=None):
    """"""
    return object

def rtsp_method_as_text(method=None):
    """"""
    return object

def rtsp_options_as_text(options=None):
    """"""
    return object

def rtsp_options_from_text(options=None):
    """"""
    return object

def rtsp_range_convert_units(range=None, unit=None):
    """"""
    return object

def rtsp_range_free(range=None):
    """"""
    return object

def rtsp_range_get_times(range=None, min=None, max=None):
    """"""
    return object

def rtsp_range_parse(rangestr=None, range=None):
    """"""
    return object

def rtsp_range_to_string(range=None):
    """"""
    return object

def rtsp_status_as_text(code=None):
    """"""
    return object

def rtsp_strresult(result=None):
    """"""
    return object

def rtsp_transport_get_manager(trans=None, manager=None, option=None):
    """"""
    return object

def rtsp_transport_get_mime(trans=None, mime=None):
    """"""
    return object

def rtsp_transport_new(transport=None):
    """"""
    return object

def rtsp_transport_parse(str=None, transport=None):
    """"""
    return object

def rtsp_url_parse(urlstr=None, url=None):
    """"""
    return object

def rtsp_version_as_text(version=None):
    """"""
    return object

def rtsp_watch_new(conn=None, funcs=None, user_data=None, notify=None):
    """"""
    return object


class RTSPAuthCredential():
    """"""

    @property
    def scheme(self):
        return object

    @property
    def params(self):
        return object

    @property
    def authorization(self):
        return object


class RTSPAuthParam():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object

    @property
    def name(self):
        return object

    @property
    def value(self):
        return object


class RTSPConnection():
    """"""
    
    def clear_auth_params(self):
        """"""
        return object
    
    def close(self):
        """"""
        return object
    
    def connect(self, timeout=None):
        """"""
        return object
    
    def connect_with_response(self, timeout=None, response=None):
        """"""
        return object
    
    def do_tunnel(self, conn2=None):
        """"""
        return object
    
    def flush(self, flush=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_ip(self):
        """"""
        return object
    
    def get_read_socket(self):
        """"""
        return object
    
    def get_remember_session_id(self):
        """"""
        return object
    
    def get_tls(self):
        """"""
        return object
    
    def get_tls_database(self):
        """"""
        return object
    
    def get_tls_interaction(self):
        """"""
        return object
    
    def get_tls_validation_flags(self):
        """"""
        return object
    
    def get_tunnelid(self):
        """"""
        return object
    
    def get_url(self):
        """"""
        return object
    
    def get_write_socket(self):
        """"""
        return object
    
    def is_tunneled(self):
        """"""
        return object
    
    def next_timeout(self, timeout=None):
        """"""
        return object
    
    def poll(self, events=None, revents=None, timeout=None):
        """"""
        return object
    
    def read(self, data=None, size=None, timeout=None):
        """"""
        return object
    
    def receive(self, message=None, timeout=None):
        """"""
        return object
    
    def reset_timeout(self):
        """"""
        return object
    
    def send(self, message=None, timeout=None):
        """"""
        return object
    
    def set_accept_certificate_func(self, func=None, user_data=None, destroy_notify=None):
        """"""
        return object
    
    def set_auth(self, method=None, user=None, _pass=None):
        """"""
        return object
    
    def set_auth_param(self, param=None, value=None):
        """"""
        return object
    
    def set_http_mode(self, enable=None):
        """"""
        return object
    
    def set_ip(self, ip=None):
        """"""
        return object
    
    def set_proxy(self, host=None, port=None):
        """"""
        return object
    
    def set_qos_dscp(self, qos_dscp=None):
        """"""
        return object
    
    def set_remember_session_id(self, remember=None):
        """"""
        return object
    
    def set_tls_database(self, database=None):
        """"""
        return object
    
    def set_tls_interaction(self, interaction=None):
        """"""
        return object
    
    def set_tls_validation_flags(self, flags=None):
        """"""
        return object
    
    def set_tunneled(self, tunneled=None):
        """"""
        return object
    
    def write(self, data=None, size=None, timeout=None):
        """"""
        return object
    @staticmethod
    def accept(socket=None, conn=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def create(url=None, conn=None):
        """"""
        return object
    @staticmethod
    def create_from_socket(socket=None, ip=None, port=None, initial_buffer=None, conn=None):
        """"""
        return object


class RTSPExtension():
    """"""
    
    def after_send(self, req=None, resp=None):
        """"""
        return object
    
    def before_send(self, req=None):
        """"""
        return object
    
    def configure_stream(self, caps=None):
        """"""
        return object
    
    def detect_server(self, resp=None):
        """"""
        return object
    
    def get_transports(self, protocols=None, transport=None):
        """"""
        return object
    
    def parse_sdp(self, sdp=None, s=None):
        """"""
        return object
    
    def receive_request(self, req=None):
        """"""
        return object
    
    def send(self, req=None, resp=None):
        """"""
        return object
    
    def setup_media(self, media=None):
        """"""
        return object
    
    def stream_select(self, url=None):
        """"""
        return object
    
    def after_send(self, req=None, resp=None):
        """"""
        return object
    
    def before_send(self, req=None):
        """"""
        return object
    
    def configure_stream(self, caps=None):
        """"""
        return object
    
    def detect_server(self, resp=None):
        """"""
        return object
    
    def get_transports(self, protocols=None, transport=None):
        """"""
        return object
    
    def parse_sdp(self, sdp=None, s=None):
        """"""
        return object
    
    def receive_request(self, req=None):
        """"""
        return object
    
    def send(self, req=None, resp=None):
        """"""
        return object
    
    def setup_media(self, media=None):
        """"""
        return object
    
    def stream_select(self, url=None):
        """"""
        return object


class RTSPExtensionInterface():
    """"""

    @property
    def parent(self):
        return object

    @property
    def detect_server(self):
        return object

    @property
    def before_send(self):
        return object

    @property
    def after_send(self):
        return object

    @property
    def parse_sdp(self):
        return object

    @property
    def setup_media(self):
        return object

    @property
    def configure_stream(self):
        return object

    @property
    def get_transports(self):
        return object

    @property
    def stream_select(self):
        return object

    @property
    def send(self):
        return object

    @property
    def receive_request(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTSPMessage():
    """"""
    
    def add_header(self, field=None, value=None):
        """"""
        return object
    
    def add_header_by_name(self, header=None, value=None):
        """"""
        return object
    
    def append_headers(self, str=None):
        """"""
        return object
    
    def copy(self, copy=None):
        """"""
        return object
    
    def dump(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_body(self, data=None, size=None):
        """"""
        return object
    
    def get_header(self, field=None, value=None, indx=None):
        """"""
        return object
    
    def get_header_by_name(self, header=None, value=None, index=None):
        """"""
        return object
    
    def get_type(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def init_data(self, channel=None):
        """"""
        return object
    
    def init_request(self, method=None, uri=None):
        """"""
        return object
    
    def init_response(self, code=None, reason=None, request=None):
        """"""
        return object
    
    def parse_auth_credentials(self, field=None):
        """"""
        return object
    
    def parse_data(self, channel=None):
        """"""
        return object
    
    def parse_request(self, method=None, uri=None, version=None):
        """"""
        return object
    
    def parse_response(self, code=None, reason=None, version=None):
        """"""
        return object
    
    def remove_header(self, field=None, indx=None):
        """"""
        return object
    
    def remove_header_by_name(self, header=None, index=None):
        """"""
        return object
    
    def set_body(self, data=None, size=None):
        """"""
        return object
    
    def steal_body(self, data=None, size=None):
        """"""
        return object
    
    def take_body(self, data=None, size=None):
        """"""
        return object
    
    def take_header(self, field=None, value=None):
        """"""
        return object
    
    def take_header_by_name(self, header=None, value=None):
        """"""
        return object
    
    def unset(self):
        """"""
        return object

    @property
    def type(self):
        return object

    @property
    def hdr_fields(self):
        return object

    @property
    def body(self):
        return object

    @property
    def body_size(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTSPRange():
    """"""
    @staticmethod
    def convert_units(range=None, unit=None):
        """"""
        return object
    @staticmethod
    def free(range=None):
        """"""
        return object
    @staticmethod
    def get_times(range=None, min=None, max=None):
        """"""
        return object
    @staticmethod
    def parse(rangestr=None, range=None):
        """"""
        return object
    @staticmethod
    def to_string(range=None):
        """"""
        return object

    @property
    def min(self):
        return object

    @property
    def max(self):
        return object


class RTSPTime():
    """"""

    @property
    def type(self):
        return object

    @property
    def seconds(self):
        return object


class RTSPTime2():
    """"""

    @property
    def frames(self):
        return object

    @property
    def year(self):
        return object

    @property
    def month(self):
        return object

    @property
    def day(self):
        return object


class RTSPTimeRange():
    """"""

    @property
    def unit(self):
        return object

    @property
    def min(self):
        return object

    @property
    def max(self):
        return object

    @property
    def min2(self):
        return object

    @property
    def max2(self):
        return object


class RTSPTransport():
    """"""
    
    def as_text(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_media_type(self, media_type=None):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    @staticmethod
    def get_manager(trans=None, manager=None, option=None):
        """"""
        return object
    @staticmethod
    def get_mime(trans=None, mime=None):
        """"""
        return object
    @staticmethod
    def new(transport=None):
        """"""
        return object
    @staticmethod
    def parse(str=None, transport=None):
        """"""
        return object

    @property
    def trans(self):
        return object

    @property
    def profile(self):
        return object

    @property
    def lower_transport(self):
        return object

    @property
    def destination(self):
        return object

    @property
    def source(self):
        return object

    @property
    def layers(self):
        return object

    @property
    def mode_play(self):
        return object

    @property
    def mode_record(self):
        return object

    @property
    def append(self):
        return object

    @property
    def interleaved(self):
        return object

    @property
    def ttl(self):
        return object

    @property
    def port(self):
        return object

    @property
    def client_port(self):
        return object

    @property
    def server_port(self):
        return object

    @property
    def ssrc(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class RTSPUrl():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def decode_path_components(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_port(self, port=None):
        """"""
        return object
    
    def get_request_uri(self):
        """"""
        return object
    
    def set_port(self, port=None):
        """"""
        return object
    @staticmethod
    def parse(urlstr=None, url=None):
        """"""
        return object

    @property
    def transports(self):
        return object

    @property
    def family(self):
        return object

    @property
    def user(self):
        return object

    @property
    def passwd(self):
        return object

    @property
    def host(self):
        return object

    @property
    def port(self):
        return object

    @property
    def abspath(self):
        return object

    @property
    def query(self):
        return object


class RTSPWatch():
    """"""
    
    def attach(self, context=None):
        """"""
        return object
    
    def get_send_backlog(self, bytes=None, messages=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def send_message(self, message=None, id=None):
        """"""
        return object
    
    def set_flushing(self, flushing=None):
        """"""
        return object
    
    def set_send_backlog(self, bytes=None, messages=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def wait_backlog(self, timeout=None):
        """"""
        return object
    
    def write_data(self, data=None, size=None, id=None):
        """"""
        return object
    @staticmethod
    def new(conn=None, funcs=None, user_data=None, notify=None):
        """"""
        return object


class RTSPWatchFuncs():
    """"""

    @property
    def message_received(self):
        return object

    @property
    def message_sent(self):
        return object

    @property
    def closed(self):
        return object

    @property
    def error(self):
        return object

    @property
    def tunnel_start(self):
        return object

    @property
    def tunnel_complete(self):
        return object

    @property
    def error_full(self):
        return object

    @property
    def tunnel_lost(self):
        return object

    @property
    def tunnel_http_response(self):
        return object

    @property
    def _gst_reserved(self):
        return object
