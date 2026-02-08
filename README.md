# Overview

I created this software to improve my skills as a software engineer by learning
how web applications work using a Python web framework. My goal was to better
understand how a web server, HTML templates, and a database work together to
create an interactive application.

This software is a Task Tracker web application built using Flask and SQLite.
The application allows users to create tasks, edit tasks, mark tasks as
completed, and filter tasks by status. The web pages are generated dynamically
based on user input and data stored in the database.

To start the test server, run:

py app.py


Then open a web browser and go to:

http://127.0.0.1:5000


The purpose of writing this software was to gain a deeper understanding of web
frameworks, routing, templates, and database integration. I had some previous
exposure to Flask during my internship, but this project helped me better
understand building a complete web application from scratch.

[Software Demo Video](ADD VIDEO LINK HERE)

---

# Web Pages

The application contains two main web pages.

The main page displays all tasks stored in the database. Users can view tasks,
mark them as completed, edit tasks, and filter tasks by status. The task list is
generated dynamically from database data.

The form page is used to create new tasks and edit existing tasks. The same page
is reused for both actions, and the content changes depending on user input and
the selected task.

The application moves between pages using Flask routes that process user
requests and return the correct HTML template.

---

# Development Environment

This software was developed using Visual Studio Code on Windows.

The programming language used was Python. The Flask framework was used to handle
web requests and routing. SQLite was used as the database for storing task data.
HTML and CSS were used to create the user interface, and Jinja templates were
used to dynamically generate web pages.

---

# Useful Websites

* [Flask Documentation](https://flask.palletsprojects.com/)
* [Python Documentation](https://docs.python.org/3/)
* [W3Schools](https://www.w3schools.com/)
* [Stack Overflow](https://stackoverflow.com/)

---

# Future Work

* Add user accounts and authentication
* Add due dates or priorities for tasks
* Improve user interface animations
* Deploy the application online
