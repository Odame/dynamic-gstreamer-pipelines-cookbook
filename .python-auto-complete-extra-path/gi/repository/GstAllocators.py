# -*- coding: utf-8 -*-
from gi.repository import Gst
ALLOCATOR_DMABUF = r"""dmabuf"""
ALLOCATOR_FD = r"""fd"""
CAPS_FEATURE_MEMORY_DMABUF = r"""memory:DMABuf"""


class FdMemoryFlags:
    """"""
    NONE = 0
    KEEP_MAPPED = 1
    MAP_PRIVATE = 2
    DONT_CLOSE = 4

def dmabuf_memory_get_fd(mem=None):
    """"""
    return object

def fd_memory_get_fd(mem=None):
    """"""
    return object

def is_dmabuf_memory(mem=None):
    """"""
    return object

def is_fd_memory(mem=None):
    """"""
    return object

def is_phys_memory(mem=None):
    """"""
    return object

def phys_memory_get_phys_addr(mem=None):
    """"""
    return object


class DmaBufAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object

    @property
    def _gst_reserved(self):
        return object


class FdAllocator(Gst.Allocator):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def alloc(allocator=None, fd=None, size=None, flags=None):
        """"""
        return object

    @property
    def parent(self):
        return object


class FdAllocatorClass():
    """"""

    @property
    def parent_class(self):
        return object


class PhysMemoryAllocator():
    """"""
    
    def get_phys_addr(self, mem=None):
        """"""
        return object


class PhysMemoryAllocatorInterface():
    """"""

    @property
    def parent_iface(self):
        return object

    @property
    def get_phys_addr(self):
        return object


class DmaBufAllocator(FdAllocator):
    """"""
    
    def __init__(self):
        """"""
        return object
    @staticmethod
    def new():
        """"""
        return object
    @staticmethod
    def alloc(allocator=None, fd=None, size=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def _gst_reserved(self):
        return object
