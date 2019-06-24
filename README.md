MISSION:
This project is a simple Python script to sort the files in a folder based on their file extension. 
My goal for this project was to learn how to perform operating system functions in Python and learn how to automate tasks. 
In doing this project, I have also learned about the functionality of batch files, as well as the great utility of the Windows Task Scheduler.
Currently, this project is only functional (or at least automatable) on a Windows system, and requires some sort of Python installation to be used functionally.

INSTRUCTIONS: 
The python script, when run, sorts the contents of the its parent folder (aka directory) into subfolders based on file extension. 
To properly use this script to sort a folder, place the "folder_cleaner" folder in the folder you want to clean.
Then, edit the batch file (.bat) that runs the Python file using python.exe. An example file is included - just fill in the path examples with the actual paths on your computer.
Running this .bat file by double left-clicking will run the script that sorts your folder. One could also run the python script from the command line, if they have Python in their PATH environment. 

To automate the sorting of the file, use the Windows Task Scheduler and schedule a task that runs the .bat file whenever you prefer. 
Personally, I use "on workstation unlock," so the folder does not get sorted while you are manipulating files within it.
IMPORTANT: Make sure that in the "action" section of the task, the "Start in (optional)" section is filled in with the location of the .bat file,
and that the .bat file is in the same folder as the python script - which should be in a subfolder of the folder you want to sort.

OTHER NOTES:
If this project is updated later, some additions might include:
- removal of duplicate files
- sorting of files into folders other than by file type
- a second batch file or other program that automatically adds the first batch file to the task scheduler when run. 
- an executable file that generates the script and batch file and schedules them on the Task scheduler automatically (without requiring Python being previously installed)
- Linux functionality