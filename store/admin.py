from django.contrib import admin

from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery,
    Battery,
    VehicleModel,
    Color,
    ChargerRating,
    ToolkitStatus,
    RvmLhrh,
    CertCard,
    PdiStatus,
    BatteryMake,
    BatteryConnectorType,
    BatteryType,
    BatteryCapacity,
    VehicleStock,
    VehicleStockDetails,
    PaymentMode,
    MoneyReceipt,

)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Season)
admin.site.register(Drop)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Delivery)
admin.site.register(Battery)
admin.site.register(VehicleModel)
admin.site.register(Color)
admin.site.register(ChargerRating)
admin.site.register(ToolkitStatus)
admin.site.register(RvmLhrh)
admin.site.register(CertCard)
admin.site.register(PdiStatus)
admin.site.register(BatteryMake)
admin.site.register(BatteryConnectorType)
admin.site.register(BatteryType)
admin.site.register(BatteryCapacity)
admin.site.register(VehicleStock)
admin.site.register(VehicleStockDetails)
admin.site.register(PaymentMode)
admin.site.register(MoneyReceipt)
