#!/usr/bin/env python

class Display:
    """This class is used to maintain information about
    displays that belong to mobile devices."""
    def __init__(physical_width=None, physical_height=None,
                 browser_width=None, browser_height=None, color_p=None, colors=None):
        self.physical_width = physical_width
        self.physical_height = physical_height
        self.browser_width = browser_width
        self.browser_height = browser_height
        
        # Does the phone have a colour display panel?
        self.color_p = color_p
        self.colors = colors
      
    def is_color(self):
        return self.color_p == True
    def colors(self):
        return self.colors
    def colours(self):
        #I'm Canadian, you insensitive clod.
        return self.colors()
    def is_colour(self):
        return self.is_color()
    def width(self):
        return self.browser_width or self.physical_width
    def height(self):
        return self.browser_height or self.physical_height
    