
import streamlit as st
import streamlit.components.v1 as components

def predict_popu(acousticness, danceability, duration_ms, energy, loudness, speechiness, valence):
    """
    this method is for prediction process 
    takes all the Audio characteristics thtat we used for modelling and returns the prediction 
    """
    prediction = model.predict([[acousticness, danceability, duration_ms, energy, loudness, speechiness, valence]])
    return prediction


def main():
    st.title("Spotify Songs")
     
    html_temp2 = """
        <div style="background-color:royalblue;padding:10px;border-radius:10px">
        <h2 style="color:white;text-align:center;">Spotify Songs</h2>
        <h1 style="color:white;text-align:center;">Popularity prediction</h1>
        </div>
        """
    # a simple html code for heading which is in blue color and we can even use "st.write()" also ut for back ground color i used this HTML ..... 
    #  to render this we use ...
    components.html(html_temp2)
    # components.html() will render the render the 

    st.image("https://cdn2.downdetector.com/static/uploads/logo/Spotify_Logo_RGB_Green.png", width=700, use_column_width=False)

    # this is to insert the image the in the wed app simple <imag/> tag in HTML
    
    #now lets get the test input from the user by wed app 
    # for this we can use "st.text_input()" which allows use to get the input from the user 
    
    acousticness = st.number_input("acousticness", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    danceability = st.number_input("danceability", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    duration_ms = st.number_input("duration_ms", min_value=0, max_value=99999999, value=200000, step=1000)
    energy = st.number_input("energy", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    loudness = st.number_input("loudness", min_value=-60.0, max_value=0.0, value=-10.0, step=0.1)
    speechiness = st.number_input("speechiness", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    valence = st.number_input("valence", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    
    result=""
    # done we got all the user inputs to predict and we need a button like a predict button we do that by "st.button()"
    # after hitting the button the prediction process will go on and then we print the success message by "st.success()"
    if st.button("Predict"):
        result=predict_popu(acousticness,danceability,duration_ms,energy,loudness,speechiness,valence)
        st.success('The Popularity of the song is {}'.format(result))

if __name__=='__main__':
    main()
