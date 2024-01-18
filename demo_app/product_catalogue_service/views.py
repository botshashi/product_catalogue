from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from auth_service.decorators import validate_jwt_token
from .models import Products
import uuid

@api_view(['POST'])
@csrf_exempt
@validate_jwt_token
def create_products(request):
    if request.method == 'POST':
        product_name = request.data.get('product_name')
        product_desc = request.data.get('description', '')
        price = request.data.get('price')
        # if user doesn't add product quantity, set it to 1
        quantity = request.data.get('quantity', 1)
        # product name and price should not be empty
        if not product_name or not price:
            return JsonResponse({'error': 'product_name and price cannot be empty'}, status=status.HTTP_400_BAD_REQUEST)

        # if user adds invalid product quantity, set it to 1
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1
        # product price validation
        try:
            price = float(price)
        except ValueError:
            return JsonResponse({'error': 'Invalid product price, only non-negative decimal allowed '},
                                status=status.HTTP_400_BAD_REQUEST)

        # if user adds invalid product quantity, set it to 1
        if quantity < 0:
            return JsonResponse({'error': 'Invalid product quantity only non-negative integer allowed '},
                                status=status.HTTP_400_BAD_REQUEST)
        # product price validation
        if price < 0:
            return JsonResponse({'error': 'Invalid product price only non-negative decimal allowed '},
                                status=status.HTTP_400_BAD_REQUEST)
        product_id = str(uuid.uuid4())
        product = Products(product_id=product_id,name=product_name, description=product_desc, price=price,
                           stock_quantity=quantity)
        try:
            product.save()
            return JsonResponse({'message': 'Product successfully created.'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(str(e))
            JsonResponse({'error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        JsonResponse({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
@validate_jwt_token
def products(request):
    if request.method == 'GET':
        try:
            serialized_product = Products.objects.all()
            res = []
            for p in serialized_product:
                res.append(p.product_id)
            data = {'products': res}
            return JsonResponse(data, status=status.HTTP_200_OK)
        except Exception as e:
            print(str(e))
            JsonResponse({'error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        JsonResponse({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
@validate_jwt_token
def product_details(request):
    if request.method == 'GET':
        prod_id = request.GET.get('product_id', None)
        try:
            product_detail = Products.objects.get(product_id=prod_id)
            res = {
                'name': product_detail.name,
                'description': product_detail.description,
                'price': product_detail.price,
                'status': 'out of stock' if product_detail.stock_quantity == 0 else 'in stock'
            }
            return JsonResponse({'product': res}, status=200)
        except Products.DoesNotExist:
            return JsonResponse({'message': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(str(e))
            JsonResponse({'error': 'Internal server error.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        JsonResponse({'error': 'Invalid request method.'}, status=status.HTTP_400_BAD_REQUEST)