import requests as req


def get_ip_address():
    
    try:
        response = req.get('https://api.ipify.org?format=json')
    except Exception as e:
        raise e
    
    return response.json()['ip']
    
def get_address_from_ip(ip):
    pass
    
def get_prayer_times(address):
    pass
