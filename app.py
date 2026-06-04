import streamlit as st
import pandas as pd
import numpy as np

DATE_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    
    # Renombrado de las columnas en minúsculas
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    
    # Conversión a tipo fecha de la columna 'date/time'
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    
    return data


st.title("Trayectos de Uber en NYC")

st.header('Análisis Exploratorio de datos')
st.subheader('Descripción')

st.text("El conjunto de datos de Uber Pickups registra solicitudes de viajes realizadas en diferentes zonas y horarios de la ciudad, permitiendo analizar patrones de demanda, horas pico, comportamiento de los usuarios y distribución geográfica de los viajes.")

# Crea un elemento de texto e informa al lector que los datos se están cargando.
data_load_state = st.text('Cargando datos...')
# Cargar 10.000 filas de datos en el dataframe.
data = load_data(10000)
# Notifique al lector que los datos se cargaron correctamente.
data_load_state.success('Datos cargados correctamente')

#st.write(data)
if st.checkbox('Mostrar datos'):
    
    st.write(data)

st.subheader('Número de trayectos por hora')

st.text("A continuación se presentan los patrones de movilidad urbana y horas pico de demanda del servicio de transporte.")

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values, x_label="Hora", y_label="Número de Trayectos")

st.text("El punto máximo de trayectos ocurre alrededor de las 17:00, donde se registra la mayor frecuencia de solicitudes de transporte. Esto coincide con las horas de salida laboral y el aumento del tráfico urbano. Después de las 18:00, la cantidad de trayectos empieza a disminuir gradualmente hasta llegar nuevamente a valores bajos durante la noche.")


st.text("El punto máximo de trayectos .. ")

st.subheader('Mapeo geográfico de los trayectos')
st.text("El siguiente mapa muestra la distribución geográfica de los trayectos de Uber en la ciudad, destacando las áreas con mayor actividad y demanda del servicio de transporte.")

st.subheader('Mapeo geográfico ...')
st.text("El siguiente mapa ... ")

st.map(data, zoom=8)

st.text("En el mapa se pueden observar concentraciones significativas de trayectos en áreas como Manhattan, especialmente en zonas cercanas a Times Square, Central Park y el distrito financiero. También se destacan otras áreas con alta actividad, como Brooklyn y Queens, donde se registran numerosos trayectos debido a la densidad poblacional y la demanda de transporte en esas zonas.")

st.text("En el mapa se pueden ... ")

#hour_to_filter = 17
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader(f'Mapeo geográfico de los trayectos a las {hour_to_filter}:00')
st.text(f"El siguiente mapa muestra la distribución geográfica de los trayectos de Uber a las {hour_to_filter}:00, destacando las áreas con mayor actividad durante esa hora específica del día.")

st.map(filtered_data, zoom=8)




