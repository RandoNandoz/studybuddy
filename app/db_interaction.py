from task.Task import Task

import firebase_admin
import firebase_admin.db

from firebase_admin import credentials

cred = credentials.Certificate('app/vshacks-project-firebase-adminsdk-guz81-a5d561efbc.json')
firebase_admin.initialize_app(cred)