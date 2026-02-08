from flask import Flask, render_template, request, redirect, url_for
from db import get_db, init_db
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    status = request.args.get("status", "all")

    db = get_db()

    if status == "active":
        tasks = db.execute(
            "SELECT * FROM tasks WHERE completed_at IS NULL ORDER BY created_at DESC"
        ).fetchall()

    elif status == "completed":
        tasks = db.execute(
            "SELECT * FROM tasks WHERE completed_at IS NOT NULL ORDER BY created_at DESC"
        ).fetchall()

    else:
        tasks = db.execute(
            "SELECT * FROM tasks ORDER BY created_at DESC"
        ).fetchall()

    db.close()

    return render_template("index.html", tasks=tasks, status=status)


@app.route("/new", methods=["GET", "POST"])
def new_task():
    if request.method == "POST":
        title = request.form["title"]
        notes = request.form["notes"]

        if not title.strip():
            return render_template(
                "form.html",
                error="Title is required"
            )

        db = get_db()
        db.execute(
            "INSERT INTO tasks (title, notes, created_at) VALUES (?, ?, ?)",
            (title, notes, datetime.now()),
        )
        db.commit()
        db.close()

        return redirect(url_for("index"))

    return render_template("form.html")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_task(id):
    db = get_db()

    task = db.execute(
        "SELECT * FROM tasks WHERE id = ?", (id,)
    ).fetchone()

    if request.method == "POST":
        title = request.form["title"]
        notes = request.form["notes"]

        if not title.strip():
            return render_template(
                "form.html",
                error="Title is required",
                task=task
            )

        db.execute(
            "UPDATE tasks SET title = ?, notes = ? WHERE id = ?",
            (title, notes, id),
        )
        db.commit()
        db.close()

        return redirect(url_for("index"))

    db.close()
    return render_template("form.html", task=task)


@app.route("/toggle/<int:id>")
def toggle_task(id):
    db = get_db()

    task = db.execute(
        "SELECT * FROM tasks WHERE id = ?", (id,)
    ).fetchone()

    if task["completed_at"]:
        db.execute(
            "UPDATE tasks SET completed_at = NULL WHERE id = ?", (id,)
        )
    else:
        db.execute(
            "UPDATE tasks SET completed_at = ? WHERE id = ?",
            (datetime.now(), id),
        )

    db.commit()
    db.close()

    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
