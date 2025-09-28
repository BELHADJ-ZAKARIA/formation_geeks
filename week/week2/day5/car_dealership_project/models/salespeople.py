# models/salespeople.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.index import get_db_connection

salespeople_bp = Blueprint("salespeople", __name__, template_folder="../templates")

@salespeople_bp.route("/salespeople")
def index():
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for("vehicles.index"))

    show = request.args.get("show")  # "archived" to list hidden ones
    cur = conn.cursor()
    if show == "archived":
        cur.execute("""
            SELECT id, name, email, phone, photo_url, is_active
            FROM salespeople
            WHERE is_active = FALSE
            ORDER BY name
        """)
    else:
        cur.execute("""
            SELECT id, name, email, phone, photo_url, is_active
            FROM salespeople
            WHERE is_active = TRUE
            ORDER BY name
        """)
    people = cur.fetchall()
    cur.close(); conn.close()
    return render_template("salespeople/index.html", people=people, show=show)

@salespeople_bp.route("/salespeople/<int:sp_id>")
def details(sp_id: int):
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for("salespeople.index"))
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, phone, photo_url, is_active FROM salespeople WHERE id=%s", (sp_id,))
    sp = cur.fetchone()
    if not sp:
        cur.close(); conn.close()
        flash("Salesperson not found.", "error")
        return redirect(url_for("salespeople.index"))

    cur.execute("""
    SELECT
            COUNT(s.id) AS cnt,
            COALESCE(SUM(v.price), 0) AS total
    FROM
        sales AS s
    JOIN
        vehicles AS v ON v.id = s.vehicle_id
    WHERE
    s.salesperson_id = %s;
      """, (sp_id,))
    stats = cur.fetchone()
    cur.close(); conn.close()
    return render_template("salespeople/details.html", sp=sp, stats=stats)

@salespeople_bp.route("/salespeople/create", methods=["GET","POST"])
def create():
    if request.method == "POST":
        name = (request.form.get("name") or "").strip()
        email = (request.form.get("email") or "").strip().lower()
        phone = (request.form.get("phone") or "").strip() or None
        photo_url = (request.form.get("photo_url") or "").strip() or None

        if not name or not email:
            flash("Name and Email are required.", "error")
            return render_template("salespeople/create.html", name=name, email=email, phone=phone, photo_url=photo_url)

        conn = get_db_connection()
        if conn is None:
            flash("ERROR: Could not connect to the database.", "error")
            return redirect(url_for("salespeople.index"))

        cur = conn.cursor()
        try:
            cur.execute("""
              INSERT INTO salespeople (name, email, phone, photo_url)
              VALUES (%s, %s, %s, %s)
              RETURNING id
            """, (name, email, phone, photo_url))
            _new_id = cur.fetchone()["id"]
            conn.commit()
            flash("Salesperson added!", "success")
            return redirect(url_for("salespeople.index"))
        except Exception as e:
            conn.rollback()
            flash(f"Database error: {e}", "error")
            return render_template("salespeople/create.html", name=name, email=email, phone=phone, photo_url=photo_url)
        finally:
            cur.close(); conn.close()

    return render_template("salespeople/create.html")

# SOFT delete: archive (hide from list, keep in DB)
@salespeople_bp.route("/salespeople/<int:sp_id>/delete", methods=["POST"])
def delete(sp_id: int):
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for("salespeople.index"))
    cur = conn.cursor()
    try:
        cur.execute("UPDATE salespeople SET is_active = FALSE WHERE id = %s", (sp_id,))
        conn.commit()
        flash("Salesperson archived (hidden).", "info")
    except Exception as e:
        conn.rollback()
        flash(f"Database error: {e}", "error")
    finally:
        cur.close(); conn.close()
    return redirect(url_for("salespeople.index"))

@salespeople_bp.route("/salespeople/<int:sp_id>/restore", methods=["POST"])
def restore(sp_id: int):
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for("salespeople.index", show="archived"))
    cur = conn.cursor()
    try:
        cur.execute("UPDATE salespeople SET is_active = TRUE WHERE id = %s", (sp_id,))
        conn.commit()
        flash("Salesperson restored.", "success")
    except Exception as e:
        conn.rollback()
        flash(f"Database error: {e}", "error")
    finally:
        cur.close(); conn.close()
    return redirect(url_for("salespeople.index", show="archived"))