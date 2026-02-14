import streamlit as st
import random
import time

# Page settings
st.set_page_config(page_title="Valentine Page", page_icon="❤️", layout="centered")

# Title
st.markdown(
    "<h1 style='text-align:center; color:#ff4b6e;'>💖 Happy Valentine’s Day 💖</h1>",
    unsafe_allow_html=True
)

st.write("")

# Message
st.markdown(
    "<h3 style='text-align:center;'>You are special, loved, and appreciated ❤️</h3>",
    unsafe_allow_html=True
)
st.write("")

# Button interaction
if st.button("Click for a Surprise 💌"):
    messages = [
        
   """ BUJJI,
En life la irukardhuku thanks bujji
Un presence dhaan enakku biggest happiness… ❤️
Innum neraya memories create pannalaam nama.
nama life happy ya epovu vachukanu ethana
sanda vadhalum adha apove seri paniranu 
ni en chloo,pattu,vairoo,thagoo,bujji,alagupulla,baby,darling.
Unna paatha udane smile automatic-ah varudhu…
Adhanala dhaan nee enakku romba special… ❤️ ❤️
Nee siricha podhu enaku ellam marandhuruvaen…
aproo,
Nee message panna udane en mood change aagidum… ❤️
aproo,
Love-na enna nu theriyadhu… ❤️
Aana un kooda irukka romba pidikkum… adhu podhum.
LOVE YOU SOO MUCH THAGAMEYYY
NIDHA ENODA UYIRE ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️"""]
    
    st.success(random.choice(messages))

# Heart animation (simple effect)
st.write("")
if st.button("Send Hearts ❤️"):
    placeholder = st.empty()
    for i in range(10):
        hearts = " ".join(["❤️" for _ in range(random.randint(5,15))])
        placeholder.markdown(
            f"<h2 style='text-align:center;'>{hearts}</h2>",
            unsafe_allow_html=True
        )
        time.sleep(0.3)

# Footer
st.write("")
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ </p>",
    unsafe_allow_html=True
)

