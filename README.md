# WaterFall
WaterFall is a implementation of Python PyQt5 and PyQtWebEngine. This is honestly me just trying to make a operational web browser in python.

# NOTE:
Current Browser functionality
--> BackButton (going backwards to previous websites)
--> ForwardButton (going forward to previous websites)
--> ReloadButton (reload the current webpage)
--> HomeButton (Load the homepage)
--> AddressBar (Load url that is in the address bar)
--------> Select All when clicked into the address bar
--------> Pressing Enter will submit the url to be loaded
--------> Shows History (drop down combobox) (NEW / UPDATED)
--> GoButton (Submit the text from addressBar to be loaded by browser)

-------------------------------------------------------------------------------------------------------------------------

Next Release:
[++] Researching Security aspects of PyQt5
Note: Is PyQT5 Secure with the base engine or do I need to add security? 

[++] Add AutoComplete to QLineEdit
Note: I want to add AutoComplete (not completed)

[++] Add setting button
Note: I want to add settings and have some general setting options defined

[++] Going to start working on a better user interface design
Note: I would like a more up-to-date user interface design with a higher quality in button options.

Researching: 
[???] Does PyQt5 have built in security?
[???] Find a graphics designer who can make better quality user interface items than me.
[???] How to save to cache like a browser specifically would? 

Answered Research: (NEW / UPDATED)
1.) Saving Cache Data for AutoComplete. 
(QCompleter)
2.)  Best way to add History drop down to QLineEdit. 
(QCombobox.setLineEdit(QLineEdit)
