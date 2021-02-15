# -*- coding: utf-8 -*-
from gi.repository import Gst


class InsertBin(Gst.Bin, Gst.ChildProxy):
    """"""
    
    def __init__(self, name=None):
        """"""
        return object
    @staticmethod
    def new(name=None):
        """"""
        return object
    
    def append(self, element=None, callback=None, user_data=None):
        """"""
        return object
    
    def insert_after(self, element=None, sibling=None, callback=None, user_data=None):
        """"""
        return object
    
    def insert_before(self, element=None, sibling=None, callback=None, user_data=None):
        """"""
        return object
    
    def prepend(self, element=None, callback=None, user_data=None):
        """"""
        return object
    
    def remove(self, element=None, callback=None, user_data=None):
        """"""
        return object

    @property
    def parent(self):
        return object

    @property
    def priv(self):
        return object


class InsertBinClass():
    """"""

    @property
    def parent_class(self):
        return object


class InsertBinPrivate():
    """"""
