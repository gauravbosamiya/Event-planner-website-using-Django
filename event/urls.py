from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),

    path('account/login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_user, name='logout'),

    path('event-category/', views.event_category, name='event-category'),
    path('category-wise-events-list/<int:pk>/', views.category_wise_events_list, name='category-wise-events-list'),

    # path('user/<int:pk>/', views.user_profile, name='user'),

    path('event/<int:pk>/', views.event_page, name='event'),
    path('event-confirmation/<int:pk>/', views.event_confirmation, name='event-confirmation'),
    path('generate-ticket/<int:pk>/', views.generate_ticket, name='generate-ticket'),

    path('account/', views.account_page, name='account'),

    path('upcoming-event/', views.upcoming_event, name='upcoming-event'),
    path('past-events/', views.past_event, name='past-events'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_page, name='contact'),
    path('event/suggestion/<int:event_id>/', views.event_suggestion, name='event_suggestion'),

    # organizers

    # path('organizers-signup', views.organizers_signup, name='organizers-signup'),
    # path('organizers-login', views.organizers_login, name='organizers-login'),


    # Admin
    path('admin-login', views.admin_login, name='admin-login'),
    path('admin-home', views.admin_home, name='admin-home'),
    path('all-events', views.all_events, name='all-events'),
    path('add-event/', views.add_event, name='admin-event'),

    path('delete-event/<int:pk>/', views.delete_event, name='delete-event'),
    path('update-event/<int:pk>/', views.update_event, name='update-event'),
    path('add-event-category/', views.add_event_category, name='add-event-category'),
    path('admin-upcoming-event/', views.admin_upcoming_event, name='admin-upcoming-event'),
    path('delete-upcoming-event/<int:pk>/', views.delete_upcoming_event, name='delete-upcoming-event'),
    path('admin-past-event/', views.admin_past_event, name='admin-past-event'),
    path('delete-past-event/<int:pk>/', views.delete_past_event, name='delete-past-event'),
    path('all-users/', views.all_users, name='all-users'),
    path('delete-user/<int:pk>/', views.delete_user, name='delete-user'),
    path('user-logout/', views.admin_logout, name='admin-logout'),
    path('new-index/', views.new_index, name='new-index')



]


