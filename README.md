# hsu-tung-hsieh-tbii-exam

# App (GUI) -- I HAVE A FEVER

## Instruction: How to Start the App?
1. Create a folder on your device
2. Download EVERYTHING in this repository to the folder
3. Open the folder with your preferred python program (PyCharm is recommended)
4. Run the python file "app.py"
5. Enjoy :)

## Important Notes
1.  Please ensure that all the images and the app.py file are in the same folder
2.  Please do not adjust the frame size (e.g. fullscreen) to maintain the original layouts
3.  It's normal if the program does not react immediately because it can be taxing for the system. Give it a few seconds and it'll work.
4.  Some users have problems with the calendar widget. You can try double-clicking it first. If that doesn't work just enter the date manualy
5.  Please wait for a few seconds if a page is blank. The system might be loading it.

## Disclaimer
This app (GUI) is not intended to provide any medical advice. Please seek professonal assistance if necessary


------------------------------------------------
## About the app
### Introduction
This app (GUI) is named "I HAVE A FEVER" and is built using Python with the TK, PIL, and datetime libraries. It aims to assist people when someone has a fever by allowing users to track body temperature and medicine intake. Additionally, it provides quick diagnoses, medical knowledge, and an export function for doctors' reference.

### Main Functional Pages
Users first need to complete the registration process. Afterward, they are directed to the homepage, which features five buttons linked to different pages:
-	Temperature Page: Tracks and records body temperature.
-	Medicine Page: Displays dosage instructions in a tree-view table and tracks medication intake.
-	Dr. Smart Page: Provides a quick analysis to determine if medical help is needed.
-	Medical Knowledge Page: Contains infographics about fever and related topics.
-	Export Function: Allows users to export the patient’s basic information and data from the temperature and medication trackers.

### Design
Video demonstration of the GUI design: https://youtu.be/-t-Q8Wt2KVs (This is what the GUI should look like)

-	Registration Process: The registration involves multiple pages, each with a background image. The app’s main character—an eggplant—appears frequently with variations to entertain users. Labels and entry boxes are positioned next to the eggplant using the "place" method for flexibility.

-	Homepage: The center of the homepage features the eggplant. Five items—a medicine can, thermometer, stethoscope, book, and printer—are actually clickable buttons. The design tries to integrate the buttons into the theme, adding cuteness and consistency.

-	Functional Pages: Widgets on the main functional pages are primarily positioned using the grid method. Pages with numerous elements or various types of content (like the medicine and medical knowledge pages) often use nested frames to maintain organization and layout consistency.

-	General Design Principles: The app adopts a consistent theme color. Most labels, buttons, and frames follow predefined sizes or fonts stored in variables to ensure uniformity and harmony. (You can definitely change the fonts!)

### Challenges and Limitations

- The "treeview" function does not support inserting widgets other than text. To achieve similar results, such as on the medicine knowledge page, I had to build it using buttons and various definitions, which complicated the code.
  
- Aligning many elements neatly on a page is challenging, often requiring nested frames to maintain a clean layout.


## Reference





