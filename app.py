import streamlit as st
from PIL import Image
st.title("SUPER KAZUMI BROS.")#タイトル入力
st.write("暗号を入力しよう（２回までしか入力できません）")#文入力

user_input = st.text_input("暗号")#テキストボックス挿入取得

submit_btn = st.button("送信")#送信ボタン挿入

image = Image.open("IMG_2167.PNG") 

mistake=Image.open("IMG_2175.PNG") 

if "increment" not in st.session_state:
    st.session_state["increment"] = 0


if submit_btn and user_input=="2315"and st.session_state["increment"]<=2:#送信ボタンを押して暗号が合っていれば
   st.image(image,width=700)#救出画像を表示する
   st.write("ゲーム　クリア！")
   st.write("おめでとう！")
   st.balloons()#風船を飛ばす

elif submit_btn and st.session_state["increment"]==0:#違うとき
     st.image(mistake,width=700)#失敗画像を表示する
     st.session_state["increment"] += 1


elif submit_btn and st.session_state["increment"] >=1:
     st.write("GAMEOVER")




