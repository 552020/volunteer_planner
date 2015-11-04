# coding: utf-8

from django.conf.urls import url

from .views import HelpDesk, PlannerView

urlpatterns = [
    url(r'^$', HelpDesk.as_view(), name="helpdesk"),

    url(
        r'^facility/(?P<pk>\d+)/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/?(#(?P<shift_id>\d+))?$',
        PlannerView.as_view(),
        name="planner_by_facility"),

]
