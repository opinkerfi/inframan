from django.db import models
import hpilo
# Create your models here.

class IloHost(models.Model):
    host_name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    serial_number = models.CharField(max_length=100, null=True, blank=True)
    product_name = models.CharField(max_length=100, null=True, blank=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    raw_host_data = models.CharField(max_length=1000000000, null=True, blank=True)
    def __unicode__(self):
        return self.host_name

    def update(self):
        """ Connect to actual ilo instance and update our own metadata """
        ilo = self.get_ilo()
        host_data = ilo.get_host_data()
        self.raw_host_data = str(host_data)
        # Iterate through every line in the host data. Populate fields as needed
        for line in host_data:
            line_type = line.get('type')
            if line_type == 209:
                # Network interfaces have type 209
                network_interfaces = line
            elif line_type == 1:
                # Basic information
                self.product_name = line.get('Product Name')
                self.serial_number = line.get('Serial Number')
            elif line_type == 17:
                # Memory modules
                pass
        self.save()

    def get_ilo(self):
        """ Get an instance of hpilo.Ilo() that represents this host.

         Example Usage:
           model_ilo = IloHost(hostname='x', login='administrator', password='x')
           actual_ilo = model_ilo.get_ilo()
           actual_ilo.get_host_data()

        """
        ilo = hpilo.Ilo(hostname=self.address, login=self.username, password=self.password)
        return ilo
