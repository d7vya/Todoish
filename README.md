

# Todoish

Todoish is a web application built with Django where you can assign daily tasks, create teams for collaborative task management, and join teams via unique links or team codes. It's designed to help users stay organized and work collaboratively on tasks with friends or colleagues.(Work in Progress)

## Features
- Create and manage personal tasks.
- Assign daily tasks to yourself or other team members.
- Create teams to collaborate on tasks with friends or colleagues.
- Join teams via invite links or team codes.
- Manage shared tasks within teams.
- Simple and intuitive user interface.

## Installation

### Prerequisites
Before you can set up Todoish, make sure you have the following installed on your system:

- Python 3.x
- Django 3.x or higher
- PostgreSQL (Optional for database; SQLite is used by default)

### Step 1: Install Python

1. Download and install Python from the official website:  
   [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Verify Python installation:
   ```bash
   python --version
   ```

   You should see something like:
   ```bash
   Python 3.x.x
   ```

### Step 2: Set up a Virtual Environment (Optional but recommended)

1. Navigate to your project directory and create a virtual environment:
   ```bash
   python -m venv todoish_env
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source todoish_env/bin/activate
     ```
   - On Windows:
     ```bash
     todoish_env\Scripts\activate
     ```

### Step 3: Install Dependencies

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/d7vya/Todoish.git
   ```

2. Navigate into the project directory:
   ```bash
   cd todoish
   ```

3. Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not available, you can manually install the dependencies with:
   ```bash
   pip install django
   pip install django-guardian
   ```

### Step 4: Set up the Database

By default, Todoish uses SQLite, but if you want to use PostgreSQL, follow these steps:

1. Install PostgreSQL (optional):
   ```bash
   sudo apt install postgresql postgresql-contrib
   ```

2. Configure the database settings in `todoish/settings.py`.

   For PostgreSQL, modify the `DATABASES` setting to look something like this:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'todoish_db',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### Step 5: Apply Migrations

1. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

### Step 6: Create a Superuser

To access the Django admin panel, you'll need a superuser account:

1. Create a superuser by running:
   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to enter a username, email, and password.

### Step 7: Run the Development Server

Start the development server:
```bash
python manage.py runserver
```

You can now access the application at:
```
http://127.0.0.1:8000/
```

### Step 8: Access the Admin Panel

To manage the application, go to the admin panel:
```
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials you created.

---

## Usage

### Creating Tasks
- Users can create daily tasks and assign them to themselves or others.
- Tasks can be marked as completed or pending.

### Creating Teams
- Users can create teams and invite others to join.
- Teams are identified by a unique invite link or team code.
- Shared tasks can be assigned within teams for collaborative task management.

### Joining Teams
- To join a team, users can use an invite link or input a team code.
- Once in a team, tasks can be assigned and managed collectively.

---

## Contributing

We welcome contributions to Todoish! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add feature'`).
5. Push to your fork (`git push origin feature-branch`).
6. Open a pull request.

---


If you have any issues or questions, feel free to open an issue on the repository!

--- 

