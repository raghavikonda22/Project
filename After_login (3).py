import streamlit as st;
import toml;
from streamlit import _RerunData
from streamlit import _RerunException
#from streamlit.script_runner import RerunException
from streamlit.source_util import get_pages

def switch_page(page_name: str):
    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")


    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise _RerunException(
                _RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
            )
        )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")
def login_system(uname):
    st.header("welcome to sakhi ");

    col1 , col2 = st.columns(2);
    with col1:
        if(st.button("breast cancer prediction ")):
            switch_page('Cycle_prediction')


    with col2:
        if(st.button("Menstrual Cycle prediction")):
            switch_page('Cycle_prediction')

    if(st.button("logout")):
        st.write("logged out successfully!");
        switch_page("Login_main");
if __name__ == '__main__':
	login_system("Hema");
