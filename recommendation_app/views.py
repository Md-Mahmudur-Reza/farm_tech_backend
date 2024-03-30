from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse


from joblib import load

region_codes = {
    'Alberta': 0,
    'British Columbia': 1,
    'Manitoba': 2,
    'New Brunswick': 3,
    'Newfoundland and Labrador': 4,
    'Nova Scotia': 5,
    'Ontario': 6,
    'Prince Edward Island': 7,
    'Quebec': 8,
    'Saskatchewan': 9
}

soil_codes = {
    'Chernozem': 0,
    'Luvisol': 1,
    'Podzol': 2
}

agr_prac_codes = {
    'Dairy farming': 0,
    'Fishing': 1,
    'Fruit farming': 2,
    'Grain farming': 3,
    'Mixed farming': 4,
    'Potato farming': 5
}



crops_codes = {
    0: 'Apples',
    1: 'Barley',
    2: 'Blueberries',
    3: 'Canola',
    4: 'Capelin',
    5: 'Cherries',
    6: 'Cod',
    7: 'Corn',
    8: 'Cranberries',
    9: 'Dairy Products',
    10: 'Grapes',
    11: 'Lentils',
    12: 'Lobster',
    13: 'Maple Syrup',
    14: 'Mussels',
    15: 'Peaches',
    16: 'Peas',
    17: 'Potatoes',
    18: 'Snow Crab',
    19: 'Soybeans',
    20: 'Strawberries',
    21: 'Wheat'
}


model = load('recommendation_app/saved_model/model.joblib')

@api_view(['POST', 'GET'])
def predictor(request):
    if request.method == 'POST':
        data = request.data
        print("Request : ", data)
        region = data.get('region')
        print("Region : ", region)
        soil_type = data.get('soil_type')
        print("soil_type : ", soil_type)
        agricultural_practices = data.get('agricultural_practices')
        print("agricultural_practices : ", agricultural_practices)


        result = model.predict([[region_codes[region],soil_codes[soil_type],agr_prac_codes[agricultural_practices]]])[0]
        print("Result : ", crops_codes[result])
        return JsonResponse({"result":crops_codes[result]})
    elif request.method == 'GET':
        return Response({"data": "null"})
    else:
        return Response({"error": "Method not allowed"}, status=405)