from django.conf.urls import patterns, include, url

urlpatterns = patterns('presentation.views.views',
    url(r'^$', 'view_homepage', name='view_homepage'),
)

urlpatterns += patterns('presentation.views.user_views',
    url(r'^writeroom/$', 'view_my_writeroom', name='view_my_writeroom'),

    url(r'^profile/id/(?P<user_uid>\w+)/$', 'view_user_profile_by_id', name='view_user_profile_by_id'),
    url(r'^profile/(?P<url_name>\w+)/$', 'view_user_profile_by_url_name', name='view_user_profile_by_url_name'),

    url(r'^my/profile/$', 'view_my_profile', name='view_my_profile'),
    url(r'^my/profile/edit/$', 'edit_my_profile', name='edit_my_profile'),
    url(r'^my/profile/account/$', 'edit_my_account', name='edit_my_account'),

)