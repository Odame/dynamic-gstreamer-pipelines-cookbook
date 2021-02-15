# -*- coding: utf-8 -*-


class ATSCDescriptorType:
    """"""
    STUFFING = 128
    AC3 = 131
    CAPTION_SERVICE = 134
    CONTENT_ADVISORY = 135
    EXTENDED_CHANNEL_NAME = 160
    SERVICE_LOCATION = 161
    TIME_SHIFTED_SERVICE = 162
    COMPONENT_NAME = 163
    DCC_DEPARTING_REQUEST = 168
    DCC_ARRIVING_REQUEST = 169
    REDISTRIBUTION_CONTROL = 170
    GENRE = 171
    PRIVATE_INFORMATION = 173
    EAC3 = 204
    ENHANCED_SIGNALING = 178
    DATA_SERVICE = 164
    PID_COUNT = 165
    DOWNLOAD_DESCRIPTOR = 166
    MULTIPROTOCOL_ENCAPSULATION = 167
    MODULE_LINK = 180
    CRC32 = 181
    GROUP_LINK = 184


class AtscMGTTableType:
    """"""
    EIT0 = 256
    EIT127 = 383
    ETT0 = 512
    ETT127 = 639


class CableOuterFECScheme:
    """"""
    UNDEFINED = 0
    NONE = 1
    RS_204_188 = 2


class ComponentStreamContent:
    """"""
    MPEG2_VIDEO = 1
    MPEG1_LAYER2_AUDIO = 2
    TELETEXT_OR_SUBTITLE = 3
    AC_3 = 4
    AVC = 5
    AAC = 6
    DTS = 7
    SRM_CPCM = 8


class ContentNibbleHi:
    """"""
    MOVIE_DRAMA = 1
    NEWS_CURRENT_AFFAIRS = 2
    SHOW_GAME_SHOW = 3
    SPORTS = 4
    CHILDREN_YOUTH_PROGRAM = 5
    MUSIC_BALLET_DANCE = 6
    ARTS_CULTURE = 7
    SOCIAL_POLITICAL_ECONOMICS = 8
    EDUCATION_SCIENCE_FACTUAL = 9
    LEISURE_HOBBIES = 10
    SPECIAL_CHARACTERISTICS = 11


class DVBCodeRate:
    """"""
    NONE = 0
    _1_2 = 1
    _2_3 = 2
    _3_4 = 3
    _4_5 = 4
    _5_6 = 5
    _6_7 = 6
    _7_8 = 7
    _8_9 = 8
    AUTO = 9
    _3_5 = 10
    _9_10 = 11
    _2_5 = 12


class DVBDescriptorType:
    """"""
    NETWORK_NAME = 64
    SERVICE_LIST = 65
    STUFFING = 66
    SATELLITE_DELIVERY_SYSTEM = 67
    CABLE_DELIVERY_SYSTEM = 68
    VBI_DATA = 69
    VBI_TELETEXT = 70
    BOUQUET_NAME = 71
    SERVICE = 72
    COUNTRY_AVAILABILITY = 73
    LINKAGE = 74
    NVOD_REFERENCE = 75
    TIME_SHIFTED_SERVICE = 76
    SHORT_EVENT = 77
    EXTENDED_EVENT = 78
    TIME_SHIFTED_EVENT = 79
    COMPONENT = 80
    MOSAIC = 81
    STREAM_IDENTIFIER = 82
    CA_IDENTIFIER = 83
    CONTENT = 84
    PARENTAL_RATING = 85
    TELETEXT = 86
    TELEPHONE = 87
    LOCAL_TIME_OFFSET = 88
    SUBTITLING = 89
    TERRESTRIAL_DELIVERY_SYSTEM = 90
    MULTILINGUAL_NETWORK_NAME = 91
    MULTILINGUAL_BOUQUET_NAME = 92
    MULTILINGUAL_SERVICE_NAME = 93
    MULTILINGUAL_COMPONENT = 94
    PRIVATE_DATA_SPECIFIER = 95
    SERVICE_MOVE = 96
    SHORT_SMOOTHING_BUFFER = 97
    FREQUENCY_LIST = 98
    PARTIAL_TRANSPORT_STREAM = 99
    DATA_BROADCAST = 100
    SCRAMBLING = 101
    DATA_BROADCAST_ID = 102
    TRANSPORT_STREAM = 103
    DSNG = 104
    PDC = 105
    AC3 = 106
    ANCILLARY_DATA = 107
    CELL_LIST = 108
    CELL_FREQUENCY_LINK = 109
    ANNOUNCEMENT_SUPPORT = 110
    APPLICATION_SIGNALLING = 111
    ADAPTATION_FIELD_DATA = 112
    SERVICE_IDENTIFIER = 113
    SERVICE_AVAILABILITY = 114
    DEFAULT_AUTHORITY = 115
    RELATED_CONTENT = 116
    TVA_ID = 117
    CONTENT_IDENTIFIER = 118
    TIMESLICE_FEC_IDENTIFIER = 119
    ECM_REPETITION_RATE = 120
    S2_SATELLITE_DELIVERY_SYSTEM = 121
    ENHANCED_AC3 = 122
    DTS = 123
    AAC = 124
    XAIT_LOCATION = 125
    FTA_CONTENT_MANAGEMENT = 126
    EXTENSION = 127


class DVBExtendedDescriptorType:
    """"""
    IMAGE_ICON = 0
    CPCM_DELIVERY_SIGNALLING = 1
    CP = 2
    CP_IDENTIFIER = 3
    T2_DELIVERY_SYSTEM = 4
    SH_DELIVERY_SYSTEM = 5
    SUPPLEMENTARY_AUDIO = 6
    NETWORK_CHANGE_NOTIFY = 7
    MESSAGE = 8
    TARGET_REGION = 9
    TARGET_REGION_NAME = 10
    SERVICE_RELOCATED = 11
    XAIT_PID = 12
    C2_DELIVERY_SYSTEM = 13
    DTS_HD_AUDIO_STREAM = 14
    DTS_NEUTRAL = 15
    VIDEO_DEPTH_RANGE = 16
    T2MI = 17
    URI_LINKAGE = 19


class DVBLinkageHandOverType:
    """"""
    RESERVED = 0
    IDENTICAL = 1
    LOCAL_VARIATION = 2
    ASSOCIATED = 3


class DVBLinkageType:
    """"""
    RESERVED_00 = 0
    INFORMATION = 1
    EPG = 2
    CA_REPLACEMENT = 3
    TS_CONTAINING_COMPLETE_SI = 4
    SERVICE_REPLACEMENT = 5
    DATA_BROADCAST = 6
    RCS_MAP = 7
    MOBILE_HAND_OVER = 8
    SYSTEM_SOFTWARE_UPDATE = 9
    TS_CONTAINING_SSU = 10
    IP_MAC_NOTIFICATION = 11
    TS_CONTAINING_INT = 12
    EVENT = 13
    EXTENDED_EVENT = 14


class DVBScramblingModeType:
    """"""
    RESERVED = 0
    CSA1 = 1
    CSA2 = 2
    CSA3_STANDARD = 3
    CSA3_MINIMAL_ENHANCED = 4
    CSA3_FULL_ENHANCED = 5
    CISSA = 16
    ATIS_0 = 112
    ATIS_F = 127


class DVBServiceType:
    """"""
    RESERVED_00 = 0
    DIGITAL_TELEVISION = 1
    DIGITAL_RADIO_SOUND = 2
    TELETEXT = 3
    NVOD_REFERENCE = 4
    NVOD_TIME_SHIFTED = 5
    MOSAIC = 6
    FM_RADIO = 7
    DVB_SRM = 8
    RESERVED_09 = 9
    ADVANCED_CODEC_DIGITAL_RADIO_SOUND = 10
    ADVANCED_CODEC_MOSAIC = 11
    DATA_BROADCAST = 12
    RESERVED_0D_COMMON_INTERFACE = 13
    RCS_MAP = 14
    RCS_FLS = 15
    DVB_MHP = 16
    MPEG2_HD_DIGITAL_TELEVISION = 17
    ADVANCED_CODEC_SD_DIGITAL_TELEVISION = 22
    ADVANCED_CODEC_SD_NVOD_TIME_SHIFTED = 23
    ADVANCED_CODEC_SD_NVOD_REFERENCE = 24
    ADVANCED_CODEC_HD_DIGITAL_TELEVISION = 25
    ADVANCED_CODEC_HD_NVOD_TIME_SHIFTED = 26
    ADVANCED_CODEC_HD_NVOD_REFERENCE = 27
    ADVANCED_CODEC_STEREO_HD_DIGITAL_TELEVISION = 28
    ADVANCED_CODEC_STEREO_HD_NVOD_TIME_SHIFTED = 29
    ADVANCED_CODEC_STEREO_HD_NVOD_REFERENCE = 30
    RESERVED_FF = 31


class DVBTeletextType:
    """"""
    NITIAL_PAGE = 1
    UBTITLE_PAGE = 2
    DDITIONAL_INFO_PAGE = 3
    ROGRAMME_SCHEDULE_PAGE = 4
    EARING_IMPAIRED_PAGE = 5


class DescriptorType:
    """"""
    RESERVED_00 = 0
    RESERVED_01 = 1
    VIDEO_STREAM = 2
    AUDIO_STREAM = 3
    HIERARCHY = 4
    REGISTRATION = 5
    DATA_STREAM_ALIGNMENT = 6
    TARGET_BACKGROUND_GRID = 7
    VIDEO_WINDOW = 8
    CA = 9
    ISO_639_LANGUAGE = 10
    SYSTEM_CLOCK = 11
    MULTIPLEX_BUFFER_UTILISATION = 12
    COPYRIGHT = 13
    MAXIMUM_BITRATE = 14
    PRIVATE_DATA_INDICATOR = 15
    SMOOTHING_BUFFER = 16
    STD = 17
    IBP = 18
    DSMCC_CAROUSEL_IDENTIFIER = 19
    DSMCC_ASSOCIATION_TAG = 20
    DSMCC_DEFERRED_ASSOCIATION_TAG = 21
    DSMCC_NPT_REFERENCE = 23
    DSMCC_NPT_ENDPOINT = 24
    DSMCC_STREAM_MODE = 25
    DSMCC_STREAM_EVENT = 26
    MPEG4_VIDEO = 27
    MPEG4_AUDIO = 28
    IOD = 29
    SL = 30
    FMC = 31
    EXTERNAL_ES_ID = 32
    MUX_CODE = 33
    FMX_BUFFER_SIZE = 34
    MULTIPLEX_BUFFER = 35
    CONTENT_LABELING = 36
    METADATA_POINTER = 37
    METADATA = 38
    METADATA_STD = 39
    AVC_VIDEO = 40
    IPMP = 41
    AVC_TIMING_AND_HRD = 42
    MPEG2_AAC_AUDIO = 43
    FLEX_MUX_TIMING = 44
    MPEG4_TEXT = 45
    MPEG4_AUDIO_EXTENSION = 46
    AUXILIARY_VIDEO_STREAM = 47
    SVC_EXTENSION = 48
    MVC_EXTENSION = 49
    J2K_VIDEO = 50
    MVC_OPERATION_POINT = 51
    MPEG2_STEREOSCOPIC_VIDEO_FORMAT = 52
    STEREOSCOPIC_PROGRAM_INFO = 53
    STEREOSCOPIC_VIDEO_INFO = 54


class ISDBDescriptorType:
    """"""
    HIERARCHICAL_TRANSMISSION = 192
    DIGITAL_COPY_CONTROL = 193
    NETWORK_IDENTIFICATION = 194
    PARTIAL_TS_TIME = 195
    AUDIO_COMPONENT = 196
    HYPERLINK = 197
    TARGET_REGION = 198
    DATA_CONTENT = 199
    VIDEO_DECODE_CONTROL = 200
    DOWNLOAD_CONTENT = 201
    CA_EMM_TS = 202
    CA_CONTRACT_INFORMATION = 203
    CA_SERVICE = 204
    TS_INFORMATION = 205
    EXTENDED_BROADCASTER = 206
    LOGO_TRANSMISSION = 207
    BASIC_LOCAL_EVENT = 208
    REFERENCE = 209
    NODE_RELATION = 210
    SHORT_NODE_INFORMATION = 211
    STC_REFERENCE = 212
    SERIES = 213
    EVENT_GROUP = 214
    SI_PARAMETER = 215
    BROADCASTER_NAME = 216
    COMPONENT_GROUP = 217
    SI_PRIME_TS = 218
    BOARD_INFORMATION = 219
    LDT_LINKAGE = 220
    CONNECTED_TRANSMISSION = 221
    CONTENT_AVAILABILITY = 222
    SERVICE_GROUP = 224


class Iso639AudioType:
    """"""
    UNDEFINED = 0
    CLEAN_EFFECTS = 1
    HEARING_IMPAIRED = 2
    VISUAL_IMPAIRED_COMMENTARY = 3


class MiscDescriptorType:
    """"""
    AC3_AUDIO_STREAM = 129
    DTG_LOGICAL_CHANNEL = 131


class ModulationType:
    """"""
    QPSK = 0
    QAM_16 = 1
    QAM_32 = 2
    QAM_64 = 3
    QAM_128 = 4
    QAM_256 = 5
    QAM_AUTO = 6
    VSB_8 = 7
    VSB_16 = 8
    PSK_8 = 9
    APSK_16 = 10
    APSK_32 = 11
    DQPSK = 12
    QAM_4_NR_ = 13
    NONE = 14


class RunningStatus:
    """"""
    UNDEFINED = 0
    NOT_RUNNING = 1
    STARTS_IN_FEW_SECONDS = 2
    PAUSING = 3
    RUNNING = 4
    OFF_AIR = 5


class SatellitePolarizationType:
    """"""
    LINEAR_HORIZONTAL = 0
    LINEAR_VERTICAL = 1
    CIRCULAR_LEFT = 2
    CIRCULAR_RIGHT = 3


class SatelliteRolloff:
    """"""
    _35 = 0
    _20 = 1
    _25 = 2
    RESERVED = 3
    AUTO = 4


class ScteStreamType:
    """"""
    SUBTITLING = 130
    ISOCH_DATA = 131
    DST_NRT = 149
    DSMCC_DCB = 176
    SIGNALING = 192
    SYNC_DATA = 194
    ASYNC_DATA = 195


class SectionATSCTableID:
    """"""
    MASTER_GUIDE = 199
    TERRESTRIAL_VIRTUAL_CHANNEL = 200
    CABLE_VIRTUAL_CHANNEL = 201
    RATING_REGION = 202
    EVENT_INFORMATION = 203
    CHANNEL_OR_EVENT_EXTENDED_TEXT = 204
    SYSTEM_TIME = 205
    DATA_EVENT = 206
    DATA_SERVICE = 207
    NETWORK_RESOURCE = 209
    LONG_TERM_SERVICE = 210
    DIRECTED_CHANNEL_CHANGE = 211
    DIRECTED_CHANNEL_CHANGE_SECTION_CODE = 212
    AGGREGATE_EVENT_INFORMATION = 214
    AGGREGATE_EXTENDED_TEXT = 215
    AGGREGATE_DATA_EVENT = 217
    SATELLITE_VIRTUAL_CHANNEL = 218


class SectionDVBTableID:
    """"""
    NETWORK_INFORMATION_ACTUAL_NETWORK = 64
    NETWORK_INFORMATION_OTHER_NETWORK = 65
    SERVICE_DESCRIPTION_ACTUAL_TS = 66
    SERVICE_DESCRIPTION_OTHER_TS = 70
    BOUQUET_ASSOCIATION = 74
    EVENT_INFORMATION_ACTUAL_TS_PRESENT = 78
    EVENT_INFORMATION_OTHER_TS_PRESENT = 79
    EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_1 = 80
    EVENT_INFORMATION_ACTUAL_TS_SCHEDULE_N = 95
    EVENT_INFORMATION_OTHER_TS_SCHEDULE_1 = 96
    EVENT_INFORMATION_OTHER_TS_SCHEDULE_N = 111
    TIME_DATE = 112
    RUNNING_STATUS = 113
    STUFFING = 114
    TIME_OFFSET = 115
    APPLICATION_INFORMATION_TABLE = 116
    CONTAINER = 117
    RELATED_CONTENT = 118
    CONTENT_IDENTIFIER = 119
    MPE_FEC = 120
    RESOLUTION_NOTIFICATION = 121
    MPE_IFEC = 122
    DISCONTINUITY_INFORMATION = 126
    SELECTION_INFORMATION = 127
    CA_MESSAGE_ECM_0 = 128
    CA_MESSAGE_ECM_1 = 129
    CA_MESSAGE_SYSTEM_PRIVATE_1 = 130
    CA_MESSAGE_SYSTEM_PRIVATE_N = 143
    SCT = 160
    FCT = 161
    TCT = 162
    SPT = 163
    CMT = 164
    TBTP = 165
    PCR_PACKET_PAYLOAD = 166
    TRANSMISSION_MODE_SUPPORT_PAYLOAD = 170
    TIM = 176
    LL_FEC_PARITY_DATA_TABLE = 177


class SectionSCTETableID:
    """"""
    EAS = 216
    EBIF = 224
    RESERVED = 225
    EISS = 226
    DII = 227
    DDB = 228
    SPLICE = 252


class SectionTableID:
    """"""
    PROGRAM_ASSOCIATION = 0
    CONDITIONAL_ACCESS = 1
    TS_PROGRAM_MAP = 2
    TS_DESCRIPTION = 3
    _14496_SCENE_DESCRIPTION = 4
    _14496_OBJET_DESCRIPTOR = 5
    METADATA = 6
    IPMP_CONTROL_INFORMATION = 7
    DSM_CC_MULTIPROTO_ENCAPSULATED_DATA = 58
    DSM_CC_U_N_MESSAGES = 59
    DSM_CC_DOWNLOAD_DATA_MESSAGES = 60
    DSM_CC_STREAM_DESCRIPTORS = 61
    DSM_CC_PRIVATE_DATA = 62
    DSM_CC_ADDRESSABLE_SECTIONS = 63
    UNSET = 255


class SectionType:
    """"""
    UNKNOWN = 0
    PAT = 1
    PMT = 2
    CAT = 3
    TSDT = 4
    EIT = 5
    NIT = 6
    BAT = 7
    SDT = 8
    TDT = 9
    TOT = 10
    ATSC_TVCT = 11
    ATSC_CVCT = 12
    ATSC_MGT = 13
    ATSC_ETT = 14
    ATSC_EIT = 15
    ATSC_STT = 16


class StreamType:
    """"""
    RESERVED_00 = 0
    VIDEO_MPEG1 = 1
    VIDEO_MPEG2 = 2
    AUDIO_MPEG1 = 3
    AUDIO_MPEG2 = 4
    PRIVATE_SECTIONS = 5
    PRIVATE_PES_PACKETS = 6
    MHEG = 7
    DSM_CC = 8
    H_222_1 = 9
    DSMCC_A = 10
    DSMCC_B = 11
    DSMCC_C = 12
    DSMCC_D = 13
    AUXILIARY = 14
    AUDIO_AAC_ADTS = 15
    VIDEO_MPEG4 = 16
    AUDIO_AAC_LATM = 17
    SL_FLEXMUX_PES_PACKETS = 18
    SL_FLEXMUX_SECTIONS = 19
    SYNCHRONIZED_DOWNLOAD = 20
    METADATA_PES_PACKETS = 21
    METADATA_SECTIONS = 22
    METADATA_DATA_CAROUSEL = 23
    METADATA_OBJECT_CAROUSEL = 24
    METADATA_SYNCHRONIZED_DOWNLOAD = 25
    MPEG2_IPMP = 26
    VIDEO_H264 = 27
    AUDIO_AAC_CLEAN = 28
    MPEG4_TIMED_TEXT = 29
    VIDEO_RVC = 30
    VIDEO_H264_SVC_SUB_BITSTREAM = 31
    VIDEO_H264_MVC_SUB_BITSTREAM = 32
    VIDEO_JP2K = 33
    VIDEO_MPEG2_STEREO_ADDITIONAL_VIEW = 34
    VIDEO_H264_STEREO_ADDITIONAL_VIEW = 35
    VIDEO_HEVC = 36
    IPMP_STREAM = 127


class TerrestrialGuardInterval:
    """"""
    _1_32 = 0
    _1_16 = 1
    _1_8 = 2
    _1_4 = 3
    AUTO = 4
    _1_128 = 5
    _19_128 = 6
    _19_256 = 7
    PN420 = 8
    PN595 = 9
    PN945 = 10


class TerrestrialHierarchy:
    """"""
    NONE = 0
    _1 = 1
    _2 = 2
    _4 = 3
    AUTO = 4


class TerrestrialTransmissionMode:
    """"""
    _2K = 0
    _8K = 1
    AUTO = 2
    _4K = 3
    _1K = 4
    _16K = 5
    _32K = 6
    C1 = 7
    C3780 = 8

def descriptor_from_custom(tag=None, data=None, length=None):
    """"""
    return object

def descriptor_from_custom_with_extension(tag=None, tag_extension=None, data=None, length=None):
    """"""
    return object

def descriptor_from_dvb_network_name(name=None):
    """"""
    return object

def descriptor_from_dvb_service(service_type=None, service_name=None, service_provider=None):
    """"""
    return object

def descriptor_from_dvb_subtitling(lang=None, type=None, composition=None, ancillary=None):
    """"""
    return object

def descriptor_from_iso_639_language(language=None):
    """"""
    return object

def descriptor_from_registration(format_identifier=None, additional_info=None, additional_info_length=None):
    """"""
    return object

def dvb_component_descriptor_free(source=None):
    """"""
    return object

def event_parse_mpegts_section(event=None):
    """"""
    return object

def find_descriptor(descriptors=None, tag=None):
    """"""
    return object

def initialize():
    """"""
    return object

def message_new_mpegts_section(parent=None, section=None):
    """"""
    return object

def message_parse_mpegts_section(message=None):
    """"""
    return object

def parse_descriptors(buffer=None, buf_len=None):
    """"""
    return object

def pat_new():
    """"""
    return object

def section_from_nit(nit=None):
    """"""
    return object

def section_from_pat(programs=None, ts_id=None):
    """"""
    return object

def section_from_pmt(pmt=None, pid=None):
    """"""
    return object

def section_from_sdt(sdt=None):
    """"""
    return object


class AtscEIT():
    """"""

    @property
    def source_id(self):
        return object

    @property
    def protocol_version(self):
        return object

    @property
    def events(self):
        return object


class AtscEITEvent():
    """"""

    @property
    def event_id(self):
        return object

    @property
    def start_time(self):
        return object

    @property
    def etm_location(self):
        return object

    @property
    def length_in_seconds(self):
        return object

    @property
    def titles(self):
        return object

    @property
    def descriptors(self):
        return object


class AtscETT():
    """"""

    @property
    def ett_table_id_extension(self):
        return object

    @property
    def protocol_version(self):
        return object

    @property
    def etm_id(self):
        return object

    @property
    def messages(self):
        return object


class AtscMGT():
    """"""

    @property
    def protocol_version(self):
        return object

    @property
    def tables_defined(self):
        return object

    @property
    def tables(self):
        return object

    @property
    def descriptors(self):
        return object


class AtscMGTTable():
    """"""

    @property
    def table_type(self):
        return object

    @property
    def pid(self):
        return object

    @property
    def version_number(self):
        return object

    @property
    def number_bytes(self):
        return object

    @property
    def descriptors(self):
        return object


class AtscMultString():
    """"""

    @property
    def iso_639_langcode(self):
        return object

    @property
    def segments(self):
        return object


class AtscSTT():
    """"""
    
    def get_datetime_utc(self):
        """"""
        return object

    @property
    def protocol_version(self):
        return object

    @property
    def system_time(self):
        return object

    @property
    def gps_utc_offset(self):
        return object

    @property
    def ds_status(self):
        return object

    @property
    def ds_dayofmonth(self):
        return object

    @property
    def ds_hour(self):
        return object

    @property
    def descriptors(self):
        return object

    @property
    def utc_datetime(self):
        return object


class AtscStringSegment():
    """"""
    
    def get_string(self):
        """"""
        return object

    @property
    def compression_type(self):
        return object

    @property
    def mode(self):
        return object

    @property
    def compressed_data_size(self):
        return object

    @property
    def compressed_data(self):
        return object

    @property
    def cached_string(self):
        return object


class AtscVCT():
    """"""

    @property
    def transport_stream_id(self):
        return object

    @property
    def protocol_version(self):
        return object

    @property
    def sources(self):
        return object

    @property
    def descriptors(self):
        return object


class AtscVCTSource():
    """"""

    @property
    def short_name(self):
        return object

    @property
    def major_channel_number(self):
        return object

    @property
    def minor_channel_number(self):
        return object

    @property
    def modulation_mode(self):
        return object

    @property
    def carrier_frequency(self):
        return object

    @property
    def channel_TSID(self):
        return object

    @property
    def program_number(self):
        return object

    @property
    def ETM_location(self):
        return object

    @property
    def access_controlled(self):
        return object

    @property
    def hidden(self):
        return object

    @property
    def path_select(self):
        return object

    @property
    def out_of_band(self):
        return object

    @property
    def hide_guide(self):
        return object

    @property
    def service_type(self):
        return object

    @property
    def source_id(self):
        return object

    @property
    def descriptors(self):
        return object


class BAT():
    """"""

    @property
    def descriptors(self):
        return object

    @property
    def streams(self):
        return object


class BATStream():
    """"""

    @property
    def transport_stream_id(self):
        return object

    @property
    def original_network_id(self):
        return object

    @property
    def descriptors(self):
        return object


class CableDeliverySystemDescriptor():
    """"""
    
    def free(self):
        """"""
        return object

    @property
    def frequency(self):
        return object

    @property
    def outer_fec(self):
        return object

    @property
    def modulation(self):
        return object

    @property
    def symbol_rate(self):
        return object

    @property
    def fec_inner(self):
        return object


class ComponentDescriptor():
    """"""

    @property
    def stream_content(self):
        return object

    @property
    def component_type(self):
        return object

    @property
    def component_tag(self):
        return object

    @property
    def language_code(self):
        return object

    @property
    def text(self):
        return object


class Content():
    """"""

    @property
    def content_nibble_1(self):
        return object

    @property
    def content_nibble_2(self):
        return object

    @property
    def user_byte(self):
        return object


class DVBLinkageDescriptor():
    """"""
    
    def free(self):
        """"""
        return object
    
    def get_event(self):
        """"""
        return object
    
    def get_extended_event(self):
        """"""
        return object
    
    def get_mobile_hand_over(self):
        """"""
        return object

    @property
    def transport_stream_id(self):
        return object

    @property
    def original_network_id(self):
        return object

    @property
    def service_id(self):
        return object

    @property
    def linkage_type(self):
        return object

    @property
    def linkage_data(self):
        return object

    @property
    def private_data_length(self):
        return object

    @property
    def private_data_bytes(self):
        return object


class DVBLinkageEvent():
    """"""

    @property
    def target_event_id(self):
        return object

    @property
    def target_listed(self):
        return object

    @property
    def event_simulcast(self):
        return object


class DVBLinkageExtendedEvent():
    """"""

    @property
    def target_event_id(self):
        return object

    @property
    def target_listed(self):
        return object

    @property
    def event_simulcast(self):
        return object

    @property
    def link_type(self):
        return object

    @property
    def target_id_type(self):
        return object

    @property
    def original_network_id_flag(self):
        return object

    @property
    def service_id_flag(self):
        return object

    @property
    def user_defined_id(self):
        return object

    @property
    def target_transport_stream_id(self):
        return object

    @property
    def target_original_network_id(self):
        return object

    @property
    def target_service_id(self):
        return object


class DVBLinkageMobileHandOver():
    """"""

    @property
    def hand_over_type(self):
        return object

    @property
    def origin_type(self):
        return object

    @property
    def network_id(self):
        return object

    @property
    def initial_service_id(self):
        return object


class DVBParentalRatingItem():
    """"""

    @property
    def country_code(self):
        return object

    @property
    def rating(self):
        return object


class DVBServiceListItem():
    """"""

    @property
    def service_id(self):
        return object

    @property
    def type(self):
        return object


class DataBroadcastDescriptor():
    """"""
    
    def free(self):
        """"""
        return object

    @property
    def data_broadcast_id(self):
        return object

    @property
    def component_tag(self):
        return object

    @property
    def length(self):
        return object

    @property
    def selector_bytes(self):
        return object

    @property
    def language_code(self):
        return object

    @property
    def text(self):
        return object


class Descriptor():
    """"""
    
    def free(self):
        """"""
        return object
    
    def parse_ca(self, ca_system_id=None, ca_pid=None, private_data=None, private_data_size=None):
        """"""
        return object
    
    def parse_cable_delivery_system(self, res=None):
        """"""
        return object
    
    def parse_dvb_bouquet_name(self, bouquet_name=None):
        """"""
        return object
    
    def parse_dvb_ca_identifier(self, list=None):
        """"""
        return object
    
    def parse_dvb_component(self, res=None):
        """"""
        return object
    
    def parse_dvb_content(self, content=None):
        """"""
        return object
    
    def parse_dvb_data_broadcast(self, res=None):
        """"""
        return object
    
    def parse_dvb_data_broadcast_id(self, data_broadcast_id=None, id_selector_bytes=None, len=None):
        """"""
        return object
    
    def parse_dvb_extended_event(self, res=None):
        """"""
        return object
    
    def parse_dvb_frequency_list(self, offset=None, list=None):
        """"""
        return object
    
    def parse_dvb_linkage(self, res=None):
        """"""
        return object
    
    def parse_dvb_multilingual_bouquet_name(self, bouquet_name_items=None):
        """"""
        return object
    
    def parse_dvb_multilingual_component(self, component_tag=None, component_description_items=None):
        """"""
        return object
    
    def parse_dvb_multilingual_network_name(self, network_name_items=None):
        """"""
        return object
    
    def parse_dvb_multilingual_service_name(self, service_name_items=None):
        """"""
        return object
    
    def parse_dvb_network_name(self, name=None):
        """"""
        return object
    
    def parse_dvb_parental_rating(self, rating=None):
        """"""
        return object
    
    def parse_dvb_private_data_specifier(self, private_data_specifier=None, private_data=None, length=None):
        """"""
        return object
    
    def parse_dvb_scrambling(self, scrambling_mode=None):
        """"""
        return object
    
    def parse_dvb_service(self, service_type=None, service_name=None, provider_name=None):
        """"""
        return object
    
    def parse_dvb_service_list(self, list=None):
        """"""
        return object
    
    def parse_dvb_short_event(self, language_code=None, event_name=None, text=None):
        """"""
        return object
    
    def parse_dvb_stream_identifier(self, component_tag=None):
        """"""
        return object
    
    def parse_dvb_stuffing(self, stuffing_bytes=None):
        """"""
        return object
    
    def parse_dvb_subtitling_idx(self, idx=None, lang=None, type=None, composition_page_id=None, ancillary_page_id=None):
        """"""
        return object
    
    def parse_dvb_subtitling_nb(self):
        """"""
        return object
    
    def parse_dvb_t2_delivery_system(self, res=None):
        """"""
        return object
    
    def parse_dvb_teletext_idx(self, idx=None, language_code=None, teletext_type=None, magazine_number=None, page_number=None):
        """"""
        return object
    
    def parse_dvb_teletext_nb(self):
        """"""
        return object
    
    def parse_iso_639_language(self, res=None):
        """"""
        return object
    
    def parse_iso_639_language_idx(self, idx=None, lang=None, audio_type=None):
        """"""
        return object
    
    def parse_iso_639_language_nb(self):
        """"""
        return object
    
    def parse_logical_channel(self, res=None):
        """"""
        return object
    
    def parse_satellite_delivery_system(self, res=None):
        """"""
        return object
    
    def parse_terrestrial_delivery_system(self, res=None):
        """"""
        return object
    @staticmethod
    def from_custom(tag=None, data=None, length=None):
        """"""
        return object
    @staticmethod
    def from_custom_with_extension(tag=None, tag_extension=None, data=None, length=None):
        """"""
        return object
    @staticmethod
    def from_dvb_network_name(name=None):
        """"""
        return object
    @staticmethod
    def from_dvb_service(service_type=None, service_name=None, service_provider=None):
        """"""
        return object
    @staticmethod
    def from_dvb_subtitling(lang=None, type=None, composition=None, ancillary=None):
        """"""
        return object
    @staticmethod
    def from_iso_639_language(language=None):
        """"""
        return object
    @staticmethod
    def from_registration(format_identifier=None, additional_info=None, additional_info_length=None):
        """"""
        return object

    @property
    def tag(self):
        return object

    @property
    def tag_extension(self):
        return object

    @property
    def length(self):
        return object

    @property
    def data(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class DvbMultilingualBouquetNameItem():
    """"""

    @property
    def language_code(self):
        return object

    @property
    def bouquet_name(self):
        return object


class DvbMultilingualComponentItem():
    """"""

    @property
    def language_code(self):
        return object

    @property
    def description(self):
        return object


class DvbMultilingualNetworkNameItem():
    """"""

    @property
    def language_code(self):
        return object

    @property
    def network_name(self):
        return object


class DvbMultilingualServiceNameItem():
    """"""

    @property
    def language_code(self):
        return object

    @property
    def provider_name(self):
        return object

    @property
    def service_name(self):
        return object


class EIT():
    """"""

    @property
    def transport_stream_id(self):
        return object

    @property
    def original_network_id(self):
        return object

    @property
    def segment_last_section_number(self):
        return object

    @property
    def last_table_id(self):
        return object

    @property
    def actual_stream(self):
        return object

    @property
    def present_following(self):
        return object

    @property
    def events(self):
        return object


class EITEvent():
    """"""

    @property
    def event_id(self):
        return object

    @property
    def start_time(self):
        return object

    @property
    def duration(self):
        return object

    @property
    def running_status(self):
        return object

    @property
    def free_CA_mode(self):
        return object

    @property
    def descriptors(self):
        return object


class ExtendedEventDescriptor():
    """"""
    
    def free(self):
        """"""
        return object

    @property
    def descriptor_number(self):
        return object

    @property
    def last_descriptor_number(self):
        return object

    @property
    def language_code(self):
        return object

    @property
    def items(self):
        return object

    @property
    def text(self):
        return object


class ExtendedEventItem():
    """"""

    @property
    def item_description(self):
        return object

    @property
    def item(self):
        return object


class ISO639LanguageDescriptor():
    """"""
    
    def descriptor_free(self):
        """"""
        return object

    @property
    def nb_language(self):
        return object

    @property
    def language(self):
        return object

    @property
    def audio_type(self):
        return object


class LogicalChannel():
    """"""

    @property
    def service_id(self):
        return object

    @property
    def visible_service(self):
        return object

    @property
    def logical_channel_number(self):
        return object


class LogicalChannelDescriptor():
    """"""

    @property
    def nb_channels(self):
        return object

    @property
    def channels(self):
        return object


class NIT():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def actual_network(self):
        return object

    @property
    def network_id(self):
        return object

    @property
    def descriptors(self):
        return object

    @property
    def streams(self):
        return object


class NITStream():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def transport_stream_id(self):
        return object

    @property
    def original_network_id(self):
        return object

    @property
    def descriptors(self):
        return object


class PMT():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def pcr_pid(self):
        return object

    @property
    def program_number(self):
        return object

    @property
    def descriptors(self):
        return object

    @property
    def streams(self):
        return object


class PMTStream():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def stream_type(self):
        return object

    @property
    def pid(self):
        return object

    @property
    def descriptors(self):
        return object


class PatProgram():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def program_number(self):
        return object

    @property
    def network_or_program_map_PID(self):
        return object


class SDT():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def original_network_id(self):
        return object

    @property
    def actual_ts(self):
        return object

    @property
    def transport_stream_id(self):
        return object

    @property
    def services(self):
        return object


class SDTService():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def service_id(self):
        return object

    @property
    def EIT_schedule_flag(self):
        return object

    @property
    def EIT_present_following_flag(self):
        return object

    @property
    def running_status(self):
        return object

    @property
    def free_CA_mode(self):
        return object

    @property
    def descriptors(self):
        return object


class SatelliteDeliverySystemDescriptor():
    """"""

    @property
    def frequency(self):
        return object

    @property
    def orbital_position(self):
        return object

    @property
    def west_east(self):
        return object

    @property
    def polarization(self):
        return object

    @property
    def roll_off(self):
        return object

    @property
    def modulation_system(self):
        return object

    @property
    def modulation_type(self):
        return object

    @property
    def symbol_rate(self):
        return object

    @property
    def fec_inner(self):
        return object


class Section():
    """"""
    
    def __init__(self, pid=None, data=None, data_size=None):
        """"""
        return object
    @staticmethod
    def new(pid=None, data=None, data_size=None):
        """"""
        return object
    
    def get_atsc_cvct(self):
        """"""
        return object
    
    def get_atsc_eit(self):
        """"""
        return object
    
    def get_atsc_ett(self):
        """"""
        return object
    
    def get_atsc_mgt(self):
        """"""
        return object
    
    def get_atsc_stt(self):
        """"""
        return object
    
    def get_atsc_tvct(self):
        """"""
        return object
    
    def get_bat(self):
        """"""
        return object
    
    def get_cat(self):
        """"""
        return object
    
    def get_data(self):
        """"""
        return object
    
    def get_eit(self):
        """"""
        return object
    
    def get_nit(self):
        """"""
        return object
    
    def get_pat(self):
        """"""
        return object
    
    def get_pmt(self):
        """"""
        return object
    
    def get_sdt(self):
        """"""
        return object
    
    def get_tdt(self):
        """"""
        return object
    
    def get_tot(self):
        """"""
        return object
    
    def get_tsdt(self):
        """"""
        return object
    
    def packetize(self, output_size=None):
        """"""
        return object
    
    def send_event(self, element=None):
        """"""
        return object
    @staticmethod
    def from_nit(nit=None):
        """"""
        return object
    @staticmethod
    def from_pat(programs=None, ts_id=None):
        """"""
        return object
    @staticmethod
    def from_pmt(pmt=None, pid=None):
        """"""
        return object
    @staticmethod
    def from_sdt(sdt=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def section_type(self):
        return object

    @property
    def pid(self):
        return object

    @property
    def table_id(self):
        return object

    @property
    def subtable_extension(self):
        return object

    @property
    def version_number(self):
        return object

    @property
    def current_next_indicator(self):
        return object

    @property
    def section_number(self):
        return object

    @property
    def last_section_number(self):
        return object

    @property
    def crc(self):
        return object

    @property
    def data(self):
        return object

    @property
    def section_length(self):
        return object

    @property
    def cached_parsed(self):
        return object

    @property
    def destroy_parsed(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def short_section(self):
        return object

    @property
    def packetizer(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class T2DeliverySystemCell():
    """"""

    @property
    def cell_id(self):
        return object

    @property
    def centre_frequencies(self):
        return object

    @property
    def sub_cells(self):
        return object


class T2DeliverySystemCellExtension():
    """"""

    @property
    def cell_id_extension(self):
        return object

    @property
    def transposer_frequency(self):
        return object


class T2DeliverySystemDescriptor():
    """"""
    
    def free(self):
        """"""
        return object

    @property
    def plp_id(self):
        return object

    @property
    def t2_system_id(self):
        return object

    @property
    def siso_miso(self):
        return object

    @property
    def bandwidth(self):
        return object

    @property
    def guard_interval(self):
        return object

    @property
    def transmission_mode(self):
        return object

    @property
    def other_frequency(self):
        return object

    @property
    def tfs(self):
        return object

    @property
    def cells(self):
        return object


class TOT():
    """"""

    @property
    def utc_time(self):
        return object

    @property
    def descriptors(self):
        return object


class TerrestrialDeliverySystemDescriptor():
    """"""

    @property
    def frequency(self):
        return object

    @property
    def bandwidth(self):
        return object

    @property
    def priority(self):
        return object

    @property
    def time_slicing(self):
        return object

    @property
    def mpe_fec(self):
        return object

    @property
    def constellation(self):
        return object

    @property
    def hierarchy(self):
        return object

    @property
    def code_rate_hp(self):
        return object

    @property
    def code_rate_lp(self):
        return object

    @property
    def guard_interval(self):
        return object

    @property
    def transmission_mode(self):
        return object

    @property
    def other_frequency(self):
        return object
