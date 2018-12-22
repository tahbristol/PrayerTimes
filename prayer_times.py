import requests as req


def get_ip_address():
    
    try:
        response = req.get('https://api.ipify.org?format=json')
    except Exception as e:
        raise e
    
    return response.json()['ip']
    
def get_address_from_ip(ip):
    api_key = 'b1978ca33eb7b1733eca5503f8046b49'
    url = f'http://api.ipstack.com/{ip}?access_key={api_key}'
    
    try:
        response = req.get(url).json()
    except Exception as e:
        raise e
    
    return f"city={response['city']}&state={response['region_code']}&country={response['country_name']}"
    
def get_prayer_times(address):
    url = 'http://api.aladhan.com/v1/timingsByCity?'
    
    try:
        response = req.get(url + address).json()
    except Exception as e:
        raise e
    
    return response['data']