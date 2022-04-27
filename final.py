import numpy as np
import pickle
import streamlit as st


st.title('HEART DISEASE PREDICTION')

loaded_model = pickle.load(open('Heartmodel.pkl', 'rb'))

def heart(input_data):

    input_data_as_numpy_array = np.asarray(input_data)
    input_reshape = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_reshape)
   



    if (prediction[0]==0):
        return st.success('This person has less chance of heart attack')
    else:
        return st.error('This person has more chance of heart attack')


def main():

    nav = st.sidebar.selectbox("Navigation",["Home","Predict"])
    if nav == "Home":
        st.write("Home")
        st.image("predict-heart-disease.jpg")


    

    if nav == "Predict":
        st.write("Pridiction  Model")
    
     
        Age = st.number_input("Enter your Age ", step = 2)
        #st.write(Age)

        sex = st.radio("Select Gender: ", ('1', '0'))
        if (sex == '1'):
            st.info("Male")
        else:
            st.info("Female")
        
        Height = st.number_input("Enter your height ", step = 2)
        #st.write(Height)

        Weight = st.number_input("Enter Weight in Kg", step = 2)
        #st.write(Weight)

        SBP = st.number_input("Enter systolic blood pressure", step = 2)
        #st.write(SBP)

        DBP = st.number_input("Enter Dystolic blood pressure", step = 2)
        #st.write(DBP)

        Cholestrol = st.selectbox(" cholestrol Level( 1 = cholestrol_Normal, 2 = cholestrol_above_normal, 3 = cholestrol_excess)" ,["1", "2","3"])
        #st.write(Cholestrol)
        if Cholestrol == "1":
            Cholestrol1 = 1
            Cholestrol2 = 0
        elif Cholestrol == "2":
            Cholestrol1 = 0
            Cholestrol2 = 1
        elif Cholestrol == "3":
            Cholestrol1 = 0
            Cholestrol2 = 0
            

        Glucose = st.selectbox(" Glucose Level( 1 = Glucose_Normal, 2 = Glucose_above_normal, 3 = Glucose_excess)" ,["1", "2","3"])
        #st.write(Glucose)
        if Glucose == "1":
            Glucose1 = 1
            Glucose2 = 0
        elif Glucose == "2":
            Glucose1 = 0
            Glucose2 = 1
        elif Glucose == "3":
            Glucose1 = 0
            Glucose2 = 0
        


        Smoking = st.selectbox(" Smoking ( 0 = Not smoking, 1 = Smoking)" ,["0", "1"])
        #st.write(Smoking)

        Alchohol = st.selectbox(" Alchohol ( 0 = Not taking Alchohol, 1 = taking Alchohol)" ,["0", "1"])
        #st.write(Alchohol)


        Activity = st.selectbox(" Activity ( 0 = Not Doing physical Activity, 1 = Doing physical Activity)" ,["0", "1"])
        #st.write(Activity)


        

        diagnosis = ''
    
        
        if st.button('PREDICT'):
            diagnosis = heart([Age,sex,Height,Weight,SBP,DBP,Cholestrol1,Cholestrol2,Glucose1,Glucose2,Smoking,Alchohol,Activity])
            
 
    
  
if __name__ == '__main__':
    main()  