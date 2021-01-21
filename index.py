import sys
import os
import speech_recognition as sr
import win32gui
import pyautogui
import sched, time 
import requests
import urllib.parse

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PySide2.QtWidgets import *
from datetime import datetime
from datetime import date
from multiprocessing import Process 
from spotify import ejecutar_spotify
from guardar_leer_csv import agregar_calendario, buscar_calendario
from bot import chatbot_response
from playsound import playsound
from os import remove

r = sr.Recognizer() 
lang="es-ES"


def reproducir_voz(texto,respuesta_audio = "respuesta.mp3"):
    if(os.path.isfile(respuesta_audio)):
        remove(respuesta_audio)
    texto = urllib.parse.quote(texto)
    url = r"https://translate.google.com.co/translate_tts?ie=UTF-8&q="+texto+r"&tl=es&client=tw-ob"
    myfile = requests.get(url)
    open(respuesta_audio, 'wb').write(myfile.content)
    playsound(respuesta_audio)
    
class VoiceWorker(QtCore.QObject):

    
    textChanged = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot()
    def task(self):
        while True:
            #print(datetime.now())
            with sr.Microphone() as source:
                #print(datetime.now())
                nombre = "Julián"
                print('Di algo: ')
                try:
                    audio = r.listen(source)
                    text = r.recognize_google(audio, language=lang)
                    print('Dijiste: {}'.format(text))

                    if (text == "Hola Lili"):
                        reproducir_voz(f"Hola {nombre}! Qué te gustaría hacer hoy?")
                        while True:
                            #print(datetime.now())
                            with sr.Microphone() as source:
                                try:
                                    audio = r.listen(source)
                                    hablar2 = r.recognize_google(audio, language=lang)
                                    print('Dijiste: {}'.format(hablar2))
                                
                                    if (hablar2== "cambiar nombre"):
                                        reproducir_voz(f"Claro!, dime el nombre que quieres que te diga")
                                        audio = r.listen(source)
                                        nombre = r.recognize_google(audio, language=lang)
                                        print('Dijiste: {}'.format(nombre))
                                        reproducir_voz(f"Perfecto, ahora te llamaré {nombre}")
                                    
                                    elif (hablar2 == "repetir"):
                                        reproducir_voz(f"Claro!, dime lo que quieres que repita")
                                        audio = r.listen(source)
                                        repetir = r.recognize_google(audio, language=lang)
                                        print('Dijiste: {}'.format(repetir))
                                        reproducir_voz(repetir)

                                    elif (hablar2 == "Cómo estás"):
                                        reproducir_voz("Bastante bien y ¿tú?")
                            
                                    elif (hablar2 == "estoy bastante bien"):
                                        reproducir_voz("¡Me alegro mucho!")
                                        
                                    elif (hablar2 == "Adiós Lili"):
                                        reproducir_voz(f"¡Hasta la próxima {nombre}!")
                                        break
                                        sys.exit()

                                    elif (hablar2 == "Reproducir canción"):
                                        reproducir_voz("Reproduciendo canción...")
                                        ejecutar_spotify("rep")
                                    
                                    elif (hablar2 == "pausar canción"):
                                        reproducir_voz("Pausando canción...")
                                        ejecutar_spotify("paus")
                                    elif (hablar2 == "siguiente canción"):
                                        reproducir_voz("Siguiente canción...")
                                        ejecutar_spotify("next")
                                    elif (hablar2 == "canción anterior"):
                                        reproducir_voz("canción anterior...")
                                        ejecutar_spotify("previous")

                                    elif (hablar2.startswith('recordar')):
                                        today = date.today()
                                        now = datetime.now()
                                        agregar_calendario(hablar2, today, now)
                                        

                                    else:
                                        respuesta = chatbot_response(text)
                                        reproducir_voz(respuesta)
                                except:
                                    print('No entendí, Abierto', sys.exc_info()[0], sys.exc_info()[1])

                except:
                    print('No entendí', sys.exc_info()[0], sys.exc_info()[1])
        
def Gui():
    app = QtWidgets.QApplication(sys.argv)

    worker = VoiceWorker()
    thread = QtCore.QThread()
    thread.start()
    worker.moveToThread(thread)

    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 350, 300)
    window.setFixedSize(350, 300) 
    window.setWindowTitle("Assistant") 

    title_label = QtWidgets.QLabel(window)
    title_label.setText("Conoce a Lili")
    title_label.move(60,5)
    title_label.setFont(QtGui.QFont("Lemon Tuesday", 35))
    title_label.resize(300,50)

    subtitle_label = QtWidgets.QLabel(window)
    subtitle_label.setText("TU ASISTENTE VIRTUAL")
    subtitle_label.move(85,40)
    subtitle_label.setFont(QtGui.QFont("Name Smile", 10))
    subtitle_label.resize(300,50)

    programs_says = QtWidgets.QLabel(window)
    programs_says.setText("¿En qué te puedo \n    ayudar hoy?")
    programs_says.move(220,80)

    you_says = QtWidgets.QLabel(window)
    you_says.move(25,100)


    label = QtWidgets.QLabel(window)
    pixmap = QPixmap('Mujer/uy feliz.png') 
    label.setPixmap(pixmap) 
    label.resize(pixmap.width(), 
                        pixmap.height())
    label.move(0,100)

    you_text = QtWidgets.QLabel(window)
    worker.textChanged.connect(you_text.setText)
    you_text.move(25,150) 

   

    start_button = QtWidgets.QPushButton(window)
    start_button.setStyleSheet("background-image : url(Recursos/microphone_rec.png);")
    start_button.resize(105,105)
    start_button.move(200,120)
    

    close_button = QtWidgets.QPushButton("Close")


    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(close_button)
    window.setLayout(v_box)

    start_button.clicked.connect(worker.task)
    close_button.clicked.connect(QtCore.QCoreApplication.instance().quit)
    window.show()
    sys.exit(app.exec())

def reloj():
    s = sched.scheduler(time.time, time.sleep) 
    def do_something(sc): 
        today = date.today()
        now = datetime.now()
        buscar_calendario(today, now)
        # do your stuff 
        s.enter(10, 1, do_something, (sc,)) 

    s.enter(10, 1, do_something, (s,)) 
    s.run() 

if __name__=='__main__': 
    p1 = Process(target = Gui)
    p1.start()
    p2 = Process(target = reloj)
    p2.start()