from django.contrib import admin
from .models import proveedor
from .models import Topping
from .models import Pizza

admin.site.register(proveedor)
admin.site.register(Topping)
admin.site.register(Pizza)


