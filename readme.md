[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/JaleneA/SCT-JaleneA)

![Tests](https://github.com/uwidcit/flaskmvc/actions/workflows/dev.yml/badge.svg)

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
$ flask admin create_staff Mrs. Bubble Bub bubble.bub@staff.com N bubblepass 1
```
![Screenshot1](./img/createstaff1.png)

```bash
$ flask admin create_staff 
```
![Screenshot2](./img/createstaff2.png)

```bash
$ flask admin list_staff 
```
![Screenshot3](./img/liststaff.png)

### Staff Commands
```bash
$ flask staff add_student 816031000 Bobby Butterbeard bobby.butterbread@mail.com
```
![Screenshot4](./img/addstudent1.png)

```bash
$ flask staff add_student
```
![Screenshot5](./img/addstudent2.png)

```bash
$ flask staff add_students students.csv
```
![Screenshot6](./img/addstudents1.png)

```bash
$ flask staff add_students
```
![Screenshot7](./img/addstudents2.png)

```bash
$ flask staff review 816031000 Overall Good Student 1
```
![Screenshot8](./img/review1.png)

```bash
$ flask staff review
```
![Screenshot9](./img/review2.png)

```bash
$ flask staff view_student_reviews 816031000
```
![Screenshot10](./img/studentreview.png)

```bash
$ flask staff search_student 816031000
```
![Screenshot11](./img/search.png)

```bash
$ flask staff list_student
```
![Screenshot12](./img/liststudents.png)

## Dependencies
* Python3/pip3
* Packages listed in requirements.txt

## Installing Dependencies
```bash
$ pip install -r requirements.txt
```

