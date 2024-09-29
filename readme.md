[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JaleneA/SCT-JaleneA)

# Student Conduct Tracker
Staff System For Recording Positive & Negative Experiences With Students.

## Project Requirements
* Add Student
* Review Student
* Search Student
* View Student Reviews

## Flask Commands
wsgi.py is a utility script for performing various tasks related to the project.

### Admin Commands
```bash
$ flask admin create_staff 
```
```bash
$ flask admin list_staff 
```

### Staff Commands
```bash
$ flask staff add_student 816031000 Bobby Butterbeard bobby.butterbread@mail.com
```
![Screenshot1](./img/addstudent.png)

```bash
$ flask staff add_student
```
* Which will activiate input prompts
![Screenshot2](./img/addstudent1.png)

```bash
$ flask staff add_students
```
```bash
$ flask staff review
```
```bash
$ flask staff view_student_reviews
```
```bash
$ flask staff search_student 
```
```bash
$ flask staff list_student 
```

## Dependencies
* Python3/pip3
* Packages listed in requirements.txt

## Installing Dependencies
```bash
$ pip install -r requirements.txt
```

