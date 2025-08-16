# Enhancement Three: Databases

This folder contains my Enhancement Three artifact for the CS-499 Computer Science Capstone. This enhancement falls under the **Databases** category.

The project is an enhanced MongoDB-backed dashboard built with Python and Dash. This version focuses on database improvements: input validation/sanitization, modular database functions, basic authentication, CSV/JSON export, and MongoDB indexing for better efficiency.

## 📁 Folder Structure
- `src/`  — All Python source code, including original and enhanced versions
- `docs/` — Word docs (run instructions, narrative)

## 📄 Documentation
- [Run Instructions (Word)](https://github.com/mat-gur/CS499-Capstone/blob/main/Enhancement3_Databases_MongoDB_Dashboard/docs/MongoDB%20Dashboard_Run_Instructions%20Rev1.1.docx)
- [User Guide (Word)](https://github.com/mat-gur/CS499-Capstone/blob/main/Enhancement3_Databases_MongoDB_Dashboard/docs/MongoDB%20Dashboard_User_Guide%20Rev1.1.docx)
- [Narrative (Word)](./docs/5-2%20Milestone%20Four_Enhancement%20Three%20-%20Databases_Guarino%2CMatthew.docx)


## 🎥 Demonstration Video
A walkthrough of this enhancement is available on YouTube:  
🔗 [Enhancement 3 - Databases Demo](https://youtu.be/RAM9ffxWQqY)

## 📘 Enhancement Narrative

### What is the artifact?
The artifact I’ve continued to enhance is the interactive MongoDB dashboard originally developed during my CS-340 Client-Server Development course. Built with Dash (by Plotly), Python, and MongoDB, the application allows users to filter and analyze shelter dog data from the Austin Animal Center. While the original project was finalized back in February, this week’s work focused specifically on improving the application's database interaction and security practices as part of my capstone project.

### Why was it selected?
I chose this artifact again because of its flexibility and relevance to real-world database applications. It provided a great foundation to showcase improvements in secure database access, modular query logic, and performance optimizations. For this enhancement, I focused entirely on how the dashboard interacts with the database layer, ensuring it is both efficient and secure.

### What enhancements were made?
1. Input Validation and Sanitization: All user-provided inputs (such as filters) are now validated before interacting with the database to prevent injection attacks and malformed queries.
2. CSV/JSON Export Feature: I added secure export functionality to allow users to download filtered datasets in CSV or JSON format for offline analysis.
3. Authentication: A basic login system was added to restrict access to the dashboard, protecting sensitive database operations from unauthorized users.
4. Indexing: MongoDB indexes were created on frequently queried fields (e.g., breed, outcome type) to significantly improve query efficiency.

### What skills and course outcomes were demonstrated?
Yes, the enhancements I made this week align strongly with outcome five, which emphasizes secure and efficient data management. By implementing input validation, user authentication, and MongoDB indexing, I demonstrated my understanding of best practices in secure database design and data processing. I also continued to support outcome four by using modern tools and frameworks in a scalable and professional way. No changes to my outcome coverage plan are needed at this time.

### Reflection on the process
This week’s focus showed me how critical it is to consider not just the frontend experience, but also how data flows behind the scenes. One challenge I faced was managing callback errors when dynamic components weren’t yet available during login, which required setting suppress_callback_exceptions=True and carefully organizing layout initialization. Another challenge was integrating login functionality into an already complex callback system. While it took some trial and error to manage the layout switching logic, this process helped me better understand Dash’s callback lifecycle and state management.
In the end, this enhancement taught me how to build secure, modular database access in a full-stack context. It also reinforced the value of user authentication and efficient query design in real-world applications.

## 📚 References
1. Valdarrama, S. (2023, November 27). Sorting algorithms in Python. https://realpython.com/sorting-algorithms-python/

2. Miller, B. N., & Ranum, D. L. (n.d.). Problem solving with algorithms and data structures using python — problem solving with algorithms and data structures 3rd Edition. https://runestone.academy/ns/books/published/pythonds3/index.html

3. Team, M. D. (n.d.). Indexes. Database Manual - MongoDB Docs. https://www.mongodb.com/docs/manual/indexes/#get-started

4. Input Validation - OWASP Cheat Sheet Series. (n.d.). https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html

5. csv — CSV File Reading and Writing. (n.d.). Python Documentation. https://docs.python.org/3/library/csv.html

6. json — JSON encoder and decoder. (n.d.). Python Documentation. https://docs.python.org/3/library/json.html

7. Team, M. D. (n.d.-b). Security. Database Manual - MongoDB Docs. https://www.mongodb.com/docs/manual/security/
