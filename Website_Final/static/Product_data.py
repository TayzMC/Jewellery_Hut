from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create Flask application
app = Flask(__name__)

# Configure SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy database
db = SQLAlchemy(app)

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.description}')"

# Create database tables
with app.app_context():
    db.create_all()

    # Sample product data
    products_data = [
        { "name": "Angel Necklace", "price": 10.99, "description": "Description of Product 1" },
        { "name": "Product 2", "price": 19.99, "description": "Description of Product 2" },
        { "name": "Product 3", "price": 29.99, "description": "Description of Product 3" }
    ]

    # Populate database with product data
    for product_data in products_data:
        product = Product(
            name=product_data["name"],
            price=product_data["price"],
            description=product_data["description"]
        )
        db.session.add(product)

    db.session.commit()
