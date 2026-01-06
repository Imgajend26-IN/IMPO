import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"


st.markdown(
    """
    <style>
    .stApp {
        background-color: ##e6f2ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Contact App")

# ADD CONTACT FORM
with st.form("add_contact"):
    name = st.text_input("Name")
    number = st.text_input("Number")
    submit = st.form_submit_button("Add Contact", type="primary",use_container_width=True)


    if submit:
        r = requests.post(
            BASE_URL + "/contact/detail",
            json={"name": name, "number": number}
        )
        if r.status_code == 200:
            st.success("Contact Added")
            st.rerun()
        else:
            st.error("Failed")

st.divider()


res = requests.get(f"{BASE_URL}/contacts")
contacts = res.json()


for c in contacts:
    with st.container(border=True):


        new_name = st.text_input("Name",c["name"],key=f"name_{c['id']}")

        new_number = st.text_input("Number", c["number"],key=f"number_{c['id']}")

        col1,col2 = st.columns(2)

    with col1:
        if st.button("update",key=f"update_{c['id']}",type="primary",use_container_width=True):
            requests.put(f"{BASE_URL}/update/{c['id']}",
                         json={"name":new_name,
                               "number": new_number})
            st.success("updated")
            st.rerun()

    with col2: 
        if st.button("delete",key=f"delete_{c['id']}",type="primary",use_container_width=True):
            requests.delete(f"{BASE_URL}/delete/{c['id']}")
            st.success("deleted")
            st.rerun()        