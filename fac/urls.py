from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset, password_reset_done, logout,login
app_name='fac'

urlpatterns=[
    url(r'^$', views.index, name='index'),
    url(r'^login/$',login,{'template_name':'fac/login.html'}, name='login'),
    url(r'^logout/$',logout,{'template_name':'fac/logout.html'}, name='logout'),
    url(r'home/(?P<username>\w+)/$',views.home,name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^Biosciences and Bioengineering/$', views.bsbe, name='bsbe'),
    url(r'^Chemical Engineering/$', views.ce, name='ce'),
    url(r'^Chemistry/$', views.ch, name='ch'),
    url(r'^Civil Engineering/$', views.civ, name='civ'),
    url(r'^Computer Science & Engineering/$', views.comp, name='comp'),
    url(r'^Design/$', views.des, name='des'),
    url(r'^Electronics & Electrical Engineering/$', views.ee, name='ee'),
    url(r'^Mathematics/$', views.math, name='math'),
    url(r'^Mechanical Engineering/$', views.mech, name='mech'),
    url(r'^Physics/$', views.ph, name='ph'),
    url(r'^profile/$',views.view_profile,name='view_profile'),
    url(r'^profile/edit/$',views.edit_user_page,name='edit_user_page'),
    url(r'^edit_user/$',views.edit_user),
    url(r'^profile/edit1/$', views.edit_user1_page, name='edit_user1_page'),
    url(r'^edit_user1/$', views.edit_user1),
    url(r'^profile/edit2/$', views.edit_user2_page, name='edit_user2_page'),
    url(r'^edit_user2/$', views.edit_user2),




    url(r'^profile/edit6/$', views.edit_user6_page, name='edit_user6_page'),
    url(r'^edit_user6/$', views.edit_user6),
    url(r'^edit5/(?P<username>\w+)/$', views.edit_user5_page, name='edit_user5_page'),
    url(r'^edit_user5/(?P<username>\w+)/$', views.edit_user5),
    url(r'^profile/edit3/$', views.edit_user3_page, name='edit_user3_page'),
    url(r'^edit_user3/$', views.edit_user3),
    url(r'^profile/edit4/$', views.edit_user4_page, name='edit_user4_page'),
    url(r'^edit_user4/$', views.edit_user4),
    url(r'^tr/(?P<username>\w+)/$',views.tr,name='tr'),

    url(r'^profile/change-password/$', views.change_password, name='change_password'),

    url(r'^password_reset/$', auth_views.password_reset,{'template_name':'fac/reset_pass.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done,{'template_name':'fac/reset_done.html'},name='password_reset_done'),
    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/complete/$', auth_views.password_reset_complete, {'template_name': 'fac/reset_password.html'},name='password_reset_complete')
]
