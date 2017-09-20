# from django.contrib.auth.models import User

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Cheese


class CheeseResource(DjangoResource):
    # Controls what data is included in the serialized output.
    preparer = FieldsPreparer(fields={
        'name': 'name',
        'age': 'age',
        'color': 'color',
    })

    # GET /
    def list(self):
        return Cheese.objects.all()

    # GET /pk/
    def detail(self, pk):
        return Cheese.objects.get(id=pk)

    # POST /
    def create(self):
        return Cheese.objects.create(
            name=self.data['name'],
            age=self.data['age'],
            color=self.data['color']
        )

    # PUT /pk/
    def update(self, pk):
        try:
            cheese = Cheese.objects.get(id=pk)
        except Cheese.DoesNotExist:
            cheese = Cheese()

        cheese.name = self.data['name'],
        cheese.age = self.data['age'],
        cheese.color = self.data['color']
        cheese.save()
        return cheese

    # DELETE /pk/
    def delete(self, pk):
        Cheese.objects.get(id=pk).delete()
