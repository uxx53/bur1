from django.conf.urls import patterns, include, url
from django.contrib import admin
#from profiles import views
import profiles.views
#from django.views import generic

urlpatterns = patterns(
    '',

    url(r'^$', profiles.views.SignInAndSignUp.as_view(template_name='home.html'),
        name='home'),
    url(r'^about/$', profiles.views.AboutView.as_view(),
        name='about'),
    url(r'^accounts/logout$', profiles.views.LogoutView.as_view(),
        name='logout'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^debugtest/$', profiles.views.DebugTestView.as_view()),
)
