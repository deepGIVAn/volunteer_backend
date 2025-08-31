gunicorn --reload --workers 1 --bind 0.0.0.0:8000 volunteer_project.wsgi:application

sudo lsof -i:8000

sudo kill -9 PID PID

NODE_OPTIONS="--max-old-space-size=1024" npm run build

pm2 ls

pm2 restart frontend