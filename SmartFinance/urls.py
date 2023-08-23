from django.urls import path
from .views import *

urlpatterns = [
    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = 'delete'),
# ----------------------------------------------------------------------
    path('elements/', elements, name = 'elements'),
    path('base/', base, name = 'base'),
# ----------------------------------------------------------------------
   # ----------------------------------------------------------------------
    path('about/', about, name = 'ABOUT'),
    path('contact/', contact, name = 'CONTACT'),
    path('', index, name = 'INDEX'),
    path('innerpage/', innerpage, name = 'INNERPAGE'),
    path('portfolio/', portfolio, name = 'PORTFOLIO'),
    path('portfoliodetails/', portfoliodetails, name = 'PORTFOLIODETAILS'),
    path('pricing/', pricing, name = 'PRICING'),
    path('services/', services, name = 'SERVICES'),
    path('faq/', faq, name = 'FAQ'),
    path('team/', team, name = 'TEAM'),
    path('testimonials/', testimonials, name = 'TESTIMONIALS'),
    path('signup/', signup, name = 'SIGNUP'),
    path('login/', login, name = 'LOGIN'),
    path('logout/', userLogOut, name = 'LOGOUT'),
# ----------------------------------------------------------------------
    path('add_category/', add_category, name = 'add_category'),
    path('allexpense/', ALL_EXPENSE, name = 'ALL_EXPENSE'),
# ----------------------------------------------------------------------
    path('add_expense/', add_expense, name = 'add_expense'),

# ----------------------------------------------------------------------
]