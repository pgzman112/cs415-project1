//Preston Zimmerman
//Diana Acrehern
//Project Cs415 3/05/21
-- MUST HAVE PYCHARM, PYTHON 3.9.2 INSTALLED ON LOCAL MACHINE  --
-- PYTHON LIBERIES NEEDED TO RUN THIS PROJECT: MATPLOTLIB, NUMPY --

STEPS TO RUN OUR PROGRAM:

1) Install Pycharm on machine (if not already installed) - google from jetbrains community version

2) Install Python version 3.9.2 (https://www.python.org/downloads/). Executable version (exe --> windows, dmg --> mac) *You must know the installed executable directory* 

3) Download zip file zimmerman_acrehern_cs415Project1.zip

4) unzip *keep note of the location you unziped too*

5) Open Pycharm

6) click File ->  New Project 
	- under location select the file at whatever location you extracted it to. it should have the name zimmerman_acrehern_cs415Project1
	- Under base interpreter select python 3.9.2. MUST BE THIS VERSION!
	- then click create and create from existing resources. 

7) Time to install python dependant libraries:
	- click File -> settings -> Project: zimmerman_acrehern_cs415Project1
	- then click Python Interpreter 
		- Click plus sign in bottom left of that window
		- Search for matplotlib, click on it and install Package
		- Next search for numpy, click on it and install package
	- Once done installing close out of that pop up window and return to base pycharm screen

8) Next we must add a run configuration. Click Add Configuration in the top right of screen
	- click drop down menu labeled templates, Find Python and click! 
		(Must click on python not Python Tests)
	- After selecting Python click on the folder next to Script Path
		- click The project drop down menu
		- Select TaskOne.py -> click ok
		- Make sure Pyhton Interpreter in use is Python 3.9
		- In top right Click Create Configuration (Give it a name of TaskOne) 
	- Click Drop down by edit config again and select edit configuration
		- click plus arrow again to add new config
		- Rename to TaskTwo
		- click folder next to script path and select taskTwo.py
		- Make sure Pyhton Interpreter in use is Python 3.9
	- Repeat steps to create run config for taskThree.py

9) Select taskOne.py under config drop down -> then click green arrow to run! -> procede to give A on project to students. :)