import streamlit as st
import numpy as np
import pandas as pd
import pickle
rad=st.sidebar.radio("Navigation",['Home','Breast Cancer Prediction','Lung Cancer Prediction'])
if rad=='Home':
    st.title("Welcome to Cancer Detection App")
    #st.image("aa.png")
    st.write('Cancer is one of the leading causes of death worldwide, accounting for almost 10 million deaths in 2020. In the same year, over 19 million new cases of cancer were diagnosed. The global cancer burden can be reduced by implementing strategies for prevention complemented with early detection and efficient treatment approaches. Cancer comprises a heterogeneous group of diseases that result from the interaction between individual genetic susceptibility factors and environmental carcinogens of physical, chemical, and infectious nature.')
    st.write('The use of ML to analyze cancer microbiome data shows that it has the potential to aid in the development of new strategies for cancer detection and prevention, possibly finding new relationships unknown yet and ultimately reducing the burden of the disease.')
if rad=='Breast Cancer Prediction':
    #st.image('bc.jpeg')
    st.title("BREAST CANCER PREDICTION")
    data=[]
    s1,s2,s3,s4,s5,s6,s7,s8,s9,s10=st.columns(10)
    a1=s1.text_input("Enter Mean Radius:",value='0')
    a2=s2.text_input("Enter Mean Texture:",value='0')
    a3=s3.text_input("Enter Mean Perimeter:",value='0')
    a4=s4.text_input("Enter Mean Area:",value='0')
    a5=s5.text_input("Enter Mean Smoothness:",value='0')
    a6=s6.text_input("Enter Mean Compactness:",value='0')
    a7=s7.text_input("Enter Mean Concavity:",value='0')
    a8=s8.text_input("Enter Mean Concave Points:",value='0')
    a9=s9.text_input("Enter Mean Symmetry:",value='0')
    a10=s10.text_input("Enter Mean Fractal Dimension:",value='0')

    s11,s12,s13,s14,s15,s16,s17,s18,s19,s20=st.columns(10)
    a11=s11.text_input("Enter Radius Error:",value='0')
    a12=s12.text_input("Enter Texture Error:",value='0')
    a13=s13.text_input("Enter Perimeter Error:",value='0')
    a14=s14.text_input("Enter Area Error:",value='0')
    a15=s15.text_input("Enter Smoothness Error:",value='0')
    a16=s16.text_input("Enter Compactness Error:",value='0')
    a17=s17.text_input("Enter Concavity Error:",value='0')
    a18=s18.text_input("Enter Concave Point Error:",value='0')
    a19=s19.text_input("Enter Symmetry Error:",value='0')
    a20=s20.text_input("Enter Fractal Dimension Error:",value='0')

    s21,s22,s23,s24,s25,s26,s27,s28,s29,s30=st.columns(10)
    a21=s21.text_input("Enter Worst Radius:",value='0')
    a22=s22.text_input("Enter Worst Texture:",value='0')
    a23=s23.text_input("Enter Worst Perimeter:",value='0')
    a24=s24.text_input("Enter Worst Area:",value='0')
    a25=s25.text_input("Enter Worst Smoothness:",value='0')
    a26=s26.text_input("Enter Worst Compactness:",value='0')
    a27=s27.text_input("Enter Worst Concavity:",value='0')
    a28=s28.text_input("Enter Worst Concave Point:",value='0')
    a29=s29.text_input("Enter Worst Symmetry:",value='0')
    a30=s30.text_input("Enter Worst Fractal Dimension:",value='0')

    if st.button("Predict"):
        data.append(float(a1))
        data.append(float(a2))
        data.append(float(a3))
        data.append(float(a4))
        data.append(float(a5))
        data.append(float(a6))
        data.append(float(a7))
        data.append(float(a8))
        data.append(float(a9))
        data.append(float(a10))

        data.append(float(a11))
        data.append(float(a12))
        data.append(float(a13))
        data.append(float(a14))
        data.append(float(a15))
        data.append(float(a16))
        data.append(float(a17))
        data.append(float(a18))
        data.append(float(a19))
        data.append(float(a20))

        data.append(float(a21))
        data.append(float(a22))
        data.append(float(a23))
        data.append(float(a24))
        data.append(float(a25))
        data.append(float(a26))
        data.append(float(a27))
        data.append(float(a28))
        data.append(float(a29))
        data.append(float(a30))
        
        d1=np.array(data).reshape(1,30)
        sc1=pickle.load(open(r'C:\Users\abhin\MACHINE LEARNING\ML_PROJECTS\Breast Cancer Prediction\scale.pkl','rb'))
        ty=sc1.transform(d1)
        import pickle
        
        # load model
        breast_cancer_detector_model = pickle.load(open(r'C:\Users\abhin\MACHINE LEARNING\ML_PROJECTS\Breast Cancer Prediction\breast_cancer_detector.pickle', 'rb'))
        
        # predict the output
        y_pred = breast_cancer_detector_model.predict(ty)
        #predd=st.write(y_pred[0])
        if y_pred==0.0:
            st.write("No Cancer")
            st.balloons()
        else:
            st.write("Cancer")
if rad=='Lung Cancer Prediction':
    #st.image('lc.jpeg')
    st.title("Lung CANCER PREDICTION")
    data1=[]
    st.write("Enter 1 for 'YES' and 0 for 'NO' ONLY")
    s1,s2,s3,s4=st.columns(4)
    a1=s1.text_input("Yellow Fingers:",value='0')
    a2=s2.text_input("Anxiety:",value='0')
    a3=s3.text_input("Peer_Pressure:",value='0')
    a4=s4.text_input("Chronic Disease:",value='0')
    s5,s6,s7,s8=st.columns(4)
    a5=s5.text_input("Fatigue:",value='0')
    a6=s6.text_input("Allergy:",value='0')
    a7=s7.text_input("Wheezing:",value='0')
    a8=s8.text_input("Alcohol Consumption:",value='0')
    s9,s10,s11=st.columns(3)
    a9=s9.text_input("Coughing:",value='0')
    a10=s10.text_input("Swallowing Difficulty:",value='0')
    a11=s11.text_input("Chest Pain:",value='0')

    if st.button("Predict"):
        data1.append(float(a1))
        data1.append(float(a2))
        data1.append(float(a3))
        data1.append(float(a4))
        data1.append(float(a5))
        data1.append(float(a6))
        data1.append(float(a7))
        data1.append(float(a8))
        data1.append(float(a9))
        data1.append(float(a10))
        data1.append(float(a11))
        d1=np.array(data1).reshape(1,11)
        # load model
        lung_cancer_detector_model = pickle.load(open(r'C:\Users\abhin\MACHINE LEARNING\ML_PROJECTS\Breast Cancer Prediction\lung_cancer_detector.pickle', 'rb'))
        
        # predict the output
        y_pred = lung_cancer_detector_model.predict(d1)
        #predd=st.write(y_pred[0])
        if y_pred==0:
            st.write("No Cancer")
            st.balloons()
        else:
            st.write("Cancer")
        
        

        
        

