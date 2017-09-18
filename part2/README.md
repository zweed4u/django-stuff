# Part 2  
With our first app in our project and with its simple view and urlconf  
we took to setting up the database.  
We learned about migrations and their typical workflow (modify model, make migrations and then migrate)  
Speaking of models we learned that they are essentially the databases layout with other metadata.  
We wrote our first model and 'activated' it via mysite settings such as in the database setup.  
We made our first migrations: `python3 manage.py makemigrations polls` and  
saw the file associated.
We even went as far as to check what sql commands would be run for that migration:  
`python3 manage.py sqlmigrate polls 0001`  
We then finally migrated which created the model tables in the database.

We then messed around in the interactive shell `python3 manage.py shell`
This was just as simple as invoking python/idle from the command line but  
provided easy access to our environment as well as the database api. 
It was crucial in the shell to always `django.setup()` after import.  
In the shell we set questions for our app and associated pub_date and saved them.  
We saw that the display was unhelpful so we made changes accordingly in our model providing a __str__ method  

Still in the model we added our own custom method to determine if a question was  
published recently. (within a day)
We took back to the shell and tested createion, enumeration, filtering and deletion.  

After playing in the shell we created a superuser `python manage.py createsuperuser`  
with credentials to view the admin page.  
Running the dev server and then navigating to 127.0.0.1/admin provided us with  
a login screen which our newly created admin user could login into and see the site administration page.  

In polls.admin we registered Question from the model so that it would have an admin  
interface and be modifiable by the admin.
We wrapped up by getting acclimated to the site administration page.
