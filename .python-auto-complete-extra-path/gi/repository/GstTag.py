# -*- coding: utf-8 -*-
from gi.repository import Gst
TAG_CAPTURING_CONTRAST = r"""capturing-contrast"""
TAG_CAPTURING_DIGITAL_ZOOM_RATIO = r"""capturing-digital-zoom-ratio"""
TAG_CAPTURING_EXPOSURE_COMPENSATION = r"""capturing-exposure-compensation"""
TAG_CAPTURING_EXPOSURE_MODE = r"""capturing-exposure-mode"""
TAG_CAPTURING_EXPOSURE_PROGRAM = r"""capturing-exposure-program"""
TAG_CAPTURING_FLASH_FIRED = r"""capturing-flash-fired"""
TAG_CAPTURING_FLASH_MODE = r"""capturing-flash-mode"""
TAG_CAPTURING_FOCAL_LENGTH = r"""capturing-focal-length"""
TAG_CAPTURING_FOCAL_LENGTH_35_MM = r"""capturing-focal-length-35mm"""
TAG_CAPTURING_FOCAL_RATIO = r"""capturing-focal-ratio"""
TAG_CAPTURING_GAIN_ADJUSTMENT = r"""capturing-gain-adjustment"""
TAG_CAPTURING_ISO_SPEED = r"""capturing-iso-speed"""
TAG_CAPTURING_METERING_MODE = r"""capturing-metering-mode"""
TAG_CAPTURING_SATURATION = r"""capturing-saturation"""
TAG_CAPTURING_SCENE_CAPTURE_TYPE = r"""capturing-scene-capture-type"""
TAG_CAPTURING_SHARPNESS = r"""capturing-sharpness"""
TAG_CAPTURING_SHUTTER_SPEED = r"""capturing-shutter-speed"""
TAG_CAPTURING_SOURCE = r"""capturing-source"""
TAG_CAPTURING_WHITE_BALANCE = r"""capturing-white-balance"""
TAG_CDDA_CDDB_DISCID = r"""discid"""
TAG_CDDA_CDDB_DISCID_FULL = r"""discid-full"""
TAG_CDDA_MUSICBRAINZ_DISCID = r"""musicbrainz-discid"""
TAG_CDDA_MUSICBRAINZ_DISCID_FULL = r"""musicbrainz-discid-full"""
TAG_CMML_CLIP = r"""cmml-clip"""
TAG_CMML_HEAD = r"""cmml-head"""
TAG_CMML_STREAM = r"""cmml-stream"""
TAG_ID3V2_HEADER_SIZE = r"""10"""
TAG_IMAGE_HORIZONTAL_PPI = r"""image-horizontal-ppi"""
TAG_IMAGE_VERTICAL_PPI = r"""image-vertical-ppi"""
TAG_MUSICAL_KEY = r"""musical-key"""
TAG_MUSICBRAINZ_ALBUMARTISTID = r"""musicbrainz-albumartistid"""
TAG_MUSICBRAINZ_ALBUMID = r"""musicbrainz-albumid"""
TAG_MUSICBRAINZ_ARTISTID = r"""musicbrainz-artistid"""
TAG_MUSICBRAINZ_TRACKID = r"""musicbrainz-trackid"""
TAG_MUSICBRAINZ_TRMID = r"""musicbrainz-trmid"""


class TagDemuxResult:
    """"""
    BROKEN_TAG = 0
    AGAIN = 1
    OK = 2


class TagImageType:
    """"""
    NONE = -1
    UNDEFINED = 0
    FRONT_COVER = 1
    BACK_COVER = 2
    LEAFLET_PAGE = 3
    MEDIUM = 4
    LEAD_ARTIST = 5
    ARTIST = 6
    CONDUCTOR = 7
    BAND_ORCHESTRA = 8
    COMPOSER = 9
    LYRICIST = 10
    RECORDING_LOCATION = 11
    DURING_RECORDING = 12
    DURING_PERFORMANCE = 13
    VIDEO_CAPTURE = 14
    FISH = 15
    ILLUSTRATION = 16
    BAND_ARTIST_LOGO = 17
    PUBLISHER_STUDIO_LOGO = 18


class TagLicenseFlags:
    """"""
    PERMITS_REPRODUCTION = 1
    PERMITS_DISTRIBUTION = 2
    PERMITS_DERIVATIVE_WORKS = 4
    PERMITS_SHARING = 8
    REQUIRES_NOTICE = 256
    REQUIRES_ATTRIBUTION = 512
    REQUIRES_SHARE_ALIKE = 1024
    REQUIRES_SOURCE_CODE = 2048
    REQUIRES_COPYLEFT = 4096
    REQUIRES_LESSER_COPYLEFT = 8192
    PROHIBITS_COMMERCIAL_USE = 65536
    PROHIBITS_HIGH_INCOME_NATION_USE = 131072
    CREATIVE_COMMONS_LICENSE = 16777216
    FREE_SOFTWARE_FOUNDATION_LICENSE = 33554432

def tag_check_language_code(lang_code=None):
    """"""
    return object

def tag_freeform_string_to_utf8(data=None, size=None, env_vars=None):
    """"""
    return object

def tag_from_id3_tag(id3_tag=None):
    """"""
    return object

def tag_from_id3_user_tag(type=None, id3_user_tag=None):
    """"""
    return object

def tag_from_vorbis_tag(vorbis_tag=None):
    """"""
    return object

def tag_get_id3v2_tag_size(buffer=None):
    """"""
    return object

def tag_get_language_code_iso_639_1(lang_code=None):
    """"""
    return object

def tag_get_language_code_iso_639_2B(lang_code=None):
    """"""
    return object

def tag_get_language_code_iso_639_2T(lang_code=None):
    """"""
    return object

def tag_get_language_codes():
    """"""
    return object

def tag_get_language_name(language_code=None):
    """"""
    return object

def tag_get_license_description(license_ref=None):
    """"""
    return object

def tag_get_license_flags(license_ref=None):
    """"""
    return object

def tag_get_license_jurisdiction(license_ref=None):
    """"""
    return object

def tag_get_license_nick(license_ref=None):
    """"""
    return object

def tag_get_license_title(license_ref=None):
    """"""
    return object

def tag_get_license_version(license_ref=None):
    """"""
    return object

def tag_get_licenses():
    """"""
    return object

def tag_id3_genre_count():
    """"""
    return object

def tag_id3_genre_get(id=None):
    """"""
    return object

def tag_image_data_to_image_sample(image_data=None, image_data_len=None, image_type=None):
    """"""
    return object

def tag_list_add_id3_image(tag_list=None, image_data=None, image_data_len=None, id3_picture_type=None):
    """"""
    return object

def tag_list_from_exif_buffer(buffer=None, byte_order=None, base_offset=None):
    """"""
    return object

def tag_list_from_exif_buffer_with_tiff_header(buffer=None):
    """"""
    return object

def tag_list_from_id3v2_tag(buffer=None):
    """"""
    return object

def tag_list_from_vorbiscomment(data=None, size=None, id_data=None, id_data_length=None, vendor_string=None):
    """"""
    return object

def tag_list_from_vorbiscomment_buffer(buffer=None, id_data=None, id_data_length=None, vendor_string=None):
    """"""
    return object

def tag_list_from_xmp_buffer(buffer=None):
    """"""
    return object

def tag_list_new_from_id3v1(data=None):
    """"""
    return object

def tag_list_to_exif_buffer(taglist=None, byte_order=None, base_offset=None):
    """"""
    return object

def tag_list_to_exif_buffer_with_tiff_header(taglist=None):
    """"""
    return object

def tag_list_to_vorbiscomment_buffer(list=None, id_data=None, id_data_length=None, vendor_string=None):
    """"""
    return object

def tag_list_to_xmp_buffer(list=None, read_only=None, schemas=None):
    """"""
    return object

def tag_parse_extended_comment(ext_comment=None, key=None, lang=None, value=None, fail_if_no_key=None):
    """"""
    return object

def tag_register_musicbrainz_tags():
    """"""
    return object

def tag_to_id3_tag(gst_tag=None):
    """"""
    return object

def tag_to_vorbis_comments(list=None, tag=None):
    """"""
    return object

def tag_to_vorbis_tag(gst_tag=None):
    """"""
    return object

def tag_xmp_list_schemas():
    """"""
    return object

def vorbis_tag_add(list=None, tag=None, value=None):
    """"""
    return object


class TagDemux(Gst.Element):
    """"""
    
    def identify_tag(self, buffer=None, start_tag=None, tag_size=None):
        """"""
        return object
    
    def merge_tags(self, start_tags=None, end_tags=None):
        """"""
        return object
    
    def parse_tag(self, buffer=None, start_tag=None, tag_size=None, tags=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def reserved(self):
        return object


class TagDemuxClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def min_start_size(self):
        return object

    @property
    def min_end_size(self):
        return object

    @property
    def identify_tag(self):
        return object

    @property
    def parse_tag(self):
        return object

    @property
    def merge_tags(self):
        return object

    @property
    def reserved(self):
        return object


class TagDemuxPrivate():
    """"""


class TagMux(Gst.Element, Gst.TagSetter):
    """"""
    
    def render_end_tag(self, tag_list=None):
        """"""
        return object
    
    def render_start_tag(self, tag_list=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TagMuxClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def render_start_tag(self):
        return object

    @property
    def render_end_tag(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class TagMuxPrivate():
    """"""


class TagXmpWriter():
    """"""
    
    def add_all_schemas(self):
        """"""
        return object
    
    def add_schema(self, schema=None):
        """"""
        return object
    
    def has_schema(self, schema=None):
        """"""
        return object
    
    def remove_all_schemas(self):
        """"""
        return object
    
    def remove_schema(self, schema=None):
        """"""
        return object
    
    def tag_list_to_xmp_buffer(self, taglist=None, read_only=None):
        """"""
        return object


class TagXmpWriterInterface():
    """"""

    @property
    def parent(self):
        return object
