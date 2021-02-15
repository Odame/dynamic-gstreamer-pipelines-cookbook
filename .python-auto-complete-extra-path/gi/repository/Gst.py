# -*- coding: utf-8 -*-
from gi.repository import GObject
ALLOCATOR_SYSMEM = r"""SystemMemory"""


class AllocatorFlags:
    """"""
    CUSTOM_ALLOC = 16
    LAST = 1048576


BUFFER_COPY_ALL = r"""15"""
BUFFER_COPY_METADATA = r"""7"""
BUFFER_OFFSET_NONE = r"""18446744073709551615"""


class BinFlags:
    """"""
    NO_RESYNC = 16384
    STREAMS_AWARE = 32768
    LAST = 524288


class BufferCopyFlags:
    """"""
    NONE = 0
    FLAGS = 1
    TIMESTAMPS = 2
    META = 4
    MEMORY = 8
    MERGE = 16
    DEEP = 32


class BufferFlags:
    """"""
    LIVE = 16
    DECODE_ONLY = 32
    DISCONT = 64
    RESYNC = 128
    CORRUPTED = 256
    MARKER = 512
    HEADER = 1024
    GAP = 2048
    DROPPABLE = 4096
    DELTA_UNIT = 8192
    TAG_MEMORY = 16384
    SYNC_AFTER = 32768
    NON_DROPPABLE = 65536
    LAST = 1048576


class BufferPoolAcquireFlags:
    """"""
    NONE = 0
    KEY_UNIT = 1
    DONTWAIT = 2
    DISCONT = 4
    LAST = 65536


class BufferingMode:
    """"""
    STREAM = 0
    DOWNLOAD = 1
    TIMESHIFT = 2
    LIVE = 3


class BusFlags:
    """"""
    FLUSHING = 16
    FLAG_LAST = 32


class BusSyncReply:
    """"""
    DROP = 0
    PASS = 1
    ASYNC = 2


CAN_INLINE = r"""1"""
CAPS_FEATURE_MEMORY_SYSTEM_MEMORY = r"""memory:SystemMemory"""
CLOCK_TIME_NONE = r"""18446744073709551615"""


class CapsFlags:
    """"""
    ANY = 16


class CapsIntersectMode:
    """"""
    ZIG_ZAG = 0
    FIRST = 1


class ClockEntryType:
    """"""
    SINGLE = 0
    PERIODIC = 1


class ClockFlags:
    """"""
    CAN_DO_SINGLE_SYNC = 16
    CAN_DO_SINGLE_ASYNC = 32
    CAN_DO_PERIODIC_SYNC = 64
    CAN_DO_PERIODIC_ASYNC = 128
    CAN_SET_RESOLUTION = 256
    CAN_SET_MASTER = 512
    NEEDS_STARTUP_SYNC = 1024
    LAST = 4096


class ClockReturn:
    """"""
    OK = 0
    EARLY = 1
    UNSCHEDULED = 2
    BUSY = 3
    BADTIME = 4
    ERROR = 5
    UNSUPPORTED = 6
    DONE = 7


class ClockType:
    """"""
    REALTIME = 0
    MONOTONIC = 1
    OTHER = 2


class CoreError:
    """"""
    FAILED = 1
    TOO_LAZY = 2
    NOT_IMPLEMENTED = 3
    STATE_CHANGE = 4
    PAD = 5
    THREAD = 6
    NEGOTIATION = 7
    EVENT = 8
    SEEK = 9
    CAPS = 10
    TAG = 11
    MISSING_PLUGIN = 12
    CLOCK = 13
    DISABLED = 14
    NUM_ERRORS = 15


DEBUG_BG_MASK = r"""240"""
DEBUG_FG_MASK = r"""15"""
DEBUG_FORMAT_MASK = r"""65280"""


class DebugColorFlags:
    """"""
    FG_BLACK = 0
    FG_RED = 1
    FG_GREEN = 2
    FG_YELLOW = 3
    FG_BLUE = 4
    FG_MAGENTA = 5
    FG_CYAN = 6
    FG_WHITE = 7
    BG_BLACK = 0
    BG_RED = 16
    BG_GREEN = 32
    BG_YELLOW = 48
    BG_BLUE = 64
    BG_MAGENTA = 80
    BG_CYAN = 96
    BG_WHITE = 112
    BOLD = 256
    UNDERLINE = 512


class DebugColorMode:
    """"""
    OFF = 0
    ON = 1
    UNIX = 2


class DebugGraphDetails:
    """"""
    MEDIA_TYPE = 1
    CAPS_DETAILS = 2
    NON_DEFAULT_PARAMS = 4
    STATES = 8
    FULL_PARAMS = 16
    ALL = 15
    VERBOSE = -1


class DebugLevel:
    """"""
    NONE = 0
    ERROR = 1
    WARNING = 2
    FIXME = 3
    INFO = 4
    DEBUG = 5
    LOG = 6
    TRACE = 7
    MEMDUMP = 9
    COUNT = 10


ELEMENT_FACTORY_KLASS_DECODER = r"""Decoder"""
ELEMENT_FACTORY_KLASS_DECRYPTOR = r"""Decryptor"""
ELEMENT_FACTORY_KLASS_DEMUXER = r"""Demuxer"""
ELEMENT_FACTORY_KLASS_DEPAYLOADER = r"""Depayloader"""
ELEMENT_FACTORY_KLASS_ENCODER = r"""Encoder"""
ELEMENT_FACTORY_KLASS_ENCRYPTOR = r"""Encryptor"""
ELEMENT_FACTORY_KLASS_FORMATTER = r"""Formatter"""
ELEMENT_FACTORY_KLASS_MEDIA_AUDIO = r"""Audio"""
ELEMENT_FACTORY_KLASS_MEDIA_IMAGE = r"""Image"""
ELEMENT_FACTORY_KLASS_MEDIA_METADATA = r"""Metadata"""
ELEMENT_FACTORY_KLASS_MEDIA_SUBTITLE = r"""Subtitle"""
ELEMENT_FACTORY_KLASS_MEDIA_VIDEO = r"""Video"""
ELEMENT_FACTORY_KLASS_MUXER = r"""Muxer"""
ELEMENT_FACTORY_KLASS_PARSER = r"""Parser"""
ELEMENT_FACTORY_KLASS_PAYLOADER = r"""Payloader"""
ELEMENT_FACTORY_KLASS_SINK = r"""Sink"""
ELEMENT_FACTORY_KLASS_SRC = r"""Source"""
ELEMENT_FACTORY_TYPE_ANY = r"""562949953421311"""
ELEMENT_FACTORY_TYPE_AUDIOVIDEO_SINKS = r"""3940649673949188"""
ELEMENT_FACTORY_TYPE_AUDIO_ENCODER = r"""1125899906842626"""
ELEMENT_FACTORY_TYPE_DECODABLE = r"""1377"""
ELEMENT_FACTORY_TYPE_DECODER = r"""1"""
ELEMENT_FACTORY_TYPE_DECRYPTOR = r"""1024"""
ELEMENT_FACTORY_TYPE_DEMUXER = r"""32"""
ELEMENT_FACTORY_TYPE_DEPAYLOADER = r"""256"""
ELEMENT_FACTORY_TYPE_ENCODER = r"""2"""
ELEMENT_FACTORY_TYPE_ENCRYPTOR = r"""2048"""
ELEMENT_FACTORY_TYPE_FORMATTER = r"""512"""
ELEMENT_FACTORY_TYPE_MAX_ELEMENTS = r"""281474976710656"""
ELEMENT_FACTORY_TYPE_MEDIA_ANY = r"""18446462598732840960"""
ELEMENT_FACTORY_TYPE_MEDIA_AUDIO = r"""1125899906842624"""
ELEMENT_FACTORY_TYPE_MEDIA_IMAGE = r"""2251799813685248"""
ELEMENT_FACTORY_TYPE_MEDIA_METADATA = r"""9007199254740992"""
ELEMENT_FACTORY_TYPE_MEDIA_SUBTITLE = r"""4503599627370496"""
ELEMENT_FACTORY_TYPE_MEDIA_VIDEO = r"""562949953421312"""
ELEMENT_FACTORY_TYPE_MUXER = r"""16"""
ELEMENT_FACTORY_TYPE_PARSER = r"""64"""
ELEMENT_FACTORY_TYPE_PAYLOADER = r"""128"""
ELEMENT_FACTORY_TYPE_SINK = r"""4"""
ELEMENT_FACTORY_TYPE_SRC = r"""8"""
ELEMENT_FACTORY_TYPE_VIDEO_ENCODER = r"""2814749767106562"""
ELEMENT_METADATA_AUTHOR = r"""author"""
ELEMENT_METADATA_DESCRIPTION = r"""description"""
ELEMENT_METADATA_DOC_URI = r"""doc-uri"""
ELEMENT_METADATA_ICON_NAME = r"""icon-name"""
ELEMENT_METADATA_KLASS = r"""klass"""
ELEMENT_METADATA_LONGNAME = r"""long-name"""
ERROR_SYSTEM = r"""system error: %s"""
EVENT_NUM_SHIFT = r"""8"""
EVENT_TYPE_BOTH = r"""3"""


class ElementFlags:
    """"""
    LOCKED_STATE = 16
    SINK = 32
    SOURCE = 64
    PROVIDE_CLOCK = 128
    REQUIRE_CLOCK = 256
    INDEXABLE = 512
    LAST = 16384


class EventType:
    """"""
    UNKNOWN = 0
    FLUSH_START = 2563
    FLUSH_STOP = 5127
    STREAM_START = 10254
    CAPS = 12814
    SEGMENT = 17934
    STREAM_COLLECTION = 19230
    TAG = 20510
    BUFFERSIZE = 23054
    SINK_MESSAGE = 25630
    STREAM_GROUP_DONE = 26894
    EOS = 28174
    TOC = 30750
    PROTECTION = 33310
    SEGMENT_DONE = 38406
    GAP = 40966
    QOS = 48641
    SEEK = 51201
    NAVIGATION = 53761
    LATENCY = 56321
    STEP = 58881
    RECONFIGURE = 61441
    TOC_SELECT = 64001
    SELECT_STREAMS = 66561
    CUSTOM_UPSTREAM = 69121
    CUSTOM_DOWNSTREAM = 71686
    CUSTOM_DOWNSTREAM_OOB = 74242
    CUSTOM_DOWNSTREAM_STICKY = 76830
    CUSTOM_BOTH = 79367
    CUSTOM_BOTH_OOB = 81923


class EventTypeFlags:
    """"""
    UPSTREAM = 1
    DOWNSTREAM = 2
    SERIALIZED = 4
    STICKY = 8
    STICKY_MULTI = 16


FLAG_SET_MASK_EXACT = r"""4294967295"""
FORMAT_PERCENT_MAX = r"""1000000"""
FORMAT_PERCENT_SCALE = r"""10000"""
FOURCC_FORMAT = r"""c%c%c%c"""


class FlowReturn:
    """"""
    CUSTOM_SUCCESS_2 = 102
    CUSTOM_SUCCESS_1 = 101
    CUSTOM_SUCCESS = 100
    OK = 0
    NOT_LINKED = -1
    FLUSHING = -2
    EOS = -3
    NOT_NEGOTIATED = -4
    ERROR = -5
    NOT_SUPPORTED = -6
    CUSTOM_ERROR = -100
    CUSTOM_ERROR_1 = -101
    CUSTOM_ERROR_2 = -102


class Format:
    """"""
    UNDEFINED = 0
    DEFAULT = 1
    BYTES = 2
    TIME = 3
    BUFFERS = 4
    PERCENT = 5


GROUP_ID_INVALID = r"""0"""


class IteratorItem:
    """"""
    SKIP = 0
    PASS = 1
    END = 2


class IteratorResult:
    """"""
    DONE = 0
    OK = 1
    RESYNC = 2
    ERROR = 3


LICENSE_UNKNOWN = r"""unknown"""
LOCK_FLAG_READWRITE = r"""3"""


class LibraryError:
    """"""
    FAILED = 1
    TOO_LAZY = 2
    INIT = 3
    SHUTDOWN = 4
    SETTINGS = 5
    ENCODE = 6
    NUM_ERRORS = 7


class LockFlags:
    """"""
    READ = 1
    WRITE = 2
    EXCLUSIVE = 4
    LAST = 256


MAP_READWRITE = r"""3"""
META_TAG_MEMORY_STR = r"""memory"""
MSECOND = r"""1000000"""


class MapFlags:
    """"""
    READ = 1
    WRITE = 2
    FLAG_LAST = 65536


class MemoryFlags:
    """"""
    READONLY = 2
    NO_SHARE = 16
    ZERO_PREFIXED = 32
    ZERO_PADDED = 64
    PHYSICALLY_CONTIGUOUS = 128
    NOT_MAPPABLE = 256
    LAST = 1048576


class MessageType:
    """"""
    UNKNOWN = 0
    EOS = 1
    ERROR = 2
    WARNING = 4
    INFO = 8
    TAG = 16
    BUFFERING = 32
    STATE_CHANGED = 64
    STATE_DIRTY = 128
    STEP_DONE = 256
    CLOCK_PROVIDE = 512
    CLOCK_LOST = 1024
    NEW_CLOCK = 2048
    STRUCTURE_CHANGE = 4096
    STREAM_STATUS = 8192
    APPLICATION = 16384
    ELEMENT = 32768
    SEGMENT_START = 65536
    SEGMENT_DONE = 131072
    DURATION_CHANGED = 262144
    LATENCY = 524288
    ASYNC_START = 1048576
    ASYNC_DONE = 2097152
    REQUEST_STATE = 4194304
    STEP_START = 8388608
    QOS = 16777216
    PROGRESS = 33554432
    TOC = 67108864
    RESET_TIME = 134217728
    STREAM_START = 268435456
    NEED_CONTEXT = 536870912
    HAVE_CONTEXT = 1073741824
    EXTENDED = 2147483648
    DEVICE_ADDED = 2147483649
    DEVICE_REMOVED = 2147483650
    PROPERTY_NOTIFY = 2147483651
    STREAM_COLLECTION = 2147483652
    STREAMS_SELECTED = 2147483653
    REDIRECT = 2147483654
    ANY = 4294967295


class MetaFlags:
    """"""
    NONE = 0
    READONLY = 1
    POOLED = 2
    LOCKED = 4
    LAST = 65536


class MiniObjectFlags:
    """"""
    LOCKABLE = 1
    LOCK_READONLY = 2
    MAY_BE_LEAKED = 4
    LAST = 16


NSECOND = r"""1"""


class ObjectFlags:
    """"""
    MAY_BE_LEAKED = 1
    LAST = 16


PARAM_CONTROLLABLE = r"""512"""
PARAM_MUTABLE_PAUSED = r"""2048"""
PARAM_MUTABLE_PLAYING = r"""4096"""
PARAM_MUTABLE_READY = r"""1024"""
PARAM_USER_SHIFT = r"""65536"""
PROTECTION_SYSTEM_ID_CAPS_FIELD = r"""protection-system"""
PTR_FORMAT = r"""paA"""


class PadDirection:
    """"""
    UNKNOWN = 0
    SRC = 1
    SINK = 2


class PadFlags:
    """"""
    BLOCKED = 16
    FLUSHING = 32
    EOS = 64
    BLOCKING = 128
    NEED_PARENT = 256
    NEED_RECONFIGURE = 512
    PENDING_EVENTS = 1024
    FIXED_CAPS = 2048
    PROXY_CAPS = 4096
    PROXY_ALLOCATION = 8192
    PROXY_SCHEDULING = 16384
    ACCEPT_INTERSECT = 32768
    ACCEPT_TEMPLATE = 65536
    LAST = 1048576


class PadLinkCheck:
    """"""
    NOTHING = 0
    HIERARCHY = 1
    TEMPLATE_CAPS = 2
    CAPS = 4
    NO_RECONFIGURE = 8
    DEFAULT = 5


class PadLinkReturn:
    """"""
    OK = 0
    WRONG_HIERARCHY = -1
    WAS_LINKED = -2
    WRONG_DIRECTION = -3
    NOFORMAT = -4
    NOSCHED = -5
    REFUSED = -6


class PadMode:
    """"""
    NONE = 0
    PUSH = 1
    PULL = 2


class PadPresence:
    """"""
    ALWAYS = 0
    SOMETIMES = 1
    REQUEST = 2


class PadProbeReturn:
    """"""
    DROP = 0
    OK = 1
    REMOVE = 2
    PASS = 3
    HANDLED = 4


class PadProbeType:
    """"""
    INVALID = 0
    IDLE = 1
    BLOCK = 2
    BUFFER = 16
    BUFFER_LIST = 32
    EVENT_DOWNSTREAM = 64
    EVENT_UPSTREAM = 128
    EVENT_FLUSH = 256
    QUERY_DOWNSTREAM = 512
    QUERY_UPSTREAM = 1024
    PUSH = 4096
    PULL = 8192
    BLOCKING = 3
    DATA_DOWNSTREAM = 112
    DATA_UPSTREAM = 128
    DATA_BOTH = 240
    BLOCK_DOWNSTREAM = 114
    BLOCK_UPSTREAM = 130
    EVENT_BOTH = 192
    QUERY_BOTH = 1536
    ALL_BOTH = 1776
    SCHEDULING = 12288


class PadTemplateFlags:
    """"""
    LAST = 256


class ParseError:
    """"""
    SYNTAX = 0
    NO_SUCH_ELEMENT = 1
    NO_SUCH_PROPERTY = 2
    LINK = 3
    COULD_NOT_SET_PROPERTY = 4
    EMPTY_BIN = 5
    EMPTY = 6
    DELAYED_LINK = 7


class ParseFlags:
    """"""
    NONE = 0
    FATAL_ERRORS = 1
    NO_SINGLE_ELEMENT_BINS = 2
    PLACE_IN_BIN = 4


class PipelineFlags:
    """"""
    FIXED_CLOCK = 524288
    LAST = 8388608


class PluginDependencyFlags:
    """"""
    NONE = 0
    RECURSE = 1
    PATHS_ARE_DEFAULT_ONLY = 2
    FILE_NAME_IS_SUFFIX = 4
    FILE_NAME_IS_PREFIX = 8
    PATHS_ARE_RELATIVE_TO_EXE = 16


class PluginError:
    """"""
    MODULE = 0
    DEPENDENCIES = 1
    NAME_MISMATCH = 2


class PluginFlags:
    """"""
    CACHED = 16
    BLACKLISTED = 32


class ProgressType:
    """"""
    START = 0
    CONTINUE = 1
    COMPLETE = 2
    CANCELED = 3
    ERROR = 4


class PromiseResult:
    """"""
    PENDING = 0
    INTERRUPTED = 1
    REPLIED = 2
    EXPIRED = 3


class QOSType:
    """"""
    OVERFLOW = 0
    UNDERFLOW = 1
    THROTTLE = 2


QUERY_NUM_SHIFT = r"""8"""
QUERY_TYPE_BOTH = r"""3"""


class QueryType:
    """"""
    UNKNOWN = 0
    POSITION = 2563
    DURATION = 5123
    LATENCY = 7683
    JITTER = 10243
    RATE = 12803
    SEEKING = 15363
    SEGMENT = 17923
    CONVERT = 20483
    FORMATS = 23043
    BUFFERING = 28163
    CUSTOM = 30723
    URI = 33283
    ALLOCATION = 35846
    SCHEDULING = 38401
    ACCEPT_CAPS = 40963
    CAPS = 43523
    DRAIN = 46086
    CONTEXT = 48643


class QueryTypeFlags:
    """"""
    UPSTREAM = 1
    DOWNSTREAM = 2
    SERIALIZED = 4


class Rank:
    """"""
    NONE = 0
    MARGINAL = 64
    SECONDARY = 128
    PRIMARY = 256


class ResourceError:
    """"""
    FAILED = 1
    TOO_LAZY = 2
    NOT_FOUND = 3
    BUSY = 4
    OPEN_READ = 5
    OPEN_WRITE = 6
    OPEN_READ_WRITE = 7
    CLOSE = 8
    READ = 9
    WRITE = 10
    SEEK = 11
    SYNC = 12
    SETTINGS = 13
    NO_SPACE_LEFT = 14
    NOT_AUTHORIZED = 15
    NUM_ERRORS = 16


SECOND = r"""1000000000"""
SEGMENT_FORMAT = r"""paB"""
SEQNUM_INVALID = r"""0"""
STIME_FORMAT = r"""c%"""


class SchedulingFlags:
    """"""
    SEEKABLE = 1
    SEQUENTIAL = 2
    BANDWIDTH_LIMITED = 4


class SearchMode:
    """"""
    EXACT = 0
    BEFORE = 1
    AFTER = 2


class SeekFlags:
    """"""
    NONE = 0
    FLUSH = 1
    ACCURATE = 2
    KEY_UNIT = 4
    SEGMENT = 8
    TRICKMODE = 16
    SKIP = 16
    SNAP_BEFORE = 32
    SNAP_AFTER = 64
    SNAP_NEAREST = 96
    TRICKMODE_KEY_UNITS = 128
    TRICKMODE_NO_AUDIO = 256


class SeekType:
    """"""
    NONE = 0
    SET = 1
    END = 2


class SegmentFlags:
    """"""
    NONE = 0
    RESET = 1
    TRICKMODE = 16
    SKIP = 16
    SEGMENT = 8
    TRICKMODE_KEY_UNITS = 128
    TRICKMODE_NO_AUDIO = 256


class StackTraceFlags:
    """"""
    FULL = 1


class State:
    """"""
    VOID_PENDING = 0
    NULL = 1
    READY = 2
    PAUSED = 3
    PLAYING = 4


class StateChange:
    """"""
    NULL_TO_READY = 10
    READY_TO_PAUSED = 19
    PAUSED_TO_PLAYING = 28
    PLAYING_TO_PAUSED = 35
    PAUSED_TO_READY = 26
    READY_TO_NULL = 17
    NULL_TO_NULL = 9
    READY_TO_READY = 18
    PAUSED_TO_PAUSED = 27
    PLAYING_TO_PLAYING = 36


class StateChangeReturn:
    """"""
    FAILURE = 0
    SUCCESS = 1
    ASYNC = 2
    NO_PREROLL = 3


class StreamError:
    """"""
    FAILED = 1
    TOO_LAZY = 2
    NOT_IMPLEMENTED = 3
    TYPE_NOT_FOUND = 4
    WRONG_TYPE = 5
    CODEC_NOT_FOUND = 6
    DECODE = 7
    ENCODE = 8
    DEMUX = 9
    MUX = 10
    FORMAT = 11
    DECRYPT = 12
    DECRYPT_NOKEY = 13
    NUM_ERRORS = 14


class StreamFlags:
    """"""
    NONE = 0
    SPARSE = 1
    SELECT = 2
    UNSELECT = 4


class StreamStatusType:
    """"""
    CREATE = 0
    ENTER = 1
    LEAVE = 2
    DESTROY = 3
    START = 8
    PAUSE = 9
    STOP = 10


class StreamType:
    """"""
    UNKNOWN = 1
    AUDIO = 2
    VIDEO = 4
    CONTAINER = 8
    TEXT = 16


class StructureChangeType:
    """"""
    LINK = 0
    UNLINK = 1


TAG_ALBUM = r"""album"""
TAG_ALBUM_ARTIST = r"""album-artist"""
TAG_ALBUM_ARTIST_SORTNAME = r"""album-artist-sortname"""
TAG_ALBUM_GAIN = r"""replaygain-album-gain"""
TAG_ALBUM_PEAK = r"""replaygain-album-peak"""
TAG_ALBUM_SORTNAME = r"""album-sortname"""
TAG_ALBUM_VOLUME_COUNT = r"""album-disc-count"""
TAG_ALBUM_VOLUME_NUMBER = r"""album-disc-number"""
TAG_APPLICATION_DATA = r"""application-data"""
TAG_APPLICATION_NAME = r"""application-name"""
TAG_ARTIST = r"""artist"""
TAG_ARTIST_SORTNAME = r"""artist-sortname"""
TAG_ATTACHMENT = r"""attachment"""
TAG_AUDIO_CODEC = r"""audio-codec"""
TAG_BEATS_PER_MINUTE = r"""beats-per-minute"""
TAG_BITRATE = r"""bitrate"""
TAG_CODEC = r"""codec"""
TAG_COMMENT = r"""comment"""
TAG_COMPOSER = r"""composer"""
TAG_COMPOSER_SORTNAME = r"""composer-sortname"""
TAG_CONDUCTOR = r"""conductor"""
TAG_CONTACT = r"""contact"""
TAG_CONTAINER_FORMAT = r"""container-format"""
TAG_COPYRIGHT = r"""copyright"""
TAG_COPYRIGHT_URI = r"""copyright-uri"""
TAG_DATE = r"""date"""
TAG_DATE_TIME = r"""datetime"""
TAG_DESCRIPTION = r"""description"""
TAG_DEVICE_MANUFACTURER = r"""device-manufacturer"""
TAG_DEVICE_MODEL = r"""device-model"""
TAG_DURATION = r"""duration"""
TAG_ENCODED_BY = r"""encoded-by"""
TAG_ENCODER = r"""encoder"""
TAG_ENCODER_VERSION = r"""encoder-version"""
TAG_EXTENDED_COMMENT = r"""extended-comment"""
TAG_GENRE = r"""genre"""
TAG_GEO_LOCATION_CAPTURE_DIRECTION = r"""geo-location-capture-direction"""
TAG_GEO_LOCATION_CITY = r"""geo-location-city"""
TAG_GEO_LOCATION_COUNTRY = r"""geo-location-country"""
TAG_GEO_LOCATION_ELEVATION = r"""geo-location-elevation"""
TAG_GEO_LOCATION_HORIZONTAL_ERROR = r"""geo-location-horizontal-error"""
TAG_GEO_LOCATION_LATITUDE = r"""geo-location-latitude"""
TAG_GEO_LOCATION_LONGITUDE = r"""geo-location-longitude"""
TAG_GEO_LOCATION_MOVEMENT_DIRECTION = r"""geo-location-movement-direction"""
TAG_GEO_LOCATION_MOVEMENT_SPEED = r"""geo-location-movement-speed"""
TAG_GEO_LOCATION_NAME = r"""geo-location-name"""
TAG_GEO_LOCATION_SUBLOCATION = r"""geo-location-sublocation"""
TAG_GROUPING = r"""grouping"""
TAG_HOMEPAGE = r"""homepage"""
TAG_IMAGE = r"""image"""
TAG_IMAGE_ORIENTATION = r"""image-orientation"""
TAG_INTERPRETED_BY = r"""interpreted-by"""
TAG_ISRC = r"""isrc"""
TAG_KEYWORDS = r"""keywords"""
TAG_LANGUAGE_CODE = r"""language-code"""
TAG_LANGUAGE_NAME = r"""language-name"""
TAG_LICENSE = r"""license"""
TAG_LICENSE_URI = r"""license-uri"""
TAG_LOCATION = r"""location"""
TAG_LYRICS = r"""lyrics"""
TAG_MAXIMUM_BITRATE = r"""maximum-bitrate"""
TAG_MIDI_BASE_NOTE = r"""midi-base-note"""
TAG_MINIMUM_BITRATE = r"""minimum-bitrate"""
TAG_NOMINAL_BITRATE = r"""nominal-bitrate"""
TAG_ORGANIZATION = r"""organization"""
TAG_PERFORMER = r"""performer"""
TAG_PREVIEW_IMAGE = r"""preview-image"""
TAG_PRIVATE_DATA = r"""private-data"""
TAG_PUBLISHER = r"""publisher"""
TAG_REFERENCE_LEVEL = r"""replaygain-reference-level"""
TAG_SERIAL = r"""serial"""
TAG_SHOW_EPISODE_NUMBER = r"""show-episode-number"""
TAG_SHOW_NAME = r"""show-name"""
TAG_SHOW_SEASON_NUMBER = r"""show-season-number"""
TAG_SHOW_SORTNAME = r"""show-sortname"""
TAG_SUBTITLE_CODEC = r"""subtitle-codec"""
TAG_TITLE = r"""title"""
TAG_TITLE_SORTNAME = r"""title-sortname"""
TAG_TRACK_COUNT = r"""track-count"""
TAG_TRACK_GAIN = r"""replaygain-track-gain"""
TAG_TRACK_NUMBER = r"""track-number"""
TAG_TRACK_PEAK = r"""replaygain-track-peak"""
TAG_USER_RATING = r"""user-rating"""
TAG_VERSION = r"""version"""
TAG_VIDEO_CODEC = r"""video-codec"""
TIME_FORMAT = r"""u:%02u:%02u.%09u"""
TOC_REPEAT_COUNT_INFINITE = r"""-1"""


class TagFlag:
    """"""
    UNDEFINED = 0
    META = 1
    ENCODED = 2
    DECODED = 3
    COUNT = 4


class TagMergeMode:
    """"""
    UNDEFINED = 0
    REPLACE_ALL = 1
    REPLACE = 2
    APPEND = 3
    PREPEND = 4
    KEEP = 5
    KEEP_ALL = 6
    COUNT = 7


class TagScope:
    """"""
    STREAM = 0
    GLOBAL = 1


class TaskState:
    """"""
    STARTED = 0
    STOPPED = 1
    PAUSED = 2


class TocEntryType:
    """"""
    ANGLE = -3
    VERSION = -2
    EDITION = -1
    INVALID = 0
    TITLE = 1
    TRACK = 2
    CHAPTER = 3


class TocLoopType:
    """"""
    NONE = 0
    FORWARD = 1
    REVERSE = 2
    PING_PONG = 3


class TocScope:
    """"""
    GLOBAL = 1
    CURRENT = 2


class TracerValueFlags:
    """"""
    NONE = 0
    OPTIONAL = 1
    AGGREGATED = 2


class TracerValueScope:
    """"""
    PROCESS = 0
    THREAD = 1
    ELEMENT = 2
    PAD = 3


class TypeFindProbability:
    """"""
    NONE = 0
    MINIMUM = 1
    POSSIBLE = 50
    LIKELY = 80
    NEARLY_CERTAIN = 99
    MAXIMUM = 100


class URIError:
    """"""
    UNSUPPORTED_PROTOCOL = 0
    BAD_URI = 1
    BAD_STATE = 2
    BAD_REFERENCE = 3


class URIType:
    """"""
    UNKNOWN = 0
    SINK = 1
    SRC = 2


URI_NO_PORT = r"""0"""
USECOND = r"""1000"""
VALUE_EQUAL = r"""0"""
VALUE_GREATER_THAN = r"""1"""
VALUE_LESS_THAN = r"""-1"""
VALUE_UNORDERED = r"""2"""
VERSION_MAJOR = r"""1"""
VERSION_MICRO = r"""5"""
VERSION_MINOR = r"""14"""
VERSION_NANO = r"""0"""


def buffer_get_max_memory():
    """"""
    return object


def calculate_linear_regression(xy=None, temp=None, n=None, m_num=None, m_denom=None, b=None, xbase=None, r_squared=None):
    """"""
    return object


def caps_features_from_string(features=None):
    """"""
    return object


def caps_from_string(string=None):
    """"""
    return object


def core_error_quark():
    """"""
    return object


def debug_add_log_function(func=None, user_data=None, notify=None):
    """"""
    return object


def debug_add_ring_buffer_logger(max_size_per_thread=None, thread_timeout=None):
    """"""
    return object


def debug_bin_to_dot_data(bin=None, details=None):
    """"""
    return object


def debug_bin_to_dot_file(bin=None, details=None, file_name=None):
    """"""
    return object


def debug_bin_to_dot_file_with_ts(bin=None, details=None, file_name=None):
    """"""
    return object


def debug_construct_term_color(colorinfo=None):
    """"""
    return object


def debug_construct_win_color(colorinfo=None):
    """"""
    return object


def debug_get_all_categories():
    """"""
    return object


def debug_get_color_mode():
    """"""
    return object


def debug_get_default_threshold():
    """"""
    return object


def debug_get_stack_trace(flags=None):
    """"""
    return object


def debug_is_active():
    """"""
    return object


def debug_is_colored():
    """"""
    return object


def debug_level_get_name(level=None):
    """"""
    return object


def debug_log(category=None, level=None, file=None, function=None, line=None, object=None, format=None, *args):
    """"""
    return object


def debug_log_default(category=None, level=None, file=None, function=None, line=None, object=None, message=None, user_data=None):
    """"""
    return object


def debug_log_valist(category=None, level=None, file=None, function=None, line=None, object=None, format=None, args=None):
    """"""
    return object


def debug_print_stack_trace():
    """"""
    return object


def debug_remove_log_function(func=None):
    """"""
    return object


def debug_remove_log_function_by_data(data=None):
    """"""
    return object


def debug_remove_ring_buffer_logger():
    """"""
    return object


def debug_ring_buffer_logger_get_logs():
    """"""
    return object


def debug_set_active(active=None):
    """"""
    return object


def debug_set_color_mode(mode=None):
    """"""
    return object


def debug_set_color_mode_from_string(mode=None):
    """"""
    return object


def debug_set_colored(colored=None):
    """"""
    return object


def debug_set_default_threshold(level=None):
    """"""
    return object


def debug_set_threshold_for_name(name=None, level=None):
    """"""
    return object


def debug_set_threshold_from_string(list=None, reset=None):
    """"""
    return object


def debug_unset_threshold_for_name(name=None):
    """"""
    return object


def deinit():
    """"""
    return object


def dynamic_type_register(plugin=None, type=None):
    """"""
    return object


def error_get_message(domain=None, code=None):
    """"""
    return object


def event_type_get_flags(type=None):
    """"""
    return object


def event_type_get_name(type=None):
    """"""
    return object


def event_type_to_quark(type=None):
    """"""
    return object


def filename_to_uri(filename=None):
    """"""
    return object


def flow_get_name(ret=None):
    """"""
    return object


def flow_to_quark(ret=None):
    """"""
    return object


def format_get_by_nick(nick=None):
    """"""
    return object


def format_get_details(format=None):
    """"""
    return object


def format_get_name(format=None):
    """"""
    return object


def format_iterate_definitions():
    """"""
    return object


def format_register(nick=None, description=None):
    """"""
    return object


def format_to_quark(format=None):
    """"""
    return object


def formats_contains(formats=None, format=None):
    """"""
    return object


def get_main_executable_path():
    """"""
    return object


def info_strdup_printf(format=None, *args):
    """"""
    return object


def info_strdup_vprintf(format=None, args=None):
    """"""
    return object


def info_vasprintf(result=None, format=None, args=None):
    """"""
    return object


def init(argc=None, argv=None):
    """"""
    return object


def init_check(argc=None, argv=None):
    """"""
    return object


def init_get_option_group():
    """"""
    return object


def is_caps_features(obj=None):
    """"""
    return object


def is_initialized():
    """"""
    return object


def library_error_quark():
    """"""
    return object


def make_element_message_details(name=None, *args):
    """"""
    return object


def message_type_get_name(type=None):
    """"""
    return object


def message_type_to_quark(type=None):
    """"""
    return object


def meta_api_type_get_tags(api=None):
    """"""
    return object


def meta_api_type_has_tag(api=None, tag=None):
    """"""
    return object


def meta_api_type_register(api=None, tags=None):
    """"""
    return object


def meta_get_info(impl=None):
    """"""
    return object


def meta_register(api=None, impl=None, size=None, init_func=None, free_func=None, transform_func=None):
    """"""
    return object


def mini_object_replace(olddata=None, newdata=None):
    """"""
    return object


def mini_object_steal(olddata=None):
    """"""
    return object


def mini_object_take(olddata=None, newdata=None):
    """"""
    return object


def pad_mode_get_name(mode=None):
    """"""
    return object


def param_spec_array(name=None, nick=None, blurb=None, element_spec=None, flags=None):
    """"""
    return object


def param_spec_fraction(name=None, nick=None, blurb=None, min_num=None, min_denom=None, max_num=None, max_denom=None, default_num=None, default_denom=None, flags=None):
    """"""
    return object


def parent_buffer_meta_api_get_type():
    """"""
    return object


def parent_buffer_meta_get_info():
    """"""
    return object


def parse_bin_from_description(bin_description=None, ghost_unlinked_pads=None):
    """"""
    return object


def parse_bin_from_description_full(bin_description=None, ghost_unlinked_pads=None, context=None, flags=None):
    """"""
    return object


def parse_error_quark():
    """"""
    return object


def parse_launch(pipeline_description=None):
    """"""
    return object


def parse_launch_full(pipeline_description=None, context=None, flags=None):
    """"""
    return object


def parse_launchv(argv=None):
    """"""
    return object


def parse_launchv_full(argv=None, context=None, flags=None):
    """"""
    return object


def plugin_error_quark():
    """"""
    return object


def poll_new(controllable=None):
    """"""
    return object


def poll_new_timer():
    """"""
    return object


def preset_get_app_dir():
    """"""
    return object


def preset_set_app_dir(app_dir=None):
    """"""
    return object


def _print(format=None, *args):
    """"""
    return object


def printerr(format=None, *args):
    """"""
    return object


def printerrln(format=None, *args):
    """"""
    return object


def println(format=None, *args):
    """"""
    return object


def protection_filter_systems_by_available_decryptors(system_identifiers=None):
    """"""
    return object


def protection_meta_api_get_type():
    """"""
    return object


def protection_meta_get_info():
    """"""
    return object


def protection_select_system(system_identifiers=None):
    """"""
    return object


def query_type_get_flags(type=None):
    """"""
    return object


def query_type_get_name(type=None):
    """"""
    return object


def query_type_to_quark(type=None):
    """"""
    return object


def reference_timestamp_meta_api_get_type():
    """"""
    return object


def reference_timestamp_meta_get_info():
    """"""
    return object


def resource_error_quark():
    """"""
    return object


def segtrap_is_enabled():
    """"""
    return object


def segtrap_set_enabled(enabled=None):
    """"""
    return object


def state_change_get_name(transition=None):
    """"""
    return object


def static_caps_get_type():
    """"""
    return object


def static_pad_template_get_type():
    """"""
    return object


def stream_error_quark():
    """"""
    return object


def stream_type_get_name(stype=None):
    """"""
    return object


def structure_from_string(string=None, end=None):
    """"""
    return object


def tag_exists(tag=None):
    """"""
    return object


def tag_get_description(tag=None):
    """"""
    return object


def tag_get_flag(tag=None):
    """"""
    return object


def tag_get_nick(tag=None):
    """"""
    return object


def tag_get_type(tag=None):
    """"""
    return object


def tag_is_fixed(tag=None):
    """"""
    return object


def tag_list_copy_value(dest=None, list=None, tag=None):
    """"""
    return object


def tag_merge_strings_with_comma(dest=None, src=None):
    """"""
    return object


def tag_merge_use_first(dest=None, src=None):
    """"""
    return object


def tag_register(name=None, flag=None, type=None, nick=None, blurb=None, func=None):
    """"""
    return object


def tag_register_static(name=None, flag=None, type=None, nick=None, blurb=None, func=None):
    """"""
    return object


def toc_entry_type_get_nick(type=None):
    """"""
    return object


def type_find_get_type():
    """"""
    return object


def type_find_register(plugin=None, name=None, rank=None, func=None, extensions=None, possible_caps=None, data=None, data_notify=None):
    """"""
    return object


def update_registry():
    """"""
    return object


def uri_construct(protocol=None, location=None):
    """"""
    return object


def uri_error_quark():
    """"""
    return object


def uri_from_string(uri=None):
    """"""
    return object


def uri_get_location(uri=None):
    """"""
    return object


def uri_get_protocol(uri=None):
    """"""
    return object


def uri_has_protocol(uri=None, protocol=None):
    """"""
    return object


def uri_is_valid(uri=None):
    """"""
    return object


def uri_join_strings(base_uri=None, ref_uri=None):
    """"""
    return object


def uri_protocol_is_supported(type=None, protocol=None):
    """"""
    return object


def uri_protocol_is_valid(protocol=None):
    """"""
    return object


def util_array_binary_search(array=None, num_elements=None, element_size=None, search_func=None, mode=None, search_data=None, user_data=None):
    """"""
    return object


def util_double_to_fraction(src=None, dest_n=None, dest_d=None):
    """"""
    return object


def util_dump_buffer(buf=None):
    """"""
    return object


def util_dump_mem(mem=None, size=None):
    """"""
    return object


def util_fraction_add(a_n=None, a_d=None, b_n=None, b_d=None, res_n=None, res_d=None):
    """"""
    return object


def util_fraction_compare(a_n=None, a_d=None, b_n=None, b_d=None):
    """"""
    return object


def util_fraction_multiply(a_n=None, a_d=None, b_n=None, b_d=None, res_n=None, res_d=None):
    """"""
    return object


def util_fraction_to_double(src_n=None, src_d=None, dest=None):
    """"""
    return object


def util_gdouble_to_guint64(value=None):
    """"""
    return object


def util_get_object_array(object=None, name=None, array=None):
    """"""
    return object


def util_get_timestamp():
    """"""
    return object


def util_greatest_common_divisor(a=None, b=None):
    """"""
    return object


def util_greatest_common_divisor_int64(a=None, b=None):
    """"""
    return object


def util_group_id_next():
    """"""
    return object


def util_guint64_to_gdouble(value=None):
    """"""
    return object


def util_seqnum_compare(s1=None, s2=None):
    """"""
    return object


def util_seqnum_next():
    """"""
    return object


def util_set_object_arg(object=None, name=None, value=None):
    """"""
    return object


def util_set_object_array(object=None, name=None, array=None):
    """"""
    return object


def util_set_value_from_string(value=None, value_str=None):
    """"""
    return object


def util_uint64_scale(val=None, num=None, denom=None):
    """"""
    return object


def util_uint64_scale_ceil(val=None, num=None, denom=None):
    """"""
    return object


def util_uint64_scale_int(val=None, num=None, denom=None):
    """"""
    return object


def util_uint64_scale_int_ceil(val=None, num=None, denom=None):
    """"""
    return object


def util_uint64_scale_int_round(val=None, num=None, denom=None):
    """"""
    return object


def util_uint64_scale_round(val=None, num=None, denom=None):
    """"""
    return object


def value_can_compare(value1=None, value2=None):
    """"""
    return object


def value_can_intersect(value1=None, value2=None):
    """"""
    return object


def value_can_subtract(minuend=None, subtrahend=None):
    """"""
    return object


def value_can_union(value1=None, value2=None):
    """"""
    return object


def value_compare(value1=None, value2=None):
    """"""
    return object


def value_deserialize(dest=None, src=None):
    """"""
    return object


def value_fixate(dest=None, src=None):
    """"""
    return object


def value_fraction_multiply(product=None, factor1=None, factor2=None):
    """"""
    return object


def value_fraction_subtract(dest=None, minuend=None, subtrahend=None):
    """"""
    return object


def value_get_bitmask(value=None):
    """"""
    return object


def value_get_caps(value=None):
    """"""
    return object


def value_get_caps_features(value=None):
    """"""
    return object


def value_get_double_range_max(value=None):
    """"""
    return object


def value_get_double_range_min(value=None):
    """"""
    return object


def value_get_flagset_flags(value=None):
    """"""
    return object


def value_get_flagset_mask(value=None):
    """"""
    return object


def value_get_fraction_denominator(value=None):
    """"""
    return object


def value_get_fraction_numerator(value=None):
    """"""
    return object


def value_get_fraction_range_max(value=None):
    """"""
    return object


def value_get_fraction_range_min(value=None):
    """"""
    return object


def value_get_int64_range_max(value=None):
    """"""
    return object


def value_get_int64_range_min(value=None):
    """"""
    return object


def value_get_int64_range_step(value=None):
    """"""
    return object


def value_get_int_range_max(value=None):
    """"""
    return object


def value_get_int_range_min(value=None):
    """"""
    return object


def value_get_int_range_step(value=None):
    """"""
    return object


def value_get_structure(value=None):
    """"""
    return object


def value_init_and_copy(dest=None, src=None):
    """"""
    return object


def value_intersect(dest=None, value1=None, value2=None):
    """"""
    return object


def value_is_fixed(value=None):
    """"""
    return object


def value_is_subset(value1=None, value2=None):
    """"""
    return object


def value_register(table=None):
    """"""
    return object


def value_serialize(value=None):
    """"""
    return object


def value_set_bitmask(value=None, bitmask=None):
    """"""
    return object


def value_set_caps(value=None, caps=None):
    """"""
    return object


def value_set_caps_features(value=None, features=None):
    """"""
    return object


def value_set_double_range(value=None, start=None, end=None):
    """"""
    return object


def value_set_flagset(value=None, flags=None, mask=None):
    """"""
    return object


def value_set_fraction(value=None, numerator=None, denominator=None):
    """"""
    return object


def value_set_fraction_range(value=None, start=None, end=None):
    """"""
    return object


def value_set_fraction_range_full(value=None, numerator_start=None, denominator_start=None, numerator_end=None, denominator_end=None):
    """"""
    return object


def value_set_int64_range(value=None, start=None, end=None):
    """"""
    return object


def value_set_int64_range_step(value=None, start=None, end=None, step=None):
    """"""
    return object


def value_set_int_range(value=None, start=None, end=None):
    """"""
    return object


def value_set_int_range_step(value=None, start=None, end=None, step=None):
    """"""
    return object


def value_set_structure(value=None, structure=None):
    """"""
    return object


def value_subtract(dest=None, minuend=None, subtrahend=None):
    """"""
    return object


def value_union(dest=None, value1=None, value2=None):
    """"""
    return object


def version(major=None, minor=None, micro=None, nano=None):
    """"""
    return object


def version_string():
    """"""
    return object


class AllocationParams():
    """"""

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
    def flags(self):
        return object

    @property
    def align(self):
        return object

    @property
    def prefix(self):
        return object

    @property
    def padding(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AllocatorClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def alloc(self):
        return object

    @property
    def free(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AllocatorPrivate():
    """"""


class AtomicQueue():
    """"""

    def __init__(self, initial_size=None):
        """"""
        return object

    @staticmethod
    def new(initial_size=None):
        """"""
        return object

    def length(self):
        """"""
        return object

    def peek(self):
        """"""
        return object

    def pop(self):
        """"""
        return object

    def push(self, data=None):
        """"""
        return object

    def ref(self):
        """"""
        return object

    def unref(self):
        """"""
        return object


class BinClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def pool(self):
        return object

    @property
    def element_added(self):
        return object

    @property
    def element_removed(self):
        return object

    @property
    def add_element(self):
        return object

    @property
    def remove_element(self):
        return object

    @property
    def handle_message(self):
        return object

    @property
    def do_latency(self):
        return object

    @property
    def deep_element_added(self):
        return object

    @property
    def deep_element_removed(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BinPrivate():
    """"""


class Bitmask():
    """"""


class Buffer():
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    @staticmethod
    def new_allocate(allocator=None, size=None, params=None):
        """"""
        return object

    @staticmethod
    def new_wrapped(data=None, size=None):
        """"""
        return object

    @staticmethod
    def new_wrapped_full(flags=None, data=None, maxsize=None, offset=None, size=None, user_data=None, notify=None):
        """"""
        return object

    def add_meta(self, info=None, params=None):
        """"""
        return object

    def add_parent_buffer_meta(self, ref=None):
        """"""
        return object

    def add_protection_meta(self, info=None):
        """"""
        return object

    def add_reference_timestamp_meta(self, reference=None, timestamp=None, duration=None):
        """"""
        return object

    def append(self, buf2=None):
        """"""
        return object

    def append_memory(self, mem=None):
        """"""
        return object

    def append_region(self, buf2=None, offset=None, size=None):
        """"""
        return object

    def copy_deep(self):
        """"""
        return object

    def copy_into(self, src=None, flags=None, offset=None, size=None):
        """"""
        return object

    def copy_region(self, flags=None, offset=None, size=None):
        """"""
        return object

    def extract(self, offset=None, dest=None, size=None):
        """"""
        return object

    def extract_dup(self, offset=None, size=None, dest=None, dest_size=None):
        """"""
        return object

    def fill(self, offset=None, src=None, size=None):
        """"""
        return object

    def find_memory(self, offset=None, size=None, idx=None, length=None, skip=None):
        """"""
        return object

    def foreach_meta(self, func=None, user_data=None):
        """"""
        return object

    def get_all_memory(self):
        """"""
        return object

    def get_flags(self):
        """"""
        return object

    def get_memory(self, idx=None):
        """"""
        return object

    def get_memory_range(self, idx=None, length=None):
        """"""
        return object

    def get_meta(self, api=None):
        """"""
        return object

    def get_n_meta(self, api_type=None):
        """"""
        return object

    def get_reference_timestamp_meta(self, reference=None):
        """"""
        return object

    def get_size(self):
        """"""
        return object

    def get_sizes(self, offset=None, maxsize=None):
        """"""
        return object

    def get_sizes_range(self, idx=None, length=None, offset=None, maxsize=None):
        """"""
        return object

    def has_flags(self, flags=None):
        """"""
        return object

    def insert_memory(self, idx=None, mem=None):
        """"""
        return object

    def is_all_memory_writable(self):
        """"""
        return object

    def is_memory_range_writable(self, idx=None, length=None):
        """"""
        return object

    def iterate_meta(self, state=None):
        """"""
        return object

    def iterate_meta_filtered(self, state=None, meta_api_type=None):
        """"""
        return object

    def map(self, info=None, flags=None):
        """"""
        return object

    def map_range(self, idx=None, length=None, info=None, flags=None):
        """"""
        return object

    def memcmp(self, offset=None, mem=None, size=None):
        """"""
        return object

    def memset(self, offset=None, val=None, size=None):
        """"""
        return object

    def n_memory(self):
        """"""
        return object

    def peek_memory(self, idx=None):
        """"""
        return object

    def prepend_memory(self, mem=None):
        """"""
        return object

    def remove_all_memory(self):
        """"""
        return object

    def remove_memory(self, idx=None):
        """"""
        return object

    def remove_memory_range(self, idx=None, length=None):
        """"""
        return object

    def remove_meta(self, meta=None):
        """"""
        return object

    def replace_all_memory(self, mem=None):
        """"""
        return object

    def replace_memory(self, idx=None, mem=None):
        """"""
        return object

    def replace_memory_range(self, idx=None, length=None, mem=None):
        """"""
        return object

    def resize(self, offset=None, size=None):
        """"""
        return object

    def resize_range(self, idx=None, length=None, offset=None, size=None):
        """"""
        return object

    def set_flags(self, flags=None):
        """"""
        return object

    def set_size(self, size=None):
        """"""
        return object

    def unmap(self, info=None):
        """"""
        return object

    def unset_flags(self, flags=None):
        """"""
        return object

    @staticmethod
    def get_max_memory():
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def pool(self):
        return object

    @property
    def pts(self):
        return object

    @property
    def dts(self):
        return object

    @property
    def duration(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def offset_end(self):
        return object


class BufferList():
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    @staticmethod
    def new_sized(size=None):
        """"""
        return object

    def calculate_size(self):
        """"""
        return object

    def copy_deep(self):
        """"""
        return object

    def foreach(self, func=None, user_data=None):
        """"""
        return object

    def get(self, idx=None):
        """"""
        return object

    def get_writable(self, idx=None):
        """"""
        return object

    def insert(self, idx=None, buffer=None):
        """"""
        return object

    def length(self):
        """"""
        return object

    def remove(self, idx=None, length=None):
        """"""
        return object


class BufferPoolAcquireParams():
    """"""

    @property
    def format(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BufferPoolClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def get_options(self):
        return object

    @property
    def set_config(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def acquire_buffer(self):
        return object

    @property
    def alloc_buffer(self):
        return object

    @property
    def reset_buffer(self):
        return object

    @property
    def release_buffer(self):
        return object

    @property
    def free_buffer(self):
        return object

    @property
    def flush_start(self):
        return object

    @property
    def flush_stop(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BufferPoolPrivate():
    """"""


class BusClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def message(self):
        return object

    @property
    def sync_message(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class BusPrivate():
    """"""


class Caps():
    """"""
    @staticmethod
    def new_any():
        """"""
        return object

    @staticmethod
    def new_empty():
        """"""
        return object

    @staticmethod
    def new_empty_simple(media_type=None):
        """"""
        return object

    @staticmethod
    def new_full(struct1=None, *args):
        """"""
        return object

    @staticmethod
    def new_full_valist(structure=None, var_args=None):
        """"""
        return object

    @staticmethod
    def new_simple(media_type=None, fieldname=None, *args):
        """"""
        return object

    def append(self, caps2=None):
        """"""
        return object

    def append_structure(self, structure=None):
        """"""
        return object

    def append_structure_full(self, structure=None, features=None):
        """"""
        return object

    def can_intersect(self, caps2=None):
        """"""
        return object

    def copy_nth(self, nth=None):
        """"""
        return object

    def filter_and_map_in_place(self, func=None, user_data=None):
        """"""
        return object

    def fixate(self):
        """"""
        return object

    def foreach(self, func=None, user_data=None):
        """"""
        return object

    def get_features(self, index=None):
        """"""
        return object

    def get_size(self):
        """"""
        return object

    def get_structure(self, index=None):
        """"""
        return object

    def intersect(self, caps2=None):
        """"""
        return object

    def intersect_full(self, caps2=None, mode=None):
        """"""
        return object

    def is_always_compatible(self, caps2=None):
        """"""
        return object

    def is_any(self):
        """"""
        return object

    def is_empty(self):
        """"""
        return object

    def is_equal(self, caps2=None):
        """"""
        return object

    def is_equal_fixed(self, caps2=None):
        """"""
        return object

    def is_fixed(self):
        """"""
        return object

    def is_strictly_equal(self, caps2=None):
        """"""
        return object

    def is_subset(self, superset=None):
        """"""
        return object

    def is_subset_structure(self, structure=None):
        """"""
        return object

    def is_subset_structure_full(self, structure=None, features=None):
        """"""
        return object

    def map_in_place(self, func=None, user_data=None):
        """"""
        return object

    def merge(self, caps2=None):
        """"""
        return object

    def merge_structure(self, structure=None):
        """"""
        return object

    def merge_structure_full(self, structure=None, features=None):
        """"""
        return object

    def normalize(self):
        """"""
        return object

    def remove_structure(self, idx=None):
        """"""
        return object

    def set_features(self, index=None, features=None):
        """"""
        return object

    def set_simple(self, field=None, *args):
        """"""
        return object

    def set_simple_valist(self, field=None, varargs=None):
        """"""
        return object

    def set_value(self, field=None, value=None):
        """"""
        return object

    def simplify(self):
        """"""
        return object

    def steal_structure(self, index=None):
        """"""
        return object

    def subtract(self, subtrahend=None):
        """"""
        return object

    def to_string(self):
        """"""
        return object

    def truncate(self):
        """"""
        return object

    @staticmethod
    def from_string(string=None) -> 'Caps':
        """"""
        return object

    @property
    def mini_object(self):
        return object


class CapsFeatures():
    """"""

    def __init__(self, feature1=None, *args):
        """"""
        return object

    @staticmethod
    def new(feature1=None, *args):
        """"""
        return object

    @staticmethod
    def new_any():
        """"""
        return object

    @staticmethod
    def new_empty():
        """"""
        return object

    @staticmethod
    def new_id(feature1=None, *args):
        """"""
        return object

    @staticmethod
    def new_id_valist(feature1=None, varargs=None):
        """"""
        return object

    @staticmethod
    def new_valist(feature1=None, varargs=None):
        """"""
        return object

    def add(self, feature=None):
        """"""
        return object

    def add_id(self, feature=None):
        """"""
        return object

    def contains(self, feature=None):
        """"""
        return object

    def contains_id(self, feature=None):
        """"""
        return object

    def copy(self):
        """"""
        return object

    def free(self):
        """"""
        return object

    def get_nth(self, i=None):
        """"""
        return object

    def get_nth_id(self, i=None):
        """"""
        return object

    def get_size(self):
        """"""
        return object

    def is_any(self):
        """"""
        return object

    def is_equal(self, features2=None):
        """"""
        return object

    def remove(self, feature=None):
        """"""
        return object

    def remove_id(self, feature=None):
        """"""
        return object

    def set_parent_refcount(self, refcount=None):
        """"""
        return object

    def to_string(self):
        """"""
        return object

    @staticmethod
    def from_string(features=None):
        """"""
        return object


class ChildProxy():
    """"""

    def child_added(self, child=None, name=None):
        """"""
        return object

    def child_removed(self, child=None, name=None):
        """"""
        return object

    def get_child_by_index(self, index=None):
        """"""
        return object

    def get_child_by_name(self, name=None):
        """"""
        return object

    def get_children_count(self):
        """"""
        return object

    def child_added(self, child=None, name=None):
        """"""
        return object

    def child_removed(self, child=None, name=None):
        """"""
        return object

    def get(self, first_property_name=None, *args):
        """"""
        return object

    def get_child_by_index(self, index=None):
        """"""
        return object

    def get_child_by_name(self, name=None):
        """"""
        return object

    def get_children_count(self):
        """"""
        return object

    def get_property(self, name=None, value=None):
        """"""
        return object

    def get_valist(self, first_property_name=None, var_args=None):
        """"""
        return object

    def lookup(self, name=None, target=None, pspec=None):
        """"""
        return object

    def set(self, first_property_name=None, *args):
        """"""
        return object

    def set_property(self, name=None, value=None):
        """"""
        return object

    def set_valist(self, first_property_name=None, var_args=None):
        """"""
        return object


class ChildProxyInterface():
    """"""

    @property
    def parent(self):
        return object

    @property
    def get_child_by_name(self):
        return object

    @property
    def get_child_by_index(self):
        return object

    @property
    def get_children_count(self):
        return object

    @property
    def child_added(self):
        return object

    @property
    def child_removed(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ClockClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def change_resolution(self):
        return object

    @property
    def get_resolution(self):
        return object

    @property
    def get_internal_time(self):
        return object

    @property
    def wait(self):
        return object

    @property
    def wait_async(self):
        return object

    @property
    def unschedule(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ClockEntry():
    """"""

    @property
    def refcount(self):
        return object

    @property
    def clock(self):
        return object

    @property
    def type(self):
        return object

    @property
    def time(self):
        return object

    @property
    def interval(self):
        return object

    @property
    def status(self):
        return object

    @property
    def func(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def destroy_data(self):
        return object

    @property
    def unscheduled(self):
        return object

    @property
    def woken_up(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ClockPrivate():
    """"""


class Context():
    """"""

    def __init__(self, context_type=None, persistent=None):
        """"""
        return object

    @staticmethod
    def new(context_type=None, persistent=None):
        """"""
        return object

    def get_context_type(self):
        """"""
        return object

    def get_structure(self):
        """"""
        return object

    def has_context_type(self, context_type=None):
        """"""
        return object

    def is_persistent(self):
        """"""
        return object

    def writable_structure(self):
        """"""
        return object


class ControlBindingClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def sync_values(self):
        return object

    @property
    def get_value(self):
        return object

    @property
    def get_value_array(self):
        return object

    @property
    def get_g_value_array(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ControlBindingPrivate():
    """"""


class ControlSourceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DateTime():
    """"""

    def __init__(self, tzoffset=None, year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object

    @staticmethod
    def new(tzoffset=None, year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object

    @staticmethod
    def new_from_g_date_time(dt=None):
        """"""
        return object

    @staticmethod
    def new_from_iso8601_string(string=None):
        """"""
        return object

    @staticmethod
    def new_from_unix_epoch_local_time(secs=None):
        """"""
        return object

    @staticmethod
    def new_from_unix_epoch_utc(secs=None):
        """"""
        return object

    @staticmethod
    def new_local_time(year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object

    @staticmethod
    def new_now_local_time():
        """"""
        return object

    @staticmethod
    def new_now_utc():
        """"""
        return object

    @staticmethod
    def new_y(year=None):
        """"""
        return object

    @staticmethod
    def new_ym(year=None, month=None):
        """"""
        return object

    @staticmethod
    def new_ymd(year=None, month=None, day=None):
        """"""
        return object

    def get_day(self):
        """"""
        return object

    def get_hour(self):
        """"""
        return object

    def get_microsecond(self):
        """"""
        return object

    def get_minute(self):
        """"""
        return object

    def get_month(self):
        """"""
        return object

    def get_second(self):
        """"""
        return object

    def get_time_zone_offset(self):
        """"""
        return object

    def get_year(self):
        """"""
        return object

    def has_day(self):
        """"""
        return object

    def has_month(self):
        """"""
        return object

    def has_second(self):
        """"""
        return object

    def has_time(self):
        """"""
        return object

    def has_year(self):
        """"""
        return object

    def ref(self):
        """"""
        return object

    def to_g_date_time(self):
        """"""
        return object

    def to_iso8601_string(self):
        """"""
        return object

    def unref(self):
        """"""
        return object


class DebugCategory():
    """"""

    def free(self):
        """"""
        return object

    def get_color(self):
        """"""
        return object

    def get_description(self):
        """"""
        return object

    def get_name(self):
        """"""
        return object

    def get_threshold(self):
        """"""
        return object

    def reset_threshold(self):
        """"""
        return object

    def set_threshold(self, level=None):
        """"""
        return object

    @property
    def threshold(self):
        return object

    @property
    def color(self):
        return object

    @property
    def name(self):
        return object

    @property
    def description(self):
        return object


class DebugMessage():
    """"""

    def get(self):
        """"""
        return object


class DeviceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def create_element(self):
        return object

    @property
    def reconfigure_element(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DeviceMonitorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DeviceMonitorPrivate():
    """"""


class DevicePrivate():
    """"""


class DeviceProviderClass():
    """"""

    def add_metadata(self, key=None, value=None):
        """"""
        return object

    def add_static_metadata(self, key=None, value=None):
        """"""
        return object

    def get_metadata(self, key=None):
        """"""
        return object

    def set_metadata(self, longname=None, classification=None, description=None, author=None):
        """"""
        return object

    def set_static_metadata(self, longname=None, classification=None, description=None, author=None):
        """"""
        return object

    @property
    def parent_class(self):
        return object

    @property
    def factory(self):
        return object

    @property
    def probe(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def metadata(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DeviceProviderFactoryClass():
    """"""


class DeviceProviderPrivate():
    """"""


class DoubleRange():
    """"""


class DynamicTypeFactoryClass():
    """"""


class ElementClass():
    """"""

    def add_metadata(self, key=None, value=None):
        """"""
        return object

    def add_pad_template(self, templ=None):
        """"""
        return object

    def add_static_metadata(self, key=None, value=None):
        """"""
        return object

    def add_static_pad_template(self, static_templ=None):
        """"""
        return object

    def add_static_pad_template_with_gtype(self, static_templ=None, pad_type=None):
        """"""
        return object

    def get_metadata(self, key=None):
        """"""
        return object

    def get_pad_template(self, name=None):
        """"""
        return object

    def get_pad_template_list(self):
        """"""
        return object

    def set_metadata(self, longname=None, classification=None, description=None, author=None):
        """"""
        return object

    def set_static_metadata(self, longname=None, classification=None, description=None, author=None):
        """"""
        return object

    @property
    def parent_class(self):
        return object

    @property
    def metadata(self):
        return object

    @property
    def elementfactory(self):
        return object

    @property
    def padtemplates(self):
        return object

    @property
    def numpadtemplates(self):
        return object

    @property
    def pad_templ_cookie(self):
        return object

    @property
    def pad_added(self):
        return object

    @property
    def pad_removed(self):
        return object

    @property
    def no_more_pads(self):
        return object

    @property
    def request_new_pad(self):
        return object

    @property
    def release_pad(self):
        return object

    @property
    def get_state(self):
        return object

    @property
    def set_state(self):
        return object

    @property
    def change_state(self):
        return object

    @property
    def state_changed(self):
        return object

    @property
    def set_bus(self):
        return object

    @property
    def provide_clock(self):
        return object

    @property
    def set_clock(self):
        return object

    @property
    def send_event(self):
        return object

    @property
    def query(self):
        return object

    @property
    def post_message(self):
        return object

    @property
    def set_context(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ElementFactoryClass():
    """"""


class Event():
    """"""
    @staticmethod
    def new_buffer_size(format=None, minsize=None, maxsize=None, async=None):
        """"""
        return object

    @staticmethod
    def new_caps(caps=None):
        """"""
        return object

    @staticmethod
    def new_custom(type=None, structure=None):
        """"""
        return object

    @staticmethod
    def new_eos():
        """"""
        return object

    @staticmethod
    def new_flush_start():
        """"""
        return object

    @staticmethod
    def new_flush_stop(reset_time=None):
        """"""
        return object

    @staticmethod
    def new_gap(timestamp=None, duration=None):
        """"""
        return object

    @staticmethod
    def new_latency(latency=None):
        """"""
        return object

    @staticmethod
    def new_navigation(structure=None):
        """"""
        return object

    @staticmethod
    def new_protection(system_id=None, data=None, origin=None):
        """"""
        return object

    @staticmethod
    def new_qos(type=None, proportion=None, diff=None, timestamp=None):
        """"""
        return object

    @staticmethod
    def new_reconfigure():
        """"""
        return object

    @staticmethod
    def new_seek(rate=None, format=None, flags=None, start_type=None, start=None, stop_type=None, stop=None):
        """"""
        return object

    @staticmethod
    def new_segment(segment=None):
        """"""
        return object

    @staticmethod
    def new_segment_done(format=None, position=None):
        """"""
        return object

    @staticmethod
    def new_select_streams(streams=None):
        """"""
        return object

    @staticmethod
    def new_sink_message(name=None, msg=None):
        """"""
        return object

    @staticmethod
    def new_step(format=None, amount=None, rate=None, flush=None, intermediate=None):
        """"""
        return object

    @staticmethod
    def new_stream_collection(collection=None):
        """"""
        return object

    @staticmethod
    def new_stream_group_done(group_id=None):
        """"""
        return object

    @staticmethod
    def new_stream_start(stream_id=None):
        """"""
        return object

    @staticmethod
    def new_tag(taglist=None):
        """"""
        return object

    @staticmethod
    def new_toc(toc=None, updated=None):
        """"""
        return object

    @staticmethod
    def new_toc_select(uid=None):
        """"""
        return object

    def copy_segment(self, segment=None):
        """"""
        return object

    def get_running_time_offset(self):
        """"""
        return object

    def get_seqnum(self):
        """"""
        return object

    def get_structure(self):
        """"""
        return object

    def has_name(self, name=None):
        """"""
        return object

    def parse_buffer_size(self, format=None, minsize=None, maxsize=None, async=None):
        """"""
        return object

    def parse_caps(self, caps=None):
        """"""
        return object

    def parse_flush_stop(self, reset_time=None):
        """"""
        return object

    def parse_gap(self, timestamp=None, duration=None):
        """"""
        return object

    def parse_group_id(self, group_id=None):
        """"""
        return object

    def parse_latency(self, latency=None):
        """"""
        return object

    def parse_protection(self, system_id=None, data=None, origin=None):
        """"""
        return object

    def parse_qos(self, type=None, proportion=None, diff=None, timestamp=None):
        """"""
        return object

    def parse_seek(self, rate=None, format=None, flags=None, start_type=None, start=None, stop_type=None, stop=None):
        """"""
        return object

    def parse_segment(self, segment=None):
        """"""
        return object

    def parse_segment_done(self, format=None, position=None):
        """"""
        return object

    def parse_select_streams(self, streams=None):
        """"""
        return object

    def parse_sink_message(self, msg=None):
        """"""
        return object

    def parse_step(self, format=None, amount=None, rate=None, flush=None, intermediate=None):
        """"""
        return object

    def parse_stream(self, stream=None):
        """"""
        return object

    def parse_stream_collection(self, collection=None):
        """"""
        return object

    def parse_stream_flags(self, flags=None):
        """"""
        return object

    def parse_stream_group_done(self, group_id=None):
        """"""
        return object

    def parse_stream_start(self, stream_id=None):
        """"""
        return object

    def parse_tag(self, taglist=None):
        """"""
        return object

    def parse_toc(self, toc=None, updated=None):
        """"""
        return object

    def parse_toc_select(self, uid=None):
        """"""
        return object

    def set_group_id(self, group_id=None):
        """"""
        return object

    def set_running_time_offset(self, offset=None):
        """"""
        return object

    def set_seqnum(self, seqnum=None):
        """"""
        return object

    def set_stream(self, stream=None):
        """"""
        return object

    def set_stream_flags(self, flags=None):
        """"""
        return object

    def writable_structure(self):
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def type(self):
        return object

    @property
    def timestamp(self):
        return object

    @property
    def seqnum(self):
        return object


class FlagSet():
    """"""
    @staticmethod
    def register(flags_type=None):
        """"""
        return object


class FormatDefinition():
    """"""

    @property
    def value(self):
        return object

    @property
    def nick(self):
        return object

    @property
    def description(self):
        return object

    @property
    def quark(self):
        return object


class Fraction():
    """"""


class FractionRange():
    """"""


class GhostPadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class GhostPadPrivate():
    """"""


class Int64Range():
    """"""


class IntRange():
    """"""


class Iterator():
    """"""

    def __init__(self, size=None, type=None, lock=None, master_cookie=None, copy=None, next=None, item=None, resync=None, free=None):
        """"""
        return object

    @staticmethod
    def new(size=None, type=None, lock=None, master_cookie=None, copy=None, next=None, item=None, resync=None, free=None):
        """"""
        return object

    @staticmethod
    def new_list(type=None, lock=None, master_cookie=None, list=None, owner=None, item=None):
        """"""
        return object

    @staticmethod
    def new_single(type=None, object=None):
        """"""
        return object

    def copy(self):
        """"""
        return object

    def filter(self, func=None, user_data=None):
        """"""
        return object

    def find_custom(self, func=None, elem=None, user_data=None):
        """"""
        return object

    def fold(self, func=None, ret=None, user_data=None):
        """"""
        return object

    def foreach(self, func=None, user_data=None):
        """"""
        return object

    def free(self):
        """"""
        return object

    def next(self, elem=None):
        """"""
        return object

    def push(self, other=None):
        """"""
        return object

    def resync(self):
        """"""
        return object

    @property
    def copy(self):
        return object

    @property
    def next(self):
        return object

    @property
    def item(self):
        return object

    @property
    def resync(self):
        return object

    @property
    def free(self):
        return object

    @property
    def pushed(self):
        return object

    @property
    def type(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def cookie(self):
        return object

    @property
    def master_cookie(self):
        return object

    @property
    def size(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class MapInfo():
    """"""

    @property
    def memory(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def data(self):
        return object

    @property
    def size(self):
        return object

    @property
    def maxsize(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Memory():
    """"""
    @staticmethod
    def new_wrapped(flags=None, data=None, maxsize=None, offset=None, size=None, user_data=None, notify=None):
        """"""
        return object

    def copy(self, offset=None, size=None):
        """"""
        return object

    def get_sizes(self, offset=None, maxsize=None):
        """"""
        return object

    def init(self, flags=None, allocator=None, parent=None, maxsize=None, align=None, offset=None, size=None):
        """"""
        return object

    def is_span(self, mem2=None, offset=None):
        """"""
        return object

    def is_type(self, mem_type=None):
        """"""
        return object

    def make_mapped(self, info=None, flags=None):
        """"""
        return object

    def map(self, info=None, flags=None):
        """"""
        return object

    def resize(self, offset=None, size=None):
        """"""
        return object

    def share(self, offset=None, size=None):
        """"""
        return object

    def unmap(self, info=None):
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def allocator(self):
        return object

    @property
    def parent(self):
        return object

    @property
    def maxsize(self):
        return object

    @property
    def align(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def size(self):
        return object


class Message():
    """"""
    @staticmethod
    def new_application(src=None, structure=None):
        """"""
        return object

    @staticmethod
    def new_async_done(src=None, running_time=None):
        """"""
        return object

    @staticmethod
    def new_async_start(src=None):
        """"""
        return object

    @staticmethod
    def new_buffering(src=None, percent=None):
        """"""
        return object

    @staticmethod
    def new_clock_lost(src=None, clock=None):
        """"""
        return object

    @staticmethod
    def new_clock_provide(src=None, clock=None, ready=None):
        """"""
        return object

    @staticmethod
    def new_custom(type=None, src=None, structure=None):
        """"""
        return object

    @staticmethod
    def new_device_added(src=None, device=None):
        """"""
        return object

    @staticmethod
    def new_device_removed(src=None, device=None):
        """"""
        return object

    @staticmethod
    def new_duration_changed(src=None):
        """"""
        return object

    @staticmethod
    def new_element(src=None, structure=None):
        """"""
        return object

    @staticmethod
    def new_eos(src=None):
        """"""
        return object

    @staticmethod
    def new_error(src=None, error=None, debug=None):
        """"""
        return object

    @staticmethod
    def new_error_with_details(src=None, error=None, debug=None, details=None):
        """"""
        return object

    @staticmethod
    def new_have_context(src=None, context=None):
        """"""
        return object

    @staticmethod
    def new_info(src=None, error=None, debug=None):
        """"""
        return object

    @staticmethod
    def new_info_with_details(src=None, error=None, debug=None, details=None):
        """"""
        return object

    @staticmethod
    def new_latency(src=None):
        """"""
        return object

    @staticmethod
    def new_need_context(src=None, context_type=None):
        """"""
        return object

    @staticmethod
    def new_new_clock(src=None, clock=None):
        """"""
        return object

    @staticmethod
    def new_progress(src=None, type=None, code=None, text=None):
        """"""
        return object

    @staticmethod
    def new_property_notify(src=None, property_name=None, val=None):
        """"""
        return object

    @staticmethod
    def new_qos(src=None, live=None, running_time=None, stream_time=None, timestamp=None, duration=None):
        """"""
        return object

    @staticmethod
    def new_redirect(src=None, location=None, tag_list=None, entry_struct=None):
        """"""
        return object

    @staticmethod
    def new_request_state(src=None, state=None):
        """"""
        return object

    @staticmethod
    def new_reset_time(src=None, running_time=None):
        """"""
        return object

    @staticmethod
    def new_segment_done(src=None, format=None, position=None):
        """"""
        return object

    @staticmethod
    def new_segment_start(src=None, format=None, position=None):
        """"""
        return object

    @staticmethod
    def new_state_changed(src=None, oldstate=None, newstate=None, pending=None):
        """"""
        return object

    @staticmethod
    def new_state_dirty(src=None):
        """"""
        return object

    @staticmethod
    def new_step_done(src=None, format=None, amount=None, rate=None, flush=None, intermediate=None, duration=None, eos=None):
        """"""
        return object

    @staticmethod
    def new_step_start(src=None, active=None, format=None, amount=None, rate=None, flush=None, intermediate=None):
        """"""
        return object

    @staticmethod
    def new_stream_collection(src=None, collection=None):
        """"""
        return object

    @staticmethod
    def new_stream_start(src=None):
        """"""
        return object

    @staticmethod
    def new_stream_status(src=None, type=None, owner=None):
        """"""
        return object

    @staticmethod
    def new_streams_selected(src=None, collection=None):
        """"""
        return object

    @staticmethod
    def new_structure_change(src=None, type=None, owner=None, busy=None):
        """"""
        return object

    @staticmethod
    def new_tag(src=None, tag_list=None):
        """"""
        return object

    @staticmethod
    def new_toc(src=None, toc=None, updated=None):
        """"""
        return object

    @staticmethod
    def new_warning(src=None, error=None, debug=None):
        """"""
        return object

    @staticmethod
    def new_warning_with_details(src=None, error=None, debug=None, details=None):
        """"""
        return object

    def add_redirect_entry(self, location=None, tag_list=None, entry_struct=None):
        """"""
        return object

    def get_num_redirect_entries(self):
        """"""
        return object

    def get_seqnum(self):
        """"""
        return object

    def get_stream_status_object(self):
        """"""
        return object

    def get_structure(self):
        """"""
        return object

    def has_name(self, name=None):
        """"""
        return object

    def parse_async_done(self, running_time=None):
        """"""
        return object

    def parse_buffering(self, percent=None):
        """"""
        return object

    def parse_buffering_stats(self, mode=None, avg_in=None, avg_out=None, buffering_left=None):
        """"""
        return object

    def parse_clock_lost(self, clock=None):
        """"""
        return object

    def parse_clock_provide(self, clock=None, ready=None):
        """"""
        return object

    def parse_context_type(self, context_type=None):
        """"""
        return object

    def parse_device_added(self, device=None):
        """"""
        return object

    def parse_device_removed(self, device=None):
        """"""
        return object

    def parse_error(self, gerror=None, debug=None):
        """"""
        return object

    def parse_error_details(self, structure=None):
        """"""
        return object

    def parse_group_id(self, group_id=None):
        """"""
        return object

    def parse_have_context(self, context=None):
        """"""
        return object

    def parse_info(self, gerror=None, debug=None):
        """"""
        return object

    def parse_info_details(self, structure=None):
        """"""
        return object

    def parse_new_clock(self, clock=None):
        """"""
        return object

    def parse_progress(self, type=None, code=None, text=None):
        """"""
        return object

    def parse_property_notify(self, object=None, property_name=None, property_value=None):
        """"""
        return object

    def parse_qos(self, live=None, running_time=None, stream_time=None, timestamp=None, duration=None):
        """"""
        return object

    def parse_qos_stats(self, format=None, processed=None, dropped=None):
        """"""
        return object

    def parse_qos_values(self, jitter=None, proportion=None, quality=None):
        """"""
        return object

    def parse_redirect_entry(self, entry_index=None, location=None, tag_list=None, entry_struct=None):
        """"""
        return object

    def parse_request_state(self, state=None):
        """"""
        return object

    def parse_reset_time(self, running_time=None):
        """"""
        return object

    def parse_segment_done(self, format=None, position=None):
        """"""
        return object

    def parse_segment_start(self, format=None, position=None):
        """"""
        return object

    def parse_state_changed(self, oldstate=None, newstate=None, pending=None):
        """"""
        return object

    def parse_step_done(self, format=None, amount=None, rate=None, flush=None, intermediate=None, duration=None, eos=None):
        """"""
        return object

    def parse_step_start(self, active=None, format=None, amount=None, rate=None, flush=None, intermediate=None):
        """"""
        return object

    def parse_stream_collection(self, collection=None):
        """"""
        return object

    def parse_stream_status(self, type=None, owner=None):
        """"""
        return object

    def parse_streams_selected(self, collection=None):
        """"""
        return object

    def parse_structure_change(self, type=None, owner=None, busy=None):
        """"""
        return object

    def parse_tag(self, tag_list=None):
        """"""
        return object

    def parse_toc(self, toc=None, updated=None):
        """"""
        return object

    def parse_warning(self, gerror=None, debug=None):
        """"""
        return object

    def parse_warning_details(self, structure=None):
        """"""
        return object

    def set_buffering_stats(self, mode=None, avg_in=None, avg_out=None, buffering_left=None):
        """"""
        return object

    def set_group_id(self, group_id=None):
        """"""
        return object

    def set_qos_stats(self, format=None, processed=None, dropped=None):
        """"""
        return object

    def set_qos_values(self, jitter=None, proportion=None, quality=None):
        """"""
        return object

    def set_seqnum(self, seqnum=None):
        """"""
        return object

    def set_stream_status_object(self, object=None):
        """"""
        return object

    def streams_selected_add(self, stream=None):
        """"""
        return object

    def streams_selected_get_size(self):
        """"""
        return object

    def streams_selected_get_stream(self, idx=None):
        """"""
        return object

    def writable_structure(self):
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def type(self):
        return object

    @property
    def timestamp(self):
        return object

    @property
    def src(self):
        return object

    @property
    def seqnum(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def cond(self):
        return object


class Meta():
    """"""
    @staticmethod
    def api_type_get_tags(api=None):
        """"""
        return object

    @staticmethod
    def api_type_has_tag(api=None, tag=None):
        """"""
        return object

    @staticmethod
    def api_type_register(api=None, tags=None):
        """"""
        return object

    @staticmethod
    def get_info(impl=None):
        """"""
        return object

    @staticmethod
    def register(api=None, impl=None, size=None, init_func=None, free_func=None, transform_func=None):
        """"""
        return object

    @property
    def flags(self):
        return object

    @property
    def info(self):
        return object


class MetaInfo():
    """"""

    @property
    def api(self):
        return object

    @property
    def type(self):
        return object

    @property
    def size(self):
        return object

    @property
    def init_func(self):
        return object

    @property
    def free_func(self):
        return object

    @property
    def transform_func(self):
        return object


class MetaTransformCopy():
    """"""

    @property
    def region(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def size(self):
        return object


class MiniObject():
    """"""

    def copy(self):
        """"""
        return object

    def get_qdata(self, quark=None):
        """"""
        return object

    def init(self, flags=None, type=None, copy_func=None, dispose_func=None, free_func=None):
        """"""
        return object

    def is_writable(self):
        """"""
        return object

    def lock(self, flags=None):
        """"""
        return object

    def make_writable(self):
        """"""
        return object

    def ref(self):
        """"""
        return object

    def set_qdata(self, quark=None, data=None, destroy=None):
        """"""
        return object

    def steal_qdata(self, quark=None):
        """"""
        return object

    def unlock(self, flags=None):
        """"""
        return object

    def unref(self):
        """"""
        return object

    def weak_ref(self, notify=None, data=None):
        """"""
        return object

    def weak_unref(self, notify=None, data=None):
        """"""
        return object

    @staticmethod
    def replace(olddata=None, newdata=None):
        """"""
        return object

    @staticmethod
    def steal(olddata=None):
        """"""
        return object

    @staticmethod
    def take(olddata=None, newdata=None):
        """"""
        return object

    @property
    def type(self):
        return object

    @property
    def refcount(self):
        return object

    @property
    def lockstate(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def copy(self):
        return object

    @property
    def dispose(self):
        return object

    @property
    def free(self):
        return object

    @property
    def n_qdata(self):
        return object

    @property
    def qdata(self):
        return object


class Object(GObject.InitiallyUnowned):
    """"""
    @staticmethod
    def check_uniqueness(list=None, name=None):
        """"""
        return object

    @staticmethod
    def default_deep_notify(object=None, orig=None, pspec=None, excluded_props=None):
        """"""
        return object

    @staticmethod
    def ref_sink(object=None):
        """"""
        return object

    @staticmethod
    def replace(oldobj=None, newobj=None):
        """"""
        return object

    def deep_notify(self, orig=None, pspec=None):
        """"""
        return object

    def add_control_binding(self, binding=None):
        """"""
        return object

    def default_error(self, error=None, debug=None):
        """"""
        return object

    def get_control_binding(self, property_name=None):
        """"""
        return object

    def get_control_rate(self):
        """"""
        return object

    def get_g_value_array(self, property_name=None, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    def get_name(self):
        """"""
        return object

    def get_parent(self):
        """"""
        return object

    def get_path_string(self):
        """"""
        return object

    def get_value(self, property_name=None, timestamp=None):
        """"""
        return object

    def get_value_array(self, property_name=None, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    def has_active_control_bindings(self):
        """"""
        return object

    def has_ancestor(self, ancestor=None):
        """"""
        return object

    def has_as_ancestor(self, ancestor=None):
        """"""
        return object

    def has_as_parent(self, parent=None):
        """"""
        return object

    def ref(self):
        """"""
        return object

    def remove_control_binding(self, binding=None):
        """"""
        return object

    def set_control_binding_disabled(self, property_name=None, disabled=None):
        """"""
        return object

    def set_control_bindings_disabled(self, disabled=None):
        """"""
        return object

    def set_control_rate(self, control_rate=None):
        """"""
        return object

    def set_name(self, name=None):
        """"""
        return object

    def set_parent(self, parent=None):
        """"""
        return object

    def suggest_next_sync(self):
        """"""
        return object

    def sync_values(self, timestamp=None):
        """"""
        return object

    def unparent(self):
        """"""
        return object

    def unref(self):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def name(self):
        return object

    @property
    def parent(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def control_bindings(self):
        return object

    @property
    def control_rate(self):
        return object

    @property
    def last_sync(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ObjectClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def path_string_separator(self):
        return object

    @property
    def deep_notify(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Pad(Object):
    """"""

    def __init__(self, name=None, direction=None):
        """"""
        return object

    @staticmethod
    def new(name=None, direction=None):
        """"""
        return object

    @staticmethod
    def new_from_static_template(templ=None, name=None):
        """"""
        return object

    @staticmethod
    def new_from_template(templ=None, name=None):
        """"""
        return object

    @staticmethod
    def link_get_name(ret=None):
        """"""
        return object

    def linked(self, peer=None):
        """"""
        return object

    def unlinked(self, peer=None):
        """"""
        return object

    def activate_mode(self, mode=None, active=None):
        """"""
        return object

    def add_probe(self, mask=None, callback=None, user_data=None, destroy_data=None):
        """"""
        return object

    def can_link(self, sinkpad=None):
        """"""
        return object

    def chain(self, buffer=None):
        """"""
        return object

    def chain_list(self, list=None):
        """"""
        return object

    def check_reconfigure(self):
        """"""
        return object

    def create_stream_id(self, parent=None, stream_id=None):
        """"""
        return object

    def create_stream_id_printf(self, parent=None, stream_id=None, *args):
        """"""
        return object

    def create_stream_id_printf_valist(self, parent=None, stream_id=None, var_args=None):
        """"""
        return object

    def event_default(self, parent=None, event=None):
        """"""
        return object

    def forward(self, forward=None, user_data=None):
        """"""
        return object

    def get_allowed_caps(self):
        """"""
        return object

    def get_current_caps(self):
        """"""
        return object

    def get_direction(self):
        """"""
        return object

    def get_element_private(self):
        """"""
        return object

    def get_last_flow_return(self):
        """"""
        return object

    def get_offset(self):
        """"""
        return object

    def get_pad_template(self):
        """"""
        return object

    def get_pad_template_caps(self):
        """"""
        return object

    def get_parent_element(self):
        """"""
        return object

    def get_peer(self):
        """"""
        return object

    def get_range(self, offset=None, size=None, buffer=None):
        """"""
        return object

    def get_sticky_event(self, event_type=None, idx=None):
        """"""
        return object

    def get_stream(self):
        """"""
        return object

    def get_stream_id(self):
        """"""
        return object

    def get_task_state(self):
        """"""
        return object

    def has_current_caps(self):
        """"""
        return object

    def is_active(self):
        """"""
        return object

    def is_blocked(self):
        """"""
        return object

    def is_blocking(self):
        """"""
        return object

    def is_linked(self):
        """"""
        return object

    def iterate_internal_links(self):
        """"""
        return object

    def iterate_internal_links_default(self, parent=None):
        """"""
        return object

    def link(self, sinkpad=None):
        """"""
        return object

    def link_full(self, sinkpad=None, flags=None):
        """"""
        return object

    def link_maybe_ghosting(self, sink=None):
        """"""
        return object

    def link_maybe_ghosting_full(self, sink=None, flags=None):
        """"""
        return object

    def mark_reconfigure(self):
        """"""
        return object

    def needs_reconfigure(self):
        """"""
        return object

    def pause_task(self):
        """"""
        return object

    def peer_query(self, query=None):
        """"""
        return object

    def peer_query_accept_caps(self, caps=None):
        """"""
        return object

    def peer_query_caps(self, filter=None):
        """"""
        return object

    def peer_query_convert(self, src_format=None, src_val=None, dest_format=None, dest_val=None):
        """"""
        return object

    def peer_query_duration(self, format=None, duration=None):
        """"""
        return object

    def peer_query_position(self, format=None, cur=None):
        """"""
        return object

    def proxy_query_accept_caps(self, query=None):
        """"""
        return object

    def proxy_query_caps(self, query=None):
        """"""
        return object

    def pull_range(self, offset=None, size=None, buffer=None):
        """"""
        return object

    def push(self, buffer=None):
        """"""
        return object

    def push_event(self, event=None):
        """"""
        return object

    def push_list(self, list=None):
        """"""
        return object

    def query(self, query=None):
        """"""
        return object

    def query_accept_caps(self, caps=None):
        """"""
        return object

    def query_caps(self, filter=None):
        """"""
        return object

    def query_convert(self, src_format=None, src_val=None, dest_format=None, dest_val=None):
        """"""
        return object

    def query_default(self, parent=None, query=None):
        """"""
        return object

    def query_duration(self, format=None, duration=None):
        """"""
        return object

    def query_position(self, format=None, cur=None):
        """"""
        return object

    def remove_probe(self, id=None):
        """"""
        return object

    def send_event(self, event=None):
        """"""
        return object

    def set_activate_function_full(self, activate=None, user_data=None, notify=None):
        """"""
        return object

    def set_activatemode_function_full(self, activatemode=None, user_data=None, notify=None):
        """"""
        return object

    def set_active(self, active=None):
        """"""
        return object

    def set_chain_function_full(self, chain=None, user_data=None, notify=None):
        """"""
        return object

    def set_chain_list_function_full(self, chainlist=None, user_data=None, notify=None):
        """"""
        return object

    def set_element_private(self, priv=None):
        """"""
        return object

    def set_event_full_function_full(self, event=None, user_data=None, notify=None):
        """"""
        return object

    def set_event_function_full(self, event=None, user_data=None, notify=None):
        """"""
        return object

    def set_getrange_function_full(self, get=None, user_data=None, notify=None):
        """"""
        return object

    def set_iterate_internal_links_function_full(self, iterintlink=None, user_data=None, notify=None):
        """"""
        return object

    def set_link_function_full(self, link=None, user_data=None, notify=None):
        """"""
        return object

    def set_offset(self, offset=None):
        """"""
        return object

    def set_query_function_full(self, query=None, user_data=None, notify=None):
        """"""
        return object

    def set_unlink_function_full(self, unlink=None, user_data=None, notify=None):
        """"""
        return object

    def start_task(self, func=None, user_data=None, notify=None):
        """"""
        return object

    def sticky_events_foreach(self, foreach_func=None, user_data=None):
        """"""
        return object

    def stop_task(self):
        """"""
        return object

    def store_sticky_event(self, event=None):
        """"""
        return object

    def unlink(self, sinkpad=None):
        """"""
        return object

    def use_fixed_caps(self):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def element_private(self):
        return object

    @property
    def padtemplate(self):
        return object

    @property
    def direction(self):
        return object

    @property
    def stream_rec_lock(self):
        return object

    @property
    def task(self):
        return object

    @property
    def block_cond(self):
        return object

    @property
    def probes(self):
        return object

    @property
    def mode(self):
        return object

    @property
    def activatefunc(self):
        return object

    @property
    def activatedata(self):
        return object

    @property
    def activatenotify(self):
        return object

    @property
    def activatemodefunc(self):
        return object

    @property
    def activatemodedata(self):
        return object

    @property
    def activatemodenotify(self):
        return object

    @property
    def peer(self):
        return object

    @property
    def linkfunc(self):
        return object

    @property
    def linkdata(self):
        return object

    @property
    def linknotify(self):
        return object

    @property
    def unlinkfunc(self):
        return object

    @property
    def unlinkdata(self):
        return object

    @property
    def unlinknotify(self):
        return object

    @property
    def chainfunc(self):
        return object

    @property
    def chaindata(self):
        return object

    @property
    def chainnotify(self):
        return object

    @property
    def chainlistfunc(self):
        return object

    @property
    def chainlistdata(self):
        return object

    @property
    def chainlistnotify(self):
        return object

    @property
    def getrangefunc(self):
        return object

    @property
    def getrangedata(self):
        return object

    @property
    def getrangenotify(self):
        return object

    @property
    def eventfunc(self):
        return object

    @property
    def eventdata(self):
        return object

    @property
    def eventnotify(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def queryfunc(self):
        return object

    @property
    def querydata(self):
        return object

    @property
    def querynotify(self):
        return object

    @property
    def iterintlinkfunc(self):
        return object

    @property
    def iterintlinkdata(self):
        return object

    @property
    def iterintlinknotify(self):
        return object

    @property
    def num_probes(self):
        return object

    @property
    def num_blocked(self):
        return object

    @property
    def priv(self):
        return object


class PadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def linked(self):
        return object

    @property
    def unlinked(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PadPrivate():
    """"""


class PadProbeInfo():
    """"""

    def get_buffer(self):
        """"""
        return object

    def get_buffer_list(self):
        """"""
        return object

    def get_event(self):
        """"""
        return object

    def get_query(self):
        """"""
        return object

    @property
    def type(self):
        return object

    @property
    def id(self):
        return object

    @property
    def data(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def size(self):
        return object


class PadTemplate(Object):
    """"""

    def __init__(self, name_template=None, direction=None, presence=None, caps=None):
        """"""
        return object

    @staticmethod
    def new(name_template=None, direction=None, presence=None, caps=None):
        """"""
        return object

    @staticmethod
    def new_from_static_pad_template_with_gtype(pad_template=None, pad_type=None):
        """"""
        return object

    @staticmethod
    def new_with_gtype(name_template=None, direction=None, presence=None, caps=None, pad_type=None):
        """"""
        return object

    def pad_created(self, pad=None):
        """"""
        return object

    def get_caps(self):
        """"""
        return object

    def pad_created(self, pad=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def name_template(self):
        return object

    @property
    def direction(self):
        return object

    @property
    def presence(self):
        return object

    @property
    def caps(self):
        return object


class PadTemplateClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def pad_created(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ParamArray(GObject.ParamSpec):
    """"""


class ParamFraction(GObject.ParamSpec):
    """"""


class ParamSpecArray():
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def element_spec(self):
        return object


class ParamSpecFraction():
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def min_num(self):
        return object

    @property
    def min_den(self):
        return object

    @property
    def max_num(self):
        return object

    @property
    def max_den(self):
        return object

    @property
    def def_num(self):
        return object

    @property
    def def_den(self):
        return object


class ParentBufferMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def buffer(self):
        return object


class ParseContext():
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    def copy(self):
        """"""
        return object

    def free(self):
        """"""
        return object

    def get_missing_elements(self):
        """"""
        return object


class PipelineClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PipelinePrivate():
    """"""


class Plugin(Object):
    """"""
    @staticmethod
    def list_free(list=None):
        """"""
        return object

    @staticmethod
    def load_by_name(name=None):
        """"""
        return object

    @staticmethod
    def load_file(filename=None):
        """"""
        return object

    @staticmethod
    def register_static(major_version=None, minor_version=None, name=None, description=None, init_func=None, version=None, license=None, source=None, package=None, origin=None):
        """"""
        return object

    @staticmethod
    def register_static_full(major_version=None, minor_version=None, name=None, description=None, init_full_func=None, version=None, license=None, source=None, package=None, origin=None, user_data=None):
        """"""
        return object

    def add_dependency(self, env_vars=None, paths=None, names=None, flags=None):
        """"""
        return object

    def add_dependency_simple(self, env_vars=None, paths=None, names=None, flags=None):
        """"""
        return object

    def get_cache_data(self):
        """"""
        return object

    def get_description(self):
        """"""
        return object

    def get_filename(self):
        """"""
        return object

    def get_license(self):
        """"""
        return object

    def get_name(self):
        """"""
        return object

    def get_origin(self):
        """"""
        return object

    def get_package(self):
        """"""
        return object

    def get_release_date_string(self):
        """"""
        return object

    def get_source(self):
        """"""
        return object

    def get_version(self):
        """"""
        return object

    def is_loaded(self):
        """"""
        return object

    def load(self):
        """"""
        return object

    def set_cache_data(self, cache_data=None):
        """"""
        return object


class PluginClass():
    """"""


class PluginDesc():
    """"""

    @property
    def major_version(self):
        return object

    @property
    def minor_version(self):
        return object

    @property
    def name(self):
        return object

    @property
    def description(self):
        return object

    @property
    def plugin_init(self):
        return object

    @property
    def version(self):
        return object

    @property
    def license(self):
        return object

    @property
    def source(self):
        return object

    @property
    def package(self):
        return object

    @property
    def origin(self):
        return object

    @property
    def release_datetime(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class PluginFeature(Object):
    """"""
    @staticmethod
    def list_copy(list=None):
        """"""
        return object

    @staticmethod
    def list_debug(list=None):
        """"""
        return object

    @staticmethod
    def list_free(list=None):
        """"""
        return object

    @staticmethod
    def rank_compare_func(p1=None, p2=None):
        """"""
        return object

    def check_version(self, min_major=None, min_minor=None, min_micro=None):
        """"""
        return object

    def get_plugin(self):
        """"""
        return object

    def get_plugin_name(self):
        """"""
        return object

    def get_rank(self):
        """"""
        return object

    def load(self):
        """"""
        return object

    def set_rank(self, rank=None):
        """"""
        return object


class PluginFeatureClass():
    """"""


class Poll():
    """"""

    def add_fd(self, fd=None):
        """"""
        return object

    def fd_can_read(self, fd=None):
        """"""
        return object

    def fd_can_write(self, fd=None):
        """"""
        return object

    def fd_ctl_read(self, fd=None, active=None):
        """"""
        return object

    def fd_ctl_write(self, fd=None, active=None):
        """"""
        return object

    def fd_has_closed(self, fd=None):
        """"""
        return object

    def fd_has_error(self, fd=None):
        """"""
        return object

    def fd_ignored(self, fd=None):
        """"""
        return object

    def free(self):
        """"""
        return object

    def get_read_gpollfd(self, fd=None):
        """"""
        return object

    def read_control(self):
        """"""
        return object

    def remove_fd(self, fd=None):
        """"""
        return object

    def restart(self):
        """"""
        return object

    def set_controllable(self, controllable=None):
        """"""
        return object

    def set_flushing(self, flushing=None):
        """"""
        return object

    def wait(self, timeout=None):
        """"""
        return object

    def write_control(self):
        """"""
        return object

    @staticmethod
    def new(controllable=None):
        """"""
        return object

    @staticmethod
    def new_timer():
        """"""
        return object


class PollFD():
    """"""

    def init(self):
        """"""
        return object

    @property
    def fd(self):
        return object

    @property
    def idx(self):
        return object


class Preset():
    """"""
    @staticmethod
    def get_app_dir():
        """"""
        return object

    @staticmethod
    def set_app_dir(app_dir=None):
        """"""
        return object

    def delete_preset(self, name=None):
        """"""
        return object

    def get_meta(self, name=None, tag=None, value=None):
        """"""
        return object

    def get_preset_names(self):
        """"""
        return object

    def get_property_names(self):
        """"""
        return object

    def load_preset(self, name=None):
        """"""
        return object

    def rename_preset(self, old_name=None, new_name=None):
        """"""
        return object

    def save_preset(self, name=None):
        """"""
        return object

    def set_meta(self, name=None, tag=None, value=None):
        """"""
        return object

    def delete_preset(self, name=None):
        """"""
        return object

    def get_meta(self, name=None, tag=None, value=None):
        """"""
        return object

    def get_preset_names(self):
        """"""
        return object

    def get_property_names(self):
        """"""
        return object

    def is_editable(self):
        """"""
        return object

    def load_preset(self, name=None):
        """"""
        return object

    def rename_preset(self, old_name=None, new_name=None):
        """"""
        return object

    def save_preset(self, name=None):
        """"""
        return object

    def set_meta(self, name=None, tag=None, value=None):
        """"""
        return object


class PresetInterface():
    """"""

    @property
    def parent(self):
        return object

    @property
    def get_preset_names(self):
        return object

    @property
    def get_property_names(self):
        return object

    @property
    def load_preset(self):
        return object

    @property
    def save_preset(self):
        return object

    @property
    def rename_preset(self):
        return object

    @property
    def delete_preset(self):
        return object

    @property
    def set_meta(self):
        return object

    @property
    def get_meta(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Promise():
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    @staticmethod
    def new_with_change_func(func=None, user_data=None, notify=None):
        """"""
        return object

    def expire(self):
        """"""
        return object

    def get_reply(self):
        """"""
        return object

    def interrupt(self):
        """"""
        return object

    def reply(self, s=None):
        """"""
        return object

    def wait(self):
        """"""
        return object

    @property
    def parent(self):
        return object


class ProtectionMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def info(self):
        return object


class ProxyPad(Pad):
    """"""
    @staticmethod
    def chain_default(pad=None, parent=None, buffer=None):
        """"""
        return object

    @staticmethod
    def chain_list_default(pad=None, parent=None, list=None):
        """"""
        return object

    @staticmethod
    def getrange_default(pad=None, parent=None, offset=None, size=None, buffer=None):
        """"""
        return object

    @staticmethod
    def iterate_internal_links_default(pad=None, parent=None):
        """"""
        return object

    def get_internal(self):
        """"""
        return object

    @property
    def pad(self):
        return object

    @property
    def priv(self):
        return object


class ProxyPadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ProxyPadPrivate():
    """"""


class Query():
    """"""
    @staticmethod
    def new_accept_caps(caps=None):
        """"""
        return object

    @staticmethod
    def new_allocation(caps=None, need_pool=None):
        """"""
        return object

    @staticmethod
    def new_buffering(format=None):
        """"""
        return object

    @staticmethod
    def new_caps(filter=None):
        """"""
        return object

    @staticmethod
    def new_context(context_type=None):
        """"""
        return object

    @staticmethod
    def new_convert(src_format=None, value=None, dest_format=None):
        """"""
        return object

    @staticmethod
    def new_custom(type=None, structure=None):
        """"""
        return object

    @staticmethod
    def new_drain():
        """"""
        return object

    @staticmethod
    def new_duration(format=None):
        """"""
        return object

    @staticmethod
    def new_formats():
        """"""
        return object

    @staticmethod
    def new_latency():
        """"""
        return object

    @staticmethod
    def new_position(format=None):
        """"""
        return object

    @staticmethod
    def new_scheduling():
        """"""
        return object

    @staticmethod
    def new_seeking(format=None):
        """"""
        return object

    @staticmethod
    def new_segment(format=None):
        """"""
        return object

    @staticmethod
    def new_uri():
        """"""
        return object

    def add_allocation_meta(self, api=None, params=None):
        """"""
        return object

    def add_allocation_param(self, allocator=None, params=None):
        """"""
        return object

    def add_allocation_pool(self, pool=None, size=None, min_buffers=None, max_buffers=None):
        """"""
        return object

    def add_buffering_range(self, start=None, stop=None):
        """"""
        return object

    def add_scheduling_mode(self, mode=None):
        """"""
        return object

    def find_allocation_meta(self, api=None, index=None):
        """"""
        return object

    def get_n_allocation_metas(self):
        """"""
        return object

    def get_n_allocation_params(self):
        """"""
        return object

    def get_n_allocation_pools(self):
        """"""
        return object

    def get_n_buffering_ranges(self):
        """"""
        return object

    def get_n_scheduling_modes(self):
        """"""
        return object

    def get_structure(self):
        """"""
        return object

    def has_scheduling_mode(self, mode=None):
        """"""
        return object

    def has_scheduling_mode_with_flags(self, mode=None, flags=None):
        """"""
        return object

    def parse_accept_caps(self, caps=None):
        """"""
        return object

    def parse_accept_caps_result(self, result=None):
        """"""
        return object

    def parse_allocation(self, caps=None, need_pool=None):
        """"""
        return object

    def parse_buffering_percent(self, busy=None, percent=None):
        """"""
        return object

    def parse_buffering_range(self, format=None, start=None, stop=None, estimated_total=None):
        """"""
        return object

    def parse_buffering_stats(self, mode=None, avg_in=None, avg_out=None, buffering_left=None):
        """"""
        return object

    def parse_caps(self, filter=None):
        """"""
        return object

    def parse_caps_result(self, caps=None):
        """"""
        return object

    def parse_context(self, context=None):
        """"""
        return object

    def parse_context_type(self, context_type=None):
        """"""
        return object

    def parse_convert(self, src_format=None, src_value=None, dest_format=None, dest_value=None):
        """"""
        return object

    def parse_duration(self, format=None, duration=None):
        """"""
        return object

    def parse_latency(self, live=None, min_latency=None, max_latency=None):
        """"""
        return object

    def parse_n_formats(self, n_formats=None):
        """"""
        return object

    def parse_nth_allocation_meta(self, index=None, params=None):
        """"""
        return object

    def parse_nth_allocation_param(self, index=None, allocator=None, params=None):
        """"""
        return object

    def parse_nth_allocation_pool(self, index=None, pool=None, size=None, min_buffers=None, max_buffers=None):
        """"""
        return object

    def parse_nth_buffering_range(self, index=None, start=None, stop=None):
        """"""
        return object

    def parse_nth_format(self, nth=None, format=None):
        """"""
        return object

    def parse_nth_scheduling_mode(self, index=None):
        """"""
        return object

    def parse_position(self, format=None, cur=None):
        """"""
        return object

    def parse_scheduling(self, flags=None, minsize=None, maxsize=None, align=None):
        """"""
        return object

    def parse_seeking(self, format=None, seekable=None, segment_start=None, segment_end=None):
        """"""
        return object

    def parse_segment(self, rate=None, format=None, start_value=None, stop_value=None):
        """"""
        return object

    def parse_uri(self, uri=None):
        """"""
        return object

    def parse_uri_redirection(self, uri=None):
        """"""
        return object

    def parse_uri_redirection_permanent(self, permanent=None):
        """"""
        return object

    def remove_nth_allocation_meta(self, index=None):
        """"""
        return object

    def remove_nth_allocation_param(self, index=None):
        """"""
        return object

    def remove_nth_allocation_pool(self, index=None):
        """"""
        return object

    def set_accept_caps_result(self, result=None):
        """"""
        return object

    def set_buffering_percent(self, busy=None, percent=None):
        """"""
        return object

    def set_buffering_range(self, format=None, start=None, stop=None, estimated_total=None):
        """"""
        return object

    def set_buffering_stats(self, mode=None, avg_in=None, avg_out=None, buffering_left=None):
        """"""
        return object

    def set_caps_result(self, caps=None):
        """"""
        return object

    def set_context(self, context=None):
        """"""
        return object

    def set_convert(self, src_format=None, src_value=None, dest_format=None, dest_value=None):
        """"""
        return object

    def set_duration(self, format=None, duration=None):
        """"""
        return object

    def set_formats(self, n_formats=None, *args):
        """"""
        return object

    def set_formatsv(self, n_formats=None, formats=None):
        """"""
        return object

    def set_latency(self, live=None, min_latency=None, max_latency=None):
        """"""
        return object

    def set_nth_allocation_param(self, index=None, allocator=None, params=None):
        """"""
        return object

    def set_nth_allocation_pool(self, index=None, pool=None, size=None, min_buffers=None, max_buffers=None):
        """"""
        return object

    def set_position(self, format=None, cur=None):
        """"""
        return object

    def set_scheduling(self, flags=None, minsize=None, maxsize=None, align=None):
        """"""
        return object

    def set_seeking(self, format=None, seekable=None, segment_start=None, segment_end=None):
        """"""
        return object

    def set_segment(self, rate=None, format=None, start_value=None, stop_value=None):
        """"""
        return object

    def set_uri(self, uri=None):
        """"""
        return object

    def set_uri_redirection(self, uri=None):
        """"""
        return object

    def set_uri_redirection_permanent(self, permanent=None):
        """"""
        return object

    def writable_structure(self):
        """"""
        return object

    @property
    def mini_object(self):
        return object

    @property
    def type(self):
        return object


class ReferenceTimestampMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def reference(self):
        return object

    @property
    def timestamp(self):
        return object

    @property
    def duration(self):
        return object


class Registry(Object):
    """"""
    @staticmethod
    def fork_is_enabled():
        """"""
        return object

    @staticmethod
    def fork_set_enabled(enabled=None):
        """"""
        return object

    @staticmethod
    def get():
        """"""
        return object

    def add_feature(self, feature=None):
        """"""
        return object

    def add_plugin(self, plugin=None):
        """"""
        return object

    def check_feature_version(self, feature_name=None, min_major=None, min_minor=None, min_micro=None):
        """"""
        return object

    def feature_filter(self, filter=None, first=None, user_data=None):
        """"""
        return object

    def find_feature(self, name=None, type=None):
        """"""
        return object

    def find_plugin(self, name=None):
        """"""
        return object

    def get_feature_list(self, type=None):
        """"""
        return object

    def get_feature_list_by_plugin(self, name=None):
        """"""
        return object

    def get_feature_list_cookie(self):
        """"""
        return object

    def get_plugin_list(self):
        """"""
        return object

    def lookup(self, filename=None):
        """"""
        return object

    def lookup_feature(self, name=None):
        """"""
        return object

    def plugin_filter(self, filter=None, first=None, user_data=None):
        """"""
        return object

    def remove_feature(self, feature=None):
        """"""
        return object

    def remove_plugin(self, plugin=None):
        """"""
        return object

    def scan_path(self, path=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def priv(self):
        return object


class RegistryClass():
    """"""

    @property
    def parent_class(self):
        return object


class RegistryPrivate():
    """"""


class Sample():
    """"""

    def __init__(self, buffer=None, caps=None, segment=None, info=None):
        """"""
        return object

    @staticmethod
    def new(buffer=None, caps=None, segment=None, info=None):
        """"""
        return object

    def get_buffer(self):
        """"""
        return object

    def get_buffer_list(self):
        """"""
        return object

    def get_caps(self):
        """"""
        return object

    def get_info(self):
        """"""
        return object

    def get_segment(self):
        """"""
        return object

    def set_buffer_list(self, buffer_list=None):
        """"""
        return object


class Segment():
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    def clip(self, format=None, start=None, stop=None, clip_start=None, clip_stop=None):
        """"""
        return object

    def copy(self):
        """"""
        return object

    def copy_into(self, dest=None):
        """"""
        return object

    def do_seek(self, rate=None, format=None, flags=None, start_type=None, start=None, stop_type=None, stop=None, update=None):
        """"""
        return object

    def free(self):
        """"""
        return object

    def init(self, format=None):
        """"""
        return object

    def is_equal(self, s1=None):
        """"""
        return object

    def offset_running_time(self, format=None, offset=None):
        """"""
        return object

    def position_from_running_time(self, format=None, running_time=None):
        """"""
        return object

    def position_from_running_time_full(self, format=None, running_time=None, position=None):
        """"""
        return object

    def position_from_stream_time(self, format=None, stream_time=None):
        """"""
        return object

    def position_from_stream_time_full(self, format=None, stream_time=None, position=None):
        """"""
        return object

    def set_running_time(self, format=None, running_time=None):
        """"""
        return object

    def to_position(self, format=None, running_time=None):
        """"""
        return object

    def to_running_time(self, format=None, position=None):
        """"""
        return object

    def to_running_time_full(self, format=None, position=None, running_time=None):
        """"""
        return object

    def to_stream_time(self, format=None, position=None):
        """"""
        return object

    def to_stream_time_full(self, format=None, position=None, stream_time=None):
        """"""
        return object

    @property
    def flags(self):
        return object

    @property
    def rate(self):
        return object

    @property
    def applied_rate(self):
        return object

    @property
    def format(self):
        return object

    @property
    def base(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def time(self):
        return object

    @property
    def position(self):
        return object

    @property
    def duration(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class StaticCaps():
    """"""

    def cleanup(self):
        """"""
        return object

    def get(self):
        """"""
        return object

    @property
    def caps(self):
        return object

    @property
    def string(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class StaticPadTemplate():
    """"""

    def get(self):
        """"""
        return object

    def get_caps(self):
        """"""
        return object

    @property
    def name_template(self):
        return object

    @property
    def direction(self):
        return object

    @property
    def presence(self):
        return object

    @property
    def static_caps(self):
        return object


class Stream(Object):
    """"""

    def __init__(self, stream_id=None, caps=None, type=None, flags=None):
        """"""
        return object

    @staticmethod
    def new(stream_id=None, caps=None, type=None, flags=None):
        """"""
        return object

    def get_caps(self):
        """"""
        return object

    def get_stream_flags(self):
        """"""
        return object

    def get_stream_id(self):
        """"""
        return object

    def get_stream_type(self):
        """"""
        return object

    def get_tags(self):
        """"""
        return object

    def set_caps(self, caps=None):
        """"""
        return object

    def set_stream_flags(self, flags=None):
        """"""
        return object

    def set_stream_type(self, stream_type=None):
        """"""
        return object

    def set_tags(self, tags=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def stream_id(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class StreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class StreamCollection(Object):
    """"""

    def __init__(self, upstream_id=None):
        """"""
        return object

    @staticmethod
    def new(upstream_id=None):
        """"""
        return object

    def stream_notify(self, stream=None, pspec=None):
        """"""
        return object

    def add_stream(self, stream=None):
        """"""
        return object

    def get_size(self):
        """"""
        return object

    def get_stream(self, index=None):
        """"""
        return object

    def get_upstream_id(self):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def upstream_id(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class StreamCollectionClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def stream_notify(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class StreamCollectionPrivate():
    """"""


class StreamPrivate():
    """"""


class Structure():
    """"""

    def __init__(self, name=None, firstfield=None, *args):
        """"""
        return object

    @staticmethod
    def new(name=None, firstfield=None, *args):
        """"""
        return object

    @staticmethod
    def new_empty(name=None):
        """"""
        return object

    @staticmethod
    def new_from_string(string=None):
        """"""
        return object

    @staticmethod
    def new_id(name_quark=None, field_quark=None, *args):
        """"""
        return object

    @staticmethod
    def new_id_empty(quark=None):
        """"""
        return object

    @staticmethod
    def new_valist(name=None, firstfield=None, varargs=None):
        """"""
        return object

    def can_intersect(self, struct2=None):
        """"""
        return object

    def copy(self):
        """"""
        return object

    def filter_and_map_in_place(self, func=None, user_data=None):
        """"""
        return object

    def fixate(self):
        """"""
        return object

    def fixate_field(self, field_name=None):
        """"""
        return object

    def fixate_field_boolean(self, field_name=None, target=None):
        """"""
        return object

    def fixate_field_nearest_double(self, field_name=None, target=None):
        """"""
        return object

    def fixate_field_nearest_fraction(self, field_name=None, target_numerator=None, target_denominator=None):
        """"""
        return object

    def fixate_field_nearest_int(self, field_name=None, target=None):
        """"""
        return object

    def fixate_field_string(self, field_name=None, target=None):
        """"""
        return object

    def foreach(self, func=None, user_data=None):
        """"""
        return object

    def free(self):
        """"""
        return object

    def get(self, first_fieldname=None, *args):
        """"""
        return object

    def get_array(self, fieldname=None, array=None):
        """"""
        return object

    def get_boolean(self, fieldname=None, value=None):
        """"""
        return object

    def get_clock_time(self, fieldname=None, value=None):
        """"""
        return object

    def get_date(self, fieldname=None, value=None):
        """"""
        return object

    def get_date_time(self, fieldname=None, value=None):
        """"""
        return object

    def get_double(self, fieldname=None, value=None):
        """"""
        return object

    def get_enum(self, fieldname=None, enumtype=None, value=None):
        """"""
        return object

    def get_field_type(self, fieldname=None):
        """"""
        return object

    def get_flagset(self, fieldname=None, value_flags=None, value_mask=None):
        """"""
        return object

    def get_fraction(self, fieldname=None, value_numerator=None, value_denominator=None):
        """"""
        return object

    def get_int(self, fieldname=None, value=None):
        """"""
        return object

    def get_int64(self, fieldname=None, value=None):
        """"""
        return object

    def get_list(self, fieldname=None, array=None):
        """"""
        return object

    def get_name(self):
        """"""
        return object

    def get_name_id(self):
        """"""
        return object

    def get_string(self, fieldname=None):
        """"""
        return object

    def get_uint(self, fieldname=None, value=None):
        """"""
        return object

    def get_uint64(self, fieldname=None, value=None):
        """"""
        return object

    def get_valist(self, first_fieldname=None, args=None):
        """"""
        return object

    def get_value(self, fieldname=None):
        """"""
        return object

    def has_field(self, fieldname=None):
        """"""
        return object

    def has_field_typed(self, fieldname=None, type=None):
        """"""
        return object

    def has_name(self, name=None):
        """"""
        return object

    def id_get(self, first_field_id=None, *args):
        """"""
        return object

    def id_get_valist(self, first_field_id=None, args=None):
        """"""
        return object

    def id_get_value(self, field=None):
        """"""
        return object

    def id_has_field(self, field=None):
        """"""
        return object

    def id_has_field_typed(self, field=None, type=None):
        """"""
        return object

    def id_set(self, fieldname=None, *args):
        """"""
        return object

    def id_set_valist(self, fieldname=None, varargs=None):
        """"""
        return object

    def id_set_value(self, field=None, value=None):
        """"""
        return object

    def id_take_value(self, field=None, value=None):
        """"""
        return object

    def intersect(self, struct2=None):
        """"""
        return object

    def is_equal(self, structure2=None):
        """"""
        return object

    def is_subset(self, superset=None):
        """"""
        return object

    def map_in_place(self, func=None, user_data=None):
        """"""
        return object

    def n_fields(self):
        """"""
        return object

    def nth_field_name(self, index=None):
        """"""
        return object

    def remove_all_fields(self):
        """"""
        return object

    def remove_field(self, fieldname=None):
        """"""
        return object

    def remove_fields(self, fieldname=None, *args):
        """"""
        return object

    def remove_fields_valist(self, fieldname=None, varargs=None):
        """"""
        return object

    def set(self, fieldname=None, *args):
        """"""
        return object

    def set_array(self, fieldname=None, array=None):
        """"""
        return object

    def set_list(self, fieldname=None, array=None):
        """"""
        return object

    def set_name(self, name=None):
        """"""
        return object

    def set_parent_refcount(self, refcount=None):
        """"""
        return object

    def set_valist(self, fieldname=None, varargs=None):
        """"""
        return object

    def set_value(self, fieldname=None, value=None):
        """"""
        return object

    def take_value(self, fieldname=None, value=None):
        """"""
        return object

    def to_string(self):
        """"""
        return object

    @staticmethod
    def from_string(string=None, end=None):
        """"""
        return object

    @property
    def type(self):
        return object

    @property
    def name(self):
        return object


class SystemClockClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class SystemClockPrivate():
    """"""


class TagList():
    """"""

    def __init__(self, tag=None, *args):
        """"""
        return object

    @staticmethod
    def new(tag=None, *args):
        """"""
        return object

    @staticmethod
    def new_empty():
        """"""
        return object

    @staticmethod
    def new_from_string(str=None):
        """"""
        return object

    @staticmethod
    def new_valist(var_args=None):
        """"""
        return object

    def add(self, mode=None, tag=None, *args):
        """"""
        return object

    def add_valist(self, mode=None, tag=None, var_args=None):
        """"""
        return object

    def add_valist_values(self, mode=None, tag=None, var_args=None):
        """"""
        return object

    def add_value(self, mode=None, tag=None, value=None):
        """"""
        return object

    def add_values(self, mode=None, tag=None, *args):
        """"""
        return object

    def foreach(self, func=None, user_data=None):
        """"""
        return object

    def get_boolean(self, tag=None, value=None):
        """"""
        return object

    def get_boolean_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_date(self, tag=None, value=None):
        """"""
        return object

    def get_date_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_date_time(self, tag=None, value=None):
        """"""
        return object

    def get_date_time_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_double(self, tag=None, value=None):
        """"""
        return object

    def get_double_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_float(self, tag=None, value=None):
        """"""
        return object

    def get_float_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_int(self, tag=None, value=None):
        """"""
        return object

    def get_int64(self, tag=None, value=None):
        """"""
        return object

    def get_int64_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_int_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_pointer(self, tag=None, value=None):
        """"""
        return object

    def get_pointer_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_sample(self, tag=None, sample=None):
        """"""
        return object

    def get_sample_index(self, tag=None, index=None, sample=None):
        """"""
        return object

    def get_scope(self):
        """"""
        return object

    def get_string(self, tag=None, value=None):
        """"""
        return object

    def get_string_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_tag_size(self, tag=None):
        """"""
        return object

    def get_uint(self, tag=None, value=None):
        """"""
        return object

    def get_uint64(self, tag=None, value=None):
        """"""
        return object

    def get_uint64_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_uint_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def get_value_index(self, tag=None, index=None):
        """"""
        return object

    def insert(self, _from=None, mode=None):
        """"""
        return object

    def is_empty(self):
        """"""
        return object

    def is_equal(self, list2=None):
        """"""
        return object

    def merge(self, list2=None, mode=None):
        """"""
        return object

    def n_tags(self):
        """"""
        return object

    def nth_tag_name(self, index=None):
        """"""
        return object

    def peek_string_index(self, tag=None, index=None, value=None):
        """"""
        return object

    def remove_tag(self, tag=None):
        """"""
        return object

    def set_scope(self, scope=None):
        """"""
        return object

    def to_string(self):
        """"""
        return object

    @staticmethod
    def copy_value(dest=None, list=None, tag=None):
        """"""
        return object

    @property
    def mini_object(self):
        return object


class TagSetter():
    """"""

    def add_tag_valist(self, mode=None, tag=None, var_args=None):
        """"""
        return object

    def add_tag_valist_values(self, mode=None, tag=None, var_args=None):
        """"""
        return object

    def add_tag_value(self, mode=None, tag=None, value=None):
        """"""
        return object

    def add_tag_values(self, mode=None, tag=None, *args):
        """"""
        return object

    def add_tags(self, mode=None, tag=None, *args):
        """"""
        return object

    def get_tag_list(self):
        """"""
        return object

    def get_tag_merge_mode(self):
        """"""
        return object

    def merge_tags(self, list=None, mode=None):
        """"""
        return object

    def reset_tags(self):
        """"""
        return object

    def set_tag_merge_mode(self, mode=None):
        """"""
        return object


class TagSetterInterface():
    """"""

    @property
    def g_iface(self):
        return object


class Task(Object):
    """"""

    def __init__(self, func=None, user_data=None, notify=None):
        """"""
        return object

    @staticmethod
    def new(func=None, user_data=None, notify=None):
        """"""
        return object

    @staticmethod
    def cleanup_all():
        """"""
        return object

    def get_pool(self):
        """"""
        return object

    def get_state(self):
        """"""
        return object

    def join(self):
        """"""
        return object

    def pause(self):
        """"""
        return object

    def set_enter_callback(self, enter_func=None, user_data=None, notify=None):
        """"""
        return object

    def set_leave_callback(self, leave_func=None, user_data=None, notify=None):
        """"""
        return object

    def set_lock(self, mutex=None):
        """"""
        return object

    def set_pool(self, pool=None):
        """"""
        return object

    def set_state(self, state=None):
        """"""
        return object

    def start(self):
        """"""
        return object

    def stop(self):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def state(self):
        return object

    @property
    def cond(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def func(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def running(self):
        return object

    @property
    def thread(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TaskClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def pool(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TaskPool(Object):
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    def cleanup(self):
        """"""
        return object

    def join(self, id=None):
        """"""
        return object

    def prepare(self):
        """"""
        return object

    def push(self, func=None, user_data=None):
        """"""
        return object

    def cleanup(self):
        """"""
        return object

    def join(self, id=None):
        """"""
        return object

    def prepare(self):
        """"""
        return object

    def push(self, func=None, user_data=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def pool(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TaskPoolClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def prepare(self):
        return object

    @property
    def cleanup(self):
        return object

    @property
    def push(self):
        return object

    @property
    def join(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TaskPrivate():
    """"""


class TimedValue():
    """"""

    @property
    def timestamp(self):
        return object

    @property
    def value(self):
        return object


class Toc():
    """"""

    def __init__(self, scope=None):
        """"""
        return object

    @staticmethod
    def new(scope=None):
        """"""
        return object

    def append_entry(self, entry=None):
        """"""
        return object

    def dump(self):
        """"""
        return object

    def find_entry(self, uid=None):
        """"""
        return object

    def get_entries(self):
        """"""
        return object

    def get_scope(self):
        """"""
        return object

    def get_tags(self):
        """"""
        return object

    def merge_tags(self, tags=None, mode=None):
        """"""
        return object

    def set_tags(self, tags=None):
        """"""
        return object


class TocEntry():
    """"""

    def __init__(self, type=None, uid=None):
        """"""
        return object

    @staticmethod
    def new(type=None, uid=None):
        """"""
        return object

    def append_sub_entry(self, subentry=None):
        """"""
        return object

    def get_entry_type(self):
        """"""
        return object

    def get_loop(self, loop_type=None, repeat_count=None):
        """"""
        return object

    def get_parent(self):
        """"""
        return object

    def get_start_stop_times(self, start=None, stop=None):
        """"""
        return object

    def get_sub_entries(self):
        """"""
        return object

    def get_tags(self):
        """"""
        return object

    def get_toc(self):
        """"""
        return object

    def get_uid(self):
        """"""
        return object

    def is_alternative(self):
        """"""
        return object

    def is_sequence(self):
        """"""
        return object

    def merge_tags(self, tags=None, mode=None):
        """"""
        return object

    def set_loop(self, loop_type=None, repeat_count=None):
        """"""
        return object

    def set_start_stop_times(self, start=None, stop=None):
        """"""
        return object

    def set_tags(self, tags=None):
        """"""
        return object


class TocSetter():
    """"""

    def get_toc(self):
        """"""
        return object

    def reset(self):
        """"""
        return object

    def set_toc(self, toc=None):
        """"""
        return object


class TocSetterInterface():
    """"""

    @property
    def g_iface(self):
        return object


class Tracer(Object):
    """"""

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TracerClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TracerFactory(PluginFeature):
    """"""
    @staticmethod
    def get_list():
        """"""
        return object

    def get_tracer_type(self):
        """"""
        return object


class TracerFactoryClass():
    """"""


class TracerPrivate():
    """"""


class TracerRecord(Object):
    """"""


class TracerRecordClass():
    """"""


class TypeFind():
    """"""

    def get_length(self):
        """"""
        return object

    def peek(self, offset=None, size=None):
        """"""
        return object

    def suggest(self, probability=None, caps=None):
        """"""
        return object

    def suggest_simple(self, probability=None, media_type=None, fieldname=None, *args):
        """"""
        return object

    @staticmethod
    def register(plugin=None, name=None, rank=None, func=None, extensions=None, possible_caps=None, data=None, data_notify=None):
        """"""
        return object

    @property
    def peek(self):
        return object

    @property
    def suggest(self):
        return object

    @property
    def data(self):
        return object

    @property
    def get_length(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TypeFindFactory(PluginFeature):
    """"""
    @staticmethod
    def get_list():
        """"""
        return object

    def call_function(self, find=None):
        """"""
        return object

    def get_caps(self):
        """"""
        return object

    def get_extensions(self):
        """"""
        return object

    def has_function(self):
        """"""
        return object


class TypeFindFactoryClass():
    """"""


class URIHandler():
    """"""

    def get_uri(self):
        """"""
        return object

    def set_uri(self, uri=None):
        """"""
        return object

    def get_protocols(self):
        """"""
        return object

    def get_uri(self):
        """"""
        return object

    def get_uri_type(self):
        """"""
        return object

    def set_uri(self, uri=None):
        """"""
        return object


class URIHandlerInterface():
    """"""

    @property
    def parent(self):
        return object

    @property
    def get_type(self):
        return object

    @property
    def get_protocols(self):
        return object

    @property
    def get_uri(self):
        return object

    @property
    def set_uri(self):
        return object


class Uri():
    """"""

    def __init__(self, scheme=None, userinfo=None, host=None, port=None, path=None, query=None, fragment=None):
        """"""
        return object

    @staticmethod
    def new(scheme=None, userinfo=None, host=None, port=None, path=None, query=None, fragment=None):
        """"""
        return object

    def append_path(self, relative_path=None):
        """"""
        return object

    def append_path_segment(self, path_segment=None):
        """"""
        return object

    def equal(self, second=None):
        """"""
        return object

    def from_string_with_base(self, uri=None):
        """"""
        return object

    def get_fragment(self):
        """"""
        return object

    def get_host(self):
        """"""
        return object

    def get_media_fragment_table(self):
        """"""
        return object

    def get_path(self):
        """"""
        return object

    def get_path_segments(self):
        """"""
        return object

    def get_path_string(self):
        """"""
        return object

    def get_port(self):
        """"""
        return object

    def get_query_keys(self):
        """"""
        return object

    def get_query_string(self):
        """"""
        return object

    def get_query_table(self):
        """"""
        return object

    def get_query_value(self, query_key=None):
        """"""
        return object

    def get_scheme(self):
        """"""
        return object

    def get_userinfo(self):
        """"""
        return object

    def is_normalized(self):
        """"""
        return object

    def is_writable(self):
        """"""
        return object

    def join(self, ref_uri=None):
        """"""
        return object

    def make_writable(self):
        """"""
        return object

    def new_with_base(self, scheme=None, userinfo=None, host=None, port=None, path=None, query=None, fragment=None):
        """"""
        return object

    def normalize(self):
        """"""
        return object

    def query_has_key(self, query_key=None):
        """"""
        return object

    def remove_query_key(self, query_key=None):
        """"""
        return object

    def set_fragment(self, fragment=None):
        """"""
        return object

    def set_host(self, host=None):
        """"""
        return object

    def set_path(self, path=None):
        """"""
        return object

    def set_path_segments(self, path_segments=None):
        """"""
        return object

    def set_path_string(self, path=None):
        """"""
        return object

    def set_port(self, port=None):
        """"""
        return object

    def set_query_string(self, query=None):
        """"""
        return object

    def set_query_table(self, query_table=None):
        """"""
        return object

    def set_query_value(self, query_key=None, query_value=None):
        """"""
        return object

    def set_scheme(self, scheme=None):
        """"""
        return object

    def set_userinfo(self, userinfo=None):
        """"""
        return object

    def to_string(self):
        """"""
        return object

    @staticmethod
    def construct(protocol=None, location=None):
        """"""
        return object

    @staticmethod
    def from_string(uri=None):
        """"""
        return object

    @staticmethod
    def get_location(uri=None):
        """"""
        return object

    @staticmethod
    def get_protocol(uri=None):
        """"""
        return object

    @staticmethod
    def has_protocol(uri=None, protocol=None):
        """"""
        return object

    @staticmethod
    def is_valid(uri=None):
        """"""
        return object

    @staticmethod
    def join_strings(base_uri=None, ref_uri=None):
        """"""
        return object

    @staticmethod
    def protocol_is_supported(type=None, protocol=None):
        """"""
        return object

    @staticmethod
    def protocol_is_valid(protocol=None):
        """"""
        return object


class ValueArray():
    """"""
    @staticmethod
    def append_and_take_value(value=None, append_value=None):
        """"""
        return object

    @staticmethod
    def append_value(value=None, append_value=None):
        """"""
        return object

    @staticmethod
    def get_size(value=None):
        """"""
        return object

    @staticmethod
    def get_value(value=None, index=None):
        """"""
        return object

    @staticmethod
    def prepend_value(value=None, prepend_value=None):
        """"""
        return object


class ValueList():
    """"""
    @staticmethod
    def append_and_take_value(value=None, append_value=None):
        """"""
        return object

    @staticmethod
    def append_value(value=None, append_value=None):
        """"""
        return object

    @staticmethod
    def concat(dest=None, value1=None, value2=None):
        """"""
        return object

    @staticmethod
    def get_size(value=None):
        """"""
        return object

    @staticmethod
    def get_value(value=None, index=None):
        """"""
        return object

    @staticmethod
    def merge(dest=None, value1=None, value2=None):
        """"""
        return object

    @staticmethod
    def prepend_value(value=None, prepend_value=None):
        """"""
        return object


class ValueTable():
    """"""

    @property
    def type(self):
        return object

    @property
    def compare(self):
        return object

    @property
    def serialize(self):
        return object

    @property
    def deserialize(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Allocator(Object):
    """"""
    @staticmethod
    def find(name=None):
        """"""
        return object

    @staticmethod
    def register(name=None, allocator=None):
        """"""
        return object

    def alloc(self, size=None, params=None):
        """"""
        return object

    def free(self, memory=None):
        """"""
        return object

    def alloc(self, size=None, params=None):
        """"""
        return object

    def free(self, memory=None):
        """"""
        return object

    def set_default(self):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def mem_type(self):
        return object

    @property
    def mem_map(self):
        return object

    @property
    def mem_unmap(self):
        return object

    @property
    def mem_copy(self):
        return object

    @property
    def mem_share(self):
        return object

    @property
    def mem_is_span(self):
        return object

    @property
    def mem_map_full(self):
        return object

    @property
    def mem_unmap_full(self):
        return object

    @property
    def _gst_reserved(self):
        return object

    @property
    def priv(self):
        return object


class BufferPool(Object):
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    @staticmethod
    def config_add_option(config=None, option=None):
        """"""
        return object

    @staticmethod
    def config_get_allocator(config=None, allocator=None, params=None):
        """"""
        return object

    @staticmethod
    def config_get_option(config=None, index=None):
        """"""
        return object

    @staticmethod
    def config_get_params(config=None, caps=None, size=None, min_buffers=None, max_buffers=None):
        """"""
        return object

    @staticmethod
    def config_has_option(config=None, option=None):
        """"""
        return object

    @staticmethod
    def config_n_options(config=None):
        """"""
        return object

    @staticmethod
    def config_set_allocator(config=None, allocator=None, params=None):
        """"""
        return object

    @staticmethod
    def config_set_params(config=None, caps=None, size=None, min_buffers=None, max_buffers=None):
        """"""
        return object

    @staticmethod
    def config_validate_params(config=None, caps=None, size=None, min_buffers=None, max_buffers=None):
        """"""
        return object

    def acquire_buffer(self, buffer=None, params=None):
        """"""
        return object

    def alloc_buffer(self, buffer=None, params=None):
        """"""
        return object

    def flush_start(self):
        """"""
        return object

    def flush_stop(self):
        """"""
        return object

    def free_buffer(self, buffer=None):
        """"""
        return object

    def get_options(self):
        """"""
        return object

    def release_buffer(self, buffer=None):
        """"""
        return object

    def reset_buffer(self, buffer=None):
        """"""
        return object

    def set_config(self, config=None):
        """"""
        return object

    def start(self):
        """"""
        return object

    def stop(self):
        """"""
        return object

    def acquire_buffer(self, buffer=None, params=None):
        """"""
        return object

    def get_config(self):
        """"""
        return object

    def get_options(self):
        """"""
        return object

    def has_option(self, option=None):
        """"""
        return object

    def is_active(self):
        """"""
        return object

    def release_buffer(self, buffer=None):
        """"""
        return object

    def set_active(self, active=None):
        """"""
        return object

    def set_config(self, config=None):
        """"""
        return object

    def set_flushing(self, flushing=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def flushing(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Bus(Object):
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    def message(self, message=None):
        """"""
        return object

    def sync_message(self, message=None):
        """"""
        return object

    def add_signal_watch(self):
        """"""
        return object

    def add_signal_watch_full(self, priority=None):
        """"""
        return object

    def add_watch(self, func=None, user_data=None):
        """"""
        return object

    def add_watch_full(self, priority=None, func=None, user_data=None, notify=None):
        """"""
        return object

    def async_signal_func(self, message=None, data=None):
        """"""
        return object

    def create_watch(self):
        """"""
        return object

    def disable_sync_message_emission(self):
        """"""
        return object

    def enable_sync_message_emission(self):
        """"""
        return object

    def get_pollfd(self, fd=None):
        """"""
        return object

    def have_pending(self):
        """"""
        return object

    def peek(self):
        """"""
        return object

    def poll(self, events=None, timeout=None):
        """"""
        return object

    def pop(self):
        """"""
        return object

    def pop_filtered(self, types=None):
        """"""
        return object

    def post(self, message=None):
        """"""
        return object

    def remove_signal_watch(self):
        """"""
        return object

    def remove_watch(self):
        """"""
        return object

    def set_flushing(self, flushing=None):
        """"""
        return object

    def set_sync_handler(self, func=None, user_data=None, notify=None):
        """"""
        return object

    def sync_signal_handler(self, message=None, data=None):
        """"""
        return object

    def timed_pop(self, timeout=None):
        """"""
        return object

    def timed_pop_filtered(self, timeout=None, types=None):
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


class Clock(Object):
    """"""
    @staticmethod
    def id_compare_func(id1=None, id2=None):
        """"""
        return object

    @staticmethod
    def id_get_time(id=None):
        """"""
        return object

    @staticmethod
    def id_ref(id=None):
        """"""
        return object

    @staticmethod
    def id_unref(id=None):
        """"""
        return object

    @staticmethod
    def id_unschedule(id=None):
        """"""
        return object

    @staticmethod
    def id_wait(id=None, jitter=None):
        """"""
        return object

    @staticmethod
    def id_wait_async(id=None, func=None, user_data=None, destroy_data=None):
        """"""
        return object

    def change_resolution(self, old_resolution=None, new_resolution=None):
        """"""
        return object

    def get_internal_time(self):
        """"""
        return object

    def get_resolution(self):
        """"""
        return object

    def unschedule(self, entry=None):
        """"""
        return object

    def wait(self, entry=None, jitter=None):
        """"""
        return object

    def wait_async(self, entry=None):
        """"""
        return object

    def add_observation(self, slave=None, master=None, r_squared=None):
        """"""
        return object

    def add_observation_unapplied(self, slave=None, master=None, r_squared=None, internal=None, external=None, rate_num=None, rate_denom=None):
        """"""
        return object

    def adjust_unlocked(self, internal=None):
        """"""
        return object

    def adjust_with_calibration(self, internal_target=None, cinternal=None, cexternal=None, cnum=None, cdenom=None):
        """"""
        return object

    def get_calibration(self, internal=None, external=None, rate_num=None, rate_denom=None):
        """"""
        return object

    def get_internal_time(self):
        """"""
        return object

    def get_master(self):
        """"""
        return object

    def get_resolution(self):
        """"""
        return object

    def get_time(self):
        """"""
        return object

    def get_timeout(self):
        """"""
        return object

    def is_synced(self):
        """"""
        return object

    def new_periodic_id(self, start_time=None, interval=None):
        """"""
        return object

    def new_single_shot_id(self, time=None):
        """"""
        return object

    def periodic_id_reinit(self, id=None, start_time=None, interval=None):
        """"""
        return object

    def set_calibration(self, internal=None, external=None, rate_num=None, rate_denom=None):
        """"""
        return object

    def set_master(self, master=None):
        """"""
        return object

    def set_resolution(self, resolution=None):
        """"""
        return object

    def set_synced(self, synced=None):
        """"""
        return object

    def set_timeout(self, timeout=None):
        """"""
        return object

    def single_shot_id_reinit(self, id=None, time=None):
        """"""
        return object

    def unadjust_unlocked(self, external=None):
        """"""
        return object

    def unadjust_with_calibration(self, external_target=None, cinternal=None, cexternal=None, cnum=None, cdenom=None):
        """"""
        return object

    def wait_for_sync(self, timeout=None):
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


class ControlBinding(Object):
    """"""

    def get_g_value_array(self, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    def get_value(self, timestamp=None):
        """"""
        return object

    def get_value_array(self, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    def sync_values(self, object=None, timestamp=None, last_sync=None):
        """"""
        return object

    def get_g_value_array(self, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    def get_value(self, timestamp=None):
        """"""
        return object

    def get_value_array(self, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    def is_disabled(self):
        """"""
        return object

    def set_disabled(self, disabled=None):
        """"""
        return object

    def sync_values(self, object=None, timestamp=None, last_sync=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def name(self):
        return object

    @property
    def pspec(self):
        return object

    @property
    def object(self):
        return object

    @property
    def disabled(self):
        return object


class ControlSource(Object):
    """"""

    def control_source_get_value(self, timestamp=None, value=None):
        """"""
        return object

    def control_source_get_value_array(self, timestamp=None, interval=None, n_values=None, values=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def get_value(self):
        return object

    @property
    def get_value_array(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Device(Object):
    """"""

    def create_element(self, name=None):
        """"""
        return object

    def reconfigure_element(self, element=None):
        """"""
        return object

    def create_element(self, name=None):
        """"""
        return object

    def get_caps(self):
        """"""
        return object

    def get_device_class(self):
        """"""
        return object

    def get_display_name(self):
        """"""
        return object

    def get_properties(self):
        """"""
        return object

    def has_classes(self, classes=None):
        """"""
        return object

    def has_classesv(self, classes=None):
        """"""
        return object

    def reconfigure_element(self, element=None):
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


class DeviceMonitor(Object):
    """"""

    def __init__(self):
        """"""
        return object

    @staticmethod
    def new():
        """"""
        return object

    def add_filter(self, classes=None, caps=None):
        """"""
        return object

    def get_bus(self):
        """"""
        return object

    def get_devices(self):
        """"""
        return object

    def get_providers(self):
        """"""
        return object

    def get_show_all_devices(self):
        """"""
        return object

    def remove_filter(self, filter_id=None):
        """"""
        return object

    def set_show_all_devices(self, show_all=None):
        """"""
        return object

    def start(self):
        """"""
        return object

    def stop(self):
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


class DeviceProvider(Object):
    """"""
    @staticmethod
    def register(plugin=None, name=None, rank=None, type=None):
        """"""
        return object

    def probe(self):
        """"""
        return object

    def start(self):
        """"""
        return object

    def stop(self):
        """"""
        return object

    def can_monitor(self):
        """"""
        return object

    def device_add(self, device=None):
        """"""
        return object

    def device_remove(self, device=None):
        """"""
        return object

    def get_bus(self):
        """"""
        return object

    def get_devices(self):
        """"""
        return object

    def get_factory(self):
        """"""
        return object

    def get_hidden_providers(self):
        """"""
        return object

    def get_metadata(self, key=None):
        """"""
        return object

    def hide_provider(self, name=None):
        """"""
        return object

    def start(self):
        """"""
        return object

    def stop(self):
        """"""
        return object

    def unhide_provider(self, name=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def devices(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DeviceProviderFactory(PluginFeature):
    """"""
    @staticmethod
    def find(name=None):
        """"""
        return object

    @staticmethod
    def get_by_name(factoryname=None):
        """"""
        return object

    @staticmethod
    def list_get_device_providers(minrank=None):
        """"""
        return object

    def get(self):
        """"""
        return object

    def get_device_provider_type(self):
        """"""
        return object

    def get_metadata(self, key=None):
        """"""
        return object

    def get_metadata_keys(self):
        """"""
        return object

    def has_classes(self, classes=None):
        """"""
        return object

    def has_classesv(self, classes=None):
        """"""
        return object


class DynamicTypeFactory(PluginFeature):
    """"""
    @staticmethod
    def load(factoryname=None):
        """"""
        return object


class Element(Object):
    """"""
    @staticmethod
    def make_from_uri(type=None, uri=None, elementname=None):
        """"""
        return object

    @staticmethod
    def register(plugin=None, name=None, rank=None, type=None):
        """"""
        return object

    @staticmethod
    def state_change_return_get_name(state_ret=None):
        """"""
        return object

    @staticmethod
    def state_get_name(state=None):
        """"""
        return object

    def change_state(self, transition=None):
        """"""
        return object

    def get_state(self, state=None, pending=None, timeout=None):
        """"""
        return object

    def no_more_pads(self):
        """"""
        return object

    def pad_added(self, pad=None):
        """"""
        return object

    def pad_removed(self, pad=None):
        """"""
        return object

    def post_message(self, message=None):
        """"""
        return object

    def provide_clock(self):
        """"""
        return object

    def query(self, query=None):
        """"""
        return object

    def release_pad(self, pad=None):
        """"""
        return object

    def request_new_pad(self, templ=None, name=None, caps=None):
        """"""
        return object

    def send_event(self, event=None):
        """"""
        return object

    def set_bus(self, bus=None):
        """"""
        return object

    def set_clock(self, clock=None):
        """"""
        return object

    def set_context(self, context=None):
        """"""
        return object

    def set_state(self, state=None):
        """"""
        return object

    def state_changed(self, oldstate=None, newstate=None, pending=None):
        """"""
        return object

    def abort_state(self):
        """"""
        return object

    def add_pad(self, pad=None):
        """"""
        return object

    def add_property_deep_notify_watch(self, property_name=None, include_value=None):
        """"""
        return object

    def add_property_notify_watch(self, property_name=None, include_value=None):
        """"""
        return object

    def call_async(self, func=None, user_data=None, destroy_notify=None):
        """"""
        return object

    def change_state(self, transition=None):
        """"""
        return object

    def continue_state(self, ret=None):
        """"""
        return object

    def create_all_pads(self):
        """"""
        return object

    def foreach_pad(self, func=None, user_data=None):
        """"""
        return object

    def foreach_sink_pad(self, func=None, user_data=None):
        """"""
        return object

    def foreach_src_pad(self, func=None, user_data=None):
        """"""
        return object

    def get_base_time(self):
        """"""
        return object

    def get_bus(self):
        """"""
        return object

    def get_clock(self):
        """"""
        return object

    def get_compatible_pad(self, pad=None, caps=None):
        """"""
        return object

    def get_compatible_pad_template(self, compattempl=None):
        """"""
        return object

    def get_context(self, context_type=None):
        """"""
        return object

    def get_context_unlocked(self, context_type=None):
        """"""
        return object

    def get_contexts(self):
        """"""
        return object

    def get_factory(self):
        """"""
        return object

    def get_metadata(self, key=None):
        """"""
        return object

    def get_pad_template(self, name=None):
        """"""
        return object

    def get_pad_template_list(self):
        """"""
        return object

    def get_request_pad(self, name=None):
        """"""
        return object

    def get_start_time(self):
        """"""
        return object

    def get_state(self, state=None, pending=None, timeout=None):
        """"""
        return object

    def get_static_pad(self, name=None) -> Pad:
        """"""
        return object

    def is_locked_state(self):
        """"""
        return object

    def iterate_pads(self):
        """"""
        return object

    def iterate_sink_pads(self):
        """"""
        return object

    def iterate_src_pads(self):
        """"""
        return object

    def link(self, dest=None):
        """"""
        return object

    def link_filtered(self, dest=None, filter=None):
        """"""
        return object

    def link_many(self, element_2=None, *args):
        """"""
        return object

    def link_pads(self, srcpadname=None, dest=None, destpadname=None):
        """"""
        return object

    def link_pads_filtered(self, srcpadname=None, dest=None, destpadname=None, filter=None):
        """"""
        return object

    def link_pads_full(self, srcpadname=None, dest=None, destpadname=None, flags=None):
        """"""
        return object

    def lost_state(self):
        """"""
        return object

    def message_full(self, type=None, domain=None, code=None, text=None, debug=None, file=None, function=None, line=None):
        """"""
        return object

    def message_full_with_details(self, type=None, domain=None, code=None, text=None, debug=None, file=None, function=None, line=None, structure=None):
        """"""
        return object

    def no_more_pads(self):
        """"""
        return object

    def post_message(self, message=None):
        """"""
        return object

    def provide_clock(self):
        """"""
        return object

    def query(self, query=None):
        """"""
        return object

    def query_convert(self, src_format=None, src_val=None, dest_format=None, dest_val=None):
        """"""
        return object

    def query_duration(self, format=None, duration=None):
        """"""
        return object

    def query_position(self, format=None, cur=None):
        """"""
        return object

    def release_request_pad(self, pad=None):
        """"""
        return object

    def remove_pad(self, pad=None):
        """"""
        return object

    def remove_property_notify_watch(self, watch_id=None):
        """"""
        return object

    def request_pad(self, templ=None, name=None, caps=None):
        """"""
        return object

    def seek(self, rate=None, format=None, flags=None, start_type=None, start=None, stop_type=None, stop=None):
        """"""
        return object

    def seek_simple(self, format=None, seek_flags=None, seek_pos=None):
        """"""
        return object

    def send_event(self, event=None):
        """"""
        return object

    def set_base_time(self, time=None):
        """"""
        return object

    def set_bus(self, bus=None):
        """"""
        return object

    def set_clock(self, clock=None):
        """"""
        return object

    def set_context(self, context=None):
        """"""
        return object

    def set_locked_state(self, locked_state=None):
        """"""
        return object

    def set_start_time(self, time=None):
        """"""
        return object

    def set_state(self, state=None):
        """"""
        return object

    def sync_state_with_parent(self):
        """"""
        return object

    def unlink(self, dest=None):
        """"""
        return object

    def unlink_many(self, element_2=None, *args):
        """"""
        return object

    def unlink_pads(self, srcpadname=None, dest=None, destpadname=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def state_lock(self):
        return object

    @property
    def state_cond(self):
        return object

    @property
    def state_cookie(self):
        return object

    @property
    def target_state(self):
        return object

    @property
    def current_state(self):
        return object

    @property
    def next_state(self):
        return object

    @property
    def pending_state(self):
        return object

    @property
    def last_return(self):
        return object

    @property
    def bus(self):
        return object

    @property
    def clock(self):
        return object

    @property
    def base_time(self):
        return object

    @property
    def start_time(self):
        return object

    @property
    def numpads(self):
        return object

    @property
    def pads(self):
        return object

    @property
    def numsrcpads(self):
        return object

    @property
    def srcpads(self):
        return object

    @property
    def numsinkpads(self):
        return object

    @property
    def sinkpads(self):
        return object

    @property
    def pads_cookie(self):
        return object

    @property
    def contexts(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ElementFactory(PluginFeature):
    """"""
    @staticmethod
    def find(name=None):
        """"""
        return object

    @staticmethod
    def list_filter(list=None, caps=None, direction=None, subsetonly=None):
        """"""
        return object

    @staticmethod
    def list_get_elements(type=None, minrank=None):
        """"""
        return object

    @staticmethod
    def make(factoryname=None, name=None) -> Element:
        """"""
        return object

    def can_sink_all_caps(self, caps=None):
        """"""
        return object

    def can_sink_any_caps(self, caps=None):
        """"""
        return object

    def can_src_all_caps(self, caps=None):
        """"""
        return object

    def can_src_any_caps(self, caps=None):
        """"""
        return object

    def create(self, name=None):
        """"""
        return object

    def get_element_type(self):
        """"""
        return object

    def get_metadata(self, key=None):
        """"""
        return object

    def get_metadata_keys(self):
        """"""
        return object

    def get_num_pad_templates(self):
        """"""
        return object

    def get_static_pad_templates(self):
        """"""
        return object

    def get_uri_protocols(self):
        """"""
        return object

    def get_uri_type(self):
        """"""
        return object

    def has_interface(self, interfacename=None):
        """"""
        return object

    def list_is_type(self, type=None):
        """"""
        return object


class GhostPad(ProxyPad):
    """"""

    def __init__(self, name=None, target=None):
        """"""
        return object

    @staticmethod
    def new(name=None, target=None):
        """"""
        return object

    @staticmethod
    def new_from_template(name=None, target=None, templ=None):
        """"""
        return object

    @staticmethod
    def new_no_target(name=None, dir=None):
        """"""
        return object

    @staticmethod
    def new_no_target_from_template(name=None, templ=None):
        """"""
        return object

    @staticmethod
    def activate_mode_default(pad=None, parent=None, mode=None, active=None):
        """"""
        return object

    @staticmethod
    def internal_activate_mode_default(pad=None, parent=None, mode=None, active=None):
        """"""
        return object

    def construct(self):
        """"""
        return object

    def get_target(self):
        """"""
        return object

    def set_target(self, newtarget=None):
        """"""
        return object

    @property
    def pad(self):
        return object

    @property
    def priv(self):
        return object


class SystemClock(Clock):
    """"""
    @staticmethod
    def obtain():
        """"""
        return object

    @staticmethod
    def set_default(new_clock=None):
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


class Bin(Element, ChildProxy):
    """"""

    def __init__(self, name=None):
        """"""
        return object

    @staticmethod
    def new(name=None):
        """"""
        return object

    def add_element(self, element=None):
        """"""
        return object

    def deep_element_added(self, sub_bin=None, child=None):
        """"""
        return object

    def deep_element_removed(self, sub_bin=None, child=None):
        """"""
        return object

    def do_latency(self):
        """"""
        return object

    def element_added(self, child=None):
        """"""
        return object

    def element_removed(self, child=None):
        """"""
        return object

    def handle_message(self, message=None):
        """"""
        return object

    def remove_element(self, element=None):
        """"""
        return object

    def add(self, element=None):
        """"""
        return object

    def add_many(self, element_1=None, *args):
        """"""
        return object

    def find_unlinked_pad(self, direction=None):
        """"""
        return object

    def get_by_interface(self, iface=None):
        """"""
        return object

    def get_by_name(self, name=None):
        """"""
        return object

    def get_by_name_recurse_up(self, name=None):
        """"""
        return object

    def get_suppressed_flags(self):
        """"""
        return object

    def iterate_all_by_interface(self, iface=None):
        """"""
        return object

    def iterate_elements(self):
        """"""
        return object

    def iterate_recurse(self):
        """"""
        return object

    def iterate_sinks(self):
        """"""
        return object

    def iterate_sorted(self):
        """"""
        return object

    def iterate_sources(self):
        """"""
        return object

    def recalculate_latency(self):
        """"""
        return object

    def remove(self, element=None):
        """"""
        return object

    def remove_many(self, element_1=None, *args):
        """"""
        return object

    def set_suppressed_flags(self, flags=None):
        """"""
        return object

    def sync_children_states(self):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def numchildren(self):
        return object

    @property
    def children(self):
        return object

    @property
    def children_cookie(self):
        return object

    @property
    def child_bus(self):
        return object

    @property
    def messages(self):
        return object

    @property
    def polling(self):
        return object

    @property
    def state_dirty(self):
        return object

    @property
    def clock_dirty(self):
        return object

    @property
    def provided_clock(self):
        return object

    @property
    def clock_provider(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Pipeline(Bin, ChildProxy):
    """"""

    def __init__(self, name=None):
        """"""
        return object

    @staticmethod
    def new(name=None) -> 'Pipeline':
        """"""
        return object

    def auto_clock(self):
        """"""
        return object

    def get_auto_flush_bus(self):
        """"""
        return object

    def get_bus(self):
        """"""
        return object

    def get_clock(self):
        """"""
        return object

    def get_delay(self):
        """"""
        return object

    def get_latency(self):
        """"""
        return object

    def get_pipeline_clock(self):
        """"""
        return object

    def set_auto_flush_bus(self, auto_flush=None):
        """"""
        return object

    def set_clock(self, clock=None):
        """"""
        return object

    def set_delay(self, delay=None):
        """"""
        return object

    def set_latency(self, latency=None):
        """"""
        return object

    def use_clock(self, clock=None):
        """"""
        return object

    @property
    def bin(self):
        return object

    @property
    def fixed_clock(self):
        return object

    @property
    def stream_time(self):
        return object

    @property
    def delay(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object
