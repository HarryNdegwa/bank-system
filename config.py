 

DATABASE_URI='postgres+psycopg2://postgres:harry1998@localhost:5432/bank_db'

 # DB_URI='postgres+psycopg2://postgres:harry1998@localhost:5432/alchemy_db'


 # CELERY STUFF
BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Nairobi'
