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
    yield (
        style.styles.big1.value,
        {
            "height": 10,
            "width": 50
        }
    )
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