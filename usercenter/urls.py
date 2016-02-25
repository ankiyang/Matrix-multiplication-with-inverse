from django.conf.urls import url

urlpatterns=[
    url(r'^register$',"usercenter.views.register",name="usercenter_register"),
    url(r'^logout',"django.contrib.auth.views.logout_then_login",name="logout_then_login"),
    url(r'^activate/(?P<code>\w+)$',"usercenter.views.activate",name="usercenter_activate"),
]