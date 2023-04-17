import streamlit as st
import sqlite3
import streamlit_login
import streamlit as st;
from httpx_oauth.clients.google import GoogleOAuth2
import asyncio
import webbrowser
from numpy import void
from pages import After_login;
from streamlit import _RerunData;
from streamlit import _RerunException;
import streamlit as st
from PIL import Image
conn = sqlite3.connect('User.db')
c = conn.cursor()
#st.set_page_config(page_title='Multipage app',layout='wide');


def UserTable_creation():
	c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT,password TEXT)')

def Verify_user(user,pwd):
	c.execute('SELECT * FROM users WHERE username =? AND password = ?',(user,pwd))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM users')
	data = c.fetchall()
	return data
def switch_page(page_name: str):

    from streamlit.source_util import get_pages
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


def main():
	st.title(" Sakhi Web Application");
	image = Image.open('health-wellbeing-womens-health-1024x683.jpg')
	st.image(image, caption='Women Wellness')
	menu = ["Main","SignUp","Login","Google"]
	choice = st.sidebar.selectbox("Menu",menu)
	if choice == "Home":
		st.subheader("Login into Ur Account")
	elif choice == "Login":
		st.subheader("Login Section")
		uname = st.sidebar.text_input("User Name")
		pwd= st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			UserTable_creation()
			if Verify_user(uname,pwd):
				st.success("Login Successfully"+uname);
				#OPEN OR GO TO THE NEW PAGE WHERE U WILL HAVE NEW PAGES HERE AND THEN WE HAVE TO GO TO THAT PAGE.
				# with open("image.png", "rb") as file:
				# 	btn = st.download_button(label="Download image",data=file,file_name="flower.png",mime="image/png");
				# st.success("Image downloaded successfully!!!!!!!!!!!!!!");
				#create a sessio variable we
				st.session_state["login_state"]="SUCCESS";
				#After_login.login_system(uname);
				switch_page('After_login');
			else:
				st.warning("Incorrect Username/Password");
				st.session_state["login_state"] = "FAILED";
	elif choice=="Google":
			st.title("Streamlit Google Login");
			st.write(streamlit_login.get_login_str(), unsafe_allow_html=True)
			st.info("Logged in successfully!!!!!!!!!");

			with open("pages/image.png", "rb") as file:
				btn = st.download_button(label="Download image", data=file, file_name="flower.png", mime="image/png");
			#st.success("Image downloaded successfully!!!!!!!!!!!!!!");
			switch_page('After_login');
			st.balloons();
	elif choice == "SignUp":
		st.subheader("New User Creation")
		nuser = st.text_input("Username");
		npassword = st.text_input("Password",type='password');
		if st.button("Signup"):
			UserTable_creation();
			c.execute('INSERT INTO users(username,password) VALUES (?,?)',(nuser,npassword));
			st.balloons();
			st.info("User Created!!!!!")
			conn.commit();

if __name__ == '__main__':
	#reset the cache...
	st.session_state["login_state"] = "FAILED";
	st.set_page_config(page_title='Multipage app', layout='wide');

	main()
