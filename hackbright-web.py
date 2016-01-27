from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    grades = hackbright.get_grades_by_github(github)
    
    return render_template('student_info.html', 
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)


@app.route("/student-add", methods=["GET"])
def get_student_creation_form():
    """Show form for creating a student."""
    
    return render_template("student_creation_form.html")


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-add", methods=["POST"])
def student_add():
    """Add a student."""

    github = request.form.get("github")
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    hackbright.make_new_student(first_name, last_name, github)

    return render_template("user_added.html", first_name=first_name,
                            last_name=last_name, github=github)


@app.route("/project", methods=["GET"])
def get_project():
    """Display information for a project."""

    project_title = request.args.get("project-title", "")
    title, description, max_grade = hackbright.get_project_by_title(project_title)
    grades = hackbright.get_grades_by_title(title)

    return render_template("project_info.html",
                           project_title=title,
                           project_description=description,
                           max_grade=max_grade,
                           grades=grades)


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
