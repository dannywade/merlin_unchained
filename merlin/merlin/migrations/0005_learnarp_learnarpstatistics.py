# Generated by Django 3.2.6 on 2021-09-14 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merlin', '0004_learnacl'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearnARP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyats_alias', models.TextField()),
                ('os', models.TextField()),
                ('interface', models.TextField()),
                ('neighbor_ip', models.TextField()),
                ('neighbor_mac', models.TextField()),
                ('origin', models.TextField()),
                ('local_proxy', models.TextField()),
                ('proxy', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LearnARPstatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyats_alias', models.TextField()),
                ('os', models.TextField()),
                ('entries_total', models.TextField()),
                ('in_drops', models.TextField()),
                ('in_replies_pkts', models.TextField()),
                ('in_requests_pkts', models.TextField()),
                ('incomplete_total', models.TextField()),
                ('out_replies_pkts', models.TextField()),
                ('out_requests_pkts', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]