from api import create_app
import os

app_env = os.environ.get('APP_ENV', 'development')

app = create_app(app_env)

if __name__ == '__main__':
    PORT = os.environ.get('PORT', 8100)
    app.run(host="0.0.0.0", port=PORT)
