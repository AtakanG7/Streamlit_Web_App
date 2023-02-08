import streamlit as st
from sumapi.api import SumAPI

#removing unnecessary objects, decorating and adjusting!
st.markdown(""" 



<header class="header0">Summarify</header>
<a  href="https://summarify.io/"><button class="a0">Summarify</button></a>

<style>

.block-container.css-12oz5g7.egzxvld2 {
    box-sizing: unset;
} 

    .css-k3w14i
    {
        display: flex;
        margin-left: 400px;
        font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    }
    
    .block-container.css-12oz5g7.egzxvld2
    {
       
        box-sizing:unset;
    }
    
    
    
    
    .css-k3w14i.effi0qh3
    {
    flex: 100px;
    margin-left:0px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .st-bc.st-b3.st-bd.st-b8.st-be.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b1.st-bn.st-au.st-ax.st-av.st-aw.st-ae.st-af.st-ag.st-ah.st-ai.st-aj.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu
    {
    margin-left:0px;
    }
    
    
    
    
  
    
    .css-1avcm0n
    {
       background-color: rgba(190, 37, 37, 0.068);
    }
    
    
    .header0
    {
        border-radius: 0px;
    background-color:#007bff00;
    width: 400px;
    background-size: 100px;
    font-size: 65px;
    color: rgb(146, 146, 146);
    text-align:center;
    border-radius: 10px;
    transition: background 0.1s, color 0.1s;
    cursor: pointer;
    text-transform: capitalize;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    }
    :hover.header0{
        color: rgb(101, 101, 101);
        
    
    }
    
    
    
   
    
    .a0{
    
    margin-left: 160px;
    margin-top:10px;
    background-color: rgb(26, 39, 184);
    margin-top: -100px;
    color: rgb(255, 255, 255);
    border: 20px;
    transition: background 0.1s, color 1s;
    border-radius: 10px;
    }
    
    :hover.a0
    {
    border-style:inherit;  
    border-color: #fe0606;
    background-color: rgb(255, 255, 255);
    color: #007bff;
    }
    
    
    
    
    .css-1lsmgbg.egzxvld0
    {
        visibility: hidden;
    }
    
    .css-14xtw13.e8zbici0
    {
        visibility: hidden;
    }
    
    .css-1n76uvr.e1tzin5v0
    {
        width: 1000;
    }
    .css-ffhzg2 
    {
    background:  #ff0000f7;
       
    }
    .css-10trblm.e16nr0p30
    {
    margin-top: 30px;
    margin-left: 50px;
    font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
    color : rgb(241, 94, 94)
    }
    .css-k3w14i.effi0qh3
    {
    font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
    }
    .block-container.css-91z34k.egzxvld4{
     box-sizing:unset;
    }
    
    .css-1n76uvr.e1tzin5v0
    {
    margin-left: 400px;
    }
    .css-1v0mbdj{
        margin-left:50px;
        transition: all 0.1s;
    }
    .p,.ol,.ul,.dl{
        font-family:'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
        color: #fe0606;
        font-weight: bold;
        
    }
    .css-ffhzg2{
        background-color: #239bb970;
    }

    
    </style>
    
    
""",unsafe_allow_html=True)

api = SumAPI(username='test', password='5Br5Yhdu4fS87C')
st.write("---")
st.title("Emotion Detection")
st.empty()

user_input = st.text_input("Write down your text...", key="input")

answer_to_input = api.sentiment_analysis(user_input, domain='general')

st.write(answer_to_input)
st.write("Answer image representation:")



if "Pozitif" == answer_to_input['evaluation']['label']:
    st.image("https://www.pngmart.com/files/12/Gradient-Great-Job-Emoji-PNG-Photo.png","Positive",width=100)
elif "Negatif" == answer_to_input['evaluation']['label']:
    st.image("https://creazilla-store.fra1.digitaloceanspaces.com/emojis/55893/angry-face-emoji-clipart-xl.png","Negative",width=100)
elif "Nötr" == answer_to_input['evaluation']['label']:
    st.image("https://cdn.pixabay.com/photo/2020/12/19/03/01/emoji-5843458_640.png","Nötr",width=100)
else:
   st.image("https://hotemoji.com/images/dl/1/blank-face-emoji-by-google.png")         



