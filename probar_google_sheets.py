
import streamlit as st
import gspread

# 1. Leer las credenciales privadas
credenciales = dict(st.secrets["gcp_service_account"])

# 2. Autenticar la cuenta de servicio
cliente = gspread.service_account_from_dict(credenciales)

# 3. Abrir la hoja de cálculo
url = st.secrets["sheet_url"]
hoja = cliente.open_by_url(url).sheet1

# 4. Mostrar los encabezados existentes
encabezados = hoja.row_values(1)

print("CONEXIÓN EXITOSA CON GOOGLE SHEETS")
print("Nombre de la hoja:", hoja.title)
print("Encabezados:", encabezados)
