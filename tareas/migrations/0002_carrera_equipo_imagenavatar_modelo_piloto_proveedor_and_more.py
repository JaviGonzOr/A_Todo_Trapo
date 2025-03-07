# Generated by Django 4.1.3 on 2025-02-21 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('circuito', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenAvatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.FileField(upload_to='Chimeneas')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coche', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('puntos', models.IntegerField(default=0)),
                ('carreras_disputadas', models.IntegerField(default=0)),
                ('victorias', models.IntegerField(default=0)),
                ('v_rapida', models.IntegerField(default=0)),
                ('podios', models.IntegerField(default=0)),
                ('avatar', models.ImageField(null=True, upload_to='Chimeneas/')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pilotos', to='tareas.equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuito', models.CharField(max_length=100)),
                ('ficha_tecnica', models.FileField(null=True, upload_to='Chimeneas')),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('puntos', models.IntegerField()),
                ('Vuelta_Rapida', models.IntegerField(default=0)),
                ('miniatura', models.ImageField(null=True, upload_to='Chimeneas/')),
                ('foto_circuito', models.ImageField(null=True, upload_to='Chimeneas/')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='tareas.carrera')),
                ('piloto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados', to='tareas.piloto')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('video_file', models.FileField(upload_to='videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visitas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('visita', models.DateTimeField(blank=True, null=True)),
                ('ubicacion', models.URLField(blank=True, null=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='imagentarea',
            name='tarea',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='ficha_tecnica',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='importante',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='material',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='modelo',
        ),
        migrations.RemoveField(
            model_name='tarea',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='imagentarea',
            name='carrera',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archivos', to='tareas.tarea'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='configuracion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='imagentarea',
            name='imagen',
            field=models.FileField(upload_to='Chimeneas'),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
        migrations.AddField(
            model_name='imagenavatar',
            name='karrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archivo', to='tareas.piloto'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='circuito',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.proveedor'),
        ),
        migrations.AddField(
            model_name='tarea',
            name='coche',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tareas.modelo'),
        ),
    ]
