from flask import Flask, url_for, render_template, request,jsonify
import json

subjectai=['LP','NGSD_NGDP']
top5=['PPPE', 'PPPPC', 'PPPSH', 'TMG_RPCH', 'TM_RPCH']
duomenys={}
app = Flask(__name__)

# Su Postman suteikiam JSON body reiksmes
@app.route('/json-e', methods=['POST']) 
def json_example():
    req_data = request.get_json()
    Country=req_data['Country']
    Population=req_data['Population']
    NGSD_NGDP=req_data['NGSD_NGDP']
    NGSD=req_data['NGSD']
    # prideti likusius top 5 laukus
    d={'Country':Country,'Population':Population,'NGSD_NGDP':NGSD_NGDP,'NGSD':NGSD}
    duomenys=d
    return duomenys
# Paimtu duomenu sutvarkymas:


with app.open_resource('static/response.json') as f:
    duomenys = [json.load(f)]

@app.route('/home')
def home():
    return (render_template('home.html',duomenys=duomenys))






'''
israiska Postman, kad issaugoti duomenis
{
{
    "Country":"ASI",
    "Population":"5",
    "NGSD_NGDP":"3",
    "NGSD":"155"
}
}
'''






































# bandymai

@app.route('/gdp',methods=['POST', 'GET'])
def form_example():
    if request.method == 'POST':
        salis=request.form.get('salis')

        return '<h1> Salies kurios spesim GDP kodas yra: {}</h1>'.format(salis)



# Prie return prideti sali, kad galima butu naudoti salies gdp radimui?
    return '''<form method="POST" >
    Salies pavadinimo trumpinys <input type="text" name="salis">
    <input type="submit">
    </form>'''



 #   ,'''
 #          Country : {},
 #          Population : {},
 #          NGSD_NGDP  : {}
 #           '''.format(Country,Population,NGSD_NGDP)
    
@app.route('/json-ei', methods=['POST'])
def json_example1():
    req_data = request.get_json()

    subjectai=req_data['Country']
    key = {subjectai[0]: subjectai}
    return '''
           Country : {} '''.format(key[subjectai[0]])

           
# Ar eina padaryti, kad ranka json koda uzprogramavus, galima ji butu pakeisti per Postman su request.json?
# Kaip būtų galima paimti reikšmes is vieno def į kitą?
@app.route('/jsonget',methods=['POST,','GET'])
def json():
    subjectai=['Country','LP','NGSD_NGDP']
    top5=['PPPEX', 'PPPPC', 'PPPSH', 'TMG_RPCH', 'TM_RPCH']

    key = {subjectai[0]:subjectai[0]}

    for i in range(0,len(top5)):
        subjectai.append(top5[i])
    for i in range(1,len(subjectai)):
        key[subjectai[i]]=subjectai[i]

    #key = json.dumps(key)
    return jsonify(key)







@app.route('/j', methods=['POST']) 
def j():
    req_data = request.get_json()

    for i in range(0,len(top5)):
        subjectai.append(top5[i])
    for i in range(1,len(subjectai)):
        subjectai[i]=req_data[subjectai[i]]


    Country=req_data['Country']
    Population=req_data['Population']
    NGSD_NGDP=req_data['NGSD_NGDP']
    NGSD=req_data['NGSD']
    # prideti likusius top 5 laukus
    d={'Country':Country,'Population':Population,'data1':NGSD_NGDP,'data2':NGSD}
    duomenys=d
    return duomenys

if __name__=="__main__":
    app.run(debug=True)
