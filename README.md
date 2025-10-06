# SpeakFree

**SpeakFree** is an advanced blogging platform designed to offer users a seamless experience in creating, managing, and interacting with content. Visitors can explore posts freely, while registered users enjoy a full suite of interactive features.

## Features

- Visitors can browse available posts.  
- Users can sign up and log in to the platform.  
- Profile creation and management is fully supported.  
- Users can create, view, edit, and delete their own posts.  
- Detailed view for each specific post is available.  
- Commenting and liking functionality is implemented on all posts.  
- Secure logout option for users.  

## Installation

Follow the steps below to set up SpeakFree locally:

### 1. Clone the Repository
Clone the project repository to your local machine:

```bash
git clone <repository_url>
cd SpeakFree

pip install pipenv    # install pipenv if not already installed
pipenv shell       # create and activate virtual environment
python3 -m venv venv   # create virtual environment
source venv/bin/activate   # activate virtual environment (Linux/macOS)
venv\Scripts\activate    # activate virtual environment (Windows)

pip install -r requirements.txt
python manage.py createsuperuser 

python manage.py runserver
````




