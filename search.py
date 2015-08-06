#! python3
# Scrapes the websites of Berkeley establishments known to occasionally offer pesto,
# searching for the presence of aforementioned pesto (the holiest of all sauces).
# Currently-searched businesses include the UCB dining commons, Cheese Board, 
# and Sliver Pizzeria.

import time, re, sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from tkinter import Tk, Text, END, mainloop

__author__ = "Owen Jow"
__version__ = "1.0.0"

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
    
def run(*args):
    # Create the GUI for the program
    window = Tk()
    window.wm_title("pesto_check") # change the window title to pesto_check
    text = Text(window, height=3, width=40)
    text.pack()
    
    """Searches specified websites for pesto and outputs the results."""
    driver = webdriver.PhantomJS("./phantomjs/bin/phantomjs")
    driver.wait = WebDriverWait(driver, 5)
    
    # Search UCB dining hall menus
    text.insert(END, "ALERT: pesto in the DC today!" if search_for_pesto(driver, 
            "http://goo.gl/VR8HpB") else "No pesto in the DC today :(")
    # Search the Cheese Board weekly menu
    text.insert(END, "\nALERT: pesto at Cheese Board this week!" if search_for_pesto(driver, 
            "http://goo.gl/rKTzgY") else "\nNo pesto at Cheese Board this week :(")
    # Search the Sliver weekly menu
    text.insert(END, "\nALERT: pesto at Sliver this week!" if search_for_pesto(driver, 
            "http://goo.gl/tP422Q") else "\nNo pesto at Sliver this week :(")
    
    mainloop()
    driver.quit()

run(sys.argv) # run the overall program
