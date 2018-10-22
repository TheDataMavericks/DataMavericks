from flask import Flask, abort, jsonify, request, render_template
from sklearn.externals import joblib
import numpy as np
import json

gbr = joblib.load('model.pkl')

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('index.html')


# Route to display all the five attributes to measure health of a county
@app.route("/routes")
def routes():
    sample_list = []
    Routes_dict = {}
    Routes_dict['Makes'] = "/makes"
    Routes_dict['Years'] = "/years"
    
    
    # Routes_dict['User Selection'] = "/attributeSelection/<userSelection>"
    
    sample_list.append(Routes_dict)
    return jsonify(sample_list)


# @app.route('/api', methods=['POST'])
# def make_prediction():
#     data = request.get_json(force=True)
#     #convert our json to a numpy array
#     one_hot_data = input_to_one_hot(data)
#     predict_request = gbr.predict([one_hot_data])
#     output = [predict_request[0]]
#     print(data)
#     return jsonify(results=output)

def input_to_one_hot(data):
    # initialize the target vector with zero values
    enc_input = np.zeros(53)
    # set the numerical input as they are
    enc_input[0] = data['Year']
    enc_input[1] = data['Mileage']
    # enc_input[2] = data['fiscal_power']
    ##################### Mark #########################
    # get the array of marks categories
    makes = ['Acura', 'Alfa', 'AM', 'Aston', 'Audi', 'Bentley', 'BMW', 'Buick',
       'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Ferrari', 'FIAT',
       'Fisker', 'Ford', 'Freightliner', 'Genesis', 'Geo', 'GMC', 'Honda',
       'HUMMER', 'Hyundai', 'INFINITI', 'Isuzu', 'Jaguar', 'Jeep', 'Kia',
       'Lamborghini', 'Land', 'Lexus', 'Lincoln', 'Lotus', 'Maserati',
       'Maybach', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mercury', 'MINI',
       'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac',
       'Porsche', 'Ram', 'Rolls-Royce', 'Saab', 'Saturn', 'Scion',
       'smart', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen',
       'Volvo']
    cols = ['Year', 'Mileage', 'Make_AM', 'Make_Acura', 'Make_Aston', 'Make_Audi',
       'Make_BMW', 'Make_Bentley', 'Make_Buick', 'Make_Cadillac',
       'Make_Chevrolet', 'Make_Chrysler', 'Make_Dodge', 'Make_FIAT',
       'Make_Ford', 'Make_GMC', 'Make_Genesis', 'Make_HUMMER', 'Make_Honda',
       'Make_Hyundai', 'Make_INFINITI', 'Make_Isuzu', 'Make_Jaguar',
       'Make_Jeep', 'Make_Kia', 'Make_Lamborghini', 'Make_Land', 'Make_Lexus',
       'Make_Lincoln', 'Make_Lotus', 'Make_MINI', 'Make_Maserati',
       'Make_Maybach', 'Make_Mazda', 'Make_Mercedes-Benz', 'Make_Mercury',
       'Make_Mitsubishi', 'Make_Nissan', 'Make_Oldsmobile', 'Make_Plymouth',
       'Make_Pontiac', 'Make_Porsche', 'Make_Ram', 'Make_Saab', 'Make_Saturn',
       'Make_Scion', 'Make_Subaru', 'Make_Suzuki', 'Make_Tesla', 'Make_Toyota',
       'Make_Volkswagen', 'Make_Volvo', 'Make_smart']

    # redefine the the user inout to match the column name
    redefinded_user_input = 'Make_'+data['Make']

    # Make sure that the index exists in the columns to prevent ValueError 
    if redefinded_user_input in cols :
        # search for the index in columns name list 
        mark_column_index = cols.index(redefinded_user_input)
        #print(mark_column_index)
        # fullfill the found index with 1
        enc_input[mark_column_index] = 1
    return enc_input

@app.route('/api',methods=['POST'])
def get_delay():
    result=request.form
    year = result['year_model']
    mileage = result['mileage']
    make = result['mark']
    print(year)
    # fiscal_power = result['fiscal_power']
    # fuel_type = result['fuel_type']

    user_input = {'Year':year, 'Mileage':mileage,  'Make':make}
    
    print(user_input)
    a = input_to_one_hot(user_input)
    price_pred = gbr.predict([a])[0]
    price_pred = round(price_pred, 2)
    return json.dumps({'Price':price_pred})

@app.route('/makes')
def supported_makes():
    print('makes invoked')
    MakeList =[]
    MakeDictionary={}
    
    # Need to fetched from mongo. But hardcoded  
    makes = ['Acura', 'Alfa', 'AM', 'Aston', 'Audi', 'Bentley', 'BMW', 'Buick',
       'Cadillac', 'Chevrolet', 'Chrysler', 'Dodge', 'Ferrari', 'FIAT',
       'Fisker', 'Ford', 'Freightliner', 'Genesis', 'Geo', 'GMC', 'Honda',
       'HUMMER', 'Hyundai', 'INFINITI', 'Isuzu', 'Jaguar', 'Jeep', 'Kia',
       'Lamborghini', 'Land', 'Lexus', 'Lincoln', 'Lotus', 'Maserati',
       'Maybach', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mercury', 'MINI',
       'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac',
       'Porsche', 'Ram', 'Rolls-Royce', 'Saab', 'Saturn', 'Scion',
       'smart', 'Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen',
       'Volvo']

    MakeDictionary['Makes'] = makes 
    MakeList.append(MakeDictionary)
    return jsonify(MakeList)  


@app.route('/years')
def supported_years():
    print('years invoked')
    YearsList =[]
    YearsDictionary={}
    
    # Need to fetched from mongo. But hardcoded at the momement.  
    years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007','2008', '2009', '2010', '2011', '2012', '2013','2014', '2015', '2016', '2017', '2018']

    YearsDictionary['Years'] = years 
    YearsList.append(YearsDictionary)
    print(YearsList)
    return jsonify(YearsList)  

  


if __name__ == '__main__':
    app.run(port=8080, debug=True)






