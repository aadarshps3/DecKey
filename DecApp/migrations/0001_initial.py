# Generated by Django 5.1.3 on 2024-11-19 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_number', models.IntegerField()),
                ('Date', models.DateField()),
                ('Party', models.CharField(max_length=255)),
                ('Reference', models.CharField(max_length=255)),
                ('Work', models.CharField(max_length=255)),
                ('Details', models.CharField(max_length=255)),
                ('Assign_to', models.CharField(max_length=255)),
                ('Status', models.CharField(choices=[('Completed', 'Completed'), ('Incompleted', 'Incompleted'), ('Pending', 'Pending')], max_length=255)),
                ('Finished_date', models.DateField()),
                ('Delivery_Date', models.CharField(max_length=255)),
                ('Bill_Amount', models.CharField(max_length=255)),
                ('Fee_amount', models.CharField(max_length=255)),
                ('DOR', models.CharField(max_length=255)),
            ],
        ),
    ]