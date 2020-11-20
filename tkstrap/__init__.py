### IMPORTS                             ###
from __future__ import annotations
from tkinter import Tk, Widget, Button
from typing import Tuple, Generator, AnyStr, Union, Callable
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
### UTILITY                             ###
def _bind(w: Widget, bind: str,  action: Callable): w.bind(bind, action)
def bind_enter(w: Widget, action: Callable): _bind(w, '<Enter>', action)
def bind_leave(w: Widget, action: Callable): _bind(w, '<Leave>', action)
change_bg = lambda w, bg: w.config(background=bg)
### UTILITY                             ###
### STYLE CLASSES                       ###
class Styles(Enum):
    """
    Holds all the styles for TkStrap
    """
    btn = {
        "height": 1, "width": 25,   # dimensions
        "foreground": "#212529",
        "relief": "flat",
        "font": ("Helvetica", 16),
        "borderwidth": 0,
        "activebackground": "azure"
    }

class _Style(object):
    """
    The _Style class is used for creating styles in TkStrap
    """

    ## Dunder                               ##
    def __init__(self, s_name: str, **opts: StandardTkOpts):
        self.s_name = s_name
        self.__ops = opts
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
    """; return _Style(self.s_name, **self.__ops)

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
        if style.name == style_name: return _Style(
            style_name,
            **style.value    # the opts
        )
    raise StyleError(style_name)

def style(w: Widget, style: _Style) -> None:
    ## Hints                                ##
    origin: str
    ## Hints                                ##
    _Styler.style(w, style)
    if style.s_name == Styles.btn.name:
        origin = w.cget("background")   # get origin
        
        # bind
        bind_enter(w, lambda *_: change_bg(w, 'azure'))
        bind_leave(w, lambda *_: change_bg(w, origin))
### FUNCS                               ###
### CLEANUP                             ###
del StandardTkOpts
del StandardTkOptsNames
### CLEANUP                             ###