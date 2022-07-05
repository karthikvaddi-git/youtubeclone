
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_thumbnail', models.ImageField(upload_to='thumbnails')),
                ('video_title', models.CharField(max_length=255)),
                ('video_desc', models.TextField()),
                ('video', models.FileField(upload_to='videos')),
            ],
        ),
    ]