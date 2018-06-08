#!/bin/bash

python manage.py migrate
python manage.py loaddata kegtypes
python manage.py loaddata beertypes
