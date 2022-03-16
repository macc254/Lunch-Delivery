
from .models import Meal
import urllib.request, json

# base_url = 'www.themealdb.com/api/json/v1/1/random.php'
base_url = 'https://world.openfoodfacts.org/api/v0/product/737628064502.json'



def get_meal():
    '''
    '''
    url = base_url
    
    res = urllib.request.urlopen(url)
    data = json.loads(res.read())

    response=[]
    strMeal = data.get('meal')
    strCategory = data.get('category')
    strInstructions = data.get('instructions')
    strMealThumb = data.get('image')
    strYoutube = data.get('youtube')
    

  

    new_meal = Meal(strMeal, strCategory, strInstructions, strMealThumb,strYoutube)
    response.append(new_meal)

    return response