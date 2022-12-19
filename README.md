https://www.food-online.shop/

<!-- HTML Documentation for FoodOnline -->
<h1>FoodOnline</h1>
<p>FoodOnline is a website that allows users to search for and order food from local restaurants. Restaurant owners can also register and create a profile for their business, including their menu and operating hours. Once approved, the restaurant's information will be displayed in the search results for users to browse and order from.</p>
<h2>Features</h2>
<ul>
  <li>Search for restaurants by keyword or city</li>
  <li>View restaurant menus and operating hours</li>
  <li>Order and pay for food online through PayPal</li>
  <li>Restaurant owners can create and manage their own profiles and menus</li>
</ul>
<h2>Registration</h2>
<p>Users and restaurant owners can both register for an account on FoodOnline. To register as a restaurant owner, click on the "ORegister Restaurant" button on the homepage and fill out the required information. Your restaurant will be reviewed by the FoodOnline team before it is added to the search results.</p>
<h2>Search</h2>
<p>To search for restaurants, simply enter a keyword or city into the search bar on the homepage and click "Search". You will be taken to a page with a list of restaurants that match your search criteria, along with their menus and operating hours. Click on a restaurant's name to view more information and place an order.</p>
<h2>Ordering and Payment</h2>
<p>To place an order, simply add items to your cart and proceed to checkout. You will be prompted to enter your delivery information and select a payment method. FoodOnline currently accepts payment through PayPal. Once your payment has been processed, your order will be placed and the restaurant will begin preparing it for delivery or pickup (depending on the restaurant's offerings).</p>

<h1>Install Django application</h1>
<p>
In order to set up the application on your local machine, you will need to follow these steps:
</p>
<ol>
  <li>Make sure you have Python 3 and pip installed on your system. You can check if you have these tools by running the following commands in your terminal:</li>
  <pre>python3 --version
  pip3 --version</pre>
  <li>Clone the repository to your local machine:</li>
  <pre>git clone https://github.com/IhorYu/FoodOnline.git</pre>
  <li>Navigate to the project directory:</li>
  <pre>cd FoodOnline</pre>
  <li>Create a virtual environment and activate it:</li>
  <pre>python3 -m venv env
  source env/bin/activate</pre>
  <li>Install the required dependencies:</li>
  <pre>pip3 install -r requirements.txt</pre>
  <li>Rename the .env-sample file to .env and fill in the necessary environment variables</li>
  <li>Run the migrations to set up the database:</li>
  <pre>python3 manage.py migrate</pre>
  <li>Start the development server:</li>
  <pre>python3 manage.py runserver</pre>
  <li>You should now be able to access the application at http://localhost:8000 in your web browser.</li>
</ol>
<p>
  That's it! You should now have the FoodOnline application running on your local machine. If you have any issues or questions while setting up the project, feel free to open an issue in the repository or reach out to the maintainer.
</p>
