#!/bin/bash
echo Starting Flask example app.
cd /var/www/html/firstapp/
gunicorn -w 2 -b 127.0.0.1:5000 firstapp:app
