from django.db.models import Count, Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Buyer,
    Season,
    Drop,
    Product,
    Order,
    Delivery,
    Accessories,
    VehicleStock,
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
    BatteryCapacity
)
from .forms import (
    SupplierForm,
    BuyerForm,
    SeasonForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm,
    AccessoriesForm,
    VehicleStockForm,
    BatteriesForm,
    VehicleModelForm,
    ColorForm,
    ChargerRatingForm,
    ToolkitStatusForm,
    RvmLhrhForm,
    CertCardForm,
    PdiStatusForm,
    BatteryMakeForm,
    BatteryConnectorTypeForm,
    BatteryTypeForm,
    BatteryCapacityForm
)

# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_supplier=True)
                Supplier.objects.create(user=user, name=name, address=address)
                return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSupplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Buyer views
@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()
    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(username=username, password=password, email=email, is_buyer=True)
                Buyer.objects.create(user=user, name=name, address=address)
                return redirect('buyer-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addbuyer.html', context)

class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'


# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('season-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSeason.html', context)


class SeasonListView(ListView):
    model = Season
    template_name = 'store/season_list.html'
    context_object_name = 'season'


# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCategory.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'store/category_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addProduct.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


@login_required(login_url='login')
def create_accessories(request):
    forms = AccessoriesForm()
    if request.method == 'POST':
        forms = AccessoriesForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('accessories-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addAccessories.html', context)


class AccessoriesListView(ListView):
    model = Accessories
    template_name = 'store/accessories_list.html'
    context_object_name = 'accessories'


@login_required(login_url='login')
def create_vehicle_stock(request):
    forms = VehicleStockForm()
    if request.method == 'POST':
        forms = VehicleStockForm(request.POST)
        if forms.is_valid():
            # forms.save()
            ch = 'a'
            ch1 = 'A'
            qrcode = forms.cleaned_data['qrcode']
            if ch in qrcode:
                productcd = qrcode.split('a')[0]
            elif ch1 in qrcode:
                productcd = qrcode.split('A')[0]
            else:
                raise Exception('Invalid qrcode')
            vehicleinvoiceno = forms.cleaned_data['vehicleinvoiceno']
            vehicleinvoicedatefromhe = forms.cleaned_data['vehicleinvoicedatefromhe']
            exciseinvoiceno = forms.cleaned_data['exciseinvoiceno']
            battery = forms.cleaned_data['battery']
            model = forms.cleaned_data['model']
            color = forms.cleaned_data['color']
            vehiclechassisno = forms.cleaned_data['vehiclechassisno']
            motorno = forms.cleaned_data['motorno']
            controllerno = forms.cleaned_data['controllerno']
            chargerno = forms.cleaned_data['chargerno']
            chargerrating = forms.cleaned_data['chargerrating']
            ownersmanualno = forms.cleaned_data['ownersmanualno']
            heronumberplate = forms.cleaned_data['heronumberplate']
            toolkit = forms.cleaned_data['toolkit']
            rvmlhrh = forms.cleaned_data['rvmlhrh']
            certcard = forms.cleaned_data['certcard']
            pdistatus = forms.cleaned_data['pdistatus']
            batterymake = forms.cleaned_data['batterymake']
            batteryconnectortype = forms.cleaned_data['batteryconnectortype']
            engravednumberonbattery = forms.cleaned_data['engravednumberonbattery']
            typeofbattery = forms.cleaned_data['typeofbattery']
            batterycapacity = forms.cleaned_data['batterycapacity']
            batterycompleteserialno = forms.cleaned_data['batterycompleteserialno']
            batterycompleteserialno2 = forms.cleaned_data['batterycompleteserialno2']
            available = True
            productdesctest = Product.objects.filter(productcode=productcd)

            VehicleStock.objects.create(
                qrcode=qrcode,
                productcode=productcd,
                productdesc=productdesctest[0],
                vehicleinvoiceno=vehicleinvoiceno,
                vehicleinvoicedatefromhe=vehicleinvoicedatefromhe,
                exciseinvoiceno=exciseinvoiceno,
                battery=battery,
                model=model,
                color=color,
                vehiclechassisno=vehiclechassisno,
                motorno=motorno,
                controllerno=controllerno,
                chargerno=chargerno,
                chargerrating=chargerrating,
                ownersmanualno=ownersmanualno,
                heronumberplate=heronumberplate,
                toolkit=toolkit,
                rvmlhrh=rvmlhrh,
                certcard=certcard,
                pdistatus=pdistatus,
                batterymake=batterymake,
                batteryconnectortype=batteryconnectortype,
                engravednumberonbattery=engravednumberonbattery,
                typeofbattery=typeofbattery,
                batterycapacity=batterycapacity,
                batterycompleteserialno=batterycompleteserialno,
                batterycompleteserialno2=batterycompleteserialno2,
                available=available
            )
            return redirect('vehicle-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addStock.html', context)


class VehicleListView(ListView):
    model = VehicleStock
    template_name = 'store/vehicle_stock_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vehiclestock'] = VehicleStock.objects.all().order_by('-id')
        return context


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            color = forms.cleaned_data['color']
            buyer = forms.cleaned_data['buyer']
            season = forms.cleaned_data['season']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                buyer=buyer,
                season=season,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addOrder.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addelivery.html', context)


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'


@login_required(login_url='login')
def create_battery(request):
    forms = BatteriesForm()
    if request.method == 'POST':
        forms = BatteriesForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('battery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addBattery.html', context)


class BatteriesListView(ListView):
    model = Battery
    template_name = 'store/batteries_list.html'
    context_object_name = 'batteries'


@login_required(login_url='login')
def create_vehicle_model(request):
    forms = VehicleModelForm()
    if request.method == 'POST':
        forms = VehicleModelForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('vehicle-model-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addVehicleModel.html', context)


class VehicleModelListView(ListView):
    model = VehicleModel
    template_name = 'store/vehicle_model_list.html'
    context_object_name = 'vehiclemodel'


@login_required(login_url='login')
def create_color(request):
    forms = ColorForm()
    if request.method == 'POST':
        forms = ColorForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('color-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addColor.html', context)


class ColorListView(ListView):
    model = Color
    template_name = 'store/color_list.html'
    context_object_name = 'color'


@login_required(login_url='login')
def create_charger_rating(request):
    forms = ChargerRatingForm()
    if request.method == 'POST':
        forms = ChargerRatingForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('charger-rating-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addChargerRating.html', context)


class ChargerRatingListView(ListView):
    model = ChargerRating
    template_name = 'store/charger_rating_list.html'
    context_object_name = 'chargerrating'


@login_required(login_url='login')
def create_toolkit_status(request):
    forms = ToolkitStatusForm()
    if request.method == 'POST':
        forms = ToolkitStatusForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('toolkit-status-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addToolkitStatus.html', context)


class ToolkitStatusListView(ListView):
    model = ToolkitStatus
    template_name = 'store/toolkit_status_list.html'
    context_object_name = 'toolkitstatus'


@login_required(login_url='login')
def create_rvm_lhrh(request):
    forms = RvmLhrhForm()
    if request.method == 'POST':
        forms = RvmLhrhForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('rvm-lhrh-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addRvmlhrh.html', context)


class RvmLhrhListView(ListView):
    model = RvmLhrh
    template_name = 'store/rvm_lhrh_list.html'
    context_object_name = 'rvmlhrh'


@login_required(login_url='login')
def create_cert_card(request):
    forms = CertCardForm()
    if request.method == 'POST':
        forms = CertCardForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('cert-card-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCertCard.html', context)


class CertCardListView(ListView):
    model = CertCard
    template_name = 'store/cert_card_list.html'
    context_object_name = 'certcard'



@login_required(login_url='login')
def create_pdi_status(request):
    forms = PdiStatusForm()
    if request.method == 'POST':
        forms = PdiStatusForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('pdi-status-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addPdiStatus.html', context)


class PdiStatusListView(ListView):
    model = PdiStatus
    template_name = 'store/pdi_status_list.html'
    context_object_name = 'pdistatus'


@login_required(login_url='login')
def create_battery_make(request):
    forms = BatteryMakeForm()
    if request.method == 'POST':
        forms = BatteryMakeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('battery-make-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addBatteryMake.html', context)


class BatteryMakeListView(ListView):
    model = BatteryMake
    template_name = 'store/battery_make_list.html'
    context_object_name = 'batterymake'


@login_required(login_url='login')
def create_battery_connector_type(request):
    forms = BatteryConnectorTypeForm()
    if request.method == 'POST':
        forms = BatteryConnectorTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('battery-connector-type-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addBatteryConnectorType.html', context)


class BatteryConnectorTypeListView(ListView):
    model = BatteryConnectorType
    template_name = 'store/battery_connector_type_list.html'
    context_object_name = 'batteryconnectortype'


@login_required(login_url='login')
def create_battery_type(request):
    forms = BatteryTypeForm()
    if request.method == 'POST':
        forms = BatteryTypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('battery-type-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addBatteryType.html', context)


class BatteryTypeListView(ListView):
    model = BatteryType
    template_name = 'store/battery_type_list.html'
    context_object_name = 'batterytype'


@login_required(login_url='login')
def create_battery_capacity(request):
    forms = BatteryCapacityForm()
    if request.method == 'POST':
        forms = BatteryCapacityForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('battery-capacity-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addBatteryCapacity.html', context)


class BatteryCapacityListView(ListView):
    model = BatteryCapacity
    template_name = 'store/battery_capacity_list.html'
    context_object_name = 'batterycapacity'


class SearchResultsView(ListView):
    model = VehicleStock
    template_name = 'store/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['x'] = VehicleStock.objects.all().order_by
        print(context)
        print(VehicleStock.objects.values_list('productcode', 'color', 'model', 'productdesc'))
        context['vehiclestockdetails'] = VehicleStock.objects.values('productcode', 'color', 'model', 'productdesc') \
            .annotate(total=Count('color')) \
            .filter(Q(productdesc__icontains=query) & Q(available=True))
        return context
