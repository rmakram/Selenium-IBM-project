First:
- You have to install python program like anaconda or Pycharm to use the tool.
In the program prompt (such as anaconda prompt), You should run the below commands to install the needed modules in python:
pip install selenium
pip install py-getch    (Asking for input in headless mode)
pip install tkinter     (The module responsible for building the App)
pip install pyinstaller 
(In prompt: after finishing editing the script, you should go to the folder that contains the python script (AAT_GUI_BG.py),
then run: #pyinstaller --onefile -w AAT_GUI_BG.py, you will find the .exe file created under DIST Folder)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Second:
Our long script is consisting of 4 parts in this order:
- Doors              (Login - Assign Tasks - Extract users' data from Tasks - Calling DXL Scripts - Close Tasks)
- Synergy            (Login and Transfer Functions)
- Jazz               (Login - Assign Tasks - Extract users' data from Tasks - Calling REPO TOOLS Scripts - Close Tasks)
- GUI Configuration  (In General - Doors - Synergy - Jazz)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Third:
For Doors, we have this index:
1.1 DOORS input data and login functions:
1.1.1  DOORS input data functions
1.1.2 DOORS Login PROGRAM_Function  (Calling input data functions)

1.2 DOORS Assign Tasks function:
1.2.1: DOORS Assign SNOW_Function
1.2.2: DOORS Assign PROGRAM_Function  (Calling Assign SNOW_Function)

1.3 DOORS Extract users' data from tasks function:
1.3.1: DOORS Extract users' data SNOW_Function
1.3.2: DOORS Extract users' data PROGRAM_Function  (Calling Extract users' data SNOW_Function)

1.4 DOORS Tasks Closure function:
1.4.1  DOORS CLOSURE SNOW_Function
1.4.2  DOORS CLOSURE PROGRAM_Function (Calling CLOSURE SNOW_Function)

1.5 DOORS Open file functions 
(Use Append mode with log files that have not headers and Read mode with the files that have headers, if not exist then use Write mode to create it)

1.6: DOORS Call DXL Scripts

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Forth:
For Synergy, we have this index:
2.1 Synergy Open files function

2.2 Synergy input data functions

2.3 Synergy login and Transfer tasks functions:
2.3.1 Synergy Transfer SNOW_Function
2.3.2 Synergy Transfer PROGRAM_Function (Call the Transfer SNOW_Function)
2.3.3 Synergy Login and Call Transfer PROGRAM_Function  (Call the Transfer PROGRAM_Function) 

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Fifth:
For JAZZ, we have this index:
3.1 JAZZ input data and login functions:
3.1.1  JAZZ input data functions
3.1.2 JAZZ Login PROGRAM_Function  (Calling input data functions)

3.2 JAZZ Assign Tasks function:
3.2.1: JAZZ Assign SNOW_Function
3.2.2: JAZZ Assign PROGRAM_Function  (Calling Assign SNOW_Function)

3.3 JAZZ Extract users' data from tasks function:
3.3.1: JAZZ Extract users' data SNOW_Function
3.3.2: JAZZ Extract users' data PROGRAM_Function  (Calling Extract users' data SNOW_Function)

3.4 JAZZ Tasks Closure function:
3.4.1  JAZZ CLOSURE SNOW_Function
3.4.2  JAZZ CLOSURE PROGRAM_Function (Calling CLOSURE SNOW_Function)

3.5 JAZZ Open file functions 
(Use Append mode with log files that have not headers and Read mode with the files that have headers, if not exist then use Write mode to create it)

3.6: JAZZ Call REPO TOOLS Scripts

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Sixth:
GUI Configuration:
4.1 General Configurtaions for App window and Tabs.
4.2 DOORS GUI
4.3 SYNERGY GUI
4.4 JAZZ GUI
4.5 IN GENERAL
Hints:
- Our app window is called: win.
- any pop out window is called new or new2.
- We have 3 configured tabs in our app with our 3 services.
- There were 3 common command in tkinter module we are using, button, label and Entry.
- Button command will have to call functions but without brackets.
- Label is to placed anywhere you need in the tab using grid option.
- Entry has to ask the user for input,  option show(*) is used with password and code functions.
- win.mainloop(), new.mainloop(),  new2.mainloop() has to be placed in the last order of any GUI configuration, 
no commands will run after it, it is used to show the main App window or the pop ups windows.

