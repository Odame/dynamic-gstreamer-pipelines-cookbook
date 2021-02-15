# -*- coding: utf-8 -*-
from gi.repository import GObject


class AppInfoCreateFlags:
    """"""
    NONE = 0
    NEEDS_TERMINAL = 1
    SUPPORTS_URIS = 2
    SUPPORTS_STARTUP_NOTIFICATION = 4


class ApplicationFlags:
    """"""
    FLAGS_NONE = 0
    IS_SERVICE = 1
    IS_LAUNCHER = 2
    HANDLES_OPEN = 4
    HANDLES_COMMAND_LINE = 8
    SEND_ENVIRONMENT = 16
    NON_UNIQUE = 32
    CAN_OVERRIDE_APP_ID = 64


class AskPasswordFlags:
    """"""
    NEED_PASSWORD = 1
    NEED_USERNAME = 2
    NEED_DOMAIN = 4
    SAVING_SUPPORTED = 8
    ANONYMOUS_SUPPORTED = 16


class BusNameOwnerFlags:
    """"""
    NONE = 0
    ALLOW_REPLACEMENT = 1
    REPLACE = 2
    DO_NOT_QUEUE = 4


class BusNameWatcherFlags:
    """"""
    NONE = 0
    AUTO_START = 1


class BusType:
    """"""
    STARTER = -1
    NONE = 0
    SYSTEM = 1
    SESSION = 2


class ConverterFlags:
    """"""
    NONE = 0
    INPUT_AT_END = 1
    FLUSH = 2


class ConverterResult:
    """"""
    ERROR = 0
    CONVERTED = 1
    FINISHED = 2
    FLUSHED = 3


class CredentialsType:
    """"""
    INVALID = 0
    LINUX_UCRED = 1
    FREEBSD_CMSGCRED = 2
    OPENBSD_SOCKPEERCRED = 3
    SOLARIS_UCRED = 4
    NETBSD_UNPCBID = 5


class DBusCallFlags:
    """"""
    NONE = 0
    NO_AUTO_START = 1
    ALLOW_INTERACTIVE_AUTHORIZATION = 2


class DBusCapabilityFlags:
    """"""
    NONE = 0
    UNIX_FD_PASSING = 1


class DBusConnectionFlags:
    """"""
    NONE = 0
    AUTHENTICATION_CLIENT = 1
    AUTHENTICATION_SERVER = 2
    AUTHENTICATION_ALLOW_ANONYMOUS = 4
    MESSAGE_BUS_CONNECTION = 8
    DELAY_MESSAGE_PROCESSING = 16


class DBusError:
    """"""
    FAILED = 0
    NO_MEMORY = 1
    SERVICE_UNKNOWN = 2
    NAME_HAS_NO_OWNER = 3
    NO_REPLY = 4
    IO_ERROR = 5
    BAD_ADDRESS = 6
    NOT_SUPPORTED = 7
    LIMITS_EXCEEDED = 8
    ACCESS_DENIED = 9
    AUTH_FAILED = 10
    NO_SERVER = 11
    TIMEOUT = 12
    NO_NETWORK = 13
    ADDRESS_IN_USE = 14
    DISCONNECTED = 15
    INVALID_ARGS = 16
    FILE_NOT_FOUND = 17
    FILE_EXISTS = 18
    UNKNOWN_METHOD = 19
    TIMED_OUT = 20
    MATCH_RULE_NOT_FOUND = 21
    MATCH_RULE_INVALID = 22
    SPAWN_EXEC_FAILED = 23
    SPAWN_FORK_FAILED = 24
    SPAWN_CHILD_EXITED = 25
    SPAWN_CHILD_SIGNALED = 26
    SPAWN_FAILED = 27
    SPAWN_SETUP_FAILED = 28
    SPAWN_CONFIG_INVALID = 29
    SPAWN_SERVICE_INVALID = 30
    SPAWN_SERVICE_NOT_FOUND = 31
    SPAWN_PERMISSIONS_INVALID = 32
    SPAWN_FILE_INVALID = 33
    SPAWN_NO_MEMORY = 34
    UNIX_PROCESS_ID_UNKNOWN = 35
    INVALID_SIGNATURE = 36
    INVALID_FILE_CONTENT = 37
    SELINUX_SECURITY_CONTEXT_UNKNOWN = 38
    ADT_AUDIT_DATA_UNKNOWN = 39
    OBJECT_PATH_IN_USE = 40
    UNKNOWN_OBJECT = 41
    UNKNOWN_INTERFACE = 42
    UNKNOWN_PROPERTY = 43
    PROPERTY_READ_ONLY = 44


class DBusInterfaceSkeletonFlags:
    """"""
    NONE = 0
    HANDLE_METHOD_INVOCATIONS_IN_THREAD = 1


class DBusMessageByteOrder:
    """"""
    BIG_ENDIAN = 66
    LITTLE_ENDIAN = 108


class DBusMessageFlags:
    """"""
    NONE = 0
    NO_REPLY_EXPECTED = 1
    NO_AUTO_START = 2
    ALLOW_INTERACTIVE_AUTHORIZATION = 4


class DBusMessageHeaderField:
    """"""
    INVALID = 0
    PATH = 1
    INTERFACE = 2
    MEMBER = 3
    ERROR_NAME = 4
    REPLY_SERIAL = 5
    DESTINATION = 6
    SENDER = 7
    SIGNATURE = 8
    NUM_UNIX_FDS = 9


class DBusMessageType:
    """"""
    INVALID = 0
    METHOD_CALL = 1
    METHOD_RETURN = 2
    ERROR = 3
    SIGNAL = 4


class DBusObjectManagerClientFlags:
    """"""
    NONE = 0
    DO_NOT_AUTO_START = 1


class DBusPropertyInfoFlags:
    """"""
    NONE = 0
    READABLE = 1
    WRITABLE = 2


class DBusProxyFlags:
    """"""
    NONE = 0
    DO_NOT_LOAD_PROPERTIES = 1
    DO_NOT_CONNECT_SIGNALS = 2
    DO_NOT_AUTO_START = 4
    GET_INVALIDATED_PROPERTIES = 8
    DO_NOT_AUTO_START_AT_CONSTRUCTION = 16


class DBusSendMessageFlags:
    """"""
    NONE = 0
    PRESERVE_SERIAL = 1


class DBusServerFlags:
    """"""
    NONE = 0
    RUN_IN_THREAD = 1
    AUTHENTICATION_ALLOW_ANONYMOUS = 2


class DBusSignalFlags:
    """"""
    NONE = 0
    NO_MATCH_RULE = 1
    MATCH_ARG0_NAMESPACE = 2
    MATCH_ARG0_PATH = 4


class DBusSubtreeFlags:
    """"""
    NONE = 0
    DISPATCH_TO_UNENUMERATED_NODES = 1
DESKTOP_APP_INFO_LOOKUP_EXTENSION_POINT_NAME = r"""gio-desktop-app-info-lookup"""


class DataStreamByteOrder:
    """"""
    BIG_ENDIAN = 0
    LITTLE_ENDIAN = 1
    HOST_ENDIAN = 2


class DataStreamNewlineType:
    """"""
    LF = 0
    CR = 1
    CR_LF = 2
    ANY = 3


class DriveStartFlags:
    """"""
    NONE = 0


class DriveStartStopType:
    """"""
    UNKNOWN = 0
    SHUTDOWN = 1
    NETWORK = 2
    MULTIDISK = 3
    PASSWORD = 4


class EmblemOrigin:
    """"""
    UNKNOWN = 0
    DEVICE = 1
    LIVEMETADATA = 2
    TAG = 3
FILE_ATTRIBUTE_ACCESS_CAN_DELETE = r"""access::can-delete"""
FILE_ATTRIBUTE_ACCESS_CAN_EXECUTE = r"""access::can-execute"""
FILE_ATTRIBUTE_ACCESS_CAN_READ = r"""access::can-read"""
FILE_ATTRIBUTE_ACCESS_CAN_RENAME = r"""access::can-rename"""
FILE_ATTRIBUTE_ACCESS_CAN_TRASH = r"""access::can-trash"""
FILE_ATTRIBUTE_ACCESS_CAN_WRITE = r"""access::can-write"""
FILE_ATTRIBUTE_DOS_IS_ARCHIVE = r"""dos::is-archive"""
FILE_ATTRIBUTE_DOS_IS_SYSTEM = r"""dos::is-system"""
FILE_ATTRIBUTE_ETAG_VALUE = r"""etag::value"""
FILE_ATTRIBUTE_FILESYSTEM_FREE = r"""filesystem::free"""
FILE_ATTRIBUTE_FILESYSTEM_READONLY = r"""filesystem::readonly"""
FILE_ATTRIBUTE_FILESYSTEM_REMOTE = r"""filesystem::remote"""
FILE_ATTRIBUTE_FILESYSTEM_SIZE = r"""filesystem::size"""
FILE_ATTRIBUTE_FILESYSTEM_TYPE = r"""filesystem::type"""
FILE_ATTRIBUTE_FILESYSTEM_USED = r"""filesystem::used"""
FILE_ATTRIBUTE_FILESYSTEM_USE_PREVIEW = r"""filesystem::use-preview"""
FILE_ATTRIBUTE_GVFS_BACKEND = r"""gvfs::backend"""
FILE_ATTRIBUTE_ID_FILE = r"""id::file"""
FILE_ATTRIBUTE_ID_FILESYSTEM = r"""id::filesystem"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_EJECT = r"""mountable::can-eject"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_MOUNT = r"""mountable::can-mount"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_POLL = r"""mountable::can-poll"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_START = r"""mountable::can-start"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_START_DEGRADED = r"""mountable::can-start-degraded"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_STOP = r"""mountable::can-stop"""
FILE_ATTRIBUTE_MOUNTABLE_CAN_UNMOUNT = r"""mountable::can-unmount"""
FILE_ATTRIBUTE_MOUNTABLE_HAL_UDI = r"""mountable::hal-udi"""
FILE_ATTRIBUTE_MOUNTABLE_IS_MEDIA_CHECK_AUTOMATIC = r"""mountable::is-media-check-automatic"""
FILE_ATTRIBUTE_MOUNTABLE_START_STOP_TYPE = r"""mountable::start-stop-type"""
FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE = r"""mountable::unix-device"""
FILE_ATTRIBUTE_MOUNTABLE_UNIX_DEVICE_FILE = r"""mountable::unix-device-file"""
FILE_ATTRIBUTE_OWNER_GROUP = r"""owner::group"""
FILE_ATTRIBUTE_OWNER_USER = r"""owner::user"""
FILE_ATTRIBUTE_OWNER_USER_REAL = r"""owner::user-real"""
FILE_ATTRIBUTE_PREVIEW_ICON = r"""preview::icon"""
FILE_ATTRIBUTE_RECENT_MODIFIED = r"""recent::modified"""
FILE_ATTRIBUTE_SELINUX_CONTEXT = r"""selinux::context"""
FILE_ATTRIBUTE_STANDARD_ALLOCATED_SIZE = r"""standard::allocated-size"""
FILE_ATTRIBUTE_STANDARD_CONTENT_TYPE = r"""standard::content-type"""
FILE_ATTRIBUTE_STANDARD_COPY_NAME = r"""standard::copy-name"""
FILE_ATTRIBUTE_STANDARD_DESCRIPTION = r"""standard::description"""
FILE_ATTRIBUTE_STANDARD_DISPLAY_NAME = r"""standard::display-name"""
FILE_ATTRIBUTE_STANDARD_EDIT_NAME = r"""standard::edit-name"""
FILE_ATTRIBUTE_STANDARD_FAST_CONTENT_TYPE = r"""standard::fast-content-type"""
FILE_ATTRIBUTE_STANDARD_ICON = r"""standard::icon"""
FILE_ATTRIBUTE_STANDARD_IS_BACKUP = r"""standard::is-backup"""
FILE_ATTRIBUTE_STANDARD_IS_HIDDEN = r"""standard::is-hidden"""
FILE_ATTRIBUTE_STANDARD_IS_SYMLINK = r"""standard::is-symlink"""
FILE_ATTRIBUTE_STANDARD_IS_VIRTUAL = r"""standard::is-virtual"""
FILE_ATTRIBUTE_STANDARD_IS_VOLATILE = r"""standard::is-volatile"""
FILE_ATTRIBUTE_STANDARD_NAME = r"""standard::name"""
FILE_ATTRIBUTE_STANDARD_SIZE = r"""standard::size"""
FILE_ATTRIBUTE_STANDARD_SORT_ORDER = r"""standard::sort-order"""
FILE_ATTRIBUTE_STANDARD_SYMBOLIC_ICON = r"""standard::symbolic-icon"""
FILE_ATTRIBUTE_STANDARD_SYMLINK_TARGET = r"""standard::symlink-target"""
FILE_ATTRIBUTE_STANDARD_TARGET_URI = r"""standard::target-uri"""
FILE_ATTRIBUTE_STANDARD_TYPE = r"""standard::type"""
FILE_ATTRIBUTE_THUMBNAILING_FAILED = r"""thumbnail::failed"""
FILE_ATTRIBUTE_THUMBNAIL_IS_VALID = r"""thumbnail::is-valid"""
FILE_ATTRIBUTE_THUMBNAIL_PATH = r"""thumbnail::path"""
FILE_ATTRIBUTE_TIME_ACCESS = r"""time::access"""
FILE_ATTRIBUTE_TIME_ACCESS_USEC = r"""time::access-usec"""
FILE_ATTRIBUTE_TIME_CHANGED = r"""time::changed"""
FILE_ATTRIBUTE_TIME_CHANGED_USEC = r"""time::changed-usec"""
FILE_ATTRIBUTE_TIME_CREATED = r"""time::created"""
FILE_ATTRIBUTE_TIME_CREATED_USEC = r"""time::created-usec"""
FILE_ATTRIBUTE_TIME_MODIFIED = r"""time::modified"""
FILE_ATTRIBUTE_TIME_MODIFIED_USEC = r"""time::modified-usec"""
FILE_ATTRIBUTE_TRASH_DELETION_DATE = r"""trash::deletion-date"""
FILE_ATTRIBUTE_TRASH_ITEM_COUNT = r"""trash::item-count"""
FILE_ATTRIBUTE_TRASH_ORIG_PATH = r"""trash::orig-path"""
FILE_ATTRIBUTE_UNIX_BLOCKS = r"""unix::blocks"""
FILE_ATTRIBUTE_UNIX_BLOCK_SIZE = r"""unix::block-size"""
FILE_ATTRIBUTE_UNIX_DEVICE = r"""unix::device"""
FILE_ATTRIBUTE_UNIX_GID = r"""unix::gid"""
FILE_ATTRIBUTE_UNIX_INODE = r"""unix::inode"""
FILE_ATTRIBUTE_UNIX_IS_MOUNTPOINT = r"""unix::is-mountpoint"""
FILE_ATTRIBUTE_UNIX_MODE = r"""unix::mode"""
FILE_ATTRIBUTE_UNIX_NLINK = r"""unix::nlink"""
FILE_ATTRIBUTE_UNIX_RDEV = r"""unix::rdev"""
FILE_ATTRIBUTE_UNIX_UID = r"""unix::uid"""


class FileAttributeInfoFlags:
    """"""
    NONE = 0
    COPY_WITH_FILE = 1
    COPY_WHEN_MOVED = 2


class FileAttributeStatus:
    """"""
    UNSET = 0
    SET = 1
    ERROR_SETTING = 2


class FileAttributeType:
    """"""
    INVALID = 0
    STRING = 1
    BYTE_STRING = 2
    BOOLEAN = 3
    UINT32 = 4
    INT32 = 5
    UINT64 = 6
    INT64 = 7
    OBJECT = 8
    STRINGV = 9


class FileCopyFlags:
    """"""
    NONE = 0
    OVERWRITE = 1
    BACKUP = 2
    NOFOLLOW_SYMLINKS = 4
    ALL_METADATA = 8
    NO_FALLBACK_FOR_MOVE = 16
    TARGET_DEFAULT_PERMS = 32


class FileCreateFlags:
    """"""
    NONE = 0
    PRIVATE = 1
    REPLACE_DESTINATION = 2


class FileMeasureFlags:
    """"""
    NONE = 0
    REPORT_ANY_ERROR = 2
    APPARENT_SIZE = 4
    NO_XDEV = 8


class FileMonitorEvent:
    """"""
    CHANGED = 0
    CHANGES_DONE_HINT = 1
    DELETED = 2
    CREATED = 3
    ATTRIBUTE_CHANGED = 4
    PRE_UNMOUNT = 5
    UNMOUNTED = 6
    MOVED = 7
    RENAMED = 8
    MOVED_IN = 9
    MOVED_OUT = 10


class FileMonitorFlags:
    """"""
    NONE = 0
    WATCH_MOUNTS = 1
    SEND_MOVED = 2
    WATCH_HARD_LINKS = 4
    WATCH_MOVES = 8


class FileQueryInfoFlags:
    """"""
    NONE = 0
    NOFOLLOW_SYMLINKS = 1


class FileType:
    """"""
    UNKNOWN = 0
    REGULAR = 1
    DIRECTORY = 2
    SYMBOLIC_LINK = 3
    SPECIAL = 4
    SHORTCUT = 5
    MOUNTABLE = 6


class FilesystemPreviewType:
    """"""
    IF_ALWAYS = 0
    IF_LOCAL = 1
    NEVER = 2


class IOErrorEnum:
    """"""
    FAILED = 0
    NOT_FOUND = 1
    EXISTS = 2
    IS_DIRECTORY = 3
    NOT_DIRECTORY = 4
    NOT_EMPTY = 5
    NOT_REGULAR_FILE = 6
    NOT_SYMBOLIC_LINK = 7
    NOT_MOUNTABLE_FILE = 8
    FILENAME_TOO_LONG = 9
    INVALID_FILENAME = 10
    TOO_MANY_LINKS = 11
    NO_SPACE = 12
    INVALID_ARGUMENT = 13
    PERMISSION_DENIED = 14
    NOT_SUPPORTED = 15
    NOT_MOUNTED = 16
    ALREADY_MOUNTED = 17
    CLOSED = 18
    CANCELLED = 19
    PENDING = 20
    READ_ONLY = 21
    CANT_CREATE_BACKUP = 22
    WRONG_ETAG = 23
    TIMED_OUT = 24
    WOULD_RECURSE = 25
    BUSY = 26
    WOULD_BLOCK = 27
    HOST_NOT_FOUND = 28
    WOULD_MERGE = 29
    FAILED_HANDLED = 30
    TOO_MANY_OPEN_FILES = 31
    NOT_INITIALIZED = 32
    ADDRESS_IN_USE = 33
    PARTIAL_INPUT = 34
    INVALID_DATA = 35
    DBUS_ERROR = 36
    HOST_UNREACHABLE = 37
    NETWORK_UNREACHABLE = 38
    CONNECTION_REFUSED = 39
    PROXY_FAILED = 40
    PROXY_AUTH_FAILED = 41
    PROXY_NEED_AUTH = 42
    PROXY_NOT_ALLOWED = 43
    BROKEN_PIPE = 44
    CONNECTION_CLOSED = 44
    NOT_CONNECTED = 45
    MESSAGE_TOO_LARGE = 46


class IOModuleScopeFlags:
    """"""
    NONE = 0
    BLOCK_DUPLICATES = 1


class IOStreamSpliceFlags:
    """"""
    NONE = 0
    CLOSE_STREAM1 = 1
    CLOSE_STREAM2 = 2
    WAIT_FOR_BOTH = 4
MENU_ATTRIBUTE_ACTION = r"""action"""
MENU_ATTRIBUTE_ACTION_NAMESPACE = r"""action-namespace"""
MENU_ATTRIBUTE_ICON = r"""icon"""
MENU_ATTRIBUTE_LABEL = r"""label"""
MENU_ATTRIBUTE_TARGET = r"""target"""
MENU_LINK_SECTION = r"""section"""
MENU_LINK_SUBMENU = r"""submenu"""


class MountMountFlags:
    """"""
    NONE = 0


class MountOperationResult:
    """"""
    HANDLED = 0
    ABORTED = 1
    UNHANDLED = 2


class MountUnmountFlags:
    """"""
    NONE = 0
    FORCE = 1
NATIVE_VOLUME_MONITOR_EXTENSION_POINT_NAME = r"""gio-native-volume-monitor"""
NETWORK_MONITOR_EXTENSION_POINT_NAME = r"""gio-network-monitor"""


class NetworkConnectivity:
    """"""
    LOCAL = 1
    LIMITED = 2
    PORTAL = 3
    FULL = 4


class NotificationPriority:
    """"""
    NORMAL = 0
    LOW = 1
    HIGH = 2
    URGENT = 3


class OutputStreamSpliceFlags:
    """"""
    NONE = 0
    CLOSE_SOURCE = 1
    CLOSE_TARGET = 2
PROXY_EXTENSION_POINT_NAME = r"""gio-proxy"""
PROXY_RESOLVER_EXTENSION_POINT_NAME = r"""gio-proxy-resolver"""


class PasswordSave:
    """"""
    NEVER = 0
    FOR_SESSION = 1
    PERMANENTLY = 2


class ResolverError:
    """"""
    NOT_FOUND = 0
    TEMPORARY_FAILURE = 1
    INTERNAL = 2


class ResolverRecordType:
    """"""
    SRV = 1
    MX = 2
    TXT = 3
    SOA = 4
    NS = 5


class ResourceError:
    """"""
    NOT_FOUND = 0
    INTERNAL = 1


class ResourceFlags:
    """"""
    NONE = 0
    COMPRESSED = 1


class ResourceLookupFlags:
    """"""
    NONE = 0
SETTINGS_BACKEND_EXTENSION_POINT_NAME = r"""gsettings-backend"""


class SettingsBindFlags:
    """"""
    DEFAULT = 0
    GET = 1
    SET = 2
    NO_SENSITIVITY = 4
    GET_NO_CHANGES = 8
    INVERT_BOOLEAN = 16


class SocketClientEvent:
    """"""
    RESOLVING = 0
    RESOLVED = 1
    CONNECTING = 2
    CONNECTED = 3
    PROXY_NEGOTIATING = 4
    PROXY_NEGOTIATED = 5
    TLS_HANDSHAKING = 6
    TLS_HANDSHAKED = 7
    COMPLETE = 8


class SocketFamily:
    """"""
    INVALID = 0
    UNIX = 1
    IPV4 = 2
    IPV6 = 10


class SocketListenerEvent:
    """"""
    BINDING = 0
    BOUND = 1
    LISTENING = 2
    LISTENED = 3


class SocketMsgFlags:
    """"""
    NONE = 0
    OOB = 1
    PEEK = 2
    DONTROUTE = 4


class SocketProtocol:
    """"""
    UNKNOWN = -1
    DEFAULT = 0
    TCP = 6
    UDP = 17
    SCTP = 132


class SocketType:
    """"""
    INVALID = 0
    STREAM = 1
    DATAGRAM = 2
    SEQPACKET = 3


class SubprocessFlags:
    """"""
    NONE = 0
    STDIN_PIPE = 1
    STDIN_INHERIT = 2
    STDOUT_PIPE = 4
    STDOUT_SILENCE = 8
    STDERR_PIPE = 16
    STDERR_SILENCE = 32
    STDERR_MERGE = 64
    INHERIT_FDS = 128
TLS_BACKEND_EXTENSION_POINT_NAME = r"""gio-tls-backend"""
TLS_DATABASE_PURPOSE_AUTHENTICATE_CLIENT = r"""1.3.6.1.5.5.7.3.2"""
TLS_DATABASE_PURPOSE_AUTHENTICATE_SERVER = r"""1.3.6.1.5.5.7.3.1"""


class TestDBusFlags:
    """"""
    NONE = 0


class TlsAuthenticationMode:
    """"""
    NONE = 0
    REQUESTED = 1
    REQUIRED = 2


class TlsCertificateFlags:
    """"""
    UNKNOWN_CA = 1
    BAD_IDENTITY = 2
    NOT_ACTIVATED = 4
    EXPIRED = 8
    REVOKED = 16
    INSECURE = 32
    GENERIC_ERROR = 64
    VALIDATE_ALL = 127


class TlsCertificateRequestFlags:
    """"""
    NONE = 0


class TlsDatabaseLookupFlags:
    """"""
    NONE = 0
    KEYPAIR = 1


class TlsDatabaseVerifyFlags:
    """"""
    NONE = 0


class TlsError:
    """"""
    UNAVAILABLE = 0
    MISC = 1
    BAD_CERTIFICATE = 2
    NOT_TLS = 3
    HANDSHAKE = 4
    CERTIFICATE_REQUIRED = 5
    EOF = 6


class TlsInteractionResult:
    """"""
    UNHANDLED = 0
    HANDLED = 1
    FAILED = 2


class TlsPasswordFlags:
    """"""
    NONE = 0
    RETRY = 2
    MANY_TRIES = 4
    FINAL_TRY = 8


class TlsRehandshakeMode:
    """"""
    NEVER = 0
    SAFELY = 1
    UNSAFELY = 2


class UnixSocketAddressType:
    """"""
    INVALID = 0
    ANONYMOUS = 1
    PATH = 2
    ABSTRACT = 3
    ABSTRACT_PADDED = 4
VFS_EXTENSION_POINT_NAME = r"""gio-vfs"""
VOLUME_IDENTIFIER_KIND_CLASS = r"""class"""
VOLUME_IDENTIFIER_KIND_HAL_UDI = r"""hal-udi"""
VOLUME_IDENTIFIER_KIND_LABEL = r"""label"""
VOLUME_IDENTIFIER_KIND_NFS_MOUNT = r"""nfs-mount"""
VOLUME_IDENTIFIER_KIND_UNIX_DEVICE = r"""unix-device"""
VOLUME_IDENTIFIER_KIND_UUID = r"""uuid"""
VOLUME_MONITOR_EXTENSION_POINT_NAME = r"""gio-volume-monitor"""


class ZlibCompressorFormat:
    """"""
    ZLIB = 0
    GZIP = 1
    RAW = 2

def action_name_is_valid(action_name=None):
    """"""
    return object

def action_parse_detailed_name(detailed_name=None, action_name=None, target_value=None):
    """"""
    return object

def action_print_detailed_name(action_name=None, target_value=None):
    """"""
    return object

def app_info_create_from_commandline(commandline=None, application_name=None, flags=None):
    """"""
    return object

def app_info_get_all():
    """"""
    return object

def app_info_get_all_for_type(content_type=None):
    """"""
    return object

def app_info_get_default_for_type(content_type=None, must_support_uris=None):
    """"""
    return object

def app_info_get_default_for_uri_scheme(uri_scheme=None):
    """"""
    return object

def app_info_get_fallback_for_type(content_type=None):
    """"""
    return object

def app_info_get_recommended_for_type(content_type=None):
    """"""
    return object

def app_info_launch_default_for_uri(uri=None, context=None):
    """"""
    return object

def app_info_launch_default_for_uri_async(uri=None, context=None, cancellable=None, callback=None, user_data=None):
    """"""
    return object

def app_info_launch_default_for_uri_finish(result=None):
    """"""
    return object

def app_info_reset_type_associations(content_type=None):
    """"""
    return object

def async_initable_newv_async(object_type=None, n_parameters=None, parameters=None, io_priority=None, cancellable=None, callback=None, user_data=None):
    """"""
    return object

def bus_get(bus_type=None, cancellable=None, callback=None, user_data=None):
    """"""
    return object

def bus_get_finish(res=None):
    """"""
    return object

def bus_get_sync(bus_type=None, cancellable=None):
    """"""
    return object

def bus_own_name(bus_type=None, name=None, flags=None, bus_acquired_handler=None, name_acquired_handler=None, name_lost_handler=None, user_data=None, user_data_free_func=None):
    """"""
    return object

def bus_own_name_on_connection(connection=None, name=None, flags=None, name_acquired_handler=None, name_lost_handler=None, user_data=None, user_data_free_func=None):
    """"""
    return object

def bus_own_name_on_connection_with_closures(connection=None, name=None, flags=None, name_acquired_closure=None, name_lost_closure=None):
    """"""
    return object

def bus_own_name_with_closures(bus_type=None, name=None, flags=None, bus_acquired_closure=None, name_acquired_closure=None, name_lost_closure=None):
    """"""
    return object

def bus_unown_name(owner_id=None):
    """"""
    return object

def bus_unwatch_name(watcher_id=None):
    """"""
    return object

def bus_watch_name(bus_type=None, name=None, flags=None, name_appeared_handler=None, name_vanished_handler=None, user_data=None, user_data_free_func=None):
    """"""
    return object

def bus_watch_name_on_connection(connection=None, name=None, flags=None, name_appeared_handler=None, name_vanished_handler=None, user_data=None, user_data_free_func=None):
    """"""
    return object

def bus_watch_name_on_connection_with_closures(connection=None, name=None, flags=None, name_appeared_closure=None, name_vanished_closure=None):
    """"""
    return object

def bus_watch_name_with_closures(bus_type=None, name=None, flags=None, name_appeared_closure=None, name_vanished_closure=None):
    """"""
    return object

def content_type_can_be_executable(type=None):
    """"""
    return object

def content_type_equals(type1=None, type2=None):
    """"""
    return object

def content_type_from_mime_type(mime_type=None):
    """"""
    return object

def content_type_get_description(type=None):
    """"""
    return object

def content_type_get_generic_icon_name(type=None):
    """"""
    return object

def content_type_get_icon(type=None):
    """"""
    return object

def content_type_get_mime_type(type=None):
    """"""
    return object

def content_type_get_symbolic_icon(type=None):
    """"""
    return object

def content_type_guess(filename=None, data=None, data_size=None, result_uncertain=None):
    """"""
    return object

def content_type_guess_for_tree(root=None):
    """"""
    return object

def content_type_is_a(type=None, supertype=None):
    """"""
    return object

def content_type_is_mime_type(type=None, mime_type=None):
    """"""
    return object

def content_type_is_unknown(type=None):
    """"""
    return object

def content_types_get_registered():
    """"""
    return object

def dbus_address_escape_value(string=None):
    """"""
    return object

def dbus_address_get_for_bus_sync(bus_type=None, cancellable=None):
    """"""
    return object

def dbus_address_get_stream(address=None, cancellable=None, callback=None, user_data=None):
    """"""
    return object

def dbus_address_get_stream_finish(res=None, out_guid=None):
    """"""
    return object

def dbus_address_get_stream_sync(address=None, out_guid=None, cancellable=None):
    """"""
    return object

def dbus_annotation_info_lookup(annotations=None, name=None):
    """"""
    return object

def dbus_error_encode_gerror(error=None):
    """"""
    return object

def dbus_error_get_remote_error(error=None):
    """"""
    return object

def dbus_error_is_remote_error(error=None):
    """"""
    return object

def dbus_error_new_for_dbus_error(dbus_error_name=None, dbus_error_message=None):
    """"""
    return object

def dbus_error_quark():
    """"""
    return object

def dbus_error_register_error(error_domain=None, error_code=None, dbus_error_name=None):
    """"""
    return object

def dbus_error_register_error_domain(error_domain_quark_name=None, quark_volatile=None, entries=None, num_entries=None):
    """"""
    return object

def dbus_error_strip_remote_error(error=None):
    """"""
    return object

def dbus_error_unregister_error(error_domain=None, error_code=None, dbus_error_name=None):
    """"""
    return object

def dbus_generate_guid():
    """"""
    return object

def dbus_gvalue_to_gvariant(gvalue=None, type=None):
    """"""
    return object

def dbus_gvariant_to_gvalue(value=None, out_gvalue=None):
    """"""
    return object

def dbus_is_address(string=None):
    """"""
    return object

def dbus_is_guid(string=None):
    """"""
    return object

def dbus_is_interface_name(string=None):
    """"""
    return object

def dbus_is_member_name(string=None):
    """"""
    return object

def dbus_is_name(string=None):
    """"""
    return object

def dbus_is_supported_address(string=None):
    """"""
    return object

def dbus_is_unique_name(string=None):
    """"""
    return object

def dtls_client_connection_new(base_socket=None, server_identity=None):
    """"""
    return object

def dtls_server_connection_new(base_socket=None, certificate=None):
    """"""
    return object

def file_new_for_commandline_arg(arg=None):
    """"""
    return object

def file_new_for_commandline_arg_and_cwd(arg=None, cwd=None):
    """"""
    return object

def file_new_for_path(path=None):
    """"""
    return object

def file_new_for_uri(uri=None):
    """"""
    return object

def file_new_tmp(tmpl=None, iostream=None):
    """"""
    return object

def file_parse_name(parse_name=None):
    """"""
    return object

def icon_deserialize(value=None):
    """"""
    return object

def icon_hash(icon=None):
    """"""
    return object

def icon_new_for_string(str=None):
    """"""
    return object

def initable_newv(object_type=None, n_parameters=None, parameters=None, cancellable=None):
    """"""
    return object

def io_error_from_errno(err_no=None):
    """"""
    return object

def io_error_quark():
    """"""
    return object

def io_extension_point_implement(extension_point_name=None, type=None, extension_name=None, priority=None):
    """"""
    return object

def io_extension_point_lookup(name=None):
    """"""
    return object

def io_extension_point_register(name=None):
    """"""
    return object

def io_modules_load_all_in_directory(dirname=None):
    """"""
    return object

def io_modules_load_all_in_directory_with_scope(dirname=None, scope=None):
    """"""
    return object

def io_modules_scan_all_in_directory(dirname=None):
    """"""
    return object

def io_modules_scan_all_in_directory_with_scope(dirname=None, scope=None):
    """"""
    return object

def io_scheduler_cancel_all_jobs():
    """"""
    return object

def io_scheduler_push_job(job_func=None, user_data=None, notify=None, io_priority=None, cancellable=None):
    """"""
    return object

def keyfile_settings_backend_new(filename=None, root_path=None, root_group=None):
    """"""
    return object

def memory_settings_backend_new():
    """"""
    return object

def network_monitor_get_default():
    """"""
    return object

def networking_init():
    """"""
    return object

def null_settings_backend_new():
    """"""
    return object

def pollable_source_new(pollable_stream=None):
    """"""
    return object

def pollable_source_new_full(pollable_stream=None, child_source=None, cancellable=None):
    """"""
    return object

def pollable_stream_read(stream=None, buffer=None, count=None, blocking=None, cancellable=None):
    """"""
    return object

def pollable_stream_write(stream=None, buffer=None, count=None, blocking=None, cancellable=None):
    """"""
    return object

def pollable_stream_write_all(stream=None, buffer=None, count=None, blocking=None, bytes_written=None, cancellable=None):
    """"""
    return object

def proxy_get_default_for_protocol(protocol=None):
    """"""
    return object

def proxy_resolver_get_default():
    """"""
    return object

def resolver_error_quark():
    """"""
    return object

def resource_error_quark():
    """"""
    return object

def resource_load(filename=None):
    """"""
    return object

def resources_enumerate_children(path=None, lookup_flags=None):
    """"""
    return object

def resources_get_info(path=None, lookup_flags=None, size=None, flags=None):
    """"""
    return object

def resources_lookup_data(path=None, lookup_flags=None):
    """"""
    return object

def resources_open_stream(path=None, lookup_flags=None):
    """"""
    return object

def resources_register(resource=None):
    """"""
    return object

def resources_unregister(resource=None):
    """"""
    return object

def settings_schema_source_get_default():
    """"""
    return object

def simple_async_report_error_in_idle(object=None, callback=None, user_data=None, domain=None, code=None, format=None, *args):
    """"""
    return object

def simple_async_report_gerror_in_idle(object=None, callback=None, user_data=None, error=None):
    """"""
    return object

def simple_async_report_take_gerror_in_idle(object=None, callback=None, user_data=None, error=None):
    """"""
    return object

def srv_target_list_sort(targets=None):
    """"""
    return object

def tls_backend_get_default():
    """"""
    return object

def tls_client_connection_new(base_io_stream=None, server_identity=None):
    """"""
    return object

def tls_error_quark():
    """"""
    return object

def tls_file_database_new(anchors=None):
    """"""
    return object

def tls_server_connection_new(base_io_stream=None, certificate=None):
    """"""
    return object

def unix_is_mount_path_system_internal(mount_path=None):
    """"""
    return object

def unix_is_system_device_path(device_path=None):
    """"""
    return object

def unix_is_system_fs_type(fs_type=None):
    """"""
    return object

def unix_mount_at(mount_path=None, time_read=None):
    """"""
    return object

def unix_mount_compare(mount1=None, mount2=None):
    """"""
    return object

def unix_mount_copy(mount_entry=None):
    """"""
    return object

def unix_mount_for(file_path=None, time_read=None):
    """"""
    return object

def unix_mount_free(mount_entry=None):
    """"""
    return object

def unix_mount_get_device_path(mount_entry=None):
    """"""
    return object

def unix_mount_get_fs_type(mount_entry=None):
    """"""
    return object

def unix_mount_get_mount_path(mount_entry=None):
    """"""
    return object

def unix_mount_guess_can_eject(mount_entry=None):
    """"""
    return object

def unix_mount_guess_icon(mount_entry=None):
    """"""
    return object

def unix_mount_guess_name(mount_entry=None):
    """"""
    return object

def unix_mount_guess_should_display(mount_entry=None):
    """"""
    return object

def unix_mount_guess_symbolic_icon(mount_entry=None):
    """"""
    return object

def unix_mount_is_readonly(mount_entry=None):
    """"""
    return object

def unix_mount_is_system_internal(mount_entry=None):
    """"""
    return object

def unix_mount_points_changed_since(time=None):
    """"""
    return object

def unix_mount_points_get(time_read=None):
    """"""
    return object

def unix_mounts_changed_since(time=None):
    """"""
    return object

def unix_mounts_get(time_read=None):
    """"""
    return object


class Action():
    """"""
    @staticmethod
    def name_is_valid(action_name=None):
        """"""
        return object
    @staticmethod
    def parse_detailed_name(detailed_name=None, action_name=None, target_value=None):
        """"""
        return object
    @staticmethod
    def print_detailed_name(action_name=None, target_value=None):
        """"""
        return object
    
    def activate(self, parameter=None):
        """"""
        return object
    
    def change_state(self, value=None):
        """"""
        return object
    
    def get_enabled(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_parameter_type(self):
        """"""
        return object
    
    def get_state(self):
        """"""
        return object
    
    def get_state_hint(self):
        """"""
        return object
    
    def get_state_type(self):
        """"""
        return object
    
    def activate(self, parameter=None):
        """"""
        return object
    
    def change_state(self, value=None):
        """"""
        return object
    
    def get_enabled(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_parameter_type(self):
        """"""
        return object
    
    def get_state(self):
        """"""
        return object
    
    def get_state_hint(self):
        """"""
        return object
    
    def get_state_type(self):
        """"""
        return object


class ActionEntry():
    """"""

    @property
    def name(self):
        return object

    @property
    def activate(self):
        return object

    @property
    def parameter_type(self):
        return object

    @property
    def state(self):
        return object

    @property
    def change_state(self):
        return object

    @property
    def padding(self):
        return object


class ActionGroup():
    """"""
    
    def action_added(self, action_name=None):
        """"""
        return object
    
    def action_enabled_changed(self, action_name=None, enabled=None):
        """"""
        return object
    
    def action_removed(self, action_name=None):
        """"""
        return object
    
    def action_state_changed(self, action_name=None, state=None):
        """"""
        return object
    
    def activate_action(self, action_name=None, parameter=None):
        """"""
        return object
    
    def change_action_state(self, action_name=None, value=None):
        """"""
        return object
    
    def get_action_enabled(self, action_name=None):
        """"""
        return object
    
    def get_action_parameter_type(self, action_name=None):
        """"""
        return object
    
    def get_action_state(self, action_name=None):
        """"""
        return object
    
    def get_action_state_hint(self, action_name=None):
        """"""
        return object
    
    def get_action_state_type(self, action_name=None):
        """"""
        return object
    
    def has_action(self, action_name=None):
        """"""
        return object
    
    def list_actions(self):
        """"""
        return object
    
    def query_action(self, action_name=None, enabled=None, parameter_type=None, state_type=None, state_hint=None, state=None):
        """"""
        return object
    
    def action_added(self, action_name=None):
        """"""
        return object
    
    def action_enabled_changed(self, action_name=None, enabled=None):
        """"""
        return object
    
    def action_removed(self, action_name=None):
        """"""
        return object
    
    def action_state_changed(self, action_name=None, state=None):
        """"""
        return object
    
    def activate_action(self, action_name=None, parameter=None):
        """"""
        return object
    
    def change_action_state(self, action_name=None, value=None):
        """"""
        return object
    
    def get_action_enabled(self, action_name=None):
        """"""
        return object
    
    def get_action_parameter_type(self, action_name=None):
        """"""
        return object
    
    def get_action_state(self, action_name=None):
        """"""
        return object
    
    def get_action_state_hint(self, action_name=None):
        """"""
        return object
    
    def get_action_state_type(self, action_name=None):
        """"""
        return object
    
    def has_action(self, action_name=None):
        """"""
        return object
    
    def list_actions(self):
        """"""
        return object
    
    def query_action(self, action_name=None, enabled=None, parameter_type=None, state_type=None, state_hint=None, state=None):
        """"""
        return object


class ActionGroupInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def has_action(self):
        return object

    @property
    def list_actions(self):
        return object

    @property
    def get_action_enabled(self):
        return object

    @property
    def get_action_parameter_type(self):
        return object

    @property
    def get_action_state_type(self):
        return object

    @property
    def get_action_state_hint(self):
        return object

    @property
    def get_action_state(self):
        return object

    @property
    def change_action_state(self):
        return object

    @property
    def activate_action(self):
        return object

    @property
    def action_added(self):
        return object

    @property
    def action_removed(self):
        return object

    @property
    def action_enabled_changed(self):
        return object

    @property
    def action_state_changed(self):
        return object

    @property
    def query_action(self):
        return object


class ActionInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def get_name(self):
        return object

    @property
    def get_parameter_type(self):
        return object

    @property
    def get_state_type(self):
        return object

    @property
    def get_state_hint(self):
        return object

    @property
    def get_enabled(self):
        return object

    @property
    def get_state(self):
        return object

    @property
    def change_state(self):
        return object

    @property
    def activate(self):
        return object


class ActionMap():
    """"""
    
    def add_action(self, action=None):
        """"""
        return object
    
    def lookup_action(self, action_name=None):
        """"""
        return object
    
    def remove_action(self, action_name=None):
        """"""
        return object
    
    def add_action(self, action=None):
        """"""
        return object
    
    def add_action_entries(self, entries=None, n_entries=None, user_data=None):
        """"""
        return object
    
    def lookup_action(self, action_name=None):
        """"""
        return object
    
    def remove_action(self, action_name=None):
        """"""
        return object


class ActionMapInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def lookup_action(self):
        return object

    @property
    def add_action(self):
        return object

    @property
    def remove_action(self):
        return object


class AppInfo():
    """"""
    @staticmethod
    def create_from_commandline(commandline=None, application_name=None, flags=None):
        """"""
        return object
    @staticmethod
    def get_all():
        """"""
        return object
    @staticmethod
    def get_all_for_type(content_type=None):
        """"""
        return object
    @staticmethod
    def get_default_for_type(content_type=None, must_support_uris=None):
        """"""
        return object
    @staticmethod
    def get_default_for_uri_scheme(uri_scheme=None):
        """"""
        return object
    @staticmethod
    def get_fallback_for_type(content_type=None):
        """"""
        return object
    @staticmethod
    def get_recommended_for_type(content_type=None):
        """"""
        return object
    @staticmethod
    def launch_default_for_uri(uri=None, context=None):
        """"""
        return object
    @staticmethod
    def launch_default_for_uri_async(uri=None, context=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    @staticmethod
    def launch_default_for_uri_finish(result=None):
        """"""
        return object
    @staticmethod
    def reset_type_associations(content_type=None):
        """"""
        return object
    
    def add_supports_type(self, content_type=None):
        """"""
        return object
    
    def can_delete(self):
        """"""
        return object
    
    def can_remove_supports_type(self):
        """"""
        return object
    
    def do_delete(self):
        """"""
        return object
    
    def dup(self):
        """"""
        return object
    
    def equal(self, appinfo2=None):
        """"""
        return object
    
    def get_commandline(self):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_display_name(self):
        """"""
        return object
    
    def get_executable(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_id(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_supported_types(self):
        """"""
        return object
    
    def launch(self, files=None, context=None):
        """"""
        return object
    
    def launch_uris(self, uris=None, context=None):
        """"""
        return object
    
    def remove_supports_type(self, content_type=None):
        """"""
        return object
    
    def set_as_default_for_extension(self, extension=None):
        """"""
        return object
    
    def set_as_default_for_type(self, content_type=None):
        """"""
        return object
    
    def set_as_last_used_for_type(self, content_type=None):
        """"""
        return object
    
    def should_show(self):
        """"""
        return object
    
    def supports_files(self):
        """"""
        return object
    
    def supports_uris(self):
        """"""
        return object
    
    def add_supports_type(self, content_type=None):
        """"""
        return object
    
    def can_delete(self):
        """"""
        return object
    
    def can_remove_supports_type(self):
        """"""
        return object
    
    def delete(self):
        """"""
        return object
    
    def dup(self):
        """"""
        return object
    
    def equal(self, appinfo2=None):
        """"""
        return object
    
    def get_commandline(self):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_display_name(self):
        """"""
        return object
    
    def get_executable(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_id(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_supported_types(self):
        """"""
        return object
    
    def launch(self, files=None, context=None):
        """"""
        return object
    
    def launch_uris(self, uris=None, context=None):
        """"""
        return object
    
    def remove_supports_type(self, content_type=None):
        """"""
        return object
    
    def set_as_default_for_extension(self, extension=None):
        """"""
        return object
    
    def set_as_default_for_type(self, content_type=None):
        """"""
        return object
    
    def set_as_last_used_for_type(self, content_type=None):
        """"""
        return object
    
    def should_show(self):
        """"""
        return object
    
    def supports_files(self):
        """"""
        return object
    
    def supports_uris(self):
        """"""
        return object


class AppInfoIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def dup(self):
        return object

    @property
    def equal(self):
        return object

    @property
    def get_id(self):
        return object

    @property
    def get_name(self):
        return object

    @property
    def get_description(self):
        return object

    @property
    def get_executable(self):
        return object

    @property
    def get_icon(self):
        return object

    @property
    def launch(self):
        return object

    @property
    def supports_uris(self):
        return object

    @property
    def supports_files(self):
        return object

    @property
    def launch_uris(self):
        return object

    @property
    def should_show(self):
        return object

    @property
    def set_as_default_for_type(self):
        return object

    @property
    def set_as_default_for_extension(self):
        return object

    @property
    def add_supports_type(self):
        return object

    @property
    def can_remove_supports_type(self):
        return object

    @property
    def remove_supports_type(self):
        return object

    @property
    def can_delete(self):
        return object

    @property
    def do_delete(self):
        return object

    @property
    def get_commandline(self):
        return object

    @property
    def get_display_name(self):
        return object

    @property
    def set_as_last_used_for_type(self):
        return object

    @property
    def get_supported_types(self):
        return object


class AppInfoMonitor(GObject.Object):
    """"""
    @staticmethod
    def get():
        """"""
        return object


class AppLaunchContext(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def get_display(self, info=None, files=None):
        """"""
        return object
    
    def get_startup_notify_id(self, info=None, files=None):
        """"""
        return object
    
    def launch_failed(self, startup_notify_id=None):
        """"""
        return object
    
    def launched(self, info=None, platform_data=None):
        """"""
        return object
    
    def get_display(self, info=None, files=None):
        """"""
        return object
    
    def get_environment(self):
        """"""
        return object
    
    def get_startup_notify_id(self, info=None, files=None):
        """"""
        return object
    
    def launch_failed(self, startup_notify_id=None):
        """"""
        return object
    
    def setenv(self, variable=None, value=None):
        """"""
        return object
    
    def unsetenv(self, variable=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class AppLaunchContextClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_display(self):
        return object

    @property
    def get_startup_notify_id(self):
        return object

    @property
    def launch_failed(self):
        return object

    @property
    def launched(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object


class AppLaunchContextPrivate():
    """"""


class Application(GObject.Object, ActionGroup, ActionMap):
    """"""
    
    def __init__(self, application_id=None, flags=None):
        """"""
        return object
    @staticmethod
    def new(application_id=None, flags=None):
        """"""
        return object
    @staticmethod
    def get_default():
        """"""
        return object
    @staticmethod
    def id_is_valid(application_id=None):
        """"""
        return object
    
    def activate(self):
        """"""
        return object
    
    def add_platform_data(self, builder=None):
        """"""
        return object
    
    def after_emit(self, platform_data=None):
        """"""
        return object
    
    def before_emit(self, platform_data=None):
        """"""
        return object
    
    def command_line(self, command_line=None):
        """"""
        return object
    
    def dbus_register(self, connection=None, object_path=None):
        """"""
        return object
    
    def dbus_unregister(self, connection=None, object_path=None):
        """"""
        return object
    
    def handle_local_options(self, options=None):
        """"""
        return object
    
    def local_command_line(self, arguments=None, exit_status=None):
        """"""
        return object
    
    def open(self, files=None, n_files=None, hint=None):
        """"""
        return object
    
    def quit_mainloop(self):
        """"""
        return object
    
    def run_mainloop(self):
        """"""
        return object
    
    def shutdown(self):
        """"""
        return object
    
    def startup(self):
        """"""
        return object
    
    def activate(self):
        """"""
        return object
    
    def add_main_option(self, long_name=None, short_name=None, flags=None, arg=None, description=None, arg_description=None):
        """"""
        return object
    
    def add_main_option_entries(self, entries=None):
        """"""
        return object
    
    def add_option_group(self, group=None):
        """"""
        return object
    
    def bind_busy_property(self, object=None, property=None):
        """"""
        return object
    
    def get_application_id(self):
        """"""
        return object
    
    def get_dbus_connection(self):
        """"""
        return object
    
    def get_dbus_object_path(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_inactivity_timeout(self):
        """"""
        return object
    
    def get_is_busy(self):
        """"""
        return object
    
    def get_is_registered(self):
        """"""
        return object
    
    def get_is_remote(self):
        """"""
        return object
    
    def get_resource_base_path(self):
        """"""
        return object
    
    def hold(self):
        """"""
        return object
    
    def mark_busy(self):
        """"""
        return object
    
    def open(self, files=None, n_files=None, hint=None):
        """"""
        return object
    
    def quit(self):
        """"""
        return object
    
    def register(self, cancellable=None):
        """"""
        return object
    
    def release(self):
        """"""
        return object
    
    def run(self, argc=None, argv=None):
        """"""
        return object
    
    def send_notification(self, id=None, notification=None):
        """"""
        return object
    
    def set_action_group(self, action_group=None):
        """"""
        return object
    
    def set_application_id(self, application_id=None):
        """"""
        return object
    
    def set_default(self):
        """"""
        return object
    
    def set_flags(self, flags=None):
        """"""
        return object
    
    def set_inactivity_timeout(self, inactivity_timeout=None):
        """"""
        return object
    
    def set_option_context_description(self, description=None):
        """"""
        return object
    
    def set_option_context_parameter_string(self, parameter_string=None):
        """"""
        return object
    
    def set_option_context_summary(self, summary=None):
        """"""
        return object
    
    def set_resource_base_path(self, resource_path=None):
        """"""
        return object
    
    def unbind_busy_property(self, object=None, property=None):
        """"""
        return object
    
    def unmark_busy(self):
        """"""
        return object
    
    def withdraw_notification(self, id=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ApplicationClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def startup(self):
        return object

    @property
    def activate(self):
        return object

    @property
    def open(self):
        return object

    @property
    def command_line(self):
        return object

    @property
    def local_command_line(self):
        return object

    @property
    def before_emit(self):
        return object

    @property
    def after_emit(self):
        return object

    @property
    def add_platform_data(self):
        return object

    @property
    def quit_mainloop(self):
        return object

    @property
    def run_mainloop(self):
        return object

    @property
    def shutdown(self):
        return object

    @property
    def dbus_register(self):
        return object

    @property
    def dbus_unregister(self):
        return object

    @property
    def handle_local_options(self):
        return object

    @property
    def padding(self):
        return object


class ApplicationCommandLine(GObject.Object):
    """"""
    
    def get_stdin(self):
        """"""
        return object
    
    def print_literal(self, message=None):
        """"""
        return object
    
    def printerr_literal(self, message=None):
        """"""
        return object
    
    def create_file_for_arg(self, arg=None):
        """"""
        return object
    
    def get_arguments(self, argc=None):
        """"""
        return object
    
    def get_cwd(self):
        """"""
        return object
    
    def get_environ(self):
        """"""
        return object
    
    def get_exit_status(self):
        """"""
        return object
    
    def get_is_remote(self):
        """"""
        return object
    
    def get_options_dict(self):
        """"""
        return object
    
    def get_platform_data(self):
        """"""
        return object
    
    def get_stdin(self):
        """"""
        return object
    
    def getenv(self, name=None):
        """"""
        return object
    
    def print_(self, format=None, *args):
        """"""
        return object
    
    def printerr(self, format=None, *args):
        """"""
        return object
    
    def set_exit_status(self, exit_status=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ApplicationCommandLineClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def print_literal(self):
        return object

    @property
    def printerr_literal(self):
        return object

    @property
    def get_stdin(self):
        return object

    @property
    def padding(self):
        return object


class ApplicationCommandLinePrivate():
    """"""


class ApplicationPrivate():
    """"""


class AsyncInitable():
    """"""
    @staticmethod
    def new_async(object_type=None, io_priority=None, cancellable=None, callback=None, user_data=None, first_property_name=None, *args):
        """"""
        return object
    @staticmethod
    def new_valist_async(object_type=None, first_property_name=None, var_args=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    @staticmethod
    def newv_async(object_type=None, n_parameters=None, parameters=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def init_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def init_finish(self, res=None):
        """"""
        return object
    
    def init_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def init_finish(self, res=None):
        """"""
        return object
    
    def new_finish(self, res=None):
        """"""
        return object


class AsyncInitableIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def init_async(self):
        return object

    @property
    def init_finish(self):
        return object


class AsyncResult():
    """"""
    
    def get_source_object(self):
        """"""
        return object
    
    def get_user_data(self):
        """"""
        return object
    
    def is_tagged(self, source_tag=None):
        """"""
        return object
    
    def get_source_object(self):
        """"""
        return object
    
    def get_user_data(self):
        """"""
        return object
    
    def is_tagged(self, source_tag=None):
        """"""
        return object
    
    def legacy_propagate_error(self):
        """"""
        return object


class AsyncResultIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def get_user_data(self):
        return object

    @property
    def get_source_object(self):
        return object

    @property
    def is_tagged(self):
        return object


class BufferedInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def fill(self):
        return object

    @property
    def fill_async(self):
        return object

    @property
    def fill_finish(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class BufferedInputStreamPrivate():
    """"""


class BufferedOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object


class BufferedOutputStreamPrivate():
    """"""


class Cancellable(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def get_current():
        """"""
        return object
    
    def cancelled(self):
        """"""
        return object
    
    def cancel(self):
        """"""
        return object
    
    def connect(self, callback=None, data=None, data_destroy_func=None):
        """"""
        return object
    
    def disconnect(self, handler_id=None):
        """"""
        return object
    
    def get_fd(self):
        """"""
        return object
    
    def is_cancelled(self):
        """"""
        return object
    
    def make_pollfd(self, pollfd=None):
        """"""
        return object
    
    def pop_current(self):
        """"""
        return object
    
    def push_current(self):
        """"""
        return object
    
    def release_fd(self):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def set_error_if_cancelled(self):
        """"""
        return object
    
    def source_new(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class CancellableClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def cancelled(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class CancellablePrivate():
    """"""


class CharsetConverterClass():
    """"""

    @property
    def parent_class(self):
        return object


class Converter():
    """"""
    
    def convert(self, inbuf=None, inbuf_size=None, outbuf=None, outbuf_size=None, flags=None, bytes_read=None, bytes_written=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def convert(self, inbuf=None, inbuf_size=None, outbuf=None, outbuf_size=None, flags=None, bytes_read=None, bytes_written=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object


class ConverterIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def convert(self):
        return object

    @property
    def reset(self):
        return object


class ConverterInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class ConverterInputStreamPrivate():
    """"""


class ConverterOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class ConverterOutputStreamPrivate():
    """"""


class Credentials(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def get_native(self, native_type=None):
        """"""
        return object
    
    def get_unix_pid(self):
        """"""
        return object
    
    def get_unix_user(self):
        """"""
        return object
    
    def is_same_user(self, other_credentials=None):
        """"""
        return object
    
    def set_native(self, native_type=None, native=None):
        """"""
        return object
    
    def set_unix_user(self, uid=None):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object


class CredentialsClass():
    """"""


class DBusAnnotationInfo():
    """"""
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def lookup(annotations=None, name=None):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def key(self):
        return object

    @property
    def value(self):
        return object

    @property
    def annotations(self):
        return object


class DBusArgInfo():
    """"""
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def name(self):
        return object

    @property
    def signature(self):
        return object

    @property
    def annotations(self):
        return object


class DBusAuthObserver(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def allow_mechanism(self, mechanism=None):
        """"""
        return object
    
    def authorize_authenticated_peer(self, stream=None, credentials=None):
        """"""
        return object


class DBusErrorEntry():
    """"""

    @property
    def error_code(self):
        return object

    @property
    def dbus_error_name(self):
        return object


class DBusInterface():
    """"""
    
    def dup_object(self):
        """"""
        return object
    
    def get_info(self):
        """"""
        return object
    
    def get_object(self):
        """"""
        return object
    
    def set_object(self, object=None):
        """"""
        return object
    
    def dup_object(self):
        """"""
        return object
    
    def get_info(self):
        """"""
        return object
    
    def get_object(self):
        """"""
        return object
    
    def set_object(self, object=None):
        """"""
        return object


class DBusInterfaceIface():
    """"""

    @property
    def parent_iface(self):
        return object

    @property
    def get_info(self):
        return object

    @property
    def get_object(self):
        return object

    @property
    def set_object(self):
        return object

    @property
    def dup_object(self):
        return object


class DBusInterfaceInfo():
    """"""
    
    def cache_build(self):
        """"""
        return object
    
    def cache_release(self):
        """"""
        return object
    
    def generate_xml(self, indent=None, string_builder=None):
        """"""
        return object
    
    def lookup_method(self, name=None):
        """"""
        return object
    
    def lookup_property(self, name=None):
        """"""
        return object
    
    def lookup_signal(self, name=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def name(self):
        return object

    @property
    def methods(self):
        return object

    @property
    def signals(self):
        return object

    @property
    def properties(self):
        return object

    @property
    def annotations(self):
        return object


class DBusInterfaceSkeleton(GObject.Object, DBusInterface):
    """"""
    
    def flush(self):
        """"""
        return object
    
    def g_authorize_method(self, invocation=None):
        """"""
        return object
    
    def get_info(self):
        """"""
        return object
    
    def get_properties(self):
        """"""
        return object
    
    def get_vtable(self):
        """"""
        return object
    
    def export(self, connection=None, object_path=None):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def get_connection(self):
        """"""
        return object
    
    def get_connections(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_info(self):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object
    
    def get_properties(self):
        """"""
        return object
    
    def get_vtable(self):
        """"""
        return object
    
    def has_connection(self, connection=None):
        """"""
        return object
    
    def set_flags(self, flags=None):
        """"""
        return object
    
    def unexport(self):
        """"""
        return object
    
    def unexport_from_connection(self, connection=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DBusInterfaceSkeletonClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_info(self):
        return object

    @property
    def get_vtable(self):
        return object

    @property
    def get_properties(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def vfunc_padding(self):
        return object

    @property
    def g_authorize_method(self):
        return object

    @property
    def signal_padding(self):
        return object


class DBusInterfaceSkeletonPrivate():
    """"""


class DBusInterfaceVTable():
    """"""

    @property
    def method_call(self):
        return object

    @property
    def get_property(self):
        return object

    @property
    def set_property(self):
        return object

    @property
    def padding(self):
        return object


class DBusMessage(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_from_blob(blob=None, blob_len=None, capabilities=None):
        """"""
        return object
    @staticmethod
    def new_method_call(name=None, path=None, interface_=None, method=None):
        """"""
        return object
    @staticmethod
    def new_signal(path=None, interface_=None, signal=None):
        """"""
        return object
    @staticmethod
    def bytes_needed(blob=None, blob_len=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def get_arg0(self):
        """"""
        return object
    
    def get_body(self):
        """"""
        return object
    
    def get_byte_order(self):
        """"""
        return object
    
    def get_destination(self):
        """"""
        return object
    
    def get_error_name(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_header(self, header_field=None):
        """"""
        return object
    
    def get_header_fields(self):
        """"""
        return object
    
    def get_interface(self):
        """"""
        return object
    
    def get_locked(self):
        """"""
        return object
    
    def get_member(self):
        """"""
        return object
    
    def get_message_type(self):
        """"""
        return object
    
    def get_num_unix_fds(self):
        """"""
        return object
    
    def get_path(self):
        """"""
        return object
    
    def get_reply_serial(self):
        """"""
        return object
    
    def get_sender(self):
        """"""
        return object
    
    def get_serial(self):
        """"""
        return object
    
    def get_signature(self):
        """"""
        return object
    
    def get_unix_fd_list(self):
        """"""
        return object
    
    def lock(self):
        """"""
        return object
    
    def new_method_error(self, error_name=None, error_message_format=None, *args):
        """"""
        return object
    
    def new_method_error_literal(self, error_name=None, error_message=None):
        """"""
        return object
    
    def new_method_error_valist(self, error_name=None, error_message_format=None, var_args=None):
        """"""
        return object
    
    def new_method_reply(self):
        """"""
        return object
    
    def print_(self, indent=None):
        """"""
        return object
    
    def set_body(self, body=None):
        """"""
        return object
    
    def set_byte_order(self, byte_order=None):
        """"""
        return object
    
    def set_destination(self, value=None):
        """"""
        return object
    
    def set_error_name(self, value=None):
        """"""
        return object
    
    def set_flags(self, flags=None):
        """"""
        return object
    
    def set_header(self, header_field=None, value=None):
        """"""
        return object
    
    def set_interface(self, value=None):
        """"""
        return object
    
    def set_member(self, value=None):
        """"""
        return object
    
    def set_message_type(self, type=None):
        """"""
        return object
    
    def set_num_unix_fds(self, value=None):
        """"""
        return object
    
    def set_path(self, value=None):
        """"""
        return object
    
    def set_reply_serial(self, value=None):
        """"""
        return object
    
    def set_sender(self, value=None):
        """"""
        return object
    
    def set_serial(self, serial=None):
        """"""
        return object
    
    def set_signature(self, value=None):
        """"""
        return object
    
    def set_unix_fd_list(self, fd_list=None):
        """"""
        return object
    
    def to_blob(self, out_size=None, capabilities=None):
        """"""
        return object
    
    def to_gerror(self):
        """"""
        return object


class DBusMethodInfo():
    """"""
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def name(self):
        return object

    @property
    def in_args(self):
        return object

    @property
    def out_args(self):
        return object

    @property
    def annotations(self):
        return object


class DBusMethodInvocation(GObject.Object):
    """"""
    
    def get_connection(self):
        """"""
        return object
    
    def get_interface_name(self):
        """"""
        return object
    
    def get_message(self):
        """"""
        return object
    
    def get_method_info(self):
        """"""
        return object
    
    def get_method_name(self):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object
    
    def get_parameters(self):
        """"""
        return object
    
    def get_property_info(self):
        """"""
        return object
    
    def get_sender(self):
        """"""
        return object
    
    def get_user_data(self):
        """"""
        return object
    
    def return_dbus_error(self, error_name=None, error_message=None):
        """"""
        return object
    
    def return_error(self, domain=None, code=None, format=None, *args):
        """"""
        return object
    
    def return_error_literal(self, domain=None, code=None, message=None):
        """"""
        return object
    
    def return_error_valist(self, domain=None, code=None, format=None, var_args=None):
        """"""
        return object
    
    def return_gerror(self, error=None):
        """"""
        return object
    
    def return_value(self, parameters=None):
        """"""
        return object
    
    def return_value_with_unix_fd_list(self, parameters=None, fd_list=None):
        """"""
        return object
    
    def take_error(self, error=None):
        """"""
        return object


class DBusNodeInfo():
    """"""
    @staticmethod
    def new_for_xml(xml_data=None):
        """"""
        return object
    
    def generate_xml(self, indent=None, string_builder=None):
        """"""
        return object
    
    def lookup_interface(self, name=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def path(self):
        return object

    @property
    def interfaces(self):
        return object

    @property
    def nodes(self):
        return object

    @property
    def annotations(self):
        return object


class DBusObject():
    """"""
    
    def get_interface(self, interface_name=None):
        """"""
        return object
    
    def get_interfaces(self):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object
    
    def interface_added(self, interface_=None):
        """"""
        return object
    
    def interface_removed(self, interface_=None):
        """"""
        return object
    
    def get_interface(self, interface_name=None):
        """"""
        return object
    
    def get_interfaces(self):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object


class DBusObjectIface():
    """"""

    @property
    def parent_iface(self):
        return object

    @property
    def get_object_path(self):
        return object

    @property
    def get_interfaces(self):
        return object

    @property
    def get_interface(self):
        return object

    @property
    def interface_added(self):
        return object

    @property
    def interface_removed(self):
        return object


class DBusObjectManager():
    """"""
    
    def get_interface(self, object_path=None, interface_name=None):
        """"""
        return object
    
    def get_object(self, object_path=None):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object
    
    def get_objects(self):
        """"""
        return object
    
    def interface_added(self, object=None, interface_=None):
        """"""
        return object
    
    def interface_removed(self, object=None, interface_=None):
        """"""
        return object
    
    def object_added(self, object=None):
        """"""
        return object
    
    def object_removed(self, object=None):
        """"""
        return object
    
    def get_interface(self, object_path=None, interface_name=None):
        """"""
        return object
    
    def get_object(self, object_path=None):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object
    
    def get_objects(self):
        """"""
        return object


class DBusObjectManagerClientClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def interface_proxy_signal(self):
        return object

    @property
    def interface_proxy_properties_changed(self):
        return object

    @property
    def padding(self):
        return object


class DBusObjectManagerClientPrivate():
    """"""


class DBusObjectManagerIface():
    """"""

    @property
    def parent_iface(self):
        return object

    @property
    def get_object_path(self):
        return object

    @property
    def get_objects(self):
        return object

    @property
    def get_object(self):
        return object

    @property
    def get_interface(self):
        return object

    @property
    def object_added(self):
        return object

    @property
    def object_removed(self):
        return object

    @property
    def interface_added(self):
        return object

    @property
    def interface_removed(self):
        return object


class DBusObjectManagerServer(GObject.Object, DBusObjectManager):
    """"""
    
    def __init__(self, object_path=None):
        """"""
        return object
    @staticmethod
    def new(object_path=None):
        """"""
        return object
    
    def export(self, object=None):
        """"""
        return object
    
    def export_uniquely(self, object=None):
        """"""
        return object
    
    def get_connection(self):
        """"""
        return object
    
    def is_exported(self, object=None):
        """"""
        return object
    
    def set_connection(self, connection=None):
        """"""
        return object
    
    def unexport(self, object_path=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DBusObjectManagerServerClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def padding(self):
        return object


class DBusObjectManagerServerPrivate():
    """"""


class DBusObjectProxy(GObject.Object, DBusObject):
    """"""
    
    def __init__(self, connection=None, object_path=None):
        """"""
        return object
    @staticmethod
    def new(connection=None, object_path=None):
        """"""
        return object
    
    def get_connection(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DBusObjectProxyClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def padding(self):
        return object


class DBusObjectProxyPrivate():
    """"""


class DBusObjectSkeleton(GObject.Object, DBusObject):
    """"""
    
    def __init__(self, object_path=None):
        """"""
        return object
    @staticmethod
    def new(object_path=None):
        """"""
        return object
    
    def authorize_method(self, interface_=None, invocation=None):
        """"""
        return object
    
    def add_interface(self, interface_=None):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def remove_interface(self, interface_=None):
        """"""
        return object
    
    def remove_interface_by_name(self, interface_name=None):
        """"""
        return object
    
    def set_object_path(self, object_path=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DBusObjectSkeletonClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def authorize_method(self):
        return object

    @property
    def padding(self):
        return object


class DBusObjectSkeletonPrivate():
    """"""


class DBusPropertyInfo():
    """"""
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def name(self):
        return object

    @property
    def signature(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def annotations(self):
        return object


class DBusProxyClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def g_properties_changed(self):
        return object

    @property
    def g_signal(self):
        return object

    @property
    def padding(self):
        return object


class DBusProxyPrivate():
    """"""


class DBusSignalInfo():
    """"""
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def name(self):
        return object

    @property
    def args(self):
        return object

    @property
    def annotations(self):
        return object


class DBusSubtreeVTable():
    """"""

    @property
    def enumerate(self):
        return object

    @property
    def introspect(self):
        return object

    @property
    def dispatch(self):
        return object

    @property
    def padding(self):
        return object


class DataInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class DataInputStreamPrivate():
    """"""


class DataOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class DataOutputStreamPrivate():
    """"""


class DatagramBased():
    """"""
    
    def condition_check(self, condition=None):
        """"""
        return object
    
    def condition_wait(self, condition=None, timeout=None, cancellable=None):
        """"""
        return object
    
    def create_source(self, condition=None, cancellable=None):
        """"""
        return object
    
    def receive_messages(self, messages=None, num_messages=None, flags=None, timeout=None, cancellable=None):
        """"""
        return object
    
    def send_messages(self, messages=None, num_messages=None, flags=None, timeout=None, cancellable=None):
        """"""
        return object
    
    def condition_check(self, condition=None):
        """"""
        return object
    
    def condition_wait(self, condition=None, timeout=None, cancellable=None):
        """"""
        return object
    
    def create_source(self, condition=None, cancellable=None):
        """"""
        return object
    
    def receive_messages(self, messages=None, num_messages=None, flags=None, timeout=None, cancellable=None):
        """"""
        return object
    
    def send_messages(self, messages=None, num_messages=None, flags=None, timeout=None, cancellable=None):
        """"""
        return object


class DatagramBasedInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def receive_messages(self):
        return object

    @property
    def send_messages(self):
        return object

    @property
    def create_source(self):
        return object

    @property
    def condition_check(self):
        return object

    @property
    def condition_wait(self):
        return object


class DesktopAppInfo(GObject.Object, AppInfo):
    """"""
    
    def __init__(self, desktop_id=None):
        """"""
        return object
    @staticmethod
    def new(desktop_id=None):
        """"""
        return object
    @staticmethod
    def new_from_filename(filename=None):
        """"""
        return object
    @staticmethod
    def new_from_keyfile(key_file=None):
        """"""
        return object
    @staticmethod
    def get_implementations(interface=None):
        """"""
        return object
    @staticmethod
    def search(search_string=None):
        """"""
        return object
    @staticmethod
    def set_desktop_env(desktop_env=None):
        """"""
        return object
    
    def get_action_name(self, action_name=None):
        """"""
        return object
    
    def get_boolean(self, key=None):
        """"""
        return object
    
    def get_categories(self):
        """"""
        return object
    
    def get_filename(self):
        """"""
        return object
    
    def get_generic_name(self):
        """"""
        return object
    
    def get_is_hidden(self):
        """"""
        return object
    
    def get_keywords(self):
        """"""
        return object
    
    def get_locale_string(self, key=None):
        """"""
        return object
    
    def get_nodisplay(self):
        """"""
        return object
    
    def get_show_in(self, desktop_env=None):
        """"""
        return object
    
    def get_startup_wm_class(self):
        """"""
        return object
    
    def get_string(self, key=None):
        """"""
        return object
    
    def has_key(self, key=None):
        """"""
        return object
    
    def launch_action(self, action_name=None, launch_context=None):
        """"""
        return object
    
    def launch_uris_as_manager(self, uris=None, launch_context=None, spawn_flags=None, user_setup=None, user_setup_data=None, pid_callback=None, pid_callback_data=None):
        """"""
        return object
    
    def list_actions(self):
        """"""
        return object


class DesktopAppInfoClass():
    """"""

    @property
    def parent_class(self):
        return object


class DesktopAppInfoLookup():
    """"""
    
    def get_default_for_uri_scheme(self, uri_scheme=None):
        """"""
        return object
    
    def get_default_for_uri_scheme(self, uri_scheme=None):
        """"""
        return object


class DesktopAppInfoLookupIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def get_default_for_uri_scheme(self):
        return object


class Drive():
    """"""
    
    def can_eject(self):
        """"""
        return object
    
    def can_poll_for_media(self):
        """"""
        return object
    
    def can_start(self):
        """"""
        return object
    
    def can_start_degraded(self):
        """"""
        return object
    
    def can_stop(self):
        """"""
        return object
    
    def changed(self):
        """"""
        return object
    
    def disconnected(self):
        """"""
        return object
    
    def eject(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_button(self):
        """"""
        return object
    
    def eject_finish(self, result=None):
        """"""
        return object
    
    def eject_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_with_operation_finish(self, result=None):
        """"""
        return object
    
    def enumerate_identifiers(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_identifier(self, kind=None):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_sort_key(self):
        """"""
        return object
    
    def get_start_stop_type(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_volumes(self):
        """"""
        return object
    
    def has_media(self):
        """"""
        return object
    
    def has_volumes(self):
        """"""
        return object
    
    def is_media_check_automatic(self):
        """"""
        return object
    
    def is_media_removable(self):
        """"""
        return object
    
    def is_removable(self):
        """"""
        return object
    
    def poll_for_media(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def poll_for_media_finish(self, result=None):
        """"""
        return object
    
    def start(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def start_finish(self, result=None):
        """"""
        return object
    
    def stop(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def stop_button(self):
        """"""
        return object
    
    def stop_finish(self, result=None):
        """"""
        return object
    
    def can_eject(self):
        """"""
        return object
    
    def can_poll_for_media(self):
        """"""
        return object
    
    def can_start(self):
        """"""
        return object
    
    def can_start_degraded(self):
        """"""
        return object
    
    def can_stop(self):
        """"""
        return object
    
    def eject(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_finish(self, result=None):
        """"""
        return object
    
    def eject_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_with_operation_finish(self, result=None):
        """"""
        return object
    
    def enumerate_identifiers(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_identifier(self, kind=None):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_sort_key(self):
        """"""
        return object
    
    def get_start_stop_type(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_volumes(self):
        """"""
        return object
    
    def has_media(self):
        """"""
        return object
    
    def has_volumes(self):
        """"""
        return object
    
    def is_media_check_automatic(self):
        """"""
        return object
    
    def is_media_removable(self):
        """"""
        return object
    
    def is_removable(self):
        """"""
        return object
    
    def poll_for_media(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def poll_for_media_finish(self, result=None):
        """"""
        return object
    
    def start(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def start_finish(self, result=None):
        """"""
        return object
    
    def stop(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def stop_finish(self, result=None):
        """"""
        return object


class DriveIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def changed(self):
        return object

    @property
    def disconnected(self):
        return object

    @property
    def eject_button(self):
        return object

    @property
    def get_name(self):
        return object

    @property
    def get_icon(self):
        return object

    @property
    def has_volumes(self):
        return object

    @property
    def get_volumes(self):
        return object

    @property
    def is_media_removable(self):
        return object

    @property
    def has_media(self):
        return object

    @property
    def is_media_check_automatic(self):
        return object

    @property
    def can_eject(self):
        return object

    @property
    def can_poll_for_media(self):
        return object

    @property
    def eject(self):
        return object

    @property
    def eject_finish(self):
        return object

    @property
    def poll_for_media(self):
        return object

    @property
    def poll_for_media_finish(self):
        return object

    @property
    def get_identifier(self):
        return object

    @property
    def enumerate_identifiers(self):
        return object

    @property
    def get_start_stop_type(self):
        return object

    @property
    def can_start(self):
        return object

    @property
    def can_start_degraded(self):
        return object

    @property
    def start(self):
        return object

    @property
    def start_finish(self):
        return object

    @property
    def can_stop(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def stop_finish(self):
        return object

    @property
    def stop_button(self):
        return object

    @property
    def eject_with_operation(self):
        return object

    @property
    def eject_with_operation_finish(self):
        return object

    @property
    def get_sort_key(self):
        return object

    @property
    def get_symbolic_icon(self):
        return object

    @property
    def is_removable(self):
        return object


class DtlsClientConnection():
    """"""
    @staticmethod
    def new(base_socket=None, server_identity=None):
        """"""
        return object
    
    def get_accepted_cas(self):
        """"""
        return object
    
    def get_server_identity(self):
        """"""
        return object
    
    def get_validation_flags(self):
        """"""
        return object
    
    def set_server_identity(self, identity=None):
        """"""
        return object
    
    def set_validation_flags(self, flags=None):
        """"""
        return object


class DtlsClientConnectionInterface():
    """"""

    @property
    def g_iface(self):
        return object


class DtlsConnection():
    """"""
    
    def accept_certificate(self, peer_cert=None, errors=None):
        """"""
        return object
    
    def handshake(self, cancellable=None):
        """"""
        return object
    
    def handshake_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def handshake_finish(self, result=None):
        """"""
        return object
    
    def shutdown(self, shutdown_read=None, shutdown_write=None, cancellable=None):
        """"""
        return object
    
    def shutdown_async(self, shutdown_read=None, shutdown_write=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def shutdown_finish(self, result=None):
        """"""
        return object
    
    def close(self, cancellable=None):
        """"""
        return object
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def emit_accept_certificate(self, peer_cert=None, errors=None):
        """"""
        return object
    
    def get_certificate(self):
        """"""
        return object
    
    def get_database(self):
        """"""
        return object
    
    def get_interaction(self):
        """"""
        return object
    
    def get_peer_certificate(self):
        """"""
        return object
    
    def get_peer_certificate_errors(self):
        """"""
        return object
    
    def get_rehandshake_mode(self):
        """"""
        return object
    
    def get_require_close_notify(self):
        """"""
        return object
    
    def handshake(self, cancellable=None):
        """"""
        return object
    
    def handshake_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def handshake_finish(self, result=None):
        """"""
        return object
    
    def set_certificate(self, certificate=None):
        """"""
        return object
    
    def set_database(self, database=None):
        """"""
        return object
    
    def set_interaction(self, interaction=None):
        """"""
        return object
    
    def set_rehandshake_mode(self, mode=None):
        """"""
        return object
    
    def set_require_close_notify(self, require_close_notify=None):
        """"""
        return object
    
    def shutdown(self, shutdown_read=None, shutdown_write=None, cancellable=None):
        """"""
        return object
    
    def shutdown_async(self, shutdown_read=None, shutdown_write=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def shutdown_finish(self, result=None):
        """"""
        return object


class DtlsConnectionInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def accept_certificate(self):
        return object

    @property
    def handshake(self):
        return object

    @property
    def handshake_async(self):
        return object

    @property
    def handshake_finish(self):
        return object

    @property
    def shutdown(self):
        return object

    @property
    def shutdown_async(self):
        return object

    @property
    def shutdown_finish(self):
        return object


class DtlsServerConnection():
    """"""
    @staticmethod
    def new(base_socket=None, certificate=None):
        """"""
        return object


class DtlsServerConnectionInterface():
    """"""

    @property
    def g_iface(self):
        return object


class EmblemClass():
    """"""


class EmblemedIconClass():
    """"""

    @property
    def parent_class(self):
        return object


class EmblemedIconPrivate():
    """"""


class File():
    """"""
    @staticmethod
    def new_build_filename(first_element=None, *args):
        """"""
        return object
    @staticmethod
    def new_for_commandline_arg(arg=None):
        """"""
        return object
    @staticmethod
    def new_for_commandline_arg_and_cwd(arg=None, cwd=None):
        """"""
        return object
    @staticmethod
    def new_for_path(path=None):
        """"""
        return object
    @staticmethod
    def new_for_uri(uri=None):
        """"""
        return object
    @staticmethod
    def new_tmp(tmpl=None, iostream=None):
        """"""
        return object
    @staticmethod
    def parse_name(parse_name=None):
        """"""
        return object
    
    def append_to(self, flags=None, cancellable=None):
        """"""
        return object
    
    def append_to_async(self, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def append_to_finish(self, res=None):
        """"""
        return object
    
    def copy(self, destination=None, flags=None, cancellable=None, progress_callback=None, progress_callback_data=None):
        """"""
        return object
    
    def copy_async(self, destination=None, flags=None, io_priority=None, cancellable=None, progress_callback=None, progress_callback_data=None, callback=None, user_data=None):
        """"""
        return object
    
    def copy_finish(self, res=None):
        """"""
        return object
    
    def create(self, flags=None, cancellable=None):
        """"""
        return object
    
    def create_async(self, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def create_finish(self, res=None):
        """"""
        return object
    
    def create_readwrite(self, flags=None, cancellable=None):
        """"""
        return object
    
    def create_readwrite_async(self, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def create_readwrite_finish(self, res=None):
        """"""
        return object
    
    def delete_file(self, cancellable=None):
        """"""
        return object
    
    def delete_file_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def delete_file_finish(self, result=None):
        """"""
        return object
    
    def dup(self):
        """"""
        return object
    
    def eject_mountable(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_mountable_finish(self, result=None):
        """"""
        return object
    
    def eject_mountable_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_mountable_with_operation_finish(self, result=None):
        """"""
        return object
    
    def enumerate_children(self, attributes=None, flags=None, cancellable=None):
        """"""
        return object
    
    def enumerate_children_async(self, attributes=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def enumerate_children_finish(self, res=None):
        """"""
        return object
    
    def equal(self, file2=None):
        """"""
        return object
    
    def find_enclosing_mount(self, cancellable=None):
        """"""
        return object
    
    def find_enclosing_mount_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def find_enclosing_mount_finish(self, res=None):
        """"""
        return object
    
    def get_basename(self):
        """"""
        return object
    
    def get_child_for_display_name(self, display_name=None):
        """"""
        return object
    
    def get_parent(self):
        """"""
        return object
    
    def get_parse_name(self):
        """"""
        return object
    
    def get_path(self):
        """"""
        return object
    
    def get_relative_path(self, descendant=None):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_uri_scheme(self):
        """"""
        return object
    
    def has_uri_scheme(self, uri_scheme=None):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def is_native(self):
        """"""
        return object
    
    def make_directory(self, cancellable=None):
        """"""
        return object
    
    def make_directory_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def make_directory_finish(self, result=None):
        """"""
        return object
    
    def make_symbolic_link(self, symlink_value=None, cancellable=None):
        """"""
        return object
    
    def measure_disk_usage(self, flags=None, cancellable=None, progress_callback=None, progress_data=None, disk_usage=None, num_dirs=None, num_files=None):
        """"""
        return object
    
    def measure_disk_usage_async(self, flags=None, io_priority=None, cancellable=None, progress_callback=None, progress_data=None, callback=None, user_data=None):
        """"""
        return object
    
    def measure_disk_usage_finish(self, result=None, disk_usage=None, num_dirs=None, num_files=None):
        """"""
        return object
    
    def monitor_dir(self, flags=None, cancellable=None):
        """"""
        return object
    
    def monitor_file(self, flags=None, cancellable=None):
        """"""
        return object
    
    def mount_enclosing_volume(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def mount_enclosing_volume_finish(self, result=None):
        """"""
        return object
    
    def mount_mountable(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def mount_mountable_finish(self, result=None):
        """"""
        return object
    
    def move(self, destination=None, flags=None, cancellable=None, progress_callback=None, progress_callback_data=None):
        """"""
        return object
    
    def open_readwrite(self, cancellable=None):
        """"""
        return object
    
    def open_readwrite_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def open_readwrite_finish(self, res=None):
        """"""
        return object
    
    def poll_mountable(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def poll_mountable_finish(self, result=None):
        """"""
        return object
    
    def prefix_matches(self, file=None):
        """"""
        return object
    
    def query_filesystem_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_filesystem_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_filesystem_info_finish(self, res=None):
        """"""
        return object
    
    def query_info(self, attributes=None, flags=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, res=None):
        """"""
        return object
    
    def query_settable_attributes(self, cancellable=None):
        """"""
        return object
    
    def query_writable_namespaces(self, cancellable=None):
        """"""
        return object
    
    def read_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_finish(self, res=None):
        """"""
        return object
    
    def read_fn(self, cancellable=None):
        """"""
        return object
    
    def replace(self, etag=None, make_backup=None, flags=None, cancellable=None):
        """"""
        return object
    
    def replace_async(self, etag=None, make_backup=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def replace_finish(self, res=None):
        """"""
        return object
    
    def replace_readwrite(self, etag=None, make_backup=None, flags=None, cancellable=None):
        """"""
        return object
    
    def replace_readwrite_async(self, etag=None, make_backup=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def replace_readwrite_finish(self, res=None):
        """"""
        return object
    
    def resolve_relative_path(self, relative_path=None):
        """"""
        return object
    
    def set_attribute(self, attribute=None, type=None, value_p=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attributes_async(self, info=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def set_attributes_finish(self, result=None, info=None):
        """"""
        return object
    
    def set_attributes_from_info(self, info=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_display_name(self, display_name=None, cancellable=None):
        """"""
        return object
    
    def set_display_name_async(self, display_name=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def set_display_name_finish(self, res=None):
        """"""
        return object
    
    def start_mountable(self, flags=None, start_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def start_mountable_finish(self, result=None):
        """"""
        return object
    
    def stop_mountable(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def stop_mountable_finish(self, result=None):
        """"""
        return object
    
    def trash(self, cancellable=None):
        """"""
        return object
    
    def trash_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def trash_finish(self, result=None):
        """"""
        return object
    
    def unmount_mountable(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_mountable_finish(self, result=None):
        """"""
        return object
    
    def unmount_mountable_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_mountable_with_operation_finish(self, result=None):
        """"""
        return object
    
    def append_to(self, flags=None, cancellable=None):
        """"""
        return object
    
    def append_to_async(self, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def append_to_finish(self, res=None):
        """"""
        return object
    
    def copy(self, destination=None, flags=None, cancellable=None, progress_callback=None, progress_callback_data=None):
        """"""
        return object
    
    def copy_async(self, destination=None, flags=None, io_priority=None, cancellable=None, progress_callback=None, progress_callback_data=None, callback=None, user_data=None):
        """"""
        return object
    
    def copy_attributes(self, destination=None, flags=None, cancellable=None):
        """"""
        return object
    
    def copy_finish(self, res=None):
        """"""
        return object
    
    def create(self, flags=None, cancellable=None):
        """"""
        return object
    
    def create_async(self, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def create_finish(self, res=None):
        """"""
        return object
    
    def create_readwrite(self, flags=None, cancellable=None):
        """"""
        return object
    
    def create_readwrite_async(self, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def create_readwrite_finish(self, res=None):
        """"""
        return object
    
    def delete(self, cancellable=None):
        """"""
        return object
    
    def delete_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def delete_finish(self, result=None):
        """"""
        return object
    
    def dup(self):
        """"""
        return object
    
    def eject_mountable(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_mountable_finish(self, result=None):
        """"""
        return object
    
    def eject_mountable_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_mountable_with_operation_finish(self, result=None):
        """"""
        return object
    
    def enumerate_children(self, attributes=None, flags=None, cancellable=None):
        """"""
        return object
    
    def enumerate_children_async(self, attributes=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def enumerate_children_finish(self, res=None):
        """"""
        return object
    
    def equal(self, file2=None):
        """"""
        return object
    
    def find_enclosing_mount(self, cancellable=None):
        """"""
        return object
    
    def find_enclosing_mount_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def find_enclosing_mount_finish(self, res=None):
        """"""
        return object
    
    def get_basename(self):
        """"""
        return object
    
    def get_child(self, name=None):
        """"""
        return object
    
    def get_child_for_display_name(self, display_name=None):
        """"""
        return object
    
    def get_parent(self):
        """"""
        return object
    
    def get_parse_name(self):
        """"""
        return object
    
    def get_path(self):
        """"""
        return object
    
    def get_relative_path(self, descendant=None):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_uri_scheme(self):
        """"""
        return object
    
    def has_parent(self, parent=None):
        """"""
        return object
    
    def has_prefix(self, prefix=None):
        """"""
        return object
    
    def has_uri_scheme(self, uri_scheme=None):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def is_native(self):
        """"""
        return object
    
    def load_bytes(self, cancellable=None, etag_out=None):
        """"""
        return object
    
    def load_bytes_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def load_bytes_finish(self, result=None, etag_out=None):
        """"""
        return object
    
    def load_contents(self, cancellable=None, contents=None, length=None, etag_out=None):
        """"""
        return object
    
    def load_contents_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def load_contents_finish(self, res=None, contents=None, length=None, etag_out=None):
        """"""
        return object
    
    def load_partial_contents_async(self, cancellable=None, read_more_callback=None, callback=None, user_data=None):
        """"""
        return object
    
    def load_partial_contents_finish(self, res=None, contents=None, length=None, etag_out=None):
        """"""
        return object
    
    def make_directory(self, cancellable=None):
        """"""
        return object
    
    def make_directory_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def make_directory_finish(self, result=None):
        """"""
        return object
    
    def make_directory_with_parents(self, cancellable=None):
        """"""
        return object
    
    def make_symbolic_link(self, symlink_value=None, cancellable=None):
        """"""
        return object
    
    def measure_disk_usage(self, flags=None, cancellable=None, progress_callback=None, progress_data=None, disk_usage=None, num_dirs=None, num_files=None):
        """"""
        return object
    
    def measure_disk_usage_async(self, flags=None, io_priority=None, cancellable=None, progress_callback=None, progress_data=None, callback=None, user_data=None):
        """"""
        return object
    
    def measure_disk_usage_finish(self, result=None, disk_usage=None, num_dirs=None, num_files=None):
        """"""
        return object
    
    def monitor(self, flags=None, cancellable=None):
        """"""
        return object
    
    def monitor_directory(self, flags=None, cancellable=None):
        """"""
        return object
    
    def monitor_file(self, flags=None, cancellable=None):
        """"""
        return object
    
    def mount_enclosing_volume(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def mount_enclosing_volume_finish(self, result=None):
        """"""
        return object
    
    def mount_mountable(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def mount_mountable_finish(self, result=None):
        """"""
        return object
    
    def move(self, destination=None, flags=None, cancellable=None, progress_callback=None, progress_callback_data=None):
        """"""
        return object
    
    def open_readwrite(self, cancellable=None):
        """"""
        return object
    
    def open_readwrite_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def open_readwrite_finish(self, res=None):
        """"""
        return object
    
    def peek_path(self):
        """"""
        return object
    
    def poll_mountable(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def poll_mountable_finish(self, result=None):
        """"""
        return object
    
    def query_default_handler(self, cancellable=None):
        """"""
        return object
    
    def query_exists(self, cancellable=None):
        """"""
        return object
    
    def query_file_type(self, flags=None, cancellable=None):
        """"""
        return object
    
    def query_filesystem_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_filesystem_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_filesystem_info_finish(self, res=None):
        """"""
        return object
    
    def query_info(self, attributes=None, flags=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, res=None):
        """"""
        return object
    
    def query_settable_attributes(self, cancellable=None):
        """"""
        return object
    
    def query_writable_namespaces(self, cancellable=None):
        """"""
        return object
    
    def read(self, cancellable=None):
        """"""
        return object
    
    def read_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_finish(self, res=None):
        """"""
        return object
    
    def replace(self, etag=None, make_backup=None, flags=None, cancellable=None):
        """"""
        return object
    
    def replace_async(self, etag=None, make_backup=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def replace_contents(self, contents=None, length=None, etag=None, make_backup=None, flags=None, new_etag=None, cancellable=None):
        """"""
        return object
    
    def replace_contents_async(self, contents=None, length=None, etag=None, make_backup=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def replace_contents_bytes_async(self, contents=None, etag=None, make_backup=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def replace_contents_finish(self, res=None, new_etag=None):
        """"""
        return object
    
    def replace_finish(self, res=None):
        """"""
        return object
    
    def replace_readwrite(self, etag=None, make_backup=None, flags=None, cancellable=None):
        """"""
        return object
    
    def replace_readwrite_async(self, etag=None, make_backup=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def replace_readwrite_finish(self, res=None):
        """"""
        return object
    
    def resolve_relative_path(self, relative_path=None):
        """"""
        return object
    
    def set_attribute(self, attribute=None, type=None, value_p=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attribute_byte_string(self, attribute=None, value=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attribute_int32(self, attribute=None, value=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attribute_int64(self, attribute=None, value=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attribute_string(self, attribute=None, value=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attribute_uint32(self, attribute=None, value=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attribute_uint64(self, attribute=None, value=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_attributes_async(self, info=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def set_attributes_finish(self, result=None, info=None):
        """"""
        return object
    
    def set_attributes_from_info(self, info=None, flags=None, cancellable=None):
        """"""
        return object
    
    def set_display_name(self, display_name=None, cancellable=None):
        """"""
        return object
    
    def set_display_name_async(self, display_name=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def set_display_name_finish(self, res=None):
        """"""
        return object
    
    def start_mountable(self, flags=None, start_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def start_mountable_finish(self, result=None):
        """"""
        return object
    
    def stop_mountable(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def stop_mountable_finish(self, result=None):
        """"""
        return object
    
    def supports_thread_contexts(self):
        """"""
        return object
    
    def trash(self, cancellable=None):
        """"""
        return object
    
    def trash_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def trash_finish(self, result=None):
        """"""
        return object
    
    def unmount_mountable(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_mountable_finish(self, result=None):
        """"""
        return object
    
    def unmount_mountable_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_mountable_with_operation_finish(self, result=None):
        """"""
        return object


class FileAttributeInfo():
    """"""

    @property
    def name(self):
        return object

    @property
    def type(self):
        return object

    @property
    def flags(self):
        return object


class FileAttributeInfoList():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def add(self, name=None, type=None, flags=None):
        """"""
        return object
    
    def dup(self):
        """"""
        return object
    
    def lookup(self, name=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def infos(self):
        return object

    @property
    def n_infos(self):
        return object


class FileAttributeMatcher():
    """"""
    
    def __init__(self, attributes=None):
        """"""
        return object
    @staticmethod
    def new(attributes=None):
        """"""
        return object
    
    def enumerate_namespace(self, ns=None):
        """"""
        return object
    
    def enumerate_next(self):
        """"""
        return object
    
    def matches(self, attribute=None):
        """"""
        return object
    
    def matches_only(self, attribute=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def subtract(self, subtract=None):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class FileDescriptorBased():
    """"""
    
    def get_fd(self):
        """"""
        return object
    
    def get_fd(self):
        """"""
        return object


class FileDescriptorBasedIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def get_fd(self):
        return object


class FileEnumerator(GObject.Object):
    """"""
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def close_fn(self, cancellable=None):
        """"""
        return object
    
    def next_file(self, cancellable=None):
        """"""
        return object
    
    def next_files_async(self, num_files=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def next_files_finish(self, result=None):
        """"""
        return object
    
    def close(self, cancellable=None):
        """"""
        return object
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def get_child(self, info=None):
        """"""
        return object
    
    def get_container(self):
        """"""
        return object
    
    def has_pending(self):
        """"""
        return object
    
    def is_closed(self):
        """"""
        return object
    
    def iterate(self, out_info=None, out_child=None, cancellable=None):
        """"""
        return object
    
    def next_file(self, cancellable=None):
        """"""
        return object
    
    def next_files_async(self, num_files=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def next_files_finish(self, result=None):
        """"""
        return object
    
    def set_pending(self, pending=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class FileEnumeratorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def next_file(self):
        return object

    @property
    def close_fn(self):
        return object

    @property
    def next_files_async(self):
        return object

    @property
    def next_files_finish(self):
        return object

    @property
    def close_async(self):
        return object

    @property
    def close_finish(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object

    @property
    def _g_reserved7(self):
        return object


class FileEnumeratorPrivate():
    """"""


class FileIOStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def tell(self):
        return object

    @property
    def can_seek(self):
        return object

    @property
    def seek(self):
        return object

    @property
    def can_truncate(self):
        return object

    @property
    def truncate_fn(self):
        return object

    @property
    def query_info(self):
        return object

    @property
    def query_info_async(self):
        return object

    @property
    def query_info_finish(self):
        return object

    @property
    def get_etag(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class FileIOStreamPrivate():
    """"""


class FileIconClass():
    """"""


class FileIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def dup(self):
        return object

    @property
    def hash(self):
        return object

    @property
    def equal(self):
        return object

    @property
    def is_native(self):
        return object

    @property
    def has_uri_scheme(self):
        return object

    @property
    def get_uri_scheme(self):
        return object

    @property
    def get_basename(self):
        return object

    @property
    def get_path(self):
        return object

    @property
    def get_uri(self):
        return object

    @property
    def get_parse_name(self):
        return object

    @property
    def get_parent(self):
        return object

    @property
    def prefix_matches(self):
        return object

    @property
    def get_relative_path(self):
        return object

    @property
    def resolve_relative_path(self):
        return object

    @property
    def get_child_for_display_name(self):
        return object

    @property
    def enumerate_children(self):
        return object

    @property
    def enumerate_children_async(self):
        return object

    @property
    def enumerate_children_finish(self):
        return object

    @property
    def query_info(self):
        return object

    @property
    def query_info_async(self):
        return object

    @property
    def query_info_finish(self):
        return object

    @property
    def query_filesystem_info(self):
        return object

    @property
    def query_filesystem_info_async(self):
        return object

    @property
    def query_filesystem_info_finish(self):
        return object

    @property
    def find_enclosing_mount(self):
        return object

    @property
    def find_enclosing_mount_async(self):
        return object

    @property
    def find_enclosing_mount_finish(self):
        return object

    @property
    def set_display_name(self):
        return object

    @property
    def set_display_name_async(self):
        return object

    @property
    def set_display_name_finish(self):
        return object

    @property
    def query_settable_attributes(self):
        return object

    @property
    def _query_settable_attributes_async(self):
        return object

    @property
    def _query_settable_attributes_finish(self):
        return object

    @property
    def query_writable_namespaces(self):
        return object

    @property
    def _query_writable_namespaces_async(self):
        return object

    @property
    def _query_writable_namespaces_finish(self):
        return object

    @property
    def set_attribute(self):
        return object

    @property
    def set_attributes_from_info(self):
        return object

    @property
    def set_attributes_async(self):
        return object

    @property
    def set_attributes_finish(self):
        return object

    @property
    def read_fn(self):
        return object

    @property
    def read_async(self):
        return object

    @property
    def read_finish(self):
        return object

    @property
    def append_to(self):
        return object

    @property
    def append_to_async(self):
        return object

    @property
    def append_to_finish(self):
        return object

    @property
    def create(self):
        return object

    @property
    def create_async(self):
        return object

    @property
    def create_finish(self):
        return object

    @property
    def replace(self):
        return object

    @property
    def replace_async(self):
        return object

    @property
    def replace_finish(self):
        return object

    @property
    def delete_file(self):
        return object

    @property
    def delete_file_async(self):
        return object

    @property
    def delete_file_finish(self):
        return object

    @property
    def trash(self):
        return object

    @property
    def trash_async(self):
        return object

    @property
    def trash_finish(self):
        return object

    @property
    def make_directory(self):
        return object

    @property
    def make_directory_async(self):
        return object

    @property
    def make_directory_finish(self):
        return object

    @property
    def make_symbolic_link(self):
        return object

    @property
    def _make_symbolic_link_async(self):
        return object

    @property
    def _make_symbolic_link_finish(self):
        return object

    @property
    def copy(self):
        return object

    @property
    def copy_async(self):
        return object

    @property
    def copy_finish(self):
        return object

    @property
    def move(self):
        return object

    @property
    def _move_async(self):
        return object

    @property
    def _move_finish(self):
        return object

    @property
    def mount_mountable(self):
        return object

    @property
    def mount_mountable_finish(self):
        return object

    @property
    def unmount_mountable(self):
        return object

    @property
    def unmount_mountable_finish(self):
        return object

    @property
    def eject_mountable(self):
        return object

    @property
    def eject_mountable_finish(self):
        return object

    @property
    def mount_enclosing_volume(self):
        return object

    @property
    def mount_enclosing_volume_finish(self):
        return object

    @property
    def monitor_dir(self):
        return object

    @property
    def monitor_file(self):
        return object

    @property
    def open_readwrite(self):
        return object

    @property
    def open_readwrite_async(self):
        return object

    @property
    def open_readwrite_finish(self):
        return object

    @property
    def create_readwrite(self):
        return object

    @property
    def create_readwrite_async(self):
        return object

    @property
    def create_readwrite_finish(self):
        return object

    @property
    def replace_readwrite(self):
        return object

    @property
    def replace_readwrite_async(self):
        return object

    @property
    def replace_readwrite_finish(self):
        return object

    @property
    def start_mountable(self):
        return object

    @property
    def start_mountable_finish(self):
        return object

    @property
    def stop_mountable(self):
        return object

    @property
    def stop_mountable_finish(self):
        return object

    @property
    def supports_thread_contexts(self):
        return object

    @property
    def unmount_mountable_with_operation(self):
        return object

    @property
    def unmount_mountable_with_operation_finish(self):
        return object

    @property
    def eject_mountable_with_operation(self):
        return object

    @property
    def eject_mountable_with_operation_finish(self):
        return object

    @property
    def poll_mountable(self):
        return object

    @property
    def poll_mountable_finish(self):
        return object

    @property
    def measure_disk_usage(self):
        return object

    @property
    def measure_disk_usage_async(self):
        return object

    @property
    def measure_disk_usage_finish(self):
        return object


class FileInfo(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def clear_status(self):
        """"""
        return object
    
    def copy_into(self, dest_info=None):
        """"""
        return object
    
    def dup(self):
        """"""
        return object
    
    def get_attribute_as_string(self, attribute=None):
        """"""
        return object
    
    def get_attribute_boolean(self, attribute=None):
        """"""
        return object
    
    def get_attribute_byte_string(self, attribute=None):
        """"""
        return object
    
    def get_attribute_data(self, attribute=None, type=None, value_pp=None, status=None):
        """"""
        return object
    
    def get_attribute_int32(self, attribute=None):
        """"""
        return object
    
    def get_attribute_int64(self, attribute=None):
        """"""
        return object
    
    def get_attribute_object(self, attribute=None):
        """"""
        return object
    
    def get_attribute_status(self, attribute=None):
        """"""
        return object
    
    def get_attribute_string(self, attribute=None):
        """"""
        return object
    
    def get_attribute_stringv(self, attribute=None):
        """"""
        return object
    
    def get_attribute_type(self, attribute=None):
        """"""
        return object
    
    def get_attribute_uint32(self, attribute=None):
        """"""
        return object
    
    def get_attribute_uint64(self, attribute=None):
        """"""
        return object
    
    def get_content_type(self):
        """"""
        return object
    
    def get_deletion_date(self):
        """"""
        return object
    
    def get_display_name(self):
        """"""
        return object
    
    def get_edit_name(self):
        """"""
        return object
    
    def get_etag(self):
        """"""
        return object
    
    def get_file_type(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_is_backup(self):
        """"""
        return object
    
    def get_is_hidden(self):
        """"""
        return object
    
    def get_is_symlink(self):
        """"""
        return object
    
    def get_modification_time(self, result=None):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def get_sort_order(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_symlink_target(self):
        """"""
        return object
    
    def has_attribute(self, attribute=None):
        """"""
        return object
    
    def has_namespace(self, name_space=None):
        """"""
        return object
    
    def list_attributes(self, name_space=None):
        """"""
        return object
    
    def remove_attribute(self, attribute=None):
        """"""
        return object
    
    def set_attribute(self, attribute=None, type=None, value_p=None):
        """"""
        return object
    
    def set_attribute_boolean(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_byte_string(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_int32(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_int64(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_mask(self, mask=None):
        """"""
        return object
    
    def set_attribute_object(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_status(self, attribute=None, status=None):
        """"""
        return object
    
    def set_attribute_string(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_stringv(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_uint32(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_attribute_uint64(self, attribute=None, attr_value=None):
        """"""
        return object
    
    def set_content_type(self, content_type=None):
        """"""
        return object
    
    def set_display_name(self, display_name=None):
        """"""
        return object
    
    def set_edit_name(self, edit_name=None):
        """"""
        return object
    
    def set_file_type(self, type=None):
        """"""
        return object
    
    def set_icon(self, icon=None):
        """"""
        return object
    
    def set_is_hidden(self, is_hidden=None):
        """"""
        return object
    
    def set_is_symlink(self, is_symlink=None):
        """"""
        return object
    
    def set_modification_time(self, mtime=None):
        """"""
        return object
    
    def set_name(self, name=None):
        """"""
        return object
    
    def set_size(self, size=None):
        """"""
        return object
    
    def set_sort_order(self, sort_order=None):
        """"""
        return object
    
    def set_symbolic_icon(self, icon=None):
        """"""
        return object
    
    def set_symlink_target(self, symlink_target=None):
        """"""
        return object
    
    def unset_attribute_mask(self):
        """"""
        return object


class FileInfoClass():
    """"""


class FileInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def tell(self):
        return object

    @property
    def can_seek(self):
        return object

    @property
    def seek(self):
        return object

    @property
    def query_info(self):
        return object

    @property
    def query_info_async(self):
        return object

    @property
    def query_info_finish(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class FileInputStreamPrivate():
    """"""


class FileMonitor(GObject.Object):
    """"""
    
    def cancel(self):
        """"""
        return object
    
    def changed(self, file=None, other_file=None, event_type=None):
        """"""
        return object
    
    def cancel(self):
        """"""
        return object
    
    def emit_event(self, child=None, other_file=None, event_type=None):
        """"""
        return object
    
    def is_cancelled(self):
        """"""
        return object
    
    def set_rate_limit(self, limit_msecs=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class FileMonitorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def changed(self):
        return object

    @property
    def cancel(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class FileMonitorPrivate():
    """"""


class FileOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def tell(self):
        return object

    @property
    def can_seek(self):
        return object

    @property
    def seek(self):
        return object

    @property
    def can_truncate(self):
        return object

    @property
    def truncate_fn(self):
        return object

    @property
    def query_info(self):
        return object

    @property
    def query_info_async(self):
        return object

    @property
    def query_info_finish(self):
        return object

    @property
    def get_etag(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class FileOutputStreamPrivate():
    """"""


class FilenameCompleter(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def got_completion_data(self):
        """"""
        return object
    
    def get_completion_suffix(self, initial_text=None):
        """"""
        return object
    
    def get_completions(self, initial_text=None):
        """"""
        return object
    
    def set_dirs_only(self, dirs_only=None):
        """"""
        return object


class FilenameCompleterClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def got_completion_data(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object


class FilterInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object


class FilterOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object


class IOExtension():
    """"""
    
    def get_name(self):
        """"""
        return object
    
    def get_priority(self):
        """"""
        return object
    
    def get_type(self):
        """"""
        return object
    
    def ref_class(self):
        """"""
        return object


class IOExtensionPoint():
    """"""
    
    def get_extension_by_name(self, name=None):
        """"""
        return object
    
    def get_extensions(self):
        """"""
        return object
    
    def get_required_type(self):
        """"""
        return object
    
    def set_required_type(self, type=None):
        """"""
        return object
    @staticmethod
    def implement(extension_point_name=None, type=None, extension_name=None, priority=None):
        """"""
        return object
    @staticmethod
    def lookup(name=None):
        """"""
        return object
    @staticmethod
    def register(name=None):
        """"""
        return object


class IOModule(GObject.TypeModule, GObject.TypePlugin):
    """"""
    
    def __init__(self, filename=None):
        """"""
        return object
    @staticmethod
    def new(filename=None):
        """"""
        return object
    @staticmethod
    def query():
        """"""
        return object
    
    def load(self):
        """"""
        return object
    
    def unload(self):
        """"""
        return object


class IOModuleClass():
    """"""


class IOModuleScope():
    """"""
    
    def block(self, basename=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    @staticmethod
    def new(flags=None):
        """"""
        return object


class IOSchedulerJob():
    """"""
    
    def send_to_mainloop(self, func=None, user_data=None, notify=None):
        """"""
        return object
    
    def send_to_mainloop_async(self, func=None, user_data=None, notify=None):
        """"""
        return object


class IOStream(GObject.Object):
    """"""
    @staticmethod
    def splice_finish(result=None):
        """"""
        return object
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def close_fn(self, cancellable=None):
        """"""
        return object
    
    def get_input_stream(self):
        """"""
        return object
    
    def get_output_stream(self):
        """"""
        return object
    
    def clear_pending(self):
        """"""
        return object
    
    def close(self, cancellable=None):
        """"""
        return object
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def get_input_stream(self):
        """"""
        return object
    
    def get_output_stream(self):
        """"""
        return object
    
    def has_pending(self):
        """"""
        return object
    
    def is_closed(self):
        """"""
        return object
    
    def set_pending(self):
        """"""
        return object
    
    def splice_async(self, stream2=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class IOStreamAdapter():
    """"""


class IOStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_input_stream(self):
        return object

    @property
    def get_output_stream(self):
        return object

    @property
    def close_fn(self):
        return object

    @property
    def close_async(self):
        return object

    @property
    def close_finish(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object

    @property
    def _g_reserved7(self):
        return object

    @property
    def _g_reserved8(self):
        return object

    @property
    def _g_reserved9(self):
        return object

    @property
    def _g_reserved10(self):
        return object


class IOStreamPrivate():
    """"""


class Icon():
    """"""
    @staticmethod
    def deserialize(value=None):
        """"""
        return object
    @staticmethod
    def hash(icon=None):
        """"""
        return object
    @staticmethod
    def new_for_string(str=None):
        """"""
        return object
    
    def equal(self, icon2=None):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def serialize(self):
        """"""
        return object
    
    def to_tokens(self, tokens=None, out_version=None):
        """"""
        return object
    
    def equal(self, icon2=None):
        """"""
        return object
    
    def serialize(self):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object


class IconIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def hash(self):
        return object

    @property
    def equal(self):
        return object

    @property
    def to_tokens(self):
        return object

    @property
    def from_tokens(self):
        return object

    @property
    def serialize(self):
        return object


class InetAddress(GObject.Object):
    """"""
    @staticmethod
    def new_any(family=None):
        """"""
        return object
    @staticmethod
    def new_from_bytes(bytes=None, family=None):
        """"""
        return object
    @staticmethod
    def new_from_string(string=None):
        """"""
        return object
    @staticmethod
    def new_loopback(family=None):
        """"""
        return object
    
    def to_bytes(self):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object
    
    def equal(self, other_address=None):
        """"""
        return object
    
    def get_family(self):
        """"""
        return object
    
    def get_is_any(self):
        """"""
        return object
    
    def get_is_link_local(self):
        """"""
        return object
    
    def get_is_loopback(self):
        """"""
        return object
    
    def get_is_mc_global(self):
        """"""
        return object
    
    def get_is_mc_link_local(self):
        """"""
        return object
    
    def get_is_mc_node_local(self):
        """"""
        return object
    
    def get_is_mc_org_local(self):
        """"""
        return object
    
    def get_is_mc_site_local(self):
        """"""
        return object
    
    def get_is_multicast(self):
        """"""
        return object
    
    def get_is_site_local(self):
        """"""
        return object
    
    def get_native_size(self):
        """"""
        return object
    
    def to_bytes(self):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class InetAddressClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def to_string(self):
        return object

    @property
    def to_bytes(self):
        return object


class InetAddressMaskClass():
    """"""

    @property
    def parent_class(self):
        return object


class InetAddressMaskPrivate():
    """"""


class InetAddressPrivate():
    """"""


class InetSocketAddressClass():
    """"""

    @property
    def parent_class(self):
        return object


class InetSocketAddressPrivate():
    """"""


class Initable():
    """"""
    @staticmethod
    def new(object_type=None, cancellable=None, error=None, first_property_name=None, *args):
        """"""
        return object
    @staticmethod
    def new_valist(object_type=None, first_property_name=None, var_args=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def newv(object_type=None, n_parameters=None, parameters=None, cancellable=None):
        """"""
        return object
    
    def init(self, cancellable=None):
        """"""
        return object
    
    def init(self, cancellable=None):
        """"""
        return object


class InitableIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def init(self):
        return object


class InputMessage():
    """"""

    @property
    def address(self):
        return object

    @property
    def vectors(self):
        return object

    @property
    def num_vectors(self):
        return object

    @property
    def bytes_received(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def control_messages(self):
        return object

    @property
    def num_control_messages(self):
        return object


class InputStream(GObject.Object):
    """"""
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def close_fn(self, cancellable=None):
        """"""
        return object
    
    def read_async(self, buffer=None, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_finish(self, result=None):
        """"""
        return object
    
    def read_fn(self, buffer=None, count=None, cancellable=None):
        """"""
        return object
    
    def skip(self, count=None, cancellable=None):
        """"""
        return object
    
    def skip_async(self, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def skip_finish(self, result=None):
        """"""
        return object
    
    def clear_pending(self):
        """"""
        return object
    
    def close(self, cancellable=None):
        """"""
        return object
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def has_pending(self):
        """"""
        return object
    
    def is_closed(self):
        """"""
        return object
    
    def read(self, buffer=None, count=None, cancellable=None):
        """"""
        return object
    
    def read_all(self, buffer=None, count=None, bytes_read=None, cancellable=None):
        """"""
        return object
    
    def read_all_async(self, buffer=None, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_all_finish(self, result=None, bytes_read=None):
        """"""
        return object
    
    def read_async(self, buffer=None, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_bytes(self, count=None, cancellable=None):
        """"""
        return object
    
    def read_bytes_async(self, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_bytes_finish(self, result=None):
        """"""
        return object
    
    def read_finish(self, result=None):
        """"""
        return object
    
    def set_pending(self):
        """"""
        return object
    
    def skip(self, count=None, cancellable=None):
        """"""
        return object
    
    def skip_async(self, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def skip_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class InputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def read_fn(self):
        return object

    @property
    def skip(self):
        return object

    @property
    def close_fn(self):
        return object

    @property
    def read_async(self):
        return object

    @property
    def read_finish(self):
        return object

    @property
    def skip_async(self):
        return object

    @property
    def skip_finish(self):
        return object

    @property
    def close_async(self):
        return object

    @property
    def close_finish(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class InputStreamPrivate():
    """"""


class InputVector():
    """"""

    @property
    def buffer(self):
        return object

    @property
    def size(self):
        return object


class ListModel():
    """"""
    
    def get_item(self, position=None):
        """"""
        return object
    
    def get_item_type(self):
        """"""
        return object
    
    def get_n_items(self):
        """"""
        return object
    
    def get_item(self, position=None):
        """"""
        return object
    
    def get_item_type(self):
        """"""
        return object
    
    def get_n_items(self):
        """"""
        return object
    
    def get_object(self, position=None):
        """"""
        return object
    
    def items_changed(self, position=None, removed=None, added=None):
        """"""
        return object


class ListModelInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def get_item_type(self):
        return object

    @property
    def get_n_items(self):
        return object

    @property
    def get_item(self):
        return object


class ListStore(GObject.Object, ListModel):
    """"""
    
    def __init__(self, item_type=None):
        """"""
        return object
    @staticmethod
    def new(item_type=None):
        """"""
        return object
    
    def append(self, item=None):
        """"""
        return object
    
    def insert(self, position=None, item=None):
        """"""
        return object
    
    def insert_sorted(self, item=None, compare_func=None, user_data=None):
        """"""
        return object
    
    def remove(self, position=None):
        """"""
        return object
    
    def remove_all(self):
        """"""
        return object
    
    def sort(self, compare_func=None, user_data=None):
        """"""
        return object
    
    def splice(self, position=None, n_removals=None, additions=None, n_additions=None):
        """"""
        return object


class ListStoreClass():
    """"""

    @property
    def parent_class(self):
        return object


class LoadableIcon():
    """"""
    
    def load(self, size=None, type=None, cancellable=None):
        """"""
        return object
    
    def load_async(self, size=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def load_finish(self, res=None, type=None):
        """"""
        return object
    
    def load(self, size=None, type=None, cancellable=None):
        """"""
        return object
    
    def load_async(self, size=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def load_finish(self, res=None, type=None):
        """"""
        return object


class LoadableIconIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def load(self):
        return object

    @property
    def load_async(self):
        return object

    @property
    def load_finish(self):
        return object


class MemoryInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class MemoryInputStreamPrivate():
    """"""


class MemoryOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class MemoryOutputStreamPrivate():
    """"""


class MenuAttributeIter(GObject.Object):
    """"""
    
    def get_next(self, out_name=None, value=None):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_next(self, out_name=None, value=None):
        """"""
        return object
    
    def get_value(self):
        """"""
        return object
    
    def next(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class MenuAttributeIterClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_next(self):
        return object


class MenuAttributeIterPrivate():
    """"""


class MenuItem(GObject.Object):
    """"""
    
    def __init__(self, label=None, detailed_action=None):
        """"""
        return object
    @staticmethod
    def new(label=None, detailed_action=None):
        """"""
        return object
    @staticmethod
    def new_from_model(model=None, item_index=None):
        """"""
        return object
    @staticmethod
    def new_section(label=None, section=None):
        """"""
        return object
    @staticmethod
    def new_submenu(label=None, submenu=None):
        """"""
        return object
    
    def get_attribute(self, attribute=None, format_string=None, *args):
        """"""
        return object
    
    def get_attribute_value(self, attribute=None, expected_type=None):
        """"""
        return object
    
    def get_link(self, link=None):
        """"""
        return object
    
    def set_action_and_target(self, action=None, format_string=None, *args):
        """"""
        return object
    
    def set_action_and_target_value(self, action=None, target_value=None):
        """"""
        return object
    
    def set_attribute(self, attribute=None, format_string=None, *args):
        """"""
        return object
    
    def set_attribute_value(self, attribute=None, value=None):
        """"""
        return object
    
    def set_detailed_action(self, detailed_action=None):
        """"""
        return object
    
    def set_icon(self, icon=None):
        """"""
        return object
    
    def set_label(self, label=None):
        """"""
        return object
    
    def set_link(self, link=None, model=None):
        """"""
        return object
    
    def set_section(self, section=None):
        """"""
        return object
    
    def set_submenu(self, submenu=None):
        """"""
        return object


class MenuLinkIter(GObject.Object):
    """"""
    
    def get_next(self, out_link=None, value=None):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_next(self, out_link=None, value=None):
        """"""
        return object
    
    def get_value(self):
        """"""
        return object
    
    def next(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class MenuLinkIterClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_next(self):
        return object


class MenuLinkIterPrivate():
    """"""


class MenuModel(GObject.Object):
    """"""
    
    def get_item_attribute_value(self, item_index=None, attribute=None, expected_type=None):
        """"""
        return object
    
    def get_item_attributes(self, item_index=None, attributes=None):
        """"""
        return object
    
    def get_item_link(self, item_index=None, link=None):
        """"""
        return object
    
    def get_item_links(self, item_index=None, links=None):
        """"""
        return object
    
    def get_n_items(self):
        """"""
        return object
    
    def is_mutable(self):
        """"""
        return object
    
    def iterate_item_attributes(self, item_index=None):
        """"""
        return object
    
    def iterate_item_links(self, item_index=None):
        """"""
        return object
    
    def get_item_attribute(self, item_index=None, attribute=None, format_string=None, *args):
        """"""
        return object
    
    def get_item_attribute_value(self, item_index=None, attribute=None, expected_type=None):
        """"""
        return object
    
    def get_item_link(self, item_index=None, link=None):
        """"""
        return object
    
    def get_n_items(self):
        """"""
        return object
    
    def is_mutable(self):
        """"""
        return object
    
    def items_changed(self, position=None, removed=None, added=None):
        """"""
        return object
    
    def iterate_item_attributes(self, item_index=None):
        """"""
        return object
    
    def iterate_item_links(self, item_index=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class MenuModelClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def is_mutable(self):
        return object

    @property
    def get_n_items(self):
        return object

    @property
    def get_item_attributes(self):
        return object

    @property
    def iterate_item_attributes(self):
        return object

    @property
    def get_item_attribute_value(self):
        return object

    @property
    def get_item_links(self):
        return object

    @property
    def iterate_item_links(self):
        return object

    @property
    def get_item_link(self):
        return object


class MenuModelPrivate():
    """"""


class Mount():
    """"""
    
    def can_eject(self):
        """"""
        return object
    
    def can_unmount(self):
        """"""
        return object
    
    def changed(self):
        """"""
        return object
    
    def eject(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_finish(self, result=None):
        """"""
        return object
    
    def eject_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_with_operation_finish(self, result=None):
        """"""
        return object
    
    def get_default_location(self):
        """"""
        return object
    
    def get_drive(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_root(self):
        """"""
        return object
    
    def get_sort_key(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_uuid(self):
        """"""
        return object
    
    def get_volume(self):
        """"""
        return object
    
    def guess_content_type(self, force_rescan=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def guess_content_type_finish(self, result=None):
        """"""
        return object
    
    def guess_content_type_sync(self, force_rescan=None, cancellable=None):
        """"""
        return object
    
    def pre_unmount(self):
        """"""
        return object
    
    def remount(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def remount_finish(self, result=None):
        """"""
        return object
    
    def unmount(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_finish(self, result=None):
        """"""
        return object
    
    def unmount_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_with_operation_finish(self, result=None):
        """"""
        return object
    
    def unmounted(self):
        """"""
        return object
    
    def can_eject(self):
        """"""
        return object
    
    def can_unmount(self):
        """"""
        return object
    
    def eject(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_finish(self, result=None):
        """"""
        return object
    
    def eject_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_with_operation_finish(self, result=None):
        """"""
        return object
    
    def get_default_location(self):
        """"""
        return object
    
    def get_drive(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_root(self):
        """"""
        return object
    
    def get_sort_key(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_uuid(self):
        """"""
        return object
    
    def get_volume(self):
        """"""
        return object
    
    def guess_content_type(self, force_rescan=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def guess_content_type_finish(self, result=None):
        """"""
        return object
    
    def guess_content_type_sync(self, force_rescan=None, cancellable=None):
        """"""
        return object
    
    def is_shadowed(self):
        """"""
        return object
    
    def remount(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def remount_finish(self, result=None):
        """"""
        return object
    
    def shadow(self):
        """"""
        return object
    
    def unmount(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_finish(self, result=None):
        """"""
        return object
    
    def unmount_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def unmount_with_operation_finish(self, result=None):
        """"""
        return object
    
    def unshadow(self):
        """"""
        return object


class MountIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def changed(self):
        return object

    @property
    def unmounted(self):
        return object

    @property
    def get_root(self):
        return object

    @property
    def get_name(self):
        return object

    @property
    def get_icon(self):
        return object

    @property
    def get_uuid(self):
        return object

    @property
    def get_volume(self):
        return object

    @property
    def get_drive(self):
        return object

    @property
    def can_unmount(self):
        return object

    @property
    def can_eject(self):
        return object

    @property
    def unmount(self):
        return object

    @property
    def unmount_finish(self):
        return object

    @property
    def eject(self):
        return object

    @property
    def eject_finish(self):
        return object

    @property
    def remount(self):
        return object

    @property
    def remount_finish(self):
        return object

    @property
    def guess_content_type(self):
        return object

    @property
    def guess_content_type_finish(self):
        return object

    @property
    def guess_content_type_sync(self):
        return object

    @property
    def pre_unmount(self):
        return object

    @property
    def unmount_with_operation(self):
        return object

    @property
    def unmount_with_operation_finish(self):
        return object

    @property
    def eject_with_operation(self):
        return object

    @property
    def eject_with_operation_finish(self):
        return object

    @property
    def get_default_location(self):
        return object

    @property
    def get_sort_key(self):
        return object

    @property
    def get_symbolic_icon(self):
        return object


class MountOperation(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def aborted(self):
        """"""
        return object
    
    def ask_password(self, message=None, default_user=None, default_domain=None, flags=None):
        """"""
        return object
    
    def ask_question(self, message=None, choices=None):
        """"""
        return object
    
    def reply(self, result=None):
        """"""
        return object
    
    def show_processes(self, message=None, processes=None, choices=None):
        """"""
        return object
    
    def show_unmount_progress(self, message=None, time_left=None, bytes_left=None):
        """"""
        return object
    
    def get_anonymous(self):
        """"""
        return object
    
    def get_choice(self):
        """"""
        return object
    
    def get_domain(self):
        """"""
        return object
    
    def get_password(self):
        """"""
        return object
    
    def get_password_save(self):
        """"""
        return object
    
    def get_username(self):
        """"""
        return object
    
    def reply(self, result=None):
        """"""
        return object
    
    def set_anonymous(self, anonymous=None):
        """"""
        return object
    
    def set_choice(self, choice=None):
        """"""
        return object
    
    def set_domain(self, domain=None):
        """"""
        return object
    
    def set_password(self, password=None):
        """"""
        return object
    
    def set_password_save(self, save=None):
        """"""
        return object
    
    def set_username(self, username=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class MountOperationClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def ask_password(self):
        return object

    @property
    def ask_question(self):
        return object

    @property
    def reply(self):
        return object

    @property
    def aborted(self):
        return object

    @property
    def show_processes(self):
        return object

    @property
    def show_unmount_progress(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object

    @property
    def _g_reserved7(self):
        return object

    @property
    def _g_reserved8(self):
        return object

    @property
    def _g_reserved9(self):
        return object


class MountOperationPrivate():
    """"""


class NativeSocketAddress():
    """"""


class NativeVolumeMonitorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_mount_for_mount_path(self):
        return object


class NetworkAddressClass():
    """"""

    @property
    def parent_class(self):
        return object


class NetworkAddressPrivate():
    """"""


class NetworkMonitor():
    """"""
    @staticmethod
    def get_default():
        """"""
        return object
    
    def can_reach(self, connectable=None, cancellable=None):
        """"""
        return object
    
    def can_reach_async(self, connectable=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def can_reach_finish(self, result=None):
        """"""
        return object
    
    def network_changed(self, network_available=None):
        """"""
        return object
    
    def can_reach(self, connectable=None, cancellable=None):
        """"""
        return object
    
    def can_reach_async(self, connectable=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def can_reach_finish(self, result=None):
        """"""
        return object
    
    def get_connectivity(self):
        """"""
        return object
    
    def get_network_available(self):
        """"""
        return object
    
    def get_network_metered(self):
        """"""
        return object


class NetworkMonitorInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def network_changed(self):
        return object

    @property
    def can_reach(self):
        return object

    @property
    def can_reach_async(self):
        return object

    @property
    def can_reach_finish(self):
        return object


class NetworkServiceClass():
    """"""

    @property
    def parent_class(self):
        return object


class NetworkServicePrivate():
    """"""


class Notification(GObject.Object):
    """"""
    
    def __init__(self, title=None):
        """"""
        return object
    @staticmethod
    def new(title=None):
        """"""
        return object
    
    def add_button(self, label=None, detailed_action=None):
        """"""
        return object
    
    def add_button_with_target(self, label=None, action=None, target_format=None, *args):
        """"""
        return object
    
    def add_button_with_target_value(self, label=None, action=None, target=None):
        """"""
        return object
    
    def set_body(self, body=None):
        """"""
        return object
    
    def set_default_action(self, detailed_action=None):
        """"""
        return object
    
    def set_default_action_and_target(self, action=None, target_format=None, *args):
        """"""
        return object
    
    def set_default_action_and_target_value(self, action=None, target=None):
        """"""
        return object
    
    def set_icon(self, icon=None):
        """"""
        return object
    
    def set_priority(self, priority=None):
        """"""
        return object
    
    def set_title(self, title=None):
        """"""
        return object
    
    def set_urgent(self, urgent=None):
        """"""
        return object


class OutputMessage():
    """"""

    @property
    def address(self):
        return object

    @property
    def vectors(self):
        return object

    @property
    def num_vectors(self):
        return object

    @property
    def bytes_sent(self):
        return object

    @property
    def control_messages(self):
        return object

    @property
    def num_control_messages(self):
        return object


class OutputStream(GObject.Object):
    """"""
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def close_fn(self, cancellable=None):
        """"""
        return object
    
    def flush(self, cancellable=None):
        """"""
        return object
    
    def flush_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def flush_finish(self, result=None):
        """"""
        return object
    
    def splice(self, source=None, flags=None, cancellable=None):
        """"""
        return object
    
    def splice_async(self, source=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def splice_finish(self, result=None):
        """"""
        return object
    
    def write_async(self, buffer=None, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def write_finish(self, result=None):
        """"""
        return object
    
    def write_fn(self, buffer=None, count=None, cancellable=None):
        """"""
        return object
    
    def clear_pending(self):
        """"""
        return object
    
    def close(self, cancellable=None):
        """"""
        return object
    
    def close_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, result=None):
        """"""
        return object
    
    def flush(self, cancellable=None):
        """"""
        return object
    
    def flush_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def flush_finish(self, result=None):
        """"""
        return object
    
    def has_pending(self):
        """"""
        return object
    
    def is_closed(self):
        """"""
        return object
    
    def is_closing(self):
        """"""
        return object
    
    def printf(self, bytes_written=None, cancellable=None, error=None, format=None, *args):
        """"""
        return object
    
    def set_pending(self):
        """"""
        return object
    
    def splice(self, source=None, flags=None, cancellable=None):
        """"""
        return object
    
    def splice_async(self, source=None, flags=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def splice_finish(self, result=None):
        """"""
        return object
    
    def vprintf(self, bytes_written=None, cancellable=None, error=None, format=None, args=None):
        """"""
        return object
    
    def write(self, buffer=None, count=None, cancellable=None):
        """"""
        return object
    
    def write_all(self, buffer=None, count=None, bytes_written=None, cancellable=None):
        """"""
        return object
    
    def write_all_async(self, buffer=None, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def write_all_finish(self, result=None, bytes_written=None):
        """"""
        return object
    
    def write_async(self, buffer=None, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def write_bytes(self, bytes=None, cancellable=None):
        """"""
        return object
    
    def write_bytes_async(self, bytes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def write_bytes_finish(self, result=None):
        """"""
        return object
    
    def write_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class OutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def write_fn(self):
        return object

    @property
    def splice(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def close_fn(self):
        return object

    @property
    def write_async(self):
        return object

    @property
    def write_finish(self):
        return object

    @property
    def splice_async(self):
        return object

    @property
    def splice_finish(self):
        return object

    @property
    def flush_async(self):
        return object

    @property
    def flush_finish(self):
        return object

    @property
    def close_async(self):
        return object

    @property
    def close_finish(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object

    @property
    def _g_reserved7(self):
        return object

    @property
    def _g_reserved8(self):
        return object


class OutputStreamPrivate():
    """"""


class OutputVector():
    """"""

    @property
    def buffer(self):
        return object

    @property
    def size(self):
        return object


class Permission(GObject.Object):
    """"""
    
    def acquire(self, cancellable=None):
        """"""
        return object
    
    def acquire_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def acquire_finish(self, result=None):
        """"""
        return object
    
    def release(self, cancellable=None):
        """"""
        return object
    
    def release_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def release_finish(self, result=None):
        """"""
        return object
    
    def acquire(self, cancellable=None):
        """"""
        return object
    
    def acquire_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def acquire_finish(self, result=None):
        """"""
        return object
    
    def get_allowed(self):
        """"""
        return object
    
    def get_can_acquire(self):
        """"""
        return object
    
    def get_can_release(self):
        """"""
        return object
    
    def impl_update(self, allowed=None, can_acquire=None, can_release=None):
        """"""
        return object
    
    def release(self, cancellable=None):
        """"""
        return object
    
    def release_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def release_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class PermissionClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def acquire(self):
        return object

    @property
    def acquire_async(self):
        return object

    @property
    def acquire_finish(self):
        return object

    @property
    def release(self):
        return object

    @property
    def release_async(self):
        return object

    @property
    def release_finish(self):
        return object

    @property
    def reserved(self):
        return object


class PermissionPrivate():
    """"""


class PollableInputStream():
    """"""
    
    def can_poll(self):
        """"""
        return object
    
    def create_source(self, cancellable=None):
        """"""
        return object
    
    def is_readable(self):
        """"""
        return object
    
    def read_nonblocking(self, buffer=None, count=None):
        """"""
        return object
    
    def can_poll(self):
        """"""
        return object
    
    def create_source(self, cancellable=None):
        """"""
        return object
    
    def is_readable(self):
        """"""
        return object
    
    def read_nonblocking(self, buffer=None, count=None, cancellable=None):
        """"""
        return object


class PollableInputStreamInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def can_poll(self):
        return object

    @property
    def is_readable(self):
        return object

    @property
    def create_source(self):
        return object

    @property
    def read_nonblocking(self):
        return object


class PollableOutputStream():
    """"""
    
    def can_poll(self):
        """"""
        return object
    
    def create_source(self, cancellable=None):
        """"""
        return object
    
    def is_writable(self):
        """"""
        return object
    
    def write_nonblocking(self, buffer=None, count=None):
        """"""
        return object
    
    def can_poll(self):
        """"""
        return object
    
    def create_source(self, cancellable=None):
        """"""
        return object
    
    def is_writable(self):
        """"""
        return object
    
    def write_nonblocking(self, buffer=None, count=None, cancellable=None):
        """"""
        return object


class PollableOutputStreamInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def can_poll(self):
        return object

    @property
    def is_writable(self):
        return object

    @property
    def create_source(self):
        return object

    @property
    def write_nonblocking(self):
        return object


class PropertyAction(GObject.Object, Action):
    """"""
    
    def __init__(self, name=None, object=None, property_name=None):
        """"""
        return object
    @staticmethod
    def new(name=None, object=None, property_name=None):
        """"""
        return object


class Proxy():
    """"""
    @staticmethod
    def get_default_for_protocol(protocol=None):
        """"""
        return object
    
    def connect(self, connection=None, proxy_address=None, cancellable=None):
        """"""
        return object
    
    def connect_async(self, connection=None, proxy_address=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_finish(self, result=None):
        """"""
        return object
    
    def supports_hostname(self):
        """"""
        return object
    
    def connect(self, connection=None, proxy_address=None, cancellable=None):
        """"""
        return object
    
    def connect_async(self, connection=None, proxy_address=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_finish(self, result=None):
        """"""
        return object
    
    def supports_hostname(self):
        """"""
        return object


class ProxyAddressClass():
    """"""

    @property
    def parent_class(self):
        return object


class ProxyAddressEnumeratorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object

    @property
    def _g_reserved7(self):
        return object


class ProxyAddressEnumeratorPrivate():
    """"""


class ProxyAddressPrivate():
    """"""


class ProxyInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def connect(self):
        return object

    @property
    def connect_async(self):
        return object

    @property
    def connect_finish(self):
        return object

    @property
    def supports_hostname(self):
        return object


class ProxyResolver():
    """"""
    @staticmethod
    def get_default():
        """"""
        return object
    
    def is_supported(self):
        """"""
        return object
    
    def lookup(self, uri=None, cancellable=None):
        """"""
        return object
    
    def lookup_async(self, uri=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_finish(self, result=None):
        """"""
        return object
    
    def is_supported(self):
        """"""
        return object
    
    def lookup(self, uri=None, cancellable=None):
        """"""
        return object
    
    def lookup_async(self, uri=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_finish(self, result=None):
        """"""
        return object


class ProxyResolverInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def is_supported(self):
        return object

    @property
    def lookup(self):
        return object

    @property
    def lookup_async(self):
        return object

    @property
    def lookup_finish(self):
        return object


class RemoteActionGroup():
    """"""
    
    def activate_action_full(self, action_name=None, parameter=None, platform_data=None):
        """"""
        return object
    
    def change_action_state_full(self, action_name=None, value=None, platform_data=None):
        """"""
        return object
    
    def activate_action_full(self, action_name=None, parameter=None, platform_data=None):
        """"""
        return object
    
    def change_action_state_full(self, action_name=None, value=None, platform_data=None):
        """"""
        return object


class RemoteActionGroupInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def activate_action_full(self):
        return object

    @property
    def change_action_state_full(self):
        return object


class Resolver(GObject.Object):
    """"""
    @staticmethod
    def free_addresses(addresses=None):
        """"""
        return object
    @staticmethod
    def free_targets(targets=None):
        """"""
        return object
    @staticmethod
    def get_default():
        """"""
        return object
    
    def lookup_by_address(self, address=None, cancellable=None):
        """"""
        return object
    
    def lookup_by_address_async(self, address=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_by_address_finish(self, result=None):
        """"""
        return object
    
    def lookup_by_name(self, hostname=None, cancellable=None):
        """"""
        return object
    
    def lookup_by_name_async(self, hostname=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_by_name_finish(self, result=None):
        """"""
        return object
    
    def lookup_records(self, rrname=None, record_type=None, cancellable=None):
        """"""
        return object
    
    def lookup_records_async(self, rrname=None, record_type=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_records_finish(self, result=None):
        """"""
        return object
    
    def lookup_service(self, rrname=None, cancellable=None):
        """"""
        return object
    
    def lookup_service_async(self, rrname=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_service_finish(self, result=None):
        """"""
        return object
    
    def reload(self):
        """"""
        return object
    
    def lookup_by_address(self, address=None, cancellable=None):
        """"""
        return object
    
    def lookup_by_address_async(self, address=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_by_address_finish(self, result=None):
        """"""
        return object
    
    def lookup_by_name(self, hostname=None, cancellable=None):
        """"""
        return object
    
    def lookup_by_name_async(self, hostname=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_by_name_finish(self, result=None):
        """"""
        return object
    
    def lookup_records(self, rrname=None, record_type=None, cancellable=None):
        """"""
        return object
    
    def lookup_records_async(self, rrname=None, record_type=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_records_finish(self, result=None):
        """"""
        return object
    
    def lookup_service(self, service=None, protocol=None, domain=None, cancellable=None):
        """"""
        return object
    
    def lookup_service_async(self, service=None, protocol=None, domain=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_service_finish(self, result=None):
        """"""
        return object
    
    def set_default(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ResolverClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def reload(self):
        return object

    @property
    def lookup_by_name(self):
        return object

    @property
    def lookup_by_name_async(self):
        return object

    @property
    def lookup_by_name_finish(self):
        return object

    @property
    def lookup_by_address(self):
        return object

    @property
    def lookup_by_address_async(self):
        return object

    @property
    def lookup_by_address_finish(self):
        return object

    @property
    def lookup_service(self):
        return object

    @property
    def lookup_service_async(self):
        return object

    @property
    def lookup_service_finish(self):
        return object

    @property
    def lookup_records(self):
        return object

    @property
    def lookup_records_async(self):
        return object

    @property
    def lookup_records_finish(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object


class ResolverPrivate():
    """"""


class Resource():
    """"""
    @staticmethod
    def new_from_data(data=None):
        """"""
        return object
    
    def _register(self):
        """"""
        return object
    
    def _unregister(self):
        """"""
        return object
    
    def enumerate_children(self, path=None, lookup_flags=None):
        """"""
        return object
    
    def get_info(self, path=None, lookup_flags=None, size=None, flags=None):
        """"""
        return object
    
    def lookup_data(self, path=None, lookup_flags=None):
        """"""
        return object
    
    def open_stream(self, path=None, lookup_flags=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def load(filename=None):
        """"""
        return object


class Seekable():
    """"""
    
    def can_seek(self):
        """"""
        return object
    
    def can_truncate(self):
        """"""
        return object
    
    def seek(self, offset=None, type=None, cancellable=None):
        """"""
        return object
    
    def tell(self):
        """"""
        return object
    
    def truncate_fn(self, offset=None, cancellable=None):
        """"""
        return object
    
    def can_seek(self):
        """"""
        return object
    
    def can_truncate(self):
        """"""
        return object
    
    def seek(self, offset=None, type=None, cancellable=None):
        """"""
        return object
    
    def tell(self):
        """"""
        return object
    
    def truncate(self, offset=None, cancellable=None):
        """"""
        return object


class SeekableIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def tell(self):
        return object

    @property
    def can_seek(self):
        return object

    @property
    def seek(self):
        return object

    @property
    def can_truncate(self):
        return object

    @property
    def truncate_fn(self):
        return object


class Settings(GObject.Object):
    """"""
    
    def __init__(self, schema_id=None):
        """"""
        return object
    @staticmethod
    def new(schema_id=None):
        """"""
        return object
    @staticmethod
    def new_full(schema=None, backend=None, path=None):
        """"""
        return object
    @staticmethod
    def new_with_backend(schema_id=None, backend=None):
        """"""
        return object
    @staticmethod
    def new_with_backend_and_path(schema_id=None, backend=None, path=None):
        """"""
        return object
    @staticmethod
    def new_with_path(schema_id=None, path=None):
        """"""
        return object
    @staticmethod
    def list_relocatable_schemas():
        """"""
        return object
    @staticmethod
    def list_schemas():
        """"""
        return object
    @staticmethod
    def sync():
        """"""
        return object
    @staticmethod
    def unbind(object=None, property=None):
        """"""
        return object
    
    def change_event(self, keys=None, n_keys=None):
        """"""
        return object
    
    def changed(self, key=None):
        """"""
        return object
    
    def writable_change_event(self, key=None):
        """"""
        return object
    
    def writable_changed(self, key=None):
        """"""
        return object
    
    def apply(self):
        """"""
        return object
    
    def bind(self, key=None, object=None, property=None, flags=None):
        """"""
        return object
    
    def bind_with_mapping(self, key=None, object=None, property=None, flags=None, get_mapping=None, set_mapping=None, user_data=None, destroy=None):
        """"""
        return object
    
    def bind_writable(self, key=None, object=None, property=None, inverted=None):
        """"""
        return object
    
    def create_action(self, key=None):
        """"""
        return object
    
    def delay(self):
        """"""
        return object
    
    def get(self, key=None, format=None, *args):
        """"""
        return object
    
    def get_boolean(self, key=None):
        """"""
        return object
    
    def get_child(self, name=None):
        """"""
        return object
    
    def get_default_value(self, key=None):
        """"""
        return object
    
    def get_double(self, key=None):
        """"""
        return object
    
    def get_enum(self, key=None):
        """"""
        return object
    
    def get_flags(self, key=None):
        """"""
        return object
    
    def get_has_unapplied(self):
        """"""
        return object
    
    def get_int(self, key=None):
        """"""
        return object
    
    def get_int64(self, key=None):
        """"""
        return object
    
    def get_mapped(self, key=None, mapping=None, user_data=None):
        """"""
        return object
    
    def get_range(self, key=None):
        """"""
        return object
    
    def get_string(self, key=None):
        """"""
        return object
    
    def get_strv(self, key=None):
        """"""
        return object
    
    def get_uint(self, key=None):
        """"""
        return object
    
    def get_uint64(self, key=None):
        """"""
        return object
    
    def get_user_value(self, key=None):
        """"""
        return object
    
    def get_value(self, key=None):
        """"""
        return object
    
    def is_writable(self, name=None):
        """"""
        return object
    
    def list_children(self):
        """"""
        return object
    
    def list_keys(self):
        """"""
        return object
    
    def range_check(self, key=None, value=None):
        """"""
        return object
    
    def reset(self, key=None):
        """"""
        return object
    
    def revert(self):
        """"""
        return object
    
    def set(self, key=None, format=None, *args):
        """"""
        return object
    
    def set_boolean(self, key=None, value=None):
        """"""
        return object
    
    def set_double(self, key=None, value=None):
        """"""
        return object
    
    def set_enum(self, key=None, value=None):
        """"""
        return object
    
    def set_flags(self, key=None, value=None):
        """"""
        return object
    
    def set_int(self, key=None, value=None):
        """"""
        return object
    
    def set_int64(self, key=None, value=None):
        """"""
        return object
    
    def set_string(self, key=None, value=None):
        """"""
        return object
    
    def set_strv(self, key=None, value=None):
        """"""
        return object
    
    def set_uint(self, key=None, value=None):
        """"""
        return object
    
    def set_uint64(self, key=None, value=None):
        """"""
        return object
    
    def set_value(self, key=None, value=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SettingsBackend(GObject.Object):
    """"""
    @staticmethod
    def flatten_tree(tree=None, path=None, keys=None, values=None):
        """"""
        return object
    @staticmethod
    def get_default():
        """"""
        return object
    
    def get_permission(self, path=None):
        """"""
        return object
    
    def get_writable(self, key=None):
        """"""
        return object
    
    def read(self, key=None, expected_type=None, default_value=None):
        """"""
        return object
    
    def read_user_value(self, key=None, expected_type=None):
        """"""
        return object
    
    def reset(self, key=None, origin_tag=None):
        """"""
        return object
    
    def subscribe(self, name=None):
        """"""
        return object
    
    def sync(self):
        """"""
        return object
    
    def unsubscribe(self, name=None):
        """"""
        return object
    
    def write(self, key=None, value=None, origin_tag=None):
        """"""
        return object
    
    def write_tree(self, tree=None, origin_tag=None):
        """"""
        return object
    
    def changed(self, key=None, origin_tag=None):
        """"""
        return object
    
    def changed_tree(self, tree=None, origin_tag=None):
        """"""
        return object
    
    def keys_changed(self, path=None, items=None, origin_tag=None):
        """"""
        return object
    
    def path_changed(self, path=None, origin_tag=None):
        """"""
        return object
    
    def path_writable_changed(self, path=None):
        """"""
        return object
    
    def writable_changed(self, key=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SettingsBackendClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def read(self):
        return object

    @property
    def get_writable(self):
        return object

    @property
    def write(self):
        return object

    @property
    def write_tree(self):
        return object

    @property
    def reset(self):
        return object

    @property
    def subscribe(self):
        return object

    @property
    def unsubscribe(self):
        return object

    @property
    def sync(self):
        return object

    @property
    def get_permission(self):
        return object

    @property
    def read_user_value(self):
        return object

    @property
    def padding(self):
        return object


class SettingsBackendPrivate():
    """"""


class SettingsClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def writable_changed(self):
        return object

    @property
    def changed(self):
        return object

    @property
    def writable_change_event(self):
        return object

    @property
    def change_event(self):
        return object

    @property
    def padding(self):
        return object


class SettingsPrivate():
    """"""


class SettingsSchema():
    """"""
    
    def get_id(self):
        """"""
        return object
    
    def get_key(self, name=None):
        """"""
        return object
    
    def get_path(self):
        """"""
        return object
    
    def has_key(self, name=None):
        """"""
        return object
    
    def list_children(self):
        """"""
        return object
    
    def list_keys(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class SettingsSchemaKey():
    """"""
    
    def get_default_value(self):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_range(self):
        """"""
        return object
    
    def get_summary(self):
        """"""
        return object
    
    def get_value_type(self):
        """"""
        return object
    
    def range_check(self, value=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class SettingsSchemaSource():
    """"""
    @staticmethod
    def new_from_directory(directory=None, parent=None, trusted=None):
        """"""
        return object
    
    def list_schemas(self, recursive=None, non_relocatable=None, relocatable=None):
        """"""
        return object
    
    def lookup(self, schema_id=None, recursive=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def get_default():
        """"""
        return object


class SimpleAction(GObject.Object, Action):
    """"""
    
    def __init__(self, name=None, parameter_type=None):
        """"""
        return object
    @staticmethod
    def new(name=None, parameter_type=None):
        """"""
        return object
    @staticmethod
    def new_stateful(name=None, parameter_type=None, state=None):
        """"""
        return object
    
    def set_enabled(self, enabled=None):
        """"""
        return object
    
    def set_state(self, value=None):
        """"""
        return object
    
    def set_state_hint(self, state_hint=None):
        """"""
        return object


class SimpleActionGroup(GObject.Object, ActionGroup, ActionMap):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def add_entries(self, entries=None, n_entries=None, user_data=None):
        """"""
        return object
    
    def insert(self, action=None):
        """"""
        return object
    
    def lookup(self, action_name=None):
        """"""
        return object
    
    def remove(self, action_name=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SimpleActionGroupClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def padding(self):
        return object


class SimpleActionGroupPrivate():
    """"""


class SimpleAsyncResult(GObject.Object, AsyncResult):
    """"""
    
    def __init__(self, source_object=None, callback=None, user_data=None, source_tag=None):
        """"""
        return object
    @staticmethod
    def new(source_object=None, callback=None, user_data=None, source_tag=None):
        """"""
        return object
    @staticmethod
    def new_error(source_object=None, callback=None, user_data=None, domain=None, code=None, format=None, *args):
        """"""
        return object
    @staticmethod
    def new_from_error(source_object=None, callback=None, user_data=None, error=None):
        """"""
        return object
    @staticmethod
    def new_take_error(source_object=None, callback=None, user_data=None, error=None):
        """"""
        return object
    @staticmethod
    def is_valid(result=None, source=None, source_tag=None):
        """"""
        return object
    
    def complete(self):
        """"""
        return object
    
    def complete_in_idle(self):
        """"""
        return object
    
    def get_op_res_gboolean(self):
        """"""
        return object
    
    def get_op_res_gpointer(self):
        """"""
        return object
    
    def get_op_res_gssize(self):
        """"""
        return object
    
    def get_source_tag(self):
        """"""
        return object
    
    def propagate_error(self):
        """"""
        return object
    
    def run_in_thread(self, func=None, io_priority=None, cancellable=None):
        """"""
        return object
    
    def set_check_cancellable(self, check_cancellable=None):
        """"""
        return object
    
    def set_error(self, domain=None, code=None, format=None, *args):
        """"""
        return object
    
    def set_error_va(self, domain=None, code=None, format=None, args=None):
        """"""
        return object
    
    def set_from_error(self, error=None):
        """"""
        return object
    
    def set_handle_cancellation(self, handle_cancellation=None):
        """"""
        return object
    
    def set_op_res_gboolean(self, op_res=None):
        """"""
        return object
    
    def set_op_res_gpointer(self, op_res=None, destroy_op_res=None):
        """"""
        return object
    
    def set_op_res_gssize(self, op_res=None):
        """"""
        return object
    
    def take_error(self, error=None):
        """"""
        return object


class SimpleAsyncResultClass():
    """"""


class SimpleIOStream(IOStream):
    """"""
    
    def __init__(self, input_stream=None, output_stream=None):
        """"""
        return object
    @staticmethod
    def new(input_stream=None, output_stream=None):
        """"""
        return object


class SimplePermission(Permission):
    """"""
    
    def __init__(self, allowed=None):
        """"""
        return object
    @staticmethod
    def new(allowed=None):
        """"""
        return object


class SimpleProxyResolver(GObject.Object, ProxyResolver):
    """"""
    @staticmethod
    def new(default_proxy=None, ignore_hosts=None):
        """"""
        return object
    
    def set_default_proxy(self, default_proxy=None):
        """"""
        return object
    
    def set_ignore_hosts(self, ignore_hosts=None):
        """"""
        return object
    
    def set_uri_proxy(self, uri_scheme=None, proxy=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SimpleProxyResolverClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class SimpleProxyResolverPrivate():
    """"""


class Socket(GObject.Object, DatagramBased, Initable):
    """"""
    
    def __init__(self, family=None, type=None, protocol=None):
        """"""
        return object
    @staticmethod
    def new(family=None, type=None, protocol=None):
        """"""
        return object
    @staticmethod
    def new_from_fd(fd=None):
        """"""
        return object
    
    def accept(self, cancellable=None):
        """"""
        return object
    
    def bind(self, address=None, allow_reuse=None):
        """"""
        return object
    
    def check_connect_result(self):
        """"""
        return object
    
    def close(self):
        """"""
        return object
    
    def condition_check(self, condition=None):
        """"""
        return object
    
    def condition_timed_wait(self, condition=None, timeout=None, cancellable=None):
        """"""
        return object
    
    def condition_wait(self, condition=None, cancellable=None):
        """"""
        return object
    
    def connect(self, address=None, cancellable=None):
        """"""
        return object
    
    def connection_factory_create_connection(self):
        """"""
        return object
    
    def create_source(self, condition=None, cancellable=None):
        """"""
        return object
    
    def get_available_bytes(self):
        """"""
        return object
    
    def get_blocking(self):
        """"""
        return object
    
    def get_broadcast(self):
        """"""
        return object
    
    def get_credentials(self):
        """"""
        return object
    
    def get_family(self):
        """"""
        return object
    
    def get_fd(self):
        """"""
        return object
    
    def get_keepalive(self):
        """"""
        return object
    
    def get_listen_backlog(self):
        """"""
        return object
    
    def get_local_address(self):
        """"""
        return object
    
    def get_multicast_loopback(self):
        """"""
        return object
    
    def get_multicast_ttl(self):
        """"""
        return object
    
    def get_option(self, level=None, optname=None, value=None):
        """"""
        return object
    
    def get_protocol(self):
        """"""
        return object
    
    def get_remote_address(self):
        """"""
        return object
    
    def get_socket_type(self):
        """"""
        return object
    
    def get_timeout(self):
        """"""
        return object
    
    def get_ttl(self):
        """"""
        return object
    
    def is_closed(self):
        """"""
        return object
    
    def is_connected(self):
        """"""
        return object
    
    def join_multicast_group(self, group=None, source_specific=None, iface=None):
        """"""
        return object
    
    def join_multicast_group_ssm(self, group=None, source_specific=None, iface=None):
        """"""
        return object
    
    def leave_multicast_group(self, group=None, source_specific=None, iface=None):
        """"""
        return object
    
    def leave_multicast_group_ssm(self, group=None, source_specific=None, iface=None):
        """"""
        return object
    
    def listen(self):
        """"""
        return object
    
    def receive(self, buffer=None, size=None, cancellable=None):
        """"""
        return object
    
    def receive_from(self, address=None, buffer=None, size=None, cancellable=None):
        """"""
        return object
    
    def receive_message(self, address=None, vectors=None, num_vectors=None, messages=None, num_messages=None, flags=None, cancellable=None):
        """"""
        return object
    
    def receive_messages(self, messages=None, num_messages=None, flags=None, cancellable=None):
        """"""
        return object
    
    def receive_with_blocking(self, buffer=None, size=None, blocking=None, cancellable=None):
        """"""
        return object
    
    def send(self, buffer=None, size=None, cancellable=None):
        """"""
        return object
    
    def send_message(self, address=None, vectors=None, num_vectors=None, messages=None, num_messages=None, flags=None, cancellable=None):
        """"""
        return object
    
    def send_messages(self, messages=None, num_messages=None, flags=None, cancellable=None):
        """"""
        return object
    
    def send_to(self, address=None, buffer=None, size=None, cancellable=None):
        """"""
        return object
    
    def send_with_blocking(self, buffer=None, size=None, blocking=None, cancellable=None):
        """"""
        return object
    
    def set_blocking(self, blocking=None):
        """"""
        return object
    
    def set_broadcast(self, broadcast=None):
        """"""
        return object
    
    def set_keepalive(self, keepalive=None):
        """"""
        return object
    
    def set_listen_backlog(self, backlog=None):
        """"""
        return object
    
    def set_multicast_loopback(self, loopback=None):
        """"""
        return object
    
    def set_multicast_ttl(self, ttl=None):
        """"""
        return object
    
    def set_option(self, level=None, optname=None, value=None):
        """"""
        return object
    
    def set_timeout(self, timeout=None):
        """"""
        return object
    
    def set_ttl(self, ttl=None):
        """"""
        return object
    
    def shutdown(self, shutdown_read=None, shutdown_write=None):
        """"""
        return object
    
    def speaks_ipv4(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketAddressClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_family(self):
        return object

    @property
    def get_native_size(self):
        return object

    @property
    def to_native(self):
        return object


class SocketAddressEnumerator(GObject.Object):
    """"""
    
    def next(self, cancellable=None):
        """"""
        return object
    
    def next_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def next_finish(self, result=None):
        """"""
        return object
    
    def next(self, cancellable=None):
        """"""
        return object
    
    def next_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def next_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object


class SocketAddressEnumeratorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def next(self):
        return object

    @property
    def next_async(self):
        return object

    @property
    def next_finish(self):
        return object


class SocketClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object

    @property
    def _g_reserved7(self):
        return object

    @property
    def _g_reserved8(self):
        return object

    @property
    def _g_reserved9(self):
        return object

    @property
    def _g_reserved10(self):
        return object


class SocketClient(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def event(self, event=None, connectable=None, connection=None):
        """"""
        return object
    
    def add_application_proxy(self, protocol=None):
        """"""
        return object
    
    def connect(self, connectable=None, cancellable=None):
        """"""
        return object
    
    def connect_async(self, connectable=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_finish(self, result=None):
        """"""
        return object
    
    def connect_to_host(self, host_and_port=None, default_port=None, cancellable=None):
        """"""
        return object
    
    def connect_to_host_async(self, host_and_port=None, default_port=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_to_host_finish(self, result=None):
        """"""
        return object
    
    def connect_to_service(self, domain=None, service=None, cancellable=None):
        """"""
        return object
    
    def connect_to_service_async(self, domain=None, service=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_to_service_finish(self, result=None):
        """"""
        return object
    
    def connect_to_uri(self, uri=None, default_port=None, cancellable=None):
        """"""
        return object
    
    def connect_to_uri_async(self, uri=None, default_port=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_to_uri_finish(self, result=None):
        """"""
        return object
    
    def get_enable_proxy(self):
        """"""
        return object
    
    def get_family(self):
        """"""
        return object
    
    def get_local_address(self):
        """"""
        return object
    
    def get_protocol(self):
        """"""
        return object
    
    def get_proxy_resolver(self):
        """"""
        return object
    
    def get_socket_type(self):
        """"""
        return object
    
    def get_timeout(self):
        """"""
        return object
    
    def get_tls(self):
        """"""
        return object
    
    def get_tls_validation_flags(self):
        """"""
        return object
    
    def set_enable_proxy(self, enable=None):
        """"""
        return object
    
    def set_family(self, family=None):
        """"""
        return object
    
    def set_local_address(self, address=None):
        """"""
        return object
    
    def set_protocol(self, protocol=None):
        """"""
        return object
    
    def set_proxy_resolver(self, proxy_resolver=None):
        """"""
        return object
    
    def set_socket_type(self, type=None):
        """"""
        return object
    
    def set_timeout(self, timeout=None):
        """"""
        return object
    
    def set_tls(self, tls=None):
        """"""
        return object
    
    def set_tls_validation_flags(self, flags=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketClientClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def event(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object


class SocketClientPrivate():
    """"""


class SocketConnectable():
    """"""
    
    def enumerate(self):
        """"""
        return object
    
    def proxy_enumerate(self):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object
    
    def enumerate(self):
        """"""
        return object
    
    def proxy_enumerate(self):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object


class SocketConnectableIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def enumerate(self):
        return object

    @property
    def proxy_enumerate(self):
        return object

    @property
    def to_string(self):
        return object


class SocketConnection(IOStream):
    """"""
    @staticmethod
    def factory_lookup_type(family=None, type=None, protocol_id=None):
        """"""
        return object
    @staticmethod
    def factory_register_type(g_type=None, family=None, type=None, protocol=None):
        """"""
        return object
    
    def connect(self, address=None, cancellable=None):
        """"""
        return object
    
    def connect_async(self, address=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def connect_finish(self, result=None):
        """"""
        return object
    
    def get_local_address(self):
        """"""
        return object
    
    def get_remote_address(self):
        """"""
        return object
    
    def get_socket(self):
        """"""
        return object
    
    def is_connected(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketConnectionClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object


class SocketConnectionPrivate():
    """"""


class SocketControlMessage(GObject.Object):
    """"""
    @staticmethod
    def deserialize(level=None, type=None, size=None, data=None):
        """"""
        return object
    
    def get_level(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def get_type(self):
        """"""
        return object
    
    def serialize(self, data=None):
        """"""
        return object
    
    def get_level(self):
        """"""
        return object
    
    def get_msg_type(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def serialize(self, data=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketControlMessageClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_size(self):
        return object

    @property
    def get_level(self):
        return object

    @property
    def get_type(self):
        return object

    @property
    def serialize(self):
        return object

    @property
    def deserialize(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class SocketControlMessagePrivate():
    """"""


class SocketListener(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def changed(self):
        """"""
        return object
    
    def event(self, event=None, socket=None):
        """"""
        return object
    
    def accept(self, source_object=None, cancellable=None):
        """"""
        return object
    
    def accept_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def accept_finish(self, result=None, source_object=None):
        """"""
        return object
    
    def accept_socket(self, source_object=None, cancellable=None):
        """"""
        return object
    
    def accept_socket_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def accept_socket_finish(self, result=None, source_object=None):
        """"""
        return object
    
    def add_address(self, address=None, type=None, protocol=None, source_object=None, effective_address=None):
        """"""
        return object
    
    def add_any_inet_port(self, source_object=None):
        """"""
        return object
    
    def add_inet_port(self, port=None, source_object=None):
        """"""
        return object
    
    def add_socket(self, socket=None, source_object=None):
        """"""
        return object
    
    def close(self):
        """"""
        return object
    
    def set_backlog(self, listen_backlog=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketListenerClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def changed(self):
        return object

    @property
    def event(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object


class SocketListenerPrivate():
    """"""


class SocketPrivate():
    """"""


class SocketService(SocketListener):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def incoming(self, connection=None, source_object=None):
        """"""
        return object
    
    def is_active(self):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketServiceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def incoming(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object


class SocketServicePrivate():
    """"""


class SrvTarget():
    """"""
    
    def __init__(self, hostname=None, port=None, priority=None, weight=None):
        """"""
        return object
    @staticmethod
    def new(hostname=None, port=None, priority=None, weight=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_hostname(self):
        """"""
        return object
    
    def get_port(self):
        """"""
        return object
    
    def get_priority(self):
        """"""
        return object
    
    def get_weight(self):
        """"""
        return object
    @staticmethod
    def list_sort(targets=None):
        """"""
        return object


class StaticResource():
    """"""
    
    def fini(self):
        """"""
        return object
    
    def get_resource(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def data_len(self):
        return object

    @property
    def resource(self):
        return object

    @property
    def next(self):
        return object

    @property
    def padding(self):
        return object


class Subprocess(GObject.Object, Initable):
    """"""
    
    def __init__(self, flags=None, error=None, argv0=None, *args):
        """"""
        return object
    @staticmethod
    def new(flags=None, error=None, argv0=None, *args):
        """"""
        return object
    @staticmethod
    def newv(argv=None, flags=None):
        """"""
        return object
    
    def communicate(self, stdin_buf=None, cancellable=None, stdout_buf=None, stderr_buf=None):
        """"""
        return object
    
    def communicate_async(self, stdin_buf=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def communicate_finish(self, result=None, stdout_buf=None, stderr_buf=None):
        """"""
        return object
    
    def communicate_utf8(self, stdin_buf=None, cancellable=None, stdout_buf=None, stderr_buf=None):
        """"""
        return object
    
    def communicate_utf8_async(self, stdin_buf=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def communicate_utf8_finish(self, result=None, stdout_buf=None, stderr_buf=None):
        """"""
        return object
    
    def force_exit(self):
        """"""
        return object
    
    def get_exit_status(self):
        """"""
        return object
    
    def get_identifier(self):
        """"""
        return object
    
    def get_if_exited(self):
        """"""
        return object
    
    def get_if_signaled(self):
        """"""
        return object
    
    def get_status(self):
        """"""
        return object
    
    def get_stderr_pipe(self):
        """"""
        return object
    
    def get_stdin_pipe(self):
        """"""
        return object
    
    def get_stdout_pipe(self):
        """"""
        return object
    
    def get_successful(self):
        """"""
        return object
    
    def get_term_sig(self):
        """"""
        return object
    
    def send_signal(self, signal_num=None):
        """"""
        return object
    
    def wait(self, cancellable=None):
        """"""
        return object
    
    def wait_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def wait_check(self, cancellable=None):
        """"""
        return object
    
    def wait_check_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def wait_check_finish(self, result=None):
        """"""
        return object
    
    def wait_finish(self, result=None):
        """"""
        return object


class SubprocessLauncher(GObject.Object):
    """"""
    
    def __init__(self, flags=None):
        """"""
        return object
    @staticmethod
    def new(flags=None):
        """"""
        return object
    
    def getenv(self, variable=None):
        """"""
        return object
    
    def set_child_setup(self, child_setup=None, user_data=None, destroy_notify=None):
        """"""
        return object
    
    def set_cwd(self, cwd=None):
        """"""
        return object
    
    def set_environ(self, env=None):
        """"""
        return object
    
    def set_flags(self, flags=None):
        """"""
        return object
    
    def set_stderr_file_path(self, path=None):
        """"""
        return object
    
    def set_stdin_file_path(self, path=None):
        """"""
        return object
    
    def set_stdout_file_path(self, path=None):
        """"""
        return object
    
    def setenv(self, variable=None, value=None, overwrite=None):
        """"""
        return object
    
    def spawn(self, error=None, argv0=None, *args):
        """"""
        return object
    
    def spawnv(self, argv=None):
        """"""
        return object
    
    def take_fd(self, source_fd=None, target_fd=None):
        """"""
        return object
    
    def take_stderr_fd(self, fd=None):
        """"""
        return object
    
    def take_stdin_fd(self, fd=None):
        """"""
        return object
    
    def take_stdout_fd(self, fd=None):
        """"""
        return object
    
    def unsetenv(self, variable=None):
        """"""
        return object


class Task(GObject.Object, AsyncResult):
    """"""
    
    def __init__(self, source_object=None, cancellable=None, callback=None, callback_data=None):
        """"""
        return object
    @staticmethod
    def new(source_object=None, cancellable=None, callback=None, callback_data=None):
        """"""
        return object
    @staticmethod
    def is_valid(result=None, source_object=None):
        """"""
        return object
    @staticmethod
    def report_error(source_object=None, callback=None, callback_data=None, source_tag=None, error=None):
        """"""
        return object
    @staticmethod
    def report_new_error(source_object=None, callback=None, callback_data=None, source_tag=None, domain=None, code=None, format=None, *args):
        """"""
        return object
    
    def attach_source(self, source=None, callback=None):
        """"""
        return object
    
    def get_cancellable(self):
        """"""
        return object
    
    def get_check_cancellable(self):
        """"""
        return object
    
    def get_completed(self):
        """"""
        return object
    
    def get_context(self):
        """"""
        return object
    
    def get_priority(self):
        """"""
        return object
    
    def get_return_on_cancel(self):
        """"""
        return object
    
    def get_source_object(self):
        """"""
        return object
    
    def get_source_tag(self):
        """"""
        return object
    
    def get_task_data(self):
        """"""
        return object
    
    def had_error(self):
        """"""
        return object
    
    def propagate_boolean(self):
        """"""
        return object
    
    def propagate_int(self):
        """"""
        return object
    
    def propagate_pointer(self):
        """"""
        return object
    
    def return_boolean(self, result=None):
        """"""
        return object
    
    def return_error(self, error=None):
        """"""
        return object
    
    def return_error_if_cancelled(self):
        """"""
        return object
    
    def return_int(self, result=None):
        """"""
        return object
    
    def return_new_error(self, domain=None, code=None, format=None, *args):
        """"""
        return object
    
    def return_pointer(self, result=None, result_destroy=None):
        """"""
        return object
    
    def run_in_thread(self, task_func=None):
        """"""
        return object
    
    def run_in_thread_sync(self, task_func=None):
        """"""
        return object
    
    def set_check_cancellable(self, check_cancellable=None):
        """"""
        return object
    
    def set_priority(self, priority=None):
        """"""
        return object
    
    def set_return_on_cancel(self, return_on_cancel=None):
        """"""
        return object
    
    def set_source_tag(self, source_tag=None):
        """"""
        return object
    
    def set_task_data(self, task_data=None, task_data_destroy=None):
        """"""
        return object


class TaskClass():
    """"""


class TcpConnection(SocketConnection):
    """"""
    
    def get_graceful_disconnect(self):
        """"""
        return object
    
    def set_graceful_disconnect(self, graceful_disconnect=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TcpConnectionClass():
    """"""

    @property
    def parent_class(self):
        return object


class TcpConnectionPrivate():
    """"""


class TcpWrapperConnection(TcpConnection):
    """"""
    
    def __init__(self, base_io_stream=None, socket=None):
        """"""
        return object
    @staticmethod
    def new(base_io_stream=None, socket=None):
        """"""
        return object
    
    def get_base_io_stream(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TcpWrapperConnectionClass():
    """"""

    @property
    def parent_class(self):
        return object


class TcpWrapperConnectionPrivate():
    """"""


class TestDBus(GObject.Object):
    """"""
    
    def __init__(self, flags=None):
        """"""
        return object
    @staticmethod
    def new(flags=None):
        """"""
        return object
    @staticmethod
    def unset():
        """"""
        return object
    
    def add_service_dir(self, path=None):
        """"""
        return object
    
    def down(self):
        """"""
        return object
    
    def get_bus_address(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def up(self):
        """"""
        return object


class ThemedIcon(GObject.Object, Icon):
    """"""
    
    def __init__(self, iconname=None):
        """"""
        return object
    @staticmethod
    def new(iconname=None):
        """"""
        return object
    @staticmethod
    def new_from_names(iconnames=None, len=None):
        """"""
        return object
    @staticmethod
    def new_with_default_fallbacks(iconname=None):
        """"""
        return object
    
    def append_name(self, iconname=None):
        """"""
        return object
    
    def get_names(self):
        """"""
        return object
    
    def prepend_name(self, iconname=None):
        """"""
        return object


class ThemedIconClass():
    """"""


class ThreadedSocketService(SocketService):
    """"""
    
    def __init__(self, max_threads=None):
        """"""
        return object
    @staticmethod
    def new(max_threads=None):
        """"""
        return object
    
    def run(self, connection=None, source_object=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ThreadedSocketServiceClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def run(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class ThreadedSocketServicePrivate():
    """"""


class TlsBackend():
    """"""
    @staticmethod
    def get_default():
        """"""
        return object
    
    def get_default_database(self):
        """"""
        return object
    
    def supports_dtls(self):
        """"""
        return object
    
    def supports_tls(self):
        """"""
        return object
    
    def get_certificate_type(self):
        """"""
        return object
    
    def get_client_connection_type(self):
        """"""
        return object
    
    def get_default_database(self):
        """"""
        return object
    
    def get_dtls_client_connection_type(self):
        """"""
        return object
    
    def get_dtls_server_connection_type(self):
        """"""
        return object
    
    def get_file_database_type(self):
        """"""
        return object
    
    def get_server_connection_type(self):
        """"""
        return object
    
    def supports_dtls(self):
        """"""
        return object
    
    def supports_tls(self):
        """"""
        return object


class TlsBackendInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def supports_tls(self):
        return object

    @property
    def get_certificate_type(self):
        return object

    @property
    def get_client_connection_type(self):
        return object

    @property
    def get_server_connection_type(self):
        return object

    @property
    def get_file_database_type(self):
        return object

    @property
    def get_default_database(self):
        return object

    @property
    def supports_dtls(self):
        return object

    @property
    def get_dtls_client_connection_type(self):
        return object

    @property
    def get_dtls_server_connection_type(self):
        return object


class TlsCertificate(GObject.Object):
    """"""
    @staticmethod
    def new_from_file(file=None):
        """"""
        return object
    @staticmethod
    def new_from_files(cert_file=None, key_file=None):
        """"""
        return object
    @staticmethod
    def new_from_pem(data=None, length=None):
        """"""
        return object
    @staticmethod
    def list_new_from_file(file=None):
        """"""
        return object
    
    def verify(self, identity=None, trusted_ca=None):
        """"""
        return object
    
    def get_issuer(self):
        """"""
        return object
    
    def is_same(self, cert_two=None):
        """"""
        return object
    
    def verify(self, identity=None, trusted_ca=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TlsCertificateClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def verify(self):
        return object

    @property
    def padding(self):
        return object


class TlsCertificatePrivate():
    """"""


class TlsClientConnection():
    """"""
    @staticmethod
    def new(base_io_stream=None, server_identity=None):
        """"""
        return object
    
    def copy_session_state(self, source=None):
        """"""
        return object
    
    def copy_session_state(self, source=None):
        """"""
        return object
    
    def get_accepted_cas(self):
        """"""
        return object
    
    def get_server_identity(self):
        """"""
        return object
    
    def get_use_ssl3(self):
        """"""
        return object
    
    def get_validation_flags(self):
        """"""
        return object
    
    def set_server_identity(self, identity=None):
        """"""
        return object
    
    def set_use_ssl3(self, use_ssl3=None):
        """"""
        return object
    
    def set_validation_flags(self, flags=None):
        """"""
        return object


class TlsClientConnectionInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def copy_session_state(self):
        return object


class TlsConnection(IOStream):
    """"""
    
    def accept_certificate(self, peer_cert=None, errors=None):
        """"""
        return object
    
    def handshake(self, cancellable=None):
        """"""
        return object
    
    def handshake_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def handshake_finish(self, result=None):
        """"""
        return object
    
    def emit_accept_certificate(self, peer_cert=None, errors=None):
        """"""
        return object
    
    def get_certificate(self):
        """"""
        return object
    
    def get_database(self):
        """"""
        return object
    
    def get_interaction(self):
        """"""
        return object
    
    def get_peer_certificate(self):
        """"""
        return object
    
    def get_peer_certificate_errors(self):
        """"""
        return object
    
    def get_rehandshake_mode(self):
        """"""
        return object
    
    def get_require_close_notify(self):
        """"""
        return object
    
    def get_use_system_certdb(self):
        """"""
        return object
    
    def handshake(self, cancellable=None):
        """"""
        return object
    
    def handshake_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def handshake_finish(self, result=None):
        """"""
        return object
    
    def set_certificate(self, certificate=None):
        """"""
        return object
    
    def set_database(self, database=None):
        """"""
        return object
    
    def set_interaction(self, interaction=None):
        """"""
        return object
    
    def set_rehandshake_mode(self, mode=None):
        """"""
        return object
    
    def set_require_close_notify(self, require_close_notify=None):
        """"""
        return object
    
    def set_use_system_certdb(self, use_system_certdb=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TlsConnectionClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def accept_certificate(self):
        return object

    @property
    def handshake(self):
        return object

    @property
    def handshake_async(self):
        return object

    @property
    def handshake_finish(self):
        return object

    @property
    def padding(self):
        return object


class TlsConnectionPrivate():
    """"""


class TlsDatabase(GObject.Object):
    """"""
    
    def create_certificate_handle(self, certificate=None):
        """"""
        return object
    
    def lookup_certificate_for_handle(self, handle=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def lookup_certificate_for_handle_async(self, handle=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_certificate_for_handle_finish(self, result=None):
        """"""
        return object
    
    def lookup_certificate_issuer(self, certificate=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def lookup_certificate_issuer_async(self, certificate=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_certificate_issuer_finish(self, result=None):
        """"""
        return object
    
    def lookup_certificates_issued_by(self, issuer_raw_dn=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def lookup_certificates_issued_by_async(self, issuer_raw_dn=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_certificates_issued_by_finish(self, result=None):
        """"""
        return object
    
    def verify_chain(self, chain=None, purpose=None, identity=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def verify_chain_async(self, chain=None, purpose=None, identity=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def verify_chain_finish(self, result=None):
        """"""
        return object
    
    def create_certificate_handle(self, certificate=None):
        """"""
        return object
    
    def lookup_certificate_for_handle(self, handle=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def lookup_certificate_for_handle_async(self, handle=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_certificate_for_handle_finish(self, result=None):
        """"""
        return object
    
    def lookup_certificate_issuer(self, certificate=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def lookup_certificate_issuer_async(self, certificate=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_certificate_issuer_finish(self, result=None):
        """"""
        return object
    
    def lookup_certificates_issued_by(self, issuer_raw_dn=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def lookup_certificates_issued_by_async(self, issuer_raw_dn=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def lookup_certificates_issued_by_finish(self, result=None):
        """"""
        return object
    
    def verify_chain(self, chain=None, purpose=None, identity=None, interaction=None, flags=None, cancellable=None):
        """"""
        return object
    
    def verify_chain_async(self, chain=None, purpose=None, identity=None, interaction=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def verify_chain_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TlsDatabaseClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def verify_chain(self):
        return object

    @property
    def verify_chain_async(self):
        return object

    @property
    def verify_chain_finish(self):
        return object

    @property
    def create_certificate_handle(self):
        return object

    @property
    def lookup_certificate_for_handle(self):
        return object

    @property
    def lookup_certificate_for_handle_async(self):
        return object

    @property
    def lookup_certificate_for_handle_finish(self):
        return object

    @property
    def lookup_certificate_issuer(self):
        return object

    @property
    def lookup_certificate_issuer_async(self):
        return object

    @property
    def lookup_certificate_issuer_finish(self):
        return object

    @property
    def lookup_certificates_issued_by(self):
        return object

    @property
    def lookup_certificates_issued_by_async(self):
        return object

    @property
    def lookup_certificates_issued_by_finish(self):
        return object

    @property
    def padding(self):
        return object


class TlsDatabasePrivate():
    """"""


class TlsFileDatabase():
    """"""
    @staticmethod
    def new(anchors=None):
        """"""
        return object


class TlsFileDatabaseInterface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def padding(self):
        return object


class TlsInteraction(GObject.Object):
    """"""
    
    def ask_password(self, password=None, cancellable=None):
        """"""
        return object
    
    def ask_password_async(self, password=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def ask_password_finish(self, result=None):
        """"""
        return object
    
    def request_certificate(self, connection=None, flags=None, cancellable=None):
        """"""
        return object
    
    def request_certificate_async(self, connection=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def request_certificate_finish(self, result=None):
        """"""
        return object
    
    def ask_password(self, password=None, cancellable=None):
        """"""
        return object
    
    def ask_password_async(self, password=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def ask_password_finish(self, result=None):
        """"""
        return object
    
    def invoke_ask_password(self, password=None, cancellable=None):
        """"""
        return object
    
    def invoke_request_certificate(self, connection=None, flags=None, cancellable=None):
        """"""
        return object
    
    def request_certificate(self, connection=None, flags=None, cancellable=None):
        """"""
        return object
    
    def request_certificate_async(self, connection=None, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def request_certificate_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TlsInteractionClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def ask_password(self):
        return object

    @property
    def ask_password_async(self):
        return object

    @property
    def ask_password_finish(self):
        return object

    @property
    def request_certificate(self):
        return object

    @property
    def request_certificate_async(self):
        return object

    @property
    def request_certificate_finish(self):
        return object

    @property
    def padding(self):
        return object


class TlsInteractionPrivate():
    """"""


class TlsPassword(GObject.Object):
    """"""
    
    def __init__(self, flags=None, description=None):
        """"""
        return object
    @staticmethod
    def new(flags=None, description=None):
        """"""
        return object
    
    def get_default_warning(self):
        """"""
        return object
    
    def get_value(self, length=None):
        """"""
        return object
    
    def set_value(self, value=None, length=None, destroy=None):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_value(self, length=None):
        """"""
        return object
    
    def get_warning(self):
        """"""
        return object
    
    def set_description(self, description=None):
        """"""
        return object
    
    def set_flags(self, flags=None):
        """"""
        return object
    
    def set_value(self, value=None, length=None):
        """"""
        return object
    
    def set_value_full(self, value=None, length=None, destroy=None):
        """"""
        return object
    
    def set_warning(self, warning=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class TlsPasswordClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_value(self):
        return object

    @property
    def set_value(self):
        return object

    @property
    def get_default_warning(self):
        return object

    @property
    def padding(self):
        return object


class TlsPasswordPrivate():
    """"""


class TlsServerConnection():
    """"""
    @staticmethod
    def new(base_io_stream=None, certificate=None):
        """"""
        return object


class TlsServerConnectionInterface():
    """"""

    @property
    def g_iface(self):
        return object


class UnixConnection(SocketConnection):
    """"""
    
    def receive_credentials(self, cancellable=None):
        """"""
        return object
    
    def receive_credentials_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def receive_credentials_finish(self, result=None):
        """"""
        return object
    
    def receive_fd(self, cancellable=None):
        """"""
        return object
    
    def send_credentials(self, cancellable=None):
        """"""
        return object
    
    def send_credentials_async(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def send_credentials_finish(self, result=None):
        """"""
        return object
    
    def send_fd(self, fd=None, cancellable=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class UnixConnectionClass():
    """"""

    @property
    def parent_class(self):
        return object


class UnixConnectionPrivate():
    """"""


class UnixCredentialsMessage(SocketControlMessage):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_with_credentials(credentials=None):
        """"""
        return object
    @staticmethod
    def is_supported():
        """"""
        return object
    
    def get_credentials(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class UnixCredentialsMessageClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object


class UnixCredentialsMessagePrivate():
    """"""


class UnixFDList(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_from_array(fds=None, n_fds=None):
        """"""
        return object
    
    def append(self, fd=None):
        """"""
        return object
    
    def get(self, index_=None):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def peek_fds(self, length=None):
        """"""
        return object
    
    def steal_fds(self, length=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class UnixFDListClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class UnixFDListPrivate():
    """"""


class UnixFDMessage(SocketControlMessage):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_with_fd_list(fd_list=None):
        """"""
        return object
    
    def append_fd(self, fd=None):
        """"""
        return object
    
    def get_fd_list(self):
        """"""
        return object
    
    def steal_fds(self, length=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class UnixFDMessageClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object


class UnixFDMessagePrivate():
    """"""


class UnixInputStream(InputStream, FileDescriptorBased, PollableInputStream):
    """"""
    
    def __init__(self, fd=None, close_fd=None):
        """"""
        return object
    @staticmethod
    def new(fd=None, close_fd=None):
        """"""
        return object
    
    def get_close_fd(self):
        """"""
        return object
    
    def get_fd(self):
        """"""
        return object
    
    def set_close_fd(self, close_fd=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class UnixInputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class UnixInputStreamPrivate():
    """"""


class UnixMountEntry():
    """"""


class UnixMountMonitor(GObject.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def get():
        """"""
        return object
    
    def set_rate_limit(self, limit_msec=None):
        """"""
        return object


class UnixMountMonitorClass():
    """"""


class UnixMountPoint():
    """"""
    
    def compare(self, mount2=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_device_path(self):
        """"""
        return object
    
    def get_fs_type(self):
        """"""
        return object
    
    def get_mount_path(self):
        """"""
        return object
    
    def get_options(self):
        """"""
        return object
    
    def guess_can_eject(self):
        """"""
        return object
    
    def guess_icon(self):
        """"""
        return object
    
    def guess_name(self):
        """"""
        return object
    
    def guess_symbolic_icon(self):
        """"""
        return object
    
    def is_loopback(self):
        """"""
        return object
    
    def is_readonly(self):
        """"""
        return object
    
    def is_user_mountable(self):
        """"""
        return object


class UnixOutputStream(OutputStream, FileDescriptorBased, PollableOutputStream):
    """"""
    
    def __init__(self, fd=None, close_fd=None):
        """"""
        return object
    @staticmethod
    def new(fd=None, close_fd=None):
        """"""
        return object
    
    def get_close_fd(self):
        """"""
        return object
    
    def get_fd(self):
        """"""
        return object
    
    def set_close_fd(self, close_fd=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class UnixOutputStreamClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object


class UnixOutputStreamPrivate():
    """"""


class UnixSocketAddressClass():
    """"""

    @property
    def parent_class(self):
        return object


class UnixSocketAddressPrivate():
    """"""


class Vfs(GObject.Object):
    """"""
    @staticmethod
    def get_default():
        """"""
        return object
    @staticmethod
    def get_local():
        """"""
        return object
    
    def add_writable_namespaces(self, list=None):
        """"""
        return object
    
    def deserialize_icon(self, value=None):
        """"""
        return object
    
    def get_file_for_path(self, path=None):
        """"""
        return object
    
    def get_file_for_uri(self, uri=None):
        """"""
        return object
    
    def get_supported_uri_schemes(self):
        """"""
        return object
    
    def is_active(self):
        """"""
        return object
    
    def local_file_add_info(self, filename=None, device=None, attribute_matcher=None, info=None, cancellable=None, extra_data=None, free_extra_data=None):
        """"""
        return object
    
    def local_file_moved(self, source=None, dest=None):
        """"""
        return object
    
    def local_file_removed(self, filename=None):
        """"""
        return object
    
    def local_file_set_attributes(self, filename=None, info=None, flags=None, cancellable=None):
        """"""
        return object
    
    def parse_name(self, parse_name=None):
        """"""
        return object
    
    def get_file_for_path(self, path=None):
        """"""
        return object
    
    def get_file_for_uri(self, uri=None):
        """"""
        return object
    
    def get_supported_uri_schemes(self):
        """"""
        return object
    
    def is_active(self):
        """"""
        return object
    
    def parse_name(self, parse_name=None):
        """"""
        return object
    
    def register_uri_scheme(self, scheme=None, uri_func=None, uri_data=None, uri_destroy=None, parse_name_func=None, parse_name_data=None, parse_name_destroy=None):
        """"""
        return object
    
    def unregister_uri_scheme(self, scheme=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object


class VfsClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def is_active(self):
        return object

    @property
    def get_file_for_path(self):
        return object

    @property
    def get_file_for_uri(self):
        return object

    @property
    def get_supported_uri_schemes(self):
        return object

    @property
    def parse_name(self):
        return object

    @property
    def local_file_add_info(self):
        return object

    @property
    def add_writable_namespaces(self):
        return object

    @property
    def local_file_set_attributes(self):
        return object

    @property
    def local_file_removed(self):
        return object

    @property
    def local_file_moved(self):
        return object

    @property
    def deserialize_icon(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object


class Volume():
    """"""
    
    def can_eject(self):
        """"""
        return object
    
    def can_mount(self):
        """"""
        return object
    
    def changed(self):
        """"""
        return object
    
    def eject(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_finish(self, result=None):
        """"""
        return object
    
    def eject_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_with_operation_finish(self, result=None):
        """"""
        return object
    
    def enumerate_identifiers(self):
        """"""
        return object
    
    def get_activation_root(self):
        """"""
        return object
    
    def get_drive(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_identifier(self, kind=None):
        """"""
        return object
    
    def get_mount(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_sort_key(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_uuid(self):
        """"""
        return object
    
    def mount_finish(self, result=None):
        """"""
        return object
    
    def mount_fn(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def removed(self):
        """"""
        return object
    
    def should_automount(self):
        """"""
        return object
    
    def can_eject(self):
        """"""
        return object
    
    def can_mount(self):
        """"""
        return object
    
    def eject(self, flags=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_finish(self, result=None):
        """"""
        return object
    
    def eject_with_operation(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def eject_with_operation_finish(self, result=None):
        """"""
        return object
    
    def enumerate_identifiers(self):
        """"""
        return object
    
    def get_activation_root(self):
        """"""
        return object
    
    def get_drive(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_identifier(self, kind=None):
        """"""
        return object
    
    def get_mount(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_sort_key(self):
        """"""
        return object
    
    def get_symbolic_icon(self):
        """"""
        return object
    
    def get_uuid(self):
        """"""
        return object
    
    def mount(self, flags=None, mount_operation=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def mount_finish(self, result=None):
        """"""
        return object
    
    def should_automount(self):
        """"""
        return object


class VolumeIface():
    """"""

    @property
    def g_iface(self):
        return object

    @property
    def changed(self):
        return object

    @property
    def removed(self):
        return object

    @property
    def get_name(self):
        return object

    @property
    def get_icon(self):
        return object

    @property
    def get_uuid(self):
        return object

    @property
    def get_drive(self):
        return object

    @property
    def get_mount(self):
        return object

    @property
    def can_mount(self):
        return object

    @property
    def can_eject(self):
        return object

    @property
    def mount_fn(self):
        return object

    @property
    def mount_finish(self):
        return object

    @property
    def eject(self):
        return object

    @property
    def eject_finish(self):
        return object

    @property
    def get_identifier(self):
        return object

    @property
    def enumerate_identifiers(self):
        return object

    @property
    def should_automount(self):
        return object

    @property
    def get_activation_root(self):
        return object

    @property
    def eject_with_operation(self):
        return object

    @property
    def eject_with_operation_finish(self):
        return object

    @property
    def get_sort_key(self):
        return object

    @property
    def get_symbolic_icon(self):
        return object


class VolumeMonitor(GObject.Object):
    """"""
    @staticmethod
    def adopt_orphan_mount(mount=None):
        """"""
        return object
    @staticmethod
    def get():
        """"""
        return object
    
    def drive_changed(self, drive=None):
        """"""
        return object
    
    def drive_connected(self, drive=None):
        """"""
        return object
    
    def drive_disconnected(self, drive=None):
        """"""
        return object
    
    def drive_eject_button(self, drive=None):
        """"""
        return object
    
    def drive_stop_button(self, drive=None):
        """"""
        return object
    
    def get_connected_drives(self):
        """"""
        return object
    
    def get_mount_for_uuid(self, uuid=None):
        """"""
        return object
    
    def get_mounts(self):
        """"""
        return object
    
    def get_volume_for_uuid(self, uuid=None):
        """"""
        return object
    
    def get_volumes(self):
        """"""
        return object
    
    def mount_added(self, mount=None):
        """"""
        return object
    
    def mount_changed(self, mount=None):
        """"""
        return object
    
    def mount_pre_unmount(self, mount=None):
        """"""
        return object
    
    def mount_removed(self, mount=None):
        """"""
        return object
    
    def volume_added(self, volume=None):
        """"""
        return object
    
    def volume_changed(self, volume=None):
        """"""
        return object
    
    def volume_removed(self, volume=None):
        """"""
        return object
    
    def get_connected_drives(self):
        """"""
        return object
    
    def get_mount_for_uuid(self, uuid=None):
        """"""
        return object
    
    def get_mounts(self):
        """"""
        return object
    
    def get_volume_for_uuid(self, uuid=None):
        """"""
        return object
    
    def get_volumes(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class VolumeMonitorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def volume_added(self):
        return object

    @property
    def volume_removed(self):
        return object

    @property
    def volume_changed(self):
        return object

    @property
    def mount_added(self):
        return object

    @property
    def mount_removed(self):
        return object

    @property
    def mount_pre_unmount(self):
        return object

    @property
    def mount_changed(self):
        return object

    @property
    def drive_connected(self):
        return object

    @property
    def drive_disconnected(self):
        return object

    @property
    def drive_changed(self):
        return object

    @property
    def is_supported(self):
        return object

    @property
    def get_connected_drives(self):
        return object

    @property
    def get_volumes(self):
        return object

    @property
    def get_mounts(self):
        return object

    @property
    def get_volume_for_uuid(self):
        return object

    @property
    def get_mount_for_uuid(self):
        return object

    @property
    def adopt_orphan_mount(self):
        return object

    @property
    def drive_eject_button(self):
        return object

    @property
    def drive_stop_button(self):
        return object

    @property
    def _g_reserved1(self):
        return object

    @property
    def _g_reserved2(self):
        return object

    @property
    def _g_reserved3(self):
        return object

    @property
    def _g_reserved4(self):
        return object

    @property
    def _g_reserved5(self):
        return object

    @property
    def _g_reserved6(self):
        return object


class ZlibCompressor(GObject.Object, Converter):
    """"""
    
    def __init__(self, format=None, level=None):
        """"""
        return object
    @staticmethod
    def new(format=None, level=None):
        """"""
        return object
    
    def get_file_info(self):
        """"""
        return object
    
    def set_file_info(self, file_info=None):
        """"""
        return object


class ZlibCompressorClass():
    """"""

    @property
    def parent_class(self):
        return object


class ZlibDecompressor(GObject.Object, Converter):
    """"""
    
    def __init__(self, format=None):
        """"""
        return object
    @staticmethod
    def new(format=None):
        """"""
        return object
    
    def get_file_info(self):
        """"""
        return object


class ZlibDecompressorClass():
    """"""

    @property
    def parent_class(self):
        return object


class BytesIcon(GObject.Object, Icon, LoadableIcon):
    """"""
    
    def __init__(self, bytes=None):
        """"""
        return object
    @staticmethod
    def new(bytes=None):
        """"""
        return object
    
    def get_bytes(self):
        """"""
        return object


class CharsetConverter(GObject.Object, Converter, Initable):
    """"""
    
    def __init__(self, to_charset=None, from_charset=None):
        """"""
        return object
    @staticmethod
    def new(to_charset=None, from_charset=None):
        """"""
        return object
    
    def get_num_fallbacks(self):
        """"""
        return object
    
    def get_use_fallback(self):
        """"""
        return object
    
    def set_use_fallback(self, use_fallback=None):
        """"""
        return object


class DBusActionGroup(GObject.Object, ActionGroup, RemoteActionGroup):
    """"""
    @staticmethod
    def get(connection=None, bus_name=None, object_path=None):
        """"""
        return object


class DBusConnection(GObject.Object, AsyncInitable, Initable):
    """"""
    @staticmethod
    def new_finish(res=None):
        """"""
        return object
    @staticmethod
    def new_for_address_finish(res=None):
        """"""
        return object
    @staticmethod
    def new_for_address_sync(address=None, flags=None, observer=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def new_sync(stream=None, guid=None, flags=None, observer=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def new(stream=None, guid=None, flags=None, observer=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    @staticmethod
    def new_for_address(address=None, flags=None, observer=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def add_filter(self, filter_function=None, user_data=None, user_data_free_func=None):
        """"""
        return object
    
    def call(self, bus_name=None, object_path=None, interface_name=None, method_name=None, parameters=None, reply_type=None, flags=None, timeout_msec=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def call_finish(self, res=None):
        """"""
        return object
    
    def call_sync(self, bus_name=None, object_path=None, interface_name=None, method_name=None, parameters=None, reply_type=None, flags=None, timeout_msec=None, cancellable=None):
        """"""
        return object
    
    def call_with_unix_fd_list(self, bus_name=None, object_path=None, interface_name=None, method_name=None, parameters=None, reply_type=None, flags=None, timeout_msec=None, fd_list=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def call_with_unix_fd_list_finish(self, out_fd_list=None, res=None):
        """"""
        return object
    
    def call_with_unix_fd_list_sync(self, bus_name=None, object_path=None, interface_name=None, method_name=None, parameters=None, reply_type=None, flags=None, timeout_msec=None, fd_list=None, out_fd_list=None, cancellable=None):
        """"""
        return object
    
    def close(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def close_finish(self, res=None):
        """"""
        return object
    
    def close_sync(self, cancellable=None):
        """"""
        return object
    
    def emit_signal(self, destination_bus_name=None, object_path=None, interface_name=None, signal_name=None, parameters=None):
        """"""
        return object
    
    def export_action_group(self, object_path=None, action_group=None):
        """"""
        return object
    
    def export_menu_model(self, object_path=None, menu=None):
        """"""
        return object
    
    def flush(self, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def flush_finish(self, res=None):
        """"""
        return object
    
    def flush_sync(self, cancellable=None):
        """"""
        return object
    
    def get_capabilities(self):
        """"""
        return object
    
    def get_exit_on_close(self):
        """"""
        return object
    
    def get_guid(self):
        """"""
        return object
    
    def get_last_serial(self):
        """"""
        return object
    
    def get_peer_credentials(self):
        """"""
        return object
    
    def get_stream(self):
        """"""
        return object
    
    def get_unique_name(self):
        """"""
        return object
    
    def is_closed(self):
        """"""
        return object
    
    def register_object(self, object_path=None, interface_info=None, vtable=None, user_data=None, user_data_free_func=None):
        """"""
        return object
    
    def register_object_with_closures(self, object_path=None, interface_info=None, method_call_closure=None, get_property_closure=None, set_property_closure=None):
        """"""
        return object
    
    def register_subtree(self, object_path=None, vtable=None, flags=None, user_data=None, user_data_free_func=None):
        """"""
        return object
    
    def remove_filter(self, filter_id=None):
        """"""
        return object
    
    def send_message(self, message=None, flags=None, out_serial=None):
        """"""
        return object
    
    def send_message_with_reply(self, message=None, flags=None, timeout_msec=None, out_serial=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def send_message_with_reply_finish(self, res=None):
        """"""
        return object
    
    def send_message_with_reply_sync(self, message=None, flags=None, timeout_msec=None, out_serial=None, cancellable=None):
        """"""
        return object
    
    def set_exit_on_close(self, exit_on_close=None):
        """"""
        return object
    
    def signal_subscribe(self, sender=None, interface_name=None, member=None, object_path=None, arg0=None, flags=None, callback=None, user_data=None, user_data_free_func=None):
        """"""
        return object
    
    def signal_unsubscribe(self, subscription_id=None):
        """"""
        return object
    
    def start_message_processing(self):
        """"""
        return object
    
    def unexport_action_group(self, export_id=None):
        """"""
        return object
    
    def unexport_menu_model(self, export_id=None):
        """"""
        return object
    
    def unregister_object(self, registration_id=None):
        """"""
        return object
    
    def unregister_subtree(self, registration_id=None):
        """"""
        return object


class DBusMenuModel(MenuModel):
    """"""
    @staticmethod
    def get(connection=None, bus_name=None, object_path=None):
        """"""
        return object


class DBusObjectManagerClient(GObject.Object, AsyncInitable, DBusObjectManager, Initable):
    """"""
    @staticmethod
    def new_finish(res=None):
        """"""
        return object
    @staticmethod
    def new_for_bus_finish(res=None):
        """"""
        return object
    @staticmethod
    def new_for_bus_sync(bus_type=None, flags=None, name=None, object_path=None, get_proxy_type_func=None, get_proxy_type_user_data=None, get_proxy_type_destroy_notify=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def new_sync(connection=None, flags=None, name=None, object_path=None, get_proxy_type_func=None, get_proxy_type_user_data=None, get_proxy_type_destroy_notify=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def new(connection=None, flags=None, name=None, object_path=None, get_proxy_type_func=None, get_proxy_type_user_data=None, get_proxy_type_destroy_notify=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    @staticmethod
    def new_for_bus(bus_type=None, flags=None, name=None, object_path=None, get_proxy_type_func=None, get_proxy_type_user_data=None, get_proxy_type_destroy_notify=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def interface_proxy_properties_changed(self, object_proxy=None, interface_proxy=None, changed_properties=None, invalidated_properties=None):
        """"""
        return object
    
    def interface_proxy_signal(self, object_proxy=None, interface_proxy=None, sender_name=None, signal_name=None, parameters=None):
        """"""
        return object
    
    def get_connection(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_name_owner(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DBusProxy(GObject.Object, AsyncInitable, DBusInterface, Initable):
    """"""
    @staticmethod
    def new_finish(res=None):
        """"""
        return object
    @staticmethod
    def new_for_bus_finish(res=None):
        """"""
        return object
    @staticmethod
    def new_for_bus_sync(bus_type=None, flags=None, info=None, name=None, object_path=None, interface_name=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def new_sync(connection=None, flags=None, info=None, name=None, object_path=None, interface_name=None, cancellable=None):
        """"""
        return object
    @staticmethod
    def new(connection=None, flags=None, info=None, name=None, object_path=None, interface_name=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    @staticmethod
    def new_for_bus(bus_type=None, flags=None, info=None, name=None, object_path=None, interface_name=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def g_properties_changed(self, changed_properties=None, invalidated_properties=None):
        """"""
        return object
    
    def g_signal(self, sender_name=None, signal_name=None, parameters=None):
        """"""
        return object
    
    def call(self, method_name=None, parameters=None, flags=None, timeout_msec=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def call_finish(self, res=None):
        """"""
        return object
    
    def call_sync(self, method_name=None, parameters=None, flags=None, timeout_msec=None, cancellable=None):
        """"""
        return object
    
    def call_with_unix_fd_list(self, method_name=None, parameters=None, flags=None, timeout_msec=None, fd_list=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def call_with_unix_fd_list_finish(self, out_fd_list=None, res=None):
        """"""
        return object
    
    def call_with_unix_fd_list_sync(self, method_name=None, parameters=None, flags=None, timeout_msec=None, fd_list=None, out_fd_list=None, cancellable=None):
        """"""
        return object
    
    def get_cached_property(self, property_name=None):
        """"""
        return object
    
    def get_cached_property_names(self):
        """"""
        return object
    
    def get_connection(self):
        """"""
        return object
    
    def get_default_timeout(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_interface_info(self):
        """"""
        return object
    
    def get_interface_name(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_name_owner(self):
        """"""
        return object
    
    def get_object_path(self):
        """"""
        return object
    
    def set_cached_property(self, property_name=None, value=None):
        """"""
        return object
    
    def set_default_timeout(self, timeout_msec=None):
        """"""
        return object
    
    def set_interface_info(self, info=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DBusServer(GObject.Object, Initable):
    """"""
    @staticmethod
    def new_sync(address=None, flags=None, guid=None, observer=None, cancellable=None):
        """"""
        return object
    
    def get_client_address(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_guid(self):
        """"""
        return object
    
    def is_active(self):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object


class Emblem(GObject.Object, Icon):
    """"""
    
    def __init__(self, icon=None):
        """"""
        return object
    @staticmethod
    def new(icon=None):
        """"""
        return object
    @staticmethod
    def new_with_origin(icon=None, origin=None):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object
    
    def get_origin(self):
        """"""
        return object


class EmblemedIcon(GObject.Object, Icon):
    """"""
    
    def __init__(self, icon=None, emblem=None):
        """"""
        return object
    @staticmethod
    def new(icon=None, emblem=None):
        """"""
        return object
    
    def add_emblem(self, emblem=None):
        """"""
        return object
    
    def clear_emblems(self):
        """"""
        return object
    
    def get_emblems(self):
        """"""
        return object
    
    def get_icon(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class FileIOStream(IOStream, Seekable):
    """"""
    
    def can_seek(self):
        """"""
        return object
    
    def can_truncate(self):
        """"""
        return object
    
    def get_etag(self):
        """"""
        return object
    
    def query_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, result=None):
        """"""
        return object
    
    def seek(self, offset=None, type=None, cancellable=None):
        """"""
        return object
    
    def tell(self):
        """"""
        return object
    
    def truncate_fn(self, size=None, cancellable=None):
        """"""
        return object
    
    def get_etag(self):
        """"""
        return object
    
    def query_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class FileIcon(GObject.Object, Icon, LoadableIcon):
    """"""
    
    def __init__(self, file=None):
        """"""
        return object
    @staticmethod
    def new(file=None):
        """"""
        return object
    
    def get_file(self):
        """"""
        return object


class FileInputStream(InputStream, Seekable):
    """"""
    
    def can_seek(self):
        """"""
        return object
    
    def query_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, result=None):
        """"""
        return object
    
    def seek(self, offset=None, type=None, cancellable=None):
        """"""
        return object
    
    def tell(self):
        """"""
        return object
    
    def query_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class FileOutputStream(OutputStream, Seekable):
    """"""
    
    def can_seek(self):
        """"""
        return object
    
    def can_truncate(self):
        """"""
        return object
    
    def get_etag(self):
        """"""
        return object
    
    def query_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, result=None):
        """"""
        return object
    
    def seek(self, offset=None, type=None, cancellable=None):
        """"""
        return object
    
    def tell(self):
        """"""
        return object
    
    def truncate_fn(self, size=None, cancellable=None):
        """"""
        return object
    
    def get_etag(self):
        """"""
        return object
    
    def query_info(self, attributes=None, cancellable=None):
        """"""
        return object
    
    def query_info_async(self, attributes=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def query_info_finish(self, result=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class FilterInputStream(InputStream):
    """"""
    
    def get_base_stream(self):
        """"""
        return object
    
    def get_close_base_stream(self):
        """"""
        return object
    
    def set_close_base_stream(self, close_base=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def base_stream(self):
        return object


class FilterOutputStream(OutputStream):
    """"""
    
    def get_base_stream(self):
        """"""
        return object
    
    def get_close_base_stream(self):
        """"""
        return object
    
    def set_close_base_stream(self, close_base=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def base_stream(self):
        return object


class InetAddressMask(GObject.Object, Initable):
    """"""
    
    def __init__(self, addr=None, length=None):
        """"""
        return object
    @staticmethod
    def new(addr=None, length=None):
        """"""
        return object
    @staticmethod
    def new_from_string(mask_string=None):
        """"""
        return object
    
    def equal(self, mask2=None):
        """"""
        return object
    
    def get_address(self):
        """"""
        return object
    
    def get_family(self):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def matches(self, address=None):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class MemoryInputStream(InputStream, PollableInputStream, Seekable):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_from_bytes(bytes=None):
        """"""
        return object
    @staticmethod
    def new_from_data(data=None, len=None, destroy=None):
        """"""
        return object
    
    def add_bytes(self, bytes=None):
        """"""
        return object
    
    def add_data(self, data=None, len=None, destroy=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class MemoryOutputStream(OutputStream, PollableOutputStream, Seekable):
    """"""
    
    def __init__(self, data=None, size=None, realloc_function=None, destroy_function=None):
        """"""
        return object
    @staticmethod
    def new(data=None, size=None, realloc_function=None, destroy_function=None):
        """"""
        return object
    @staticmethod
    def new_resizable():
        """"""
        return object
    
    def get_data(self):
        """"""
        return object
    
    def get_data_size(self):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def steal_as_bytes(self):
        """"""
        return object
    
    def steal_data(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class Menu(MenuModel):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def append(self, label=None, detailed_action=None):
        """"""
        return object
    
    def append_item(self, item=None):
        """"""
        return object
    
    def append_section(self, label=None, section=None):
        """"""
        return object
    
    def append_submenu(self, label=None, submenu=None):
        """"""
        return object
    
    def freeze(self):
        """"""
        return object
    
    def insert(self, position=None, label=None, detailed_action=None):
        """"""
        return object
    
    def insert_item(self, position=None, item=None):
        """"""
        return object
    
    def insert_section(self, position=None, label=None, section=None):
        """"""
        return object
    
    def insert_submenu(self, position=None, label=None, submenu=None):
        """"""
        return object
    
    def prepend(self, label=None, detailed_action=None):
        """"""
        return object
    
    def prepend_item(self, item=None):
        """"""
        return object
    
    def prepend_section(self, label=None, section=None):
        """"""
        return object
    
    def prepend_submenu(self, label=None, submenu=None):
        """"""
        return object
    
    def remove(self, position=None):
        """"""
        return object
    
    def remove_all(self):
        """"""
        return object


class NativeVolumeMonitor(VolumeMonitor):
    """"""

    @property
    def parent_instance(self):
        return object


class NetworkAddress(GObject.Object, SocketConnectable):
    """"""
    
    def __init__(self, hostname=None, port=None):
        """"""
        return object
    @staticmethod
    def new(hostname=None, port=None):
        """"""
        return object
    @staticmethod
    def new_loopback(port=None):
        """"""
        return object
    @staticmethod
    def parse(host_and_port=None, default_port=None):
        """"""
        return object
    @staticmethod
    def parse_uri(uri=None, default_port=None):
        """"""
        return object
    
    def get_hostname(self):
        """"""
        return object
    
    def get_port(self):
        """"""
        return object
    
    def get_scheme(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class NetworkService(GObject.Object, SocketConnectable):
    """"""
    
    def __init__(self, service=None, protocol=None, domain=None):
        """"""
        return object
    @staticmethod
    def new(service=None, protocol=None, domain=None):
        """"""
        return object
    
    def get_domain(self):
        """"""
        return object
    
    def get_protocol(self):
        """"""
        return object
    
    def get_scheme(self):
        """"""
        return object
    
    def get_service(self):
        """"""
        return object
    
    def set_scheme(self, scheme=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ProxyAddressEnumerator(SocketAddressEnumerator):
    """"""

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class SocketAddress(GObject.Object, SocketConnectable):
    """"""
    @staticmethod
    def new_from_native(native=None, len=None):
        """"""
        return object
    
    def get_family(self):
        """"""
        return object
    
    def get_native_size(self):
        """"""
        return object
    
    def to_native(self, dest=None, destlen=None):
        """"""
        return object
    
    def get_family(self):
        """"""
        return object
    
    def get_native_size(self):
        """"""
        return object
    
    def to_native(self, dest=None, destlen=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object


class UnixSocketAddress(SocketAddress, SocketConnectable):
    """"""
    
    def __init__(self, path=None):
        """"""
        return object
    @staticmethod
    def new(path=None):
        """"""
        return object
    @staticmethod
    def new_abstract(path=None, path_len=None):
        """"""
        return object
    @staticmethod
    def new_with_type(path=None, path_len=None, type=None):
        """"""
        return object
    @staticmethod
    def abstract_names_supported():
        """"""
        return object
    
    def get_address_type(self):
        """"""
        return object
    
    def get_is_abstract(self):
        """"""
        return object
    
    def get_path(self):
        """"""
        return object
    
    def get_path_len(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class BufferedInputStream(FilterInputStream, Seekable):
    """"""
    
    def __init__(self, base_stream=None):
        """"""
        return object
    @staticmethod
    def new(base_stream=None):
        """"""
        return object
    @staticmethod
    def new_sized(base_stream=None, size=None):
        """"""
        return object
    
    def fill(self, count=None, cancellable=None):
        """"""
        return object
    
    def fill_async(self, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def fill_finish(self, result=None):
        """"""
        return object
    
    def fill(self, count=None, cancellable=None):
        """"""
        return object
    
    def fill_async(self, count=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def fill_finish(self, result=None):
        """"""
        return object
    
    def get_available(self):
        """"""
        return object
    
    def get_buffer_size(self):
        """"""
        return object
    
    def peek(self, buffer=None, offset=None, count=None):
        """"""
        return object
    
    def peek_buffer(self, count=None):
        """"""
        return object
    
    def read_byte(self, cancellable=None):
        """"""
        return object
    
    def set_buffer_size(self, size=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class BufferedOutputStream(FilterOutputStream, Seekable):
    """"""
    
    def __init__(self, base_stream=None):
        """"""
        return object
    @staticmethod
    def new(base_stream=None):
        """"""
        return object
    @staticmethod
    def new_sized(base_stream=None, size=None):
        """"""
        return object
    
    def get_auto_grow(self):
        """"""
        return object
    
    def get_buffer_size(self):
        """"""
        return object
    
    def set_auto_grow(self, auto_grow=None):
        """"""
        return object
    
    def set_buffer_size(self, size=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ConverterInputStream(FilterInputStream, PollableInputStream):
    """"""
    
    def __init__(self, base_stream=None, converter=None):
        """"""
        return object
    @staticmethod
    def new(base_stream=None, converter=None):
        """"""
        return object
    
    def get_converter(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ConverterOutputStream(FilterOutputStream, PollableOutputStream):
    """"""
    
    def __init__(self, base_stream=None, converter=None):
        """"""
        return object
    @staticmethod
    def new(base_stream=None, converter=None):
        """"""
        return object
    
    def get_converter(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DataInputStream(BufferedInputStream, Seekable):
    """"""
    
    def __init__(self, base_stream=None):
        """"""
        return object
    @staticmethod
    def new(base_stream=None):
        """"""
        return object
    
    def get_byte_order(self):
        """"""
        return object
    
    def get_newline_type(self):
        """"""
        return object
    
    def read_byte(self, cancellable=None):
        """"""
        return object
    
    def read_int16(self, cancellable=None):
        """"""
        return object
    
    def read_int32(self, cancellable=None):
        """"""
        return object
    
    def read_int64(self, cancellable=None):
        """"""
        return object
    
    def read_line(self, length=None, cancellable=None):
        """"""
        return object
    
    def read_line_async(self, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_line_finish(self, result=None, length=None):
        """"""
        return object
    
    def read_line_finish_utf8(self, result=None, length=None):
        """"""
        return object
    
    def read_line_utf8(self, length=None, cancellable=None):
        """"""
        return object
    
    def read_uint16(self, cancellable=None):
        """"""
        return object
    
    def read_uint32(self, cancellable=None):
        """"""
        return object
    
    def read_uint64(self, cancellable=None):
        """"""
        return object
    
    def read_until(self, stop_chars=None, length=None, cancellable=None):
        """"""
        return object
    
    def read_until_async(self, stop_chars=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_until_finish(self, result=None, length=None):
        """"""
        return object
    
    def read_upto(self, stop_chars=None, stop_chars_len=None, length=None, cancellable=None):
        """"""
        return object
    
    def read_upto_async(self, stop_chars=None, stop_chars_len=None, io_priority=None, cancellable=None, callback=None, user_data=None):
        """"""
        return object
    
    def read_upto_finish(self, result=None, length=None):
        """"""
        return object
    
    def set_byte_order(self, order=None):
        """"""
        return object
    
    def set_newline_type(self, type=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class DataOutputStream(FilterOutputStream, Seekable):
    """"""
    
    def __init__(self, base_stream=None):
        """"""
        return object
    @staticmethod
    def new(base_stream=None):
        """"""
        return object
    
    def get_byte_order(self):
        """"""
        return object
    
    def put_byte(self, data=None, cancellable=None):
        """"""
        return object
    
    def put_int16(self, data=None, cancellable=None):
        """"""
        return object
    
    def put_int32(self, data=None, cancellable=None):
        """"""
        return object
    
    def put_int64(self, data=None, cancellable=None):
        """"""
        return object
    
    def put_string(self, str=None, cancellable=None):
        """"""
        return object
    
    def put_uint16(self, data=None, cancellable=None):
        """"""
        return object
    
    def put_uint32(self, data=None, cancellable=None):
        """"""
        return object
    
    def put_uint64(self, data=None, cancellable=None):
        """"""
        return object
    
    def set_byte_order(self, order=None):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class InetSocketAddress(SocketAddress, SocketConnectable):
    """"""
    
    def __init__(self, address=None, port=None):
        """"""
        return object
    @staticmethod
    def new(address=None, port=None):
        """"""
        return object
    @staticmethod
    def new_from_string(address=None, port=None):
        """"""
        return object
    
    def get_address(self):
        """"""
        return object
    
    def get_flowinfo(self):
        """"""
        return object
    
    def get_port(self):
        """"""
        return object
    
    def get_scope_id(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object


class ProxyAddress(InetSocketAddress, SocketConnectable):
    """"""
    
    def __init__(self, inetaddr=None, port=None, protocol=None, dest_hostname=None, dest_port=None, username=None, password=None):
        """"""
        return object
    @staticmethod
    def new(inetaddr=None, port=None, protocol=None, dest_hostname=None, dest_port=None, username=None, password=None):
        """"""
        return object
    
    def get_destination_hostname(self):
        """"""
        return object
    
    def get_destination_port(self):
        """"""
        return object
    
    def get_destination_protocol(self):
        """"""
        return object
    
    def get_password(self):
        """"""
        return object
    
    def get_protocol(self):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_username(self):
        """"""
        return object

    @property
    def parent_instance(self):
        return object

    @property
    def priv(self):
        return object
