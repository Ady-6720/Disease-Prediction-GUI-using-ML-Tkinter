{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a68ae4bb-f00a-4b17-b662-a3a3d81e008c",
   "metadata": {},
   "source": [
    "<h1>Disease Prediction & Gui using ML & Tkinter<h1>\n",
    "    <h4>Project by: Aditya D Malode<h4>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 501,
   "id": "69244819-2c14-42e6-a7f5-e38a5cf665a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: tk in c:\\users\\aditya\\anaconda3\\lib\\site-packages (0.1.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install tk"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dc8326d-eb5c-4b93-aa24-4e27f9b3dcb9",
   "metadata": {},
   "source": [
    "<h2>Importing Important & Required Libraries<h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 502,
   "id": "9b709961-0a43-47d8-8c13-600350dfe4e1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from tkinter import *\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from PIL import ImageTk, Image  "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8716d507-04fe-4ed5-ba30-e247ac5e2fb5",
   "metadata": {},
   "source": [
    "<h2>List Of Symptoms<h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 503,
   "id": "9476a231-33b1-43b7-89f8-fca42b724f3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',\n",
    "'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',\n",
    "'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',\n",
    "'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',\n",
    "'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',\n",
    "'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',\n",
    "'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',\n",
    "'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',\n",
    "'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',\n",
    "'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',\n",
    "'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',\n",
    "'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',\n",
    "'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',\n",
    "'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',\n",
    "'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',\n",
    "'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',\n",
    "'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',\n",
    "'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',\n",
    "'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',\n",
    "'yellow_crust_ooze']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc7b1433-763a-49e5-a8ea-8b4a648bdaa3",
   "metadata": {},
   "source": [
    "<h2>List Of Disease<h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 504,
   "id": "1f54ae85-8f67-4746-89ec-6c14ad8c790a",
   "metadata": {},
   "outputs": [],
   "source": [
    "disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',\n",
    "'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',\n",
    "' Migraine','Cervical spondylosis',\n",
    "'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',\n",
    "'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',\n",
    "'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',\n",
    "'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',\n",
    "'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',\n",
    "'Impetigo']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 505,
   "id": "7f8e1dfd-1352-4a4d-a22d-a378e55a2edc",
   "metadata": {},
   "outputs": [],
   "source": [
    "l2=[]\n",
    "for x in range(0,len(l1)):\n",
    "    l2.append(0)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ea196bb-06c2-459f-9514-22dc2f961397",
   "metadata": {},
   "source": [
    "<h2>Reading Training Dataset<h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 506,
   "id": "b6e8d811-05df-48b1-b1cd-64a4c714d26d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(\"Training.csv\")\n",
    "\n",
    "df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 507,
   "id": "8c7c99da-4131-4d20-b2b2-178d7d4ac535",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  0,  0, ..., 38, 39, 40], dtype=int64)"
      ]
     },
     "execution_count": 507,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X= df[l1]\n",
    "\n",
    "y = df[[\"prognosis\"]]\n",
    "np.ravel(y)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "58731a8c-8da9-450c-af43-f3deda3bec45",
   "metadata": {},
   "source": [
    "<h2>Reading Testing Dataset<h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 508,
   "id": "6616d14c-9882-4391-a7c6-eb332120387b",
   "metadata": {},
   "outputs": [],
   "source": [
    "tr=pd.read_csv(\"Testing.csv\")\n",
    "tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,\n",
    "'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,\n",
    "'Migraine':11,'Cervical spondylosis':12,\n",
    "'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,\n",
    "'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,\n",
    "'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,\n",
    "'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,\n",
    "'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,\n",
    "'Impetigo':40}},inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 509,
   "id": "57f0da57-3bcf-43e4-b8e9-70735bf523e9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,\n",
       "       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,\n",
       "       34, 35, 36, 37, 38, 39, 40], dtype=int64)"
      ]
     },
     "execution_count": 509,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test= tr[l1]\n",
    "y_test = tr[[\"prognosis\"]]\n",
    "np.ravel(y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fe10387a-01df-42f7-b19a-d944b4bb7c60",
   "metadata": {},
   "source": [
    "<h1>Function to conclude major disease<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 510,
   "id": "f0ae56d1-daeb-45c2-92f4-a3cf6db075de",
   "metadata": {},
   "outputs": [],
   "source": [
    "def MainConclusion():\n",
    "\n",
    "    from sklearn import tree\n",
    "\n",
    "    clf3 = tree.DecisionTreeClassifier()   \n",
    "    clf3 = clf3.fit(X,y)\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=clf3.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "    for k in range(0,len(l1)):\n",
    "        # print (k,)\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "    inputtest = [l2]\n",
    "    predict = clf3.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "    if (h=='yes'):\n",
    "        t1.delete(\"1.0\", END)\n",
    "        t1.insert(END, disease[a])\n",
    "    else:\n",
    "        t1.delete(\"1.0\", END)\n",
    "        t1.insert(END, \"No Conclusion ! Cunsult a Doctor!\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6535d2c0-3e0b-4062-8185-955764ee334a",
   "metadata": {},
   "source": [
    "<h1>Function to conclude other disease that can be possible<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 511,
   "id": "6c4b3737-8227-4d0a-8668-81ece95bc130",
   "metadata": {},
   "outputs": [],
   "source": [
    "def SecondaryConslusion():\n",
    "    from sklearn.ensemble import RandomForestClassifier\n",
    "    clf4 = RandomForestClassifier()\n",
    "    clf4 = clf4.fit(X,np.ravel(y))\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=clf4.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = clf4.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "\n",
    "    if (h=='yes'):\n",
    "        t2.delete(\"1.0\", END)\n",
    "        t2.insert(END, disease[a])\n",
    "    else:\n",
    "        t2.delete(\"1.0\", END)\n",
    "        t2.insert(END, \"No Conclusion ! Cunsult a Doctor!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 512,
   "id": "ab4b1de9-da80-4068-87e8-51ffc596b539",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Major():\n",
    "    from sklearn.naive_bayes import GaussianNB\n",
    "    gnb = GaussianNB()\n",
    "    gnb=gnb.fit(X,np.ravel(y))\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    y_pred=gnb.predict(X_test)\n",
    "    print(accuracy_score(y_test, y_pred))\n",
    "    print(accuracy_score(y_test, y_pred,normalize=False))\n",
    "    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]\n",
    "    for k in range(0,len(l1)):\n",
    "        for z in psymptoms:\n",
    "            if(z==l1[k]):\n",
    "                l2[k]=1\n",
    "\n",
    "    inputtest = [l2]\n",
    "    predict = gnb.predict(inputtest)\n",
    "    predicted=predict[0]\n",
    "    h='no'\n",
    "    for a in range(0,len(disease)):\n",
    "        if(predicted == a):\n",
    "            h='yes'\n",
    "            break\n",
    "    if (h=='yes'):\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, disease[a])\n",
    "    else:\n",
    "        t3.delete(\"1.0\", END)\n",
    "        t3.insert(END, \"No Conclusion ! Cunsult a Doctor!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "86d3ce68-1c0e-46ab-b599-76d1dae042b7",
   "metadata": {},
   "source": [
    "<h1>Configuring Visual Appearance for the Interface<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 513,
   "id": "2c26a453-497d-4aae-8656-4e7995ffde39",
   "metadata": {},
   "outputs": [],
   "source": [
    "root = Tk()\n",
    "root.configure(background = 'AntiqueWhite1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 514,
   "id": "72c35146-4de8-4efe-8750-4c6c38753246",
   "metadata": {},
   "outputs": [],
   "source": [
    "Symptom1 = StringVar()\n",
    "Symptom1.set(None)\n",
    "Symptom2 = StringVar()\n",
    "Symptom2.set(None)\n",
    "Symptom3 = StringVar()\n",
    "Symptom3.set(None)\n",
    "Symptom4 = StringVar()\n",
    "Symptom4.set(None)\n",
    "Symptom5 = StringVar()\n",
    "Symptom5.set(None)\n",
    "Name = StringVar()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7af7f53b-1d07-4cef-9774-92319d3f58cd",
   "metadata": {},
   "source": [
    "<h3>Text Body of Interface<h3>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 515,
   "id": "04b6a86a-f9f1-4e46-bfa9-8bb2e5731831",
   "metadata": {},
   "outputs": [],
   "source": [
    "w2 = Label(root, justify=CENTER, text=\"    Disease Prediction\", fg=\"Black\", bg=\"AntiqueWhite1\")\n",
    "w2.config(font=(\"Arial\", 30))\n",
    "w2.grid(row=1, column=0, columnspan=2, padx=110)\n",
    "w2 = Label(root, justify=RIGHT, text=\"A guided project by Aditya Malode\", fg=\"black\", bg=\"AntiqueWhite1\")\n",
    "w2.config(font=(\"Arial\", 10))\n",
    "w2.grid(row=2, column=0, columnspan=2, padx=110)\n",
    "w2 = Label(root, justify=CENTER, text=\"-----COVID-19 Warning !-----\", fg=\"red\", bg=\"black\")\n",
    "w2.config(font=(\"Arial\", 25))\n",
    "w2.grid(row=3, column=0, columnspan=2, padx=110)\n",
    "w2 = Label(root, justify=CENTER, text=\"If have Fever, Sore Throat, Cold or Headech\", fg=\"red\", bg=\"AntiqueWhite1\")\n",
    "w2.config(font=(\"Arial\", 15))\n",
    "w2.grid(row=4, column=0, columnspan=2, padx=110)\n",
    "w2 = Label(root, justify=CENTER, text=\"Cunsult a Doctor & Follow COVID-19 Guidlines\", fg=\"red\", bg=\"AntiqueWhite1\")\n",
    "w2.config(font=(\"Arial\", 15))\n",
    "w2.grid(row=5, column=0, columnspan=2, padx=110)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9493de9f-daff-4c92-9ac7-3c95b837e3e9",
   "metadata": {},
   "source": [
    "<h1>User Interaction Componants<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 516,
   "id": "d6406303-59b8-41ee-825b-db2de011fa73",
   "metadata": {},
   "outputs": [],
   "source": [
    "NameLb = Label(root, text=\"Patient Name:\", fg=\"green\", bg=\"AntiqueWhite1\")\n",
    "AgeLb = Label(root, text=\"Patient Age:\", fg=\"blue\", bg=\"AntiqueWhite1\")\n",
    "NameLb.grid(row=6, column=0, pady=15, sticky=W)\n",
    "S1Lb = Label(root, text=\"Enter Symptom\", fg=\"Blue\", bg=\"AntiqueWhite1\")\n",
    "S1Lb.grid(row=8, column=0, pady=10, sticky=W)\n",
    "S1Lb = Label(root, text=\"Enter Symptom\", fg=\"blue\", bg=\"AntiqueWhite1\")\n",
    "S1Lb.grid(row=10, column=0, pady=10, sticky=W)\n",
    "S1Lb = Label(root, text=\"Enter Symptom\", fg=\"blue\", bg=\"AntiqueWhite1\")\n",
    "S1Lb.grid(row=12, column=0, pady=10, sticky=W)\n",
    "S1Lb = Label(root, text=\"Enter Symptom\", fg=\"blue\", bg=\"AntiqueWhite1\")\n",
    "S1Lb.grid(row=14, column=0, pady=10, sticky=W)\n",
    "S1Lb = Label(root, text=\"Enter Symptom\", fg=\"blue\", bg=\"AntiqueWhite1\")\n",
    "S1Lb.grid(row=16, column=0, pady=10, sticky=W)\n",
    "S1Lb = Label(root, text=\"Enter Symptom\", fg=\"blue\", bg=\"AntiqueWhite1\")\n",
    "S1Lb.grid(row=18, column=0, pady=10, sticky=W)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 517,
   "id": "4feeff0d-727e-4f3c-a0d8-8519f9ad5ee2",
   "metadata": {},
   "outputs": [],
   "source": [
    "OPTIONS = sorted(l1)\n",
    "NameEn = Entry(root, textvariable=Name)\n",
    "NameEn.grid(row=6, column=1)\n",
    "S1En = OptionMenu(root, Symptom1,*OPTIONS)\n",
    "S1En.grid(row=8, column=1)\n",
    "S2En = OptionMenu(root, Symptom2,*OPTIONS)\n",
    "S2En.grid(row=10, column=1)\n",
    "S3En = OptionMenu(root, Symptom3,*OPTIONS)\n",
    "S3En.grid(row=12, column=1)\n",
    "S4En = OptionMenu(root, Symptom4,*OPTIONS)\n",
    "S4En.grid(row=14, column=1)\n",
    "S5En = OptionMenu(root, Symptom5,*OPTIONS)\n",
    "S5En.grid(row=16, column=1)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7843ed78-fb0f-44d2-a8cc-f0d4f36f1d18",
   "metadata": {},
   "source": [
    "<h1>Final Step<h1>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8502d06-1ce0-4fb4-b7d3-44af0afe70a0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9512195121951219\n",
      "39\n",
      "0.9512195121951219\n",
      "39\n",
      "0.9512195121951219\n",
      "39\n"
     ]
    }
   ],
   "source": [
    "dst = Button(root, text=\"Conclusion 1\", command=DecisionTree,bg=\"AntiqueWhite1\",fg=\"green\")\n",
    "dst.grid(row=22, column=1,padx=10)\n",
    "rnf = Button(root, text=\"Conclusion 2\", command=randomforest,bg=\"AntiqueWhite1\",fg=\"green\")\n",
    "rnf.grid(row=26, column=1,padx=10)\n",
    "lr = Button(root, text=\"Dominating\", command=NaiveBayes,bg=\"AntiqueWhite1\",fg=\"green\")\n",
    "lr.grid(row=30, column=1,padx=10)\n",
    "#textfileds\n",
    "t1 = Text(root, height=1, width=40,bg=\"yellow\",fg=\"red\")\n",
    "t1.grid(row=24, column=1, padx=40)\n",
    "t2 = Text(root, height=1, width=40,bg=\"yellow\",fg=\"red\")\n",
    "t2.grid(row=28, column=1 , padx=40)\n",
    "t3 = Text(root, height=1, width=40,bg=\"yellow\",fg=\"red\")\n",
    "t3.grid(row=32, column=1 , padx=40)\n",
    "root.mainloop()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
