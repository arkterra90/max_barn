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

   - JavaScript plays a pivotal role in enhancing the customer-facing experience by improving page navigation speed.

   - Upon submission of a contact form, a user-friendly alert message is displayed to inform customers that their submission has been successfully received.

