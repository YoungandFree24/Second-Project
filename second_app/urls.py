#these are the routes for my app, like in flask

# we must import path here
from django.urls import path

# we must import our views file from soup/views.py
from . import views

# Now we can attach each route to the specfified route in our views.py
urlpatterns = [
    # path('',views.index),
    # path('another_route', views.another_route),
    # path('redirected_route', views.redirected_method),
    path('', views.root)
#     path('blogs', views.index),
#     path('blogs/new', views.new),
#     path('blogs/create', views.create),
#     path('blogs/12',views.show),
#     path('blogs/12/edit', views.edit),
#     path('blogs/12/delete', views.destroy)
]

# '' means by default and it is implied / which is different from flask
#  '' = '/' in flask