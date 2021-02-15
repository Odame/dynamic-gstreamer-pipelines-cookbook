# -*- coding: utf-8 -*-
ANALYZER_ANALYZING = r"""1"""
ASCII_DTOSTR_BUF_SIZE = r"""39"""


class AsciiType:
    """"""
    ALNUM = 1
    ALPHA = 2
    CNTRL = 4
    DIGIT = 8
    GRAPH = 16
    LOWER = 32
    PRINT = 64
    PUNCT = 128
    SPACE = 256
    UPPER = 512
    XDIGIT = 1024
BIG_ENDIAN = r"""4321"""


class BookmarkFileError:
    """"""
    INVALID_URI = 0
    INVALID_VALUE = 1
    APP_NOT_REGISTERED = 2
    URI_NOT_FOUND = 3
    READ = 4
    UNKNOWN_ENCODING = 5
    WRITE = 6
    FILE_NOT_FOUND = 7
CSET_A_2_Z = r"""ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
CSET_DIGITS = r"""0123456789"""
CSET_a_2_z = r"""abcdefghijklmnopqrstuvwxyz"""


class ChecksumType:
    """"""
    MD5 = 0
    SHA1 = 1
    SHA256 = 2
    SHA512 = 3
    SHA384 = 4


class ConvertError:
    """"""
    NO_CONVERSION = 0
    ILLEGAL_SEQUENCE = 1
    FAILED = 2
    PARTIAL_INPUT = 3
    BAD_URI = 4
    NOT_ABSOLUTE_PATH = 5
    NO_MEMORY = 6
    EMBEDDED_NUL = 7
DATALIST_FLAGS_MASK = r"""3"""
DATE_BAD_DAY = r"""0"""
DATE_BAD_JULIAN = r"""0"""
DATE_BAD_YEAR = r"""0"""
DIR_SEPARATOR = r"""47"""
DIR_SEPARATOR_S = r"""/"""


class DateDMY:
    """"""
    DAY = 0
    MONTH = 1
    YEAR = 2


class DateMonth:
    """"""
    BAD_MONTH = 0
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12


class DateWeekday:
    """"""
    BAD_WEEKDAY = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
E = r"""2.718282"""


class ErrorType:
    """"""
    UNKNOWN = 0
    UNEXP_EOF = 1
    UNEXP_EOF_IN_STRING = 2
    UNEXP_EOF_IN_COMMENT = 3
    NON_DIGIT_IN_CONST = 4
    DIGIT_RADIX = 5
    FLOAT_RADIX = 6
    FLOAT_MALFORMED = 7


class FileError:
    """"""
    EXIST = 0
    ISDIR = 1
    ACCES = 2
    NAMETOOLONG = 3
    NOENT = 4
    NOTDIR = 5
    NXIO = 6
    NODEV = 7
    ROFS = 8
    TXTBSY = 9
    FAULT = 10
    LOOP = 11
    NOSPC = 12
    NOMEM = 13
    MFILE = 14
    NFILE = 15
    BADF = 16
    INVAL = 17
    PIPE = 18
    AGAIN = 19
    INTR = 20
    IO = 21
    PERM = 22
    NOSYS = 23
    FAILED = 24


class FileTest:
    """"""
    IS_REGULAR = 1
    IS_SYMLINK = 2
    IS_DIR = 4
    IS_EXECUTABLE = 8
    EXISTS = 16


class FormatSizeFlags:
    """"""
    DEFAULT = 0
    LONG_FORMAT = 1
    IEC_UNITS = 2
    BITS = 4
GINT16_FORMAT = r"""hi"""
GINT16_MODIFIER = r"""h"""
GINT32_FORMAT = r"""i"""
GINT32_MODIFIER = r"""None"""
GINT64_FORMAT = r"""li"""
GINT64_MODIFIER = r"""l"""
GINTPTR_FORMAT = r"""li"""
GINTPTR_MODIFIER = r"""l"""
GNUC_FUNCTION = r"""None"""
GNUC_PRETTY_FUNCTION = r"""None"""
GSIZE_FORMAT = r"""lu"""
GSIZE_MODIFIER = r"""l"""
GSSIZE_FORMAT = r"""li"""
GSSIZE_MODIFIER = r"""l"""
GUINT16_FORMAT = r"""hu"""
GUINT32_FORMAT = r"""u"""
GUINT64_FORMAT = r"""lu"""
GUINTPTR_FORMAT = r"""lu"""
HAVE_GINT64 = r"""1"""
HAVE_GNUC_VARARGS = r"""1"""
HAVE_GNUC_VISIBILITY = r"""1"""
HAVE_GROWING_STACK = r"""0"""
HAVE_ISO_VARARGS = r"""1"""
HOOK_FLAG_USER_SHIFT = r"""4"""


class HookFlagMask:
    """"""
    ACTIVE = 1
    IN_CALL = 2
    MASK = 15
IEEE754_DOUBLE_BIAS = r"""1023"""
IEEE754_FLOAT_BIAS = r"""127"""


class IOChannelError:
    """"""
    FBIG = 0
    INVAL = 1
    IO = 2
    ISDIR = 3
    NOSPC = 4
    NXIO = 5
    OVERFLOW = 6
    PIPE = 7
    FAILED = 8


class IOCondition:
    """"""
    IN = 1
    OUT = 4
    PRI = 2
    ERR = 8
    HUP = 16
    NVAL = 32


class IOError:
    """"""
    NONE = 0
    AGAIN = 1
    INVAL = 2
    UNKNOWN = 3


class IOFlags:
    """"""
    APPEND = 1
    NONBLOCK = 2
    IS_READABLE = 4
    IS_WRITABLE = 8
    IS_WRITEABLE = 8
    IS_SEEKABLE = 16
    MASK = 31
    GET_MASK = 31
    SET_MASK = 3


class IOStatus:
    """"""
    ERROR = 0
    NORMAL = 1
    EOF = 2
    AGAIN = 3
KEY_FILE_DESKTOP_ACTION_GROUP_PREFIX = r"""Desktop Action"""
KEY_FILE_DESKTOP_GROUP = r"""Desktop Entry"""
KEY_FILE_DESKTOP_KEY_ACTIONS = r"""Actions"""
KEY_FILE_DESKTOP_KEY_CATEGORIES = r"""Categories"""
KEY_FILE_DESKTOP_KEY_COMMENT = r"""Comment"""
KEY_FILE_DESKTOP_KEY_DBUS_ACTIVATABLE = r"""DBusActivatable"""
KEY_FILE_DESKTOP_KEY_EXEC = r"""Exec"""
KEY_FILE_DESKTOP_KEY_FULLNAME = r"""X-GNOME-FullName"""
KEY_FILE_DESKTOP_KEY_GENERIC_NAME = r"""GenericName"""
KEY_FILE_DESKTOP_KEY_GETTEXT_DOMAIN = r"""X-GNOME-Gettext-Domain"""
KEY_FILE_DESKTOP_KEY_HIDDEN = r"""Hidden"""
KEY_FILE_DESKTOP_KEY_ICON = r"""Icon"""
KEY_FILE_DESKTOP_KEY_KEYWORDS = r"""Keywords"""
KEY_FILE_DESKTOP_KEY_MIME_TYPE = r"""MimeType"""
KEY_FILE_DESKTOP_KEY_NAME = r"""Name"""
KEY_FILE_DESKTOP_KEY_NOT_SHOW_IN = r"""NotShowIn"""
KEY_FILE_DESKTOP_KEY_NO_DISPLAY = r"""NoDisplay"""
KEY_FILE_DESKTOP_KEY_ONLY_SHOW_IN = r"""OnlyShowIn"""
KEY_FILE_DESKTOP_KEY_PATH = r"""Path"""
KEY_FILE_DESKTOP_KEY_STARTUP_NOTIFY = r"""StartupNotify"""
KEY_FILE_DESKTOP_KEY_STARTUP_WM_CLASS = r"""StartupWMClass"""
KEY_FILE_DESKTOP_KEY_TERMINAL = r"""Terminal"""
KEY_FILE_DESKTOP_KEY_TRY_EXEC = r"""TryExec"""
KEY_FILE_DESKTOP_KEY_TYPE = r"""Type"""
KEY_FILE_DESKTOP_KEY_URL = r"""URL"""
KEY_FILE_DESKTOP_KEY_VERSION = r"""Version"""
KEY_FILE_DESKTOP_TYPE_APPLICATION = r"""Application"""
KEY_FILE_DESKTOP_TYPE_DIRECTORY = r"""Directory"""
KEY_FILE_DESKTOP_TYPE_LINK = r"""Link"""


class KeyFileError:
    """"""
    UNKNOWN_ENCODING = 0
    PARSE = 1
    NOT_FOUND = 2
    KEY_NOT_FOUND = 3
    GROUP_NOT_FOUND = 4
    INVALID_VALUE = 5


class KeyFileFlags:
    """"""
    NONE = 0
    KEEP_COMMENTS = 1
    KEEP_TRANSLATIONS = 2
LITTLE_ENDIAN = r"""1234"""
LN10 = r"""2.302585"""
LN2 = r"""0.693147"""
LOG_2_BASE_10 = r"""0.301030"""
LOG_DOMAIN = r"""0"""
LOG_FATAL_MASK = r"""5"""
LOG_LEVEL_USER_SHIFT = r"""8"""


class LogLevelFlags:
    """"""
    FLAG_RECURSION = 1
    FLAG_FATAL = 2
    LEVEL_ERROR = 4
    LEVEL_CRITICAL = 8
    LEVEL_WARNING = 16
    LEVEL_MESSAGE = 32
    LEVEL_INFO = 64
    LEVEL_DEBUG = 128
    LEVEL_MASK = -4


class LogWriterOutput:
    """"""
    HANDLED = 1
    UNHANDLED = 0
MAJOR_VERSION = r"""2"""
MAXINT16 = r"""32767"""
MAXINT32 = r"""2147483647"""
MAXINT64 = r"""9223372036854775807"""
MAXINT8 = r"""127"""
MAXUINT16 = r"""65535"""
MAXUINT32 = r"""4294967295"""
MAXUINT64 = r"""18446744073709551615"""
MAXUINT8 = r"""255"""
MICRO_VERSION = r"""1"""
MININT16 = r"""-32768"""
MININT32 = r"""-2147483648"""
MININT64 = r"""-9223372036854775808"""
MININT8 = r"""-128"""
MINOR_VERSION = r"""56"""
MODULE_SUFFIX = r"""so"""


class MarkupCollectType:
    """"""
    INVALID = 0
    STRING = 1
    STRDUP = 2
    BOOLEAN = 3
    TRISTATE = 4
    OPTIONAL = 65536


class MarkupError:
    """"""
    BAD_UTF8 = 0
    EMPTY = 1
    PARSE = 2
    UNKNOWN_ELEMENT = 3
    UNKNOWN_ATTRIBUTE = 4
    INVALID_CONTENT = 5
    MISSING_ATTRIBUTE = 6


class MarkupParseFlags:
    """"""
    DO_NOT_USE_THIS_UNSUPPORTED_FLAG = 1
    TREAT_CDATA_AS_TEXT = 2
    PREFIX_ERROR_POSITION = 4
    IGNORE_QUALIFIED = 8


class NormalizeMode:
    """"""
    DEFAULT = 0
    NFD = 0
    DEFAULT_COMPOSE = 1
    NFC = 1
    ALL = 2
    NFKD = 2
    ALL_COMPOSE = 3
    NFKC = 3


class NumberParserError:
    """"""
    INVALID = 0
    OUT_OF_BOUNDS = 1
OPTION_REMAINING = r"""None"""


class OnceStatus:
    """"""
    NOTCALLED = 0
    PROGRESS = 1
    READY = 2


class OptionArg:
    """"""
    NONE = 0
    STRING = 1
    INT = 2
    CALLBACK = 3
    FILENAME = 4
    STRING_ARRAY = 5
    FILENAME_ARRAY = 6
    DOUBLE = 7
    INT64 = 8


class OptionError:
    """"""
    UNKNOWN_OPTION = 0
    BAD_VALUE = 1
    FAILED = 2


class OptionFlags:
    """"""
    NONE = 0
    HIDDEN = 1
    IN_MAIN = 2
    REVERSE = 4
    NO_ARG = 8
    FILENAME = 16
    OPTIONAL_ARG = 32
    NOALIAS = 64
PDP_ENDIAN = r"""3412"""
PI = r"""3.141593"""
PID_FORMAT = r"""i"""
PI_2 = r"""1.570796"""
PI_4 = r"""0.785398"""
POLLFD_FORMAT = r"""%d"""
PRIORITY_DEFAULT = r"""0"""
PRIORITY_DEFAULT_IDLE = r"""200"""
PRIORITY_HIGH = r"""-100"""
PRIORITY_HIGH_IDLE = r"""100"""
PRIORITY_LOW = r"""300"""


class RegexCompileFlags:
    """"""
    CASELESS = 1
    MULTILINE = 2
    DOTALL = 4
    EXTENDED = 8
    ANCHORED = 16
    DOLLAR_ENDONLY = 32
    UNGREEDY = 512
    RAW = 2048
    NO_AUTO_CAPTURE = 4096
    OPTIMIZE = 8192
    FIRSTLINE = 262144
    DUPNAMES = 524288
    NEWLINE_CR = 1048576
    NEWLINE_LF = 2097152
    NEWLINE_CRLF = 3145728
    NEWLINE_ANYCRLF = 5242880
    BSR_ANYCRLF = 8388608
    JAVASCRIPT_COMPAT = 33554432


class RegexError:
    """"""
    COMPILE = 0
    OPTIMIZE = 1
    REPLACE = 2
    MATCH = 3
    INTERNAL = 4
    STRAY_BACKSLASH = 101
    MISSING_CONTROL_CHAR = 102
    UNRECOGNIZED_ESCAPE = 103
    QUANTIFIERS_OUT_OF_ORDER = 104
    QUANTIFIER_TOO_BIG = 105
    UNTERMINATED_CHARACTER_CLASS = 106
    INVALID_ESCAPE_IN_CHARACTER_CLASS = 107
    RANGE_OUT_OF_ORDER = 108
    NOTHING_TO_REPEAT = 109
    UNRECOGNIZED_CHARACTER = 112
    POSIX_NAMED_CLASS_OUTSIDE_CLASS = 113
    UNMATCHED_PARENTHESIS = 114
    INEXISTENT_SUBPATTERN_REFERENCE = 115
    UNTERMINATED_COMMENT = 118
    EXPRESSION_TOO_LARGE = 120
    MEMORY_ERROR = 121
    VARIABLE_LENGTH_LOOKBEHIND = 125
    MALFORMED_CONDITION = 126
    TOO_MANY_CONDITIONAL_BRANCHES = 127
    ASSERTION_EXPECTED = 128
    UNKNOWN_POSIX_CLASS_NAME = 130
    POSIX_COLLATING_ELEMENTS_NOT_SUPPORTED = 131
    HEX_CODE_TOO_LARGE = 134
    INVALID_CONDITION = 135
    SINGLE_BYTE_MATCH_IN_LOOKBEHIND = 136
    INFINITE_LOOP = 140
    MISSING_SUBPATTERN_NAME_TERMINATOR = 142
    DUPLICATE_SUBPATTERN_NAME = 143
    MALFORMED_PROPERTY = 146
    UNKNOWN_PROPERTY = 147
    SUBPATTERN_NAME_TOO_LONG = 148
    TOO_MANY_SUBPATTERNS = 149
    INVALID_OCTAL_VALUE = 151
    TOO_MANY_BRANCHES_IN_DEFINE = 154
    DEFINE_REPETION = 155
    INCONSISTENT_NEWLINE_OPTIONS = 156
    MISSING_BACK_REFERENCE = 157
    INVALID_RELATIVE_REFERENCE = 158
    BACKTRACKING_CONTROL_VERB_ARGUMENT_FORBIDDEN = 159
    UNKNOWN_BACKTRACKING_CONTROL_VERB = 160
    NUMBER_TOO_BIG = 161
    MISSING_SUBPATTERN_NAME = 162
    MISSING_DIGIT = 163
    INVALID_DATA_CHARACTER = 164
    EXTRA_SUBPATTERN_NAME = 165
    BACKTRACKING_CONTROL_VERB_ARGUMENT_REQUIRED = 166
    INVALID_CONTROL_CHAR = 168
    MISSING_NAME = 169
    NOT_SUPPORTED_IN_CLASS = 171
    TOO_MANY_FORWARD_REFERENCES = 172
    NAME_TOO_LONG = 175
    CHARACTER_VALUE_TOO_LARGE = 176


class RegexMatchFlags:
    """"""
    ANCHORED = 16
    NOTBOL = 128
    NOTEOL = 256
    NOTEMPTY = 1024
    PARTIAL = 32768
    NEWLINE_CR = 1048576
    NEWLINE_LF = 2097152
    NEWLINE_CRLF = 3145728
    NEWLINE_ANY = 4194304
    NEWLINE_ANYCRLF = 5242880
    BSR_ANYCRLF = 8388608
    BSR_ANY = 16777216
    PARTIAL_SOFT = 32768
    PARTIAL_HARD = 134217728
    NOTEMPTY_ATSTART = 268435456
SEARCHPATH_SEPARATOR = r"""58"""
SEARCHPATH_SEPARATOR_S = r""":"""
SIZEOF_LONG = r"""8"""
SIZEOF_SIZE_T = r"""8"""
SIZEOF_SSIZE_T = r"""8"""
SIZEOF_VOID_P = r"""8"""
SOURCE_CONTINUE = r"""true"""
SOURCE_REMOVE = r"""false"""
SQRT2 = r"""1.414214"""
STR_DELIMITERS = r"""_-|> <."""
SYSDEF_AF_INET = r"""2"""
SYSDEF_AF_INET6 = r"""10"""
SYSDEF_AF_UNIX = r"""1"""
SYSDEF_MSG_DONTROUTE = r"""4"""
SYSDEF_MSG_OOB = r"""1"""
SYSDEF_MSG_PEEK = r"""2"""


class SeekType:
    """"""
    CUR = 0
    SET = 1
    END = 2


class ShellError:
    """"""
    BAD_QUOTING = 0
    EMPTY_STRING = 1
    FAILED = 2


class SliceConfig:
    """"""
    ALWAYS_MALLOC = 1
    BYPASS_MAGAZINES = 2
    WORKING_SET_MSECS = 3
    COLOR_INCREMENT = 4
    CHUNK_SIZES = 5
    CONTENTION_COUNTER = 6


class SpawnError:
    """"""
    FORK = 0
    READ = 1
    CHDIR = 2
    ACCES = 3
    PERM = 4
    TOO_BIG = 5
    _2BIG = 5
    NOEXEC = 6
    NAMETOOLONG = 7
    NOENT = 8
    NOMEM = 9
    NOTDIR = 10
    LOOP = 11
    TXTBUSY = 12
    IO = 13
    NFILE = 14
    MFILE = 15
    INVAL = 16
    ISDIR = 17
    LIBBAD = 18
    FAILED = 19


class SpawnFlags:
    """"""
    DEFAULT = 0
    LEAVE_DESCRIPTORS_OPEN = 1
    DO_NOT_REAP_CHILD = 2
    SEARCH_PATH = 4
    STDOUT_TO_DEV_NULL = 8
    STDERR_TO_DEV_NULL = 16
    CHILD_INHERITS_STDIN = 32
    FILE_AND_ARGV_ZERO = 64
    SEARCH_PATH_FROM_ENVP = 128
    CLOEXEC_PIPES = 256
TIME_SPAN_DAY = r"""86400000000"""
TIME_SPAN_HOUR = r"""3600000000"""
TIME_SPAN_MILLISECOND = r"""1000"""
TIME_SPAN_MINUTE = r"""60000000"""
TIME_SPAN_SECOND = r"""1000000"""


class TestFileType:
    """"""
    DIST = 0
    BUILT = 1


class TestLogType:
    """"""
    NONE = 0
    ERROR = 1
    START_BINARY = 2
    LIST_CASE = 3
    SKIP_CASE = 4
    START_CASE = 5
    STOP_CASE = 6
    MIN_RESULT = 7
    MAX_RESULT = 8
    MESSAGE = 9
    START_SUITE = 10
    STOP_SUITE = 11


class TestResult:
    """"""
    SUCCESS = 0
    SKIPPED = 1
    FAILURE = 2
    INCOMPLETE = 3


class TestSubprocessFlags:
    """"""
    STDIN = 1
    STDOUT = 2
    STDERR = 4


class TestTrapFlags:
    """"""
    SILENCE_STDOUT = 128
    SILENCE_STDERR = 256
    INHERIT_STDIN = 512


class ThreadError:
    """"""
    THREAD_ERROR_AGAIN = 0


class TimeType:
    """"""
    STANDARD = 0
    DAYLIGHT = 1
    UNIVERSAL = 2


class TokenType:
    """"""
    EOF = 0
    LEFT_PAREN = 40
    RIGHT_PAREN = 41
    LEFT_CURLY = 123
    RIGHT_CURLY = 125
    LEFT_BRACE = 91
    RIGHT_BRACE = 93
    EQUAL_SIGN = 61
    COMMA = 44
    NONE = 256
    ERROR = 257
    CHAR = 258
    BINARY = 259
    OCTAL = 260
    INT = 261
    HEX = 262
    FLOAT = 263
    STRING = 264
    SYMBOL = 265
    IDENTIFIER = 266
    IDENTIFIER_NULL = 267
    COMMENT_SINGLE = 268
    COMMENT_MULTI = 269


class TraverseFlags:
    """"""
    LEAVES = 1
    NON_LEAVES = 2
    ALL = 3
    MASK = 3
    LEAFS = 1
    NON_LEAFS = 2


class TraverseType:
    """"""
    IN_ORDER = 0
    PRE_ORDER = 1
    POST_ORDER = 2
    LEVEL_ORDER = 3
UNICHAR_MAX_DECOMPOSITION_LENGTH = r"""18"""
URI_RESERVED_CHARS_GENERIC_DELIMITERS = r""":/?#[]@"""
URI_RESERVED_CHARS_SUBCOMPONENT_DELIMITERS = r"""!$&'()*+,;="""
USEC_PER_SEC = r"""1000000"""


class UnicodeBreakType:
    """"""
    MANDATORY = 0
    CARRIAGE_RETURN = 1
    LINE_FEED = 2
    COMBINING_MARK = 3
    SURROGATE = 4
    ZERO_WIDTH_SPACE = 5
    INSEPARABLE = 6
    NON_BREAKING_GLUE = 7
    CONTINGENT = 8
    SPACE = 9
    AFTER = 10
    BEFORE = 11
    BEFORE_AND_AFTER = 12
    HYPHEN = 13
    NON_STARTER = 14
    OPEN_PUNCTUATION = 15
    CLOSE_PUNCTUATION = 16
    QUOTATION = 17
    EXCLAMATION = 18
    IDEOGRAPHIC = 19
    NUMERIC = 20
    INFIX_SEPARATOR = 21
    SYMBOL = 22
    ALPHABETIC = 23
    PREFIX = 24
    POSTFIX = 25
    COMPLEX_CONTEXT = 26
    AMBIGUOUS = 27
    UNKNOWN = 28
    NEXT_LINE = 29
    WORD_JOINER = 30
    HANGUL_L_JAMO = 31
    HANGUL_V_JAMO = 32
    HANGUL_T_JAMO = 33
    HANGUL_LV_SYLLABLE = 34
    HANGUL_LVT_SYLLABLE = 35
    CLOSE_PARANTHESIS = 36
    CONDITIONAL_JAPANESE_STARTER = 37
    HEBREW_LETTER = 38
    REGIONAL_INDICATOR = 39
    EMOJI_BASE = 40
    EMOJI_MODIFIER = 41
    ZERO_WIDTH_JOINER = 42


class UnicodeScript:
    """"""
    INVALID_CODE = -1
    COMMON = 0
    INHERITED = 1
    ARABIC = 2
    ARMENIAN = 3
    BENGALI = 4
    BOPOMOFO = 5
    CHEROKEE = 6
    COPTIC = 7
    CYRILLIC = 8
    DESERET = 9
    DEVANAGARI = 10
    ETHIOPIC = 11
    GEORGIAN = 12
    GOTHIC = 13
    GREEK = 14
    GUJARATI = 15
    GURMUKHI = 16
    HAN = 17
    HANGUL = 18
    HEBREW = 19
    HIRAGANA = 20
    KANNADA = 21
    KATAKANA = 22
    KHMER = 23
    LAO = 24
    LATIN = 25
    MALAYALAM = 26
    MONGOLIAN = 27
    MYANMAR = 28
    OGHAM = 29
    OLD_ITALIC = 30
    ORIYA = 31
    RUNIC = 32
    SINHALA = 33
    SYRIAC = 34
    TAMIL = 35
    TELUGU = 36
    THAANA = 37
    THAI = 38
    TIBETAN = 39
    CANADIAN_ABORIGINAL = 40
    YI = 41
    TAGALOG = 42
    HANUNOO = 43
    BUHID = 44
    TAGBANWA = 45
    BRAILLE = 46
    CYPRIOT = 47
    LIMBU = 48
    OSMANYA = 49
    SHAVIAN = 50
    LINEAR_B = 51
    TAI_LE = 52
    UGARITIC = 53
    NEW_TAI_LUE = 54
    BUGINESE = 55
    GLAGOLITIC = 56
    TIFINAGH = 57
    SYLOTI_NAGRI = 58
    OLD_PERSIAN = 59
    KHAROSHTHI = 60
    UNKNOWN = 61
    BALINESE = 62
    CUNEIFORM = 63
    PHOENICIAN = 64
    PHAGS_PA = 65
    NKO = 66
    KAYAH_LI = 67
    LEPCHA = 68
    REJANG = 69
    SUNDANESE = 70
    SAURASHTRA = 71
    CHAM = 72
    OL_CHIKI = 73
    VAI = 74
    CARIAN = 75
    LYCIAN = 76
    LYDIAN = 77
    AVESTAN = 78
    BAMUM = 79
    EGYPTIAN_HIEROGLYPHS = 80
    IMPERIAL_ARAMAIC = 81
    INSCRIPTIONAL_PAHLAVI = 82
    INSCRIPTIONAL_PARTHIAN = 83
    JAVANESE = 84
    KAITHI = 85
    LISU = 86
    MEETEI_MAYEK = 87
    OLD_SOUTH_ARABIAN = 88
    OLD_TURKIC = 89
    SAMARITAN = 90
    TAI_THAM = 91
    TAI_VIET = 92
    BATAK = 93
    BRAHMI = 94
    MANDAIC = 95
    CHAKMA = 96
    MEROITIC_CURSIVE = 97
    MEROITIC_HIEROGLYPHS = 98
    MIAO = 99
    SHARADA = 100
    SORA_SOMPENG = 101
    TAKRI = 102
    BASSA_VAH = 103
    CAUCASIAN_ALBANIAN = 104
    DUPLOYAN = 105
    ELBASAN = 106
    GRANTHA = 107
    KHOJKI = 108
    KHUDAWADI = 109
    LINEAR_A = 110
    MAHAJANI = 111
    MANICHAEAN = 112
    MENDE_KIKAKUI = 113
    MODI = 114
    MRO = 115
    NABATAEAN = 116
    OLD_NORTH_ARABIAN = 117
    OLD_PERMIC = 118
    PAHAWH_HMONG = 119
    PALMYRENE = 120
    PAU_CIN_HAU = 121
    PSALTER_PAHLAVI = 122
    SIDDHAM = 123
    TIRHUTA = 124
    WARANG_CITI = 125
    AHOM = 126
    ANATOLIAN_HIEROGLYPHS = 127
    HATRAN = 128
    MULTANI = 129
    OLD_HUNGARIAN = 130
    SIGNWRITING = 131
    ADLAM = 132
    BHAIKSUKI = 133
    MARCHEN = 134
    NEWA = 135
    OSAGE = 136
    TANGUT = 137
    MASARAM_GONDI = 138
    NUSHU = 139
    SOYOMBO = 140
    ZANABAZAR_SQUARE = 141


class UnicodeType:
    """"""
    CONTROL = 0
    FORMAT = 1
    UNASSIGNED = 2
    PRIVATE_USE = 3
    SURROGATE = 4
    LOWERCASE_LETTER = 5
    MODIFIER_LETTER = 6
    OTHER_LETTER = 7
    TITLECASE_LETTER = 8
    UPPERCASE_LETTER = 9
    SPACING_MARK = 10
    ENCLOSING_MARK = 11
    NON_SPACING_MARK = 12
    DECIMAL_NUMBER = 13
    LETTER_NUMBER = 14
    OTHER_NUMBER = 15
    CONNECT_PUNCTUATION = 16
    DASH_PUNCTUATION = 17
    CLOSE_PUNCTUATION = 18
    FINAL_PUNCTUATION = 19
    INITIAL_PUNCTUATION = 20
    OTHER_PUNCTUATION = 21
    OPEN_PUNCTUATION = 22
    CURRENCY_SYMBOL = 23
    MODIFIER_SYMBOL = 24
    MATH_SYMBOL = 25
    OTHER_SYMBOL = 26
    LINE_SEPARATOR = 27
    PARAGRAPH_SEPARATOR = 28
    SPACE_SEPARATOR = 29


class UserDirectory:
    """"""
    DIRECTORY_DESKTOP = 0
    DIRECTORY_DOCUMENTS = 1
    DIRECTORY_DOWNLOAD = 2
    DIRECTORY_MUSIC = 3
    DIRECTORY_PICTURES = 4
    DIRECTORY_PUBLIC_SHARE = 5
    DIRECTORY_TEMPLATES = 6
    DIRECTORY_VIDEOS = 7
    N_DIRECTORIES = 8
VA_COPY_AS_ARRAY = r"""1"""
VERSION_MIN_REQUIRED = r"""2"""


class VariantClass:
    """"""
    BOOLEAN = 98
    BYTE = 121
    INT16 = 110
    UINT16 = 113
    INT32 = 105
    UINT32 = 117
    INT64 = 120
    UINT64 = 116
    HANDLE = 104
    DOUBLE = 100
    STRING = 115
    OBJECT_PATH = 111
    SIGNATURE = 103
    VARIANT = 118
    MAYBE = 109
    ARRAY = 97
    TUPLE = 40
    DICT_ENTRY = 123


class VariantParseError:
    """"""
    FAILED = 0
    BASIC_TYPE_EXPECTED = 1
    CANNOT_INFER_TYPE = 2
    DEFINITE_TYPE_EXPECTED = 3
    INPUT_NOT_AT_END = 4
    INVALID_CHARACTER = 5
    INVALID_FORMAT_STRING = 6
    INVALID_OBJECT_PATH = 7
    INVALID_SIGNATURE = 8
    INVALID_TYPE_STRING = 9
    NO_COMMON_TYPE = 10
    NUMBER_OUT_OF_RANGE = 11
    NUMBER_TOO_BIG = 12
    TYPE_ERROR = 13
    UNEXPECTED_TOKEN = 14
    UNKNOWN_KEYWORD = 15
    UNTERMINATED_STRING_CONSTANT = 16
    VALUE_EXPECTED = 17
WIN32_MSG_HANDLE = r"""19981206"""

def access(filename=None, mode=None):
    """"""
    return object

def ascii_digit_value(c=None):
    """"""
    return object

def ascii_dtostr(buffer=None, buf_len=None, d=None):
    """"""
    return object

def ascii_formatd(buffer=None, buf_len=None, format=None, d=None):
    """"""
    return object

def ascii_strcasecmp(s1=None, s2=None):
    """"""
    return object

def ascii_strdown(str=None, len=None):
    """"""
    return object

def ascii_string_to_signed(str=None, base=None, min=None, max=None, out_num=None):
    """"""
    return object

def ascii_string_to_unsigned(str=None, base=None, min=None, max=None, out_num=None):
    """"""
    return object

def ascii_strncasecmp(s1=None, s2=None, n=None):
    """"""
    return object

def ascii_strtod(nptr=None, endptr=None):
    """"""
    return object

def ascii_strtoll(nptr=None, endptr=None, base=None):
    """"""
    return object

def ascii_strtoull(nptr=None, endptr=None, base=None):
    """"""
    return object

def ascii_strup(str=None, len=None):
    """"""
    return object

def ascii_tolower(c=None):
    """"""
    return object

def ascii_toupper(c=None):
    """"""
    return object

def ascii_xdigit_value(c=None):
    """"""
    return object

def assert_warning(log_domain=None, file=None, line=None, pretty_function=None, expression=None):
    """"""
    return object

def assertion_message(domain=None, file=None, line=None, func=None, message=None):
    """"""
    return object

def assertion_message_cmpnum(domain=None, file=None, line=None, func=None, expr=None, arg1=None, cmp=None, arg2=None, numtype=None):
    """"""
    return object

def assertion_message_cmpstr(domain=None, file=None, line=None, func=None, expr=None, arg1=None, cmp=None, arg2=None):
    """"""
    return object

def assertion_message_error(domain=None, file=None, line=None, func=None, expr=None, error=None, error_domain=None, error_code=None):
    """"""
    return object

def assertion_message_expr(domain=None, file=None, line=None, func=None, expr=None):
    """"""
    return object

def atexit(func=None):
    """"""
    return object

def atomic_int_add(atomic=None, val=None):
    """"""
    return object

def atomic_int_and(atomic=None, val=None):
    """"""
    return object

def atomic_int_compare_and_exchange(atomic=None, oldval=None, newval=None):
    """"""
    return object

def atomic_int_dec_and_test(atomic=None):
    """"""
    return object

def atomic_int_exchange_and_add(atomic=None, val=None):
    """"""
    return object

def atomic_int_get(atomic=None):
    """"""
    return object

def atomic_int_inc(atomic=None):
    """"""
    return object

def atomic_int_or(atomic=None, val=None):
    """"""
    return object

def atomic_int_set(atomic=None, newval=None):
    """"""
    return object

def atomic_int_xor(atomic=None, val=None):
    """"""
    return object

def atomic_pointer_add(atomic=None, val=None):
    """"""
    return object

def atomic_pointer_and(atomic=None, val=None):
    """"""
    return object

def atomic_pointer_compare_and_exchange(atomic=None, oldval=None, newval=None):
    """"""
    return object

def atomic_pointer_get(atomic=None):
    """"""
    return object

def atomic_pointer_or(atomic=None, val=None):
    """"""
    return object

def atomic_pointer_set(atomic=None, newval=None):
    """"""
    return object

def atomic_pointer_xor(atomic=None, val=None):
    """"""
    return object

def base64_decode(text=None, out_len=None):
    """"""
    return object

def base64_decode_inplace(text=None, out_len=None):
    """"""
    return object

def base64_decode_step(_in=None, len=None, out=None, state=None, save=None):
    """"""
    return object

def base64_encode(data=None, len=None):
    """"""
    return object

def base64_encode_close(break_lines=None, out=None, state=None, save=None):
    """"""
    return object

def base64_encode_step(_in=None, len=None, break_lines=None, out=None, state=None, save=None):
    """"""
    return object

def basename(file_name=None):
    """"""
    return object

def bit_lock(address=None, lock_bit=None):
    """"""
    return object

def bit_nth_lsf(mask=None, nth_bit=None):
    """"""
    return object

def bit_nth_msf(mask=None, nth_bit=None):
    """"""
    return object

def bit_storage(number=None):
    """"""
    return object

def bit_trylock(address=None, lock_bit=None):
    """"""
    return object

def bit_unlock(address=None, lock_bit=None):
    """"""
    return object

def bookmark_file_error_quark():
    """"""
    return object

def build_filename(first_element=None, *args):
    """"""
    return object

def build_filename_valist(first_element=None, args=None):
    """"""
    return object

def build_filenamev(args=None):
    """"""
    return object

def build_path(separator=None, first_element=None, *args):
    """"""
    return object

def build_pathv(separator=None, args=None):
    """"""
    return object

def byte_array_free(array=None, free_segment=None):
    """"""
    return object

def byte_array_free_to_bytes(array=None):
    """"""
    return object

def byte_array_new():
    """"""
    return object

def byte_array_new_take(data=None, len=None):
    """"""
    return object

def byte_array_unref(array=None):
    """"""
    return object

def chdir(path=None):
    """"""
    return object

def check_version(required_major=None, required_minor=None, required_micro=None):
    """"""
    return object

def checksum_type_get_length(checksum_type=None):
    """"""
    return object

def child_watch_add(pid=None, function=None, data=None):
    """"""
    return object

def child_watch_add_full(priority=None, pid=None, function=None, data=None, notify=None):
    """"""
    return object

def child_watch_source_new(pid=None):
    """"""
    return object

def clear_error():
    """"""
    return object

def clear_handle_id(tag_ptr=None, clear_func=None):
    """"""
    return object

def clear_pointer(pp=None, destroy=None):
    """"""
    return object

def close(fd=None):
    """"""
    return object

def compute_checksum_for_bytes(checksum_type=None, data=None):
    """"""
    return object

def compute_checksum_for_data(checksum_type=None, data=None, length=None):
    """"""
    return object

def compute_checksum_for_string(checksum_type=None, str=None, length=None):
    """"""
    return object

def compute_hmac_for_bytes(digest_type=None, key=None, data=None):
    """"""
    return object

def compute_hmac_for_data(digest_type=None, key=None, key_len=None, data=None, length=None):
    """"""
    return object

def compute_hmac_for_string(digest_type=None, key=None, key_len=None, str=None, length=None):
    """"""
    return object

def convert(str=None, len=None, to_codeset=None, from_codeset=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def convert_error_quark():
    """"""
    return object

def convert_with_fallback(str=None, len=None, to_codeset=None, from_codeset=None, fallback=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def convert_with_iconv(str=None, len=None, converter=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def datalist_clear(datalist=None):
    """"""
    return object

def datalist_foreach(datalist=None, func=None, user_data=None):
    """"""
    return object

def datalist_get_data(datalist=None, key=None):
    """"""
    return object

def datalist_get_flags(datalist=None):
    """"""
    return object

def datalist_id_dup_data(datalist=None, key_id=None, dup_func=None, user_data=None):
    """"""
    return object

def datalist_id_get_data(datalist=None, key_id=None):
    """"""
    return object

def datalist_id_remove_no_notify(datalist=None, key_id=None):
    """"""
    return object

def datalist_id_replace_data(datalist=None, key_id=None, oldval=None, newval=None, destroy=None, old_destroy=None):
    """"""
    return object

def datalist_id_set_data_full(datalist=None, key_id=None, data=None, destroy_func=None):
    """"""
    return object

def datalist_init(datalist=None):
    """"""
    return object

def datalist_set_flags(datalist=None, flags=None):
    """"""
    return object

def datalist_unset_flags(datalist=None, flags=None):
    """"""
    return object

def dataset_destroy(dataset_location=None):
    """"""
    return object

def dataset_foreach(dataset_location=None, func=None, user_data=None):
    """"""
    return object

def dataset_id_get_data(dataset_location=None, key_id=None):
    """"""
    return object

def dataset_id_remove_no_notify(dataset_location=None, key_id=None):
    """"""
    return object

def dataset_id_set_data_full(dataset_location=None, key_id=None, data=None, destroy_func=None):
    """"""
    return object

def date_get_days_in_month(month=None, year=None):
    """"""
    return object

def date_get_monday_weeks_in_year(year=None):
    """"""
    return object

def date_get_sunday_weeks_in_year(year=None):
    """"""
    return object

def date_is_leap_year(year=None):
    """"""
    return object

def date_strftime(s=None, slen=None, format=None, date=None):
    """"""
    return object

def date_time_compare(dt1=None, dt2=None):
    """"""
    return object

def date_time_equal(dt1=None, dt2=None):
    """"""
    return object

def date_time_hash(datetime=None):
    """"""
    return object

def date_valid_day(day=None):
    """"""
    return object

def date_valid_dmy(day=None, month=None, year=None):
    """"""
    return object

def date_valid_julian(julian_date=None):
    """"""
    return object

def date_valid_month(month=None):
    """"""
    return object

def date_valid_weekday(weekday=None):
    """"""
    return object

def date_valid_year(year=None):
    """"""
    return object

def dcgettext(domain=None, msgid=None, category=None):
    """"""
    return object

def dgettext(domain=None, msgid=None):
    """"""
    return object

def dir_make_tmp(tmpl=None):
    """"""
    return object

def direct_equal(v1=None, v2=None):
    """"""
    return object

def direct_hash(v=None):
    """"""
    return object

def dngettext(domain=None, msgid=None, msgid_plural=None, n=None):
    """"""
    return object

def double_equal(v1=None, v2=None):
    """"""
    return object

def double_hash(v=None):
    """"""
    return object

def dpgettext(domain=None, msgctxtid=None, msgidoffset=None):
    """"""
    return object

def dpgettext2(domain=None, context=None, msgid=None):
    """"""
    return object

def environ_getenv(envp=None, variable=None):
    """"""
    return object

def environ_setenv(envp=None, variable=None, value=None, overwrite=None):
    """"""
    return object

def environ_unsetenv(envp=None, variable=None):
    """"""
    return object

def file_error_from_errno(err_no=None):
    """"""
    return object

def file_error_quark():
    """"""
    return object

def file_get_contents(filename=None, contents=None, length=None):
    """"""
    return object

def file_open_tmp(tmpl=None, name_used=None):
    """"""
    return object

def file_read_link(filename=None):
    """"""
    return object

def file_set_contents(filename=None, contents=None, length=None):
    """"""
    return object

def file_test(filename=None, test=None):
    """"""
    return object

def filename_display_basename(filename=None):
    """"""
    return object

def filename_display_name(filename=None):
    """"""
    return object

def filename_from_uri(uri=None, hostname=None):
    """"""
    return object

def filename_from_utf8(utf8string=None, len=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def filename_to_uri(filename=None, hostname=None):
    """"""
    return object

def filename_to_utf8(opsysstring=None, len=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def find_program_in_path(program=None):
    """"""
    return object

def format_size(size=None):
    """"""
    return object

def format_size_for_display(size=None):
    """"""
    return object

def format_size_full(size=None, flags=None):
    """"""
    return object

def fprintf(file=None, format=None, *args):
    """"""
    return object

def free(mem=None):
    """"""
    return object

def get_application_name():
    """"""
    return object

def get_charset(charset=None):
    """"""
    return object

def get_codeset():
    """"""
    return object

def get_current_dir():
    """"""
    return object

def get_current_time(result=None):
    """"""
    return object

def get_environ():
    """"""
    return object

def get_filename_charsets(charsets=None):
    """"""
    return object

def get_home_dir():
    """"""
    return object

def get_host_name():
    """"""
    return object

def get_language_names():
    """"""
    return object

def get_locale_variants(locale=None):
    """"""
    return object

def get_monotonic_time():
    """"""
    return object

def get_num_processors():
    """"""
    return object

def get_prgname():
    """"""
    return object

def get_real_name():
    """"""
    return object

def get_real_time():
    """"""
    return object

def get_system_config_dirs():
    """"""
    return object

def get_system_data_dirs():
    """"""
    return object

def get_tmp_dir():
    """"""
    return object

def get_user_cache_dir():
    """"""
    return object

def get_user_config_dir():
    """"""
    return object

def get_user_data_dir():
    """"""
    return object

def get_user_name():
    """"""
    return object

def get_user_runtime_dir():
    """"""
    return object

def get_user_special_dir(directory=None):
    """"""
    return object

def getenv(variable=None):
    """"""
    return object

def hash_table_add(hash_table=None, key=None):
    """"""
    return object

def hash_table_contains(hash_table=None, key=None):
    """"""
    return object

def hash_table_destroy(hash_table=None):
    """"""
    return object

def hash_table_insert(hash_table=None, key=None, value=None):
    """"""
    return object

def hash_table_lookup(hash_table=None, key=None):
    """"""
    return object

def hash_table_lookup_extended(hash_table=None, lookup_key=None, orig_key=None, value=None):
    """"""
    return object

def hash_table_remove(hash_table=None, key=None):
    """"""
    return object

def hash_table_remove_all(hash_table=None):
    """"""
    return object

def hash_table_replace(hash_table=None, key=None, value=None):
    """"""
    return object

def hash_table_size(hash_table=None):
    """"""
    return object

def hash_table_steal(hash_table=None, key=None):
    """"""
    return object

def hash_table_steal_all(hash_table=None):
    """"""
    return object

def hash_table_unref(hash_table=None):
    """"""
    return object

def hook_destroy(hook_list=None, hook_id=None):
    """"""
    return object

def hook_destroy_link(hook_list=None, hook=None):
    """"""
    return object

def hook_free(hook_list=None, hook=None):
    """"""
    return object

def hook_insert_before(hook_list=None, sibling=None, hook=None):
    """"""
    return object

def hook_prepend(hook_list=None, hook=None):
    """"""
    return object

def hook_unref(hook_list=None, hook=None):
    """"""
    return object

def hostname_is_ascii_encoded(hostname=None):
    """"""
    return object

def hostname_is_ip_address(hostname=None):
    """"""
    return object

def hostname_is_non_ascii(hostname=None):
    """"""
    return object

def hostname_to_ascii(hostname=None):
    """"""
    return object

def hostname_to_unicode(hostname=None):
    """"""
    return object

def iconv(converter=None, inbuf=None, inbytes_left=None, outbuf=None, outbytes_left=None):
    """"""
    return object

def iconv_open(to_codeset=None, from_codeset=None):
    """"""
    return object

def idle_add(function=None, data=None):
    """"""
    return object

def idle_add_full(priority=None, function=None, data=None, notify=None):
    """"""
    return object

def idle_remove_by_data(data=None):
    """"""
    return object

def idle_source_new():
    """"""
    return object

def int64_equal(v1=None, v2=None):
    """"""
    return object

def int64_hash(v=None):
    """"""
    return object

def int_equal(v1=None, v2=None):
    """"""
    return object

def int_hash(v=None):
    """"""
    return object

def intern_static_string(string=None):
    """"""
    return object

def intern_string(string=None):
    """"""
    return object

def io_add_watch(channel=None, condition=None, func=None, user_data=None):
    """"""
    return object

def io_add_watch_full(channel=None, priority=None, condition=None, func=None, user_data=None, notify=None):
    """"""
    return object

def io_channel_error_from_errno(en=None):
    """"""
    return object

def io_channel_error_quark():
    """"""
    return object

def io_create_watch(channel=None, condition=None):
    """"""
    return object

def key_file_error_quark():
    """"""
    return object

def listenv():
    """"""
    return object

def locale_from_utf8(utf8string=None, len=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def locale_to_utf8(opsysstring=None, len=None, bytes_read=None, bytes_written=None):
    """"""
    return object

def log(log_domain=None, log_level=None, format=None, *args):
    """"""
    return object

def log_default_handler(log_domain=None, log_level=None, message=None, unused_data=None):
    """"""
    return object

def log_remove_handler(log_domain=None, handler_id=None):
    """"""
    return object

def log_set_always_fatal(fatal_mask=None):
    """"""
    return object

def log_set_default_handler(log_func=None, user_data=None):
    """"""
    return object

def log_set_fatal_mask(log_domain=None, fatal_mask=None):
    """"""
    return object

def log_set_handler(log_domain=None, log_levels=None, log_func=None, user_data=None):
    """"""
    return object

def log_set_handler_full(log_domain=None, log_levels=None, log_func=None, user_data=None, destroy=None):
    """"""
    return object

def log_set_writer_func(func=None, user_data=None, user_data_free=None):
    """"""
    return object

def log_structured(log_domain=None, log_level=None, *args):
    """"""
    return object

def log_structured_array(log_level=None, fields=None, n_fields=None):
    """"""
    return object

def log_structured_standard(log_domain=None, log_level=None, file=None, line=None, func=None, message_format=None, *args):
    """"""
    return object

def log_variant(log_domain=None, log_level=None, fields=None):
    """"""
    return object

def log_writer_default(log_level=None, fields=None, n_fields=None, user_data=None):
    """"""
    return object

def log_writer_format_fields(log_level=None, fields=None, n_fields=None, use_color=None):
    """"""
    return object

def log_writer_is_journald(output_fd=None):
    """"""
    return object

def log_writer_journald(log_level=None, fields=None, n_fields=None, user_data=None):
    """"""
    return object

def log_writer_standard_streams(log_level=None, fields=None, n_fields=None, user_data=None):
    """"""
    return object

def log_writer_supports_color(output_fd=None):
    """"""
    return object

def logv(log_domain=None, log_level=None, format=None, args=None):
    """"""
    return object

def main_context_default():
    """"""
    return object

def main_context_get_thread_default():
    """"""
    return object

def main_context_ref_thread_default():
    """"""
    return object

def main_current_source():
    """"""
    return object

def main_depth():
    """"""
    return object

def malloc(n_bytes=None):
    """"""
    return object

def malloc0(n_bytes=None):
    """"""
    return object

def malloc0_n(n_blocks=None, n_block_bytes=None):
    """"""
    return object

def malloc_n(n_blocks=None, n_block_bytes=None):
    """"""
    return object

def markup_collect_attributes(element_name=None, attribute_names=None, attribute_values=None, error=None, first_type=None, first_attr=None, *args):
    """"""
    return object

def markup_error_quark():
    """"""
    return object

def markup_escape_text(text=None, length=None):
    """"""
    return object

def markup_printf_escaped(format=None, *args):
    """"""
    return object

def markup_vprintf_escaped(format=None, args=None):
    """"""
    return object

def mem_is_system_malloc():
    """"""
    return object

def mem_profile():
    """"""
    return object

def mem_set_vtable(vtable=None):
    """"""
    return object

def memdup(mem=None, byte_size=None):
    """"""
    return object

def mkdir_with_parents(pathname=None, mode=None):
    """"""
    return object

def mkdtemp(tmpl=None):
    """"""
    return object

def mkdtemp_full(tmpl=None, mode=None):
    """"""
    return object

def mkstemp(tmpl=None):
    """"""
    return object

def mkstemp_full(tmpl=None, flags=None, mode=None):
    """"""
    return object

def nullify_pointer(nullify_location=None):
    """"""
    return object

def number_parser_error_quark():
    """"""
    return object

def on_error_query(prg_name=None):
    """"""
    return object

def on_error_stack_trace(prg_name=None):
    """"""
    return object

def once_init_enter(location=None):
    """"""
    return object

def once_init_leave(location=None, result=None):
    """"""
    return object

def option_error_quark():
    """"""
    return object

def parse_debug_string(string=None, keys=None, nkeys=None):
    """"""
    return object

def path_get_basename(file_name=None):
    """"""
    return object

def path_get_dirname(file_name=None):
    """"""
    return object

def path_is_absolute(file_name=None):
    """"""
    return object

def path_skip_root(file_name=None):
    """"""
    return object

def pattern_match(pspec=None, string_length=None, string=None, string_reversed=None):
    """"""
    return object

def pattern_match_simple(pattern=None, string=None):
    """"""
    return object

def pattern_match_string(pspec=None, string=None):
    """"""
    return object

def pointer_bit_lock(address=None, lock_bit=None):
    """"""
    return object

def pointer_bit_trylock(address=None, lock_bit=None):
    """"""
    return object

def pointer_bit_unlock(address=None, lock_bit=None):
    """"""
    return object

def poll(fds=None, nfds=None, timeout=None):
    """"""
    return object

def prefix_error(err=None, format=None, *args):
    """"""
    return object

def _print(format=None, *args):
    """"""
    return object

def printerr(format=None, *args):
    """"""
    return object

def printf(format=None, *args):
    """"""
    return object

def printf_string_upper_bound(format=None, args=None):
    """"""
    return object

def propagate_error(dest=None, src=None):
    """"""
    return object

def propagate_prefixed_error(dest=None, src=None, format=None, *args):
    """"""
    return object

def ptr_array_find(haystack=None, needle=None, index_=None):
    """"""
    return object

def ptr_array_find_with_equal_func(haystack=None, needle=None, equal_func=None, index_=None):
    """"""
    return object

def qsort_with_data(pbase=None, total_elems=None, size=None, compare_func=None, user_data=None):
    """"""
    return object

def quark_from_static_string(string=None):
    """"""
    return object

def quark_from_string(string=None):
    """"""
    return object

def quark_to_string(quark=None):
    """"""
    return object

def quark_try_string(string=None):
    """"""
    return object

def random_double():
    """"""
    return object

def random_double_range(begin=None, end=None):
    """"""
    return object

def random_int():
    """"""
    return object

def random_int_range(begin=None, end=None):
    """"""
    return object

def random_set_seed(seed=None):
    """"""
    return object

def realloc(mem=None, n_bytes=None):
    """"""
    return object

def realloc_n(mem=None, n_blocks=None, n_block_bytes=None):
    """"""
    return object

def regex_check_replacement(replacement=None, has_references=None):
    """"""
    return object

def regex_error_quark():
    """"""
    return object

def regex_escape_nul(string=None, length=None):
    """"""
    return object

def regex_escape_string(string=None, length=None):
    """"""
    return object

def regex_match_simple(pattern=None, string=None, compile_options=None, match_options=None):
    """"""
    return object

def regex_split_simple(pattern=None, string=None, compile_options=None, match_options=None):
    """"""
    return object

def reload_user_special_dirs_cache():
    """"""
    return object

def return_if_fail_warning(log_domain=None, pretty_function=None, expression=None):
    """"""
    return object

def rmdir(filename=None):
    """"""
    return object

def sequence_get(iter=None):
    """"""
    return object

def sequence_insert_before(iter=None, data=None):
    """"""
    return object

def sequence_move(src=None, dest=None):
    """"""
    return object

def sequence_move_range(dest=None, begin=None, end=None):
    """"""
    return object

def sequence_range_get_midpoint(begin=None, end=None):
    """"""
    return object

def sequence_remove(iter=None):
    """"""
    return object

def sequence_remove_range(begin=None, end=None):
    """"""
    return object

def sequence_set(iter=None, data=None):
    """"""
    return object

def sequence_swap(a=None, b=None):
    """"""
    return object

def set_application_name(application_name=None):
    """"""
    return object

def set_error(err=None, domain=None, code=None, format=None, *args):
    """"""
    return object

def set_error_literal(err=None, domain=None, code=None, message=None):
    """"""
    return object

def set_prgname(prgname=None):
    """"""
    return object

def set_print_handler(func=None):
    """"""
    return object

def set_printerr_handler(func=None):
    """"""
    return object

def setenv(variable=None, value=None, overwrite=None):
    """"""
    return object

def shell_error_quark():
    """"""
    return object

def shell_parse_argv(command_line=None, argcp=None, argvp=None):
    """"""
    return object

def shell_quote(unquoted_string=None):
    """"""
    return object

def shell_unquote(quoted_string=None):
    """"""
    return object

def slice_alloc(block_size=None):
    """"""
    return object

def slice_alloc0(block_size=None):
    """"""
    return object

def slice_copy(block_size=None, mem_block=None):
    """"""
    return object

def slice_free1(block_size=None, mem_block=None):
    """"""
    return object

def slice_free_chain_with_offset(block_size=None, mem_chain=None, next_offset=None):
    """"""
    return object

def slice_get_config(ckey=None):
    """"""
    return object

def slice_get_config_state(ckey=None, address=None, n_values=None):
    """"""
    return object

def slice_set_config(ckey=None, value=None):
    """"""
    return object

def snprintf(string=None, n=None, format=None, *args):
    """"""
    return object

def source_remove(tag=None):
    """"""
    return object

def source_remove_by_funcs_user_data(funcs=None, user_data=None):
    """"""
    return object

def source_remove_by_user_data(user_data=None):
    """"""
    return object

def source_set_name_by_id(tag=None, name=None):
    """"""
    return object

def spaced_primes_closest(num=None):
    """"""
    return object

def spawn_async(working_directory=None, argv=None, envp=None, flags=None, child_setup=None, user_data=None, child_pid=None):
    """"""
    return object

def spawn_async_with_pipes(working_directory=None, argv=None, envp=None, flags=None, child_setup=None, user_data=None, child_pid=None, standard_input=None, standard_output=None, standard_error=None):
    """"""
    return object

def spawn_check_exit_status(exit_status=None):
    """"""
    return object

def spawn_close_pid(pid=None):
    """"""
    return object

def spawn_command_line_async(command_line=None):
    """"""
    return object

def spawn_command_line_sync(command_line=None, standard_output=None, standard_error=None, exit_status=None):
    """"""
    return object

def spawn_error_quark():
    """"""
    return object

def spawn_exit_error_quark():
    """"""
    return object

def spawn_sync(working_directory=None, argv=None, envp=None, flags=None, child_setup=None, user_data=None, standard_output=None, standard_error=None, exit_status=None):
    """"""
    return object

def sprintf(string=None, format=None, *args):
    """"""
    return object

def stpcpy(dest=None, src=None):
    """"""
    return object

def str_equal(v1=None, v2=None):
    """"""
    return object

def str_has_prefix(str=None, prefix=None):
    """"""
    return object

def str_has_suffix(str=None, suffix=None):
    """"""
    return object

def str_hash(v=None):
    """"""
    return object

def str_is_ascii(str=None):
    """"""
    return object

def str_match_string(search_term=None, potential_hit=None, accept_alternates=None):
    """"""
    return object

def str_to_ascii(str=None, from_locale=None):
    """"""
    return object

def str_tokenize_and_fold(string=None, translit_locale=None, ascii_alternates=None):
    """"""
    return object

def strcanon(string=None, valid_chars=None, substitutor=None):
    """"""
    return object

def strcasecmp(s1=None, s2=None):
    """"""
    return object

def strchomp(string=None):
    """"""
    return object

def strchug(string=None):
    """"""
    return object

def strcmp0(str1=None, str2=None):
    """"""
    return object

def strcompress(source=None):
    """"""
    return object

def strconcat(string1=None, *args):
    """"""
    return object

def strdelimit(string=None, delimiters=None, new_delimiter=None):
    """"""
    return object

def strdown(string=None):
    """"""
    return object

def strdup(str=None):
    """"""
    return object

def strdup_printf(format=None, *args):
    """"""
    return object

def strdup_vprintf(format=None, args=None):
    """"""
    return object

def strdupv(str_array=None):
    """"""
    return object

def strerror(errnum=None):
    """"""
    return object

def strescape(source=None, exceptions=None):
    """"""
    return object

def strfreev(str_array=None):
    """"""
    return object

def string_new(init=None):
    """"""
    return object

def string_new_len(init=None, len=None):
    """"""
    return object

def string_sized_new(dfl_size=None):
    """"""
    return object

def strip_context(msgid=None, msgval=None):
    """"""
    return object

def strjoin(separator=None, *args):
    """"""
    return object

def strjoinv(separator=None, str_array=None):
    """"""
    return object

def strlcat(dest=None, src=None, dest_size=None):
    """"""
    return object

def strlcpy(dest=None, src=None, dest_size=None):
    """"""
    return object

def strncasecmp(s1=None, s2=None, n=None):
    """"""
    return object

def strndup(str=None, n=None):
    """"""
    return object

def strnfill(length=None, fill_char=None):
    """"""
    return object

def strreverse(string=None):
    """"""
    return object

def strrstr(haystack=None, needle=None):
    """"""
    return object

def strrstr_len(haystack=None, haystack_len=None, needle=None):
    """"""
    return object

def strsignal(signum=None):
    """"""
    return object

def strsplit(string=None, delimiter=None, max_tokens=None):
    """"""
    return object

def strsplit_set(string=None, delimiters=None, max_tokens=None):
    """"""
    return object

def strstr_len(haystack=None, haystack_len=None, needle=None):
    """"""
    return object

def strtod(nptr=None, endptr=None):
    """"""
    return object

def strup(string=None):
    """"""
    return object

def strv_contains(strv=None, str=None):
    """"""
    return object

def strv_get_type():
    """"""
    return object

def strv_length(str_array=None):
    """"""
    return object

def test_add_data_func(testpath=None, test_data=None, test_func=None):
    """"""
    return object

def test_add_data_func_full(testpath=None, test_data=None, test_func=None, data_free_func=None):
    """"""
    return object

def test_add_func(testpath=None, test_func=None):
    """"""
    return object

def test_add_vtable(testpath=None, data_size=None, test_data=None, data_setup=None, data_test=None, data_teardown=None):
    """"""
    return object

def test_assert_expected_messages_internal(domain=None, file=None, line=None, func=None):
    """"""
    return object

def test_bug(bug_uri_snippet=None):
    """"""
    return object

def test_bug_base(uri_pattern=None):
    """"""
    return object

def test_build_filename(file_type=None, first_path=None, *args):
    """"""
    return object

def test_create_case(test_name=None, data_size=None, test_data=None, data_setup=None, data_test=None, data_teardown=None):
    """"""
    return object

def test_create_suite(suite_name=None):
    """"""
    return object

def test_expect_message(log_domain=None, log_level=None, pattern=None):
    """"""
    return object

def test_fail():
    """"""
    return object

def test_failed():
    """"""
    return object

def test_get_dir(file_type=None):
    """"""
    return object

def test_get_filename(file_type=None, first_path=None, *args):
    """"""
    return object

def test_get_root():
    """"""
    return object

def test_incomplete(msg=None):
    """"""
    return object

def test_init(argc=None, argv=None, *args):
    """"""
    return object

def test_log_set_fatal_handler(log_func=None, user_data=None):
    """"""
    return object

def test_log_type_name(log_type=None):
    """"""
    return object

def test_maximized_result(maximized_quantity=None, format=None, *args):
    """"""
    return object

def test_message(format=None, *args):
    """"""
    return object

def test_minimized_result(minimized_quantity=None, format=None, *args):
    """"""
    return object

def test_queue_destroy(destroy_func=None, destroy_data=None):
    """"""
    return object

def test_queue_free(gfree_pointer=None):
    """"""
    return object

def test_rand_double():
    """"""
    return object

def test_rand_double_range(range_start=None, range_end=None):
    """"""
    return object

def test_rand_int():
    """"""
    return object

def test_rand_int_range(begin=None, end=None):
    """"""
    return object

def test_run():
    """"""
    return object

def test_run_suite(suite=None):
    """"""
    return object

def test_set_nonfatal_assertions():
    """"""
    return object

def test_skip(msg=None):
    """"""
    return object

def test_subprocess():
    """"""
    return object

def test_timer_elapsed():
    """"""
    return object

def test_timer_last():
    """"""
    return object

def test_timer_start():
    """"""
    return object

def test_trap_assertions(domain=None, file=None, line=None, func=None, assertion_flags=None, pattern=None):
    """"""
    return object

def test_trap_fork(usec_timeout=None, test_trap_flags=None):
    """"""
    return object

def test_trap_has_passed():
    """"""
    return object

def test_trap_reached_timeout():
    """"""
    return object

def test_trap_subprocess(test_path=None, usec_timeout=None, test_flags=None):
    """"""
    return object

def thread_error_quark():
    """"""
    return object

def thread_exit(retval=None):
    """"""
    return object

def thread_pool_get_max_idle_time():
    """"""
    return object

def thread_pool_get_max_unused_threads():
    """"""
    return object

def thread_pool_get_num_unused_threads():
    """"""
    return object

def thread_pool_set_max_idle_time(interval=None):
    """"""
    return object

def thread_pool_set_max_unused_threads(max_threads=None):
    """"""
    return object

def thread_pool_stop_unused_threads():
    """"""
    return object

def thread_self():
    """"""
    return object

def thread_yield():
    """"""
    return object

def time_val_from_iso8601(iso_date=None, time_=None):
    """"""
    return object

def timeout_add(interval=None, function=None, data=None):
    """"""
    return object

def timeout_add_full(priority=None, interval=None, function=None, data=None, notify=None):
    """"""
    return object

def timeout_add_seconds(interval=None, function=None, data=None):
    """"""
    return object

def timeout_add_seconds_full(priority=None, interval=None, function=None, data=None, notify=None):
    """"""
    return object

def timeout_source_new(interval=None):
    """"""
    return object

def timeout_source_new_seconds(interval=None):
    """"""
    return object

def trash_stack_height(stack_p=None):
    """"""
    return object

def trash_stack_peek(stack_p=None):
    """"""
    return object

def trash_stack_pop(stack_p=None):
    """"""
    return object

def trash_stack_push(stack_p=None, data_p=None):
    """"""
    return object

def try_malloc(n_bytes=None):
    """"""
    return object

def try_malloc0(n_bytes=None):
    """"""
    return object

def try_malloc0_n(n_blocks=None, n_block_bytes=None):
    """"""
    return object

def try_malloc_n(n_blocks=None, n_block_bytes=None):
    """"""
    return object

def try_realloc(mem=None, n_bytes=None):
    """"""
    return object

def try_realloc_n(mem=None, n_blocks=None, n_block_bytes=None):
    """"""
    return object

def ucs4_to_utf16(str=None, len=None, items_read=None, items_written=None):
    """"""
    return object

def ucs4_to_utf8(str=None, len=None, items_read=None, items_written=None):
    """"""
    return object

def unichar_break_type(c=None):
    """"""
    return object

def unichar_combining_class(uc=None):
    """"""
    return object

def unichar_compose(a=None, b=None, ch=None):
    """"""
    return object

def unichar_decompose(ch=None, a=None, b=None):
    """"""
    return object

def unichar_digit_value(c=None):
    """"""
    return object

def unichar_fully_decompose(ch=None, compat=None, result=None, result_len=None):
    """"""
    return object

def unichar_get_mirror_char(ch=None, mirrored_ch=None):
    """"""
    return object

def unichar_get_script(ch=None):
    """"""
    return object

def unichar_isalnum(c=None):
    """"""
    return object

def unichar_isalpha(c=None):
    """"""
    return object

def unichar_iscntrl(c=None):
    """"""
    return object

def unichar_isdefined(c=None):
    """"""
    return object

def unichar_isdigit(c=None):
    """"""
    return object

def unichar_isgraph(c=None):
    """"""
    return object

def unichar_islower(c=None):
    """"""
    return object

def unichar_ismark(c=None):
    """"""
    return object

def unichar_isprint(c=None):
    """"""
    return object

def unichar_ispunct(c=None):
    """"""
    return object

def unichar_isspace(c=None):
    """"""
    return object

def unichar_istitle(c=None):
    """"""
    return object

def unichar_isupper(c=None):
    """"""
    return object

def unichar_iswide(c=None):
    """"""
    return object

def unichar_iswide_cjk(c=None):
    """"""
    return object

def unichar_isxdigit(c=None):
    """"""
    return object

def unichar_iszerowidth(c=None):
    """"""
    return object

def unichar_to_utf8(c=None, outbuf=None):
    """"""
    return object

def unichar_tolower(c=None):
    """"""
    return object

def unichar_totitle(c=None):
    """"""
    return object

def unichar_toupper(c=None):
    """"""
    return object

def unichar_type(c=None):
    """"""
    return object

def unichar_validate(ch=None):
    """"""
    return object

def unichar_xdigit_value(c=None):
    """"""
    return object

def unicode_canonical_decomposition(ch=None, result_len=None):
    """"""
    return object

def unicode_canonical_ordering(string=None, len=None):
    """"""
    return object

def unicode_script_from_iso15924(iso15924=None):
    """"""
    return object

def unicode_script_to_iso15924(script=None):
    """"""
    return object

def unix_error_quark():
    """"""
    return object

def unix_fd_add(fd=None, condition=None, function=None, user_data=None):
    """"""
    return object

def unix_fd_add_full(priority=None, fd=None, condition=None, function=None, user_data=None, notify=None):
    """"""
    return object

def unix_fd_source_new(fd=None, condition=None):
    """"""
    return object

def unix_open_pipe(fds=None, flags=None):
    """"""
    return object

def unix_set_fd_nonblocking(fd=None, nonblock=None):
    """"""
    return object

def unix_signal_add(signum=None, handler=None, user_data=None):
    """"""
    return object

def unix_signal_add_full(priority=None, signum=None, handler=None, user_data=None, notify=None):
    """"""
    return object

def unix_signal_source_new(signum=None):
    """"""
    return object

def unlink(filename=None):
    """"""
    return object

def unsetenv(variable=None):
    """"""
    return object

def uri_escape_string(unescaped=None, reserved_chars_allowed=None, allow_utf8=None):
    """"""
    return object

def uri_list_extract_uris(uri_list=None):
    """"""
    return object

def uri_parse_scheme(uri=None):
    """"""
    return object

def uri_unescape_segment(escaped_string=None, escaped_string_end=None, illegal_characters=None):
    """"""
    return object

def uri_unescape_string(escaped_string=None, illegal_characters=None):
    """"""
    return object

def usleep(microseconds=None):
    """"""
    return object

def utf16_to_ucs4(str=None, len=None, items_read=None, items_written=None):
    """"""
    return object

def utf16_to_utf8(str=None, len=None, items_read=None, items_written=None):
    """"""
    return object

def utf8_casefold(str=None, len=None):
    """"""
    return object

def utf8_collate(str1=None, str2=None):
    """"""
    return object

def utf8_collate_key(str=None, len=None):
    """"""
    return object

def utf8_collate_key_for_filename(str=None, len=None):
    """"""
    return object

def utf8_find_next_char(p=None, end=None):
    """"""
    return object

def utf8_find_prev_char(str=None, p=None):
    """"""
    return object

def utf8_get_char(p=None):
    """"""
    return object

def utf8_get_char_validated(p=None, max_len=None):
    """"""
    return object

def utf8_make_valid(str=None, len=None):
    """"""
    return object

def utf8_normalize(str=None, len=None, mode=None):
    """"""
    return object

def utf8_offset_to_pointer(str=None, offset=None):
    """"""
    return object

def utf8_pointer_to_offset(str=None, pos=None):
    """"""
    return object

def utf8_prev_char(p=None):
    """"""
    return object

def utf8_strchr(p=None, len=None, c=None):
    """"""
    return object

def utf8_strdown(str=None, len=None):
    """"""
    return object

def utf8_strlen(p=None, max=None):
    """"""
    return object

def utf8_strncpy(dest=None, src=None, n=None):
    """"""
    return object

def utf8_strrchr(p=None, len=None, c=None):
    """"""
    return object

def utf8_strreverse(str=None, len=None):
    """"""
    return object

def utf8_strup(str=None, len=None):
    """"""
    return object

def utf8_substring(str=None, start_pos=None, end_pos=None):
    """"""
    return object

def utf8_to_ucs4(str=None, len=None, items_read=None, items_written=None):
    """"""
    return object

def utf8_to_ucs4_fast(str=None, len=None, items_written=None):
    """"""
    return object

def utf8_to_utf16(str=None, len=None, items_read=None, items_written=None):
    """"""
    return object

def utf8_validate(str=None, max_len=None, end=None):
    """"""
    return object

def uuid_string_is_valid(str=None):
    """"""
    return object

def uuid_string_random():
    """"""
    return object

def variant_get_gtype():
    """"""
    return object

def variant_is_object_path(string=None):
    """"""
    return object

def variant_is_signature(string=None):
    """"""
    return object

def variant_parse(type=None, text=None, limit=None, endptr=None):
    """"""
    return object

def variant_parse_error_print_context(error=None, source_str=None):
    """"""
    return object

def variant_parse_error_quark():
    """"""
    return object

def variant_parser_get_error_quark():
    """"""
    return object

def variant_type_checked_(arg0=None):
    """"""
    return object

def variant_type_string_is_valid(type_string=None):
    """"""
    return object

def variant_type_string_scan(string=None, limit=None, endptr=None):
    """"""
    return object

def vasprintf(string=None, format=None, args=None):
    """"""
    return object

def vfprintf(file=None, format=None, args=None):
    """"""
    return object

def vprintf(format=None, args=None):
    """"""
    return object

def vsnprintf(string=None, n=None, format=None, args=None):
    """"""
    return object

def vsprintf(string=None, format=None, args=None):
    """"""
    return object

def warn_message(domain=None, file=None, line=None, func=None, warnexpr=None):
    """"""
    return object


class Array():
    """"""
    @staticmethod
    def append_vals(array=None, data=None, len=None):
        """"""
        return object
    @staticmethod
    def free(array=None, free_segment=None):
        """"""
        return object
    @staticmethod
    def get_element_size(array=None):
        """"""
        return object
    @staticmethod
    def insert_vals(array=None, index_=None, data=None, len=None):
        """"""
        return object
    @staticmethod
    def new(zero_terminated=None, clear_=None, element_size=None):
        """"""
        return object
    @staticmethod
    def prepend_vals(array=None, data=None, len=None):
        """"""
        return object
    @staticmethod
    def ref(array=None):
        """"""
        return object
    @staticmethod
    def remove_index(array=None, index_=None):
        """"""
        return object
    @staticmethod
    def remove_index_fast(array=None, index_=None):
        """"""
        return object
    @staticmethod
    def remove_range(array=None, index_=None, length=None):
        """"""
        return object
    @staticmethod
    def set_clear_func(array=None, clear_func=None):
        """"""
        return object
    @staticmethod
    def set_size(array=None, length=None):
        """"""
        return object
    @staticmethod
    def sized_new(zero_terminated=None, clear_=None, element_size=None, reserved_size=None):
        """"""
        return object
    @staticmethod
    def sort(array=None, compare_func=None):
        """"""
        return object
    @staticmethod
    def sort_with_data(array=None, compare_func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def unref(array=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def len(self):
        return object


class AsyncQueue():
    """"""
    
    def length(self):
        """"""
        return object
    
    def length_unlocked(self):
        """"""
        return object
    
    def lock(self):
        """"""
        return object
    
    def pop(self):
        """"""
        return object
    
    def pop_unlocked(self):
        """"""
        return object
    
    def push(self, data=None):
        """"""
        return object
    
    def push_front(self, item=None):
        """"""
        return object
    
    def push_front_unlocked(self, item=None):
        """"""
        return object
    
    def push_sorted(self, data=None, func=None, user_data=None):
        """"""
        return object
    
    def push_sorted_unlocked(self, data=None, func=None, user_data=None):
        """"""
        return object
    
    def push_unlocked(self, data=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def ref_unlocked(self):
        """"""
        return object
    
    def remove(self, item=None):
        """"""
        return object
    
    def remove_unlocked(self, item=None):
        """"""
        return object
    
    def sort(self, func=None, user_data=None):
        """"""
        return object
    
    def sort_unlocked(self, func=None, user_data=None):
        """"""
        return object
    
    def timed_pop(self, end_time=None):
        """"""
        return object
    
    def timed_pop_unlocked(self, end_time=None):
        """"""
        return object
    
    def timeout_pop(self, timeout=None):
        """"""
        return object
    
    def timeout_pop_unlocked(self, timeout=None):
        """"""
        return object
    
    def try_pop(self):
        """"""
        return object
    
    def try_pop_unlocked(self):
        """"""
        return object
    
    def unlock(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def unref_and_unlock(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_full(item_free_func=None):
        """"""
        return object


class BookmarkFile():
    """"""
    
    def add_application(self, uri=None, name=None, exec=None):
        """"""
        return object
    
    def add_group(self, uri=None, group=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_added(self, uri=None):
        """"""
        return object
    
    def get_app_info(self, uri=None, name=None, exec=None, count=None, stamp=None):
        """"""
        return object
    
    def get_applications(self, uri=None, length=None):
        """"""
        return object
    
    def get_description(self, uri=None):
        """"""
        return object
    
    def get_groups(self, uri=None, length=None):
        """"""
        return object
    
    def get_icon(self, uri=None, href=None, mime_type=None):
        """"""
        return object
    
    def get_is_private(self, uri=None):
        """"""
        return object
    
    def get_mime_type(self, uri=None):
        """"""
        return object
    
    def get_modified(self, uri=None):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def get_title(self, uri=None):
        """"""
        return object
    
    def get_uris(self, length=None):
        """"""
        return object
    
    def get_visited(self, uri=None):
        """"""
        return object
    
    def has_application(self, uri=None, name=None):
        """"""
        return object
    
    def has_group(self, uri=None, group=None):
        """"""
        return object
    
    def has_item(self, uri=None):
        """"""
        return object
    
    def load_from_data(self, data=None, length=None):
        """"""
        return object
    
    def load_from_data_dirs(self, file=None, full_path=None):
        """"""
        return object
    
    def load_from_file(self, filename=None):
        """"""
        return object
    
    def move_item(self, old_uri=None, new_uri=None):
        """"""
        return object
    
    def remove_application(self, uri=None, name=None):
        """"""
        return object
    
    def remove_group(self, uri=None, group=None):
        """"""
        return object
    
    def remove_item(self, uri=None):
        """"""
        return object
    
    def set_added(self, uri=None, added=None):
        """"""
        return object
    
    def set_app_info(self, uri=None, name=None, exec=None, count=None, stamp=None):
        """"""
        return object
    
    def set_description(self, uri=None, description=None):
        """"""
        return object
    
    def set_groups(self, uri=None, groups=None, length=None):
        """"""
        return object
    
    def set_icon(self, uri=None, href=None, mime_type=None):
        """"""
        return object
    
    def set_is_private(self, uri=None, is_private=None):
        """"""
        return object
    
    def set_mime_type(self, uri=None, mime_type=None):
        """"""
        return object
    
    def set_modified(self, uri=None, modified=None):
        """"""
        return object
    
    def set_title(self, uri=None, title=None):
        """"""
        return object
    
    def set_visited(self, uri=None, visited=None):
        """"""
        return object
    
    def to_data(self, length=None):
        """"""
        return object
    
    def to_file(self, filename=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object


class ByteArray():
    """"""
    @staticmethod
    def append(array=None, data=None, len=None):
        """"""
        return object
    @staticmethod
    def free(array=None, free_segment=None):
        """"""
        return object
    @staticmethod
    def free_to_bytes(array=None):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_take(data=None, len=None):
        """"""
        return object
    @staticmethod
    def prepend(array=None, data=None, len=None):
        """"""
        return object
    @staticmethod
    def ref(array=None):
        """"""
        return object
    @staticmethod
    def remove_index(array=None, index_=None):
        """"""
        return object
    @staticmethod
    def remove_index_fast(array=None, index_=None):
        """"""
        return object
    @staticmethod
    def remove_range(array=None, index_=None, length=None):
        """"""
        return object
    @staticmethod
    def set_size(array=None, length=None):
        """"""
        return object
    @staticmethod
    def sized_new(reserved_size=None):
        """"""
        return object
    @staticmethod
    def sort(array=None, compare_func=None):
        """"""
        return object
    @staticmethod
    def sort_with_data(array=None, compare_func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def unref(array=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def len(self):
        return object


class Bytes():
    """"""
    
    def __init__(self, data=None, size=None):
        """"""
        return object
    @staticmethod
    def new(data=None, size=None):
        """"""
        return object
    @staticmethod
    def new_static(data=None, size=None):
        """"""
        return object
    @staticmethod
    def new_take(data=None, size=None):
        """"""
        return object
    @staticmethod
    def new_with_free_func(data=None, size=None, free_func=None, user_data=None):
        """"""
        return object
    
    def compare(self, bytes2=None):
        """"""
        return object
    
    def equal(self, bytes2=None):
        """"""
        return object
    
    def get_data(self, size=None):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def new_from_bytes(self, offset=None, length=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def unref_to_array(self):
        """"""
        return object
    
    def unref_to_data(self, size=None):
        """"""
        return object


class Checksum():
    """"""
    
    def __init__(self, checksum_type=None):
        """"""
        return object
    @staticmethod
    def new(checksum_type=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_digest(self, buffer=None, digest_len=None):
        """"""
        return object
    
    def get_string(self):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def update(self, data=None, length=None):
        """"""
        return object
    @staticmethod
    def type_get_length(checksum_type=None):
        """"""
        return object


class Cond():
    """"""
    
    def broadcast(self):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def signal(self):
        """"""
        return object
    
    def wait(self, mutex=None):
        """"""
        return object
    
    def wait_until(self, mutex=None, end_time=None):
        """"""
        return object

    @property
    def p(self):
        return object

    @property
    def i(self):
        return object


class Data():
    """"""


class Date():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_dmy(day=None, month=None, year=None):
        """"""
        return object
    @staticmethod
    def new_julian(julian_day=None):
        """"""
        return object
    
    def add_days(self, n_days=None):
        """"""
        return object
    
    def add_months(self, n_months=None):
        """"""
        return object
    
    def add_years(self, n_years=None):
        """"""
        return object
    
    def clamp(self, min_date=None, max_date=None):
        """"""
        return object
    
    def clear(self, n_dates=None):
        """"""
        return object
    
    def compare(self, rhs=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def days_between(self, date2=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_day(self):
        """"""
        return object
    
    def get_day_of_year(self):
        """"""
        return object
    
    def get_iso8601_week_of_year(self):
        """"""
        return object
    
    def get_julian(self):
        """"""
        return object
    
    def get_monday_week_of_year(self):
        """"""
        return object
    
    def get_month(self):
        """"""
        return object
    
    def get_sunday_week_of_year(self):
        """"""
        return object
    
    def get_weekday(self):
        """"""
        return object
    
    def get_year(self):
        """"""
        return object
    
    def is_first_of_month(self):
        """"""
        return object
    
    def is_last_of_month(self):
        """"""
        return object
    
    def order(self, date2=None):
        """"""
        return object
    
    def set_day(self, day=None):
        """"""
        return object
    
    def set_dmy(self, day=None, month=None, y=None):
        """"""
        return object
    
    def set_julian(self, julian_date=None):
        """"""
        return object
    
    def set_month(self, month=None):
        """"""
        return object
    
    def set_parse(self, str=None):
        """"""
        return object
    
    def set_time(self, time_=None):
        """"""
        return object
    
    def set_time_t(self, timet=None):
        """"""
        return object
    
    def set_time_val(self, timeval=None):
        """"""
        return object
    
    def set_year(self, year=None):
        """"""
        return object
    
    def subtract_days(self, n_days=None):
        """"""
        return object
    
    def subtract_months(self, n_months=None):
        """"""
        return object
    
    def subtract_years(self, n_years=None):
        """"""
        return object
    
    def to_struct_tm(self, tm=None):
        """"""
        return object
    
    def valid(self):
        """"""
        return object
    @staticmethod
    def get_days_in_month(month=None, year=None):
        """"""
        return object
    @staticmethod
    def get_monday_weeks_in_year(year=None):
        """"""
        return object
    @staticmethod
    def get_sunday_weeks_in_year(year=None):
        """"""
        return object
    @staticmethod
    def is_leap_year(year=None):
        """"""
        return object
    @staticmethod
    def strftime(s=None, slen=None, format=None, date=None):
        """"""
        return object
    @staticmethod
    def valid_day(day=None):
        """"""
        return object
    @staticmethod
    def valid_dmy(day=None, month=None, year=None):
        """"""
        return object
    @staticmethod
    def valid_julian(julian_date=None):
        """"""
        return object
    @staticmethod
    def valid_month(month=None):
        """"""
        return object
    @staticmethod
    def valid_weekday(weekday=None):
        """"""
        return object
    @staticmethod
    def valid_year(year=None):
        """"""
        return object

    @property
    def julian_days(self):
        return object

    @property
    def julian(self):
        return object

    @property
    def dmy(self):
        return object

    @property
    def day(self):
        return object

    @property
    def month(self):
        return object

    @property
    def year(self):
        return object


class DateTime():
    """"""
    
    def __init__(self, tz=None, year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object
    @staticmethod
    def new(tz=None, year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object
    @staticmethod
    def new_from_iso8601(text=None, default_tz=None):
        """"""
        return object
    @staticmethod
    def new_from_timeval_local(tv=None):
        """"""
        return object
    @staticmethod
    def new_from_timeval_utc(tv=None):
        """"""
        return object
    @staticmethod
    def new_from_unix_local(t=None):
        """"""
        return object
    @staticmethod
    def new_from_unix_utc(t=None):
        """"""
        return object
    @staticmethod
    def new_local(year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object
    @staticmethod
    def new_now(tz=None):
        """"""
        return object
    @staticmethod
    def new_now_local():
        """"""
        return object
    @staticmethod
    def new_now_utc():
        """"""
        return object
    @staticmethod
    def new_utc(year=None, month=None, day=None, hour=None, minute=None, seconds=None):
        """"""
        return object
    
    def add(self, timespan=None):
        """"""
        return object
    
    def add_days(self, days=None):
        """"""
        return object
    
    def add_full(self, years=None, months=None, days=None, hours=None, minutes=None, seconds=None):
        """"""
        return object
    
    def add_hours(self, hours=None):
        """"""
        return object
    
    def add_minutes(self, minutes=None):
        """"""
        return object
    
    def add_months(self, months=None):
        """"""
        return object
    
    def add_seconds(self, seconds=None):
        """"""
        return object
    
    def add_weeks(self, weeks=None):
        """"""
        return object
    
    def add_years(self, years=None):
        """"""
        return object
    
    def difference(self, begin=None):
        """"""
        return object
    
    def format(self, format=None):
        """"""
        return object
    
    def get_day_of_month(self):
        """"""
        return object
    
    def get_day_of_week(self):
        """"""
        return object
    
    def get_day_of_year(self):
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
    
    def get_seconds(self):
        """"""
        return object
    
    def get_timezone_abbreviation(self):
        """"""
        return object
    
    def get_utc_offset(self):
        """"""
        return object
    
    def get_week_numbering_year(self):
        """"""
        return object
    
    def get_week_of_year(self):
        """"""
        return object
    
    def get_year(self):
        """"""
        return object
    
    def get_ymd(self, year=None, month=None, day=None):
        """"""
        return object
    
    def is_daylight_savings(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def to_local(self):
        """"""
        return object
    
    def to_timeval(self, tv=None):
        """"""
        return object
    
    def to_timezone(self, tz=None):
        """"""
        return object
    
    def to_unix(self):
        """"""
        return object
    
    def to_utc(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def compare(dt1=None, dt2=None):
        """"""
        return object
    @staticmethod
    def equal(dt1=None, dt2=None):
        """"""
        return object
    @staticmethod
    def hash(datetime=None):
        """"""
        return object


class DebugKey():
    """"""

    @property
    def key(self):
        return object

    @property
    def value(self):
        return object


class Dir():
    """"""
    
    def close(self):
        """"""
        return object
    
    def read_name(self):
        """"""
        return object
    
    def rewind(self):
        """"""
        return object
    @staticmethod
    def make_tmp(tmpl=None):
        """"""
        return object
    @staticmethod
    def open(path=None, flags=None):
        """"""
        return object


class Error():
    """"""
    
    def __init__(self, domain=None, code=None, format=None, *args):
        """"""
        return object
    @staticmethod
    def new(domain=None, code=None, format=None, *args):
        """"""
        return object
    @staticmethod
    def new_literal(domain=None, code=None, message=None):
        """"""
        return object
    @staticmethod
    def new_valist(domain=None, code=None, format=None, args=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def matches(self, domain=None, code=None):
        """"""
        return object

    @property
    def domain(self):
        return object

    @property
    def code(self):
        return object

    @property
    def message(self):
        return object


class HashTable():
    """"""
    @staticmethod
    def add(hash_table=None, key=None):
        """"""
        return object
    @staticmethod
    def contains(hash_table=None, key=None):
        """"""
        return object
    @staticmethod
    def destroy(hash_table=None):
        """"""
        return object
    @staticmethod
    def find(hash_table=None, predicate=None, user_data=None):
        """"""
        return object
    @staticmethod
    def foreach(hash_table=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def foreach_remove(hash_table=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def foreach_steal(hash_table=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def get_keys(hash_table=None):
        """"""
        return object
    @staticmethod
    def get_keys_as_array(hash_table=None, length=None):
        """"""
        return object
    @staticmethod
    def get_values(hash_table=None):
        """"""
        return object
    @staticmethod
    def insert(hash_table=None, key=None, value=None):
        """"""
        return object
    @staticmethod
    def lookup(hash_table=None, key=None):
        """"""
        return object
    @staticmethod
    def lookup_extended(hash_table=None, lookup_key=None, orig_key=None, value=None):
        """"""
        return object
    @staticmethod
    def new(hash_func=None, key_equal_func=None):
        """"""
        return object
    @staticmethod
    def new_full(hash_func=None, key_equal_func=None, key_destroy_func=None, value_destroy_func=None):
        """"""
        return object
    @staticmethod
    def ref(hash_table=None):
        """"""
        return object
    @staticmethod
    def remove(hash_table=None, key=None):
        """"""
        return object
    @staticmethod
    def remove_all(hash_table=None):
        """"""
        return object
    @staticmethod
    def replace(hash_table=None, key=None, value=None):
        """"""
        return object
    @staticmethod
    def size(hash_table=None):
        """"""
        return object
    @staticmethod
    def steal(hash_table=None, key=None):
        """"""
        return object
    @staticmethod
    def steal_all(hash_table=None):
        """"""
        return object
    @staticmethod
    def unref(hash_table=None):
        """"""
        return object


class HashTableIter():
    """"""
    
    def get_hash_table(self):
        """"""
        return object
    
    def init(self, hash_table=None):
        """"""
        return object
    
    def next(self, key=None, value=None):
        """"""
        return object
    
    def remove(self):
        """"""
        return object
    
    def replace(self, value=None):
        """"""
        return object
    
    def steal(self):
        """"""
        return object

    @property
    def dummy1(self):
        return object

    @property
    def dummy2(self):
        return object

    @property
    def dummy3(self):
        return object

    @property
    def dummy4(self):
        return object

    @property
    def dummy5(self):
        return object

    @property
    def dummy6(self):
        return object


class Hmac():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def get_digest(self, buffer=None, digest_len=None):
        """"""
        return object
    
    def get_string(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def update(self, data=None, length=None):
        """"""
        return object
    @staticmethod
    def new(digest_type=None, key=None, key_len=None):
        """"""
        return object


class Hook():
    """"""
    
    def compare_ids(self, sibling=None):
        """"""
        return object
    @staticmethod
    def alloc(hook_list=None):
        """"""
        return object
    @staticmethod
    def destroy(hook_list=None, hook_id=None):
        """"""
        return object
    @staticmethod
    def destroy_link(hook_list=None, hook=None):
        """"""
        return object
    @staticmethod
    def find(hook_list=None, need_valids=None, func=None, data=None):
        """"""
        return object
    @staticmethod
    def find_data(hook_list=None, need_valids=None, data=None):
        """"""
        return object
    @staticmethod
    def find_func(hook_list=None, need_valids=None, func=None):
        """"""
        return object
    @staticmethod
    def find_func_data(hook_list=None, need_valids=None, func=None, data=None):
        """"""
        return object
    @staticmethod
    def first_valid(hook_list=None, may_be_in_call=None):
        """"""
        return object
    @staticmethod
    def free(hook_list=None, hook=None):
        """"""
        return object
    @staticmethod
    def get(hook_list=None, hook_id=None):
        """"""
        return object
    @staticmethod
    def insert_before(hook_list=None, sibling=None, hook=None):
        """"""
        return object
    @staticmethod
    def insert_sorted(hook_list=None, hook=None, func=None):
        """"""
        return object
    @staticmethod
    def next_valid(hook_list=None, hook=None, may_be_in_call=None):
        """"""
        return object
    @staticmethod
    def prepend(hook_list=None, hook=None):
        """"""
        return object
    @staticmethod
    def ref(hook_list=None, hook=None):
        """"""
        return object
    @staticmethod
    def unref(hook_list=None, hook=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def next(self):
        return object

    @property
    def prev(self):
        return object

    @property
    def ref_count(self):
        return object

    @property
    def hook_id(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def func(self):
        return object

    @property
    def destroy(self):
        return object


class HookList():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def init(self, hook_size=None):
        """"""
        return object
    
    def invoke(self, may_recurse=None):
        """"""
        return object
    
    def invoke_check(self, may_recurse=None):
        """"""
        return object
    
    def marshal(self, may_recurse=None, marshaller=None, marshal_data=None):
        """"""
        return object
    
    def marshal_check(self, may_recurse=None, marshaller=None, marshal_data=None):
        """"""
        return object

    @property
    def seq_id(self):
        return object

    @property
    def hook_size(self):
        return object

    @property
    def is_setup(self):
        return object

    @property
    def hooks(self):
        return object

    @property
    def dummy3(self):
        return object

    @property
    def finalize_hook(self):
        return object

    @property
    def dummy(self):
        return object


class IConv():
    """"""
    
    def (self, inbuf=None, inbytes_left=None, outbuf=None, outbytes_left=None):
        """"""
        return object
    
    def close(self):
        """"""
        return object
    @staticmethod
    def open(to_codeset=None, from_codeset=None):
        """"""
        return object


class IOChannel():
    """"""
    @staticmethod
    def new_file(filename=None, mode=None):
        """"""
        return object
    @staticmethod
    def unix_new(fd=None):
        """"""
        return object
    
    def close(self):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def get_buffer_condition(self):
        """"""
        return object
    
    def get_buffer_size(self):
        """"""
        return object
    
    def get_buffered(self):
        """"""
        return object
    
    def get_close_on_unref(self):
        """"""
        return object
    
    def get_encoding(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_line_term(self, length=None):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def read(self, buf=None, count=None, bytes_read=None):
        """"""
        return object
    
    def read_chars(self, buf=None, count=None, bytes_read=None):
        """"""
        return object
    
    def read_line(self, str_return=None, length=None, terminator_pos=None):
        """"""
        return object
    
    def read_line_string(self, buffer=None, terminator_pos=None):
        """"""
        return object
    
    def read_to_end(self, str_return=None, length=None):
        """"""
        return object
    
    def read_unichar(self, thechar=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def seek(self, offset=None, type=None):
        """"""
        return object
    
    def seek_position(self, offset=None, type=None):
        """"""
        return object
    
    def set_buffer_size(self, size=None):
        """"""
        return object
    
    def set_buffered(self, buffered=None):
        """"""
        return object
    
    def set_close_on_unref(self, do_close=None):
        """"""
        return object
    
    def set_encoding(self, encoding=None):
        """"""
        return object
    
    def set_flags(self, flags=None):
        """"""
        return object
    
    def set_line_term(self, line_term=None, length=None):
        """"""
        return object
    
    def shutdown(self, flush=None):
        """"""
        return object
    
    def unix_get_fd(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def write(self, buf=None, count=None, bytes_written=None):
        """"""
        return object
    
    def write_chars(self, buf=None, count=None, bytes_written=None):
        """"""
        return object
    
    def write_unichar(self, thechar=None):
        """"""
        return object
    @staticmethod
    def error_from_errno(en=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def funcs(self):
        return object

    @property
    def encoding(self):
        return object

    @property
    def read_cd(self):
        return object

    @property
    def write_cd(self):
        return object

    @property
    def line_term(self):
        return object

    @property
    def line_term_len(self):
        return object

    @property
    def buf_size(self):
        return object

    @property
    def read_buf(self):
        return object

    @property
    def encoded_read_buf(self):
        return object

    @property
    def write_buf(self):
        return object

    @property
    def partial_write_buf(self):
        return object

    @property
    def use_buffer(self):
        return object

    @property
    def do_encode(self):
        return object

    @property
    def close_on_unref(self):
        return object

    @property
    def is_readable(self):
        return object

    @property
    def is_writeable(self):
        return object

    @property
    def is_seekable(self):
        return object

    @property
    def reserved1(self):
        return object

    @property
    def reserved2(self):
        return object


class IOFuncs():
    """"""

    @property
    def io_read(self):
        return object

    @property
    def io_write(self):
        return object

    @property
    def io_seek(self):
        return object

    @property
    def io_close(self):
        return object

    @property
    def io_create_watch(self):
        return object

    @property
    def io_free(self):
        return object

    @property
    def io_set_flags(self):
        return object

    @property
    def io_get_flags(self):
        return object


class KeyFile():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_boolean(self, group_name=None, key=None):
        """"""
        return object
    
    def get_boolean_list(self, group_name=None, key=None, length=None):
        """"""
        return object
    
    def get_comment(self, group_name=None, key=None):
        """"""
        return object
    
    def get_double(self, group_name=None, key=None):
        """"""
        return object
    
    def get_double_list(self, group_name=None, key=None, length=None):
        """"""
        return object
    
    def get_groups(self, length=None):
        """"""
        return object
    
    def get_int64(self, group_name=None, key=None):
        """"""
        return object
    
    def get_integer(self, group_name=None, key=None):
        """"""
        return object
    
    def get_integer_list(self, group_name=None, key=None, length=None):
        """"""
        return object
    
    def get_keys(self, group_name=None, length=None):
        """"""
        return object
    
    def get_locale_for_key(self, group_name=None, key=None, locale=None):
        """"""
        return object
    
    def get_locale_string(self, group_name=None, key=None, locale=None):
        """"""
        return object
    
    def get_locale_string_list(self, group_name=None, key=None, locale=None, length=None):
        """"""
        return object
    
    def get_start_group(self):
        """"""
        return object
    
    def get_string(self, group_name=None, key=None):
        """"""
        return object
    
    def get_string_list(self, group_name=None, key=None, length=None):
        """"""
        return object
    
    def get_uint64(self, group_name=None, key=None):
        """"""
        return object
    
    def get_value(self, group_name=None, key=None):
        """"""
        return object
    
    def has_group(self, group_name=None):
        """"""
        return object
    
    def has_key(self, group_name=None, key=None):
        """"""
        return object
    
    def load_from_bytes(self, bytes=None, flags=None):
        """"""
        return object
    
    def load_from_data(self, data=None, length=None, flags=None):
        """"""
        return object
    
    def load_from_data_dirs(self, file=None, full_path=None, flags=None):
        """"""
        return object
    
    def load_from_dirs(self, file=None, search_dirs=None, full_path=None, flags=None):
        """"""
        return object
    
    def load_from_file(self, file=None, flags=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def remove_comment(self, group_name=None, key=None):
        """"""
        return object
    
    def remove_group(self, group_name=None):
        """"""
        return object
    
    def remove_key(self, group_name=None, key=None):
        """"""
        return object
    
    def save_to_file(self, filename=None):
        """"""
        return object
    
    def set_boolean(self, group_name=None, key=None, value=None):
        """"""
        return object
    
    def set_boolean_list(self, group_name=None, key=None, list=None, length=None):
        """"""
        return object
    
    def set_comment(self, group_name=None, key=None, comment=None):
        """"""
        return object
    
    def set_double(self, group_name=None, key=None, value=None):
        """"""
        return object
    
    def set_double_list(self, group_name=None, key=None, list=None, length=None):
        """"""
        return object
    
    def set_int64(self, group_name=None, key=None, value=None):
        """"""
        return object
    
    def set_integer(self, group_name=None, key=None, value=None):
        """"""
        return object
    
    def set_integer_list(self, group_name=None, key=None, list=None, length=None):
        """"""
        return object
    
    def set_list_separator(self, separator=None):
        """"""
        return object
    
    def set_locale_string(self, group_name=None, key=None, locale=None, string=None):
        """"""
        return object
    
    def set_locale_string_list(self, group_name=None, key=None, locale=None, list=None, length=None):
        """"""
        return object
    
    def set_string(self, group_name=None, key=None, string=None):
        """"""
        return object
    
    def set_string_list(self, group_name=None, key=None, list=None, length=None):
        """"""
        return object
    
    def set_uint64(self, group_name=None, key=None, value=None):
        """"""
        return object
    
    def set_value(self, group_name=None, key=None, value=None):
        """"""
        return object
    
    def to_data(self, length=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object


class List():
    """"""
    @staticmethod
    def alloc():
        """"""
        return object
    @staticmethod
    def append(list=None, data=None):
        """"""
        return object
    @staticmethod
    def concat(list1=None, list2=None):
        """"""
        return object
    @staticmethod
    def copy(list=None):
        """"""
        return object
    @staticmethod
    def copy_deep(list=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def delete_link(list=None, link_=None):
        """"""
        return object
    @staticmethod
    def find(list=None, data=None):
        """"""
        return object
    @staticmethod
    def find_custom(list=None, data=None, func=None):
        """"""
        return object
    @staticmethod
    def first(list=None):
        """"""
        return object
    @staticmethod
    def foreach(list=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def free(list=None):
        """"""
        return object
    @staticmethod
    def free_1(list=None):
        """"""
        return object
    @staticmethod
    def free_full(list=None, free_func=None):
        """"""
        return object
    @staticmethod
    def index(list=None, data=None):
        """"""
        return object
    @staticmethod
    def insert(list=None, data=None, position=None):
        """"""
        return object
    @staticmethod
    def insert_before(list=None, sibling=None, data=None):
        """"""
        return object
    @staticmethod
    def insert_sorted(list=None, data=None, func=None):
        """"""
        return object
    @staticmethod
    def insert_sorted_with_data(list=None, data=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def last(list=None):
        """"""
        return object
    @staticmethod
    def length(list=None):
        """"""
        return object
    @staticmethod
    def nth(list=None, n=None):
        """"""
        return object
    @staticmethod
    def nth_data(list=None, n=None):
        """"""
        return object
    @staticmethod
    def nth_prev(list=None, n=None):
        """"""
        return object
    @staticmethod
    def position(list=None, llink=None):
        """"""
        return object
    @staticmethod
    def prepend(list=None, data=None):
        """"""
        return object
    @staticmethod
    def remove(list=None, data=None):
        """"""
        return object
    @staticmethod
    def remove_all(list=None, data=None):
        """"""
        return object
    @staticmethod
    def remove_link(list=None, llink=None):
        """"""
        return object
    @staticmethod
    def reverse(list=None):
        """"""
        return object
    @staticmethod
    def sort(list=None, compare_func=None):
        """"""
        return object
    @staticmethod
    def sort_with_data(list=None, compare_func=None, user_data=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def next(self):
        return object

    @property
    def prev(self):
        return object


class LogField():
    """"""

    @property
    def key(self):
        return object

    @property
    def value(self):
        return object

    @property
    def length(self):
        return object


class MainContext():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def acquire(self):
        """"""
        return object
    
    def add_poll(self, fd=None, priority=None):
        """"""
        return object
    
    def check(self, max_priority=None, fds=None, n_fds=None):
        """"""
        return object
    
    def dispatch(self):
        """"""
        return object
    
    def find_source_by_funcs_user_data(self, funcs=None, user_data=None):
        """"""
        return object
    
    def find_source_by_id(self, source_id=None):
        """"""
        return object
    
    def find_source_by_user_data(self, user_data=None):
        """"""
        return object
    
    def get_poll_func(self):
        """"""
        return object
    
    def invoke(self, function=None, data=None):
        """"""
        return object
    
    def invoke_full(self, priority=None, function=None, data=None, notify=None):
        """"""
        return object
    
    def is_owner(self):
        """"""
        return object
    
    def iteration(self, may_block=None):
        """"""
        return object
    
    def pending(self):
        """"""
        return object
    
    def pop_thread_default(self):
        """"""
        return object
    
    def prepare(self, priority=None):
        """"""
        return object
    
    def push_thread_default(self):
        """"""
        return object
    
    def query(self, max_priority=None, timeout_=None, fds=None, n_fds=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def release(self):
        """"""
        return object
    
    def remove_poll(self, fd=None):
        """"""
        return object
    
    def set_poll_func(self, func=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    
    def wait(self, cond=None, mutex=None):
        """"""
        return object
    
    def wakeup(self):
        """"""
        return object
    @staticmethod
    def default():
        """"""
        return object
    @staticmethod
    def get_thread_default():
        """"""
        return object
    @staticmethod
    def ref_thread_default():
        """"""
        return object


class MainLoop():
    """"""
    
    def __init__(self, context=None, is_running=None):
        """"""
        return object
    @staticmethod
    def new(context=None, is_running=None):
        """"""
        return object
    
    def get_context(self):
        """"""
        return object
    
    def is_running(self):
        """"""
        return object
    
    def quit(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def run(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class MappedFile():
    """"""
    
    def __init__(self, filename=None, writable=None):
        """"""
        return object
    @staticmethod
    def new(filename=None, writable=None):
        """"""
        return object
    @staticmethod
    def new_from_fd(fd=None, writable=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_bytes(self):
        """"""
        return object
    
    def get_contents(self):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class MarkupParseContext():
    """"""
    
    def __init__(self, parser=None, flags=None, user_data=None, user_data_dnotify=None):
        """"""
        return object
    @staticmethod
    def new(parser=None, flags=None, user_data=None, user_data_dnotify=None):
        """"""
        return object
    
    def end_parse(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_element(self):
        """"""
        return object
    
    def get_element_stack(self):
        """"""
        return object
    
    def get_position(self, line_number=None, char_number=None):
        """"""
        return object
    
    def get_user_data(self):
        """"""
        return object
    
    def parse(self, text=None, text_len=None):
        """"""
        return object
    
    def pop(self):
        """"""
        return object
    
    def push(self, parser=None, user_data=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class MarkupParser():
    """"""

    @property
    def start_element(self):
        return object

    @property
    def end_element(self):
        return object

    @property
    def text(self):
        return object

    @property
    def passthrough(self):
        return object

    @property
    def error(self):
        return object


class MatchInfo():
    """"""
    
    def expand_references(self, string_to_expand=None):
        """"""
        return object
    
    def fetch(self, match_num=None):
        """"""
        return object
    
    def fetch_all(self):
        """"""
        return object
    
    def fetch_named(self, name=None):
        """"""
        return object
    
    def fetch_named_pos(self, name=None, start_pos=None, end_pos=None):
        """"""
        return object
    
    def fetch_pos(self, match_num=None, start_pos=None, end_pos=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_match_count(self):
        """"""
        return object
    
    def get_regex(self):
        """"""
        return object
    
    def get_string(self):
        """"""
        return object
    
    def is_partial_match(self):
        """"""
        return object
    
    def matches(self):
        """"""
        return object
    
    def next(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class MemVTable():
    """"""

    @property
    def malloc(self):
        return object

    @property
    def realloc(self):
        return object

    @property
    def free(self):
        return object

    @property
    def calloc(self):
        return object

    @property
    def try_malloc(self):
        return object

    @property
    def try_realloc(self):
        return object


class Node():
    """"""
    
    def child_index(self, data=None):
        """"""
        return object
    
    def child_position(self, child=None):
        """"""
        return object
    
    def children_foreach(self, flags=None, func=None, data=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def copy_deep(self, copy_func=None, data=None):
        """"""
        return object
    
    def depth(self):
        """"""
        return object
    
    def destroy(self):
        """"""
        return object
    
    def find(self, order=None, flags=None, data=None):
        """"""
        return object
    
    def find_child(self, flags=None, data=None):
        """"""
        return object
    
    def first_sibling(self):
        """"""
        return object
    
    def get_root(self):
        """"""
        return object
    
    def insert(self, position=None, node=None):
        """"""
        return object
    
    def insert_after(self, sibling=None, node=None):
        """"""
        return object
    
    def insert_before(self, sibling=None, node=None):
        """"""
        return object
    
    def is_ancestor(self, descendant=None):
        """"""
        return object
    
    def last_child(self):
        """"""
        return object
    
    def last_sibling(self):
        """"""
        return object
    
    def max_height(self):
        """"""
        return object
    
    def n_children(self):
        """"""
        return object
    
    def n_nodes(self, flags=None):
        """"""
        return object
    
    def nth_child(self, n=None):
        """"""
        return object
    
    def prepend(self, node=None):
        """"""
        return object
    
    def reverse_children(self):
        """"""
        return object
    
    def traverse(self, order=None, flags=None, max_depth=None, func=None, data=None):
        """"""
        return object
    
    def unlink(self):
        """"""
        return object
    @staticmethod
    def new(data=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def next(self):
        return object

    @property
    def prev(self):
        return object

    @property
    def parent(self):
        return object

    @property
    def children(self):
        return object


class Once():
    """"""
    
    def impl(self, func=None, arg=None):
        """"""
        return object
    @staticmethod
    def init_enter(location=None):
        """"""
        return object
    @staticmethod
    def init_leave(location=None, result=None):
        """"""
        return object

    @property
    def status(self):
        return object

    @property
    def retval(self):
        return object


class OptionContext():
    """"""
    
    def add_group(self, group=None):
        """"""
        return object
    
    def add_main_entries(self, entries=None, translation_domain=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_help(self, main_help=None, group=None):
        """"""
        return object
    
    def get_help_enabled(self):
        """"""
        return object
    
    def get_ignore_unknown_options(self):
        """"""
        return object
    
    def get_main_group(self):
        """"""
        return object
    
    def get_strict_posix(self):
        """"""
        return object
    
    def get_summary(self):
        """"""
        return object
    
    def parse(self, argc=None, argv=None):
        """"""
        return object
    
    def parse_strv(self, arguments=None):
        """"""
        return object
    
    def set_description(self, description=None):
        """"""
        return object
    
    def set_help_enabled(self, help_enabled=None):
        """"""
        return object
    
    def set_ignore_unknown_options(self, ignore_unknown=None):
        """"""
        return object
    
    def set_main_group(self, group=None):
        """"""
        return object
    
    def set_strict_posix(self, strict_posix=None):
        """"""
        return object
    
    def set_summary(self, summary=None):
        """"""
        return object
    
    def set_translate_func(self, func=None, data=None, destroy_notify=None):
        """"""
        return object
    
    def set_translation_domain(self, domain=None):
        """"""
        return object
    @staticmethod
    def new(parameter_string=None):
        """"""
        return object


class OptionEntry():
    """"""

    @property
    def long_name(self):
        return object

    @property
    def short_name(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def arg(self):
        return object

    @property
    def arg_data(self):
        return object

    @property
    def description(self):
        return object

    @property
    def arg_description(self):
        return object


class OptionGroup():
    """"""
    
    def __init__(self, name=None, description=None, help_description=None, user_data=None, destroy=None):
        """"""
        return object
    @staticmethod
    def new(name=None, description=None, help_description=None, user_data=None, destroy=None):
        """"""
        return object
    
    def add_entries(self, entries=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def set_error_hook(self, error_func=None):
        """"""
        return object
    
    def set_parse_hooks(self, pre_parse_func=None, post_parse_func=None):
        """"""
        return object
    
    def set_translate_func(self, func=None, data=None, destroy_notify=None):
        """"""
        return object
    
    def set_translation_domain(self, domain=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class PatternSpec():
    """"""
    
    def equal(self, pspec2=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    @staticmethod
    def new(pattern=None):
        """"""
        return object


class PollFD():
    """"""

    @property
    def fd(self):
        return object

    @property
    def events(self):
        return object

    @property
    def revents(self):
        return object


class Private():
    """"""
    
    def get(self):
        """"""
        return object
    
    def replace(self, value=None):
        """"""
        return object
    
    def set(self, value=None):
        """"""
        return object

    @property
    def p(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def future(self):
        return object


class PtrArray():
    """"""
    @staticmethod
    def add(array=None, data=None):
        """"""
        return object
    @staticmethod
    def find(haystack=None, needle=None, index_=None):
        """"""
        return object
    @staticmethod
    def find_with_equal_func(haystack=None, needle=None, equal_func=None, index_=None):
        """"""
        return object
    @staticmethod
    def foreach(array=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def free(array=None, free_seg=None):
        """"""
        return object
    @staticmethod
    def insert(array=None, index_=None, data=None):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_full(reserved_size=None, element_free_func=None):
        """"""
        return object
    @staticmethod
    def new_with_free_func(element_free_func=None):
        """"""
        return object
    @staticmethod
    def ref(array=None):
        """"""
        return object
    @staticmethod
    def remove(array=None, data=None):
        """"""
        return object
    @staticmethod
    def remove_fast(array=None, data=None):
        """"""
        return object
    @staticmethod
    def remove_index(array=None, index_=None):
        """"""
        return object
    @staticmethod
    def remove_index_fast(array=None, index_=None):
        """"""
        return object
    @staticmethod
    def remove_range(array=None, index_=None, length=None):
        """"""
        return object
    @staticmethod
    def set_free_func(array=None, element_free_func=None):
        """"""
        return object
    @staticmethod
    def set_size(array=None, length=None):
        """"""
        return object
    @staticmethod
    def sized_new(reserved_size=None):
        """"""
        return object
    @staticmethod
    def sort(array=None, compare_func=None):
        """"""
        return object
    @staticmethod
    def sort_with_data(array=None, compare_func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def unref(array=None):
        """"""
        return object

    @property
    def pdata(self):
        return object

    @property
    def len(self):
        return object


class Queue():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def delete_link(self, link_=None):
        """"""
        return object
    
    def find(self, data=None):
        """"""
        return object
    
    def find_custom(self, data=None, func=None):
        """"""
        return object
    
    def foreach(self, func=None, user_data=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def free_full(self, free_func=None):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def index(self, data=None):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def insert_after(self, sibling=None, data=None):
        """"""
        return object
    
    def insert_before(self, sibling=None, data=None):
        """"""
        return object
    
    def insert_sorted(self, data=None, func=None, user_data=None):
        """"""
        return object
    
    def is_empty(self):
        """"""
        return object
    
    def link_index(self, link_=None):
        """"""
        return object
    
    def peek_head(self):
        """"""
        return object
    
    def peek_head_link(self):
        """"""
        return object
    
    def peek_nth(self, n=None):
        """"""
        return object
    
    def peek_nth_link(self, n=None):
        """"""
        return object
    
    def peek_tail(self):
        """"""
        return object
    
    def peek_tail_link(self):
        """"""
        return object
    
    def pop_head(self):
        """"""
        return object
    
    def pop_head_link(self):
        """"""
        return object
    
    def pop_nth(self, n=None):
        """"""
        return object
    
    def pop_nth_link(self, n=None):
        """"""
        return object
    
    def pop_tail(self):
        """"""
        return object
    
    def pop_tail_link(self):
        """"""
        return object
    
    def push_head(self, data=None):
        """"""
        return object
    
    def push_head_link(self, link_=None):
        """"""
        return object
    
    def push_nth(self, data=None, n=None):
        """"""
        return object
    
    def push_nth_link(self, n=None, link_=None):
        """"""
        return object
    
    def push_tail(self, data=None):
        """"""
        return object
    
    def push_tail_link(self, link_=None):
        """"""
        return object
    
    def remove(self, data=None):
        """"""
        return object
    
    def remove_all(self, data=None):
        """"""
        return object
    
    def reverse(self):
        """"""
        return object
    
    def sort(self, compare_func=None, user_data=None):
        """"""
        return object
    
    def unlink(self, link_=None):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def head(self):
        return object

    @property
    def tail(self):
        return object

    @property
    def length(self):
        return object


class RWLock():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def reader_lock(self):
        """"""
        return object
    
    def reader_trylock(self):
        """"""
        return object
    
    def reader_unlock(self):
        """"""
        return object
    
    def writer_lock(self):
        """"""
        return object
    
    def writer_trylock(self):
        """"""
        return object
    
    def writer_unlock(self):
        """"""
        return object

    @property
    def p(self):
        return object

    @property
    def i(self):
        return object


class Rand():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def double(self):
        """"""
        return object
    
    def double_range(self, begin=None, end=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def int(self):
        """"""
        return object
    
    def int_range(self, begin=None, end=None):
        """"""
        return object
    
    def set_seed(self, seed=None):
        """"""
        return object
    
    def set_seed_array(self, seed=None, seed_length=None):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_with_seed(seed=None):
        """"""
        return object
    @staticmethod
    def new_with_seed_array(seed=None, seed_length=None):
        """"""
        return object


class RecMutex():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def lock(self):
        """"""
        return object
    
    def trylock(self):
        """"""
        return object
    
    def unlock(self):
        """"""
        return object

    @property
    def p(self):
        return object

    @property
    def i(self):
        return object


class Regex():
    """"""
    
    def __init__(self, pattern=None, compile_options=None, match_options=None):
        """"""
        return object
    @staticmethod
    def new(pattern=None, compile_options=None, match_options=None):
        """"""
        return object
    
    def get_capture_count(self):
        """"""
        return object
    
    def get_compile_flags(self):
        """"""
        return object
    
    def get_has_cr_or_lf(self):
        """"""
        return object
    
    def get_match_flags(self):
        """"""
        return object
    
    def get_max_backref(self):
        """"""
        return object
    
    def get_max_lookbehind(self):
        """"""
        return object
    
    def get_pattern(self):
        """"""
        return object
    
    def get_string_number(self, name=None):
        """"""
        return object
    
    def match(self, string=None, match_options=None, match_info=None):
        """"""
        return object
    
    def match_all(self, string=None, match_options=None, match_info=None):
        """"""
        return object
    
    def match_all_full(self, string=None, string_len=None, start_position=None, match_options=None, match_info=None):
        """"""
        return object
    
    def match_full(self, string=None, string_len=None, start_position=None, match_options=None, match_info=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def replace(self, string=None, string_len=None, start_position=None, replacement=None, match_options=None):
        """"""
        return object
    
    def replace_eval(self, string=None, string_len=None, start_position=None, match_options=None, eval=None, user_data=None):
        """"""
        return object
    
    def replace_literal(self, string=None, string_len=None, start_position=None, replacement=None, match_options=None):
        """"""
        return object
    
    def split(self, string=None, match_options=None):
        """"""
        return object
    
    def split_full(self, string=None, string_len=None, start_position=None, match_options=None, max_tokens=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def check_replacement(replacement=None, has_references=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    @staticmethod
    def escape_nul(string=None, length=None):
        """"""
        return object
    @staticmethod
    def escape_string(string=None, length=None):
        """"""
        return object
    @staticmethod
    def match_simple(pattern=None, string=None, compile_options=None, match_options=None):
        """"""
        return object
    @staticmethod
    def split_simple(pattern=None, string=None, compile_options=None, match_options=None):
        """"""
        return object


class SList():
    """"""
    @staticmethod
    def alloc():
        """"""
        return object
    @staticmethod
    def append(list=None, data=None):
        """"""
        return object
    @staticmethod
    def concat(list1=None, list2=None):
        """"""
        return object
    @staticmethod
    def copy(list=None):
        """"""
        return object
    @staticmethod
    def copy_deep(list=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def delete_link(list=None, link_=None):
        """"""
        return object
    @staticmethod
    def find(list=None, data=None):
        """"""
        return object
    @staticmethod
    def find_custom(list=None, data=None, func=None):
        """"""
        return object
    @staticmethod
    def foreach(list=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def free(list=None):
        """"""
        return object
    @staticmethod
    def free_1(list=None):
        """"""
        return object
    @staticmethod
    def free_full(list=None, free_func=None):
        """"""
        return object
    @staticmethod
    def index(list=None, data=None):
        """"""
        return object
    @staticmethod
    def insert(list=None, data=None, position=None):
        """"""
        return object
    @staticmethod
    def insert_before(slist=None, sibling=None, data=None):
        """"""
        return object
    @staticmethod
    def insert_sorted(list=None, data=None, func=None):
        """"""
        return object
    @staticmethod
    def insert_sorted_with_data(list=None, data=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def last(list=None):
        """"""
        return object
    @staticmethod
    def length(list=None):
        """"""
        return object
    @staticmethod
    def nth(list=None, n=None):
        """"""
        return object
    @staticmethod
    def nth_data(list=None, n=None):
        """"""
        return object
    @staticmethod
    def position(list=None, llink=None):
        """"""
        return object
    @staticmethod
    def prepend(list=None, data=None):
        """"""
        return object
    @staticmethod
    def remove(list=None, data=None):
        """"""
        return object
    @staticmethod
    def remove_all(list=None, data=None):
        """"""
        return object
    @staticmethod
    def remove_link(list=None, link_=None):
        """"""
        return object
    @staticmethod
    def reverse(list=None):
        """"""
        return object
    @staticmethod
    def sort(list=None, compare_func=None):
        """"""
        return object
    @staticmethod
    def sort_with_data(list=None, compare_func=None, user_data=None):
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def next(self):
        return object


class Scanner():
    """"""
    
    def cur_line(self):
        """"""
        return object
    
    def cur_position(self):
        """"""
        return object
    
    def cur_token(self):
        """"""
        return object
    
    def cur_value(self):
        """"""
        return object
    
    def destroy(self):
        """"""
        return object
    
    def eof(self):
        """"""
        return object
    
    def error(self, format=None, *args):
        """"""
        return object
    
    def get_next_token(self):
        """"""
        return object
    
    def input_file(self, input_fd=None):
        """"""
        return object
    
    def input_text(self, text=None, text_len=None):
        """"""
        return object
    
    def lookup_symbol(self, symbol=None):
        """"""
        return object
    
    def peek_next_token(self):
        """"""
        return object
    
    def scope_add_symbol(self, scope_id=None, symbol=None, value=None):
        """"""
        return object
    
    def scope_foreach_symbol(self, scope_id=None, func=None, user_data=None):
        """"""
        return object
    
    def scope_lookup_symbol(self, scope_id=None, symbol=None):
        """"""
        return object
    
    def scope_remove_symbol(self, scope_id=None, symbol=None):
        """"""
        return object
    
    def set_scope(self, scope_id=None):
        """"""
        return object
    
    def sync_file_offset(self):
        """"""
        return object
    
    def unexp_token(self, expected_token=None, identifier_spec=None, symbol_spec=None, symbol_name=None, message=None, is_error=None):
        """"""
        return object
    
    def warn(self, format=None, *args):
        """"""
        return object
    @staticmethod
    def new(config_templ=None):
        """"""
        return object

    @property
    def user_data(self):
        return object

    @property
    def max_parse_errors(self):
        return object

    @property
    def parse_errors(self):
        return object

    @property
    def input_name(self):
        return object

    @property
    def qdata(self):
        return object

    @property
    def config(self):
        return object

    @property
    def token(self):
        return object

    @property
    def value(self):
        return object

    @property
    def line(self):
        return object

    @property
    def position(self):
        return object

    @property
    def next_token(self):
        return object

    @property
    def next_value(self):
        return object

    @property
    def next_line(self):
        return object

    @property
    def next_position(self):
        return object

    @property
    def symbol_table(self):
        return object

    @property
    def input_fd(self):
        return object

    @property
    def text(self):
        return object

    @property
    def text_end(self):
        return object

    @property
    def buffer(self):
        return object

    @property
    def scope_id(self):
        return object

    @property
    def msg_handler(self):
        return object


class ScannerConfig():
    """"""

    @property
    def cset_skip_characters(self):
        return object

    @property
    def cset_identifier_first(self):
        return object

    @property
    def cset_identifier_nth(self):
        return object

    @property
    def cpair_comment_single(self):
        return object

    @property
    def case_sensitive(self):
        return object

    @property
    def skip_comment_multi(self):
        return object

    @property
    def skip_comment_single(self):
        return object

    @property
    def scan_comment_multi(self):
        return object

    @property
    def scan_identifier(self):
        return object

    @property
    def scan_identifier_1char(self):
        return object

    @property
    def scan_identifier_NULL(self):
        return object

    @property
    def scan_symbols(self):
        return object

    @property
    def scan_binary(self):
        return object

    @property
    def scan_octal(self):
        return object

    @property
    def scan_float(self):
        return object

    @property
    def scan_hex(self):
        return object

    @property
    def scan_hex_dollar(self):
        return object

    @property
    def scan_string_sq(self):
        return object

    @property
    def scan_string_dq(self):
        return object

    @property
    def numbers_2_int(self):
        return object

    @property
    def int_2_float(self):
        return object

    @property
    def identifier_2_string(self):
        return object

    @property
    def char_2_token(self):
        return object

    @property
    def symbol_2_token(self):
        return object

    @property
    def scope_0_fallback(self):
        return object

    @property
    def store_int64(self):
        return object

    @property
    def padding_dummy(self):
        return object


class Sequence():
    """"""
    
    def append(self, data=None):
        """"""
        return object
    
    def foreach(self, func=None, user_data=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_begin_iter(self):
        """"""
        return object
    
    def get_end_iter(self):
        """"""
        return object
    
    def get_iter_at_pos(self, pos=None):
        """"""
        return object
    
    def get_length(self):
        """"""
        return object
    
    def insert_sorted(self, data=None, cmp_func=None, cmp_data=None):
        """"""
        return object
    
    def insert_sorted_iter(self, data=None, iter_cmp=None, cmp_data=None):
        """"""
        return object
    
    def is_empty(self):
        """"""
        return object
    
    def lookup(self, data=None, cmp_func=None, cmp_data=None):
        """"""
        return object
    
    def lookup_iter(self, data=None, iter_cmp=None, cmp_data=None):
        """"""
        return object
    
    def prepend(self, data=None):
        """"""
        return object
    
    def search(self, data=None, cmp_func=None, cmp_data=None):
        """"""
        return object
    
    def search_iter(self, data=None, iter_cmp=None, cmp_data=None):
        """"""
        return object
    
    def sort(self, cmp_func=None, cmp_data=None):
        """"""
        return object
    
    def sort_iter(self, cmp_func=None, cmp_data=None):
        """"""
        return object
    @staticmethod
    def foreach_range(begin=None, end=None, func=None, user_data=None):
        """"""
        return object
    @staticmethod
    def get(iter=None):
        """"""
        return object
    @staticmethod
    def insert_before(iter=None, data=None):
        """"""
        return object
    @staticmethod
    def move(src=None, dest=None):
        """"""
        return object
    @staticmethod
    def move_range(dest=None, begin=None, end=None):
        """"""
        return object
    @staticmethod
    def new(data_destroy=None):
        """"""
        return object
    @staticmethod
    def range_get_midpoint(begin=None, end=None):
        """"""
        return object
    @staticmethod
    def remove(iter=None):
        """"""
        return object
    @staticmethod
    def remove_range(begin=None, end=None):
        """"""
        return object
    @staticmethod
    def set(iter=None, data=None):
        """"""
        return object
    @staticmethod
    def sort_changed(iter=None, cmp_func=None, cmp_data=None):
        """"""
        return object
    @staticmethod
    def sort_changed_iter(iter=None, iter_cmp=None, cmp_data=None):
        """"""
        return object
    @staticmethod
    def swap(a=None, b=None):
        """"""
        return object


class SequenceIter():
    """"""
    
    def compare(self, b=None):
        """"""
        return object
    
    def get_position(self):
        """"""
        return object
    
    def get_sequence(self):
        """"""
        return object
    
    def is_begin(self):
        """"""
        return object
    
    def is_end(self):
        """"""
        return object
    
    def move(self, delta=None):
        """"""
        return object
    
    def next(self):
        """"""
        return object
    
    def prev(self):
        """"""
        return object


class Source():
    """"""
    
    def __init__(self, source_funcs=None, struct_size=None):
        """"""
        return object
    @staticmethod
    def new(source_funcs=None, struct_size=None):
        """"""
        return object
    
    def add_child_source(self, child_source=None):
        """"""
        return object
    
    def add_poll(self, fd=None):
        """"""
        return object
    
    def add_unix_fd(self, fd=None, events=None):
        """"""
        return object
    
    def attach(self, context=None):
        """"""
        return object
    
    def destroy(self):
        """"""
        return object
    
    def get_can_recurse(self):
        """"""
        return object
    
    def get_context(self):
        """"""
        return object
    
    def get_current_time(self, timeval=None):
        """"""
        return object
    
    def get_id(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_priority(self):
        """"""
        return object
    
    def get_ready_time(self):
        """"""
        return object
    
    def get_time(self):
        """"""
        return object
    
    def is_destroyed(self):
        """"""
        return object
    
    def modify_unix_fd(self, tag=None, new_events=None):
        """"""
        return object
    
    def query_unix_fd(self, tag=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def remove_child_source(self, child_source=None):
        """"""
        return object
    
    def remove_poll(self, fd=None):
        """"""
        return object
    
    def remove_unix_fd(self, tag=None):
        """"""
        return object
    
    def set_callback(self, func=None, data=None, notify=None):
        """"""
        return object
    
    def set_callback_indirect(self, callback_data=None, callback_funcs=None):
        """"""
        return object
    
    def set_can_recurse(self, can_recurse=None):
        """"""
        return object
    
    def set_funcs(self, funcs=None):
        """"""
        return object
    
    def set_name(self, name=None):
        """"""
        return object
    
    def set_priority(self, priority=None):
        """"""
        return object
    
    def set_ready_time(self, ready_time=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def remove(tag=None):
        """"""
        return object
    @staticmethod
    def remove_by_funcs_user_data(funcs=None, user_data=None):
        """"""
        return object
    @staticmethod
    def remove_by_user_data(user_data=None):
        """"""
        return object
    @staticmethod
    def set_name_by_id(tag=None, name=None):
        """"""
        return object

    @property
    def callback_data(self):
        return object

    @property
    def callback_funcs(self):
        return object

    @property
    def source_funcs(self):
        return object

    @property
    def ref_count(self):
        return object

    @property
    def context(self):
        return object

    @property
    def priority(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def source_id(self):
        return object

    @property
    def poll_fds(self):
        return object

    @property
    def prev(self):
        return object

    @property
    def next(self):
        return object

    @property
    def name(self):
        return object

    @property
    def priv(self):
        return object


class SourceCallbackFuncs():
    """"""

    @property
    def ref(self):
        return object

    @property
    def unref(self):
        return object

    @property
    def get(self):
        return object


class SourceFuncs():
    """"""

    @property
    def prepare(self):
        return object

    @property
    def check(self):
        return object

    @property
    def dispatch(self):
        return object

    @property
    def finalize(self):
        return object

    @property
    def closure_callback(self):
        return object

    @property
    def closure_marshal(self):
        return object


class SourcePrivate():
    """"""


class StatBuf():
    """"""


class String():
    """"""
    
    def append(self, val=None):
        """"""
        return object
    
    def append_c(self, c=None):
        """"""
        return object
    
    def append_len(self, val=None, len=None):
        """"""
        return object
    
    def append_printf(self, format=None, *args):
        """"""
        return object
    
    def append_unichar(self, wc=None):
        """"""
        return object
    
    def append_uri_escaped(self, unescaped=None, reserved_chars_allowed=None, allow_utf8=None):
        """"""
        return object
    
    def append_vprintf(self, format=None, args=None):
        """"""
        return object
    
    def ascii_down(self):
        """"""
        return object
    
    def ascii_up(self):
        """"""
        return object
    
    def assign(self, rval=None):
        """"""
        return object
    
    def down(self):
        """"""
        return object
    
    def equal(self, v2=None):
        """"""
        return object
    
    def erase(self, pos=None, len=None):
        """"""
        return object
    
    def free(self, free_segment=None):
        """"""
        return object
    
    def free_to_bytes(self):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def insert(self, pos=None, val=None):
        """"""
        return object
    
    def insert_c(self, pos=None, c=None):
        """"""
        return object
    
    def insert_len(self, pos=None, val=None, len=None):
        """"""
        return object
    
    def insert_unichar(self, pos=None, wc=None):
        """"""
        return object
    
    def overwrite(self, pos=None, val=None):
        """"""
        return object
    
    def overwrite_len(self, pos=None, val=None, len=None):
        """"""
        return object
    
    def prepend(self, val=None):
        """"""
        return object
    
    def prepend_c(self, c=None):
        """"""
        return object
    
    def prepend_len(self, val=None, len=None):
        """"""
        return object
    
    def prepend_unichar(self, wc=None):
        """"""
        return object
    
    def printf(self, format=None, *args):
        """"""
        return object
    
    def set_size(self, len=None):
        """"""
        return object
    
    def truncate(self, len=None):
        """"""
        return object
    
    def up(self):
        """"""
        return object
    
    def vprintf(self, format=None, args=None):
        """"""
        return object

    @property
    def str(self):
        return object

    @property
    def len(self):
        return object

    @property
    def allocated_len(self):
        return object


class StringChunk():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def insert(self, string=None):
        """"""
        return object
    
    def insert_const(self, string=None):
        """"""
        return object
    
    def insert_len(self, string=None, len=None):
        """"""
        return object
    @staticmethod
    def new(size=None):
        """"""
        return object


class TestCase():
    """"""


class TestConfig():
    """"""

    @property
    def test_initialized(self):
        return object

    @property
    def test_quick(self):
        return object

    @property
    def test_perf(self):
        return object

    @property
    def test_verbose(self):
        return object

    @property
    def test_quiet(self):
        return object

    @property
    def test_undefined(self):
        return object


class TestLogBuffer():
    """"""
    
    def free(self):
        """"""
        return object
    
    def pop(self):
        """"""
        return object
    
    def push(self, n_bytes=None, bytes=None):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def data(self):
        return object

    @property
    def msgs(self):
        return object


class TestLogMsg():
    """"""
    
    def free(self):
        """"""
        return object

    @property
    def log_type(self):
        return object

    @property
    def n_strings(self):
        return object

    @property
    def strings(self):
        return object

    @property
    def n_nums(self):
        return object

    @property
    def nums(self):
        return object


class TestSuite():
    """"""
    
    def add(self, test_case=None):
        """"""
        return object
    
    def add_suite(self, nestedsuite=None):
        """"""
        return object


class Thread():
    """"""
    
    def __init__(self, name=None, func=None, data=None):
        """"""
        return object
    @staticmethod
    def new(name=None, func=None, data=None):
        """"""
        return object
    @staticmethod
    def try_new(name=None, func=None, data=None):
        """"""
        return object
    
    def join(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    @staticmethod
    def exit(retval=None):
        """"""
        return object
    @staticmethod
    def self():
        """"""
        return object
    @staticmethod
    def _yield():
        """"""
        return object


class ThreadPool():
    """"""
    
    def free(self, immediate=None, wait_=None):
        """"""
        return object
    
    def get_max_threads(self):
        """"""
        return object
    
    def get_num_threads(self):
        """"""
        return object
    
    def move_to_front(self, data=None):
        """"""
        return object
    
    def push(self, data=None):
        """"""
        return object
    
    def set_max_threads(self, max_threads=None):
        """"""
        return object
    
    def set_sort_function(self, func=None, user_data=None):
        """"""
        return object
    
    def unprocessed(self):
        """"""
        return object
    @staticmethod
    def get_max_idle_time():
        """"""
        return object
    @staticmethod
    def get_max_unused_threads():
        """"""
        return object
    @staticmethod
    def get_num_unused_threads():
        """"""
        return object
    @staticmethod
    def new(func=None, user_data=None, max_threads=None, exclusive=None):
        """"""
        return object
    @staticmethod
    def set_max_idle_time(interval=None):
        """"""
        return object
    @staticmethod
    def set_max_unused_threads(max_threads=None):
        """"""
        return object
    @staticmethod
    def stop_unused_threads():
        """"""
        return object

    @property
    def func(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def exclusive(self):
        return object


class TimeVal():
    """"""
    
    def add(self, microseconds=None):
        """"""
        return object
    
    def to_iso8601(self):
        """"""
        return object
    @staticmethod
    def from_iso8601(iso_date=None, time_=None):
        """"""
        return object

    @property
    def tv_sec(self):
        return object

    @property
    def tv_usec(self):
        return object


class TimeZone():
    """"""
    
    def __init__(self, identifier=None):
        """"""
        return object
    @staticmethod
    def new(identifier=None):
        """"""
        return object
    @staticmethod
    def new_local():
        """"""
        return object
    @staticmethod
    def new_utc():
        """"""
        return object
    
    def adjust_time(self, type=None, time_=None):
        """"""
        return object
    
    def find_interval(self, type=None, time_=None):
        """"""
        return object
    
    def get_abbreviation(self, interval=None):
        """"""
        return object
    
    def get_offset(self, interval=None):
        """"""
        return object
    
    def is_dst(self, interval=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class Timer():
    """"""
    
    def _continue(self):
        """"""
        return object
    
    def destroy(self):
        """"""
        return object
    
    def elapsed(self, microseconds=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object


class TrashStack():
    """"""
    @staticmethod
    def height(stack_p=None):
        """"""
        return object
    @staticmethod
    def peek(stack_p=None):
        """"""
        return object
    @staticmethod
    def pop(stack_p=None):
        """"""
        return object
    @staticmethod
    def push(stack_p=None, data_p=None):
        """"""
        return object

    @property
    def next(self):
        return object


class Tree():
    """"""
    
    def destroy(self):
        """"""
        return object
    
    def foreach(self, func=None, user_data=None):
        """"""
        return object
    
    def height(self):
        """"""
        return object
    
    def insert(self, key=None, value=None):
        """"""
        return object
    
    def lookup(self, key=None):
        """"""
        return object
    
    def lookup_extended(self, lookup_key=None, orig_key=None, value=None):
        """"""
        return object
    
    def nnodes(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def remove(self, key=None):
        """"""
        return object
    
    def replace(self, key=None, value=None):
        """"""
        return object
    
    def search(self, search_func=None, user_data=None):
        """"""
        return object
    
    def steal(self, key=None):
        """"""
        return object
    
    def traverse(self, traverse_func=None, traverse_type=None, user_data=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def new(key_compare_func=None):
        """"""
        return object
    @staticmethod
    def new_full(key_compare_func=None, key_compare_data=None, key_destroy_func=None, value_destroy_func=None):
        """"""
        return object
    @staticmethod
    def new_with_data(key_compare_func=None, key_compare_data=None):
        """"""
        return object


class Variant():
    """"""
    
    def __init__(self, format_string=None, *args):
        """"""
        return object
    @staticmethod
    def new(format_string=None, *args):
        """"""
        return object
    @staticmethod
    def new_array(child_type=None, children=None, n_children=None):
        """"""
        return object
    @staticmethod
    def new_boolean(value=None):
        """"""
        return object
    @staticmethod
    def new_byte(value=None):
        """"""
        return object
    @staticmethod
    def new_bytestring(string=None):
        """"""
        return object
    @staticmethod
    def new_bytestring_array(strv=None, length=None):
        """"""
        return object
    @staticmethod
    def new_dict_entry(key=None, value=None):
        """"""
        return object
    @staticmethod
    def new_double(value=None):
        """"""
        return object
    @staticmethod
    def new_fixed_array(element_type=None, elements=None, n_elements=None, element_size=None):
        """"""
        return object
    @staticmethod
    def new_from_bytes(type=None, bytes=None, trusted=None):
        """"""
        return object
    @staticmethod
    def new_from_data(type=None, data=None, size=None, trusted=None, notify=None, user_data=None):
        """"""
        return object
    @staticmethod
    def new_handle(value=None):
        """"""
        return object
    @staticmethod
    def new_int16(value=None):
        """"""
        return object
    @staticmethod
    def new_int32(value=None):
        """"""
        return object
    @staticmethod
    def new_int64(value=None):
        """"""
        return object
    @staticmethod
    def new_maybe(child_type=None, child=None):
        """"""
        return object
    @staticmethod
    def new_object_path(object_path=None):
        """"""
        return object
    @staticmethod
    def new_objv(strv=None, length=None):
        """"""
        return object
    @staticmethod
    def new_parsed(format=None, *args):
        """"""
        return object
    @staticmethod
    def new_parsed_va(format=None, app=None):
        """"""
        return object
    @staticmethod
    def new_printf(format_string=None, *args):
        """"""
        return object
    @staticmethod
    def new_signature(signature=None):
        """"""
        return object
    @staticmethod
    def new_string(string=None):
        """"""
        return object
    @staticmethod
    def new_strv(strv=None, length=None):
        """"""
        return object
    @staticmethod
    def new_take_string(string=None):
        """"""
        return object
    @staticmethod
    def new_tuple(children=None, n_children=None):
        """"""
        return object
    @staticmethod
    def new_uint16(value=None):
        """"""
        return object
    @staticmethod
    def new_uint32(value=None):
        """"""
        return object
    @staticmethod
    def new_uint64(value=None):
        """"""
        return object
    @staticmethod
    def new_va(format_string=None, endptr=None, app=None):
        """"""
        return object
    @staticmethod
    def new_variant(value=None):
        """"""
        return object
    
    def byteswap(self):
        """"""
        return object
    
    def check_format_string(self, format_string=None, copy_only=None):
        """"""
        return object
    
    def classify(self):
        """"""
        return object
    
    def compare(self, two=None):
        """"""
        return object
    
    def dup_bytestring(self, length=None):
        """"""
        return object
    
    def dup_bytestring_array(self, length=None):
        """"""
        return object
    
    def dup_objv(self, length=None):
        """"""
        return object
    
    def dup_string(self, length=None):
        """"""
        return object
    
    def dup_strv(self, length=None):
        """"""
        return object
    
    def equal(self, two=None):
        """"""
        return object
    
    def get(self, format_string=None, *args):
        """"""
        return object
    
    def get_boolean(self):
        """"""
        return object
    
    def get_byte(self):
        """"""
        return object
    
    def get_bytestring(self):
        """"""
        return object
    
    def get_bytestring_array(self, length=None):
        """"""
        return object
    
    def get_child(self, index_=None, format_string=None, *args):
        """"""
        return object
    
    def get_child_value(self, index_=None):
        """"""
        return object
    
    def get_data(self):
        """"""
        return object
    
    def get_data_as_bytes(self):
        """"""
        return object
    
    def get_double(self):
        """"""
        return object
    
    def get_fixed_array(self, n_elements=None, element_size=None):
        """"""
        return object
    
    def get_handle(self):
        """"""
        return object
    
    def get_int16(self):
        """"""
        return object
    
    def get_int32(self):
        """"""
        return object
    
    def get_int64(self):
        """"""
        return object
    
    def get_maybe(self):
        """"""
        return object
    
    def get_normal_form(self):
        """"""
        return object
    
    def get_objv(self, length=None):
        """"""
        return object
    
    def get_size(self):
        """"""
        return object
    
    def get_string(self, length=None):
        """"""
        return object
    
    def get_strv(self, length=None):
        """"""
        return object
    
    def get_type(self):
        """"""
        return object
    
    def get_type_string(self):
        """"""
        return object
    
    def get_uint16(self):
        """"""
        return object
    
    def get_uint32(self):
        """"""
        return object
    
    def get_uint64(self):
        """"""
        return object
    
    def get_va(self, format_string=None, endptr=None, app=None):
        """"""
        return object
    
    def get_variant(self):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def is_container(self):
        """"""
        return object
    
    def is_floating(self):
        """"""
        return object
    
    def is_normal_form(self):
        """"""
        return object
    
    def is_of_type(self, type=None):
        """"""
        return object
    
    def iter_new(self):
        """"""
        return object
    
    def lookup(self, key=None, format_string=None, *args):
        """"""
        return object
    
    def lookup_value(self, key=None, expected_type=None):
        """"""
        return object
    
    def n_children(self):
        """"""
        return object
    
    def print_(self, type_annotate=None):
        """"""
        return object
    
    def print_string(self, string=None, type_annotate=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def ref_sink(self):
        """"""
        return object
    
    def store(self, data=None):
        """"""
        return object
    
    def take_ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object
    @staticmethod
    def is_object_path(string=None):
        """"""
        return object
    @staticmethod
    def is_signature(string=None):
        """"""
        return object
    @staticmethod
    def parse(type=None, text=None, limit=None, endptr=None):
        """"""
        return object
    @staticmethod
    def parse_error_print_context(error=None, source_str=None):
        """"""
        return object
    @staticmethod
    def parse_error_quark():
        """"""
        return object
    @staticmethod
    def parser_get_error_quark():
        """"""
        return object


class VariantBuilder():
    """"""
    
    def __init__(self, type=None):
        """"""
        return object
    @staticmethod
    def new(type=None):
        """"""
        return object
    
    def add(self, format_string=None, *args):
        """"""
        return object
    
    def add_parsed(self, format=None, *args):
        """"""
        return object
    
    def add_value(self, value=None):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def close(self):
        """"""
        return object
    
    def end(self):
        """"""
        return object
    
    def init(self, type=None):
        """"""
        return object
    
    def open(self, type=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class VariantDict():
    """"""
    
    def __init__(self, from_asv=None):
        """"""
        return object
    @staticmethod
    def new(from_asv=None):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def contains(self, key=None):
        """"""
        return object
    
    def end(self):
        """"""
        return object
    
    def init(self, from_asv=None):
        """"""
        return object
    
    def insert(self, key=None, format_string=None, *args):
        """"""
        return object
    
    def insert_value(self, key=None, value=None):
        """"""
        return object
    
    def lookup(self, key=None, format_string=None, *args):
        """"""
        return object
    
    def lookup_value(self, key=None, expected_type=None):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def remove(self, key=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object


class VariantIter():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def init(self, value=None):
        """"""
        return object
    
    def loop(self, format_string=None, *args):
        """"""
        return object
    
    def n_children(self):
        """"""
        return object
    
    def next(self, format_string=None, *args):
        """"""
        return object
    
    def next_value(self):
        """"""
        return object

    @property
    def x(self):
        return object


class VariantType():
    """"""
    
    def __init__(self, type_string=None):
        """"""
        return object
    @staticmethod
    def new(type_string=None):
        """"""
        return object
    @staticmethod
    def new_array(element=None):
        """"""
        return object
    @staticmethod
    def new_dict_entry(key=None, value=None):
        """"""
        return object
    @staticmethod
    def new_maybe(element=None):
        """"""
        return object
    @staticmethod
    def new_tuple(items=None, length=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def dup_string(self):
        """"""
        return object
    
    def element(self):
        """"""
        return object
    
    def equal(self, type2=None):
        """"""
        return object
    
    def first(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_string_length(self):
        """"""
        return object
    
    def hash(self):
        """"""
        return object
    
    def is_array(self):
        """"""
        return object
    
    def is_basic(self):
        """"""
        return object
    
    def is_container(self):
        """"""
        return object
    
    def is_definite(self):
        """"""
        return object
    
    def is_dict_entry(self):
        """"""
        return object
    
    def is_maybe(self):
        """"""
        return object
    
    def is_subtype_of(self, supertype=None):
        """"""
        return object
    
    def is_tuple(self):
        """"""
        return object
    
    def is_variant(self):
        """"""
        return object
    
    def key(self):
        """"""
        return object
    
    def n_items(self):
        """"""
        return object
    
    def next(self):
        """"""
        return object
    
    def peek_string(self):
        """"""
        return object
    
    def value(self):
        """"""
        return object
    @staticmethod
    def checked_(arg0=None):
        """"""
        return object
    @staticmethod
    def string_is_valid(type_string=None):
        """"""
        return object
    @staticmethod
    def string_scan(string=None, limit=None, endptr=None):
        """"""
        return object
