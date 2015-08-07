# pesto_check [v1.0.0]
We all know that [pesto](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/BasilPesto.JPG/1920px-BasilPesto.JPG) is the greatest and most heavenly of all sauces... but where to get it? This program offers a solution [for residents of the UC Berkeley area], by scraping the websites of nearby restaurants known to occasionally offer dishes with pesto. Currently-searched businesses include the UCB dining commons, Cheese Board, and Sliver Pizzeria.

To run, simply download all of the files and execute either `./run_pesto_check` or `python3 search.py` through the command line. A GUI will be launched in the upper-right hand corner of the screen: ![alt text](https://github.com/ohjay/pesto_check/blob/master/gui_example.png "A screenshot of the pesto check UI")

(Note that the only platform that pesto_check currently supports is OS X, because that is the only platform to which the lead (and only) developer has current access.)

Also, the Python bindings for Selenium must be installed on your computer. If they are not, then you can obtain them easily with the command `pip install selenium`, or by visiting the Selenium [download page](http://www.seleniumhq.org/download/).

We hope you enjoy the pesto (assuming it's even possible _not_ to, that is)!

## Running pesto_check as an application [OS X 10.4-]
For those who want to avoid all that Terminal lingo, or simply speed up the Pesto Check workflow: It is possible (and easy) to run pesto_check as an application, provided you're running a version of OS X later than 10.3. This will require the use of the [Automator](https://support.apple.com/en-ph/HT2488) software, which should be pre-installed on your system.

### Creating the Pesto Check app
1. As always, download all of the files in this repository. This can be done with the command `git clone https://github.com/ohjay/pesto_check.git`.
2. In the folder that you just downloaded, navigate to the `app` directory and open two files: `app/pesto_check.sh` and `app/search.py`.
3. Within these files, there are three filepaths that need to be changed. They are as follows:
  + **Line 9 in `pesto_check.sh`**: Fill in the absolute path to `app/search.py`
  + **Line 15 in `pesto_check.sh`**: Fill in the absolute path to the `python3` command
  + **Line 92 in `search.py`**: Fill in the absolute path to `bin/phantomjs` (this should be contained
    in the `phantomjs` folder that you just downloaded)
4. Open Automator (if you don't know where it is, Spotlight it), and select **Application** as the workflow template.
5. In the Utilities section of the Actions/Library sidebar, select **Run Shell Script**.
6. In the window on the right, select **/bin/bash** as the shell. Then copy/paste the contents of the `app/pesto_check.sh` script into the input box.
7. Save the app (for example to the Applications folder) as `Pesto Check`. [Technically, of course, the name can be anything you like!]

### [Optional] Adding an icon to your app
1. Open Finder and enter the `pesto_check/app` folder again. Copy (⌘C) the `basil_pesto.icns` file to the clipboard.
2. Now navigate to the directory in which you just saved Pesto Check.
3. Right-click `Pesto Check.app` and choose **Get Info**.
4. Select the icon in the top-left hand corner. It should take on a faint blue outline.
5. Paste from the Clipboard (⌘V) your icns file. The default icon should be replaced by a bowl of pesto.

That's it! Now you can run Pesto Check as a regular OS X application. Like any other app, this can be [added to the dock](https://github.com/ohjay/pesto_check/blob/master/in_dock.png) or run from the Launchpad. Have fun!
