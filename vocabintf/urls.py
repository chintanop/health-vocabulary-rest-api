from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('',

    #Code Resource View
    url(r'^code/(?P<vocab>.+)/(?P<code_val>.+)/$', 'umls.views.code_resource_view'),

    #Relationship Resource View
    url(r'^rel/(?P<vocab>.+)/(?P<code_val>.+)/(?P<rel_type>.+)/$', 'umls.views.rel_resource_view'),

    #Mapping Resource View
    url(r'^map/(?P<source_vocab>.+)/(?P<code_val>.+)/(?P<target_vocab>.+)/$', 'umls.views.map_resource_view'),

    url(r'^demo', TemplateView.as_view(template_name="demo.html")),

    #Concept Resource View
    url(r'^concept/(?P<cui>.+)/$', 'umls.views.concept_resource_view'),
)