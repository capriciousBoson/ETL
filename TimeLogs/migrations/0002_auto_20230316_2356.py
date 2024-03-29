# Generated by Django 4.1.7 on 2023-03-16 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimeLogs', '0001_initial'),
    ]

    def update_data(apps, scema_editor):
        TimeLogs = apps.get_model('TimeLogs', 'TimeLogs')
        for obj in TimeLogs.objects.all():
            if obj.booking_codes == '':
                obj.booking_codes = None
                obj.save()
                
    operations = [
        migrations.RunPython(update_data),
    ]
