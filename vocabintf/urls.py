from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

urlpatterns = patterns('',

                       # Code Resource View
                       url(r'^code/(?P<vocab>.+)/(?P<code_val>.+)/$',
                           'umls.views.code_resource_view'),

                       # Relationship Resource View
                       url(r'^rel/(?P<vocab>.+)/(?P<code_val>.+)/(?P<rel_type>.+)/$',
                           'umls.views.rel_resource_view'),

                       # Mapping Resource View
                       url(r'^map/(?P<source_vocab>.+)/(?P<code_val>.+)/(?P<target_vocab>.+)/$',
                           'umls.views.map_resource_view'),

                       # Concept Children View
                       url(r'^concepts/(?P<cui>.+)/children$',
                           'umls.views.concept_child_resource_view'),

                       # Concept Parent View
                       url(r'^concepts/(?P<cui>.+)/parents$',
                           'umls.views.concept_par_resource_view'),

                       # Concept Parent View
                       url(r'^concepts/(?P<cui>.+)/synonyms$',
                           'umls.views.concept_synonyms_resource_view'),

                       # Concept Resource View
                       url(r'^concepts/(?P<cui>.+)$',
                           'umls.views.concept_resource_view'),

                       # Concept Term
                       #url(r'^concepts/(?P<cui>.+)/synonym/(?P<sab>.+)/$', '
                       #umls.views.concept_synonym_resource_view'),
                       url(r'^concepts$',
                           'umls.views.concept_term_resource_view'),

                       url(r'^concepts_bulk$',
                           'umls.views.concepts_bulk_resource_view'),

                       # Bulk Concepts Parent View
                       url(r'^concepts_bulk/(?P<cui_list>.+)/parents$',
                           'umls.views.concepts_bulk_par_resource_view'),

                       # Codes Resource View
                       url(r'^codes$', 'umls.views.code_res_view'),

                       # Codes Resource View
                       url(r'^codes/(?P<code>.+)/sab/(?P<sab>.+)/$',
                           'umls.views.code_det_view'),

                       url(r'^demo',
                           TemplateView.as_view(template_name="demo.html")),
                       )
