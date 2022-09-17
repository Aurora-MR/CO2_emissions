# Api ejecuta query sql y devuelve un dataframe
import pandas as pd
import requests
import io

url = 'https://3wecq7h5ea.execute-api.us-east-2.amazonaws.com/prod/nn?query='



def apirequest(query):
    '''
    Ejecuta query sql y devuelve un dataframe
    '''
    try:
       error_message = ''
    
       response = requests.get (url+query )
       if response.status_code == 200:
            df = pd.read_csv(io.BytesIO(response.content))
    
       else: 
            print(f' error :{response.status_code}')
    
    except Exception as exception:
        
        error_message = exception
        print (f'error exception : {error_message}')
    
    return df