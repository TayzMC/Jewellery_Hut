# website.py
from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
sample_products = [
    {"name": "Diamond Ring", "description": "This 4 bead set round brillant cut lab grown diamonds, each set in 4 platnium claws, standing on top of a 18 carat gold band. ","enviromental_impact": "Lab grown Diamonds, have all the sparkle of natural diamonds without damaging the earth, sustainably sorced from UK labs. All metal on the ring is repurposed pre-loved gold and platnium. Once again, putting a strain on the mining market. Near zero carbon footprint", "price": 1099.99, "image_filename": "DiamondR.webp", "image_url": "/static/DiamondR.webp"},
    {"name": "Gold Necklace", "description": "9 carat gold necklace,with a timeless design, complete with a secure lobster style catch.", "enviromental_impact": "All made from ethically sourced recylced gold, traceable and comes with COC certification (chain of custody)", "price": 599.99, "image_filename": "GoldNeck.webp", "image_url": "/static/GoldNeck.webp"},
    {"name": "Rolex Watch", "description": "Luxurious Rolex watch with a stainless steel bracelet, with a diamond dot face and a fluted 16 carat while gold bezel.","enviromental_impact": "To ensure we are not putting a strain on the earths natural resources, this is a fully refirbished pre-owned Rolex.",  "price": 29999.99, "image_filename": "Rolex.jpg", "image_url": "/static/Rolex.jpg"},
    {"name": "Winged Design Bracelet", "description": "Sterling silver (925), pair of wings holding a gold plated sterling silver sphere on a sterling silver curb chain. Complete with a 1.5 inch adjuster, perfect for anyone.","enviromental_impact": "This is crafted from recycled sterling silver, that has been re-purposed to become this beautiful necklace you see infront of you today. This ensures in our company we dont use the minimal resources we have on this earth.",  "price": 249.99, "image_filename": "product_image.jpg", "image_url": "/static/product_image.jpg"},
    {"name": "Signet Ring", "description": "Timeless black onyx inlaid 9 carat gold gents Signit Ring. A modern take on a design that is centuries old. ","enviromental_impact": "Hand carved onyx to minimize machine usage and emissions. Recycled Gold from donated pieces, to create a stunning work of art that can be used for years to come.  ",  "price": 499.99, "image_filename": "Signit.jpg", "image_url": "/static/Signit.jpg"}
]

@app.route('/')
def index():
    return render_template('index.html', products=sample_products)

@app.route('/product_details/<product_name>')
def product_details(product_name):
    # Find the product with the matching name
    product = next((p for p in sample_products if p['name'] == product_name), None)

    if product:
        return render_template('product_details.html', product=product)
    else:
        return "Product not found"

if __name__ == '__main__':
    app.run(debug=True)
