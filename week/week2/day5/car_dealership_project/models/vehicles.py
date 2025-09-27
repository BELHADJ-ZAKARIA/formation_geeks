from flask import Blueprint, render_template, request, redirect, url_for, flash
import psycopg2.extras
from database.index import get_db_connection
import math

# Create a Blueprint for vehicle-related routes
vehicles_bp = Blueprint("vehicles", __name__)

# --- Helper Function ---
def get_vehicle(vehicle_id):
    """Gets a single vehicle by its ID."""
    conn = get_db_connection()
    if conn is None:
        flash("Database connection failed.", "error")
        return None
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('SELECT * FROM vehicles WHERE id = %s', (vehicle_id,))
    vehicle = cursor.fetchone()
    cursor.close()
    conn.close()
    return vehicle

# --- Routes ---
@vehicles_bp.route('/')
def index():
    """Shows a paginated list of all vehicles."""
    conn = get_db_connection()
    
    # CRITICAL FIX: Check if the connection failed before using it
    if conn is None:
        flash("ERROR: Could not connect to the database. Please check your configuration.", "error")
        # Since you have no templates yet, we return a simple error message.
        return "<h1>Database Connection Error</h1><p>Could not connect to the database. Please check the server logs.</p>", 500

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Pagination logic
    page = request.args.get('page', 1, type=int)
    per_page = 6
    offset = (page - 1) * per_page
    
    cursor.execute('SELECT COUNT(*) FROM vehicles')
    total_vehicles = cursor.fetchone()[0]
    total_pages = math.ceil(total_vehicles / per_page)
    
    cursor.execute('SELECT * FROM vehicles ORDER BY id DESC LIMIT %s OFFSET %s', (per_page, offset))
    vehicles = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    # This will fail until you create the index.html template, but the database error is fixed.
    return render_template('index.html', vehicles=vehicles, page=page, total_pages=total_pages)

@vehicles_bp.route('/search')
def search():
    """Searches for vehicles by make or model."""
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for('vehicles.index'))

    query = request.args.get('query', '')
    if not query:
        return redirect(url_for('vehicles.index'))
        
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    search_query = f"%{query}%"
    cursor.execute('SELECT * FROM vehicles WHERE make ILIKE %s OR model ILIKE %s', (search_query, search_query))
    vehicles = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    flash(f'{len(vehicles)} results found for "{query}"', 'info')
    return render_template('index.html', vehicles=vehicles, page=1, total_pages=1, search_query=query)


@vehicles_bp.route('/<int:vehicle_id>')
def details(vehicle_id):
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for('vehicles.index'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM vehicles WHERE id=%s", (vehicle_id,))
    vehicle = cur.fetchone()
    if not vehicle:
        cur.close(); conn.close()
        flash("Vehicle not found.", "error")
        return redirect(url_for('vehicles.index'))

    cur.execute("""
      SELECT s.id, s.sale_date, s.sale_price,
             c.name AS customer_name,
             sp.name AS salesperson_name
      FROM sales s
      JOIN customers c ON c.id = s.customer_id
      LEFT JOIN salespeople sp ON sp.id = s.salesperson_id
      WHERE s.vehicle_id = %s
    """, (vehicle_id,))
    sale = cur.fetchone()
    cur.close(); conn.close()
    return render_template('details.html', vehicle=vehicle, sale=sale)

@vehicles_bp.route('/create', methods=('GET', 'POST'))
def create():
    """Handles the creation of a new vehicle."""
    if request.method == 'POST':
        vin = request.form['vin']
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        price = request.form['price']
        color = request.form['color']
        photo_url = request.form.get("photo_url")
        
        if not all([vin, make, model, year, price, photo_url]):
            flash('All fields except color are required!', 'error')
        else:
            conn = get_db_connection()
            if conn is None:
                flash("ERROR: Could not connect to the database.", "error")
                return redirect(url_for('vehicles.index'))

            cursor = conn.cursor()
            cursor.execute('INSERT INTO vehicles (vin, make, model, year, price, color, photo_url) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                           (vin, make, model, year, price, color, photo_url))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Vehicle added successfully!', 'success')
            return redirect(url_for('vehicles.index'))
            
    return render_template('create.html')

@vehicles_bp.route('/<int:vehicle_id>/edit', methods=('GET', 'POST'))
def edit(vehicle_id):
    """Handles updating an existing vehicle."""
    vehicle = get_vehicle(vehicle_id)
    if vehicle is None:
        flash('Vehicle not found or database error.', 'error')
        return redirect(url_for('vehicles.index'))

    if request.method == 'POST':
        vin = request.form['vin']
        make = request.form['make']
        model = request.form['model']
        year = request.form['year']
        price = request.form['price']
        color = request.form['color']
        photo_url = request.form.get("photo_url")
        
        if not all([vin, make, model, year, price, photo_url]):
            flash('All fields except color are required!', 'error')
        else:
            conn = get_db_connection()
            if conn is None:
                flash("ERROR: Could not connect to the database.", "error")
                return redirect(url_for('vehicles.index'))
                
            cursor = conn.cursor()
            cursor.execute('UPDATE vehicles SET vin = %s, make = %s, model = %s, year = %s, price = %s, color = %s, photo_url = %s WHERE id = %s',
                           (vin, make, model, year, price, color, photo_url, vehicle_id))
            conn.commit()
            cursor.close()
            conn.close()
            flash('Vehicle updated successfully!', 'success')
            return redirect(url_for('vehicles.index'))

    return render_template('edit.html', vehicle=vehicle)

@vehicles_bp.route('/<int:vehicle_id>/delete', methods=('POST',))
def delete(vehicle_id):
    """Handles the deletion of a vehicle."""
    # The get_vehicle helper already checks for existence
    vehicle = get_vehicle(vehicle_id)
    if vehicle:
        conn = get_db_connection()
        if conn is None:
            flash("ERROR: Could not connect to the database.", "error")
            return redirect(url_for('vehicles.index'))

        cursor = conn.cursor()
        cursor.execute('DELETE FROM vehicles WHERE id = %s', (vehicle_id,))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Vehicle deleted successfully.', 'success')
    else:
        flash('Vehicle not found or database error.', 'error')
        
    return redirect(url_for('vehicles.index'))

@vehicles_bp.route('/stats')
def stats():
    conn = get_db_connection()
    if conn is None:
        flash("ERROR: Could not connect to the database.", "error")
        return redirect(url_for('vehicles.index'))

    cur = conn.cursor()

    # 1) KPIs
    cur.execute("SELECT COUNT(*) AS cnt, COALESCE(SUM(price),0) AS total_value FROM vehicles")
    row = cur.fetchone()
    total_vehicles = row["cnt"] if row else 0
    inventory_value = float(row["total_value"]) if row else 0.0

    # 2) Vehicles by make (bar)
    cur.execute("""
        SELECT make, COUNT(*) AS make_count
        FROM vehicles
        GROUP BY make
        ORDER BY make;
    """)
    vbymake = cur.fetchall()
    labels_make = [r["make"] for r in vbymake]
    counts_make = [int(r["make_count"]) for r in vbymake]

    # 3) Average price by make (bar)
    cur.execute("""
        SELECT make, ROUND(AVG(price)::numeric, 2) AS avg_price
        FROM vehicles
        GROUP BY make
        ORDER BY avg_price DESC;
    """)
    avgpm = cur.fetchall()
    labels_avg_make = [r["make"] for r in avgpm]
    values_avg_make = [float(r["avg_price"]) for r in avgpm]

    # 4) Vehicles by year (line)
    cur.execute("""
        SELECT year, COUNT(*) AS cnt
        FROM vehicles
        GROUP BY year
        ORDER BY year;
    """)
    vbyyear = cur.fetchall()
    labels_year = [int(r["year"]) for r in vbyyear]
    counts_year = [int(r["cnt"]) for r in vbyyear]

    # 5) Price buckets (doughnut)
    cur.execute("""
        WITH b AS (
          SELECT CASE
              WHEN price < 10000 THEN 'Under 10k'
              WHEN price < 20000 THEN '10k–20k'
              WHEN price < 30000 THEN '20k–30k'
              WHEN price < 40000 THEN '30k–40k'
              ELSE '40k+'
            END AS bucket
          FROM vehicles
        )
        SELECT bucket, COUNT(*) AS cnt
        FROM b
        GROUP BY bucket
        ORDER BY CASE bucket
          WHEN 'Under 10k' THEN 1
          WHEN '10k–20k' THEN 2
          WHEN '20k–30k' THEN 3
          WHEN '30k–40k' THEN 4
          ELSE 5
        END;
    """)
    pb = cur.fetchall()
    bucket_labels = [r["bucket"] for r in pb]
    bucket_counts = [int(r["cnt"]) for r in pb]

    # 6) Most/least expensive (cards)
    cur.execute("SELECT * FROM vehicles ORDER BY price DESC LIMIT 1")
    most_expensive = cur.fetchone()
    cur.execute("SELECT * FROM vehicles ORDER BY price ASC LIMIT 1")
    least_expensive = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        "stats.html",
        total_vehicles=total_vehicles,
        inventory_value=inventory_value,
        vehicles_by_make=vbymake,
        most_expensive=most_expensive,
        least_expensive=least_expensive,
        # chart data
        labels_make=labels_make, counts_make=counts_make,
        labels_avg_make=labels_avg_make, values_avg_make=values_avg_make,
        labels_year=labels_year, counts_year=counts_year,
        bucket_labels=bucket_labels, bucket_counts=bucket_counts
    )
