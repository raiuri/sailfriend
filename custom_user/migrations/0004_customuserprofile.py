# Generated by Django 5.1.1 on 2024-10-11 02:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0003_alter_customuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birth_date', models.DateField()),
                ('nationality', models.CharField(choices=[('afghan', 'Afghan'), ('albanian', 'Albanian'), ('algerian', 'Algerian'), ('american', 'American'), ('andorran', 'Andorran'), ('angolan', 'Angolan'), ('antiguan', 'Antiguan'), ('argentine', 'Argentine'), ('armenian', 'Armenian'), ('australian', 'Australian'), ('austrian', 'Austrian'), ('azerbaijani', 'Azerbaijani'), ('bahamian', 'Bahamian'), ('bahraini', 'Bahraini'), ('bangladeshi', 'Bangladeshi'), ('barbadian', 'Barbadian'), ('belarusian', 'Belarusian'), ('belgian', 'Belgian'), ('belizean', 'Belizean'), ('beninese', 'Beninese'), ('bhutanese', 'Bhutanese'), ('bolivian', 'Bolivian'), ('bosnian', 'Bosnian'), ('botswanan', 'Botswanan'), ('brazilian', 'Brazilian'), ('british', 'British'), ('bruneian', 'Bruneian'), ('bulgarian', 'Bulgarian'), ('burkinabe', 'Burkinabe'), ('burmese', 'Burmese'), ('burundian', 'Burundian'), ('cambodian', 'Cambodian'), ('cameroonian', 'Cameroonian'), ('canadian', 'Canadian'), ('cape_verdean', 'Cape Verdean'), ('central_african', 'Central African'), ('chadian', 'Chadian'), ('chilean', 'Chilean'), ('chinese', 'Chinese'), ('colombian', 'Colombian'), ('comoran', 'Comoran'), ('congolese', 'Congolese'), ('costa_rican', 'Costa Rican'), ('croatian', 'Croatian'), ('cuban', 'Cuban'), ('cypriot', 'Cypriot'), ('czech', 'Czech'), ('danish', 'Danish'), ('djiboutian', 'Djiboutian'), ('dominican', 'Dominican'), ('dutch', 'Dutch'), ('east_timorese', 'East Timorese'), ('ecuadorean', 'Ecuadorean'), ('egyptian', 'Egyptian'), ('emirati', 'Emirati'), ('equatorial_guinean', 'Equatorial Guinean'), ('eritrean', 'Eritrean'), ('estonian', 'Estonian'), ('ethiopian', 'Ethiopian'), ('fijian', 'Fijian'), ('finnish', 'Finnish'), ('french', 'French'), ('gabonese', 'Gabonese'), ('gambian', 'Gambian'), ('georgian', 'Georgian'), ('german', 'German'), ('ghanaian', 'Ghanaian'), ('greek', 'Greek'), ('grenadian', 'Grenadian'), ('guatemalan', 'Guatemalan'), ('guinean', 'Guinean'), ('guyanese', 'Guyanese'), ('haitian', 'Haitian'), ('honduran', 'Honduran'), ('hungarian', 'Hungarian'), ('icelandic', 'Icelandic'), ('indian', 'Indian'), ('indonesian', 'Indonesian'), ('iranian', 'Iranian'), ('iraqi', 'Iraqi'), ('irish', 'Irish'), ('israeli', 'Israeli'), ('italian', 'Italian'), ('ivoirian', 'Ivoirian'), ('jamaican', 'Jamaican'), ('japanese', 'Japanese'), ('jordanian', 'Jordanian'), ('kazakh', 'Kazakh'), ('kenyan', 'Kenyan'), ('korean', 'Korean'), ('kuwaiti', 'Kuwaiti'), ('kyrgyz', 'Kyrgyz'), ('lao', 'Lao'), ('latvian', 'Latvian'), ('lebanese', 'Lebanese'), ('liberian', 'Liberian'), ('libyan', 'Libyan'), ('lithuanian', 'Lithuanian'), ('luxembourgish', 'Luxembourgish'), ('macedonian', 'Macedonian'), ('malagasy', 'Malagasy'), ('malawian', 'Malawian'), ('malaysian', 'Malaysian'), ('malian', 'Malian'), ('maltese', 'Maltese'), ('mauritanian', 'Mauritanian'), ('mauritian', 'Mauritian'), ('mexican', 'Mexican'), ('moldovan', 'Moldovan'), ('monacan', 'Monacan'), ('mongolian', 'Mongolian'), ('montenegrin', 'Montenegrin'), ('moroccan', 'Moroccan'), ('mozambican', 'Mozambican'), ('namibian', 'Namibian'), ('nepalese', 'Nepalese'), ('new_zealander', 'New Zealander'), ('nicaraguan', 'Nicaraguan'), ('nigerian', 'Nigerian'), ('norwegian', 'Norwegian'), ('omani', 'Omani'), ('pakistani', 'Pakistani'), ('panamanian', 'Panamanian'), ('paraguayan', 'Paraguayan'), ('peruvian', 'Peruvian'), ('philippine', 'Philippine'), ('polish', 'Polish'), ('portuguese', 'Portuguese'), ('qatari', 'Qatari'), ('romanian', 'Romanian'), ('russian', 'Russian'), ('rwandan', 'Rwandan'), ('saudi', 'Saudi'), ('scottish', 'Scottish'), ('senegalese', 'Senegalese'), ('serbian', 'Serbian'), ('singaporean', 'Singaporean'), ('slovak', 'Slovak'), ('slovenian', 'Slovenian'), ('somali', 'Somali'), ('south_african', 'South African'), ('spanish', 'Spanish'), ('sri_lankan', 'Sri Lankan'), ('sudanese', 'Sudanese'), ('surinamese', 'Surinamese'), ('swazi', 'Swazi'), ('swedish', 'Swedish'), ('swiss', 'Swiss'), ('syrian', 'Syrian'), ('taiwanese', 'Taiwanese'), ('tajik', 'Tajik'), ('tanzanian', 'Tanzanian'), ('thai', 'Thai'), ('togolese', 'Togolese'), ('trinidadian', 'Trinidadian'), ('tunisian', 'Tunisian'), ('turkish', 'Turkish'), ('turkmen', 'Turkmen'), ('ugandan', 'Ugandan'), ('ukrainian', 'Ukrainian'), ('uruguayan', 'Uruguayan'), ('uzbek', 'Uzbek'), ('venezuelan', 'Venezuelan'), ('vietnamese', 'Vietnamese'), ('welsh', 'Welsh'), ('yemeni', 'Yemeni'), ('zambian', 'Zambian'), ('zimbabwean', 'Zimbabwean')], max_length=20)),
                ('surname', models.CharField(max_length=100)),
                ('languages_spoken', models.JSONField(default=list)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
