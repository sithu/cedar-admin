"""Start up script"""

from app import views
from app import app, admin

# Create admin
admin = admin.Admin(app, 
    'Popular Plastic', 
    index_view=views.AdminIndexView())
#admin.add_view(BlankView(name='Blank', url='blank', endpoint='blank'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
