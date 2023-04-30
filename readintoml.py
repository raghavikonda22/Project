import toml

# toml_dict = toml.loads(toml_string)  # Read from a string
import streamlit as st;
bgcolor=st.color_picker("chosse the bakground color u need ");
print(bgcolor);
input_file_name = "pages/.streamlit/config.toml"
with open(input_file_name,'r+') as toml_file:
    toml_dict = toml.load(toml_file)
    toml_dict['theme']['backgroundColor']=bgcolor;
    toml.dump(toml_dict,toml_file);
    print(toml_dict);
