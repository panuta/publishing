from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'presentation.views.views',

    url(r'^$', 'view_homepage', name='view_homepage'),
)

urlpatterns += patterns(
    'presentation.views.user_views',

    url(r'^profile/id/(?P<user_uid>\w+)/$', 'view_user_profile_by_id', name='view_user_profile_by_id'),
    url(r'^profile/(?P<url_name>\w+)/$', 'view_user_profile_by_url_name', name='view_user_profile_by_url_name'),
    url(r'^my/profile/$', 'view_my_profile', name='view_my_profile'),
)

urlpatterns += patterns(
    'presentation.views.user_writeroom_views',

    url(r'^my/writeroom/$', 'view_user_writeroom', name='view_user_writeroom'),
    url(r'^my/writeroom/writing/$', 'start_new_writing', name='start_new_writing'),
)

urlpatterns += patterns(
    'presentation.views.user_messages_views',

    url(r'^my/messages/$', 'view_user_messages', name='view_user_messages'),
)

urlpatterns += patterns(
    'presentation.views.user_balance_views',

    url(r'^my/balance/$', 'view_user_balance', name='view_user_balance'),
)

urlpatterns += patterns(
    'presentation.views.user_settings_views',

    url(r'^my/settings/profile/$', 'view_user_settings_profile', name='view_user_settings_profile'),
    url(r'^my/settings/account/$', 'view_user_settings_account', name='view_user_settings_account'),
)