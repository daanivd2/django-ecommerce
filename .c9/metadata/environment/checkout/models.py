{"filter":false,"title":"models.py","tooltip":"/checkout/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":10,"column":42},"action":"remove","lines":["from django.contrib import admin","from .models import Order, OrderLineItem","","# Register your models here.","class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","    ","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline,) ","    ","admin.site.register(Order, OrderAdmin)    "],"id":2},{"start":{"row":0,"column":0},"end":{"row":28,"column":65},"action":"insert","lines":["from django.db import models","from products.models import Product","","# Create your models here.","","# Create your models here.","class Order(models.Model):","    full_name = models.CharField(max_length=50, blank=False)","    phone_number = models.CharField(max_length=20, blank=False)","    country = models.CharField(max_length=40, blank=False)","    postcode = models.CharField(max_length=20, blank=True)","    town_or_city = models.CharField(max_length=40, blank=False)","    street_address1 = models.CharField(max_length=40, blank=False)","    street_address2 = models.CharField(max_length=40, blank=False)","    county = models.CharField(max_length=40, blank=False)","    date = models.DateField()","","    def __str__(self):","        return \"{0}-{1}-{2}\".format(self.id, self.date, self.full_name)","","","class OrderLineItem(models.Model):","    order = models.ForeignKey(Order, null=False)","    product = models.ForeignKey(Product, null=False)","    quantity = models.IntegerField(blank=False)","","    def __str__(self):","        return \"{0} {1} @ {2}\".format(","            self.quantity, self.product.name, self.product.price)"]}]]},"ace":{"folds":[],"scrolltop":106,"scrollleft":0,"selection":{"start":{"row":16,"column":0},"end":{"row":16,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1562150985506,"hash":"b9af50b366751cf71f5b759239b3ee3acfc34e1f"}