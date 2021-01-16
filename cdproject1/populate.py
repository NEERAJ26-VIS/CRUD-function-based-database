
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdproject1.settings')
django.setup()
from faker import Faker
from myapp.models import Employee
f=Faker()
def populate(n):
    for i in range(n):
        eno=f.random_int(min=1,max=20)
        ename=f.name()
        esal=f.random_int(min=10000,max=50000)
        eaddr=f.address()
        e=Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,eaddr=eaddr)
populate(20)        
