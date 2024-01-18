import uuid

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class Products(DjangoCassandraModel):

    class Meta:
        app_label = 'product_catalogue_service'

    product_id = columns.Text(primary_key=True)
    name = columns.Text(required=True)
    description = columns.Text(required=False)
    price = columns.Decimal(default=0.0)
    stock_quantity = columns.Integer(default=0)

