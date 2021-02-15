# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import Gst
from gi.repository import GstBase
BUFFER_POOL_OPTION_VIDEO_AFFINE_TRANSFORMATION_META = r"""GstBufferPoolOptionVideoAffineTransformation"""
BUFFER_POOL_OPTION_VIDEO_ALIGNMENT = r"""GstBufferPoolOptionVideoAlignment"""
BUFFER_POOL_OPTION_VIDEO_GL_TEXTURE_UPLOAD_META = r"""GstBufferPoolOptionVideoGLTextureUploadMeta"""
BUFFER_POOL_OPTION_VIDEO_META = r"""GstBufferPoolOptionVideoMeta"""
CAPS_FEATURE_META_GST_VIDEO_AFFINE_TRANSFORMATION_META = r"""meta:GstVideoAffineTransformation"""
CAPS_FEATURE_META_GST_VIDEO_GL_TEXTURE_UPLOAD_META = r"""meta:GstVideoGLTextureUploadMeta"""
CAPS_FEATURE_META_GST_VIDEO_META = r"""meta:GstVideoMeta"""
CAPS_FEATURE_META_GST_VIDEO_OVERLAY_COMPOSITION = r"""meta:GstVideoOverlayComposition"""


class ColorBalanceType:
    """"""
    HARDWARE = 0
    SOFTWARE = 1
META_TAG_VIDEO_COLORSPACE_STR = r"""colorspace"""
META_TAG_VIDEO_ORIENTATION_STR = r"""orientation"""
META_TAG_VIDEO_SIZE_STR = r"""size"""
META_TAG_VIDEO_STR = r"""video"""


class NavigationCommand:
    """"""
    INVALID = 0
    MENU1 = 1
    MENU2 = 2
    MENU3 = 3
    MENU4 = 4
    MENU5 = 5
    MENU6 = 6
    MENU7 = 7
    LEFT = 20
    RIGHT = 21
    UP = 22
    DOWN = 23
    ACTIVATE = 24
    PREV_ANGLE = 30
    NEXT_ANGLE = 31


class NavigationEventType:
    """"""
    INVALID = 0
    KEY_PRESS = 1
    KEY_RELEASE = 2
    MOUSE_BUTTON_PRESS = 3
    MOUSE_BUTTON_RELEASE = 4
    MOUSE_MOVE = 5
    COMMAND = 6


class NavigationMessageType:
    """"""
    INVALID = 0
    MOUSE_OVER = 1
    COMMANDS_CHANGED = 2
    ANGLES_CHANGED = 3
    EVENT = 4


class NavigationQueryType:
    """"""
    INVALID = 0
    COMMANDS = 1
    ANGLES = 2
VIDEO_COLORIMETRY_BT2020 = r"""bt2020"""
VIDEO_COLORIMETRY_BT601 = r"""bt601"""
VIDEO_COLORIMETRY_BT709 = r"""bt709"""
VIDEO_COLORIMETRY_SMPTE240M = r"""smpte240m"""
VIDEO_COLORIMETRY_SRGB = r"""sRGB"""
VIDEO_COMP_A = r"""3"""
VIDEO_COMP_B = r"""2"""
VIDEO_COMP_G = r"""1"""
VIDEO_COMP_INDEX = r"""0"""
VIDEO_COMP_PALETTE = r"""1"""
VIDEO_COMP_R = r"""0"""
VIDEO_COMP_U = r"""1"""
VIDEO_COMP_V = r"""2"""
VIDEO_COMP_Y = r"""0"""
VIDEO_CONVERTER_OPT_ALPHA_MODE = r"""GstVideoConverter.alpha-mode"""
VIDEO_CONVERTER_OPT_ALPHA_VALUE = r"""GstVideoConverter.alpha-value"""
VIDEO_CONVERTER_OPT_BORDER_ARGB = r"""GstVideoConverter.border-argb"""
VIDEO_CONVERTER_OPT_CHROMA_MODE = r"""GstVideoConverter.chroma-mode"""
VIDEO_CONVERTER_OPT_CHROMA_RESAMPLER_METHOD = r"""GstVideoConverter.chroma-resampler-method"""
VIDEO_CONVERTER_OPT_DEST_HEIGHT = r"""GstVideoConverter.dest-height"""
VIDEO_CONVERTER_OPT_DEST_WIDTH = r"""GstVideoConverter.dest-width"""
VIDEO_CONVERTER_OPT_DEST_X = r"""GstVideoConverter.dest-x"""
VIDEO_CONVERTER_OPT_DEST_Y = r"""GstVideoConverter.dest-y"""
VIDEO_CONVERTER_OPT_DITHER_METHOD = r"""GstVideoConverter.dither-method"""
VIDEO_CONVERTER_OPT_DITHER_QUANTIZATION = r"""GstVideoConverter.dither-quantization"""
VIDEO_CONVERTER_OPT_FILL_BORDER = r"""GstVideoConverter.fill-border"""
VIDEO_CONVERTER_OPT_GAMMA_MODE = r"""GstVideoConverter.gamma-mode"""
VIDEO_CONVERTER_OPT_MATRIX_MODE = r"""GstVideoConverter.matrix-mode"""
VIDEO_CONVERTER_OPT_PRIMARIES_MODE = r"""GstVideoConverter.primaries-mode"""
VIDEO_CONVERTER_OPT_RESAMPLER_METHOD = r"""GstVideoConverter.resampler-method"""
VIDEO_CONVERTER_OPT_RESAMPLER_TAPS = r"""GstVideoConverter.resampler-taps"""
VIDEO_CONVERTER_OPT_SRC_HEIGHT = r"""GstVideoConverter.src-height"""
VIDEO_CONVERTER_OPT_SRC_WIDTH = r"""GstVideoConverter.src-width"""
VIDEO_CONVERTER_OPT_SRC_X = r"""GstVideoConverter.src-x"""
VIDEO_CONVERTER_OPT_SRC_Y = r"""GstVideoConverter.src-y"""
VIDEO_CONVERTER_OPT_THREADS = r"""GstVideoConverter.threads"""
VIDEO_DECODER_MAX_ERRORS = r"""10"""
VIDEO_DECODER_SINK_NAME = r"""sink"""
VIDEO_DECODER_SRC_NAME = r"""src"""
VIDEO_ENCODER_SINK_NAME = r"""sink"""
VIDEO_ENCODER_SRC_NAME = r"""src"""
VIDEO_FORMATS_ALL = r"""{ I420, YV12, YUY2, UYVY, AYUV, RGBx, BGRx, xRGB, xBGR, RGBA, BGRA, ARGB, ABGR, RGB, BGR, Y41B, Y42B, YVYU, Y444, v210, v216, NV12, NV21, GRAY8, GRAY16_BE, GRAY16_LE, v308, RGB16, BGR16, RGB15, BGR15, UYVP, A420, RGB8P, YUV9, YVU9, IYU1, ARGB64, AYUV64, r210, I420_10BE, I420_10LE, I422_10BE, I422_10LE, Y444_10BE, Y444_10LE, GBR, GBR_10BE, GBR_10LE, NV16, NV24, NV12_64Z32, A420_10BE, A420_10LE, A422_10BE, A422_10LE, A444_10BE, A444_10LE, NV61, P010_10BE, P010_10LE, IYU2, VYUY, GBRA, GBRA_10BE, GBRA_10LE, GBR_12BE, GBR_12LE, GBRA_12BE, GBRA_12LE, I420_12BE, I420_12LE, I422_12BE, I422_12LE, Y444_12BE, Y444_12LE, GRAY10_LE32, NV12_10LE32, NV16_10LE32 }"""
VIDEO_FPS_RANGE = r"""(fraction) [ 0, max ]"""
VIDEO_MAX_COMPONENTS = r"""4"""
VIDEO_MAX_PLANES = r"""4"""
VIDEO_OVERLAY_COMPOSITION_BLEND_FORMATS = r"""{ BGRx, RGBx, xRGB, xBGR, RGBA, BGRA, ARGB, ABGR, RGB, BGR, I420, YV12, AYUV, YUY2, UYVY, v308, Y41B, Y42B, Y444, NV12, NV21, A420, YUV9, YVU9, IYU1, GRAY8 }"""
VIDEO_RESAMPLER_OPT_CUBIC_B = r"""GstVideoResampler.cubic-b"""
VIDEO_RESAMPLER_OPT_CUBIC_C = r"""GstVideoResampler.cubic-c"""
VIDEO_RESAMPLER_OPT_ENVELOPE = r"""GstVideoResampler.envelope"""
VIDEO_RESAMPLER_OPT_MAX_TAPS = r"""GstVideoResampler.max-taps"""
VIDEO_RESAMPLER_OPT_SHARPEN = r"""GstVideoResampler.sharpen"""
VIDEO_RESAMPLER_OPT_SHARPNESS = r"""GstVideoResampler.sharpness"""
VIDEO_SCALER_OPT_DITHER_METHOD = r"""GstVideoScaler.dither-method"""
VIDEO_SIZE_RANGE = r"""(int) [ 1, max ]"""
VIDEO_TILE_TYPE_MASK = r"""65535"""
VIDEO_TILE_TYPE_SHIFT = r"""16"""
VIDEO_TILE_X_TILES_MASK = r"""65535"""
VIDEO_TILE_Y_TILES_SHIFT = r"""16"""


class VideoAlphaMode:
    """"""
    COPY = 0
    SET = 1
    MULT = 2


class VideoBufferFlags:
    """"""
    INTERLACED = 1048576
    TFF = 2097152
    RFF = 4194304
    ONEFIELD = 8388608
    MULTIPLE_VIEW = 16777216
    FIRST_IN_BUNDLE = 33554432
    LAST = 268435456


class VideoChromaFlags:
    """"""
    NONE = 0
    INTERLACED = 1


class VideoChromaMethod:
    """"""
    NEAREST = 0
    LINEAR = 1


class VideoChromaMode:
    """"""
    FULL = 0
    UPSAMPLE_ONLY = 1
    DOWNSAMPLE_ONLY = 2
    NONE = 3


class VideoChromaSite:
    """"""
    UNKNOWN = 0
    NONE = 1
    H_COSITED = 2
    V_COSITED = 4
    ALT_LINE = 8
    COSITED = 6
    JPEG = 1
    MPEG2 = 2
    DV = 14


class VideoCodecFrameFlags:
    """"""
    DECODE_ONLY = 1
    SYNC_POINT = 2
    FORCE_KEYFRAME = 4
    FORCE_KEYFRAME_HEADERS = 8


class VideoColorMatrix:
    """"""
    UNKNOWN = 0
    RGB = 1
    FCC = 2
    BT709 = 3
    BT601 = 4
    SMPTE240M = 5
    BT2020 = 6


class VideoColorPrimaries:
    """"""
    UNKNOWN = 0
    BT709 = 1
    BT470M = 2
    BT470BG = 3
    SMPTE170M = 4
    SMPTE240M = 5
    FILM = 6
    BT2020 = 7
    ADOBERGB = 8


class VideoColorRange:
    """"""
    UNKNOWN = 0
    _0_255 = 1
    _16_235 = 2


class VideoDitherFlags:
    """"""
    NONE = 0
    INTERLACED = 1
    QUANTIZE = 2


class VideoDitherMethod:
    """"""
    NONE = 0
    VERTERR = 1
    FLOYD_STEINBERG = 2
    SIERRA_LITE = 3
    BAYER = 4


class VideoFieldOrder:
    """"""
    UNKNOWN = 0
    TOP_FIELD_FIRST = 1
    BOTTOM_FIELD_FIRST = 2


class VideoFlags:
    """"""
    NONE = 0
    VARIABLE_FPS = 1
    PREMULTIPLIED_ALPHA = 2


class VideoFormat:
    """"""
    UNKNOWN = 0
    ENCODED = 1
    I420 = 2
    YV12 = 3
    YUY2 = 4
    UYVY = 5
    AYUV = 6
    RGBX = 7
    BGRX = 8
    XRGB = 9
    XBGR = 10
    RGBA = 11
    BGRA = 12
    ARGB = 13
    ABGR = 14
    RGB = 15
    BGR = 16
    Y41B = 17
    Y42B = 18
    YVYU = 19
    Y444 = 20
    V210 = 21
    V216 = 22
    NV12 = 23
    NV21 = 24
    GRAY8 = 25
    GRAY16_BE = 26
    GRAY16_LE = 27
    V308 = 28
    RGB16 = 29
    BGR16 = 30
    RGB15 = 31
    BGR15 = 32
    UYVP = 33
    A420 = 34
    RGB8P = 35
    YUV9 = 36
    YVU9 = 37
    IYU1 = 38
    ARGB64 = 39
    AYUV64 = 40
    R210 = 41
    I420_10BE = 42
    I420_10LE = 43
    I422_10BE = 44
    I422_10LE = 45
    Y444_10BE = 46
    Y444_10LE = 47
    GBR = 48
    GBR_10BE = 49
    GBR_10LE = 50
    NV16 = 51
    NV24 = 52
    NV12_64Z32 = 53
    A420_10BE = 54
    A420_10LE = 55
    A422_10BE = 56
    A422_10LE = 57
    A444_10BE = 58
    A444_10LE = 59
    NV61 = 60
    P010_10BE = 61
    P010_10LE = 62
    IYU2 = 63
    VYUY = 64
    GBRA = 65
    GBRA_10BE = 66
    GBRA_10LE = 67
    GBR_12BE = 68
    GBR_12LE = 69
    GBRA_12BE = 70
    GBRA_12LE = 71
    I420_12BE = 72
    I420_12LE = 73
    I422_12BE = 74
    I422_12LE = 75
    Y444_12BE = 76
    Y444_12LE = 77
    GRAY10_LE32 = 78
    NV12_10LE32 = 79
    NV16_10LE32 = 80


class VideoFormatFlags:
    """"""
    YUV = 1
    RGB = 2
    GRAY = 4
    ALPHA = 8
    LE = 16
    PALETTE = 32
    COMPLEX = 64
    UNPACK = 128
    TILED = 256


class VideoFrameFlags:
    """"""
    NONE = 0
    INTERLACED = 1
    TFF = 2
    RFF = 4
    ONEFIELD = 8
    MULTIPLE_VIEW = 16
    FIRST_IN_BUNDLE = 32


class VideoFrameMapFlags:
    """"""
    NO_REF = 65536
    LAST = 16777216


class VideoGLTextureOrientation:
    """"""
    NORMAL_Y_NORMAL = 0
    NORMAL_Y_FLIP = 1
    FLIP_Y_NORMAL = 2
    FLIP_Y_FLIP = 3


class VideoGLTextureType:
    """"""
    LUMINANCE = 0
    LUMINANCE_ALPHA = 1
    RGB16 = 2
    RGB = 3
    RGBA = 4
    R = 5
    RG = 6


class VideoGammaMode:
    """"""
    NONE = 0
    REMAP = 1


class VideoInterlaceMode:
    """"""
    PROGRESSIVE = 0
    INTERLEAVED = 1
    MIXED = 2
    FIELDS = 3


class VideoMatrixMode:
    """"""
    FULL = 0
    INPUT_ONLY = 1
    OUTPUT_ONLY = 2
    NONE = 3


class VideoMultiviewFlags:
    """"""
    NONE = 0
    RIGHT_VIEW_FIRST = 1
    LEFT_FLIPPED = 2
    LEFT_FLOPPED = 4
    RIGHT_FLIPPED = 8
    RIGHT_FLOPPED = 16
    HALF_ASPECT = 16384
    MIXED_MONO = 32768


class VideoMultiviewFramePacking:
    """"""
    NONE = -1
    MONO = 0
    LEFT = 1
    RIGHT = 2
    SIDE_BY_SIDE = 3
    SIDE_BY_SIDE_QUINCUNX = 4
    COLUMN_INTERLEAVED = 5
    ROW_INTERLEAVED = 6
    TOP_BOTTOM = 7
    CHECKERBOARD = 8


class VideoMultiviewMode:
    """"""
    NONE = -1
    MONO = 0
    LEFT = 1
    RIGHT = 2
    SIDE_BY_SIDE = 3
    SIDE_BY_SIDE_QUINCUNX = 4
    COLUMN_INTERLEAVED = 5
    ROW_INTERLEAVED = 6
    TOP_BOTTOM = 7
    CHECKERBOARD = 8
    FRAME_BY_FRAME = 32
    MULTIVIEW_FRAME_BY_FRAME = 33
    SEPARATED = 34


class VideoOrientationMethod:
    """"""
    IDENTITY = 0
    _90R = 1
    _180 = 2
    _90L = 3
    HORIZ = 4
    VERT = 5
    UL_LR = 6
    UR_LL = 7
    AUTO = 8
    CUSTOM = 9


class VideoOverlayFormatFlags:
    """"""
    NONE = 0
    PREMULTIPLIED_ALPHA = 1
    GLOBAL_ALPHA = 2


class VideoPackFlags:
    """"""
    NONE = 0
    TRUNCATE_RANGE = 1
    INTERLACED = 2


class VideoPrimariesMode:
    """"""
    NONE = 0
    MERGE_ONLY = 1
    FAST = 2


class VideoResamplerFlags:
    """"""
    NONE = 0
    HALF_TAPS = 1


class VideoResamplerMethod:
    """"""
    NEAREST = 0
    LINEAR = 1
    CUBIC = 2
    SINC = 3
    LANCZOS = 4


class VideoScalerFlags:
    """"""
    NONE = 0
    INTERLACED = 1


class VideoTileMode:
    """"""
    UNKNOWN = 0
    ZFLIPZ_2X2 = 65536


class VideoTileType:
    """"""
    INDEXED = 0


class VideoTimeCodeFlags:
    """"""
    NONE = 0
    DROP_FRAME = 1
    INTERLACED = 2


class VideoTransferFunction:
    """"""
    UNKNOWN = 0
    GAMMA10 = 1
    GAMMA18 = 2
    GAMMA20 = 3
    GAMMA22 = 4
    BT709 = 5
    SMPTE240M = 6
    SRGB = 7
    GAMMA28 = 8
    LOG100 = 9
    LOG316 = 10
    BT2020_12 = 11
    ADOBERGB = 12

def buffer_add_video_affine_transformation_meta(buffer=None):
    """"""
    return object

def buffer_add_video_gl_texture_upload_meta(buffer=None, texture_orientation=None, n_textures=None, texture_type=None, upload=None, user_data=None, user_data_copy=None, user_data_free=None):
    """"""
    return object

def buffer_add_video_meta(buffer=None, flags=None, format=None, width=None, height=None):
    """"""
    return object

def buffer_add_video_meta_full(buffer=None, flags=None, format=None, width=None, height=None, n_planes=None, offset=None, stride=None):
    """"""
    return object

def buffer_add_video_overlay_composition_meta(buf=None, comp=None):
    """"""
    return object

def buffer_add_video_region_of_interest_meta(buffer=None, roi_type=None, x=None, y=None, w=None, h=None):
    """"""
    return object

def buffer_add_video_region_of_interest_meta_id(buffer=None, roi_type=None, x=None, y=None, w=None, h=None):
    """"""
    return object

def buffer_add_video_time_code_meta(buffer=None, tc=None):
    """"""
    return object

def buffer_add_video_time_code_meta_full(buffer=None, fps_n=None, fps_d=None, latest_daily_jam=None, flags=None, hours=None, minutes=None, seconds=None, frames=None, field_count=None):
    """"""
    return object

def buffer_get_video_meta(buffer=None):
    """"""
    return object

def buffer_get_video_meta_id(buffer=None, id=None):
    """"""
    return object

def buffer_get_video_region_of_interest_meta_id(buffer=None, id=None):
    """"""
    return object

def buffer_pool_config_get_video_alignment(config=None, align=None):
    """"""
    return object

def buffer_pool_config_set_video_alignment(config=None, align=None):
    """"""
    return object

def is_video_overlay_prepare_window_handle_message(msg=None):
    """"""
    return object

def navigation_event_get_type(event=None):
    """"""
    return object

def navigation_event_parse_command(event=None, command=None):
    """"""
    return object

def navigation_event_parse_key_event(event=None, key=None):
    """"""
    return object

def navigation_event_parse_mouse_button_event(event=None, button=None, x=None, y=None):
    """"""
    return object

def navigation_event_parse_mouse_move_event(event=None, x=None, y=None):
    """"""
    return object

def navigation_message_get_type(message=None):
    """"""
    return object

def navigation_message_new_angles_changed(src=None, cur_angle=None, n_angles=None):
    """"""
    return object

def navigation_message_new_commands_changed(src=None):
    """"""
    return object

def navigation_message_new_event(src=None, event=None):
    """"""
    return object

def navigation_message_new_mouse_over(src=None, active=None):
    """"""
    return object

def navigation_message_parse_angles_changed(message=None, cur_angle=None, n_angles=None):
    """"""
    return object

def navigation_message_parse_event(message=None, event=None):
    """"""
    return object

def navigation_message_parse_mouse_over(message=None, active=None):
    """"""
    return object

def navigation_query_get_type(query=None):
    """"""
    return object

def navigation_query_new_angles():
    """"""
    return object

def navigation_query_new_commands():
    """"""
    return object

def navigation_query_parse_angles(query=None, cur_angle=None, n_angles=None):
    """"""
    return object

def navigation_query_parse_commands_length(query=None, n_cmds=None):
    """"""
    return object

def navigation_query_parse_commands_nth(query=None, nth=None, cmd=None):
    """"""
    return object

def navigation_query_set_angles(query=None, cur_angle=None, n_angles=None):
    """"""
    return object

def navigation_query_set_commandsv(query=None, n_cmds=None, cmds=None):
    """"""
    return object

def video_affine_transformation_meta_api_get_type():
    """"""
    return object

def video_affine_transformation_meta_get_info():
    """"""
    return object

def video_blend(dest=None, src=None, x=None, y=None, global_alpha=None):
    """"""
    return object

def video_blend_scale_linear_RGBA(src=None, src_buffer=None, dest_height=None, dest_width=None, dest=None, dest_buffer=None):
    """"""
    return object

def video_calculate_display_ratio(dar_n=None, dar_d=None, video_width=None, video_height=None, video_par_n=None, video_par_d=None, display_par_n=None, display_par_d=None):
    """"""
    return object

def video_chroma_from_string(s=None):
    """"""
    return object

def video_chroma_resample(resample=None, lines=None, width=None):
    """"""
    return object

def video_chroma_resample_new(method=None, site=None, flags=None, format=None, h_factor=None, v_factor=None):
    """"""
    return object

def video_chroma_to_string(site=None):
    """"""
    return object

def video_color_matrix_get_Kr_Kb(matrix=None, Kr=None, Kb=None):
    """"""
    return object

def video_color_primaries_get_info(primaries=None):
    """"""
    return object

def video_color_range_offsets(range=None, info=None, offset=None, scale=None):
    """"""
    return object

def video_color_transfer_decode(func=None, val=None):
    """"""
    return object

def video_color_transfer_encode(func=None, val=None):
    """"""
    return object

def video_convert_sample(sample=None, to_caps=None, timeout=None):
    """"""
    return object

def video_convert_sample_async(sample=None, to_caps=None, timeout=None, callback=None, user_data=None, destroy_notify=None):
    """"""
    return object

def video_converter_new(in_info=None, out_info=None, config=None):
    """"""
    return object

def video_crop_meta_api_get_type():
    """"""
    return object

def video_crop_meta_get_info():
    """"""
    return object

def video_dither_new(method=None, flags=None, format=None, quantizer=None, width=None):
    """"""
    return object

def video_event_is_force_key_unit(event=None):
    """"""
    return object

def video_event_new_downstream_force_key_unit(timestamp=None, stream_time=None, running_time=None, all_headers=None, count=None):
    """"""
    return object

def video_event_new_still_frame(in_still=None):
    """"""
    return object

def video_event_new_upstream_force_key_unit(running_time=None, all_headers=None, count=None):
    """"""
    return object

def video_event_parse_downstream_force_key_unit(event=None, timestamp=None, stream_time=None, running_time=None, all_headers=None, count=None):
    """"""
    return object

def video_event_parse_still_frame(event=None, in_still=None):
    """"""
    return object

def video_event_parse_upstream_force_key_unit(event=None, running_time=None, all_headers=None, count=None):
    """"""
    return object

def video_field_order_from_string(order=None):
    """"""
    return object

def video_field_order_to_string(order=None):
    """"""
    return object

def video_format_from_fourcc(fourcc=None):
    """"""
    return object

def video_format_from_masks(depth=None, bpp=None, endianness=None, red_mask=None, green_mask=None, blue_mask=None, alpha_mask=None):
    """"""
    return object

def video_format_from_string(format=None):
    """"""
    return object

def video_format_get_info(format=None):
    """"""
    return object

def video_format_get_palette(format=None, size=None):
    """"""
    return object

def video_format_to_fourcc(format=None):
    """"""
    return object

def video_format_to_string(format=None):
    """"""
    return object

def video_gl_texture_upload_meta_api_get_type():
    """"""
    return object

def video_gl_texture_upload_meta_get_info():
    """"""
    return object

def video_guess_framerate(duration=None, dest_n=None, dest_d=None):
    """"""
    return object

def video_interlace_mode_from_string(mode=None):
    """"""
    return object

def video_interlace_mode_to_string(mode=None):
    """"""
    return object

def video_meta_api_get_type():
    """"""
    return object

def video_meta_get_info():
    """"""
    return object

def video_meta_transform_scale_get_quark():
    """"""
    return object

def video_multiview_get_doubled_height_modes():
    """"""
    return object

def video_multiview_get_doubled_size_modes():
    """"""
    return object

def video_multiview_get_doubled_width_modes():
    """"""
    return object

def video_multiview_get_mono_modes():
    """"""
    return object

def video_multiview_get_unpacked_modes():
    """"""
    return object

def video_multiview_guess_half_aspect(mv_mode=None, width=None, height=None, par_n=None, par_d=None):
    """"""
    return object

def video_multiview_mode_from_caps_string(caps_mview_mode=None):
    """"""
    return object

def video_multiview_mode_to_caps_string(mview_mode=None):
    """"""
    return object

def video_multiview_video_info_change_mode(info=None, out_mview_mode=None, out_mview_flags=None):
    """"""
    return object

def video_overlay_composition_meta_api_get_type():
    """"""
    return object

def video_overlay_composition_meta_get_info():
    """"""
    return object

def video_overlay_install_properties(oclass=None, last_prop_id=None):
    """"""
    return object

def video_overlay_set_property(object=None, last_prop_id=None, property_id=None, value=None):
    """"""
    return object

def video_region_of_interest_meta_api_get_type():
    """"""
    return object

def video_region_of_interest_meta_get_info():
    """"""
    return object

def video_scaler_new(method=None, flags=None, n_taps=None, in_size=None, out_size=None, options=None):
    """"""
    return object

def video_tile_get_index(mode=None, x=None, y=None, x_tiles=None, y_tiles=None):
    """"""
    return object

def video_time_code_meta_api_get_type():
    """"""
    return object

def video_time_code_meta_get_info():
    """"""
    return object


class ColorBalance():
    """"""
    
    def get_balance_type(self):
        """"""
        return object
    
    def get_value(self, channel=None):
        """"""
        return object
    
    def list_channels(self):
        """"""
        return object
    
    def set_value(self, channel=None, value=None):
        """"""
        return object
    
    def value_changed(self, channel=None, value=None):
        """"""
        return object
    
    def get_balance_type(self):
        """"""
        return object
    
    def get_value(self, channel=None):
        """"""
        return object
    
    def list_channels(self):
        """"""
        return object
    
    def set_value(self, channel=None, value=None):
        """"""
        return object
    
    def value_changed(self, channel=None, value=None):
        """"""
        return object


class ColorBalanceChannel(GObject.Object):
    """"""
    
    def value_changed(self, value=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def label(self):
        return object

    @property
    def min_value(self):
        return object

    @property
    def max_value(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ColorBalanceChannelClass():
    """"""

    @property
    def parent(self):
        return object

    @property
    def value_changed(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class ColorBalanceInterface():
    """"""

    @property
    def iface(self):
        return object

    @property
    def list_channels(self):
        return object

    @property
    def set_value(self):
        return object

    @property
    def get_value(self):
        return object

    @property
    def get_balance_type(self):
        return object

    @property
    def value_changed(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class Navigation():
    """"""
    @staticmethod
    def event_get_type(event=None):
        """"""
        return object
    @staticmethod
    def event_parse_command(event=None, command=None):
        """"""
        return object
    @staticmethod
    def event_parse_key_event(event=None, key=None):
        """"""
        return object
    @staticmethod
    def event_parse_mouse_button_event(event=None, button=None, x=None, y=None):
        """"""
        return object
    @staticmethod
    def event_parse_mouse_move_event(event=None, x=None, y=None):
        """"""
        return object
    @staticmethod
    def message_get_type(message=None):
        """"""
        return object
    @staticmethod
    def message_new_angles_changed(src=None, cur_angle=None, n_angles=None):
        """"""
        return object
    @staticmethod
    def message_new_commands_changed(src=None):
        """"""
        return object
    @staticmethod
    def message_new_event(src=None, event=None):
        """"""
        return object
    @staticmethod
    def message_new_mouse_over(src=None, active=None):
        """"""
        return object
    @staticmethod
    def message_parse_angles_changed(message=None, cur_angle=None, n_angles=None):
        """"""
        return object
    @staticmethod
    def message_parse_event(message=None, event=None):
        """"""
        return object
    @staticmethod
    def message_parse_mouse_over(message=None, active=None):
        """"""
        return object
    @staticmethod
    def query_get_type(query=None):
        """"""
        return object
    @staticmethod
    def query_new_angles():
        """"""
        return object
    @staticmethod
    def query_new_commands():
        """"""
        return object
    @staticmethod
    def query_parse_angles(query=None, cur_angle=None, n_angles=None):
        """"""
        return object
    @staticmethod
    def query_parse_commands_length(query=None, n_cmds=None):
        """"""
        return object
    @staticmethod
    def query_parse_commands_nth(query=None, nth=None, cmd=None):
        """"""
        return object
    @staticmethod
    def query_set_angles(query=None, cur_angle=None, n_angles=None):
        """"""
        return object
    @staticmethod
    def query_set_commands(query=None, n_cmds=None, *args):
        """"""
        return object
    @staticmethod
    def query_set_commandsv(query=None, n_cmds=None, cmds=None):
        """"""
        return object
    
    def send_event(self, structure=None):
        """"""
        return object
    
    def send_command(self, command=None):
        """"""
        return object
    
    def send_event(self, structure=None):
        """"""
        return object
    
    def send_key_event(self, event=None, key=None):
        """"""
        return object
    
    def send_mouse_event(self, event=None, button=None, x=None, y=None):
        """"""
        return object


class NavigationInterface():
    """"""

    @property
    def iface(self):
        return object

    @property
    def send_event(self):
        return object


class VideoAffineTransformationMeta():
    """"""
    
    def apply_matrix(self, matrix=None):
        """"""
        return object
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def matrix(self):
        return object


class VideoAlignment():
    """"""
    
    def reset(self):
        """"""
        return object

    @property
    def padding_top(self):
        return object

    @property
    def padding_bottom(self):
        return object

    @property
    def padding_left(self):
        return object

    @property
    def padding_right(self):
        return object

    @property
    def stride_align(self):
        return object


class VideoBufferPool(Gst.BufferPool):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def bufferpool(self):
        return object

    @property
    def priv(self):
        return object


class VideoBufferPoolClass():
    """"""

    @property
    def parent_class(self):
        return object


class VideoBufferPoolPrivate():
    """"""


class VideoChromaResample():
    """"""
    
    def (self, lines=None, width=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_info(self, n_lines=None, offset=None):
        """"""
        return object
    @staticmethod
    def new(method=None, site=None, flags=None, format=None, h_factor=None, v_factor=None):
        """"""
        return object


class VideoCodecFrame():
    """"""
    
    def get_user_data(self):
        """"""
        return object
    
    def ref(self):
        """"""
        return object
    
    def set_user_data(self, user_data=None, notify=None):
        """"""
        return object
    
    def unref(self):
        """"""
        return object

    @property
    def ref_count(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def system_frame_number(self):
        return object

    @property
    def decode_frame_number(self):
        return object

    @property
    def presentation_frame_number(self):
        return object

    @property
    def dts(self):
        return object

    @property
    def pts(self):
        return object

    @property
    def duration(self):
        return object

    @property
    def distance_from_sync(self):
        return object

    @property
    def input_buffer(self):
        return object

    @property
    def output_buffer(self):
        return object

    @property
    def deadline(self):
        return object

    @property
    def events(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def user_data_destroy_notify(self):
        return object


class VideoCodecState():
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
    def info(self):
        return object

    @property
    def caps(self):
        return object

    @property
    def codec_data(self):
        return object

    @property
    def allocation_caps(self):
        return object

    @property
    def padding(self):
        return object


class VideoColorPrimariesInfo():
    """"""

    @property
    def primaries(self):
        return object

    @property
    def Wx(self):
        return object

    @property
    def Wy(self):
        return object

    @property
    def Rx(self):
        return object

    @property
    def Ry(self):
        return object

    @property
    def Gx(self):
        return object

    @property
    def Gy(self):
        return object

    @property
    def Bx(self):
        return object

    @property
    def By(self):
        return object


class VideoColorimetry():
    """"""
    
    def from_string(self, color=None):
        """"""
        return object
    
    def is_equal(self, other=None):
        """"""
        return object
    
    def matches(self, color=None):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object

    @property
    def range(self):
        return object

    @property
    def matrix(self):
        return object

    @property
    def transfer(self):
        return object

    @property
    def primaries(self):
        return object


class VideoConverter():
    """"""
    
    def frame(self, src=None, dest=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_config(self):
        """"""
        return object
    
    def set_config(self, config=None):
        """"""
        return object
    @staticmethod
    def new(in_info=None, out_info=None, config=None):
        """"""
        return object


class VideoCropMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def x(self):
        return object

    @property
    def y(self):
        return object

    @property
    def width(self):
        return object

    @property
    def height(self):
        return object


class VideoDecoder(Gst.Element):
    """"""
    
    def close(self):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def drain(self):
        """"""
        return object
    
    def finish(self):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def getcaps(self, filter=None):
        """"""
        return object
    
    def handle_frame(self, frame=None):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def parse(self, frame=None, adapter=None, at_eos=None):
        """"""
        return object
    
    def propose_allocation(self, query=None):
        """"""
        return object
    
    def reset(self, hard=None):
        """"""
        return object
    
    def set_format(self, state=None):
        """"""
        return object
    
    def sink_event(self, event=None):
        """"""
        return object
    
    def sink_query(self, query=None):
        """"""
        return object
    
    def src_event(self, event=None):
        """"""
        return object
    
    def src_query(self, query=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def transform_meta(self, frame=None, meta=None):
        """"""
        return object
    
    def add_to_frame(self, n_bytes=None):
        """"""
        return object
    
    def allocate_output_buffer(self):
        """"""
        return object
    
    def allocate_output_frame(self, frame=None):
        """"""
        return object
    
    def allocate_output_frame_with_params(self, frame=None, params=None):
        """"""
        return object
    
    def drop_frame(self, frame=None):
        """"""
        return object
    
    def finish_frame(self, frame=None):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_buffer_pool(self):
        """"""
        return object
    
    def get_estimate_rate(self):
        """"""
        return object
    
    def get_frame(self, frame_number=None):
        """"""
        return object
    
    def get_frames(self):
        """"""
        return object
    
    def get_latency(self, min_latency=None, max_latency=None):
        """"""
        return object
    
    def get_max_decode_time(self, frame=None):
        """"""
        return object
    
    def get_max_errors(self):
        """"""
        return object
    
    def get_needs_format(self):
        """"""
        return object
    
    def get_oldest_frame(self):
        """"""
        return object
    
    def get_output_state(self):
        """"""
        return object
    
    def get_packetized(self):
        """"""
        return object
    
    def get_pending_frame_size(self):
        """"""
        return object
    
    def get_qos_proportion(self):
        """"""
        return object
    
    def have_frame(self):
        """"""
        return object
    
    def merge_tags(self, tags=None, mode=None):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def proxy_getcaps(self, caps=None, filter=None):
        """"""
        return object
    
    def release_frame(self, frame=None):
        """"""
        return object
    
    def set_estimate_rate(self, enabled=None):
        """"""
        return object
    
    def set_latency(self, min_latency=None, max_latency=None):
        """"""
        return object
    
    def set_max_errors(self, num=None):
        """"""
        return object
    
    def set_needs_format(self, enabled=None):
        """"""
        return object
    
    def set_output_state(self, fmt=None, width=None, height=None, reference=None):
        """"""
        return object
    
    def set_packetized(self, packetized=None):
        """"""
        return object
    
    def set_use_default_pad_acceptcaps(self, use=None):
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
    def stream_lock(self):
        return object

    @property
    def input_segment(self):
        return object

    @property
    def output_segment(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def padding(self):
        return object


class VideoDecoderClass():
    """"""

    @property
    def element_class(self):
        return object

    @property
    def open(self):
        return object

    @property
    def close(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def parse(self):
        return object

    @property
    def set_format(self):
        return object

    @property
    def reset(self):
        return object

    @property
    def finish(self):
        return object

    @property
    def handle_frame(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def negotiate(self):
        return object

    @property
    def decide_allocation(self):
        return object

    @property
    def propose_allocation(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def sink_query(self):
        return object

    @property
    def src_query(self):
        return object

    @property
    def getcaps(self):
        return object

    @property
    def drain(self):
        return object

    @property
    def transform_meta(self):
        return object

    @property
    def padding(self):
        return object


class VideoDecoderPrivate():
    """"""


class VideoDirection():
    """"""


class VideoDirectionInterface():
    """"""

    @property
    def iface(self):
        return object


class VideoDither():
    """"""
    
    def free(self):
        """"""
        return object
    
    def line(self, line=None, x=None, y=None, width=None):
        """"""
        return object
    @staticmethod
    def new(method=None, flags=None, format=None, quantizer=None, width=None):
        """"""
        return object


class VideoEncoder(Gst.Element, Gst.Preset):
    """"""
    
    def close(self):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def finish(self):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def getcaps(self, filter=None):
        """"""
        return object
    
    def handle_frame(self, frame=None):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def pre_push(self, frame=None):
        """"""
        return object
    
    def propose_allocation(self, query=None):
        """"""
        return object
    
    def reset(self, hard=None):
        """"""
        return object
    
    def set_format(self, state=None):
        """"""
        return object
    
    def sink_event(self, event=None):
        """"""
        return object
    
    def sink_query(self, query=None):
        """"""
        return object
    
    def src_event(self, event=None):
        """"""
        return object
    
    def src_query(self, query=None):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def transform_meta(self, frame=None, meta=None):
        """"""
        return object
    
    def allocate_output_buffer(self, size=None):
        """"""
        return object
    
    def allocate_output_frame(self, frame=None, size=None):
        """"""
        return object
    
    def finish_frame(self, frame=None):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_frame(self, frame_number=None):
        """"""
        return object
    
    def get_frames(self):
        """"""
        return object
    
    def get_latency(self, min_latency=None, max_latency=None):
        """"""
        return object
    
    def get_max_encode_time(self, frame=None):
        """"""
        return object
    
    def get_oldest_frame(self):
        """"""
        return object
    
    def get_output_state(self):
        """"""
        return object
    
    def is_qos_enabled(self):
        """"""
        return object
    
    def merge_tags(self, tags=None, mode=None):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def proxy_getcaps(self, caps=None, filter=None):
        """"""
        return object
    
    def set_headers(self, headers=None):
        """"""
        return object
    
    def set_latency(self, min_latency=None, max_latency=None):
        """"""
        return object
    
    def set_min_pts(self, min_pts=None):
        """"""
        return object
    
    def set_output_state(self, caps=None, reference=None):
        """"""
        return object
    
    def set_qos_enabled(self, enabled=None):
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
    def stream_lock(self):
        return object

    @property
    def input_segment(self):
        return object

    @property
    def output_segment(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def padding(self):
        return object


class VideoEncoderClass():
    """"""

    @property
    def element_class(self):
        return object

    @property
    def open(self):
        return object

    @property
    def close(self):
        return object

    @property
    def start(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def set_format(self):
        return object

    @property
    def handle_frame(self):
        return object

    @property
    def reset(self):
        return object

    @property
    def finish(self):
        return object

    @property
    def pre_push(self):
        return object

    @property
    def getcaps(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def negotiate(self):
        return object

    @property
    def decide_allocation(self):
        return object

    @property
    def propose_allocation(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def sink_query(self):
        return object

    @property
    def src_query(self):
        return object

    @property
    def transform_meta(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoEncoderPrivate():
    """"""


class VideoFilter(GstBase.BaseTransform):
    """"""
    
    def set_info(self, incaps=None, in_info=None, outcaps=None, out_info=None):
        """"""
        return object
    
    def transform_frame(self, inframe=None, outframe=None):
        """"""
        return object
    
    def transform_frame_ip(self, frame=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def negotiated(self):
        return object

    @property
    def in_info(self):
        return object

    @property
    def out_info(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoFilterClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def set_info(self):
        return object

    @property
    def transform_frame(self):
        return object

    @property
    def transform_frame_ip(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoFormatInfo():
    """"""

    @property
    def format(self):
        return object

    @property
    def name(self):
        return object

    @property
    def description(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def bits(self):
        return object

    @property
    def n_components(self):
        return object

    @property
    def shift(self):
        return object

    @property
    def depth(self):
        return object

    @property
    def pixel_stride(self):
        return object

    @property
    def n_planes(self):
        return object

    @property
    def plane(self):
        return object

    @property
    def poffset(self):
        return object

    @property
    def w_sub(self):
        return object

    @property
    def h_sub(self):
        return object

    @property
    def unpack_format(self):
        return object

    @property
    def unpack_func(self):
        return object

    @property
    def pack_lines(self):
        return object

    @property
    def pack_func(self):
        return object

    @property
    def tile_mode(self):
        return object

    @property
    def tile_ws(self):
        return object

    @property
    def tile_hs(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoFrame():
    """"""
    
    def copy(self, src=None):
        """"""
        return object
    
    def copy_plane(self, src=None, plane=None):
        """"""
        return object
    
    def map(self, info=None, buffer=None, flags=None):
        """"""
        return object
    
    def map_id(self, info=None, buffer=None, id=None, flags=None):
        """"""
        return object
    
    def unmap(self):
        """"""
        return object

    @property
    def info(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def buffer(self):
        return object

    @property
    def meta(self):
        return object

    @property
    def id(self):
        return object

    @property
    def data(self):
        return object

    @property
    def map(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoGLTextureUploadMeta():
    """"""
    
    def upload(self, texture_id=None):
        """"""
        return object
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def texture_orientation(self):
        return object

    @property
    def n_textures(self):
        return object

    @property
    def texture_type(self):
        return object

    @property
    def buffer(self):
        return object

    @property
    def upload(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def user_data_copy(self):
        return object

    @property
    def user_data_free(self):
        return object


class VideoInfo():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def align(self, align=None):
        """"""
        return object
    
    def convert(self, src_format=None, src_value=None, dest_format=None, dest_value=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def from_caps(self, caps=None):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def is_equal(self, other=None):
        """"""
        return object
    
    def set_format(self, format=None, width=None, height=None):
        """"""
        return object
    
    def to_caps(self):
        """"""
        return object

    @property
    def finfo(self):
        return object

    @property
    def interlace_mode(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def width(self):
        return object

    @property
    def height(self):
        return object

    @property
    def size(self):
        return object

    @property
    def views(self):
        return object

    @property
    def chroma_site(self):
        return object

    @property
    def colorimetry(self):
        return object

    @property
    def par_n(self):
        return object

    @property
    def par_d(self):
        return object

    @property
    def fps_n(self):
        return object

    @property
    def fps_d(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def stride(self):
        return object


class VideoMeta():
    """"""
    
    def map(self, plane=None, info=None, data=None, stride=None, flags=None):
        """"""
        return object
    
    def unmap(self, plane=None, info=None):
        """"""
        return object
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def buffer(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def format(self):
        return object

    @property
    def id(self):
        return object

    @property
    def width(self):
        return object

    @property
    def height(self):
        return object

    @property
    def n_planes(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def stride(self):
        return object

    @property
    def map(self):
        return object

    @property
    def unmap(self):
        return object


class VideoMetaTransform():
    """"""
    @staticmethod
    def scale_get_quark():
        """"""
        return object

    @property
    def in_info(self):
        return object

    @property
    def out_info(self):
        return object


class VideoMultiviewFlagsSet(Gst.FlagSet):
    """"""


class VideoOrientation():
    """"""
    
    def get_hcenter(self, center=None):
        """"""
        return object
    
    def get_hflip(self, flip=None):
        """"""
        return object
    
    def get_vcenter(self, center=None):
        """"""
        return object
    
    def get_vflip(self, flip=None):
        """"""
        return object
    
    def set_hcenter(self, center=None):
        """"""
        return object
    
    def set_hflip(self, flip=None):
        """"""
        return object
    
    def set_vcenter(self, center=None):
        """"""
        return object
    
    def set_vflip(self, flip=None):
        """"""
        return object
    
    def get_hcenter(self, center=None):
        """"""
        return object
    
    def get_hflip(self, flip=None):
        """"""
        return object
    
    def get_vcenter(self, center=None):
        """"""
        return object
    
    def get_vflip(self, flip=None):
        """"""
        return object
    
    def set_hcenter(self, center=None):
        """"""
        return object
    
    def set_hflip(self, flip=None):
        """"""
        return object
    
    def set_vcenter(self, center=None):
        """"""
        return object
    
    def set_vflip(self, flip=None):
        """"""
        return object


class VideoOrientationInterface():
    """"""

    @property
    def iface(self):
        return object

    @property
    def get_hflip(self):
        return object

    @property
    def get_vflip(self):
        return object

    @property
    def get_hcenter(self):
        return object

    @property
    def get_vcenter(self):
        return object

    @property
    def set_hflip(self):
        return object

    @property
    def set_vflip(self):
        return object

    @property
    def set_hcenter(self):
        return object

    @property
    def set_vcenter(self):
        return object


class VideoOverlay():
    """"""
    @staticmethod
    def install_properties(oclass=None, last_prop_id=None):
        """"""
        return object
    @staticmethod
    def set_property(object=None, last_prop_id=None, property_id=None, value=None):
        """"""
        return object
    
    def expose(self):
        """"""
        return object
    
    def handle_events(self, handle_events=None):
        """"""
        return object
    
    def set_render_rectangle(self, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def set_window_handle(self, handle=None):
        """"""
        return object
    
    def expose(self):
        """"""
        return object
    
    def got_window_handle(self, handle=None):
        """"""
        return object
    
    def handle_events(self, handle_events=None):
        """"""
        return object
    
    def prepare_window_handle(self):
        """"""
        return object
    
    def set_render_rectangle(self, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def set_window_handle(self, handle=None):
        """"""
        return object


class VideoOverlayComposition():
    """"""
    
    def __init__(self, rectangle=None):
        """"""
        return object
    @staticmethod
    def new(rectangle=None):
        """"""
        return object
    
    def add_rectangle(self, rectangle=None):
        """"""
        return object
    
    def blend(self, video_buf=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def get_rectangle(self, n=None):
        """"""
        return object
    
    def get_seqnum(self):
        """"""
        return object
    
    def make_writable(self):
        """"""
        return object
    
    def n_rectangles(self):
        """"""
        return object


class VideoOverlayCompositionMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def overlay(self):
        return object


class VideoOverlayInterface():
    """"""

    @property
    def iface(self):
        return object

    @property
    def expose(self):
        return object

    @property
    def handle_events(self):
        return object

    @property
    def set_render_rectangle(self):
        return object

    @property
    def set_window_handle(self):
        return object


class VideoOverlayProperties():
    """"""


class VideoOverlayRectangle():
    """"""
    @staticmethod
    def new_raw(pixels=None, render_x=None, render_y=None, render_width=None, render_height=None, flags=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def get_flags(self):
        """"""
        return object
    
    def get_global_alpha(self):
        """"""
        return object
    
    def get_pixels_argb(self, flags=None):
        """"""
        return object
    
    def get_pixels_ayuv(self, flags=None):
        """"""
        return object
    
    def get_pixels_raw(self, flags=None):
        """"""
        return object
    
    def get_pixels_unscaled_argb(self, flags=None):
        """"""
        return object
    
    def get_pixels_unscaled_ayuv(self, flags=None):
        """"""
        return object
    
    def get_pixels_unscaled_raw(self, flags=None):
        """"""
        return object
    
    def get_render_rectangle(self, render_x=None, render_y=None, render_width=None, render_height=None):
        """"""
        return object
    
    def get_seqnum(self):
        """"""
        return object
    
    def set_global_alpha(self, global_alpha=None):
        """"""
        return object
    
    def set_render_rectangle(self, render_x=None, render_y=None, render_width=None, render_height=None):
        """"""
        return object


class VideoRectangle():
    """"""

    @property
    def x(self):
        return object

    @property
    def y(self):
        return object

    @property
    def w(self):
        return object

    @property
    def h(self):
        return object


class VideoRegionOfInterestMeta():
    """"""
    
    def add_param(self, s=None):
        """"""
        return object
    
    def get_param(self, name=None):
        """"""
        return object
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def roi_type(self):
        return object

    @property
    def id(self):
        return object

    @property
    def parent_id(self):
        return object

    @property
    def x(self):
        return object

    @property
    def y(self):
        return object

    @property
    def w(self):
        return object

    @property
    def h(self):
        return object

    @property
    def params(self):
        return object


class VideoResampler():
    """"""
    
    def clear(self):
        """"""
        return object
    
    def init(self, method=None, flags=None, n_phases=None, n_taps=None, shift=None, in_size=None, out_size=None, options=None):
        """"""
        return object

    @property
    def in_size(self):
        return object

    @property
    def out_size(self):
        return object

    @property
    def max_taps(self):
        return object

    @property
    def n_phases(self):
        return object

    @property
    def offset(self):
        return object

    @property
    def phase(self):
        return object

    @property
    def n_taps(self):
        return object

    @property
    def taps(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoScaler():
    """"""
    
    def 2d(self, vscale=None, format=None, src=None, src_stride=None, dest=None, dest_stride=None, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def combine_packed_YUV(self, uv_scale=None, in_format=None, out_format=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_coeff(self, out_offset=None, in_offset=None, n_taps=None):
        """"""
        return object
    
    def get_max_taps(self):
        """"""
        return object
    
    def horizontal(self, format=None, src=None, dest=None, dest_offset=None, width=None):
        """"""
        return object
    
    def vertical(self, format=None, src_lines=None, dest=None, dest_offset=None, width=None):
        """"""
        return object
    @staticmethod
    def new(method=None, flags=None, n_taps=None, in_size=None, out_size=None, options=None):
        """"""
        return object


class VideoSink(GstBase.BaseSink):
    """"""
    @staticmethod
    def center_rect(src=None, dst=None, result=None, scaling=None):
        """"""
        return object
    
    def show_frame(self, buf=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def width(self):
        return object

    @property
    def height(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoSinkClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def show_frame(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class VideoSinkPrivate():
    """"""


class VideoTimeCode():
    """"""
    
    def __init__(self, fps_n=None, fps_d=None, latest_daily_jam=None, flags=None, hours=None, minutes=None, seconds=None, frames=None, field_count=None):
        """"""
        return object
    @staticmethod
    def new(fps_n=None, fps_d=None, latest_daily_jam=None, flags=None, hours=None, minutes=None, seconds=None, frames=None, field_count=None):
        """"""
        return object
    @staticmethod
    def new_empty():
        """"""
        return object
    @staticmethod
    def new_from_date_time(fps_n=None, fps_d=None, dt=None, flags=None, field_count=None):
        """"""
        return object
    @staticmethod
    def new_from_string(tc_str=None):
        """"""
        return object
    
    def add_frames(self, frames=None):
        """"""
        return object
    
    def add_interval(self, tc_inter=None):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def compare(self, tc2=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def frames_since_daily_jam(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def increment_frame(self):
        """"""
        return object
    
    def init(self, fps_n=None, fps_d=None, latest_daily_jam=None, flags=None, hours=None, minutes=None, seconds=None, frames=None, field_count=None):
        """"""
        return object
    
    def init_from_date_time(self, fps_n=None, fps_d=None, dt=None, flags=None, field_count=None):
        """"""
        return object
    
    def is_valid(self):
        """"""
        return object
    
    def nsec_since_daily_jam(self):
        """"""
        return object
    
    def to_date_time(self):
        """"""
        return object
    
    def to_string(self):
        """"""
        return object

    @property
    def config(self):
        return object

    @property
    def hours(self):
        return object

    @property
    def minutes(self):
        return object

    @property
    def seconds(self):
        return object

    @property
    def frames(self):
        return object

    @property
    def field_count(self):
        return object


class VideoTimeCodeConfig():
    """"""

    @property
    def fps_n(self):
        return object

    @property
    def fps_d(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def latest_daily_jam(self):
        return object


class VideoTimeCodeInterval():
    """"""
    
    def __init__(self, hours=None, minutes=None, seconds=None, frames=None):
        """"""
        return object
    @staticmethod
    def new(hours=None, minutes=None, seconds=None, frames=None):
        """"""
        return object
    @staticmethod
    def new_from_string(tc_inter_str=None):
        """"""
        return object
    
    def clear(self):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def init(self, hours=None, minutes=None, seconds=None, frames=None):
        """"""
        return object

    @property
    def hours(self):
        return object

    @property
    def minutes(self):
        return object

    @property
    def seconds(self):
        return object

    @property
    def frames(self):
        return object


class VideoTimeCodeMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def tc(self):
        return object
