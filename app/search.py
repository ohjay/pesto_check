#! python3
# Scrapes the websites of Berkeley establishments known to occasionally offer pesto,
# searching for the presence of aforementioned pesto (the holiest of all sauces).
# Currently-searched businesses include the UCB dining commons, Cheese Board, 
# and Sliver Pizzeria.

import re, sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import Tk, Text, END, mainloop

__author__ = "Owen Jow"
__version__ = "1.0.0"

#####################################
# Utility (search helper) functions # 
#####################################

def search_and_output_incl_date(driver, text, url, tag_type, name):
    """Checks NAME's website (specified by the given url) for pesto, and also gets the date
    that the pesto will be available. The date in question should be contained within 
    the first TAG_TYPE html tags found before the occurrence of "pesto". When it has 
    this information, the function will update the text widget with its findings.
    
    Arguments:
    driver -- A Selenium webdriver
    text -- The widget to be updated
    url -- The url to be searched (as a string)
    tag_type -- The type of HTML tag in which the date will be contained (ex. "h4" or "h5")
    name -- the name of the establishment that is being checked
    
    Returns nothing, but updates the widget as desired.
    """
    # Get the site's page source
    driver.get(url)
    pg_src = driver.page_source
    
    match_obj = re.search(r"\b[Pp]esto\b", pg_src)
    pesto_index = match_obj.start() if match_obj else -1
    start_h5 = pg_src.rfind("<" + tag_type + ">", 0, pesto_index) # the date is b/e <TAG_TYPE> tags
    end_h5 = pg_src.rfind("</" + tag_type + ">", 0, pesto_index)
    
    date_start = start_h5 + len(tag_type) + 2 # +len(tag_type)+2 removes the opening tag
    if pesto_index != -1:
        text.insert(END, name + " STATUS: Pesto available on " \
                + pg_src[date_start:end_h5] + "!\n", ("green",))
    else:
        text.insert(END, name + " STATUS: No pesto :(\n", ("red",))
    
def search_for_pesto(driver, url):
    """Checks the specified website for the existence of pesto. The website
    is assumed to be some kind of eatery that sometimes serves food with pesto.
    
    Arguments:
    driver -- A Selenium webdriver
    url -- The url of the website to be searched
    
    Returns true if the website contains pesto, and false otherwise.
    
    >>> driver = webdriver.PhantomJS("./phantomjs/bin/phantomjs")
    >>> search_for_pesto(driver, "google.com")
    False
    >>> search_for_pesto(driver, "http://allrecipes.com/recipe/pesto/")
    True
    """
    driver.get(url)
    pg_src = driver.page_source
    return re.search(r'[Pp]esto', pg_src) is not None
    
def search_and_output(driver, url, text, name, for_week=True):
    """Calls the search function and updates the text widget with the information.
    
    Arguments:
    driver -- A Selenium webdriver
    url -- The url of the website to be searched
    text -- The text widget to be updated with the newly acquired information
    name -- The name of the establishment being searched (preferably in all caps)
    for_week -- A boolean specifying whether or not the results pertain to the whole week
    """
    if search_for_pesto(driver, url):
        text.insert(END, name + " STATUS: Pesto available " \
                + ("this week!\n" if for_week else "today!\n"), ("green",))
    else:
        text.insert(END, name + " STATUS: No pesto :(\n", ("red",))
        
###########################################
# Specialized restaurant search functions # 
###########################################

def search_sliver_and_output(driver, text):
    """Searches the Sliver website for pesto pizza and outputs to the text widget
    either the date that the pizza will be available or a 'not found' message."""
    search_and_output_incl_date(driver, text, "http://goo.gl/tP422Q", "h3", "SLIVER")
    
def search_cheeseboard_and_output(driver, text):
    """Searches the Cheese Board website for pesto pizza and outputs both the date 
    and a confirmation if found. Otherwise it will output a std 'not found' message."""
    search_and_output_incl_date(driver, text, "http://goo.gl/rKTzgY", "h4", "CHEESE BOARD")

###################
# Main subroutine # 
###################

def run(*args):
    # Create the GUI for the program
    window = Tk()
    window.wm_title("pesto_check") # change the window title to pesto_check
    text = Text(window, height=3, width=65, bg="black", padx=5, pady=5, 
            highlightthickness=1)
    text.pack()
    
    # Tag configs for green/red font color
    text.tag_config("green", foreground="green")
    text.tag_config("red", foreground="red")
    
    # Set GUI position on screen (we'll put it on the upper-right hand corner)
    window.update_idletasks() # make sure that the width is up to date
    width = window.winfo_screenwidth()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = width - size[0]
    window.geometry("%dx%d+%d+%d" % (size + (x, 0)))
    
    """Searches specified websites for pesto and outputs the results."""
    # The path to the PhantomJS executable (shown below) will need to be changed on your system
    # Example path: /Users/owenjow/pesto_check/phantomjs/bin/phantomjs
    driver = webdriver.PhantomJS("[PATH-TO-phantomjs]") ### CHANGE THIS ###
    driver.wait = WebDriverWait(driver, 5)
    
    # Search UCB dining hall menus
    search_and_output(driver, "http://goo.gl/VR8HpB", text, "DC", False)
    # Search the Cheese Board weekly menu
    search_cheeseboard_and_output(driver, text)
    # Search the Sliver weekly menu
    search_sliver_and_output(driver, text)
    
    # Bring the Tkinter window to the front
    window.lift()
    window.attributes("-topmost", True)
    
    text.configure(state="disabled") # there's no need to allow user input!
    mainloop()
    driver.quit()

run(sys.argv) # run the overall program
