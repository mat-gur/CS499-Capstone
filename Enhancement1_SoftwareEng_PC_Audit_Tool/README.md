# Enhancement One: Software Design and Engineering 

This folder contains my Enhancement One artifact for the CS-499 Computer Science Capstone. This enhancement falls under the category of **Software Engineering and Design**.

The project is an enhanced version of my PC Audit Tool — a Python-based GUI application that gathers USB activity, antivirus information, and device audit data. This version features improved structure, enhanced error handling, refined logging, and updated UI elements.


## 📁 Folder Structure

- `src/` — All Python source code modules
- `docs/` — Word documents including: run instructions, user guide, and narrative.


## 📄 Documentation

- [Run Instructions (Word)](./docs/PC%20Audit%20Tool_Run_Instructions%20Rev1.1.docx)

- [User Guide (Word)](./docs/PC%20Audit%20Tool_User_Guide%20Rev%201.1.docx)
  
- [Narrative (Word)](./docs/3-2%20Milestone%20Two_Enhancement1_SWDesign&Eng_Guarino,Matthew.docx)


## 🎥 Demonstration Video

Watch the walkthrough of this enhancement on YouTube:  
🔗 [Enhancement 1 - PC Audit Tool Demo](https://youtu.be/6jackT5Y_oc)


## 📘 Enhancement Narrative

### What is the artifact?

This artifact is a personal project of mine, which I call the “PC Audit Tool." I began creating it around February of this year (2025). The tool is a Python-based desktop application that uses a GUI (graphical user interface). The idea was to mimic what my job was using to audit their PCs in a secure area. My design, however, is very simple and small. It gives users quick access to information like active USB ports, system ping and ipconfig checks, and antivirus information (in my case: Malwarebytes info)

### Why was it selected?

I selected this artifact because I wanted to see if I could simply copy what my job had and make the application “better” in a sense. Going through the enhancement of this application taught me that it isn’t as easy as just compiling a bunch a code in one file and hoping for the best. By enhancing the project, it taught me to produce cleaner code, separate certain components, and improve UI design. All of which are important skills in this field of software engineering. 

### What enhancements were made?

The enhancements that I completed this week were the following:
1.	Modularizing subprocess logic
2.	Put in some error handling with try/expect blocks 
3.	Added a logging tab to track user activity (i.e., USB scans, ping, antivirus check)
4.	Redesigned the UI by adding some icons and a visual checklist for when certain tasks were completed (USB scan, ping, antivirus check)
5.	Made a fallback antivirus detection (for users without Malwarebytes)
  
NOTE: Even though enhancement (V) was not in the original plan, I realized that not everyone is going to have Malwarebytes installed on their PCs. Rather than drastically changing the application, the fallback is to check Windows Defender’s information. 


### What skills and course outcomes were demonstrated?

For this enhancement, my goal was to meet 3, 4, and 5 of the course outcomes. I’m happy to say that these outcomes have been met with the work that I’ve done. 
Starting with outcome 3, which focuses on designing and evaluating computing solutions using sound algorithmic principles, was clearly demonstrated in the way I modularized subprocess logic and built mechanisms for parsing system data (like USB activity and antivirus logs). I made some trade-offs to prevent the GUI from freezing or crashing when dealing with external system calls by making better error handling, status feedback, and timeouts. The entire application is designed around solving real-world problems, with practical and scalable techniques.
With outcome 4, it was met by using well-founded tools like Tkinter, the Python subprocess module, and structured logging. These enhancements improved the overall usability and maintainability of the application as a whole. The value added with features like USB checks, real-time ping, and event log aligns well with the security mindset for IT professionals. 
Lastly, outcome 5 is the most important because of my concentration in information security. The improvements I made to detect USB usage, monitor antivirus logs, and surface system health shortcuts show a strong security mindset. These aren’t just nice-to-have features; they’re about visibility, traceability, and anticipating misuse or vulnerability. I also made sure that subprocesses were executed in a controlled, non-blocking manner to avoid accidental system strain or potential exploitation.
With that being said, no changes to my outcome coverage plan are needed at this time.


### Reflection on the process
While enhancing and modifying my artifact, I quickly began to come up with more and more ways to improve it. For example, the visual checklist was not part of the enhancement plan, but it’s a nice addition to this application because it visually shows you what has been checked and what has not. Also, going through the improvements, I thought to myself, “How can I make this visually more appealing?” Which is why I added custom icons.
There were a couple of challenges that I faced while working on this project. 1.) the readback of the USB devices and 2.) System tools like Control Panel, System Info, Computer Management, and event logs would lock up the application if two were open at the same time. The USB readback issue was that I was reading every port on my PC and motherboard, but it wasn’t showing what it was. This has since been fixed, and now you can see if a USB storage device is plugged in. I had to research more reliable methods for parsing USB history and refine the logic to make sure that it’s consistent. 
This project has taught me a lot about writing software that not only works, but works well under different conditions and use cases.

