# -*- coding: utf-8 -*-


class ModuleFlags:
    """"""
    LAZY = 1
    LOCAL = 2
    MASK = 3

def module_build_path(directory=None, module_name=None):
    """"""
    return object

def module_error():
    """"""
    return object

def module_supported():
    """"""
    return object


class Module():
    """"""
    
    def close(self):
        """"""
        return object
    
    def make_resident(self):
        """"""
        return object
    
    def name(self):
        """"""
        return object
    
    def symbol(self, symbol_name=None, symbol=None):
        """"""
        return object
    @staticmethod
    def build_path(directory=None, module_name=None):
        """"""
        return object
    @staticmethod
    def error():
        """"""
        return object
    @staticmethod
    def open(file_name=None, flags=None):
        """"""
        return object
    @staticmethod
    def supported():
        """"""
        return object
