# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import Gst


class AudioVisualizerShader:
    """"""
    NONE = 0
    FADE = 1
    FADE_AND_MOVE_UP = 2
    FADE_AND_MOVE_DOWN = 3
    FADE_AND_MOVE_LEFT = 4
    FADE_AND_MOVE_RIGHT = 5
    FADE_AND_MOVE_HORIZ_OUT = 6
    FADE_AND_MOVE_HORIZ_IN = 7
    FADE_AND_MOVE_VERT_OUT = 8
    FADE_AND_MOVE_VERT_IN = 9


class DiscovererResult:
    """"""
    OK = 0
    URI_INVALID = 1
    ERROR = 2
    TIMEOUT = 3
    BUSY = 4
    MISSING_PLUGINS = 5


class DiscovererSerializeFlags:
    """"""
    BASIC = 0
    CAPS = 1
    TAGS = 2
    MISC = 4
    ALL = 7
ENCODING_CATEGORY_CAPTURE = r"""capture"""
ENCODING_CATEGORY_DEVICE = r"""device"""
ENCODING_CATEGORY_FILE_EXTENSION = r"""file-extension"""
ENCODING_CATEGORY_ONLINE_SERVICE = r"""online-service"""
ENCODING_CATEGORY_STORAGE_EDITING = r"""storage-editing"""


class InstallPluginsReturn:
    """"""
    SUCCESS = 0
    NOT_FOUND = 1
    ERROR = 2
    PARTIAL_SUCCESS = 3
    USER_ABORT = 4
    CRASHED = 100
    INVALID = 101
    STARTED_OK = 200
    INTERNAL_FAILURE = 201
    HELPER_MISSING = 202
    INSTALL_IN_PROGRESS = 203
PLUGINS_BASE_VERSION_MAJOR = r"""1"""
PLUGINS_BASE_VERSION_MICRO = r"""5"""
PLUGINS_BASE_VERSION_MINOR = r"""14"""
PLUGINS_BASE_VERSION_NANO = r"""0"""

def codec_utils_aac_caps_set_level_and_profile(caps=None, audio_config=None, len=None):
    """"""
    return object

def codec_utils_aac_get_channels(audio_config=None, len=None):
    """"""
    return object

def codec_utils_aac_get_index_from_sample_rate(rate=None):
    """"""
    return object

def codec_utils_aac_get_level(audio_config=None, len=None):
    """"""
    return object

def codec_utils_aac_get_profile(audio_config=None, len=None):
    """"""
    return object

def codec_utils_aac_get_sample_rate(audio_config=None, len=None):
    """"""
    return object

def codec_utils_aac_get_sample_rate_from_index(sr_idx=None):
    """"""
    return object

def codec_utils_h264_caps_set_level_and_profile(caps=None, sps=None, len=None):
    """"""
    return object

def codec_utils_h264_get_level(sps=None, len=None):
    """"""
    return object

def codec_utils_h264_get_level_idc(level=None):
    """"""
    return object

def codec_utils_h264_get_profile(sps=None, len=None):
    """"""
    return object

def codec_utils_h265_caps_set_level_tier_and_profile(caps=None, profile_tier_level=None, len=None):
    """"""
    return object

def codec_utils_h265_get_level(profile_tier_level=None, len=None):
    """"""
    return object

def codec_utils_h265_get_level_idc(level=None):
    """"""
    return object

def codec_utils_h265_get_profile(profile_tier_level=None, len=None):
    """"""
    return object

def codec_utils_h265_get_tier(profile_tier_level=None, len=None):
    """"""
    return object

def codec_utils_mpeg4video_caps_set_level_and_profile(caps=None, vis_obj_seq=None, len=None):
    """"""
    return object

def codec_utils_mpeg4video_get_level(vis_obj_seq=None, len=None):
    """"""
    return object

def codec_utils_mpeg4video_get_profile(vis_obj_seq=None, len=None):
    """"""
    return object

def codec_utils_opus_create_caps(rate=None, channels=None, channel_mapping_family=None, stream_count=None, coupled_count=None, channel_mapping=None):
    """"""
    return object

def codec_utils_opus_create_caps_from_header(header=None, comments=None):
    """"""
    return object

def codec_utils_opus_create_header(rate=None, channels=None, channel_mapping_family=None, stream_count=None, coupled_count=None, channel_mapping=None, pre_skip=None, output_gain=None):
    """"""
    return object

def codec_utils_opus_parse_caps(caps=None, rate=None, channels=None, channel_mapping_family=None, stream_count=None, coupled_count=None, channel_mapping=None):
    """"""
    return object

def codec_utils_opus_parse_header(header=None, rate=None, channels=None, channel_mapping_family=None, stream_count=None, coupled_count=None, channel_mapping=None, pre_skip=None, output_gain=None):
    """"""
    return object

def encoding_list_all_targets(categoryname=None):
    """"""
    return object

def encoding_list_available_categories():
    """"""
    return object

def install_plugins_async(details=None, ctx=None, func=None, user_data=None):
    """"""
    return object

def install_plugins_installation_in_progress():
    """"""
    return object

def install_plugins_return_get_name(ret=None):
    """"""
    return object

def install_plugins_supported():
    """"""
    return object

def install_plugins_sync(details=None, ctx=None):
    """"""
    return object

def is_missing_plugin_message(msg=None):
    """"""
    return object

def missing_decoder_installer_detail_new(decode_caps=None):
    """"""
    return object

def missing_decoder_message_new(element=None, decode_caps=None):
    """"""
    return object

def missing_element_installer_detail_new(factory_name=None):
    """"""
    return object

def missing_element_message_new(element=None, factory_name=None):
    """"""
    return object

def missing_encoder_installer_detail_new(encode_caps=None):
    """"""
    return object

def missing_encoder_message_new(element=None, encode_caps=None):
    """"""
    return object

def missing_plugin_message_get_description(msg=None):
    """"""
    return object

def missing_plugin_message_get_installer_detail(msg=None):
    """"""
    return object

def missing_uri_sink_installer_detail_new(protocol=None):
    """"""
    return object

def missing_uri_sink_message_new(element=None, protocol=None):
    """"""
    return object

def missing_uri_source_installer_detail_new(protocol=None):
    """"""
    return object

def missing_uri_source_message_new(element=None, protocol=None):
    """"""
    return object

def pb_utils_add_codec_description_to_tag_list(taglist=None, codec_tag=None, caps=None):
    """"""
    return object

def pb_utils_get_codec_description(caps=None):
    """"""
    return object

def pb_utils_get_decoder_description(caps=None):
    """"""
    return object

def pb_utils_get_element_description(factory_name=None):
    """"""
    return object

def pb_utils_get_encoder_description(caps=None):
    """"""
    return object

def pb_utils_get_sink_description(protocol=None):
    """"""
    return object

def pb_utils_get_source_description(protocol=None):
    """"""
    return object

def pb_utils_init():
    """"""
    return object

def plugins_base_version(major=None, minor=None, micro=None, nano=None):
    """"""
    return object

def plugins_base_version_string():
    """"""
    return object


class AudioVisualizer(Gst.Element):
    """"""
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def render(self, audio=None, video=None):
        """"""
        return object
    
    def setup(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def req_spf(self):
        return object

    @property
    def vinfo(self):
        return object

    @property
    def ainfo(self):
        return object

    @property
    def priv(self):
        return object


class AudioVisualizerClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def setup(self):
        return object

    @property
    def render(self):
        return object

    @property
    def decide_allocation(self):
        return object


class AudioVisualizerPrivate():
    """"""


class Discoverer(GObject.Object):
    """"""
    
    def __init__(self, timeout=None):
        """"""
        return object
    @staticmethod
    def new(timeout=None):
        """"""
        return object
    
    def discovered(self, info=None, err=None):
        """"""
        return object
    
    def finished(self):
        """"""
        return object
    
    def source_setup(self, source=None):
        """"""
        return object
    
    def starting(self):
        """"""
        return object
    
    def discover_uri(self, uri=None):
        """"""
        return object
    
    def discover_uri_async(self, uri=None):
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
    def _reserved(self):
        return object


class DiscovererClass():
    """"""

    @property
    def parentclass(self):
        return object

    @property
    def finished(self):
        return object

    @property
    def starting(self):
        return object

    @property
    def discovered(self):
        return object

    @property
    def source_setup(self):
        return object

    @property
    def _reserved(self):
        return object


class DiscovererInfo(GObject.Object):
    """"""
    @staticmethod
    def from_variant(variant=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def get_audio_streams(self):
        """"""
        return object
    
    def get_container_streams(self):
        """"""
        return object
    
    def get_duration(self):
        """"""
        return object
    
    def get_live(self):
        """"""
        return object
    
    def get_misc(self):
        """"""
        return object
    
    def get_missing_elements_installer_details(self):
        """"""
        return object
    
    def get_result(self):
        """"""
        return object
    
    def get_seekable(self):
        """"""
        return object
    
    def get_stream_info(self):
        """"""
        return object
    
    def get_stream_list(self):
        """"""
        return object
    
    def get_streams(self, streamtype=None):
        """"""
        return object
    
    def get_subtitle_streams(self):
        """"""
        return object
    
    def get_tags(self):
        """"""
        return object
    
    def get_toc(self):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_video_streams(self):
        """"""
        return object
    
    def to_variant(self, flags=None):
        """"""
        return object


class DiscovererPrivate():
    """"""


class DiscovererStreamInfo(GObject.Object):
    """"""
    @staticmethod
    def list_free(infos=None):
        """"""
        return object
    
    def get_caps(self):
        """"""
        return object
    
    def get_misc(self):
        """"""
        return object
    
    def get_next(self):
        """"""
        return object
    
    def get_previous(self):
        """"""
        return object
    
    def get_stream_id(self):
        """"""
        return object
    
    def get_stream_type_nick(self):
        """"""
        return object
    
    def get_tags(self):
        """"""
        return object
    
    def get_toc(self):
        """"""
        return object


class DiscovererSubtitleInfo(DiscovererStreamInfo):
    """"""
    
    def get_language(self):
        """"""
        return object


class DiscovererVideoInfo(DiscovererStreamInfo):
    """"""
    
    def get_bitrate(self):
        """"""
        return object
    
    def get_depth(self):
        """"""
        return object
    
    def get_framerate_denom(self):
        """"""
        return object
    
    def get_framerate_num(self):
        """"""
        return object
    
    def get_height(self):
        """"""
        return object
    
    def get_max_bitrate(self):
        """"""
        return object
    
    def get_par_denom(self):
        """"""
        return object
    
    def get_par_num(self):
        """"""
        return object
    
    def get_width(self):
        """"""
        return object
    
    def is_image(self):
        """"""
        return object
    
    def is_interlaced(self):
        """"""
        return object


class EncodingAudioProfileClass():
    """"""


class EncodingContainerProfileClass():
    """"""


class EncodingProfile(GObject.Object):
    """"""
    @staticmethod
    def find(targetname=None, profilename=None, category=None):
        """"""
        return object
    @staticmethod
    def from_discoverer(info=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def get_allow_dynamic_output(self):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_file_extension(self):
        """"""
        return object
    
    def get_format(self):
        """"""
        return object
    
    def get_input_caps(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_presence(self):
        """"""
        return object
    
    def get_preset(self):
        """"""
        return object
    
    def get_preset_name(self):
        """"""
        return object
    
    def get_restriction(self):
        """"""
        return object
    
    def get_type_nick(self):
        """"""
        return object
    
    def is_enabled(self):
        """"""
        return object
    
    def is_equal(self, b=None):
        """"""
        return object
    
    def set_allow_dynamic_output(self, allow_dynamic_output=None):
        """"""
        return object
    
    def set_description(self, description=None):
        """"""
        return object
    
    def set_enabled(self, enabled=None):
        """"""
        return object
    
    def set_format(self, format=None):
        """"""
        return object
    
    def set_name(self, name=None):
        """"""
        return object
    
    def set_presence(self, presence=None):
        """"""
        return object
    
    def set_preset(self, preset=None):
        """"""
        return object
    
    def set_preset_name(self, preset_name=None):
        """"""
        return object
    
    def set_restriction(self, restriction=None):
        """"""
        return object


class EncodingProfileClass():
    """"""


class EncodingTarget(GObject.Object):
    """"""
    
    def __init__(self, name=None, category=None, description=None, profiles=None):
        """"""
        return object
    @staticmethod
    def new(name=None, category=None, description=None, profiles=None):
        """"""
        return object
    @staticmethod
    def load(name=None, category=None):
        """"""
        return object
    @staticmethod
    def load_from_file(filepath=None):
        """"""
        return object
    
    def add_profile(self, profile=None):
        """"""
        return object
    
    def get_category(self):
        """"""
        return object
    
    def get_description(self):
        """"""
        return object
    
    def get_name(self):
        """"""
        return object
    
    def get_profile(self, name=None):
        """"""
        return object
    
    def get_profiles(self):
        """"""
        return object
    
    def save(self):
        """"""
        return object
    
    def save_to_file(self, filepath=None):
        """"""
        return object


class EncodingVideoProfile(EncodingProfile):
    """"""
    
    def __init__(self, format=None, preset=None, restriction=None, presence=None):
        """"""
        return object
    @staticmethod
    def new(format=None, preset=None, restriction=None, presence=None):
        """"""
        return object
    
    def get_pass(self):
        """"""
        return object
    
    def get_variableframerate(self):
        """"""
        return object
    
    def set_pass(self, _pass=None):
        """"""
        return object
    
    def set_variableframerate(self, variableframerate=None):
        """"""
        return object


class EncodingVideoProfileClass():
    """"""


class InstallPluginsContext():
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
    
    def set_confirm_search(self, confirm_search=None):
        """"""
        return object
    
    def set_desktop_id(self, desktop_id=None):
        """"""
        return object
    
    def set_startup_notification_id(self, startup_id=None):
        """"""
        return object
    
    def set_xid(self, xid=None):
        """"""
        return object


class DiscovererAudioInfo(DiscovererStreamInfo):
    """"""
    
    def get_bitrate(self):
        """"""
        return object
    
    def get_channel_mask(self):
        """"""
        return object
    
    def get_channels(self):
        """"""
        return object
    
    def get_depth(self):
        """"""
        return object
    
    def get_language(self):
        """"""
        return object
    
    def get_max_bitrate(self):
        """"""
        return object
    
    def get_sample_rate(self):
        """"""
        return object


class DiscovererContainerInfo(DiscovererStreamInfo):
    """"""
    
    def get_streams(self):
        """"""
        return object


class EncodingAudioProfile(EncodingProfile):
    """"""
    
    def __init__(self, format=None, preset=None, restriction=None, presence=None):
        """"""
        return object
    @staticmethod
    def new(format=None, preset=None, restriction=None, presence=None):
        """"""
        return object


class EncodingContainerProfile(EncodingProfile):
    """"""
    
    def __init__(self, name=None, description=None, format=None, preset=None):
        """"""
        return object
    @staticmethod
    def new(name=None, description=None, format=None, preset=None):
        """"""
        return object
    
    def add_profile(self, profile=None):
        """"""
        return object
    
    def contains_profile(self, profile=None):
        """"""
        return object
    
    def get_profiles(self):
        """"""
        return object
