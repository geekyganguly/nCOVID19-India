import requests
import json
import re


myths_img = [
    '/assets/images/myths/1.png',
    '/assets/images/myths/2.png',
    '/assets/images/myths/3.png',
    '/assets/images/myths/4.png',
    '/assets/images/myths/5.png',
    '/assets/images/myths/6.png',
    '/assets/images/myths/7.png',
    '/assets/images/myths/8.png',
    '/assets/images/myths/9.png',
    '/assets/images/myths/10.png',
    '/assets/images/myths/11.png',
    '/assets/images/myths/12.png',
    '/assets/images/myths/13.png',
    '/assets/images/myths/14.png'
]

myths_data = [
    'Cold weather and snow CANNOT kill the CoronaVirus .',
    'The coronavirus CAN be transmitted in areas with hot and humid climates.',
    'The coronavirus CANNOT be transmitted through mosquito bites.',
    'There is NO evidence that companion animals/pets such as dogs or cats can transmit the coronavirus.',
    'Taking a hot bath DOES NOT prevent the coronavirus.',
    'Hand dryers are NOT effective in killing the coronavirus.',
    'Ultraviolet light SHOULD NOT be used for sterilization and can cause skin irritation.',
    'Thermal scanners CAN detect if people have a fever but CANNOT detect whether or not someone has the coronavirus.',
    'Spraying alcohol or chlorine all over your body WILL NOT kill viruses that have already entered your body.',
    'Vaccines against pneumonia, such as pneumococcal vaccine and Haemophilus influenzae type b (Hib) vaccine, DO NOT provide protection against the coronavirus.',
    'There is NO evidence that regularly rinsing the nose with saline has protected people from infection with the coronavirus.',
    'Garlic is healthy but there is NO evidence from the current outbreak that eating garlic has protected people from the coronavirus.',
    'Antibiotics DO NOT work against viruses, antibiotics only work against bacteria.',
    'To date, there is NO specific medicine recommended to prevent or treat the coronavirus.'
]

urls = {
    'world_summary_data_url' : 'https://corona.lmao.ninja/v2/all?yesterday',
    'india_latest_data_url' : 'https://api.rootnet.in/covid19-in/stats/latest',
    'india_timeline_url' : 'https://api.rootnet.in/covid19-in/stats/history',
    'states_contacts_url' : 'https://api.rootnet.in/covid19-in/contacts',
    'medical_colleges_url' : 'https://api.rootnet.in/covid19-in/hospitals/medical-colleges',
    'hospitals_beds_url' : 'https://api.rootnet.in/covid19-in/hospitals/beds',
}

def get_data(url):
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.text)
    return data

def get_world_data(url):
    world_summary_data = get_data(url)
    world_confirmed = world_summary_data["cases"]
    world_active = world_summary_data["active"]
    world_recovered = world_summary_data["recovered"]
    world_deaths = world_summary_data["deaths"]
    return world_confirmed, world_active, world_recovered, world_deaths

def get_india_data(url):
    india_summary_data = get_data(url)
    india_confirmed = india_summary_data["data"]["summary"]['total']
    india_recovered = india_summary_data["data"]["summary"]['discharged']
    india_deaths = india_summary_data["data"]["summary"]['deaths']
    india_active = int(india_confirmed) - (int(india_recovered) + int(india_deaths))
    update_date = re.compile(r'\d\d\d\d-\d\d-\d\d').search(india_summary_data["lastOriginUpdate"]).group()
    return update_date, india_confirmed, india_active, india_recovered, india_deaths

def get_state_data(url, state):
    india_summary_data = get_data(url)
    for i in india_summary_data["data"]["regional"]:
        if state in i.values():
            state_confirmed = i['totalConfirmed']
            state_recovered = i['discharged']
            state_deaths = i['deaths']
            state_active = int(state_confirmed) - (int(state_recovered) + int(state_deaths))
    return state_confirmed, state_active, state_recovered, state_deaths

def get_india_timeline_data(url):
    timeline_data = get_data(url)
    date = []
    confirmed = []
    recovered = []
    deaths = []
    for i in timeline_data['data']:
        date.append(i['day'])
        confirmed.append(i['summary']['total'])
        recovered.append(i['summary']['discharged'])
        deaths.append(i['summary']['deaths'])
    return date, confirmed, recovered, deaths

def get_states_data(url):
    india_summary_data = get_data(url)
    states = []
    confirmed = []
    active = []
    recovered = []
    deaths = []
    for i in india_summary_data['data']["regional"]:
        states.append(i['loc'])
        confirmed.append(i['totalConfirmed'])
        recovered.append(i['discharged'])
        deaths.append(i['deaths'])
        active.append(int(i['totalConfirmed']) - (int(i['discharged']) - int(i['deaths'])))
    return states, confirmed, active, recovered, deaths

def get_states_contacts_data(url):
    contacts_data = get_data(url)
    states_contacts = contacts_data["data"]["contacts"]["regional"]
    return states_contacts

def get_medical_colleges_data(url):
    medical_data = get_data(url)
    medical_colleges = medical_data["data"]["medicalColleges"]
    return medical_colleges

def get_hosipital_bed_data(url):
    beds_data = get_data(url)
    beds = beds_data["data"]["regional"]
    return beds
