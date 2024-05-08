<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products</title>
    <!-- Link Bootstrap CSS -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="{{ url_for('static', filename='main.css') }}" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1>Products</h1>
        <div class="row">
            {% for product in products %}
            <div class="col-md-4">
                <div class="card">
                    <img src="{{ url_for('static', filename=product['image']) }}" class="card-img-top" alt="Product Image">
                    <div class="card-body">
                        <h5 class="card-title">{{ product['name'] }}</h5>
                        <p class="card-text">Price: ${{ product['price'] }}</p>
                        <p class="card-text">{{ product['description'] }}</p>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</body>
</html>

