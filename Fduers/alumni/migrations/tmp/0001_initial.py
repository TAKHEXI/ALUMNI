# Generated by Django 3.2.5 on 2021-07-19 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DEFAULT', max_length=30, verbose_name='标题')),
                ('startTime', models.DateTimeField(verbose_name='开始时间')),
                ('endTime', models.DateTimeField(verbose_name='结束时间')),
                ('location', models.CharField(max_length=200, verbose_name='详细地点')),
                ('cost', models.PositiveIntegerField(verbose_name='费用')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='城市')),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='院系')),
            ],
            options={
                'verbose_name': '院系',
                'verbose_name_plural': '院系',
            },
        ),
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='行业')),
            ],
            options={
                'verbose_name': '行业',
                'verbose_name_plural': '行业',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='省份')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=3000)),
            ],
            options={
                'verbose_name': 'test',
                'verbose_name_plural': 'test',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='用户名')),
                ('mail', models.CharField(max_length=20, verbose_name='邮箱')),
                ('grade', models.IntegerField(verbose_name='届次')),
                ('studentID', models.CharField(max_length=20, verbose_name='学号')),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('referrer', models.CharField(max_length=30, verbose_name='推荐人')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('photo', models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='user_photo/%Y/%m/%d', verbose_name='头像')),
                ('essay', models.TextField(default='', max_length=30, verbose_name='个性签名')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.city', verbose_name='城市')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.department', verbose_name='院系')),
                ('industry', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.industry', verbose_name='行业')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Tie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('content', models.TextField(max_length=200, verbose_name='内容')),
                ('createdTime', models.DateTimeField(verbose_name='发布时间')),
                ('replyTime', models.DateTimeField(verbose_name='最新回复时间')),
                ('access', models.IntegerField(default=0, verbose_name='浏览量')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.user', verbose_name='作者')),
                ('relatedActivity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.activity', verbose_name='相关活动')),
                ('tag', models.ManyToManyField(to='alumni.Tag', verbose_name='所属标签')),
            ],
            options={
                'verbose_name': '帖子',
                'verbose_name_plural': '帖子',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('studentID', models.CharField(max_length=20, verbose_name='学号')),
                ('grade', models.IntegerField(verbose_name='界次')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.department', verbose_name='院系')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200, verbose_name='回复内容')),
                ('relatedTie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.tie', verbose_name='相关帖')),
            ],
            options={
                'verbose_name': '楼层',
                'verbose_name_plural': '楼层',
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='专业')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.department', verbose_name='所属院系')),
            ],
            options={
                'verbose_name': '专业',
                'verbose_name_plural': '专业',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(db_column='f', default='北京', on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.province'),
        ),
        migrations.AddField(
            model_name='activity',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='alumni.city', verbose_name='所在城市'),
        ),
    ]
