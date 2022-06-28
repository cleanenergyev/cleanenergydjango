from django.db import models

from users.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Drop(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    productcode = models.PositiveIntegerField(unique=True)
    mrp = models.PositiveIntegerField()
    gst = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=120, unique=True)
    accessoriescode = models.PositiveIntegerField(unique=True)
    mrp = models.PositiveIntegerField()
    gst = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Battery(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ChargerRating(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ToolkitStatus(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class RvmLhrh(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CertCard(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class PdiStatus(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class BatteryMake(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class BatteryConnectorType(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class BatteryType(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class BatteryCapacity(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class VehicleStock(models.Model):

    qrcode = models.CharField(max_length=120, unique=True)
    productcode = models.PositiveIntegerField()
    productdesc = models.CharField(max_length=120)
    vehicleinvoiceno = models.CharField(max_length=120)
    vehicleinvoicedatefromhe = models.DateField()
    exciseinvoiceno = models.CharField(max_length=120)
    battery = models.ForeignKey(Battery, on_delete=models.CASCADE)
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    vehiclechassisno = models.CharField(max_length=120, unique=True)
    motorno = models.CharField(max_length=120, unique=True)
    controllerno = models.CharField(max_length=120)
    chargerno = models.CharField(max_length=120)
    chargerrating = models.ForeignKey(ChargerRating, on_delete=models.CASCADE)
    ownersmanualno = models.CharField(max_length=120)
    heronumberplate = models.CharField(max_length=20, default='NA', blank=True, null=True)
    toolkit = models.ForeignKey(ToolkitStatus, on_delete=models.CASCADE)
    rvmlhrh = models.ForeignKey(RvmLhrh, on_delete=models.CASCADE)
    certcard = models.ForeignKey(CertCard, on_delete=models.CASCADE)
    pdistatus = models.ForeignKey(PdiStatus, on_delete=models.CASCADE)
    batterymake = models.ForeignKey(BatteryMake, on_delete=models.CASCADE)
    batteryconnectortype = models.ForeignKey(BatteryConnectorType, on_delete=models.CASCADE)
    engravednumberonbattery = models.CharField(max_length=50, default='NA', blank=True, null=True)
    typeofbattery = models.ForeignKey(BatteryType, on_delete=models.CASCADE)
    batterycapacity = models.ForeignKey(BatteryCapacity, on_delete=models.CASCADE)
    batterycompleteserialno = models.CharField(max_length=50, blank=True, null=True)
    batterycompleteserialno2 = models.CharField(max_length=50, blank=True, null=True, default='')
    available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.qrcode


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    design = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, null=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.product.name


class VehicleStockDetails(models.Model):
    productcode = models.ForeignKey(VehicleStock, on_delete=models.CASCADE)
    productdesc = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.productdesc


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.courier_name


class Uom(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class SparePartsStock(models.Model):
    qrcode = models.CharField(max_length=120, unique=True)
    materialcode = models.PositiveIntegerField()
    materialdesc = models.CharField(max_length=120)
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE)
    vendorinvoicedate = models.DateField()
    vendorinvoiceno = models.CharField(max_length=120)
    available = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.qrcode
