### IMPORTS                             ###
from tkinter.ttk import Style
from tkinter import Tk  # possible issue
from typing import Tuple, Generator
from enum import Enum
### IMPORTS                             ###
### DOCUMENTATION                       ###
### DOCUMENTATION                       ###
### ARBITRARY CONSTANTS                 ###
Options, StyleName = str, dict
### ARBITRARY CONSTANTS                 ###
### EXCEPTIONS                          ###
class StyleError(Exception):
    def __init__(self, provided_style: str) -> None:
        super().__init__(f"Style Not Recognized, {provided_style}")
### EXCEPTIONS                          ###
### STYLES                              ###
class style(object):
    class styles(Enum):
        """
        Enum holding all styles for tks
        """
        ## Button Styles                    ##
        big1 = "big-1.TButton"
        big2 = "big-2.TButton"
        big3 = "big-3.TButton"
        big4 = "big-4.TButton"
        big5 = "big-5.TButton"
        ## Button Styles                    ##
    """
    For loading styles
    """
    ## Get Style Method                     ##
    def __call__(self, style_name: str) -> str:
        ## Hints                            ##
        style: self.styles
        ## Hints                            ##
        """
        For getting a style
        """
        for style in self.styles:
            if style_name == style.name: return style.value
        raise StyleError(style_name)
    ## Get Style Method                     ##
### STYLES                              ###
### FUNCS                               ###
def _button_styles() -> Generator[Tuple[StyleName, Options], None, None]:
    ## Documentation                        ##
    """
    Initializes Button Styles

    Not meant for use outside of module
    """
    ## Documentation                        ##
    ## big                                  ##
    yield (style.styles.big1.value, {
        "height": 50, "width": 25,
        "font": ("Helvetica", 50)
    })
    yield (style.styles.big2.value, {
        "height": 45, "width": 25,
        "font": ("Helvetica", 45)
    })    
    yield (style.styles.big3.value, {
        "height": 40, "width": 25,
        "font": ("Helvetica", 40)
    })    
    yield (style.styles.big4.value, {
        "height": 35, "width": 25,
        "font": ("Helvetica", 35)
    })    
    yield (style.styles.big5.value, {
        "height": 30, "width": 25,
        "font": ("Helvetica", 30)
    })    
    ## big                                  ##

def init(master: Tk) -> style:
    """
    Initializes Tkstrap
    """
    base = Style(master=master)
    config: Tuple[StyleName, Options]
    for config in _button_styles(): base.configure(config[0], **config[1])
    return style()
### FUNCS                               ###
### CLEANUP                             ###
del StyleName
del Options
### CLEANUP                             ###