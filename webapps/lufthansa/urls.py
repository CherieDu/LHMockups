from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'lufthansa.views.registration_low', name='registration_low'),
    url(r'^registration_low', 'lufthansa.views.registration_low', name='registration_low'),
    url(r'^registration_medium', 'lufthansa.views.registration_medium', name='registration_medium'),
    url(r'^registration_high', 'lufthansa.views.registration_high', name='registration_high'),
    url(r'^registration_mixed', 'lufthansa.views.registration_mixed', name='registration_mixed'),
    url(r'^preference_panel', 'lufthansa.views.preference_panel', name='preference_panel'),

)