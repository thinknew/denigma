from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required

from models import Measurement, Intervention, Factor, Strain, Assay, Regimen, Epistasis, Manipulation
from views import InterventionList, InterventionCreate, InterventionUpdate #, InterventionDelete
from views import FactorList, CreateFactor, FactorDetail, FactorDelete#, FactorCreate, FactorUpdate
from views import CreateStrain, UpdateStrain
from views import ManipulationDetail


from data.views import Delete


urlpatterns = patterns('lifespan.views',
    url(r'^$', 'index', name='lifespan'),

    # Studies:
    url(r'^studies/$', 'studies', name='studies'),
    url(r'^study/(?P<pk>\d+)', 'study'),
    url(r'^studies/add', 'add_studies', name='add_studies'),
    url(r'^study/edit/(?P<pk>\d+)', 'edit_study'),
    url(r'^study/delete/(?P<pk>\d+)', 'delete_study'),
    url(r'^studies/archive/$', 'studies_archive', name='studies_archive'),

    # Experiments:
    url(r'^experiments/$', 'experiments', name='experiments'),
    url(r'^experiment/(?P<pk>\d+)', 'experiment',),
    url(r'^experiment/add/(?P<pk>\d*)', 'add_experiment', name='add_experiment'),
    url(r'^experiment/edit/(?P<pk>\d+)', 'edit_experiment'),
    url(r'^experiment/delete/(?P<pk>\d+)', 'delete_experiment'),

    # Measurements:
    #url(r'^measurements/$', 'measurements', name='measurements'),
    url(r'^measurements/$',
        ListView.as_view(queryset=Measurement.objects.all(),
            template_name='lifespan/measurements.html'), name='measurements'),
    url(r'^measurement/(?P<pk>\d+)',
        DetailView.as_view(model=Measurement,
            template_name='lifespan/measurement.html')),

    # Comparisions:
    url(r'^comparisons/$', 'comparisons', name='comparisons'),
    url(r'^comparison/(?P<pk>\d+)', 'comparison'),
    url(r'^comparison/add', 'add_comparison', name='add_comparison'),
    url(r'^comparison/edit/(?P<pk>\d+)', 'edit_comparison'),

    # Interventions:
    url(r'^interventions/$', InterventionList.as_view(),
        name='interventions'),
    url(r'^interventions/list/$', ListView.as_view( # Depricated.
        queryset=Intervention.objects.all(),
        template_name='lifespan/interventions.html',
        context_object_name='interventions'),
        name='interventions_list'),
    url(r'interventions/archive$', 'interventions', name='interventions_archive'),
    url(r'^intervention/(?P<pk>\d+)', DetailView.as_view(model=Intervention,
        template_name='lifespan/intervention.html'), name='intervention'),
    url(r'^intervention/add', 'add_intervention', name='add_intervention'),
    url(r'^intervention/edit/(?P<pk>\d+)', 'edit_intervention'),
    url(r'^intervention/create/$', InterventionCreate.as_view(),
        name='create_intervention'), #
    url(r'^intervention/update/(?P<pk>\d+)',
        login_required(InterventionUpdate.as_view()),
        name='update_intervention'), #
    url(r'^intervention/delete/(?P<pk>\d+)', 'delete_intervention'), #alias remove
#    url(r'^intervention/delete/(?P<pk>\d+)',
#         login_required(InterventionDelete.as_view())),
    url(r'^interventions/link/$', 'link_interventions', name='link_interventions'),

    # Factors:
    url(r'^factors/$', FactorList.as_view(), name='factors'),
    url(r'^factors/archive/$', ListView.as_view(queryset=Factor.objects.all(),
        template_name='lifespan/factors_archive.html', context_object_name='factors'),
        name='factors_archive'),
    url(r'^factor/(?P<pk>\d+)/$', FactorDetail.as_view(), name='factor'),
    url(r'^factor/add/$', 'add_factor', name='add_factor'),
    url(r'^factor/edit/(?P<pk>\d+)/$', 'edit_factor'),
    url(r'^factor/remove/(?P<pk>\d+)/$', 'remove_factor', name='remove_factor'),
    url(r'^factor/delete/(?P<pk>\d+)/$', FactorDelete.as_view(), name='delete-factor'),
    url(r'^factor/create/$', CreateFactor.as_view(), name='create-factor'),
    url(r'^factor/(?P<slug>.+)/$', FactorDetail.as_view(), name='factor'),

    # Strains;
    url(r'^strains/$', ListView.as_view(queryset=Strain.objects.all(),
        template_name='lifespan/strains.html', context_object_name="strains" ),
        name='strains'),
    url(r'^strain/(?P<pk>\d+)', DetailView.as_view(model=Strain,
        template_name='lifespan/strain.html')),
    url(r'^strain/create/$',CreateStrain.as_view(), name='create-strain'),
    url(r'^strain/update/(?P<pk>\d+)', login_required(UpdateStrain.as_view()), name='update-strain'),

    # Assays:
    url(r'^assays/$', ListView.as_view(queryset=Assay.objects.all(),
        template_name='lifespan/assays.html', context_object_name="assays"),
        name='assays'),
    url(r'^assay/(?P<pk>\d+)', DetailView.as_view(model=Assay,
        template_name='lifespan/assay.html')),

    # Others:
    url(r'^epistases/$', ListView.as_view(queryset=Epistasis.objects.all(),
        template_name='lifespan/epistases.html', context_object_name='epistases'),
        name='epistases'),
    url(r'^epistasis', 'epistasis', name='epistasis'),

    url(r'^regimens/$', ListView.as_view(queryset=Regimen.objects.all(),
        template_name='lifespan/regimens.html', context_object_name='regimens'),
        name='regimen'),
    url(r'^regimen/(?P<pk>\d+)', 'regimen', name='regimen'),
    url(r'^manipulations/$', ListView.as_view(queryset=Manipulation.objects.all(),
        template_name='lifespan/manipulations.html',
        context_object_name='manipulations'),
        name='manipulations'),
    url(r'^manipulation/(?P<pk>\d+)/$', ManipulationDetail.as_view(), name='manipulation'),
    url(r'^manipulation/(?P<slug>.+)/$', ManipulationDetail.as_view(), name='manipulaiton'),
    url(r'^type/$', 'type'),

    # Depricated:
    url(r'^genage/describe', 'describe'),
    url(r'^genage/functional_description', 'functional_description'),
    url(r'^integrity', 'integrity', name='integrity'),
    url(r'^(?P<table>\w+)/replace/(?P<field>\w+)/(?P<term>.+)/(?P<by>.+)/$', 'replace'),
    url(r'^gendr/dump', 'dump'),
    url(r'^map/species/(?P<model>.+)', 'map_species', name='map_species'),
    url(r'^correct/$', 'correct_classes', name='correct_classes'),
)
##234567891123456789212345678931234567894123456789512345678961234567897123456789