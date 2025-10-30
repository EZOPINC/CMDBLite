from django.db import models

class Application(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Server(models.Model):
    hostname = models.CharField(max_length=100, unique=True)
    ip_address = models.GenericIPAddressField()
    os = models.CharField(max_length=50)
    environment = models.CharField(max_length=50, choices=[
        ('DEV', 'Development'),
        ('TEST', 'Testing'),
        ('PROD', 'Production'),
    ])
    applications = models.ManyToManyField(Application, related_name="servers")

    def __str__(self):
        return self.hostname


class Database(models.Model):
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    host = models.ForeignKey(Server, on_delete=models.CASCADE)
    applications = models.ManyToManyField(Application, related_name="databases")

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    depends_on = models.ManyToManyField('self', blank=True, symmetrical=False)
    applications = models.ManyToManyField(Application, related_name="services")

    def __str__(self):
        return self.name
