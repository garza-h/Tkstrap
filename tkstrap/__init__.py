### IMPORTS                             ###
from __future__ import annotations
import tkstrap.__imports__ as _
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
    def __init__(self, provided_style: _.AnyStr) -> None:
        super().__init__(f"Style Not Recognized, {provided_style}")
### EXCEPTIONS                          ###
### UTILITY                             ###
def _bind(w: _.Widget, bind: str,  action: _.Callable): w.bind(bind, action)
def bind_enter(w: _.Widget, action: _.Callable): _bind(w, '<Enter>', action)
def bind_leave(w: _.Widget, action: _.Callable): _bind(w, '<Leave>', action)
change_bg = lambda w, bg: w.config(background=bg)

def hover(w: _.Widget, enter: _.AnyStr, leave: _.AnyStr) -> None:
    bind_enter(w, lambda *_: change_bg(w, enter))
    bind_leave(w, lambda *_: change_bg(w, leave))
### UTILITY                             ###
### STYLE CLASSES                       ###
class Styles(_.Enum):
    """
    Holds all the styles for TkStrap
    """
    btn = ({"hover": ("azure", "origin")}, {
        "height": 1, "width": 20,   # dimensions
        "foreground": "#212529",
        "relief": "flat",
        "font": ("Helvetica Neue", 16),
        "borderwidth": 0,
        "activebackground": "azure"
    })

    btn_primary = ({"hover": ("#0069d9", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#fff"),
        "background": "#007bff", "activebackground": "#0069d9",
    })

    btn_secondary = ({"hover": ("#5a6268", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#fff"),
        "background": "#6c757d", "activebackground": "#5a6268"
    })

    btn_success = ({"hover": ("#218838", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#fff"),
        "background": "#28a745", "activebackground": "#218838"
    })

    btn_info = ({"hover": ("#138496", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#fff"),
        "background": "#17a2b8", "activebackground": "#138496"
    })

    btn_warning = ({"hover": ("#e0a800", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#212529"),
        "background": "#ffc107", "activebackground": "#e0a800"
    })
    
    btn_danger = ({"hover": ("#c82333", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#fff"),
        "background": "#dc3545", "activebackground": "#c82333"
    })

    btn_dark = ({"hover": ("#23272b", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#fff"),
        "background": "#343a40", "activebackground": "#23272b"
    })

    btn_light = ({"hover": ("#e2e6ea", "origin")}, btn[1]|{
        **dict.fromkeys(("foreground", "activeforeground"), "#212529"),
        "background": "#f8f9fa", "activebackground": "#e2e6ea"
    })

class _Style(object):
    """
    The _Style class is used for creating styles in TkStrap
    """

    ## Dunder                               ##
    def __init__(self, s_name: str, binds: dict, **opts: StandardTkOpts):
        self.s_name = s_name
        self.binds = binds
        self.__ops = opts
    def __repr__(self): return str(self)    # calls the __str__ dunder
    def __str__(self): return f"{self.__ops}"
    def __call__(self, arg: _.AnyStr): return self.__ops if arg == 'dict' else 0
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
    def style(cls, widget: _.Widget, style: _Style) -> None:
        """
        Styles the specified widget with the specified style
        """
        ## Checks                           ##
        assert isinstance(*(w := (widget, _.Widget))), cls.__inst(*w)
        assert isinstance(*(s := (style, _Style))), cls.__inst(*s)
        ## Checks                           ##
        ## Style Widget                     ##
        widget.config(**style('dict'))
        ## Style Widget                     ##
### STYLE CLASSES                       ###
### FUNCS                               ###
def get(style_name: _.AnyStr) -> _Style:
    ## Hints                                ##
    style: Styles
    ## Hints                                ##
    style_name = _.sub("\-", "_", style_name)
    for style in Styles:
        if style.name == style_name: return _Style(
            style_name,
            style.value[0],
            **style.value[1]    # the opts
        )
    raise StyleError(style_name)

def style(w: _.Widget, style: _Style) -> None:
    _Styler.style(w, style)
    origin = w.cget("background")
    hov = (b := style.binds).get("hover")
    if hov: hover(w, hov[0], origin if hov[1] == 'origin' else hov[1])
### FUNCS                               ###
### CLEANUP                             ###
del StandardTkOpts
del StandardTkOptsNames
### CLEANUP                             ###