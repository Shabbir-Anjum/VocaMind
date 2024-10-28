# Generated by Django 5.1.1 on 2024-10-10 12:52

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Behaviour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_greeting', models.CharField(max_length=250)),
                ('agent_prompt', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=25)),
                ('language', models.CharField(choices=[('english', 'English'), ('spanish', 'Spanish'), ('french', 'French'), ('german', 'German')], default='english', max_length=7)),
                ('voice', models.CharField(choices=[('adam', 'Adam'), ('alice', 'Alice')], default='adam', max_length=5)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_llm', models.CharField(choices=[('gpt-4o-mini', 'GPT-4o mini'), ('gpt-4o', 'GPT-4o')], default='gpt-4o-mini', max_length=11)),
                ('custom_knowledge', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('behaviour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='console.behaviour')),
                ('identity', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='console.identity')),
                ('knowledge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='console.knowledge')),
            ],
        ),
        migrations.CreateModel(
            name='KnowledgeFileItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_item', models.FileField(blank=True, null=True, upload_to='files/')),
                ('status_url', models.CharField(choices=[('Indexed', 'Index'), ('Active', 'Active'), ('Errored', 'Error')], default='Indexed', max_length=7)),
                ('knowledge', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='console.knowledge')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='console.agent')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='console.customer')),
            ],
        ),
    ]