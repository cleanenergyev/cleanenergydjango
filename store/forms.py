from django import forms

from .models import Season, Drop, Product, Order, Delivery, Accessories, Battery, VehicleModel, Color, \
    ChargerRating, ToolkitStatus, RvmLhrh, CertCard, PdiStatus, BatteryMake, BatteryConnectorType, BatteryType,\
    BatteryCapacity, VehicleStock


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))

class BuyerForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'data-val': 'true',
        'data-val-required': 'Please enter username',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'password',
        'data-val': 'true',
        'data-val-required': 'Please enter password',
    }))
    retype_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'id': 'retype_password',
        'data-val': 'true',
        'data-val-required': 'Please enter retype_password',
    }))


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
        }


class DropForm(forms.ModelForm):
    class Meta:
        model = Drop
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'productcode', 'mrp', 'gst']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'productcode': forms.NumberInput(attrs={'class': 'form-control', 'id': 'productcode'}),
            'mrp': forms.NumberInput(attrs={'class': 'form-control', 'id': 'mrp'}),
            'gst': forms.NumberInput(attrs={'class': 'form-control', 'id': 'gst'})
        }


class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['name', 'accessoriescode', 'mrp', 'gst']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'accessoriescode': forms.NumberInput(attrs={'class': 'form-control', 'id': 'accessoriescode'}),
            'mrp': forms.NumberInput(attrs={'class': 'form-control', 'id': 'mrp'}),
            'gst': forms.NumberInput(attrs={'class': 'form-control', 'id': 'gst'})
        }


class DateInput(forms.DateInput):
    input_type = 'date'


class VehicleStockForm(forms.ModelForm):
    class Meta:
        model = VehicleStock
        fields = ['qrcode', 'vehicleinvoiceno', 'vehicleinvoicedatefromhe', 'exciseinvoiceno', 'battery',
                  'model', 'color', 'vehiclechassisno', 'motorno', 'controllerno', 'chargerno', 'chargerrating',
                  'ownersmanualno', 'heronumberplate', 'toolkit', 'rvmlhrh', 'certcard', 'pdistatus', 'batterymake',
                  'batteryconnectortype', 'engravednumberonbattery', 'typeofbattery', 'batterycapacity',
                  'batterycompleteserialno', 'batterycompleteserialno2']
        widgets = {
            'qrcode': forms.TextInput(attrs={'class': 'form-control', 'id': 'qrcode'}),
            'vehicleinvoiceno': forms.TextInput(attrs={'class': 'form-control', 'id': 'vehicleinvoiceno'}),
            'vehicleinvoicedatefromhe': DateInput(),
            'exciseinvoiceno': forms.TextInput(attrs={'class': 'form-control', 'id': 'exciseinvoiceno'}),
            'battery': forms.Select(attrs={'class': 'form-control', 'id': 'batteries'}),
            'model': forms.Select(attrs={'class': 'form-control', 'id': 'model'}),
            'color': forms.Select(attrs={'class': 'form-control', 'id': 'color'}),
            'vehiclechassisno': forms.TextInput(attrs={'class': 'form-control', 'id': 'vehiclechassisno'}),
            'motorno': forms.TextInput(attrs={'class': 'form-control', 'id': 'motorno'}),
            'controllerno': forms.TextInput(attrs={'class': 'form-control', 'id': 'controllerno'}),
            'chargerno': forms.TextInput(attrs={'class': 'form-control', 'id': 'chargerno'}),
            'chargerrating': forms.Select(attrs={'class': 'form-control', 'id': 'chargerrating'}),
            'ownersmanualno': forms.TextInput(attrs={'class': 'form-control', 'id': 'ownersmanualno'}),
            'heronumberplate': forms.TextInput(attrs={'class': 'form-control', 'id': 'heronumberplate'}),
            'toolkit': forms.Select(attrs={'class': 'form-control', 'id': 'toolkit'}),
            'rvmlhrh': forms.Select(attrs={'class': 'form-control', 'id': 'rvmlhrh'}),
            'certcard': forms.Select(attrs={'class': 'form-control', 'id': 'certcard'}),
            'pdistatus': forms.Select(attrs={'class': 'form-control', 'id': 'pdistatus'}),
            'batterymake': forms.Select(attrs={'class': 'form-control', 'id': 'batterymake'}),
            'batteryconnectortype': forms.Select(attrs={'class': 'form-control', 'id': 'batteryconnectortype'}),
            'engravednumberonbattery': forms.TextInput(attrs={'class': 'form-control', 'id': 'engravednumberonbattery'}),
            'typeofbattery': forms.Select(attrs={'class': 'form-control', 'id': 'typeofbattery'}),
            'batterycapacity': forms.Select(attrs={'class': 'form-control', 'id': 'batterycapacity'}),
            'batterycompleteserialno': forms.TextInput(attrs={'class': 'form-control', 'id': 'batterycompleteserialno'}),
            'batterycompleteserialno2': forms.TextInput(attrs={'class': 'form-control', 'id': 'batterycompleteserialno2'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'product', 'design', 'color', 'buyer', 'season', 'drop']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'design': forms.TextInput(attrs={'class': 'form-control', 'id': 'design'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'id': 'color'}),
            'buyer': forms.Select(attrs={'class': 'form-control', 'id': 'buyer'}),
            'season': forms.Select(attrs={'class': 'form-control', 'id': 'season'}),
            'drop': forms.Select(attrs={'class': 'form-control', 'id': 'drop'}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={'class': 'form-control', 'id': 'order'}),
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
        }


class BatteriesForm(forms.ModelForm):
    class Meta:
        model = Battery
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class VehicleModelForm(forms.ModelForm):
    class Meta:
        model = VehicleModel
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class ChargerRatingForm(forms.ModelForm):
    class Meta:
        model = ChargerRating
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class ToolkitStatusForm(forms.ModelForm):
    class Meta:
        model = ToolkitStatus
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class RvmLhrhForm(forms.ModelForm):
    class Meta:
        model = RvmLhrh
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class CertCardForm(forms.ModelForm):
    class Meta:
        model = CertCard
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class PdiStatusForm(forms.ModelForm):
    class Meta:
        model = PdiStatus
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class BatteryMakeForm(forms.ModelForm):
    class Meta:
        model = BatteryMake
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class BatteryConnectorTypeForm(forms.ModelForm):
    class Meta:
        model = BatteryConnectorType
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class BatteryTypeForm(forms.ModelForm):
    class Meta:
        model = BatteryType
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class BatteryCapacityForm(forms.ModelForm):
    class Meta:
        model = BatteryCapacity
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }