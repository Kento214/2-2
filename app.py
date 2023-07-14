import streamlit as st
import streamlit.components.v1 as stc
import base64
import time
from PIL import Image
st.title("SUPER KAZUMI BROS.")#タイトル入力
st.write("暗号を入力しよう（２回までしか入力できません）")#文入力

user_input = st.text_input("暗号")#テキストボックス挿入取得

submit_btn = st.button("送信")#送信ボタン挿入

image = Image.open("IMG_2167.PNG") 

mistake=Image.open("IMG_2175.PNG") 

if "increment" not in st.session_state:
    st.session_state["increment"] = 0


if submit_btn and user_input=="2315"and st.session_state["increment"]<2:#送信ボタンを押して暗号が合っていれば
   audio_path1 = "Clear.mp3"

   audio_placeholder = st.empty()

   file_= open(audio_path1,"rb")
   contents = file_.read()
   file_.close()

   audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
   audio_html = """ <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not supprt the audio element.
                    </audio>
                 """ %audio_str   
   audio_placeholder.empty()
   time.sleep(0.5)
   audio_placeholder.markdown(audio_html,unsafe_allow_html=True)
    
   st.image(image,use_column_width=True)#救出画像を表示する
   st.write("ゲーム　クリア！")
   st.write("おめでとう！")
   st.balloons()#風船を飛ばす

elif submit_btn and st.session_state["increment"]==0:#違うとき
     audio_path1 = "Missed.mp3"

     audio_placeholder = st.empty()

     file_= open(audio_path1,"rb")
     contents = file_.read()
     file_.close()

     audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
     audio_html= """ <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not supprt the audio element.
                    </audio>
                 """ %audio_str   
     audio_placeholder.empty()
     time.sleep(0.5)
     audio_placeholder.markdown(audio_html,unsafe_allow_html=True)

    
     st.image(mistake,use_column_width=True)#失敗画像を表示する
     st.session_state["increment"] += 1


elif submit_btn and st.session_state["increment"] >=1:
     audio_path1 = "Missed.mp3"

     audio_placeholder = st.empty()

     file_= open(audio_path1,"rb")
     contents = file_.read()
     file_.close()

     audio_str = "data:audio/ogg;base64,%s"%(base64.b64encode(contents).decode())
     audio_html= """ <audio autoplay=True>
                    <source src="%s" type="audio/ogg" autoplay=True>
                    Your browser does not supprt the audio element.
                    </audio>
                 """ %audio_str   
     audio_placeholder.empty()
     time.sleep(0.5)
     audio_placeholder.markdown(audio_html,unsafe_allow_html=True)

     
     st.write("GAMEOVER")
     st.session_state["increment"] += 1




