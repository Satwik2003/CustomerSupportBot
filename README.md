# Combined Rasa and Django Project
This project integrates a Rasa chatbot with a Django web application.

## Prerequisites
Before you begin, ensure you have the following installed on your machine:
- Python (3.6 or later)
- pip (Python package installer)
- Rasa
- Django
- Git

## Setup Instructions
1. Clone Both Repositories

Clone the repositories for the Django project and the Rasa chatbot.

```bash
git clone <URL to django_rasa_project repo>
git clone <URL to CustomerSupportBot repo>
```

2. Project Structure

After cloning, you will have two main directories:
```console
->django_rasa_project
->CustomerSupportBot (main repo)
```

3. Place Projects Separately

Move both cloned repositories to your desktop or any other preferred location.

4. Open Projects in VSCode
   
Open both django_rasa_project and CustomerSupportBot in separate instances of VSCode.

5. Open Terminals/Command Prompt
   
Open two terminals or command prompts:

<ul>
    <li> One for django_rasa_project </li>
    <li> One for CustomerSupportBot </li>
</ul>

6. Setup and Run Django Project

**Terminal 1:**
    
a. Navigate to the chatbot_project folder in django_rasa_project:

```console
cd path\to\django_rasa_project\chatbot_project
```

b. Apply database migrations:
```console
python manage.py migrate
```

c. Start the Django development server:
```console    
python manage.py runserver
```
You should see output like this:
```console
Starting development server at http://127.0.0.1:8000/
```

7. Setup and Run Rasa Chatbot
   
**Terminal 2:**

a. Navigate to the CustomerSupportBot directory:
```console
cd path\to\CustomerSupportBot
```

b. Train the Rasa model:
```console
rasa train
```

c. Start the Rasa server:
```console
rasa run
```
You should see output like this:
```console
root - Rasa server is up and running.
```

8. Access the Application
Open your web browser and navigate to:
<ul>
    <li>http://127.0.0.1:8000/chatbot/</li>
    <li>http://127.0.0.1:8000/</li>
</ul>

You should now see the integrated Django application with the Rasa chatbot.

And we're good to go!


