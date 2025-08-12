# Enhancement Two: Algorithms and Data Structure

This folder contains my Enhancement Two artifact for the CS-499 Computer Science Capstone. This enhancement falls under the category of Data Structures and Algorithms.

The project is an enhanced version of my MongoDB Dashboard, a Python-based web application built with Dash that visualizes and filters animal shelter data. This version features a custom Binary Search Tree (BST) for in-memory data filtering, enhanced performance through MongoDB indexing, and  improvements in input validation.


## 📁 Folder Structure

- `src/` — All Python source code, including original and enhanced versions
- `docs/` — Word documents including run instructions, user guide, and enhancement narrative

## 📄 Documentation

- [Run Instructions (Word)](./docs/MongoDB%20Dashboard_Run_Instructions%20Rev1.1.docx)  
- [User Guide (Word)](./docs/MongoDB%20Dashboard_User_Guide%20Rev1.1.docx)
- [Narrative (Word)](./docs/4-2%20Milestone%20Three_Enhancement%20Two_Algorithms&DataStructure_Guarino,Matthew.docx)

## 🎥 Demonstration Video

Watch the walkthrough of this enhancement on YouTube:  
🔗 [Enhancement 2 - MongoDB Dashboard Demo](https://youtu.be/aVHHI_yZ5Zc)


## 📘 Enhancement Narrative

### What is the artifact?

The artifact that I’ve decided to enhance is an interactive MongoDB dashboard originally made for a previous course project (CS-340 Client Server Development), focused on database interaction and visualization. The application was built using Dash by Plotly, Python, and MongoDB. Its main purpose was to help users filter and analyze shelter dog data from the Austin Animal Center. The final submission of this project was back in February of this year; since then, it has been enhanced to incorporate stronger algorithmic and data structure implementations as part of this capstone course. 

### Why was it selected?

I chose this artifact because it shows my ability to work with real-world data while applying principles of efficient data handling, searching, and sorting. Before the enhancement, the dashboard had basic functionality and “light” MongoDB filtering. However, for this enhancement, I made several improvements that better align with best practices in algorithms and data structures. 

### What enhancements were made?

I have made the following enhancements:
1.	Made client-side sorting and searching using custom Python logic
2.	Created an in-memory breed index using a Python dictionary to streamline filtering logic and reduce redundancy in repeated queries.
3.	Refactored the sorting and filtering logic into modular functions to promote code reuse and separation. 
4.	I made a binary search tree (BST) to organize dog entries by intake age, enabling efficient age range filtering and supporting future scalability for larger databases. 


### What skills and course outcomes were demonstrated?

Yes, I met the course outcomes that I originally set in the beginning. For outcome three, I applied algorithmic thinking and principles to redesign the dashboard’s data handling logic. With the BST and a breed index dictionary in place, both are strong examples of how I approached problems with data structure tradeoffs in mind. In outcome four, I leveraged Python and Dash effectively, using these tools in a professional and scalable way. I also modularized the application logic, which not only improves maintainability but also shows my ability to apply innovative computing techniques. 

### Reflection on the process

Working on this artifact helped me see just how much of an impact efficient data structures can make on user experience, especially when dealing with interactive applications. One challenge that I faced was making sure that the client-side enhancements did not interfere with the original MongoDB filtering or break the user interface. Another challenge was figuring out how to integrate the BST structure meaningfully within a web-based dashboard while keeping the logic clear and traceable. 
In the end, these challenges helped me become a better problem solver. I learned how to break the logic into smaller, testable components and gained a deeper understanding of the way memory and performance optimization matter, even in user-facing applications. 
