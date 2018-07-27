# django-react attempt 2

## how to setup dev environment
1. clone down this git repo
1. create a virtual environment with the following packages
- django
- djangorestframework
- django-webpack-loader
1. make sure you are in the virtual environment while developing on this app
1. if you haven't yet, run makemigrations and migrate models for the api app
1. for the front end react cd into the 'frontend' directory
1. run npm install to get dependecies for the react project
1. run npm start in the frontend directory and make sure the react server is running on port 3000
1. cd into root directory and run the django server on port 8000
1. going to the root url of localhost:8000 should display the react app
1. going to routes such as /api or /admin should load the correct django apps

# How to set up a new project of your own

## project setup
1. create virtual environment and install django into it
1. create django project
1. cd into django project directory and run migrations
1. run django server to confirm django app is running correctly

## react setup
1. from project root directory
1. run npx create-react-app
1. at this point add reacts gitingore directories and files to the root repos gitignore if applicable
1. run npm start from react app directory to confirm react was installed correctly
1. run 'npm run eject' so that further configuration can happen

## integrating react with django
1. while still in your virtual environment run pip install django-webpack-loader
1. add 'webpack_loader' into djangos installed apps and also add the following code
```
WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json'),
        }
}
```
```
TEMPLATES = [
    {
        # ... other settings
        'DIRS': [os.path.join(BASE_DIR, "templates"), ],
        # ... other settings
    },
]
```
1. create a directory in your project root folder name templates, create an index.html and add the following code
```
{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Ponynote</title>
  </head>
  <body>
    <div id="root">
    </div>
      {% render_bundle 'main' %}
  </body>
</html>
```
1. in your django project folders urls.py add the following code
```
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', TemplateView.as_view(template_name="index.html")),
]
```
1. cd back into the react apps root directory and run npm install webpack-bundle-tracker --save-dev
1. in the webpack config/paths.js file add this code
```
module.exports = {
  // ... other values
  statsRoot: resolveApp('../'),
}
```
1. in config/webpack.config.dev.js change the urls like so
```
const publicPath = 'http://localhost:3000/';
const publicUrl = 'http://localhost:3000/';
```
1. in the same file add the following code, replacing webpackHotDevClient
```
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: [
    // ... KEEP OTHER VALUES
    // this will be found near line 30 of the file
    require.resolve('webpack-dev-server/client') + '?http://localhost:3000',
    require.resolve('webpack/hot/dev-server'),
    // require.resolve('react-dev-utils/webpackHotDevClient'),
  ],
  plugins: [
    // this will be found near line 215-220 of the file.
    // ... other plugins
    new BundleTracker({path: paths.statsRoot, filename: 'webpack-stats.dev.json'}),
  ],
}
```
1. in config/webpackDevServer.config.js add
```
headers: {
  'Access-Control-Allow-Origin': '*'
},
```
