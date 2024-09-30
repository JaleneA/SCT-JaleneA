[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JaleneA/SCT-JaleneA)

![Tests](https://github.com/uwidcit/flaskmvc/actions/workflows/dev.yml/badge.svg)

# Student Conduct Tracker
Staff System For Recording Positive & Negative Experiences With Students.


## Project Requirements
* Add Student
* Review Student
* Search Student
* View Student Reviews


## Dependencies
* Python3/pip3
* Packages listed in requirements.txt


## Installing Dependencies
```bash
$ pip install -r requirements.txt
```


## Flask MVC Template
A template for flask applications structured in the Model View Controller pattern


## Initializing the Database
When connecting the project to a fresh empty database ensure the appropriate configuration is set then file then run the following command. This must also be executed once when running the app on heroku by opening the heroku console, executing bash and running the command in the dyno.


```bash
$ flask init
```


## Flask Commands
wsgi.py is a utility script for performing various tasks related to the project.


### Admin Commands
```bash
# Creating a Staff Account (inline)
$ flask admin create_staff Mrs. Bubble Bub bubble.bub@staff.com N bubblepass 1
```

```bash
# Creating a Staff Account (interactive input)
$ flask admin create_staff 
```

```bash
# List All Staff Accounts
$ flask admin list_staff 
```
<details>
<summary>Snippets</summary>

![Screenshot1](./img/createstaff1.png)
![Screenshot2](./img/createstaff2.png)
![Screenshot3](./img/liststaff.png)

</details>


### Staff Commands
```bash
# Adding a Student Record (inline)
$ flask staff add_student 816031000 Bobby Butterbeard bobby.butterbread@mail.com
```

```bash
# Adding a Student Record (interactive input)
$ flask staff add_student
```

```bash
# Adding Multiple Student Records (inline)
$ flask staff add_students students.csv
```

```bash
# Adding Multiple Student Records (interactive input)
$ flask staff add_students
```

```bash
# Reviewing a Student (inline)
$ flask staff review 816031000 Overall Good Student 1
```

```bash
# Reviewing a Student (interactive input)
$ flask staff review
```

```bash
# Viewing Student Reviews (inline only)
$ flask staff view_student_reviews 816031000
```

```bash
# Search Student (inline only)
$ flask staff search_student 816031000
```

```bash
# List All Students
$ flask staff list_students
```

<details>
<summary>Snippets</summary>

![Screenshot4](./img/addstudent1.png)
![Screenshot5](./img/addstudent2.png)
![Screenshot6](./img/addstudents1.png)
![Screenshot7](./img/addstudents2.png)
![Screenshot8](./img/review1.png)
![Screenshot9](./img/review2.png)
![Screenshot10](./img/studentreview.png)
![Screenshot11](./img/search.png)
![Screenshot12](./img/liststudents.png)

</details>

# Testing

## Unit & Integration
Unit and Integration tests are created in the App/test.
You can then execute all user tests as follows:

```bash
$ flask test staff
```

or run all application tests with the following command:

```bash
$ pytest
```