# Generated by Django 3.1.2 on 2022-02-02 11:55

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email_verified', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Binding_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Binding_Name', models.CharField(max_length=100)),
                ('Author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_image', models.URLField()),
                ('Isbn10', models.CharField(max_length=15)),
                ('Isbn13', models.CharField(max_length=15)),
                ('Book_Title', models.CharField(max_length=100, unique=True)),
                ('Book_subtitle', models.CharField(blank=True, max_length=30, null=True)),
                ('Publication_year', models.DateField()),
                ('Language', models.CharField(max_length=100)),
                ('No_Of_Copies_Actual', models.IntegerField()),
                ('No_Of_Copies_Current', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('no_pages', models.IntegerField(blank=True, null=True)),
                ('version', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('Binding_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.binding_details')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shelf_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shelf_Id', models.CharField(max_length=100)),
                ('Floor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.IntegerField()),
                ('User_Name', models.CharField(max_length=100)),
                ('Is_Admin', models.CharField(max_length=100)),
                ('Designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='student_detaiels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_image', models.ImageField(default='media\\student\\default\\profile.png', upload_to='student/')),
                ('Student_Usn', models.CharField(default='ABC4567890', max_length=100)),
                ('Sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M', max_length=2)),
                ('Date_Of_Birth', models.DateField(blank=True, null=True)),
                ('Department', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact_Number', models.CharField(blank=True, default='0123456789', max_length=100, null=True)),
                ('fine', models.IntegerField(default=0)),
                ('College_Name', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.college')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Borrower_ID', models.IntegerField()),
                ('Borrowed_From_Date', models.DateTimeField()),
                ('Borrowed_To_Date', models.DateTimeField()),
                ('Actual_Return_date', models.DateTimeField()),
                ('Book_ID', models.ManyToManyField(to='app.Book_Details')),
                ('Issued_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.staff_details')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.student_detaiels')),
            ],
        ),
        migrations.AddField(
            model_name='book_details',
            name='Category_Type',
            field=models.ManyToManyField(to='app.Category_Details'),
        ),
        migrations.CreateModel(
            name='Authe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_token', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
