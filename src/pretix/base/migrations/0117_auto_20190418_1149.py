# Generated by Django 2.2 on 2019-04-18 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0116_auto_20190402_0722'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemvariation',
            name='original_price',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='If set, this will be displayed next to '
                                                                              'the current price to show that the '
                                                                              'current price is a discounted one. '
                                                                              'This is just a cosmetic setting and '
                                                                              'will not actually impact pricing.',
                                      max_digits=7, null=True, verbose_name='Original price'),
        ),
    ]