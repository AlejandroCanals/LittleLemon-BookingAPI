# Exercise Summary from Meta Back-end Course: Configure a Little Lemon Reservations API

The main objective of this exercise focuses on setting up an API to manage reservations in a MySQL database using Django. Users can make reservations through a form on the website, and the data is stored and presented in JSON format.

1. **Initial Setup**: A basic Django environment is provided in a ZIP file. This includes initial files and configurations needed to start the project and application.

2. **Virtual Environment Activation**: `pipenv` is used to activate a virtual environment that isolates the project's dependencies.

3. **MySQL Database Configuration**: It is assumed that MySQL is installed locally and an administration user has been configured. The necessary migrations are carried out to configure the database.

4. **Reservation Form**: A model form called `BookingForm` is created which is based on the reservation model `Booking`.

5. **Views and URLs**: Views and URLs are configured for booking management and integrated into the existing website.

6. **Forms Processing**: The information from the forms is processed and stored in the MySQL database.

7. **Output in JSON Format**: The reservation data is converted into JSON objects and returned as a response for display on the web page.


![png](https://github.com/iTzSRK/LittleLemon-BookingAPI/raw/main/images/1.PNG)
![png](https://github.com/iTzSRK/LittleLemon-BookingAPI/raw/main/images/2.png)

## Additional
- I have learned how to use gitignore to not upload sensitive files.
- I have also learned how to hide SQL keys when sharing projects on Github using python-decouple, a library that facilitates the management of configurations in environment variables.


## Used technology
- HTML
- CSS
- Python
- Django
- MySQL
- Javacript


# Little Lemon Booking API Setup

This repository contains the setup and instructions for creating a basic booking API using Django. The objective of this exercise is to set up an API endpoint to send form data to a MySQL database and return a JSON object to be displayed on a web page.

## Quick Start

Follow the steps below to set up the project:

### Prerequisites

- Ensure you have MySQL installed on your local machine and have set up the admin user.
- You will need Python and pipenv installed.

### Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/iTzSRK/LittleLemon-BookingAPI.git
```

2. Navigate to the project directory:

```bash
cd LittleLemon-BookingAPI
```

3. Activate the virtual environment using pipenv:

```bash
pipenv shell
```

4. Install the required dependencies:

```bash
pipenv install django
pipenv install mysqlclient
```

### Database Setup

Before proceeding with migrations, make sure you have created the correct MySQL user, assigned privileges, and configured the database.

Create a .env file and fill it in with the credentials of your local database.

```dotenv
DEBUG=True
DB_NAME=reservations
DB_USER=    
DB_PASSWORD=
DB_HOST=127.0.0.1
DB_PORT=3306
```

Run the necessary commands to ensure the user can access the database.

### Run Migrations

Run the following commands to perform database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server

Start the development server by running:

```bash
python manage.py runserver
```

## Usage

- Access the Little Lemon website and navigate to the "Book" tab to make reservations.
- View the reservations on the "Bookings" page.

## Folder Structure

- `littlelemon` - The main project folder.
  - `restaurant` - The app containing the booking functionality.
    - `forms.py` - Contains the `BookingForm` class for form processing.
    - `models.py` - Defines the `Booking` model.
    - `views.py` - Contains view functions for the website.
    - `urls.py` - App-level URL configuration.
  - `templates` - Contains HTML templates for rendering pages.
  - `settings.py` - Project settings.
  - `urls.py` - Project-level URL configuration.
```

Make sure to customize the details and paths of your project in these instructions. Once you've added this section to your README.md on GitHub, users should be able to follow these steps to download, set up, and start your project.

