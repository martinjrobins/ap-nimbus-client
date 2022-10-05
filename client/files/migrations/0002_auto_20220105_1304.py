# Generated by Django 3.2.10 on 2022-01-05 13:04
import os

from django.contrib.auth.hashers import make_password
from django.db import migrations


PREDEF_ION_CURRENTS = [
    {'name': 'IKr',
     'alternative_name': 'herg',
     'metadata_tags': 'membrane_rapid_delayed_rectifier_potassium_current_conductance, membrane_rapid_delayed_rectifier_potassium_current_conductance_scaling_factor',
     'channel_protein': 'K_v 11.1 ',
     'gene': 'hERG or KCNH2',
     'description': 'Rapid delayed rectifier potassium current',
     'default_hill_coefficient': 1,
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.18},

    {'name': 'INa',
     'metadata_tags': 'membrane_fast_sodium_current_conductance, membrane_fast_sodium_current_conductance_scaling_factor',
     'channel_protein': 'Na_v 1.5',
     'gene': 'SCN5A',
     'description': 'Fast sodium current',
     'default_hill_coefficient': 1,
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.2},

    {'name': 'ICaL',
     'metadata_tags': 'membrane_L_type_calcium_current_conductance, membrane_L_type_calcium_current_conductance_scaling_factor',
     'channel_protein': 'Ca_v 1.2',
     'gene': 'CACNA1C',
     'description': 'Long-lasting (L-type) calcium current',
     'default_hill_coefficient': 1,
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.15},

    {'name': 'IKs',
     'metadata_tags': 'membrane_slow_delayed_rectifier_potassium_current_conductance, membrane_slow_delayed_rectifier_potassium_current_conductance_scaling_factor',
     'channel_protein': 'K_v 7.1',
     'gene': 'KCNQ1/minK',
     'description': 'Slow delayed rectifier potassium current',
     'default_hill_coefficient': 1,
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.17},

    {'name': 'IK1',
     'metadata_tags': 'membrane_inward_rectifier_potassium_current_conductance, membrane_inward_rectifier_potassium_current_conductance_scaling_factor',
     'channel_protein': 'K_ir 2.1',
     'gene': 'KCNJ2',
     'description': 'Inward rectifier potassium current',
     'default_hill_coefficient': 1,
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.18},

    {'name': 'Ito',
     'metadata_tags': 'membrane_fast_transient_outward_current_conductance, membrane_fast_transient_outward_current_conductance_scaling_factor, membrane_transient_outward_current_conductance, membrane_transient_outward_current_conductance_scaling_factor',
     'channel_protein': 'K_v 4.3',
     'gene': 'KCND3',
     'description': '(Fast) transient outward potassium current',
     'default_hill_coefficient': 1,
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.15},

    {'name': 'INaL',
     'metadata_tags': 'membrane_persistent_sodium_current_conductance, membrane_persistent_sodium_current_conductance_scaling_factor',
     'default_hill_coefficient': 1,
     'gene': 'SCN5A',
     'description': 'Late/Persistent sodium current',
     'channel_protein': 'Na_v 1.5',
     'default_saturation_level': 0,
     'default_spread_of_uncertainty': 0.2},
]

PREDEF_MODELS = [
    {'name': r'Shannon et al.',
     'year': 2004,
     'description': r'rabbit ventricular cell model',
     'cellml_link': r'https://models.cellml.org/exposure/d72a36fe0b7e121068c96bcb1ff6044a/shannon_wang_puglisi_weber_bers_2004_a.cellml/view',
     'paper_link': r'https://www.ncbi.nlm.nih.gov/pubmed/15347581',
     'ap_predict_model_call': r'1'},

    {'name': 'TenTusscher et al.',
     'year': 2006,
     'description': 'human ventricular cell model (epicardial)',
     'cellml_link': 'https://models.cellml.org/exposure/a7179d94365ff0c9c0e6eb7c6a787d3d/ten_tusscher_model_2006_IK1Ko_epi_units.cellml/view',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/16565318',
     'ap_predict_model_call': '2'},

    {'name': 'Mahajan et al.',
     'year': 2008,
     'description': 'rabbit ventricular cell model',
     'cellml_link': 'https://models.cellml.org/exposure/a5586b72d07ce03fc40fc98ee846d7a5/mahajan_shiferaw_sato_baher_olcese_xie_yang_chen_restrepo_karma_garfinkel_qu_weiss_2008.cellml/view',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/18160660',
     'ap_predict_model_call': '3'},

    {'name': 'Hund, Rudy',
     'year': 2004,
     'description': 'canine ventricular cell model',
     'cellml_link': 'https://models.cellml.org/exposure/f4b7120aa512c7f5e7a0664abcee3e8b/view',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/15505083',
     'ap_predict_model_call': '4'},

    {'name': 'Grandi et al.',
     'year': 2010,
     'description': 'human ventricular cell model (epicardial)',
     'cellml_link': 'https://models.cellml.org/e/96/grandi_pasqualini_bers_2010.cellml/view',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/19835882',
     'ap_predict_model_call': '5'},

    {'name': r"O'Hara et al.",
     'year': 2011,
     'description': 'human ventricular cell model (endocardial)',
     'cellml_link': 'https://models.cellml.org/e/71',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/21637795',
     'ap_predict_model_call': '6'},

    {'name': 'Paci et al.',
     'year': 2013,
     'description': 'ventricular-like stem-cell derived myocyte model',
     'cellml_link': 'https://models.cellml.org/e/16d',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/23722932',
     'ap_predict_model_call': '7'},

    {'name': r"O'Hara-Rudy",
     'version': 'CiPA-v1.0',
     'year': 2017,
     'description': 'human ventricular cell model (endocardial)',
     'cellml_link': 'https://models.cellml.org/e/4e8/',
     'paper_link': 'https://www.ncbi.nlm.nih.gov/pubmed/28878692',
     'ap_predict_model_call': '8'},
]

PREDEF_MODEL_ION_CURRENTS = [
    {'model_name': r'Shannon et al.', 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito']},
    {'model_name': 'TenTusscher et al.', 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito']},
    {'model_name': 'Mahajan et al.', 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito']},
    {'model_name': 'Hund, Rudy', 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito']},
    {'model_name': 'Grandi et al.', 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito']},
    {'model_name': r"O'Hara et al.", 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito', 'INaL']},
    {'model_name': 'Paci et al.', 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito']},
    {'model_name': r"O'Hara-Rudy", 'ion_currents':['IKr', 'INa', 'ICaL', 'IKs', 'IK1', 'Ito', 'INaL']},
]


def create_admin(apps, schema_editor):
    # We can't import the model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    User = apps.get_model('accounts', 'User')
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    full_name = os.environ.get('DJANGO_SUPERUSER_USERNAME', email)
    institution = os.environ.get('DJANGO_SUPERUSER_INSTITUTION', 'unknown')
    password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
    User.objects.create(
            email=email,
            full_name=full_name,
            institution=institution,
            password=make_password(password),
            is_superuser=True,
            is_staff=True,
            is_active=True,
    )


def create_predefined_currents(apps, schema_editor):
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    User = apps.get_model('accounts', 'User')
    IonCurrent = apps.get_model('files', 'IonCurrent')
    user = User.objects.get(email=email)
    for predef_current in PREDEF_ION_CURRENTS:
        IonCurrent.objects.create(author=user, **predef_current)


def create_predefined_models(apps, schema_editor):
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    User = apps.get_model('accounts', 'User')
    CellmlModel = apps.get_model('files', 'CellmlModel')
    user = User.objects.get(email=email)
    for predef_model in PREDEF_MODELS:
        CellmlModel.objects.create(author=user, predefined=True, **predef_model)


def link_model_current(apps, schema_editor):
    email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
    User = apps.get_model('accounts', 'User')
    CellmlModel = apps.get_model('files', 'CellmlModel')
    IonCurrent = apps.get_model('files', 'IonCurrent')
    for model in PREDEF_MODEL_ION_CURRENTS:
        cellml_model = CellmlModel.objects.get(name=model['model_name'])
        for current in model['ion_currents']:
            ion_current = IonCurrent.objects.get(name=current)
            cellml_model.ion_currents.add(ion_current)
        cellml_model.save()


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin),
        migrations.RunPython(create_predefined_currents),
        migrations.RunPython(create_predefined_models),
        migrations.RunPython(link_model_current),
    ]
