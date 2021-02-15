# -*- coding: utf-8 -*-
from gi.repository import Gst
from gi.repository import GstBase
AUDIO_CHANNELS_RANGE = r"""(int) [ 1, max ]"""
AUDIO_CONVERTER_OPT_DITHER_METHOD = r"""GstAudioConverter.dither-method"""
AUDIO_CONVERTER_OPT_MIX_MATRIX = r"""GstAudioConverter.mix-matrix"""
AUDIO_CONVERTER_OPT_NOISE_SHAPING_METHOD = r"""GstAudioConverter.noise-shaping-method"""
AUDIO_CONVERTER_OPT_QUANTIZATION = r"""GstAudioConverter.quantization"""
AUDIO_CONVERTER_OPT_RESAMPLER_METHOD = r"""GstAudioConverter.resampler-method"""
AUDIO_DECODER_MAX_ERRORS = r"""10"""
AUDIO_DECODER_SINK_NAME = r"""sink"""
AUDIO_DECODER_SRC_NAME = r"""src"""
AUDIO_DEF_CHANNELS = r"""2"""
AUDIO_DEF_FORMAT = r"""S16LE"""
AUDIO_DEF_RATE = r"""44100"""
AUDIO_ENCODER_SINK_NAME = r"""sink"""
AUDIO_ENCODER_SRC_NAME = r"""src"""
AUDIO_FORMATS_ALL = r""" { S8, U8, S16LE, S16BE, U16LE, U16BE, S24_32LE, S24_32BE, U24_32LE, U24_32BE, S32LE, S32BE, U32LE, U32BE, S24LE, S24BE, U24LE, U24BE, S20LE, S20BE, U20LE, U20BE, S18LE, S18BE, U18LE, U18BE, F32LE, F32BE, F64LE, F64BE }"""
AUDIO_RATE_RANGE = r"""(int) [ 1, max ]"""
AUDIO_RESAMPLER_OPT_CUBIC_B = r"""GstAudioResampler.cubic-b"""
AUDIO_RESAMPLER_OPT_CUBIC_C = r"""GstAudioResampler.cubic-c"""
AUDIO_RESAMPLER_OPT_CUTOFF = r"""GstAudioResampler.cutoff"""
AUDIO_RESAMPLER_OPT_FILTER_INTERPOLATION = r"""GstAudioResampler.filter-interpolation"""
AUDIO_RESAMPLER_OPT_FILTER_MODE = r"""GstAudioResampler.filter-mode"""
AUDIO_RESAMPLER_OPT_FILTER_MODE_THRESHOLD = r"""GstAudioResampler.filter-mode-threshold"""
AUDIO_RESAMPLER_OPT_FILTER_OVERSAMPLE = r"""GstAudioResampler.filter-oversample"""
AUDIO_RESAMPLER_OPT_MAX_PHASE_ERROR = r"""GstAudioResampler.max-phase-error"""
AUDIO_RESAMPLER_OPT_N_TAPS = r"""GstAudioResampler.n-taps"""
AUDIO_RESAMPLER_OPT_STOP_ATTENUATION = r"""GstAudioResampler.stop-attenutation"""
AUDIO_RESAMPLER_OPT_TRANSITION_BANDWIDTH = r"""GstAudioResampler.transition-bandwidth"""
AUDIO_RESAMPLER_QUALITY_DEFAULT = r"""4"""
AUDIO_RESAMPLER_QUALITY_MAX = r"""10"""
AUDIO_RESAMPLER_QUALITY_MIN = r"""0"""


class AudioBaseSinkDiscontReason:
    """"""
    NO_DISCONT = 0
    NEW_CAPS = 1
    FLUSH = 2
    SYNC_LATENCY = 3
    ALIGNMENT = 4
    DEVICE_FAILURE = 5


class AudioBaseSinkSlaveMethod:
    """"""
    RESAMPLE = 0
    SKEW = 1
    NONE = 2
    CUSTOM = 3


class AudioBaseSrcSlaveMethod:
    """"""
    RESAMPLE = 0
    RE_TIMESTAMP = 1
    SKEW = 2
    NONE = 3


class AudioCdSrcMode:
    """"""
    NORMAL = 0
    CONTINUOUS = 1


class AudioChannelMixerFlags:
    """"""
    NONE = 0
    NON_INTERLEAVED_IN = 1
    NON_INTERLEAVED_OUT = 2
    UNPOSITIONED_IN = 4
    UNPOSITIONED_OUT = 8


class AudioChannelPosition:
    """"""
    NONE = -3
    MONO = -2
    INVALID = -1
    FRONT_LEFT = 0
    FRONT_RIGHT = 1
    FRONT_CENTER = 2
    LFE1 = 3
    REAR_LEFT = 4
    REAR_RIGHT = 5
    FRONT_LEFT_OF_CENTER = 6
    FRONT_RIGHT_OF_CENTER = 7
    REAR_CENTER = 8
    LFE2 = 9
    SIDE_LEFT = 10
    SIDE_RIGHT = 11
    TOP_FRONT_LEFT = 12
    TOP_FRONT_RIGHT = 13
    TOP_FRONT_CENTER = 14
    TOP_CENTER = 15
    TOP_REAR_LEFT = 16
    TOP_REAR_RIGHT = 17
    TOP_SIDE_LEFT = 18
    TOP_SIDE_RIGHT = 19
    TOP_REAR_CENTER = 20
    BOTTOM_FRONT_CENTER = 21
    BOTTOM_FRONT_LEFT = 22
    BOTTOM_FRONT_RIGHT = 23
    WIDE_LEFT = 24
    WIDE_RIGHT = 25
    SURROUND_LEFT = 26
    SURROUND_RIGHT = 27


class AudioConverterFlags:
    """"""
    NONE = 0
    IN_WRITABLE = 1
    VARIABLE_RATE = 2


class AudioDitherMethod:
    """"""
    NONE = 0
    RPDF = 1
    TPDF = 2
    TPDF_HF = 3


class AudioFlags:
    """"""
    NONE = 0
    UNPOSITIONED = 1


class AudioFormat:
    """"""
    UNKNOWN = 0
    ENCODED = 1
    S8 = 2
    U8 = 3
    S16LE = 4
    S16BE = 5
    U16LE = 6
    U16BE = 7
    S24_32LE = 8
    S24_32BE = 9
    U24_32LE = 10
    U24_32BE = 11
    S32LE = 12
    S32BE = 13
    U32LE = 14
    U32BE = 15
    S24LE = 16
    S24BE = 17
    U24LE = 18
    U24BE = 19
    S20LE = 20
    S20BE = 21
    U20LE = 22
    U20BE = 23
    S18LE = 24
    S18BE = 25
    U18LE = 26
    U18BE = 27
    F32LE = 28
    F32BE = 29
    F64LE = 30
    F64BE = 31
    S16 = 4
    U16 = 6
    S24_32 = 8
    U24_32 = 10
    S32 = 12
    U32 = 14
    S24 = 16
    U24 = 18
    S20 = 20
    U20 = 22
    S18 = 24
    U18 = 26
    F32 = 28
    F64 = 30


class AudioFormatFlags:
    """"""
    INTEGER = 1
    FLOAT = 2
    SIGNED = 4
    COMPLEX = 16
    UNPACK = 32


class AudioLayout:
    """"""
    INTERLEAVED = 0
    NON_INTERLEAVED = 1


class AudioNoiseShapingMethod:
    """"""
    NONE = 0
    ERROR_FEEDBACK = 1
    SIMPLE = 2
    MEDIUM = 3
    HIGH = 4


class AudioPackFlags:
    """"""
    NONE = 0
    TRUNCATE_RANGE = 1


class AudioQuantizeFlags:
    """"""
    NONE = 0
    NON_INTERLEAVED = 1


class AudioResamplerFilterInterpolation:
    """"""
    NONE = 0
    LINEAR = 1
    CUBIC = 2


class AudioResamplerFilterMode:
    """"""
    INTERPOLATED = 0
    FULL = 1
    AUTO = 2


class AudioResamplerFlags:
    """"""
    NONE = 0
    NON_INTERLEAVED_IN = 1
    NON_INTERLEAVED_OUT = 2
    VARIABLE_RATE = 4


class AudioResamplerMethod:
    """"""
    NEAREST = 0
    LINEAR = 1
    CUBIC = 2
    BLACKMAN_NUTTALL = 3
    KAISER = 4


class AudioRingBufferFormatType:
    """"""
    RAW = 0
    MU_LAW = 1
    A_LAW = 2
    IMA_ADPCM = 3
    MPEG = 4
    GSM = 5
    IEC958 = 6
    AC3 = 7
    EAC3 = 8
    DTS = 9
    MPEG2_AAC = 10
    MPEG4_AAC = 11
    MPEG2_AAC_RAW = 12
    MPEG4_AAC_RAW = 13
    FLAC = 14


class AudioRingBufferState:
    """"""
    STOPPED = 0
    PAUSED = 1
    STARTED = 2
    ERROR = 3
META_TAG_AUDIO_CHANNELS_STR = r"""channels"""
META_TAG_AUDIO_RATE_STR = r"""rate"""
META_TAG_AUDIO_STR = r"""audio"""


class StreamVolumeFormat:
    """"""
    LINEAR = 0
    CUBIC = 1
    DB = 2

def audio_buffer_clip(buffer=None, segment=None, rate=None, bpf=None):
    """"""
    return object

def audio_buffer_reorder_channels(buffer=None, format=None, channels=None, _from=None, to=None):
    """"""
    return object

def audio_channel_get_fallback_mask(channels=None):
    """"""
    return object

def audio_channel_mixer_new(flags=None, format=None, in_channels=None, in_position=None, out_channels=None, out_position=None):
    """"""
    return object

def audio_channel_mixer_new_with_matrix(flags=None, format=None, in_channels=None, out_channels=None, matrix=None):
    """"""
    return object

def audio_channel_positions_from_mask(channels=None, channel_mask=None, position=None):
    """"""
    return object

def audio_channel_positions_to_mask(position=None, channels=None, force_order=None, channel_mask=None):
    """"""
    return object

def audio_channel_positions_to_string(position=None, channels=None):
    """"""
    return object

def audio_channel_positions_to_valid_order(position=None, channels=None):
    """"""
    return object

def audio_check_valid_channel_positions(position=None, channels=None, force_order=None):
    """"""
    return object

def audio_clipping_meta_api_get_type():
    """"""
    return object

def audio_clipping_meta_get_info():
    """"""
    return object

def audio_downmix_meta_api_get_type():
    """"""
    return object

def audio_downmix_meta_get_info():
    """"""
    return object

def audio_format_build_integer(sign=None, endianness=None, width=None, depth=None):
    """"""
    return object

def audio_format_fill_silence(info=None, dest=None, length=None):
    """"""
    return object

def audio_format_from_string(format=None):
    """"""
    return object

def audio_format_get_info(format=None):
    """"""
    return object

def audio_format_info_get_type():
    """"""
    return object

def audio_format_to_string(format=None):
    """"""
    return object

def audio_get_channel_reorder_map(channels=None, _from=None, to=None, reorder_map=None):
    """"""
    return object

def audio_iec61937_frame_size(spec=None):
    """"""
    return object

def audio_iec61937_payload(src=None, src_n=None, dst=None, dst_n=None, spec=None, endianness=None):
    """"""
    return object

def audio_quantize_new(dither=None, ns=None, flags=None, format=None, channels=None, quantizer=None):
    """"""
    return object

def audio_reorder_channels(data=None, size=None, format=None, channels=None, _from=None, to=None):
    """"""
    return object

def audio_resampler_new(method=None, flags=None, format=None, channels=None, in_rate=None, out_rate=None, options=None):
    """"""
    return object

def audio_resampler_options_set_quality(method=None, quality=None, in_rate=None, out_rate=None, options=None):
    """"""
    return object

def buffer_add_audio_clipping_meta(buffer=None, format=None, start=None, end=None):
    """"""
    return object

def buffer_add_audio_downmix_meta(buffer=None, from_position=None, from_channels=None, to_position=None, to_channels=None, matrix=None):
    """"""
    return object

def buffer_get_audio_downmix_meta_for_channels(buffer=None, to_position=None, to_channels=None):
    """"""
    return object

def stream_volume_convert_volume(_from=None, to=None, val=None):
    """"""
    return object


class AudioAggregator(GstBase.Aggregator):
    """"""
    
    def aggregate_one_buffer(self, pad=None, inbuf=None, in_offset=None, outbuf=None, out_offset=None, num_frames=None):
        """"""
        return object
    
    def create_output_buffer(self, num_frames=None):
        """"""
        return object
    
    def set_sink_caps(self, pad=None, caps=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def current_caps(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioAggregatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def create_output_buffer(self):
        return object

    @property
    def aggregate_one_buffer(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioAggregatorConvertPadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioAggregatorConvertPadPrivate():
    """"""


class AudioAggregatorPad(GstBase.AggregatorPad):
    """"""
    
    def convert_buffer(self, in_info=None, out_info=None, buffer=None):
        """"""
        return object
    
    def update_conversion_info(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def info(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioAggregatorPadClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def convert_buffer(self):
        return object

    @property
    def update_conversion_info(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioAggregatorPadPrivate():
    """"""


class AudioAggregatorPrivate():
    """"""


class AudioBaseSink(GstBase.BaseSink):
    """"""
    
    def create_ringbuffer(self):
        """"""
        return object
    
    def payload(self, buffer=None):
        """"""
        return object
    
    def create_ringbuffer(self):
        """"""
        return object
    
    def get_alignment_threshold(self):
        """"""
        return object
    
    def get_discont_wait(self):
        """"""
        return object
    
    def get_drift_tolerance(self):
        """"""
        return object
    
    def get_provide_clock(self):
        """"""
        return object
    
    def get_slave_method(self):
        """"""
        return object
    
    def report_device_failure(self):
        """"""
        return object
    
    def set_alignment_threshold(self, alignment_threshold=None):
        """"""
        return object
    
    def set_custom_slaving_callback(self, callback=None, user_data=None, notify=None):
        """"""
        return object
    
    def set_discont_wait(self, discont_wait=None):
        """"""
        return object
    
    def set_drift_tolerance(self, drift_tolerance=None):
        """"""
        return object
    
    def set_provide_clock(self, provide=None):
        """"""
        return object
    
    def set_slave_method(self, method=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def ringbuffer(self):
        return object

    @property
    def buffer_time(self):
        return object

    @property
    def latency_time(self):
        return object

    @property
    def next_sample(self):
        return object

    @property
    def provided_clock(self):
        return object

    @property
    def eos_rendering(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioBaseSinkClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def create_ringbuffer(self):
        return object

    @property
    def payload(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioBaseSinkPrivate():
    """"""


class AudioBaseSrc(GstBase.PushSrc):
    """"""
    
    def create_ringbuffer(self):
        """"""
        return object
    
    def create_ringbuffer(self):
        """"""
        return object
    
    def get_provide_clock(self):
        """"""
        return object
    
    def get_slave_method(self):
        """"""
        return object
    
    def set_provide_clock(self, provide=None):
        """"""
        return object
    
    def set_slave_method(self, method=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def ringbuffer(self):
        return object

    @property
    def buffer_time(self):
        return object

    @property
    def latency_time(self):
        return object

    @property
    def next_sample(self):
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


class AudioBaseSrcClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def create_ringbuffer(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioBaseSrcPrivate():
    """"""


class AudioCdSrc(GstBase.PushSrc, Gst.URIHandler):
    """"""
    
    def close(self):
        """"""
        return object
    
    def open(self, device=None):
        """"""
        return object
    
    def read_sector(self, sector=None):
        """"""
        return object
    
    def add_track(self, track=None):
        """"""
        return object

    @property
    def pushsrc(self):
        return object

    @property
    def tags(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _gst_reserved1(self):
        return object

    @property
    def _gst_reserved2(self):
        return object


class AudioCdSrcClass():
    """"""

    @property
    def pushsrc_class(self):
        return object

    @property
    def open(self):
        return object

    @property
    def close(self):
        return object

    @property
    def read_sector(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioCdSrcPrivate():
    """"""


class AudioCdSrcTrack():
    """"""

    @property
    def is_audio(self):
        return object

    @property
    def num(self):
        return object

    @property
    def start(self):
        return object

    @property
    def end(self):
        return object

    @property
    def tags(self):
        return object

    @property
    def _gst_reserved1(self):
        return object

    @property
    def _gst_reserved2(self):
        return object


class AudioChannelMixer():
    """"""
    
    def free(self):
        """"""
        return object
    
    def is_passthrough(self):
        """"""
        return object
    
    def samples(self, _in=None, out=None, samples=None):
        """"""
        return object
    @staticmethod
    def new(flags=None, format=None, in_channels=None, in_position=None, out_channels=None, out_position=None):
        """"""
        return object
    @staticmethod
    def new_with_matrix(flags=None, format=None, in_channels=None, out_channels=None, matrix=None):
        """"""
        return object


class AudioClippingMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def format(self):
        return object

    @property
    def start(self):
        return object

    @property
    def end(self):
        return object


class AudioClock(Gst.SystemClock):
    """"""
    
    def __init__(self, name=None, func=None, user_data=None, destroy_notify=None):
        """"""
        return object
    @staticmethod
    def new(name=None, func=None, user_data=None, destroy_notify=None):
        """"""
        return object
    
    def adjust(self, time=None):
        """"""
        return object
    
    def get_time(self):
        """"""
        return object
    
    def invalidate(self):
        """"""
        return object
    
    def reset(self, time=None):
        """"""
        return object

    @property
    def clock(self):
        return object

    @property
    def func(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def destroy_notify(self):
        return object

    @property
    def last_time(self):
        return object

    @property
    def time_offset(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioClockClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioConverter():
    """"""
    
    def __init__(self, flags=None, in_info=None, out_info=None, config=None):
        """"""
        return object
    @staticmethod
    def new(flags=None, in_info=None, out_info=None, config=None):
        """"""
        return object
    
    def convert(self, flags=None, _in=None, in_size=None, out=None, out_size=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_config(self, in_rate=None, out_rate=None):
        """"""
        return object
    
    def get_in_frames(self, out_frames=None):
        """"""
        return object
    
    def get_max_latency(self):
        """"""
        return object
    
    def get_out_frames(self, in_frames=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def samples(self, flags=None, _in=None, in_frames=None, out=None, out_frames=None):
        """"""
        return object
    
    def supports_inplace(self):
        """"""
        return object
    
    def update_config(self, in_rate=None, out_rate=None, config=None):
        """"""
        return object


class AudioDecoder(Gst.Element):
    """"""
    
    def close(self):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def flush(self, hard=None):
        """"""
        return object
    
    def getcaps(self, filter=None):
        """"""
        return object
    
    def handle_frame(self, buffer=None):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def parse(self, adapter=None, offset=None, length=None):
        """"""
        return object
    
    def pre_push(self, buffer=None):
        """"""
        return object
    
    def propose_allocation(self, query=None):
        """"""
        return object
    
    def set_format(self, caps=None):
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
    
    def transform_meta(self, outbuf=None, meta=None, inbuf=None):
        """"""
        return object
    
    def allocate_output_buffer(self, size=None):
        """"""
        return object
    
    def finish_frame(self, buf=None, frames=None):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_audio_info(self):
        """"""
        return object
    
    def get_delay(self):
        """"""
        return object
    
    def get_drainable(self):
        """"""
        return object
    
    def get_estimate_rate(self):
        """"""
        return object
    
    def get_latency(self, min=None, max=None):
        """"""
        return object
    
    def get_max_errors(self):
        """"""
        return object
    
    def get_min_latency(self):
        """"""
        return object
    
    def get_needs_format(self):
        """"""
        return object
    
    def get_parse_state(self, sync=None, eos=None):
        """"""
        return object
    
    def get_plc(self):
        """"""
        return object
    
    def get_plc_aware(self):
        """"""
        return object
    
    def get_tolerance(self):
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
    
    def set_allocation_caps(self, allocation_caps=None):
        """"""
        return object
    
    def set_drainable(self, enabled=None):
        """"""
        return object
    
    def set_estimate_rate(self, enabled=None):
        """"""
        return object
    
    def set_latency(self, min=None, max=None):
        """"""
        return object
    
    def set_max_errors(self, num=None):
        """"""
        return object
    
    def set_min_latency(self, num=None):
        """"""
        return object
    
    def set_needs_format(self, enabled=None):
        """"""
        return object
    
    def set_output_format(self, info=None):
        """"""
        return object
    
    def set_plc(self, enabled=None):
        """"""
        return object
    
    def set_plc_aware(self, plc=None):
        """"""
        return object
    
    def set_tolerance(self, tolerance=None):
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
    def _gst_reserved(self):
        return object


class AudioDecoderClass():
    """"""

    @property
    def element_class(self):
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
    def parse(self):
        return object

    @property
    def handle_frame(self):
        return object

    @property
    def flush(self):
        return object

    @property
    def pre_push(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def open(self):
        return object

    @property
    def close(self):
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
    def sink_query(self):
        return object

    @property
    def src_query(self):
        return object

    @property
    def getcaps(self):
        return object

    @property
    def transform_meta(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioDecoderPrivate():
    """"""


class AudioDownmixMeta():
    """"""
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def meta(self):
        return object

    @property
    def from_position(self):
        return object

    @property
    def to_position(self):
        return object

    @property
    def from_channels(self):
        return object

    @property
    def to_channels(self):
        return object

    @property
    def matrix(self):
        return object


class AudioEncoder(Gst.Element, Gst.Preset):
    """"""
    
    def close(self):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def flush(self):
        """"""
        return object
    
    def getcaps(self, filter=None):
        """"""
        return object
    
    def handle_frame(self, buffer=None):
        """"""
        return object
    
    def negotiate(self):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def pre_push(self, buffer=None):
        """"""
        return object
    
    def propose_allocation(self, query=None):
        """"""
        return object
    
    def set_format(self, info=None):
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
    
    def transform_meta(self, outbuf=None, meta=None, inbuf=None):
        """"""
        return object
    
    def allocate_output_buffer(self, size=None):
        """"""
        return object
    
    def finish_frame(self, buffer=None, samples=None):
        """"""
        return object
    
    def get_allocator(self, allocator=None, params=None):
        """"""
        return object
    
    def get_audio_info(self):
        """"""
        return object
    
    def get_drainable(self):
        """"""
        return object
    
    def get_frame_max(self):
        """"""
        return object
    
    def get_frame_samples_max(self):
        """"""
        return object
    
    def get_frame_samples_min(self):
        """"""
        return object
    
    def get_hard_min(self):
        """"""
        return object
    
    def get_hard_resync(self):
        """"""
        return object
    
    def get_latency(self, min=None, max=None):
        """"""
        return object
    
    def get_lookahead(self):
        """"""
        return object
    
    def get_mark_granule(self):
        """"""
        return object
    
    def get_perfect_timestamp(self):
        """"""
        return object
    
    def get_tolerance(self):
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
    
    def set_allocation_caps(self, allocation_caps=None):
        """"""
        return object
    
    def set_drainable(self, enabled=None):
        """"""
        return object
    
    def set_frame_max(self, num=None):
        """"""
        return object
    
    def set_frame_samples_max(self, num=None):
        """"""
        return object
    
    def set_frame_samples_min(self, num=None):
        """"""
        return object
    
    def set_hard_min(self, enabled=None):
        """"""
        return object
    
    def set_hard_resync(self, enabled=None):
        """"""
        return object
    
    def set_headers(self, headers=None):
        """"""
        return object
    
    def set_latency(self, min=None, max=None):
        """"""
        return object
    
    def set_lookahead(self, num=None):
        """"""
        return object
    
    def set_mark_granule(self, enabled=None):
        """"""
        return object
    
    def set_output_format(self, caps=None):
        """"""
        return object
    
    def set_perfect_timestamp(self, enabled=None):
        """"""
        return object
    
    def set_tolerance(self, tolerance=None):
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
    def _gst_reserved(self):
        return object


class AudioEncoderClass():
    """"""

    @property
    def element_class(self):
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
    def flush(self):
        return object

    @property
    def pre_push(self):
        return object

    @property
    def sink_event(self):
        return object

    @property
    def src_event(self):
        return object

    @property
    def getcaps(self):
        return object

    @property
    def open(self):
        return object

    @property
    def close(self):
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
    def transform_meta(self):
        return object

    @property
    def sink_query(self):
        return object

    @property
    def src_query(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioEncoderPrivate():
    """"""


class AudioFilter(GstBase.BaseTransform):
    """"""
    
    def setup(self, info=None):
        """"""
        return object

    @property
    def basetransform(self):
        return object

    @property
    def info(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioFilterClass():
    """"""
    
    def add_pad_templates(self, allowed_caps=None):
        """"""
        return object

    @property
    def basetransformclass(self):
        return object

    @property
    def setup(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioFormatInfo():
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
    def endianness(self):
        return object

    @property
    def width(self):
        return object

    @property
    def depth(self):
        return object

    @property
    def silence(self):
        return object

    @property
    def unpack_format(self):
        return object

    @property
    def unpack_func(self):
        return object

    @property
    def pack_func(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioInfo():
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def convert(self, src_fmt=None, src_val=None, dest_fmt=None, dest_val=None):
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
    
    def set_format(self, format=None, rate=None, channels=None, position=None):
        """"""
        return object
    
    def to_caps(self):
        """"""
        return object

    @property
    def finfo(self):
        return object

    @property
    def flags(self):
        return object

    @property
    def layout(self):
        return object

    @property
    def rate(self):
        return object

    @property
    def channels(self):
        return object

    @property
    def bpf(self):
        return object

    @property
    def position(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioQuantize():
    """"""
    
    def free(self):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def samples(self, _in=None, out=None, samples=None):
        """"""
        return object
    @staticmethod
    def new(dither=None, ns=None, flags=None, format=None, channels=None, quantizer=None):
        """"""
        return object


class AudioResampler():
    """"""
    
    def free(self):
        """"""
        return object
    
    def get_in_frames(self, out_frames=None):
        """"""
        return object
    
    def get_max_latency(self):
        """"""
        return object
    
    def get_out_frames(self, in_frames=None):
        """"""
        return object
    
    def resample(self, _in=None, in_frames=None, out=None, out_frames=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def update(self, in_rate=None, out_rate=None, options=None):
        """"""
        return object
    @staticmethod
    def new(method=None, flags=None, format=None, channels=None, in_rate=None, out_rate=None, options=None):
        """"""
        return object
    @staticmethod
    def options_set_quality(method=None, quality=None, in_rate=None, out_rate=None, options=None):
        """"""
        return object


class AudioRingBuffer(Gst.Object):
    """"""
    @staticmethod
    def debug_spec_buff(spec=None):
        """"""
        return object
    @staticmethod
    def debug_spec_caps(spec=None):
        """"""
        return object
    @staticmethod
    def parse_caps(spec=None, caps=None):
        """"""
        return object
    
    def acquire(self, spec=None):
        """"""
        return object
    
    def activate(self, active=None):
        """"""
        return object
    
    def clear_all(self):
        """"""
        return object
    
    def close_device(self):
        """"""
        return object
    
    def commit(self, sample=None, data=None, in_samples=None, out_samples=None, accum=None):
        """"""
        return object
    
    def delay(self):
        """"""
        return object
    
    def open_device(self):
        """"""
        return object
    
    def pause(self):
        """"""
        return object
    
    def release(self):
        """"""
        return object
    
    def resume(self):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def stop(self):
        """"""
        return object
    
    def acquire(self, spec=None):
        """"""
        return object
    
    def activate(self, active=None):
        """"""
        return object
    
    def advance(self, advance=None):
        """"""
        return object
    
    def clear(self, segment=None):
        """"""
        return object
    
    def clear_all(self):
        """"""
        return object
    
    def close_device(self):
        """"""
        return object
    
    def commit(self, sample=None, data=None, in_samples=None, out_samples=None, accum=None):
        """"""
        return object
    
    def convert(self, src_fmt=None, src_val=None, dest_fmt=None, dest_val=None):
        """"""
        return object
    
    def delay(self):
        """"""
        return object
    
    def device_is_open(self):
        """"""
        return object
    
    def is_acquired(self):
        """"""
        return object
    
    def is_active(self):
        """"""
        return object
    
    def is_flushing(self):
        """"""
        return object
    
    def may_start(self, allowed=None):
        """"""
        return object
    
    def open_device(self):
        """"""
        return object
    
    def pause(self):
        """"""
        return object
    
    def prepare_read(self, segment=None, readptr=None, len=None):
        """"""
        return object
    
    def read(self, sample=None, data=None, len=None, timestamp=None):
        """"""
        return object
    
    def release(self):
        """"""
        return object
    
    def samples_done(self):
        """"""
        return object
    
    def set_callback(self, cb=None, user_data=None):
        """"""
        return object
    
    def set_callback_full(self, cb=None, user_data=None, notify=None):
        """"""
        return object
    
    def set_channel_positions(self, position=None):
        """"""
        return object
    
    def set_flushing(self, flushing=None):
        """"""
        return object
    
    def set_sample(self, sample=None):
        """"""
        return object
    
    def set_timestamp(self, readseg=None, timestamp=None):
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
    def cond(self):
        return object

    @property
    def open(self):
        return object

    @property
    def acquired(self):
        return object

    @property
    def memory(self):
        return object

    @property
    def size(self):
        return object

    @property
    def timestamps(self):
        return object

    @property
    def spec(self):
        return object

    @property
    def samples_per_seg(self):
        return object

    @property
    def empty_seg(self):
        return object

    @property
    def state(self):
        return object

    @property
    def segdone(self):
        return object

    @property
    def segbase(self):
        return object

    @property
    def waiting(self):
        return object

    @property
    def callback(self):
        return object

    @property
    def cb_data(self):
        return object

    @property
    def need_reorder(self):
        return object

    @property
    def channel_reorder_map(self):
        return object

    @property
    def flushing(self):
        return object

    @property
    def may_start(self):
        return object

    @property
    def active(self):
        return object

    @property
    def cb_data_notify(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioRingBufferClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def open_device(self):
        return object

    @property
    def acquire(self):
        return object

    @property
    def release(self):
        return object

    @property
    def close_device(self):
        return object

    @property
    def start(self):
        return object

    @property
    def pause(self):
        return object

    @property
    def resume(self):
        return object

    @property
    def stop(self):
        return object

    @property
    def delay(self):
        return object

    @property
    def activate(self):
        return object

    @property
    def commit(self):
        return object

    @property
    def clear_all(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioRingBufferSpec():
    """"""

    @property
    def caps(self):
        return object

    @property
    def type(self):
        return object

    @property
    def info(self):
        return object

    @property
    def latency_time(self):
        return object

    @property
    def buffer_time(self):
        return object

    @property
    def segsize(self):
        return object

    @property
    def segtotal(self):
        return object

    @property
    def seglatency(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioSink(AudioBaseSink):
    """"""
    
    def close(self):
        """"""
        return object
    
    def delay(self):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def prepare(self, spec=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def unprepare(self):
        """"""
        return object
    
    def write(self, data=None, length=None):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def thread(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioSinkClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def open(self):
        return object

    @property
    def prepare(self):
        return object

    @property
    def unprepare(self):
        return object

    @property
    def close(self):
        return object

    @property
    def write(self):
        return object

    @property
    def delay(self):
        return object

    @property
    def reset(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioSrc(AudioBaseSrc):
    """"""
    
    def close(self):
        """"""
        return object
    
    def delay(self):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def prepare(self, spec=None):
        """"""
        return object
    
    def read(self, data=None, length=None, timestamp=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def unprepare(self):
        """"""
        return object

    @property
    def element(self):
        return object

    @property
    def thread(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioSrcClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def open(self):
        return object

    @property
    def prepare(self):
        return object

    @property
    def unprepare(self):
        return object

    @property
    def close(self):
        return object

    @property
    def read(self):
        return object

    @property
    def delay(self):
        return object

    @property
    def reset(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class AudioStreamAlign():
    """"""
    
    def __init__(self, rate=None, alignment_threshold=None, discont_wait=None):
        """"""
        return object
    @staticmethod
    def new(rate=None, alignment_threshold=None, discont_wait=None):
        """"""
        return object
    
    def copy(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def get_alignment_threshold(self):
        """"""
        return object
    
    def get_discont_wait(self):
        """"""
        return object
    
    def get_rate(self):
        """"""
        return object
    
    def get_samples_since_discont(self):
        """"""
        return object
    
    def get_timestamp_at_discont(self):
        """"""
        return object
    
    def mark_discont(self):
        """"""
        return object
    
    def process(self, discont=None, timestamp=None, n_samples=None, out_timestamp=None, out_duration=None, out_sample_position=None):
        """"""
        return object
    
    def set_alignment_threshold(self, alignment_threshold=None):
        """"""
        return object
    
    def set_discont_wait(self, discont_wait=None):
        """"""
        return object
    
    def set_rate(self, rate=None):
        """"""
        return object


class StreamVolume():
    """"""
    @staticmethod
    def convert_volume(_from=None, to=None, val=None):
        """"""
        return object
    
    def get_mute(self):
        """"""
        return object
    
    def get_volume(self, format=None):
        """"""
        return object
    
    def set_mute(self, mute=None):
        """"""
        return object
    
    def set_volume(self, format=None, val=None):
        """"""
        return object


class StreamVolumeInterface():
    """"""

    @property
    def iface(self):
        return object


class AudioAggregatorConvertPad(AudioAggregatorPad):
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
