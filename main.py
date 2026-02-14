import streamlit as st
import time
import random
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

# Page Config
st.set_page_config(page_title="Ultimate Valentine 💖", page_icon="💘")

# ---------- Background + Floating Hearts ----------
st.markdown("""
<style>
body {
    background: linear-gradient(to right, #ffe6f2, #fff0f5);
}

/* Floating Hearts */
.heart {
  position: fixed;
  color: #ff4d6d;
  animation: float 6s infinite;
  font-size: 24px;
}

@keyframes float {
  0% { transform: translateY(100vh); opacity: 1; }
  100% { transform: translateY(-10vh); opacity: 0; }
}
</style>

<div class="heart" style="left:10%;">💖</div>
<div class="heart" style="left:30%; animation-delay:2s;">💘</div>
<div class="heart" style="left:50%; animation-delay:4s;">💗</div>
<div class="heart" style="left:70%; animation-delay:1s;">💓</div>
<div class="heart" style="left:90%; animation-delay:3s;">💕</div>
""", unsafe_allow_html=True)

# ---------- Background Music ----------
st.markdown("""
<audio autoplay loop>
  <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.title("💖 Happy Valentine's Day 💖")
st.write("---")

name = st.text_input("Enter your special person's name ❤️")

# ---------- Typing Animation ----------
def type_writer(text):
    placeholder = st.empty()
    typed = ""
    for char in text:
        typed += char
        placeholder.markdown(f"<h3 style='color:#ff4d6d'>{typed}</h3>", unsafe_allow_html=True)
        time.sleep(0.03)

if st.button("💌 Show Love Message"):
    if name:
        message = f"""
Dear {name},
BUJJI,
Nee siricha podhu enaku ellam marandhuruvaen…
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
NIDHA ENODA UYIRE ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️


Happy Valentine’s Day ❤️
        """
        type_writer(message)
        st.balloons()
    else:
        st.error("Please enter a name ❤️")

st.write("---")

# ---------- Funny Moving No Button ----------
st.subheader("Will you be my Valentine? 💍")

col1, col2 = st.columns(2)

with col1:
    if st.button("YES 💖"):
        st.success("YAYYYY!!! You made my heart explode with happiness 😍💘")
        st.balloons()

with col2:
    no_position = random.randint(0, 100)
    st.markdown(f"""
        <div style="position:relative; left:{no_position}px;">
        </div>
    """, unsafe_allow_html=True)
    st.button("No 😜")

st.write("---")

# ---------- PDF Love Letter Generator ----------
def create_pdf(name):
    file_name = "love_letter.pdf"
    doc = SimpleDocTemplate(file_name)
    elements = []

    styles = getSampleStyleSheet()
    style = styles["Normal"]

    text = f"""
    Dear {name},
    BUJJI,
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
NIDHA ENODA UYIRE ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️
    """

    elements.append(Paragraph(text, style))
    elements.append(Spacer(1, 0.5 * inch))
    doc.build(elements)

    return file_name

if st.button("🌹 Download Love Letter as PDF"):
    if name:
        pdf_file = create_pdf(name)
        with open(pdf_file, "rb") as f:
            st.download_button("Click to Download 💌", f, file_name="Love_Letter.pdf")
    else:
        st.error("Enter name first ❤️")

st.write("---")
st.caption("Made with ❤️✨")
