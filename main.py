import streamlit as st

st.write(">#*H1 title*")
st.metric(label="Car speed",value="20m/s", delta="1.2%")

st.image("img.webp", caption="Gojo Satoru")
state = st.checkbox("Subscribe")
if state:
    st.write("Subscribed!")
def clicked():
        st.write("Thank you!")
btn = st.button("Like", on_click=clicked)
select = st.selectbox("How old are you?", options= {1,2,3,4})

radio_btn = st.radio("Interest",options={"Football","basketball","Volleyball"},key="interest")
if st.session_state.interest =="Football":
      st.write("So, you like football?")
multi_select = st.multiselect("What is your fav song?",options={"sadf","sdf","saw"})
upload = st.file_uploader("Please upload an image", type="webp")
