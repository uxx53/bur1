from django.conf.urls import patterns, include, url
from django.contrib import admin
from profiles.views import SignInAndSignUp, LogoutView, AboutView
from chapter04 import views

urlpatterns = patterns(
    '',
 #   url(r'^$', SignInAndSignUp.as_view(template_name='home.html'),name='home'),
    url(r'^about/$', AboutView.as_view(),name='about'),
    url(r'^accounts/logout$', LogoutView.as_view(),name='logout'),
    url(r'^admin/', include(admin.site.urls)),

    # Chapter 4 URLs
    # ----------------------
    url(r'^hello-fn/(?P<name>\w+)/$', views.hello_fn),
    url(r'^hello-fn/$', views.hello_fn),

    url(r'^hello-cl/(?P<name>\w+)/$', views.HelloView.as_view()),
    url(r'^hello-cl/$', views.HelloView.as_view()),

    url(r'^hello-su/(?P<name>\w+)/$', views.SuperVillainView.as_view()),
    url(r'^hello-su/$', views.SuperVillainView.as_view()),

    url(r'^myfeed/$', views.MyFeed.as_view(), name='home'),
    url(r'^public/$', views.PublicPostJSONView.as_view()),
    url(r'^list/$', views.AutorList.as_view(), name='list_notes'),
    url(r'^create/$', views.AutorCreate.as_view(), name='create_note'),
    url(r'^edit/(?P<pk>\d+)/$', views.AutorEdit.as_view(), name='edit_note'),
    url(r'^delete/(?P<pk>\d+)/$',views.AutorDelete.as_view(), name='delete_note'),

)
