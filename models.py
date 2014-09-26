from django.db import models
import re
import ARClient.helpers


# Create your models here.
class Type(models.Model):

    class Meta:

        ordering = ['-id']
        verbose_name = 'Device type'
        verbose_name_plural = 'Device types'

    id = models.AutoField(max_length=15, primary_key=True)
    name = models.CharField(max_length=45, verbose_name='Type handle')
    desc = models.CharField(max_length=750, verbose_name='Type description')
    has_wifi = models.BooleanField(default=True, verbose_name='WiFI enabled?')
    icon_url = models.URLField(max_length=650)
    can_rec_files = models.NullBooleanField(default=False)
    default_port = models.IntegerField(default=None, null=True)
    gcm = models.BooleanField(default=False)

    def __str__(self):
        return self.desc


class Device(models.Model):

    class Meta:

        ordering = ['-id']
        verbose_name = 'AutoRemote Device'

    id = models.AutoField(max_length=15, primary_key=True, verbose_name='Device ID')
    name = models.CharField(max_length=250, verbose_name='Device Name')
    type = models.ForeignKey(Type)
    LANip = models.GenericIPAddressField(protocol='IPv4', verbose_name='Device LAN IP')
    pubip = models.CharField(max_length=375, verbose_name='Device public IP or hostname', blank=True)
    port = models.IntegerField(max_length=5, verbose_name='Device port to use for connections', default='1818')
    ttl = models.IntegerField(max_length=15, verbose_name='Message TTL',default=0)
    gcm_key = models.CharField(max_length=4096, verbose_name='Device GCM key (if available)', blank=True)

    def save(self, *args, **kwargs):
        ex = re.compile(r'goo.gl')
        if ex.search(self.gcm_key) != None:
            self.gcm_key = ARClient.helpers.get_gcm_key(self.gcm_key)
        super(Device, self).save(*args, **kwargs)

    def __str__(self):
        return self.name