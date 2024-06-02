from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    user = request.user
    hello = 'Hello world'

    context = {
        'user': user,
        'hello' : hello,
    }
    return render(request, 'main/home.html', context)

from django.shortcuts import render
import requests

def stock_data_view(request):
    # Your Polygon.io API key
    api_key = '1eLTsTnV48K6invlrMV1Qop4iS8U__Xp'
    
    # Symbol of the stock you want to fetch data for
    symbol = 'AAPL'  # Change this to the symbol of the stock you want to fetch
    
    # Construct the API endpoint URL
    api_url = f'https://api.polygon.io/v1/meta/symbols/{symbol}/company?apiKey={api_key}'
    
    try:
        # Fetch stock data from Polygon.io API
        response = requests.get(api_url)
        data = response.json()
        
        # Extract relevant data
        company_name = data.get('name', '')
        company_symbol = data.get('symbol', '')
        sector = data.get('sector', '')
        industry = data.get('industry', '')
        description = data.get('description', '')
        
        # Pass data to the template
        context = {
            'company_name': company_name,
            'company_symbol': company_symbol,
            'sector': sector,
            'industry': industry,
            'description': description,
        }
        
        # Render the template with the fetched data
        return render(request, 'main/home.html', context)
    
    except Exception as e:
        error_message = f'Error fetching stock data: {str(e)}'
        return render(request, 'main/home.html', {'error_message': error_message})

def undefined(request):

    return render(request, 'main/undefined.html')