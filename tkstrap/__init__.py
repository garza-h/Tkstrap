### IMPORTS                             ###
from __future__ import annotations
from tkinter import Tk, Widget
from typing import Tuple, Generator, AnyStr, Union
from enum import Enum
from dataclasses import dataclass
from itertools import chain
### IMPORTS                             ###
### DOCUMENTATION                       ###
"""
"""
### DOCUMENTATION                       ###
### ARBITRARY CONSTANTS                 ###
StandardTkOpts = dict
StandardTkOptsNames = str
### ARBITRARY CONSTANTS                 ###
### EXCEPTIONS                          ###
class StyleError(Exception):
    def __init__(self, provided_style: str) -> None:
        super().__init__(f"Style Not Recognized, {provided_style}")
### EXCEPTIONS                          ###
### STYLE CLASSES                       ###
class Styles(Enum):
    """
    Holds all the styles for TkStrap
    """
    btn = {
        "height": 1,
        "width": 25,
        "font": ("Helvetica", 25),
        "borderwidth": 0,
        "relief": "flat"
    }

class _Style(object):
    """
    The _Style class is used for creating styles in TkStrap
    """

    ## Dunder                               ##
    def __init__(self, **opts: StandardTkOpts): self.__ops = opts
    def __repr__(self): return str(self)    # calls the __str__ dunder
    def __str__(self): return f"{self.__ops}"
    def __call__(self, arg: AnyStr): return self.__ops if arg == 'dict' else 0
    ## Dunder                               ##
    def add(self, **opts: StandardTkOpts) -> None: """
    Adds the additional options to the current options
    """; self.__ops |= opts

    def rm(self, *opts: StandardTkOptsNames) -> None:"""
    Removes the provided options in the 'opts' variable from the
    current options
    """; self.__ops = {k:v for k,v in self.__ops.items() if k not in opts}

    def edit(self, **opts: StandardTkOpts) -> None: """
    Edits the provided options for the current options
    """; self.add(**opts)
    
    def blank_slate(self) -> None: """
    Clears all options.

    Cannot be undone
    """; self.__ops.clear()

    def copy(self) -> _Style: """
    Returns a copy of the instance
    """; return _Style(self.__ops)

class _Styler(object):
    __inst = lambda var, cls_ : f"'{type(var)}' is not an instance of {cls_}"
    @classmethod
    def style(cls, widget: Widget, style: _Style) -> None:
        """
        Styles the specified widget with the specified style
        """
        ## Checks                           ##
        assert isinstance(*(w := (widget, Widget))), cls.__inst(*w)
        assert isinstance(*(s := (style, _Style))), cls.__inst(*s)
        ## Checks                           ##
        ## Style Widget                     ##
        widget.config(**style('dict'))
        ## Style Widget                     ##
### STYLE CLASSES                       ###
### FUNCS                               ###
def get(style_name: AnyStr) -> _Style:
    ## Hints                                ##
    style: Styles
    ## Hints                                ##
    for style in Styles:
        if style.name == style_name: return _Style(**style.value)
    raise StyleError(style_name)
def style(widget: Widget, style: _Style) -> None:
    _Styler.style(widget, style)
### FUNCS                               ###
### CLEANUP                             ###
del StandardTkOpts
del StandardTkOptsNames
### CLEANUP                             ###