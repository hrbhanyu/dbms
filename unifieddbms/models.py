from django.db import models

# Create your models here.
class host_info(models.Model):
    server_id = models.AutoField(primary_key=True)
    server_name = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50)
    remote_port = models.IntegerField()
    os_type = models.CharField(max_length=100)
    db_type = models.CharField(max_length=50)
    region = models.CharField(max_length=200)
    def __unicode__(self):
        return self.server_name
    class Meta:
        app_label = 'unifieddbms'


class database_info(models.Model):
    instance_id = models.AutoField(primary_key=True)
    instance_name = models.CharField(max_length=200)
    db_port = models.IntegerField()
    db_version = models.CharField(max_length=200)
    db_edition = models.CharField(max_length=200)
    server_id = models.ForeignKey(host_info,on_delete=models.CASCADE)
    def __unicode__(self):
        return self.instance_name
    class Meta:
        app_label = 'unifieddbms'