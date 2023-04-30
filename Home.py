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
    st.header("Welcome to Sakhi ");
    #create a logout button at this point;
    # with open("pages/image.png", "rb") as file:
    #     btn = st.download_button(label="Download image",data=file,file_name="flower.png",mime="image/png");
    # #adding the colour picker to it.
    # bgcolor = st.color_picker("chosse the bakground color u need ",value="#FFFAFA");
    # print(bgcolor);
    # input_file_name = ".streamlit/config.toml"
    # with open(input_file_name, 'r') as toml_file:
    #     toml_dict = toml.load(toml_file)
    #     toml_dict['theme']['backgroundColor'] = bgcolor;
    # toml_file.close();
    #
    # f = open(".streamlit/config.toml", 'w')
    # toml.dump(toml_dict, f)
    # f.close()
    #
    # print(toml_dict);
    # if 'n_rows' not in st.session_state:
    #     st.session_state.n_rows = 1
    #
    # add = st.button(label="+")
    # sub = st.button(label="-")
    # if add:
    #     st.session_state.n_rows += 1
    #     st.experimental_rerun()
    # if sub:
    #     if st.session_state.n_rows>0:
    #         st.session_state.n_rows -= 1
    #         st.experimental_rerun()
    #     else:
    #         st.warning("all the text boxes were deleted")
    #
    # for i in range(st.session_state.n_rows):
    #     # add text inputs here
    #     st.text_input(label="TextBox "+str(i), key=i)  # Pass index as key

    col1 , col2 = st.columns(2);
    with col1:
        if(st.button("Predict breast cancer")):
            switch_page('Breast_cancer');
    with col2:
        if(st.button("Predict menstrual cycle")):
            switch_page('menstrualcycle');
    # else:
    #     Login_main.main();
    # if (st.button("change color")):
    #     switch_page("After_login");
    if(st.sidebar.button("Logout")):
        st.write("Logout successfully!");
        switch_page("Home");
if __name__ == '__main__':
	login_system("Hema");