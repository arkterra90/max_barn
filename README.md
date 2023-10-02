# Max_Barn CRM Documentation

## Project Description

Max_Barn is a personal project implemented with Django to create a web application that assists a barn building business in managing new customer contacts and initiating the sales process. It streamlines the handling of inquiries, facilitates initial contact with customers, and provides a centralized dashboard for employees to track customer interactions and project details. Max_Barn also utilizes JavaScript to enhance the front-end user experience, making it a valuable tool for the Maxwell Barn Company.

## Overview

Max_Barn is a web-based Customer Relationship Management (CRM) system designed to facilitate the management of customer interactions for the Maxwell Barn Company. This project streamlines the process of handling customer inquiries, initial contact, site visits, and tracking customer details.

## Distinctiveness and Complexity

1. **Front-End Efficiency**: Max_Barn prioritizes user experience by incorporating JavaScript for dynamic div toggling in the front-end. This approach enhances page loading speed compared to a traditional Django-driven template rendering method.

2. **Dynamic Contact Form**: When users request a quote or visit the contact page, they encounter a dynamic contact form. This form is fully powered by Django and is based on the Customer Model. It utilizes choices to simplify the selection of specific details related to customer inquiries.

3. **Admin Dashboard**:

   - Once a contact form is submitted, the customer's information is stored in the "First Contacts" section of the admin dashboard. This dashboard is accessible to authorized employees through a link at the bottom of the customer-facing website. Note that the admin dashboard is restricted to logged-in users.

   - Employees can initiate first contact with customers and record essential details using the associated form.

   - During site visits, employees can use the building input form to take detailed notes related to the building process.

   - Employees can access the existing customer list on the admin dashboard at any time and add notes to customer profiles for better customer detail tracking.

4. **Data Models**:

   - Max_Barn utilizes the following models to support its functionality:

     - `User`: Represents employees.
     - `Customer`: Stores information from the contact input form.
     - `CustomerNote`: Records notes entered by employees.
     - `Contact`: Tracks initial contact between employees and customers.
     - `Building`: Stores specifications and details of building projects.
     - `BuildingNote`: Records additional notes associated with building projects.
     - `Payment`: Manages payment records for building projects.

5. **JavaScript Integration**:

   - JavaScript plays a pivotal role in enhancing the customer-facing experience by improving page navigation speed. The associated java file for this can be found in static/images/index.js.

   - Upon submission of a contact form, a user-friendly alert message is displayed to inform customers that their submission has been successfully received.

## Installation and Getting Started

Follow these steps to install Django and get the Max_Barn CRM project up and running on your development server:

### Prerequisites

Before you begin, make sure you have the following prerequisites installed on your system:

- **Python**: Django is a Python web framework, so ensure you have Python installed. You can download it from [Python's official website](https://www.python.org/downloads/).

### 1. Clone the Repository

First, clone the Max_Barn CRM project repository from GitHub to your local machine:

```bash
git clone https://github.com/your-username/max_barn.git
```

Replace `your-username` with your GitHub username.

### 2. Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to isolate project dependencies. Navigate to the project directory and create a virtual environment:

```bash
cd max_barn
python -m venv venv
```

Activate the virtual environment:

- **On Windows**:

```bash
venv\Scripts\activate
```

- **On macOS and Linux**:

```bash
source venv/bin/activate
```

### 3. Install Django and Dependencies

Install Django and the project's dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

By default, Max_Barn uses SQLite as its database for development purposes. You can configure the database settings in the `max_barn/settings.py` file. Update the `DATABASES` section as needed, including setting the database name, user, and password.

### 5. Apply Migrations

Apply the initial database migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### 6. Create an Admin User

You'll need an admin user to access the admin dashboard. Create one by running:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin user credentials.

### 7. Run the Development Server

Now, you can start the Django development server:

```bash
python manage.py runserver
```

The development server will run, and you can access the Max_Barn CRM by opening your web browser and navigating to `http://127.0.0.1:8000/`.

### 8. Access the Admin Dashboard

To access the admin dashboard, go to `http://127.0.0.1:8000/admin/` in your web browser. Log in with the admin credentials you created earlier to manage customer data and interact with the CRM.

You're now ready to start using the Max_Barn CRM for managing customer interactions and building projects on your local development server.