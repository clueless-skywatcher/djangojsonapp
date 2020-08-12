# djangojsonapp
A Django RESTful API that shows the activity periods of registered users.

The database is already populated with dummy data. The final JSON output can be found at
https://djangojsonapp.herokuapp.com/users/.

The API endpoint for the app is located at https://djangojsonapp.herokuapp.com/userapi/.

How it was done:
- Made a "djsonapi" app that houses all the REST API logic.
- Defined the User and ActivityPeriod models and made the required migrations.
  - ActivityPeriod has a ForeignKey named user to User with an on-delete cascade constraint.
  - User id is a CharField with a primary key constraint.
- Defined the serializers for parsing to JSON.
  - ActivityPeriodSerializer serializes the ActivityPeriod model, and formats the start_time and end_time.
  - UserSerializer serializes the User model. The activity_periods is given by the ActivityPeriodSerializer.
- Made the required views.
  - Defined a UserViewSet that is attached to the API router. This contains a queryset that sorts the users'
  ids alphabetically. It also takes in the UserSerializer.
  - The show_json() view makes a GET request (using the requests module) to the API endpoint, and generates
  a pretty-printed JSON from the requested data, and passes it to the "users/" route.
- Made a custom management command called "populatejson" that populates the database with dummy users and their
activity periods. The command deletes any existing records in all the tables and repopulates them.
- Registered all models in the admins page.
- Deployed the app using Gunicorn WSGI server on Heroku.
- Added an environment variable "HEROKU_APP_NAME" to reference the name of the app wherever "localhost" is referenced.
- Ran the prepopulate command in the heroku bash shell.

Libraries used (other than Django):
- djangorestframework (for making the serializers and API router)
- requests (for making the GET request to API)
- json (for displaying a pretty-printed JSON object to the webpage)
- os (for referencing the environment variable)
