# Generated by Django 3.2.13 on 2024-01-16 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_payplan_pay_plan_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payplan',
            name='pay_plan_id',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='pay_plan',
        ),
        migrations.AlterField(
            model_name='user',
            name='pay_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='shortener.payplan'),
        ),
    ]
