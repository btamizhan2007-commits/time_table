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
