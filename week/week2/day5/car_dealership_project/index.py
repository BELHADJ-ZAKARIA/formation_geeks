from flask import Flask, render_template, request
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException
import os
import traceback

from models import vehicles_bp
from models import sales_bp
from models import customers_bp
from models import salespeople_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(vehicles_bp, url_prefix="/")
app.register_blueprint(sales_bp, url_prefix="/")
app.register_blueprint(customers_bp, url_prefix="/")
app.register_blueprint(salespeople_bp, url_prefix="/")

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.errorhandler(404)
def handle_404(e):
    status = 404
    message = getattr(e, "description", "The requested resource was not found.")
    return render_template("errors/404.html", message=message), status

@app.errorhandler(HTTPException)
def handle_http_exception(e: HTTPException):
    """All other HTTP* (e.g., 400, 403, 405, etc.)."""
    status = e.code or 500
    message = e.description or "An unexpected error occurred."
    specific = f"errors/{status}.html"
    try:
        return render_template(specific, message=message), status
    except Exception:
        return render_template("errors/generic.html", status=status, message=message), status

@app.errorhandler(Exception)
def handle_exception(e):
    """Non-HTTP exceptions (code bugs, DB errors, etc.)."""
    status = 500
    traceback.print_exc()
    return render_template("errors/500.html"), status

if __name__ == "__main__":
    app.run(debug=True)
    