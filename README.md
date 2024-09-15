# E-Commerce Web Application

## Overview

This is a Flask-based e-commerce web application that allows users to browse products, add items to their cart, and complete purchases using Stripe for payment processing. The application includes user authentication, a shopping cart system, and a simple product catalog.

## Features

- User registration and authentication
- Product browsing and search
- Shopping cart functionality
- Secure checkout process using Stripe
- Responsive design for mobile and desktop use

## Technologies Used

- Python 3.8+
- Flask 2.0+
- SQLAlchemy
- Flask-Login for user session management
- Stripe API for payment processing
- Bootstrap 5 for frontend styling

## Installation

1. Clone the repository:
git clone https://github.com/ylawrenceemenike/ecommerce-app.git
cd ecommerce-app

2. Create a virtual environment and activate it:
python -m venv env
source env/bin/activate # On Windows use env\Scripts\activate

3. Install the required packages:
pip install -r requirements.txt


4. Set up environment variables:
- Create a `.env` file in the project root
- Add the following variables:
  ```
  FLASK_APP=app.py
  FLASK_ENV=development
  SECRET_KEY=your_secret_key
  STRIPE_SECRET_KEY=your_stripe_secret_key
  STRIPE_PUBLISHABLE_KEY=your_stripe_publishable_key
  ```

5. Initialize the database:
   flask db upgrade


## Running the Application

1. Start the Flask development server:
   flask run


2. Open a web browser and navigate to `http://localhost:5000`

## Testing

To run the test suite: pytest


## Deployment

This application can be deployed on various platforms such as Heroku, AWS, or DigitalOcean. Make sure to set the appropriate environment variables and configure the database for production use.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
