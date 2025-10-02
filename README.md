# Ex03 Time Table
# Date:02/10/2025
# AIM
To write a html webpage page to display your slot timetable.

# ALGORITHM
## STEP 1
Create a Django-admin Interface.

## STEP 2
Create a static folder and inert HTML code.

## STEP 3
Create a simple table using `<table>` tag in html.

## STEP 4
Add header row using `<th>` tag.

## STEP 5
Add your timetable using `<td>` tag.

## STEP 6
Execute the program using runserver command.

# PROGRAM
### home.html
```
<!DOCTYPE html>
<html>
<head>
    <title>Semester Timetable</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; text-align: center; }
        th, td { border: 1px solid rgb(58, 5, 5); padding: 10px; }
        th { background-color: rgb(176, 30, 127); }
        h1 { text-align: center; }
    </style>
</head>
<body>
    <h1>Semester Timetable - TAMIZHAN B (25018064)</h1>
    <table>
        <tr>
            <th>Day/Time</th>
            <th>8-10</th>
            <th>10-12</th>
            <th>12-1</th>
            <th>1-3</th>
            <th>3-5</th>
        </tr>
        {% for day, slots in timetable.items %}
        <tr>
            <td><b>{{ day }}</b></td>
            {% for slot in slots %}
            <td>{{ slot }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>

    <h2>Subjects</h2>
    <table>
        <tr><th>Subject Code</th><th>Subject Name</th></tr>
        {% for subj in subjects %}
        <tr>
            <td>{{ subj.code }}</td>
            <td>{{ subj.name }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
```
### views.py
```
from django.shortcuts import render

def home(request):
    # Timetable data (you can later make this dynamic using DB models)
    timetable = {
        "Monday": ["WEB", "PY", "LUNCH", "PY", "CE"],
        "Tuesday": ["FREE SLOT", "CE", "LUNCH", "PY", "CE"],
        "Wednesday": ["WEB", "WEB", "LUNCH", "MM", "CE"],
        "Thursday": ["FREE SLOT", "CE", "LUNCH", "PY", "PY"],
        "Friday": ["FREE SLOT", "WEB", "LUNCH", "FREE SLOT", "FREE SLOT"],
    }
    
    subjects = [
        {"code": "19AI414", "name": "Fundamentals of Web Application Development (WEB)"},
        {"code": "19EN101", "name": "COMMUNICATIVE ENGLISH (CE)"},
        {"code": "19AI301", "name": "PYTHON (PY)"},
       
    ]

    return render(request, "timetable/home.html", {"timetable": timetable, "subjects": subjects})
```
# OUTPUT
<img width="927" height="832" alt="image" src="https://github.com/user-attachments/assets/2f1081dc-17cd-41a0-89cb-893ccc8b90c3" />

# RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
