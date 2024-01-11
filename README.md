# FoodOnline: Online Food Ordering Platform

## Overview
FoodOnline is a Django-based web application that provides an online platform for ordering food from various restaurants. It is designed to facilitate users in searching and ordering food from their favorite restaurants with ease.

## Features
- **User Authentication**: Supports customer and vendor accounts with registration, login, and password reset functionalities.
- **Vendor Management**: Allows vendors to manage their profiles, menus, and orders.
- **Dynamic Menu Building**: Vendors can create and modify their menus, adding categories and food items dynamically.
- **Cart Functionality**: Users can add food items to their cart and proceed to checkout.
- **Order Management**: Supports order placement, tracking, and management for both customers and vendors.
- **Payment Integration**: Includes payment processing functionality (e.g., PayPal integration).
- **Responsive Design**: The application is designed with a responsive layout for optimal viewing on various devices.

## Installation
1. **Clone the Repository**:
   ```
   git clone https://github.com/IhorYu/FoodOnline.git
   cd FoodOnline
   ```
2. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```
3. **Setup Database**:
   - Configure your database settings in `FoodOnline_main/settings.py`.
4. **Run Migrations**:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Run the Application**:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application via the browser at `localhost:8000`.
- Register as a customer or vendor.
- Explore food menus, add items to the cart, and proceed to checkout.

## Technologies Used
- Django Framework
- PostgreSQL (with PostGIS for geospatial data)
- JavaScript, HTML, CSS for frontend
- PayPal API for payment processing

## Contributing
Contributions to the FoodOnline project are welcome. Please feel free to fork the repository, make changes, and submit pull requests.
