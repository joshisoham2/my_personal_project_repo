import streamlit as st
import pandas as pd

from prediction_helper import predict


st.title("Toyota Corolla Price Predictor")


age_08_04 = mfg_month = mfg_year = None
km = hp = met_color = automatic = cc = doors = None
gears = quarterly_tax = weight = mfr_guarantee = None
bovag_guarantee = guarantee_period = abs = airbag_1 = airbag_2 = None 
airco = automatic_airco = boardcomputer = cd_player = None 
central_lock = powered_windows = power_steering = radio = None 
mistlamps = sport_model = backseat_divider = metallic_rim = None 
radio_cassette = parking_assistant = tow_bar = None

color_dict = {'Color_Black': 0, 'Color_Blue': 0, 'Color_Green': 0, 'Color_Grey': 0, 'Color_Red': 0, 'Color_Silver': 0, 'Color_Violet': 0,
               'Color_White': 0, 'Color_Yellow': 0}

fuel_type_dict = {'Fuel_Type_Diesel': 0, 'Fuel_Type_Petrol': 0}

categorical_options = {
    "Fuel Type": ['Diesel', 'CNG', 'Petrol'], 
    "Color": ['Beige', 'Black', 'Blue', 'Green', 'Grey', 'Red', 'Silver', 'Violet', 'White', 'Yellow']
}

yes_no_options = {
    "Metallic Color": ["Yes", "No"],
    "Automatic": ["Yes", "No"],
    "Manufacture Guarantee": ["Yes", "No"],
    "BOVAG Guarantee": ["Yes", "No"],
    "Anti-lock Braking System": ["Yes", "No"],
    "Driver's Side Airbag": ["Yes", "No"],
    "Front Passenger Airbag": ["Yes", "No"],
    "Airconditioning": ["Yes", "No"],
    "Automatic Airconditioning": ["Yes", "No"],
    "Board Computer": ["Yes", "No"],
    "CD Player": ["Yes", "No"],
    "Central Locking System": ["Yes", "No"],
    "Powered Windows": ["Yes", "No"],
    "Power Steering": ["Yes", "No"],
    "Radio": ["Yes", "No"],
    "Mist lamps": ["Yes", "No"],
    "Sport Model": ["Yes", "No"],
    "Backseat Divider": ["Yes", "No"],
    "Metallic Rim": ["Yes", "No"],
    "Radio Cassette": ["Yes", "No"],
    "Parking Assistant": ["Yes", "No"],
    "Tow Bar": ["Yes", "No"]
}


# Create six rows of six columns each
row1 = st.columns(6)
row2 = st.columns(6)
row3 = st.columns(6)
row4 = st.columns(6)
row5 = st.columns(6)
row6 = st.columns(6)



with row1[0]:
    age_08_04 = st.number_input("Age in Months as of Aug. 2004", min_value=1, step=1, max_value=80)
with row1[1]:
    mfg_month = st.number_input("Manufacturing Month", min_value=1, step=1, max_value=12)
with row1[2]:
    mfg_year = st.number_input("Manufacturing Year", min_value=1998, step=1, max_value=2004)
with row1[3]:
    value = st.selectbox('Fuel Type', categorical_options['Fuel Type'])
    text_value = f"Fuel_Type_{value}"
    if text_value in fuel_type_dict.keys():
        fuel_type_dict[text_value] = 1
with row1[4]:
    value = st.selectbox('Color', categorical_options['Color'])
    text_value = f"Color_{value}"
    if text_value in color_dict.keys():
        color_dict[text_value] = 1
with row1[5]:
    km = st.number_input("KM", min_value=1, step=1, max_value=243000)

with row2[0]:
    cc = st.number_input("Engine Capacity", min_value=1300, step=1, max_value=16000)
with row2[2]:
    doors = st.number_input("Number of Doors", min_value=2, step=1, max_value=5)
with row2[3]:
    gears = st.number_input("Number of Gears", min_value=3, step=1, max_value=6)   
with row2[4]:
    quarterly_tax = st.number_input("Quarterly Tax", min_value=19, step=1, max_value=283)   
with row2[5]:
    weight = st.number_input("Weight", min_value=1000, step=1, max_value=1615)     


 
with row3[0]:
    hp = st.number_input("HP", min_value=69, step=1, max_value=192)
with row3[1]:
    value = st.selectbox("Metallic Color", yes_no_options["Metallic Color"])
    if value == "Yes": 
        met_color = 1
    else:
        met_color = 0
with row3[2]:
    value = st.selectbox("Automatic", yes_no_options["Automatic"])
    if value == "Yes": 
        automatic = 1
    else:
        automatic = 0
with row3[3]:
    value = st.selectbox("Manufacture Guarantee", yes_no_options["Manufacture Guarantee"])
    if value == "Yes": 
        mfr_guarantee = 1
    else:
        mfr_guarantee = 0
with row3[4]:
    value = st.selectbox("BOVAG Guarantee", yes_no_options["BOVAG Guarantee"])
    if value == "Yes": 
        bovag_guarantee = 1
    else:
        bovag_guarantee = 0 
with row3[5]:
    guarantee_period = st.number_input("Guarantee Period", min_value=3, step=1, max_value=36)

with row4[0]:
    value = st.selectbox("Anti-lock Braking System", yes_no_options["Anti-lock Braking System"])
    if value == "Yes": 
        abs = 1
    else:
        abs = 0
with row4[1]:
    value = st.selectbox("Driver's Side Airbag", yes_no_options["Driver's Side Airbag"])
    if value == "Yes": 
        airbag_1 = 1
    else:
        airbag_1 = 0        
with row4[2]:
    value = st.selectbox("Front Passenger Airbag", yes_no_options["Front Passenger Airbag"])
    if value == "Yes": 
        airbag_2 = 1
    else:
        airbag_2 = 0     
with row4[3]:
    value = st.selectbox("Airconditioning", yes_no_options["Airconditioning"])
    if value == "Yes": 
        airco = 1
    else:
        airco = 0                   
with row4[4]:
    value = st.selectbox("Automatic Airconditioning", yes_no_options["Automatic Airconditioning"])
    if value == "Yes": 
        automatic_airco = 1
    else:
        automatic_airco = 0 
with row4[5]:
    value = st.selectbox("Board Computer", yes_no_options["Board Computer"])
    if value == "Yes": 
        boardcomputer = 1
    else:
        boardcomputer = 0  

with row5[0]:
    value = st.selectbox("CD Player", yes_no_options["CD Player"])
    if value == "Yes": 
        cd_player = 1
    else:
        cd_player = 0  
with row5[1]:
    value = st.selectbox("Central Locking System", yes_no_options["Central Locking System"])
    if value == "Yes": 
        central_lock = 1
    else:
        central_lock = 0    
with row5[2]:
    value = st.selectbox("Powered Windows", yes_no_options["Powered Windows"])
    if value == "Yes": 
        powered_windows = 1
    else:
        powered_windows = 0 
with row5[3]:
    value = st.selectbox("Power Steering", yes_no_options["Power Steering"])
    if value == "Yes": 
        power_steering = 1
    else:
        power_steering = 0    
with row5[4]:
    value = st.selectbox("Radio", yes_no_options["Radio"])
    if value == "Yes": 
        radio = 1
    else:
        radio = 0  
with row5[5]:
    value = st.selectbox("Mist lamps", yes_no_options["Mist lamps"])
    if value == "Yes": 
        mistlamps = 1
    else:
        mistlamps = 0     

with row6[0]:
    value = st.selectbox("Sport Model", yes_no_options["Sport Model"])
    if value == "Yes": 
        sport_model = 1
    else:
        sport_model = 0     
with row6[1]:
    value = st.selectbox("Backseat Divider", yes_no_options["Backseat Divider"])
    if value == "Yes": 
        backseat_divider = 1
    else:
        backseat_divider = 0   
with row6[2]:
    value = st.selectbox("Metallic Rim", yes_no_options["Metallic Rim"])
    if value == "Yes": 
        metallic_rim = 1
    else:
        metallic_rim = 0     
with row6[3]:
    value = st.selectbox("Radio Cassette", yes_no_options["Radio Cassette"])
    if value == "Yes": 
        radio_cassette = 1
    else:
        radio_cassette = 0         
with row6[3]:
    value = st.selectbox("Parking Assistant", yes_no_options["Parking Assistant"])
    if value == "Yes": 
        parking_assistant = 1
    else:
        parking_assistant = 0    
with row6[4]:
    value = st.selectbox("Tow Bar", yes_no_options["Tow Bar"])
    if value == "Yes": 
        tow_bar = 1
    else:
        tow_bar = 0        

input_dict = {
    'Age_08_04': age_08_04, 
    'Mfg_Month': mfg_month, 
    'Mfg_Year': mfg_year, 
    'KM': km, 
    'HP': hp, 
    'Met_Color': met_color, 
    'Automatic': automatic, 
    'CC': cc, 
    'Doors': doors, 
    'Gears': gears,
    'Quarterly_Tax': quarterly_tax, 
    'Weight': weight, 
    'Mfr_Guarantee': mfr_guarantee, 
    'BOVAG_Guarantee': bovag_guarantee, 
    'Guarantee_Period': guarantee_period, 
    'ABS': abs, 
    'Airbag_1': airbag_1, 
    'Airbag_2': airbag_2, 
    'Airco': airco, 
    'Automatic_airco': automatic_airco, 
    'Boardcomputer': boardcomputer, 
    'CD_Player': cd_player, 
    'Central_Lock': central_lock, 
    'Powered_Windows': powered_windows, 
    'Power_Steering': power_steering, 
    'Radio': radio, 
    'Mistlamps': mistlamps, 
    'Sport_Model': sport_model, 
    'Backseat_Divider': backseat_divider, 
    'Metallic_Rim': metallic_rim, 
    'Radio_cassette': radio_cassette, 
    'Parking_Assistant': parking_assistant, 
    'Tow_Bar': tow_bar
}    

input_dict.update(fuel_type_dict)
input_dict.update(color_dict)


input_df = pd.DataFrame.from_dict([input_dict])

if st.button('Predict'):
    prediction = predict(input_df)
    st.success(f'Predicted Toyota Corolla Price: €{prediction}')