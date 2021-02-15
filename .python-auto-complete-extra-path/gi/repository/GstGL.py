# -*- coding: utf-8 -*-
from gi.repository import Gst
from gi.repository import GstBase
BUFFER_POOL_OPTION_GL_SYNC_META = r"""GstBufferPoolOptionGLSyncMeta"""
BUFFER_POOL_OPTION_GL_TEXTURE_TARGET_2D = r"""GstBufferPoolOptionGLTextureTarget2D"""
BUFFER_POOL_OPTION_GL_TEXTURE_TARGET_EXTERNAL_OES = r"""GstBufferPoolOptionGLTextureTargetExternalOES"""
BUFFER_POOL_OPTION_GL_TEXTURE_TARGET_RECTANGLE = r"""GstBufferPoolOptionGLTextureTargetRectangle"""
CAPS_FEATURE_MEMORY_GL_BUFFER = r"""memory:GLBuffer"""
CAPS_FEATURE_MEMORY_GL_MEMORY = r"""memory:GLMemory"""


class GLAPI:
    """"""
    NONE = 0
    OPENGL = 1
    OPENGL3 = 2
    GLES1 = 32768
    GLES2 = 65536
    ANY = 4294967295


class GLBaseMemoryError:
    """"""
    FAILED = 0
    OLD_LIBS = 1
    RESOURCE_UNAVAILABLE = 2


class GLBaseMemoryTransfer:
    """"""
    DOWNLOAD = 1048576
    UPLOAD = 2097152


class GLContextError:
    """"""
    FAILED = 0
    WRONG_CONFIG = 1
    WRONG_API = 2
    OLD_LIBS = 3
    CREATE_CONTEXT = 4
    RESOURCE_UNAVAILABLE = 5


class GLDisplayType:
    """"""
    NONE = 0
    X11 = 1
    WAYLAND = 2
    COCOA = 4
    WIN32 = 8
    DISPMANX = 16
    EGL = 32
    VIV_FB = 64
    GBM = 128
    ANY = 4294967295


class GLFormat:
    """"""
    LUMINANCE = 6409
    ALPHA = 6406
    LUMINANCE_ALPHA = 6410
    RED = 6403
    R8 = 33321
    RG = 33319
    RG8 = 33323
    RGB = 6407
    RGB8 = 32849
    RGB565 = 36194
    RGBA = 6408
    RGBA8 = 32856
    DEPTH_COMPONENT16 = 33189
    DEPTH24_STENCIL8 = 35056


class GLPlatform:
    """"""
    NONE = 0
    EGL = 1
    GLX = 2
    WGL = 4
    CGL = 8
    EAGL = 16
    ANY = 4294967295


class GLQueryType:
    """"""
    NONE = 0
    TIME_ELAPSED = 1
    TIMESTAMP = 2


class GLSLError:
    """"""
    COMPILE = 0
    LINK = 1
    PROGRAM = 2


class GLSLProfile:
    """"""
    NONE = 0
    ES = 1
    CORE = 2
    COMPATIBILITY = 4
    ANY = -1


class GLSLVersion:
    """"""
    NONE = 0
    _100 = 100
    _110 = 110
    _120 = 120
    _130 = 130
    _140 = 140
    _150 = 150
    _300 = 300
    _310 = 310
    _320 = 320
    _330 = 330
    _400 = 400
    _410 = 410
    _420 = 420
    _430 = 430
    _440 = 440
    _450 = 450


class GLStereoDownmix:
    """"""
    GREEN_MAGENTA_DUBOIS = 0
    RED_CYAN_DUBOIS = 1
    AMBER_BLUE_DUBOIS = 2


class GLTextureTarget:
    """"""
    NONE = 0
    _2D = 1
    RECTANGLE = 2
    EXTERNAL_OES = 3


class GLUploadReturn:
    """"""
    DONE = 1
    ERROR = -1
    UNSUPPORTED = -2
    RECONFIGURE = -3


class GLWindowError:
    """"""
    FAILED = 0
    OLD_LIBS = 1
    RESOURCE_UNAVAILABLE = 2
GL_ALLOCATION_PARAMS_ALLOC_FLAG_ALLOC = r"""1"""
GL_ALLOCATION_PARAMS_ALLOC_FLAG_BUFFER = r"""16"""
GL_ALLOCATION_PARAMS_ALLOC_FLAG_USER = r"""65536"""
GL_ALLOCATION_PARAMS_ALLOC_FLAG_VIDEO = r"""8"""
GL_ALLOCATION_PARAMS_ALLOC_FLAG_WRAP_GPU_HANDLE = r"""4"""
GL_ALLOCATION_PARAMS_ALLOC_FLAG_WRAP_SYSMEM = r"""2"""
GL_API_GLES1_NAME = r"""gles1"""
GL_API_GLES2_NAME = r"""gles2"""
GL_API_OPENGL3_NAME = r"""opengl3"""
GL_API_OPENGL_NAME = r"""opengl"""
GL_BASE_MEMORY_ALLOCATOR_NAME = r"""GLBaseMemory"""
GL_BUFFER_ALLOCATOR_NAME = r"""GLBuffer"""
GL_COLOR_CONVERT_FORMATS = r"""{ RGBA, RGB, RGBx, BGR, BGRx, BGRA, xRGB, xBGR, ARGB, ABGR, Y444, I420, YV12, Y42B, Y41B, NV12, NV21, YUY2, UYVY, AYUV, GRAY8, GRAY16_LE, GRAY16_BE, RGB16, BGR16 }"""
GL_COLOR_CONVERT_VIDEO_CAPS = r"""video/x-raw("""
GL_CONTEXT_TYPE_CGL = r"""gst.gl.context.CGL"""
GL_CONTEXT_TYPE_EAGL = r"""gst.gl.context.EAGL"""
GL_CONTEXT_TYPE_EGL = r"""gst.gl.context.EGL"""
GL_CONTEXT_TYPE_GLX = r"""gst.gl.context.GLX"""
GL_CONTEXT_TYPE_WGL = r"""gst.gl.context.WGL"""
GL_DISPLAY_CONTEXT_TYPE = r"""gst.gl.GLDisplay"""
GL_DISPLAY_EGL_NAME = r"""gst.gl.display.egl"""
GL_MEMORY_ALLOCATOR_NAME = r"""GLMemory"""
GL_MEMORY_PBO_ALLOCATOR_NAME = r"""GLMemoryPBO"""
GL_MEMORY_VIDEO_FORMATS_STR = r"""{ RGBA, BGRA, RGBx, BGRx, ARGB, ABGR, xRGB, xBGR, RGB, BGR, RGB16, BGR16, AYUV, I420, YV12, NV12, NV21, YUY2, UYVY, Y41B, Y42B, Y444, GRAY8, GRAY16_LE, GRAY16_BE }"""
GL_RENDERBUFFER_ALLOCATOR_NAME = r"""GLRenderbuffer"""
GL_TEXTURE_TARGET_2D_STR = r"""2D"""
GL_TEXTURE_TARGET_EXTERNAL_OES_STR = r"""external-oes"""
GL_TEXTURE_TARGET_RECTANGLE_STR = r"""rectangle"""
MAP_GL = r"""131072"""

def buffer_add_gl_sync_meta(context=None, buffer=None):
    """"""
    return object

def buffer_add_gl_sync_meta_full(context=None, buffer=None, data=None):
    """"""
    return object

def buffer_pool_config_get_gl_allocation_params(config=None):
    """"""
    return object

def buffer_pool_config_set_gl_allocation_params(config=None, params=None):
    """"""
    return object

def context_get_gl_display(context=None, display=None):
    """"""
    return object

def context_set_gl_display(context=None, display=None):
    """"""
    return object

def gl_api_from_string(api_s=None):
    """"""
    return object

def gl_api_to_string(api=None):
    """"""
    return object

def gl_async_debug_new():
    """"""
    return object

def gl_base_memory_alloc(allocator=None, params=None):
    """"""
    return object

def gl_base_memory_error_quark():
    """"""
    return object

def gl_base_memory_init_once():
    """"""
    return object

def gl_buffer_init_once():
    """"""
    return object

def gl_check_extension(name=None, ext=None):
    """"""
    return object

def gl_element_propagate_display_context(element=None, display=None):
    """"""
    return object

def gl_ensure_element_data(element=None, display_ptr=None, other_context_ptr=None):
    """"""
    return object

def gl_format_from_video_info(context=None, vinfo=None, plane=None):
    """"""
    return object

def gl_format_type_n_bytes(format=None, type=None):
    """"""
    return object

def gl_get_plane_data_size(info=None, align=None, plane=None):
    """"""
    return object

def gl_get_plane_start(info=None, valign=None, plane=None):
    """"""
    return object

def gl_handle_context_query(element=None, query=None, display=None, context=None, other_context=None):
    """"""
    return object

def gl_handle_set_context(element=None, context=None, display=None, other_context=None):
    """"""
    return object

def gl_insert_debug_marker(context=None, format=None, *args):
    """"""
    return object

def gl_memory_init_once():
    """"""
    return object

def gl_memory_pbo_init_once():
    """"""
    return object

def gl_platform_from_string(platform_s=None):
    """"""
    return object

def gl_platform_to_string(platform=None):
    """"""
    return object

def gl_query_local_gl_context(element=None, direction=None, context_ptr=None):
    """"""
    return object

def gl_query_new(context=None, query_type=None):
    """"""
    return object

def gl_renderbuffer_init_once():
    """"""
    return object

def gl_sized_gl_format_from_gl_format_type(context=None, format=None, type=None):
    """"""
    return object

def gl_sync_meta_api_get_type():
    """"""
    return object

def gl_sync_meta_get_info():
    """"""
    return object

def gl_texture_target_from_gl(target=None):
    """"""
    return object

def gl_texture_target_from_string(str=None):
    """"""
    return object

def gl_texture_target_to_buffer_pool_option(target=None):
    """"""
    return object

def gl_texture_target_to_gl(target=None):
    """"""
    return object

def gl_texture_target_to_string(target=None):
    """"""
    return object

def gl_value_get_texture_target_mask(value=None):
    """"""
    return object

def gl_value_set_texture_target(value=None, target=None):
    """"""
    return object

def gl_value_set_texture_target_from_mask(value=None, target_mask=None):
    """"""
    return object

def gl_version_to_glsl_version(gl_api=None, maj=None, min=None):
    """"""
    return object

def glsl_error_quark():
    """"""
    return object

def glsl_profile_from_string(string=None):
    """"""
    return object

def glsl_profile_to_string(profile=None):
    """"""
    return object

def glsl_string_get_version_profile(s=None, version=None, profile=None):
    """"""
    return object

def glsl_version_from_string(string=None):
    """"""
    return object

def glsl_version_profile_from_string(string=None, version_ret=None, profile_ret=None):
    """"""
    return object

def glsl_version_profile_to_string(version=None, profile=None):
    """"""
    return object

def glsl_version_to_string(version=None):
    """"""
    return object

def is_gl_base_memory(mem=None):
    """"""
    return object

def is_gl_buffer(mem=None):
    """"""
    return object

def is_gl_memory(mem=None):
    """"""
    return object

def is_gl_memory_pbo(mem=None):
    """"""
    return object

def is_gl_renderbuffer(mem=None):
    """"""
    return object


class GLAllocationParams():
    """"""
    
    def copy(self):
        """"""
        return object
    
    def copy_data(self, dest=None):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def free_data(self):
        """"""
        return object
    
    def init(self, struct_size=None, alloc_flags=None, copy=None, free=None, context=None, alloc_size=None, alloc_params=None, wrapped_data=None, gl_handle=None, user_data=None, notify=None):
        """"""
        return object

    @property
    def struct_size(self):
        return object

    @property
    def copy(self):
        return object

    @property
    def free(self):
        return object

    @property
    def alloc_flags(self):
        return object

    @property
    def alloc_size(self):
        return object

    @property
    def alloc_params(self):
        return object

    @property
    def context(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def wrapped_data(self):
        return object

    @property
    def gl_handle(self):
        return object

    @property
    def _padding(self):
        return object


class GLAsyncDebug():
    """"""
    
    def free(self):
        """"""
        return object
    
    def freeze(self):
        """"""
        return object
    
    def init(self):
        """"""
        return object
    
    def output_log_msg(self):
        """"""
        return object
    
    def store_log_msg(self, cat=None, level=None, file=None, function=None, line=None, object=None, format=None, *args):
        """"""
        return object
    
    def store_log_msg_valist(self, cat=None, level=None, file=None, function=None, line=None, object=None, format=None, varargs=None):
        """"""
        return object
    
    def thaw(self):
        """"""
        return object
    
    def unset(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object

    @property
    def state_flags(self):
        return object

    @property
    def cat(self):
        return object

    @property
    def level(self):
        return object

    @property
    def file(self):
        return object

    @property
    def function(self):
        return object

    @property
    def line(self):
        return object

    @property
    def object(self):
        return object

    @property
    def debug_msg(self):
        return object

    @property
    def callback(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def _padding(self):
        return object


class GLBaseFilter(GstBase.BaseTransform):
    """"""
    
    def gl_set_caps(self, incaps=None, outcaps=None):
        """"""
        return object
    
    def gl_start(self):
        """"""
        return object
    
    def gl_stop(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def display(self):
        return object

    @property
    def context(self):
        return object

    @property
    def in_caps(self):
        return object

    @property
    def out_caps(self):
        return object

    @property
    def _padding(self):
        return object

    @property
    def priv(self):
        return object


class GLBaseFilterClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def supported_gl_api(self):
        return object

    @property
    def gl_start(self):
        return object

    @property
    def gl_stop(self):
        return object

    @property
    def gl_set_caps(self):
        return object

    @property
    def _padding(self):
        return object


class GLBaseFilterPrivate():
    """"""


class GLBaseMemory():
    """"""
    
    def alloc_data(self):
        """"""
        return object
    
    def init(self, allocator=None, parent=None, context=None, params=None, size=None, user_data=None, notify=None):
        """"""
        return object
    
    def memcpy(self, dest=None, offset=None, size=None):
        """"""
        return object
    @staticmethod
    def alloc(allocator=None, params=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    @staticmethod
    def init_once():
        """"""
        return object

    @property
    def mem(self):
        return object

    @property
    def context(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def map_flags(self):
        return object

    @property
    def map_count(self):
        return object

    @property
    def gl_map_count(self):
        return object

    @property
    def data(self):
        return object

    @property
    def query(self):
        return object

    @property
    def alloc_size(self):
        return object

    @property
    def alloc_data(self):
        return object

    @property
    def notify(self):
        return object

    @property
    def user_data(self):
        return object

    @property
    def _padding(self):
        return object


class GLBaseMemoryAllocator(Gst.Allocator):
    """"""
    
    def alloc(self, params=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def fallback_mem_copy(self):
        return object

    @property
    def _padding(self):
        return object


class GLBaseMemoryAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def alloc(self):
        return object

    @property
    def create(self):
        return object

    @property
    def map(self):
        return object

    @property
    def unmap(self):
        return object

    @property
    def copy(self):
        return object

    @property
    def destroy(self):
        return object

    @property
    def _padding(self):
        return object


class GLBuffer():
    """"""
    @staticmethod
    def init_once():
        """"""
        return object

    @property
    def mem(self):
        return object

    @property
    def id(self):
        return object

    @property
    def target(self):
        return object

    @property
    def usage_hints(self):
        return object


class GLBufferAllocationParams():
    """"""
    
    def __init__(self, context=None, alloc_size=None, alloc_params=None, gl_target=None, gl_usage=None):
        """"""
        return object
    @staticmethod
    def new(context=None, alloc_size=None, alloc_params=None, gl_target=None, gl_usage=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def gl_target(self):
        return object

    @property
    def gl_usage(self):
        return object

    @property
    def _padding(self):
        return object


class GLBufferAllocator(GLBaseMemoryAllocator):
    """"""

    @property
    def parent(self):
        return object

    @property
    def _padding(self):
        return object


class GLBufferAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLBufferPool(Gst.BufferPool):
    """"""
    
    def __init__(self, context=None):
        """"""
        return object
    @staticmethod
    def new(context=None):
        """"""
        return object

    @property
    def bufferpool(self):
        return object

    @property
    def context(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _padding(self):
        return object


class GLBufferPoolClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLBufferPoolPrivate():
    """"""


class GLColorConvert(Gst.Object):
    """"""
    
    def __init__(self, context=None):
        """"""
        return object
    @staticmethod
    def new(context=None):
        """"""
        return object
    @staticmethod
    def fixate_caps(context=None, direction=None, caps=None, other=None):
        """"""
        return object
    @staticmethod
    def transform_caps(context=None, direction=None, caps=None, filter=None):
        """"""
        return object
    
    def decide_allocation(self, query=None):
        """"""
        return object
    
    def perform(self, inbuf=None):
        """"""
        return object
    
    def set_caps(self, in_caps=None, out_caps=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def context(self):
        return object

    @property
    def in_info(self):
        return object

    @property
    def out_info(self):
        return object

    @property
    def initted(self):
        return object

    @property
    def passthrough(self):
        return object

    @property
    def inbuf(self):
        return object

    @property
    def outbuf(self):
        return object

    @property
    def fbo(self):
        return object

    @property
    def shader(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _reserved(self):
        return object


class GLColorConvertClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLColorConvertPrivate():
    """"""


class GLContext(Gst.Object):
    """"""
    
    def __init__(self, display=None):
        """"""
        return object
    @staticmethod
    def new(display=None):
        """"""
        return object
    @staticmethod
    def new_wrapped(display=None, handle=None, context_type=None, available_apis=None):
        """"""
        return object
    @staticmethod
    def default_get_proc_address(gl_api=None, name=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    @staticmethod
    def get_current():
        """"""
        return object
    @staticmethod
    def get_current_gl_api(platform=None, major=None, minor=None):
        """"""
        return object
    @staticmethod
    def get_current_gl_context(context_type=None):
        """"""
        return object
    @staticmethod
    def get_proc_address_with_platform(context_type=None, gl_api=None, name=None):
        """"""
        return object
    
    def activate(self, activate=None):
        """"""
        return object
    
    def check_feature(self, feature=None):
        """"""
        return object
    
    def choose_format(self):
        """"""
        return object
    
    def create_context(self, gl_api=None, other_context=None):
        """"""
        return object
    
    def destroy_context(self):
        """"""
        return object
    
    def get_gl_api(self):
        """"""
        return object
    
    def get_gl_context(self):
        """"""
        return object
    
    def get_gl_platform(self):
        """"""
        return object
    
    def get_gl_platform_version(self, major=None, minor=None):
        """"""
        return object
    
    def swap_buffers(self):
        """"""
        return object
    
    def activate(self, activate=None):
        """"""
        return object
    
    def can_share(self, other_context=None):
        """"""
        return object
    
    def check_feature(self, feature=None):
        """"""
        return object
    
    def check_framebuffer_status(self, fbo_target=None):
        """"""
        return object
    
    def check_gl_version(self, api=None, maj=None, min=None):
        """"""
        return object
    
    def clear_framebuffer(self):
        """"""
        return object
    
    def clear_shader(self):
        """"""
        return object
    
    def create(self, other_context=None):
        """"""
        return object
    
    def destroy(self):
        """"""
        return object
    
    def fill_info(self):
        """"""
        return object
    
    def get_display(self):
        """"""
        return object
    
    def get_gl_api(self):
        """"""
        return object
    
    def get_gl_context(self):
        """"""
        return object
    
    def get_gl_platform(self):
        """"""
        return object
    
    def get_gl_platform_version(self, major=None, minor=None):
        """"""
        return object
    
    def get_gl_version(self, maj=None, min=None):
        """"""
        return object
    
    def get_proc_address(self, name=None):
        """"""
        return object
    
    def get_thread(self):
        """"""
        return object
    
    def get_window(self):
        """"""
        return object
    
    def is_shared(self):
        """"""
        return object
    
    def set_shared_with(self, share=None):
        """"""
        return object
    
    def set_window(self, window=None):
        """"""
        return object
    
    def supports_glsl_profile_version(self, version=None, profile=None):
        """"""
        return object
    
    def swap_buffers(self):
        """"""
        return object
    
    def thread_add(self, func=None, data=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def display(self):
        return object

    @property
    def window(self):
        return object

    @property
    def gl_vtable(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _reserved(self):
        return object


class GLContextClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_current_context(self):
        return object

    @property
    def get_gl_context(self):
        return object

    @property
    def get_gl_api(self):
        return object

    @property
    def get_gl_platform(self):
        return object

    @property
    def get_proc_address(self):
        return object

    @property
    def activate(self):
        return object

    @property
    def choose_format(self):
        return object

    @property
    def create_context(self):
        return object

    @property
    def destroy_context(self):
        return object

    @property
    def swap_buffers(self):
        return object

    @property
    def check_feature(self):
        return object

    @property
    def get_gl_platform_version(self):
        return object

    @property
    def _reserved(self):
        return object


class GLContextPrivate():
    """"""


class GLDisplay(Gst.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def create_window(self):
        """"""
        return object
    
    def get_handle(self):
        """"""
        return object
    
    def add_context(self, context=None):
        """"""
        return object
    
    def create_context(self, other_context=None, p_context=None):
        """"""
        return object
    
    def create_window(self):
        """"""
        return object
    
    def egl_from_gl_display(self):
        """"""
        return object
    
    def filter_gl_api(self, gl_api=None):
        """"""
        return object
    
    def find_window(self, data=None, compare_func=None):
        """"""
        return object
    
    def get_gl_api(self):
        """"""
        return object
    
    def get_gl_api_unlocked(self):
        """"""
        return object
    
    def get_gl_context_for_thread(self, thread=None):
        """"""
        return object
    
    def get_handle(self):
        """"""
        return object
    
    def get_handle_type(self):
        """"""
        return object
    
    def remove_window(self, window=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def type(self):
        return object

    @property
    def windows(self):
        return object

    @property
    def main_context(self):
        return object

    @property
    def main_loop(self):
        return object

    @property
    def event_source(self):
        return object

    @property
    def priv(self):
        return object


class GLDisplayClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def get_handle(self):
        return object

    @property
    def create_window(self):
        return object

    @property
    def _padding(self):
        return object


class GLDisplayEGL(GLDisplay):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def new_with_egl_display(display=None):
        """"""
        return object
    @staticmethod
    def get_from_native(type=None, display=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def display(self):
        return object

    @property
    def foreign_display(self):
        return object

    @property
    def _padding(self):
        return object


class GLDisplayEGLClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLDisplayPrivate():
    """"""


class GLDisplayWayland(GLDisplay):
    """"""
    
    def __init__(self, name=None):
        """"""
        return object
    @staticmethod
    def new(name=None):
        """"""
        return object
    @staticmethod
    def new_with_display(display=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def display(self):
        return object

    @property
    def registry(self):
        return object

    @property
    def compositor(self):
        return object

    @property
    def subcompositor(self):
        return object

    @property
    def shell(self):
        return object

    @property
    def foreign_display(self):
        return object

    @property
    def _padding(self):
        return object


class GLDisplayWaylandClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLDisplayX11(GLDisplay):
    """"""
    
    def __init__(self, name=None):
        """"""
        return object
    @staticmethod
    def new(name=None):
        """"""
        return object
    @staticmethod
    def new_with_display(display=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def name(self):
        return object

    @property
    def display(self):
        return object

    @property
    def xcb_connection(self):
        return object

    @property
    def foreign_display(self):
        return object

    @property
    def _padding(self):
        return object


class GLDisplayX11Class():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLFilter(GLBaseFilter):
    """"""
    @staticmethod
    def add_rgba_pad_templates(klass=None):
        """"""
        return object
    
    def filter(self, inbuf=None, outbuf=None):
        """"""
        return object
    
    def filter_texture(self, in_tex=None, out_tex=None):
        """"""
        return object
    
    def init_fbo(self):
        """"""
        return object
    
    def set_caps(self, incaps=None, outcaps=None):
        """"""
        return object
    
    def transform_internal_caps(self, direction=None, caps=None, filter_caps=None):
        """"""
        return object
    
    def draw_fullscreen_quad(self):
        """"""
        return object
    
    def filter_texture(self, inbuf=None, outbuf=None):
        """"""
        return object
    
    def render_to_target(self, input=None, output=None, func=None, data=None):
        """"""
        return object
    
    def render_to_target_with_shader(self, input=None, output=None, shader=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def in_info(self):
        return object

    @property
    def out_info(self):
        return object

    @property
    def in_texture_target(self):
        return object

    @property
    def out_texture_target(self):
        return object

    @property
    def out_caps(self):
        return object

    @property
    def fbo(self):
        return object

    @property
    def gl_result(self):
        return object

    @property
    def inbuf(self):
        return object

    @property
    def outbuf(self):
        return object

    @property
    def default_shader(self):
        return object

    @property
    def valid_attributes(self):
        return object

    @property
    def vao(self):
        return object

    @property
    def vbo_indices(self):
        return object

    @property
    def vertex_buffer(self):
        return object

    @property
    def draw_attr_position_loc(self):
        return object

    @property
    def draw_attr_texture_loc(self):
        return object

    @property
    def _padding(self):
        return object


class GLFilterClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def set_caps(self):
        return object

    @property
    def filter(self):
        return object

    @property
    def filter_texture(self):
        return object

    @property
    def init_fbo(self):
        return object

    @property
    def transform_internal_caps(self):
        return object

    @property
    def _padding(self):
        return object


class GLFramebuffer(Gst.Object):
    """"""
    
    def __init__(self, context=None):
        """"""
        return object
    @staticmethod
    def new(context=None):
        """"""
        return object
    @staticmethod
    def new_with_default_depth(context=None, width=None, height=None):
        """"""
        return object
    
    def attach(self, attachment_point=None, mem=None):
        """"""
        return object
    
    def bind(self):
        """"""
        return object
    
    def draw_to_texture(self, mem=None, func=None, user_data=None):
        """"""
        return object
    
    def get_effective_dimensions(self, width=None, height=None):
        """"""
        return object
    
    def get_id(self):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def context(self):
        return object

    @property
    def fbo_id(self):
        return object

    @property
    def attachments(self):
        return object

    @property
    def _padding(self):
        return object

    @property
    def priv(self):
        return object


class GLFramebufferClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLFramebufferPrivate():
    """"""


class GLFuncs():
    """"""

    @property
    def BindTexture(self):
        return object

    @property
    def BlendFunc(self):
        return object

    @property
    def Clear(self):
        return object

    @property
    def ClearColor(self):
        return object

    @property
    def ClearStencil(self):
        return object

    @property
    def ColorMask(self):
        return object

    @property
    def CopyTexSubImage2D(self):
        return object

    @property
    def DeleteTextures(self):
        return object

    @property
    def DepthFunc(self):
        return object

    @property
    def DepthMask(self):
        return object

    @property
    def Disable(self):
        return object

    @property
    def DrawArrays(self):
        return object

    @property
    def DrawElements(self):
        return object

    @property
    def Enable(self):
        return object

    @property
    def Finish(self):
        return object

    @property
    def Flush(self):
        return object

    @property
    def FrontFace(self):
        return object

    @property
    def CullFace(self):
        return object

    @property
    def GenTextures(self):
        return object

    @property
    def GetError(self):
        return object

    @property
    def GetIntegerv(self):
        return object

    @property
    def GetBooleanv(self):
        return object

    @property
    def GetFloatv(self):
        return object

    @property
    def GetString(self):
        return object

    @property
    def Hint(self):
        return object

    @property
    def IsTexture(self):
        return object

    @property
    def PixelStorei(self):
        return object

    @property
    def ReadPixels(self):
        return object

    @property
    def Scissor(self):
        return object

    @property
    def StencilFunc(self):
        return object

    @property
    def StencilMask(self):
        return object

    @property
    def StencilOp(self):
        return object

    @property
    def TexImage2D(self):
        return object

    @property
    def TexParameterfv(self):
        return object

    @property
    def TexParameteri(self):
        return object

    @property
    def TexParameteriv(self):
        return object

    @property
    def GetTexParameterfv(self):
        return object

    @property
    def GetTexParameteriv(self):
        return object

    @property
    def TexSubImage2D(self):
        return object

    @property
    def CopyTexImage2D(self):
        return object

    @property
    def Viewport(self):
        return object

    @property
    def IsEnabled(self):
        return object

    @property
    def LineWidth(self):
        return object

    @property
    def PolygonOffset(self):
        return object

    @property
    def TexParameterf(self):
        return object

    @property
    def TexImage3D(self):
        return object

    @property
    def TexSubImage3D(self):
        return object

    @property
    def CompressedTexImage2D(self):
        return object

    @property
    def CompressedTexSubImage2D(self):
        return object

    @property
    def SampleCoverage(self):
        return object

    @property
    def GetBufferParameteriv(self):
        return object

    @property
    def GenBuffers(self):
        return object

    @property
    def BindBuffer(self):
        return object

    @property
    def BufferData(self):
        return object

    @property
    def BufferSubData(self):
        return object

    @property
    def DeleteBuffers(self):
        return object

    @property
    def IsBuffer(self):
        return object

    @property
    def ActiveTexture(self):
        return object

    @property
    def MapBuffer(self):
        return object

    @property
    def UnmapBuffer(self):
        return object

    @property
    def GetStringi(self):
        return object

    @property
    def MapBufferRange(self):
        return object

    @property
    def BlendEquation(self):
        return object

    @property
    def BlendColor(self):
        return object

    @property
    def BlendFuncSeparate(self):
        return object

    @property
    def BlendEquationSeparate(self):
        return object

    @property
    def StencilFuncSeparate(self):
        return object

    @property
    def StencilMaskSeparate(self):
        return object

    @property
    def StencilOpSeparate(self):
        return object

    @property
    def EGLImageTargetTexture2D(self):
        return object

    @property
    def EGLImageTargetRenderbufferStorage(self):
        return object

    @property
    def GenRenderbuffers(self):
        return object

    @property
    def DeleteRenderbuffers(self):
        return object

    @property
    def BindRenderbuffer(self):
        return object

    @property
    def RenderbufferStorage(self):
        return object

    @property
    def GenFramebuffers(self):
        return object

    @property
    def BindFramebuffer(self):
        return object

    @property
    def FramebufferTexture2D(self):
        return object

    @property
    def FramebufferRenderbuffer(self):
        return object

    @property
    def IsRenderbuffer(self):
        return object

    @property
    def CheckFramebufferStatus(self):
        return object

    @property
    def DeleteFramebuffers(self):
        return object

    @property
    def GenerateMipmap(self):
        return object

    @property
    def GetFramebufferAttachmentParameteriv(self):
        return object

    @property
    def GetRenderbufferParameteriv(self):
        return object

    @property
    def IsFramebuffer(self):
        return object

    @property
    def BlitFramebuffer(self):
        return object

    @property
    def DiscardFramebuffer(self):
        return object

    @property
    def ReadBuffer(self):
        return object

    @property
    def DrawBuffers(self):
        return object

    @property
    def ClientActiveTexture(self):
        return object

    @property
    def AlphaFunc(self):
        return object

    @property
    def Fogf(self):
        return object

    @property
    def Fogfv(self):
        return object

    @property
    def LoadMatrixf(self):
        return object

    @property
    def Materialfv(self):
        return object

    @property
    def PointSize(self):
        return object

    @property
    def TexEnvfv(self):
        return object

    @property
    def Color4ub(self):
        return object

    @property
    def ColorPointer(self):
        return object

    @property
    def DisableClientState(self):
        return object

    @property
    def EnableClientState(self):
        return object

    @property
    def LoadIdentity(self):
        return object

    @property
    def MatrixMode(self):
        return object

    @property
    def NormalPointer(self):
        return object

    @property
    def TexCoordPointer(self):
        return object

    @property
    def TexEnvi(self):
        return object

    @property
    def VertexPointer(self):
        return object

    @property
    def PushMatrix(self):
        return object

    @property
    def PopMatrix(self):
        return object

    @property
    def PushAttrib(self):
        return object

    @property
    def PopAttrib(self):
        return object

    @property
    def TexImage1D(self):
        return object

    @property
    def Rotatef(self):
        return object

    @property
    def Translatef(self):
        return object

    @property
    def Scalef(self):
        return object

    @property
    def Lightfv(self):
        return object

    @property
    def ColorMaterial(self):
        return object

    @property
    def ShadeModel(self):
        return object

    @property
    def DepthRangef(self):
        return object

    @property
    def ClearDepthf(self):
        return object

    @property
    def ClipPlanef(self):
        return object

    @property
    def ReleaseShaderCompiler(self):
        return object

    @property
    def GetShaderPrecisionFormat(self):
        return object

    @property
    def ShaderBinary(self):
        return object

    @property
    def RenderbufferStorageMultisampleIMG(self):
        return object

    @property
    def FramebufferTexture2DMultisampleIMG(self):
        return object

    @property
    def GetTexLevelParameteriv(self):
        return object

    @property
    def GetTexImage(self):
        return object

    @property
    def DepthRange(self):
        return object

    @property
    def DrawBuffer(self):
        return object

    @property
    def ClearDepth(self):
        return object

    @property
    def ClipPlane(self):
        return object

    @property
    def CreateProgram(self):
        return object

    @property
    def CreateShader(self):
        return object

    @property
    def DeleteShader(self):
        return object

    @property
    def AttachShader(self):
        return object

    @property
    def UseProgram(self):
        return object

    @property
    def DeleteProgram(self):
        return object

    @property
    def GetShaderInfoLog(self):
        return object

    @property
    def GetProgramInfoLog(self):
        return object

    @property
    def GetShaderiv(self):
        return object

    @property
    def GetProgramiv(self):
        return object

    @property
    def DetachShader(self):
        return object

    @property
    def GetAttachedShaders(self):
        return object

    @property
    def IsShader(self):
        return object

    @property
    def IsProgram(self):
        return object

    @property
    def ShaderSource(self):
        return object

    @property
    def CompileShader(self):
        return object

    @property
    def LinkProgram(self):
        return object

    @property
    def GetUniformLocation(self):
        return object

    @property
    def Uniform1f(self):
        return object

    @property
    def Uniform2f(self):
        return object

    @property
    def Uniform3f(self):
        return object

    @property
    def Uniform4f(self):
        return object

    @property
    def Uniform1fv(self):
        return object

    @property
    def Uniform2fv(self):
        return object

    @property
    def Uniform3fv(self):
        return object

    @property
    def Uniform4fv(self):
        return object

    @property
    def Uniform1i(self):
        return object

    @property
    def Uniform2i(self):
        return object

    @property
    def Uniform3i(self):
        return object

    @property
    def Uniform4i(self):
        return object

    @property
    def Uniform1iv(self):
        return object

    @property
    def Uniform2iv(self):
        return object

    @property
    def Uniform3iv(self):
        return object

    @property
    def Uniform4iv(self):
        return object

    @property
    def UniformMatrix2fv(self):
        return object

    @property
    def UniformMatrix3fv(self):
        return object

    @property
    def UniformMatrix4fv(self):
        return object

    @property
    def GetUniformfv(self):
        return object

    @property
    def GetUniformiv(self):
        return object

    @property
    def GetActiveUniform(self):
        return object

    @property
    def GetShaderSource(self):
        return object

    @property
    def ValidateProgram(self):
        return object

    @property
    def VertexAttribPointer(self):
        return object

    @property
    def EnableVertexAttribArray(self):
        return object

    @property
    def DisableVertexAttribArray(self):
        return object

    @property
    def VertexAttrib1f(self):
        return object

    @property
    def VertexAttrib1fv(self):
        return object

    @property
    def VertexAttrib2f(self):
        return object

    @property
    def VertexAttrib2fv(self):
        return object

    @property
    def VertexAttrib3f(self):
        return object

    @property
    def VertexAttrib3fv(self):
        return object

    @property
    def VertexAttrib4f(self):
        return object

    @property
    def VertexAttrib4fv(self):
        return object

    @property
    def GetVertexAttribfv(self):
        return object

    @property
    def GetVertexAttribiv(self):
        return object

    @property
    def GetVertexAttribPointerv(self):
        return object

    @property
    def GetAttribLocation(self):
        return object

    @property
    def BindAttribLocation(self):
        return object

    @property
    def GetActiveAttrib(self):
        return object

    @property
    def CreateProgramObject(self):
        return object

    @property
    def CreateShaderObject(self):
        return object

    @property
    def DeleteObject(self):
        return object

    @property
    def AttachObject(self):
        return object

    @property
    def UseProgramObject(self):
        return object

    @property
    def GetInfoLog(self):
        return object

    @property
    def GetObjectParameteriv(self):
        return object

    @property
    def DetachObject(self):
        return object

    @property
    def GetAttachedObjects(self):
        return object

    @property
    def GenPrograms(self):
        return object

    @property
    def DeletePrograms(self):
        return object

    @property
    def BindProgram(self):
        return object

    @property
    def ProgramString(self):
        return object

    @property
    def ProgramLocalParameter4fv(self):
        return object

    @property
    def UniformMatrix2x3fv(self):
        return object

    @property
    def UniformMatrix3x2fv(self):
        return object

    @property
    def UniformMatrix2x4fv(self):
        return object

    @property
    def UniformMatrix4x2fv(self):
        return object

    @property
    def UniformMatrix3x4fv(self):
        return object

    @property
    def UniformMatrix4x3fv(self):
        return object

    @property
    def BindFragDataLocation(self):
        return object

    @property
    def DebugMessageControl(self):
        return object

    @property
    def DebugMessageInsert(self):
        return object

    @property
    def DebugMessageCallback(self):
        return object

    @property
    def GetDebugMessageLog(self):
        return object

    @property
    def GetPointerv(self):
        return object

    @property
    def PushDebugGroup(self):
        return object

    @property
    def PopDebugGroup(self):
        return object

    @property
    def ObjectLabel(self):
        return object

    @property
    def GetObjectLabel(self):
        return object

    @property
    def ObjectPtrLabel(self):
        return object

    @property
    def GetObjectPtrLabel(self):
        return object

    @property
    def InsertEventMarker(self):
        return object

    @property
    def PushGroupMarker(self):
        return object

    @property
    def PopGroupMarker(self):
        return object

    @property
    def StringMarker(self):
        return object

    @property
    def GenVertexArrays(self):
        return object

    @property
    def DeleteVertexArrays(self):
        return object

    @property
    def BindVertexArray(self):
        return object

    @property
    def IsVertexArray(self):
        return object

    @property
    def FenceSync(self):
        return object

    @property
    def IsSync(self):
        return object

    @property
    def DeleteSync(self):
        return object

    @property
    def ClientWaitSync(self):
        return object

    @property
    def WaitSync(self):
        return object

    @property
    def GetSynciv(self):
        return object

    @property
    def CopyBufferSubData(self):
        return object

    @property
    def GetBufferSubData(self):
        return object

    @property
    def GenQueries(self):
        return object

    @property
    def DeleteQueries(self):
        return object

    @property
    def IsQuery(self):
        return object

    @property
    def BeginQuery(self):
        return object

    @property
    def EndQuery(self):
        return object

    @property
    def QueryCounter(self):
        return object

    @property
    def GetQueryiv(self):
        return object

    @property
    def GetQueryObjectiv(self):
        return object

    @property
    def GetQueryObjectuiv(self):
        return object

    @property
    def GetQueryObjecti64v(self):
        return object

    @property
    def GetQueryObjectui64v(self):
        return object

    @property
    def padding(self):
        return object


class GLMemory():
    """"""
    
    def copy_into(self, tex_id=None, target=None, tex_format=None, width=None, height=None):
        """"""
        return object
    
    def copy_teximage(self, tex_id=None, out_target=None, out_tex_format=None, out_width=None, out_height=None):
        """"""
        return object
    
    def get_texture_format(self):
        """"""
        return object
    
    def get_texture_height(self):
        """"""
        return object
    
    def get_texture_id(self):
        """"""
        return object
    
    def get_texture_target(self):
        """"""
        return object
    
    def get_texture_width(self):
        """"""
        return object
    
    def init(self, allocator=None, parent=None, context=None, target=None, tex_format=None, params=None, info=None, plane=None, valign=None, user_data=None, notify=None):
        """"""
        return object
    
    def read_pixels(self, read_pointer=None):
        """"""
        return object
    
    def texsubimage(self, read_pointer=None):
        """"""
        return object
    @staticmethod
    def init_once():
        """"""
        return object
    @staticmethod
    def setup_buffer(allocator=None, buffer=None, params=None, tex_formats=None, wrapped_data=None, n_wrapped_pointers=None):
        """"""
        return object

    @property
    def mem(self):
        return object

    @property
    def tex_id(self):
        return object

    @property
    def tex_target(self):
        return object

    @property
    def tex_format(self):
        return object

    @property
    def info(self):
        return object

    @property
    def valign(self):
        return object

    @property
    def plane(self):
        return object

    @property
    def tex_scaling(self):
        return object

    @property
    def texture_wrapped(self):
        return object

    @property
    def unpack_length(self):
        return object

    @property
    def tex_width(self):
        return object

    @property
    def _padding(self):
        return object


class GLMemoryAllocator(GLBaseMemoryAllocator):
    """"""
    @staticmethod
    def get_default(context=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def _padding(self):
        return object


class GLMemoryAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def map(self):
        return object

    @property
    def copy(self):
        return object

    @property
    def unmap(self):
        return object

    @property
    def _padding(self):
        return object


class GLMemoryEGL():
    """"""


class GLMemoryEGLAllocator():
    """"""


class GLMemoryEGLAllocatorClass():
    """"""


class GLMemoryPBO():
    """"""
    
    def copy_into_texture(self, tex_id=None, target=None, tex_format=None, width=None, height=None, stride=None, respecify=None):
        """"""
        return object
    
    def download_transfer(self):
        """"""
        return object
    
    def upload_transfer(self):
        """"""
        return object
    @staticmethod
    def init_once():
        """"""
        return object

    @property
    def mem(self):
        return object

    @property
    def pbo(self):
        return object

    @property
    def _padding(self):
        return object


class GLMemoryPBOAllocator(GLMemoryAllocator):
    """"""

    @property
    def parent(self):
        return object

    @property
    def _padding(self):
        return object


class GLMemoryPBOAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLOverlayCompositor(Gst.Object):
    """"""
    
    def __init__(self, context=None):
        """"""
        return object
    @staticmethod
    def new(context=None):
        """"""
        return object
    @staticmethod
    def add_caps(caps=None):
        """"""
        return object
    
    def draw_overlays(self):
        """"""
        return object
    
    def free_overlays(self):
        """"""
        return object
    
    def upload_overlays(self, buf=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def context(self):
        return object

    @property
    def last_window_width(self):
        return object

    @property
    def last_window_height(self):
        return object

    @property
    def overlays(self):
        return object

    @property
    def shader(self):
        return object

    @property
    def position_attrib(self):
        return object

    @property
    def texcoord_attrib(self):
        return object

    @property
    def _padding(self):
        return object


class GLOverlayCompositorClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLQuery():
    """"""
    
    def counter(self):
        """"""
        return object
    
    def end(self):
        """"""
        return object
    
    def free(self):
        """"""
        return object
    
    def init(self, context=None, query_type=None):
        """"""
        return object
    
    def result(self):
        """"""
        return object
    
    def start(self):
        """"""
        return object
    
    def unset(self):
        """"""
        return object
    @staticmethod
    def local_gl_context(element=None, direction=None, context_ptr=None):
        """"""
        return object
    @staticmethod
    def new(context=None, query_type=None):
        """"""
        return object

    @property
    def context(self):
        return object

    @property
    def query_type(self):
        return object

    @property
    def query_id(self):
        return object

    @property
    def supported(self):
        return object

    @property
    def start_called(self):
        return object

    @property
    def debug(self):
        return object

    @property
    def _padding(self):
        return object


class GLRenderbuffer():
    """"""
    
    def get_format(self):
        """"""
        return object
    
    def get_height(self):
        """"""
        return object
    
    def get_id(self):
        """"""
        return object
    
    def get_width(self):
        """"""
        return object
    @staticmethod
    def init_once():
        """"""
        return object

    @property
    def mem(self):
        return object

    @property
    def renderbuffer_id(self):
        return object

    @property
    def renderbuffer_format(self):
        return object

    @property
    def width(self):
        return object

    @property
    def height(self):
        return object

    @property
    def renderbuffer_wrapped(self):
        return object

    @property
    def _padding(self):
        return object


class GLRenderbufferAllocationParams():
    """"""
    
    def __init__(self, context=None, alloc_params=None, renderbuffer_format=None, width=None, height=None):
        """"""
        return object
    @staticmethod
    def new(context=None, alloc_params=None, renderbuffer_format=None, width=None, height=None):
        """"""
        return object
    @staticmethod
    def new_wrapped(context=None, alloc_params=None, renderbuffer_format=None, width=None, height=None, gl_handle=None, user_data=None, notify=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def renderbuffer_format(self):
        return object

    @property
    def width(self):
        return object

    @property
    def height(self):
        return object

    @property
    def _padding(self):
        return object


class GLRenderbufferAllocator(GLBaseMemoryAllocator):
    """"""

    @property
    def parent(self):
        return object

    @property
    def _padding(self):
        return object


class GLRenderbufferAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLSLStage(Gst.Object):
    """"""
    
    def __init__(self, context=None, type=None):
        """"""
        return object
    @staticmethod
    def new(context=None, type=None):
        """"""
        return object
    @staticmethod
    def new_default_fragment(context=None):
        """"""
        return object
    @staticmethod
    def new_default_vertex(context=None):
        """"""
        return object
    @staticmethod
    def new_with_string(context=None, type=None, version=None, profile=None, str=None):
        """"""
        return object
    @staticmethod
    def new_with_strings(context=None, type=None, version=None, profile=None, n_strings=None, str=None):
        """"""
        return object
    
    def compile(self):
        """"""
        return object
    
    def get_handle(self):
        """"""
        return object
    
    def get_profile(self):
        """"""
        return object
    
    def get_shader_type(self):
        """"""
        return object
    
    def get_version(self):
        """"""
        return object
    
    def set_strings(self, version=None, profile=None, n_strings=None, str=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def context(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _padding(self):
        return object


class GLSLStageClass():
    """"""

    @property
    def parent(self):
        return object

    @property
    def _padding(self):
        return object


class GLSLStagePrivate():
    """"""


class GLShader(Gst.Object):
    """"""
    
    def __init__(self, context=None):
        """"""
        return object
    @staticmethod
    def new(context=None):
        """"""
        return object
    @staticmethod
    def new_default(context=None):
        """"""
        return object
    @staticmethod
    def new_link_with_stages(context=None, error=None, *args):
        """"""
        return object
    @staticmethod
    def new_with_stages(context=None, error=None, *args):
        """"""
        return object
    
    def attach(self, stage=None):
        """"""
        return object
    
    def attach_unlocked(self, stage=None):
        """"""
        return object
    
    def bind_attribute_location(self, index=None, name=None):
        """"""
        return object
    
    def bind_frag_data_location(self, index=None, name=None):
        """"""
        return object
    
    def compile_attach_stage(self, stage=None):
        """"""
        return object
    
    def detach(self, stage=None):
        """"""
        return object
    
    def detach_unlocked(self, stage=None):
        """"""
        return object
    
    def get_attribute_location(self, name=None):
        """"""
        return object
    
    def get_program_handle(self):
        """"""
        return object
    
    def is_linked(self):
        """"""
        return object
    
    def link(self):
        """"""
        return object
    
    def release(self):
        """"""
        return object
    
    def release_unlocked(self):
        """"""
        return object
    
    def set_uniform_1f(self, name=None, value=None):
        """"""
        return object
    
    def set_uniform_1fv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_1i(self, name=None, value=None):
        """"""
        return object
    
    def set_uniform_1iv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_2f(self, name=None, v0=None, v1=None):
        """"""
        return object
    
    def set_uniform_2fv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_2i(self, name=None, v0=None, v1=None):
        """"""
        return object
    
    def set_uniform_2iv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_3f(self, name=None, v0=None, v1=None, v2=None):
        """"""
        return object
    
    def set_uniform_3fv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_3i(self, name=None, v0=None, v1=None, v2=None):
        """"""
        return object
    
    def set_uniform_3iv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_4f(self, name=None, v0=None, v1=None, v2=None, v3=None):
        """"""
        return object
    
    def set_uniform_4fv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_4i(self, name=None, v0=None, v1=None, v2=None, v3=None):
        """"""
        return object
    
    def set_uniform_4iv(self, name=None, count=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_2fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_2x3fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_2x4fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_3fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_3x2fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_3x4fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_4fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_4x2fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def set_uniform_matrix_4x3fv(self, name=None, count=None, transpose=None, value=None):
        """"""
        return object
    
    def use(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def context(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _padding(self):
        return object


class GLShaderClass():
    """"""

    @property
    def parent_class(self):
        return object


class GLShaderPrivate():
    """"""


class GLSyncMeta():
    """"""
    
    def set_sync_point(self, context=None):
        """"""
        return object
    
    def wait(self, context=None):
        """"""
        return object
    
    def wait_cpu(self, context=None):
        """"""
        return object
    @staticmethod
    def get_info():
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def context(self):
        return object

    @property
    def data(self):
        return object

    @property
    def set_sync(self):
        return object

    @property
    def set_sync_gl(self):
        return object

    @property
    def wait(self):
        return object

    @property
    def wait_gl(self):
        return object

    @property
    def wait_cpu(self):
        return object

    @property
    def wait_cpu_gl(self):
        return object

    @property
    def copy(self):
        return object

    @property
    def free(self):
        return object

    @property
    def free_gl(self):
        return object


class GLUpload(Gst.Object):
    """"""
    
    def __init__(self, context=None):
        """"""
        return object
    @staticmethod
    def new(context=None):
        """"""
        return object
    @staticmethod
    def get_input_template_caps():
        """"""
        return object
    
    def get_caps(self, in_caps=None, out_caps=None):
        """"""
        return object
    
    def perform_with_buffer(self, buffer=None, outbuf_ptr=None):
        """"""
        return object
    
    def propose_allocation(self, decide_query=None, query=None):
        """"""
        return object
    
    def set_caps(self, in_caps=None, out_caps=None):
        """"""
        return object
    
    def set_context(self, context=None):
        """"""
        return object
    
    def transform_caps(self, context=None, direction=None, caps=None, filter=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def context(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _reserved(self):
        return object


class GLUploadClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLUploadPrivate():
    """"""


class GLVideoAllocationParams():
    """"""
    
    def __init__(self, context=None, alloc_params=None, v_info=None, plane=None, valign=None, target=None, tex_format=None):
        """"""
        return object
    @staticmethod
    def new(context=None, alloc_params=None, v_info=None, plane=None, valign=None, target=None, tex_format=None):
        """"""
        return object
    @staticmethod
    def new_wrapped_data(context=None, alloc_params=None, v_info=None, plane=None, valign=None, target=None, tex_format=None, wrapped_data=None, user_data=None, notify=None):
        """"""
        return object
    @staticmethod
    def new_wrapped_gl_handle(context=None, alloc_params=None, v_info=None, plane=None, valign=None, target=None, tex_format=None, gl_handle=None, user_data=None, notify=None):
        """"""
        return object
    @staticmethod
    def new_wrapped_texture(context=None, alloc_params=None, v_info=None, plane=None, valign=None, target=None, tex_format=None, tex_id=None, user_data=None, notify=None):
        """"""
        return object
    
    def copy_data(self, dest_vid=None):
        """"""
        return object
    
    def free_data(self):
        """"""
        return object
    
    def init_full(self, struct_size=None, alloc_flags=None, copy=None, free=None, context=None, alloc_params=None, v_info=None, plane=None, valign=None, target=None, tex_format=None, wrapped_data=None, gl_handle=None, user_data=None, notify=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def v_info(self):
        return object

    @property
    def plane(self):
        return object

    @property
    def valign(self):
        return object

    @property
    def target(self):
        return object

    @property
    def tex_format(self):
        return object

    @property
    def _padding(self):
        return object


class GLViewConvert(Gst.Object):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    
    def fixate_caps(self, direction=None, caps=None, othercaps=None):
        """"""
        return object
    
    def get_output(self, outbuf_ptr=None):
        """"""
        return object
    
    def perform(self, inbuf=None):
        """"""
        return object
    
    def reset(self):
        """"""
        return object
    
    def set_caps(self, in_caps=None, out_caps=None):
        """"""
        return object
    
    def set_context(self, context=None):
        """"""
        return object
    
    def submit_input_buffer(self, is_discont=None, input=None):
        """"""
        return object
    
    def transform_caps(self, direction=None, caps=None, filter=None):
        """"""
        return object

    @property
    def object(self):
        return object

    @property
    def context(self):
        return object

    @property
    def shader(self):
        return object

    @property
    def input_mode_override(self):
        return object

    @property
    def input_flags_override(self):
        return object

    @property
    def output_mode_override(self):
        return object

    @property
    def output_flags_override(self):
        return object

    @property
    def downmix_mode(self):
        return object

    @property
    def in_info(self):
        return object

    @property
    def out_info(self):
        return object

    @property
    def from_texture_target(self):
        return object

    @property
    def to_texture_target(self):
        return object

    @property
    def caps_passthrough(self):
        return object

    @property
    def initted(self):
        return object

    @property
    def reconfigure(self):
        return object

    @property
    def fbo(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _padding(self):
        return object


class GLViewConvertClass():
    """"""

    @property
    def object_class(self):
        return object

    @property
    def _padding(self):
        return object


class GLViewConvertPrivate():
    """"""


class GLWindow(Gst.Object):
    """"""
    
    def __init__(self, display=None):
        """"""
        return object
    @staticmethod
    def new(display=None):
        """"""
        return object
    @staticmethod
    def error_quark():
        """"""
        return object
    
    def close(self):
        """"""
        return object
    
    def draw(self):
        """"""
        return object
    
    def get_display(self):
        """"""
        return object
    
    def get_window_handle(self):
        """"""
        return object
    
    def handle_events(self, handle_events=None):
        """"""
        return object
    
    def open(self):
        """"""
        return object
    
    def queue_resize(self):
        """"""
        return object
    
    def quit(self):
        """"""
        return object
    
    def run(self):
        """"""
        return object
    
    def send_message(self, callback=None, data=None):
        """"""
        return object
    
    def send_message_async(self, callback=None, data=None, destroy=None):
        """"""
        return object
    
    def set_preferred_size(self, width=None, height=None):
        """"""
        return object
    
    def set_render_rectangle(self, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def set_window_handle(self, handle=None):
        """"""
        return object
    
    def show(self):
        """"""
        return object
    
    def draw(self):
        """"""
        return object
    
    def get_context(self):
        """"""
        return object
    
    def get_display(self):
        """"""
        return object
    
    def get_surface_dimensions(self, width=None, height=None):
        """"""
        return object
    
    def get_window_handle(self):
        """"""
        return object
    
    def handle_events(self, handle_events=None):
        """"""
        return object
    
    def queue_resize(self):
        """"""
        return object
    
    def quit(self):
        """"""
        return object
    
    def resize(self, width=None, height=None):
        """"""
        return object
    
    def run(self):
        """"""
        return object
    
    def send_key_event(self, event_type=None, key_str=None):
        """"""
        return object
    
    def send_message(self, callback=None, data=None):
        """"""
        return object
    
    def send_message_async(self, callback=None, data=None, destroy=None):
        """"""
        return object
    
    def send_mouse_event(self, event_type=None, button=None, posx=None, posy=None):
        """"""
        return object
    
    def set_close_callback(self, callback=None, data=None, destroy_notify=None):
        """"""
        return object
    
    def set_draw_callback(self, callback=None, data=None, destroy_notify=None):
        """"""
        return object
    
    def set_preferred_size(self, width=None, height=None):
        """"""
        return object
    
    def set_render_rectangle(self, x=None, y=None, width=None, height=None):
        """"""
        return object
    
    def set_resize_callback(self, callback=None, data=None, destroy_notify=None):
        """"""
        return object
    
    def set_window_handle(self, handle=None):
        """"""
        return object
    
    def show(self):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def lock(self):
        return object

    @property
    def display(self):
        return object

    @property
    def context_ref(self):
        return object

    @property
    def is_drawing(self):
        return object

    @property
    def draw(self):
        return object

    @property
    def draw_data(self):
        return object

    @property
    def draw_notify(self):
        return object

    @property
    def close(self):
        return object

    @property
    def close_data(self):
        return object

    @property
    def close_notify(self):
        return object

    @property
    def resize(self):
        return object

    @property
    def resize_data(self):
        return object

    @property
    def resize_notify(self):
        return object

    @property
    def queue_resize(self):
        return object

    @property
    def main_context(self):
        return object

    @property
    def priv(self):
        return object

    @property
    def _reserved(self):
        return object


class GLWindowClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def get_display(self):
        return object

    @property
    def set_window_handle(self):
        return object

    @property
    def get_window_handle(self):
        return object

    @property
    def draw(self):
        return object

    @property
    def run(self):
        return object

    @property
    def quit(self):
        return object

    @property
    def send_message(self):
        return object

    @property
    def send_message_async(self):
        return object

    @property
    def open(self):
        return object

    @property
    def close(self):
        return object

    @property
    def handle_events(self):
        return object

    @property
    def set_preferred_size(self):
        return object

    @property
    def show(self):
        return object

    @property
    def set_render_rectangle(self):
        return object

    @property
    def queue_resize(self):
        return object

    @property
    def _reserved(self):
        return object


class GLWindowPrivate():
    """"""
