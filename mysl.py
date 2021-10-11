# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""An example of showing geographic data."""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk
from PIL import Image
import urllib.request
urllib.request.urlretrieve('https://github.com/Yailertpai/YaiHW/blob/main/ooo.jpg?raw=true', "sample.png")
picture = Image.open("sample.png")
st.set_page_config(layout="wide")
st.image(picture,use_column_width=True)


# SETTING PAGE CONFIG TO WIDE MODE
st.title("Dhakorn Lertpaithoon 6130805621")
st.title("Homework_Geodatasci")
##################################################################################
###########################################################################################

# LAYING OUT THE TOP SECTION OF THE APP


Day = st.selectbox("please choose the DAY",("1/1/2019", "2/1/2019","3/1/2019","4/1/2019","5/1/2019"))
hour_selected = st.slider("Select hour of travelling🚘", 0, 23)
st.sidebar.markdown("Selection Hour🚙") 


st.write(
    """
    ##
    This web is show about  the number of the travelling start 
    This web was designed that you can adjust the time that you want to check it! by sliding tab bar  
    """) 


timedisplay = "Selected Day : " + Day
st.title(timedisplay)


# LOADING DATA
DATE_TIME = "date/time"
data_1 = ("https://raw.githubusercontent.com/Maplub/odsample/master/20190101.csv")
data_2 = ("https://raw.githubusercontent.com/Maplub/odsample/master/20190102.csv")
data_3= ("https://raw.githubusercontent.com/Maplub/odsample/master/20190103.csv")
data_4 = ("https://raw.githubusercontent.com/Maplub/odsample/master/20190104.csv")
data_5 = ("https://raw.githubusercontent.com/Maplub/odsample/master/20190105.csv")

#SELECT DATA ACCORDING TO Day
if Day == "1/1/2019" :
  DATA_URL = data_1
elif Day == "2/1/20199" :
  DATA_URL = data_2
elif Day == "3/1/2019" :
  DATA_URL = data_3
elif Day == "4/1/2019" :
  DATA_URL = data_4
elif Day == "5/1/2019" :
  DATA_URL = data_5

@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data = data[['timestart','latstartl','lonstartl']].copy()
    data = data.rename(columns = {'timestart': 'Date/Time', 'latstartl': 'Lat', 'lonstartl': 'Lon'}, inplace = False)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data


data = load_data(100000)

##################################################################################
##################################################################################
# CREATING FUNCTION FOR MAPS

def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,                                                         
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))
    
##################################################################################
##################################################################################
# FILTERING DATA BY HOUR SELECTED
data = data[(data[DATE_TIME].dt.hour == hour_selected) & (data[DATE_TIME].dt.year == 2019)]


# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
zoom_level = 11
#midpoint1 = (np.average(data1["lat"]), np.average(data1["lon"]))
#midpoint2 = (np.average(data2["lat"]), np.average(data2["lon"]))
midpoint = [13.736717, 100.523186]

st.write("**check time that you want to travelling**")
map(data, midpoint[0], midpoint[1], zoom_level)


# FILTERING DATA FOR THE HISTOGRAM
filtered = data[
    (data[DATE_TIME].dt.hour >= hour_selected) & (data[DATE_TIME].dt.hour < (hour_selected + 1))
    ]

hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]

chart_data = pd.DataFrame({"minute": range(60), "travelling started": hist})

# LAYING OUT THE HISTOGRAM SECTION
st.write("")

st.write("**The moment the car runs on the road %i:00 and %i:00** 🚒" % (hour_selected, (hour_selected + 1) % 24))

st.altair_chart(alt.Chart(chart_data)
    .mark_area(
        interpolate='step-after',
    ).encode(
        x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
        y=alt.Y("travelling started:Q"),
        tooltip=['minute', 'travelling started']
    ).configure_mark(
        opacity=1,
        color='indigo'
    ), use_container_width=True)

st.write("THANK YOU FOR COME TOO SEE MY WEB😛")
import urllib.request
urllib.request.urlretrieve('https://github.com/Yailertpai/YaiHW/blob/main/8989.jpg?raw=true', "8989.png")
picture2 = Image.open("8989.png")

st.image(picture2,use_column_width=True)
