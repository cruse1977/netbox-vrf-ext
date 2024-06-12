# Generated by Django 5.0.6 on 2024-05-18 22:08

import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dcim', '0187_alter_device_vc_position'),
        ('extras', '0115_convert_dashboard_widgets'),
        ('ipam', '0069_gfk_indexes'),
        ('tenancy', '0015_contactassignment_rename_content_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='VRFInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('rd', models.CharField(blank=True, max_length=21, null=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='dcim.device')),
                ('export_targets', models.ManyToManyField(blank=True, related_name='instance_exporting_vrfs', to='ipam.routetarget')),
                ('import_targets', models.ManyToManyField(blank=True, related_name='instance_importing_vrfs', to='ipam.routetarget')),
                ('loopback_interface', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_related', to='dcim.interface')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tenants', to='tenancy.tenant')),
                ('vrf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to='ipam.vrf')),
            ],
            options={
                'verbose_name': 'VRF Instance',
                'verbose_name_plural': 'VRF Instances',
                'unique_together': {('vrf', 'device')},
            },
        ),
    ]