from django.urls import path


from . import views


app_name = 'expenses'

urlpatterns = [

path('', views.expenses_view_list, name='expenses_list'),
path('<int:expense_id>/', views.expenses_detail, name = 'expenses_detail'),
path('create/', views.expenses_create, name='expenses_create' ),
path('update/<int:expense_id>/', views.expenses_update, name='expenses_update'),
path('delete/<int:expense_id>/', views.expenses_delete, name='expenses_delete'),
path('feedback/', views.contact, name='expenses_feedback'),


]



# app_name = 'accounts'
# urlpatterns = [

# path('login/', login_view, name = 'login'),

# path('logout/', logout_view, name = 'logout'),

# path('login/', login_view, name = 'register'),

# path('login/', login_view, name = 'login'),

# path('login/', login_view, name = 'login'),


# ]