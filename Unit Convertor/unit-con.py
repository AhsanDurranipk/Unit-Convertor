import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

def convert_units(value, from_unit, to_unit):
    try:
        result = (value * ureg(from_unit)).to(to_unit)
        return result.magnitude
    except Exception as e:
        return f"Error: {e}"

# Streamlit UI
st.title("🔄 Professional Unit Converter")
st.subheader("By Ahsan Durrani")
st.write("Convert between different units effortlessly!")

# Dropdown categories
categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day"],
    "Area": ["square meter", "square kilometer", "square foot", "square inch", "acre", "hectare"],
    "Volume": ["liter", "milliliter", "cubic meter", "gallon", "pint"],
    "Speed": ["meter per second", "kilometer per hour", "mile per hour", "knot"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt hour"],
    "Pressure": ["pascal", "bar", "atmosphere", "torr", "psi"],
    "Data Storage": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]
}

category = st.selectbox("Select a category", list(categories.keys()))
from_unit = st.selectbox("From Unit", categories[category])
to_unit = st.selectbox("To Unit", categories[category])
value = st.number_input("Enter value", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result} {to_unit}")