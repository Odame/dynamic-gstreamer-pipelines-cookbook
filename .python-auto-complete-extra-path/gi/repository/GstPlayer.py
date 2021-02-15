# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import Gst


class PlayerColorBalanceType:
    """"""
    HUE = 3
    BRIGHTNESS = 0
    SATURATION = 2
    CONTRAST = 1


class PlayerError:
    """"""
    FAILED = 0


class PlayerSnapshotFormat:
    """"""
    RAW_NATIVE = 0
    RAW_XRGB = 1
    RAW_BGRX = 2
    JPG = 3
    PNG = 4


class PlayerState:
    """"""
    STOPPED = 0
    BUFFERING = 1
    PAUSED = 2
    PLAYING = 3

def player_color_balance_type_get_name(type=None):
    """"""
    return object

def player_error_get_name(error=None):
    """"""
    return object

def player_error_quark():
    """"""
    return object

def player_state_get_name(state=None):
    """"""
    return object


class Player(Gst.Object):
    """"""
    
    def __init__(self, video_renderer=None, signal_dispatcher=None):
        """"""
        return object
    @staticmethod
    def new(video_renderer=None, signal_dispatcher=None):
        """"""
        return object
    @staticmethod
    def config_get_position_update_interval(config=None):
        """"""
        return object
    @staticmethod
    def config_get_seek_accurate(config=None):
        """"""
        return object
    @staticmethod
    def config_get_user_agent(config=None):
        """"""
        return object
    @staticmethod
    def config_set_position_update_interval(config=None, interval=None):
        """"""
        return object
    @staticmethod
    def config_set_seek_accurate(config=None, accurate=None):
        """"""
        return object
    @staticmethod
    def config_set_user_agent(config=None, agent=None):
        """"""
        return object
    @staticmethod
    def get_audio_streams(info=None):
        """"""
        return object
    @staticmethod
    def get_subtitle_streams(info=None):
        """"""
        return object
    @staticmethod
    def get_video_streams(info=None):
        """"""
        return object
    @staticmethod
    def visualizations_free(viss=None):
        """"""
        return object
    @staticmethod
    def visualizations_get():
        """"""
        return object
    
    def get_audio_video_offset(self):
        """"""
        return object
    
    def get_color_balance(self, type=None):
        """"""
        return object
    
    def get_config(self):
        """"""
        return object
    
    def get_current_audio_track(self):
        """"""
        return object
    
    def get_current_subtitle_track(self):
        """"""
        return object
    
    def get_current_video_track(self):
        """"""
        return object
    
    def get_current_visualization(self):
        """"""
        return object
    
    def get_duration(self):
        """"""
        return object
    
    def get_media_info(self):
        """"""
        return object
    
    def get_multiview_flags(self):
        """"""
        return object
    
    def get_multiview_mode(self):
        """"""
        return object
    
    def get_mute(self):
        """"""
        return object
    
    def get_pipeline(self):
        """"""
        return object
    
    def get_position(self):
        """"""
        return object
    
    def get_rate(self):
        """"""
        return object
    
    def get_subtitle_uri(self):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_video_snapshot(self, format=None, config=None):
        """"""
        return object
    
    def get_volume(self):
        """"""
        return object
    
    def has_color_balance(self):
        """"""
        return object
    
    def pause(self):
        """"""
        return object
    
    def play(self):
        """"""
        return object
    
    def seek(self, position=None):
        """"""
        return object
    
    def set_audio_track(self, stream_index=None):
        """"""
        return object
    
    def set_audio_track_enabled(self, enabled=None):
        """"""
        return object
    
    def set_audio_video_offset(self, offset=None):
        """"""
        return object
    
    def set_color_balance(self, type=None, value=None):
        """"""
        return object
    
    def set_config(self, config=None):
        """"""
        return object
    
    def set_multiview_flags(self, flags=None):
        """"""
        return object
    
    def set_multiview_mode(self, mode=None):
        """"""
        return object
    
    def set_mute(self, val=None):
        """"""
        return object
    
    def set_rate(self, rate=None):
        """"""
        return object
    
    def set_subtitle_track(self, stream_index=None):
        """"""
        return object
    
    def set_subtitle_track_enabled(self, enabled=None):
        """"""
        return object
    
    def set_subtitle_uri(self, uri=None):
        """"""
        return object
    
    def set_uri(self, uri=None):
        """"""
        return object
    
    def set_video_track(self, stream_index=None):
        """"""
        return object
    
    def set_video_track_enabled(self, enabled=None):
        """"""
        return object
    
    def set_visualization(self, name=None):
        """"""
        return object
    
    def set_visualization_enabled(self, enabled=None):
        """"""
        return object
    
    def set_volume(self, val=None):
        """"""
        return object
    
    def stop(self):
        """"""
        return object


class PlayerAudioInfoClass():
    """"""


class PlayerClass():
    """"""


class PlayerGMainContextSignalDispatcherClass():
    """"""


class PlayerMediaInfo(GObject.Object):
    """"""
    
    def get_audio_streams(self):
        """"""
        return object
    
    def get_container_format(self):
        """"""
        return object
    
    def get_duration(self):
        """"""
        return object
    
    def get_image_sample(self):
        """"""
        return object
    
    def get_number_of_audio_streams(self):
        """"""
        return object
    
    def get_number_of_streams(self):
        """"""
        return object
    
    def get_number_of_subtitle_streams(self):
        """"""
        return object
    
    def get_number_of_video_streams(self):
        """"""
        return object
    
    def get_stream_list(self):
        """"""
        return object
    
    def get_subtitle_streams(self):
        """"""
        return object
    
    def get_tags(self):
        """"""
        return object
    
    def get_title(self):
        """"""
        return object
    
    def get_uri(self):
        """"""
        return object
    
    def get_video_streams(self):
        """"""
        return object
    
    def is_live(self):
        """"""
        return object
    
    def is_seekable(self):
        """"""
        return object


class PlayerMediaInfoClass():
    """"""


class PlayerSignalDispatcher():
    """"""
    
    def dispatch(self, player=None, emitter=None, data=None, destroy=None):
        """"""
        return object


class PlayerSignalDispatcherInterface():
    """"""

    @property
    def parent_iface(self):
        return object

    @property
    def dispatch(self):
        return object


class PlayerStreamInfo(GObject.Object):
    """"""
    
    def get_caps(self):
        """"""
        return object
    
    def get_codec(self):
        """"""
        return object
    
    def get_index(self):
        """"""
        return object
    
    def get_stream_type(self):
        """"""
        return object
    
    def get_tags(self):
        """"""
        return object


class PlayerStreamInfoClass():
    """"""


class PlayerSubtitleInfo(PlayerStreamInfo):
    """"""
    
    def get_language(self):
        """"""
        return object


class PlayerSubtitleInfoClass():
    """"""


class PlayerVideoInfo(PlayerStreamInfo):
    """"""
    
    def get_bitrate(self):
        """"""
        return object
    
    def get_framerate(self, fps_n=None, fps_d=None):
        """"""
        return object
    
    def get_height(self):
        """"""
        return object
    
    def get_max_bitrate(self):
        """"""
        return object
    
    def get_pixel_aspect_ratio(self, par_n=None, par_d=None):
        """"""
        return object
    
    def get_width(self):
        """"""
        return object


class PlayerVideoInfoClass():
    """"""


class PlayerVideoOverlayVideoRendererClass():
    """"""


class PlayerVideoRenderer():
    """"""
    
    def create_video_sink(self, player=None):
        """"""
        return object


class PlayerVideoRendererInterface():
    """"""

    @property
    def parent_iface(self):
        return object

    @property
    def create_video_sink(self):
        return object


class PlayerVisualization():
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
    def description(self):
        return object


class PlayerAudioInfo(PlayerStreamInfo):
    """"""
    
    def get_bitrate(self):
        """"""
        return object
    
    def get_channels(self):
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


class PlayerGMainContextSignalDispatcher(GObject.Object, PlayerSignalDispatcher):
    """"""
    @staticmethod
    def new(application_context=None):
        """"""
        return object


class PlayerVideoOverlayVideoRenderer(GObject.Object, PlayerVideoRenderer):
    """"""
    @staticmethod
    def new(window_handle=None):
        """"""
        return object
    @staticmethod
    def new_with_sink(window_handle=None, video_sink=None):
        """"""
        return object
    
    def expose(self):
        """"""
        return object
    
    def get_render_rectangle(self, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def get_window_handle(self):
        """"""
        return object
    
    def set_render_rectangle(self, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def set_window_handle(self, window_handle=None):
        """"""
        return object
