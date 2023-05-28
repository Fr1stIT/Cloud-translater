from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox as mb
import requests
import json
import threading
import subprocess
import pyttsx3
global de_voice, en_voice, es_voice, fr_voice, it_voice, ja_voice, pl_voice, ru_voice
tts = pyttsx3.init()
voices = tts.getProperty('voices')
de_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0"
en_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
es_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
fr_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0"
it_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0"
ja_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0"
pl_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PL-PL_PAULINA_11.0"
ru_voice = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0"
global input_text, input_language
check_from = True
light = False
def button_settings():
    global light
    def button_dark_theme():
        global light
        light = False
        window ['bg'] = 'gray10'
        buttonsettings ['bg'] = 'gray20'
        buttonsettings ['fg'] = 'white'
        input_label ['bg'] = 'gray10'
        input_label ['fg'] = 'white'
        input_box ['bg'] = 'gray20'
        input_box ['fg'] = 'white'
        buttoninputsound ['bg'] = 'gray20'
        buttoninputsound ['fg'] = 'white'
        input_transliteration_label ['bg'] = 'gray10'
        input_transliteration_label ['fg'] = 'white'
        input_transliteration_box ['bg'] = 'gray20'
        input_transliteration_box ['fg'] = 'white'
        translate_label ['bg'] = 'gray10'
        translate_label ['fg'] = 'white'
        translate_box ['bg'] = 'gray20'
        translate_box ['fg'] = 'white'
        buttontranslatesound ['bg'] = 'gray20'
        buttontranslatesound ['fg'] = 'white'
        transliteration_label ['bg'] = 'gray10'
        transliteration_label ['fg'] = 'white'
        transliteration_box ['bg'] = 'gray20'
        transliteration_box ['fg'] = 'white'
        window1 ['bg'] = 'gray20'
        label_languages ['bg'] = 'gray20'
        label_languages ['fg'] = 'white'
        label_themes ['bg'] = 'gray20'
        label_themes ['fg'] = 'white'
        theme_dark ['bg'] = 'gray20'
        theme_dark ['fg'] = 'white'
        theme_light ['bg'] = 'gray20'
        theme_light ['fg'] = 'white'
        applybutton ['bg'] = 'gray20'
        applybutton ['fg'] = 'white'
    def button_light_theme():
        global light
        light = True
        window ['bg'] = 'gray90'
        buttonsettings ['bg'] = 'white'
        buttonsettings ['fg'] = 'black'
        input_label ['bg'] = 'gray90'
        input_label ['fg'] = 'black'
        input_box ['bg'] = 'white'
        input_box ['fg'] = 'black'
        buttoninputsound ['bg'] = 'white'
        buttoninputsound ['fg'] = 'black'
        input_transliteration_label ['bg'] = 'gray90'
        input_transliteration_label ['fg'] = 'black'
        input_transliteration_box ['bg'] = 'white'
        input_transliteration_box ['fg'] = 'black'
        translate_label ['bg'] = 'gray90'
        translate_label ['fg'] = 'black'
        translate_box ['bg'] = 'white'
        translate_box ['fg'] = 'black'
        buttontranslatesound ['bg'] = 'white'
        buttontranslatesound ['fg'] = 'black'
        transliteration_label ['bg'] = 'gray90'
        transliteration_label ['fg'] = 'black'
        transliteration_box ['bg'] = 'white'
        transliteration_box ['fg'] = 'black'
        window1 ['bg'] = 'white'
        label_languages ['bg'] = 'white'
        label_languages ['fg'] = 'black'
        label_themes ['bg'] = 'white'
        label_themes ['fg'] = 'black'
        theme_dark ['bg'] = 'white'
        theme_dark ['fg'] = 'black'
        theme_light ['bg'] = 'white'
        theme_light ['fg'] = 'black'
        applybutton ['bg'] = 'white'
        applybutton ['fg'] = 'black'
    def button_apply():
        language = set_languages.get()
        if language == 'Español':
            window1.destroy()
        elif language == 'Беларуская':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['be.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Български':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['bg.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Қазақ':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['kk.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Русский':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['ru.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Српски':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['sr.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Українська':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['uk.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Deutsch':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['de.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'English':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['en.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Italiano':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['it.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
    if light == False:
        window1 = Tk()
        window1.title('Ajustes')
        window1.geometry('305x105')
        window1 ['bg'] = 'gray20'
        window1.resizable(False, False)
        label_languages = Label(window1, text = 'Lenguaje principal:')
        label_languages ['bg'] = 'gray20'
        label_languages ['fg'] = 'white'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ('Español', 'Беларуская', 'Български', 'Қазақ', 'Русский', 'Српски', 'Українська', 'Deutsch', 'English', 'Italiano')  
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Tema principal:')
        label_themes ['bg'] = 'gray20'
        label_themes ['fg'] = 'white'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Oscuro', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'gray20'
        theme_dark ['fg'] = 'white'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Ligero', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'gray20'
        theme_light ['fg'] = 'white'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'Aplicar', command = button_apply)
        applybutton ['bg'] = 'gray20'
        applybutton ['fg'] = 'white'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 105, y = 70, width = 100, height = 25)
    else:
        window1 = Tk()
        window1.title('Ajustes')
        window1.geometry('305x105')
        window1 ['bg'] = 'white'
        window1.resizable(False, False)
        label_languages = Label(window1, text = 'Lenguaje principal:')
        label_languages ['bg'] = 'white'
        label_languages ['fg'] = 'black'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ('Español', 'Беларуская', 'Български', 'Қазақ', 'Русский', 'Српски', 'Українська', 'Deutsch', 'English', 'Italiano')
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Tema principal:')
        label_themes ['bg'] = 'white'
        label_themes ['fg'] = 'black'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Oscuro', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'white'
        theme_dark ['fg'] = 'black'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Ligero', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'white'
        theme_light ['fg'] = 'black'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'Aplicar', command = button_apply)
        applybutton ['bg'] = 'white'
        applybutton ['fg'] = 'black'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 105, y = 70, width = 100, height = 25)
def translate():
    while True:
        global translate_language, input_text, input_language
        global check_from
        input_text = input_box.get('1.0', 'end')
        input_language = input_languages.get()
        translate_language = translate_languages.get()
        if input_language == 'Definir idioma':
            check_from = False
        elif input_language == 'Árabe':
            input_language = 'ar'
        elif input_language == 'Armenio':
            input_language = 'hy'
        elif input_language == 'Bielorruso':
            input_language = 'be'
        elif input_language == 'Búlgaro':
            input_language = 'bg'
        elif input_language == 'Chino':
            input_language = 'zh-Hans'
        elif input_language == 'Croata':
            input_language = 'hr'
        elif input_language == 'Checo':
            input_language = 'cs'
        elif input_language == 'Danés':
            input_language = 'da'
        elif input_language == 'Holandés':
            input_language = 'nl'
        elif input_language == 'Inglés':
            input_language = 'en'
        elif input_language == 'Estonio':
            input_language = 'et'
        elif input_language == 'Finlandés':
            input_language = 'fi'
        elif input_language == 'Francés':
            input_language = 'fr'
        elif input_language == 'Alemán':
            input_language = 'de'
        elif input_language == 'Griego':
            input_language = 'el'
        elif input_language == 'Hebreo':
            input_language = 'he'
        elif input_language == 'Hindi':
            input_language = 'hi'
        elif input_language == 'Italiano':
            input_language = 'it'
        elif input_language == 'Japonés':
            input_language = 'ja'
        elif input_language == 'Kazajo':
            input_language = 'kk'
        elif input_language == 'Coreano':
            input_language = 'ko'
        elif input_language == 'Letón':
            input_language = 'lv'
        elif input_language == 'Lituano':
            input_language = 'lt'
        elif input_language == 'Noruego':
            input_language = 'no'
        elif input_language == 'Polaco':
            input_language = 'pl'
        elif input_language == 'Portugués':
            input_language = 'pt'
        elif input_language == 'Ruso':
            input_language = 'ru'
        elif input_language == 'Serbio':
            input_language = 'sr-Cyrl'
        elif input_language == 'Eslovaco':
            input_language = 'sk'
        elif input_language == 'Esloveno':
            input_language = 'sl'
        elif input_language == 'Español':
            input_language = 'es'
        elif input_language == 'Sueco':
            input_language = 'sv'
        elif input_language == 'Ucranio':
            input_language = 'uk'
        if translate_language == 'Árabe':
            translate_language = 'ar'
        elif translate_language == 'Armenio':
            translate_language = 'hy'
        elif translate_language == 'Bielorruso':
            translate_language = 'be'
        elif translate_language == 'Búlgaro':
            translate_language = 'bg'
        elif translate_language == 'Chino':
            translate_language = 'zh-Hans'
        elif translate_language == 'Croata':
            translate_language = 'hr'
        elif translate_language == 'Checo':
            translate_language = 'cs'
        elif translate_language == 'Danés':
            translate_language = 'da'
        elif translate_language == 'Holandés':
            translate_language = 'nl'
        elif translate_language == 'Inglés':
            translate_language = 'en'
        elif translate_language == 'Estonio':
            translate_language = 'et'
        elif translate_language == 'Finlandés':
            translate_language = 'fi'
        elif translate_language == 'Francés':
            translate_language = 'fr'
        elif translate_language == 'Alemán':
            translate_language = 'de'
        elif translate_language == 'Griego':
            translate_language = 'el'
        elif translate_language == 'Hebreo':
            translate_language = 'he'
        elif translate_language == 'Hindi':
            translate_language = 'hi'
        elif translate_language == 'Italiano':
            translate_language = 'it'
        elif translate_language == 'Japonés':
            translate_language = 'ja'
        elif translate_language == 'Kazajo':
            translate_language = 'kk'
        elif translate_language == 'Coreano':
            translate_language = 'ko'
        elif translate_language == 'Letón':
            translate_language = 'lv'
        elif translate_language == 'Lituano':
            translate_language = 'lt'
        elif translate_language == 'Noruego':
            translate_language = 'no'
        elif translate_language == 'Polaco':
            translate_language = 'pl'
        elif translate_language == 'Portugués':
            translate_language = 'pt'
        elif translate_language == 'Ruso':
            translate_language = 'ru'
        elif translate_language == 'Serbio':
            translate_language = 'sr-Cyrl'
        elif translate_language == 'Eslovaco':
            translate_language = 'sk'
        elif translate_language == 'Esloveno':
            translate_language = 'sl'
        elif translate_language == 'Español':
            translate_language = 'es'
        elif translate_language == 'Sueco':
            translate_language = 'sv'
        elif translate_language == 'Ucranio':
            translate_language = 'uk'
        url = "http://api-b2b.backenster.com/b1/api/v3/translate"
        if check_from == True:
            payload = {  
                "from": input_language,
                "to": translate_language,
                "data": input_text ,
                "platform": "api",
                "enableTransliteration": True,
            }
        if check_from == False:
            payload = {  
                "to": translate_language,
                "data": input_text ,
                "platform": "api",
                "enableTransliteration": True,
            }
        headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "a_PubgbFDaOmtDzpBknonSxtZLRaBv2QcPZ4UwUfNLNUEOuaQxELkWJzbAyiSlILICx3bbI7SuKxu5I4bM"
        }
        response = requests.post(url, json=payload, headers=headers)
        jsonData = response.text
        dictData = json.loads(jsonData)
        data = dictData["result"]
        sourceTrans = dictData["sourceTransliteration"]
        targetTrans = dictData["targetTransliteration"]
        translate_box.configure(state = 'normal')
        translate_box.delete('1.0', 'end')
        translate_box.insert('1.0', data)
        translate_box.configure(state = 'disabled')
        transliteration_box.configure(state = 'normal')
        transliteration_box.delete('1.0', 'end')
        transliteration_box.insert('1.0', targetTrans)
        transliteration_box.configure(state = 'disabled')
        input_transliteration_box.configure(state = 'normal')
        input_transliteration_box.delete('1.0', 'end')
        input_transliteration_box.insert('1.0', sourceTrans)
        input_transliteration_box.configure(state = 'disabled')
def button_input_sound():
    global input_text, input_language
    if input_language == "de":
        tts.setProperty('voice' , de_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    elif input_language == "en":
        tts.setProperty('voice' , en_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    elif input_language == "es":
        tts.setProperty('voice' , es_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    elif input_language == "fr":
        tts.setProperty('voice' , fr_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    elif input_language == "it":
        tts.setProperty('voice' , it_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    elif input_language == "ja":
        tts.setProperty('voice' , ja_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    elif input_language == "ru":
        tts.setProperty('voice' , ru_voice)
        tts.say(str(input_text))
        tts.runAndWait()
    else:
        msg = "Este idioma no es compatible con la síntesis"
        mb.showerror("Error", msg)
def button_translate_sound():
    global translate_language, data
    if translate_language == "de":
        tts.setProperty('voice' , de_voice)
        tts.say(str(data))
        tts.runAndWait()
    elif translate_language == "en":
        tts.setProperty('voice' , en_voice)
        tts.say(str(data))
        tts.runAndWait()
    elif translate_language == "es":
        tts.setProperty('voice' , es_voice)
        tts.say(str(data))
    elif translate_language == "fr":
        tts.setProperty('voice' , fr_voice)
        tts.say(str(data))
        tts.runAndWait()
    elif translate_language == "it":
        tts.setProperty('voice' , it_voice)
        tts.say(str(data))
        tts.runAndWait()
    elif translate_language == "ja":
        tts.setProperty('voice' , ja_voice)
        tts.say(str(data))
        tts.runAndWait()
    elif translate_language == "ru":
        tts.setProperty('voice' , ru_voice)
        tts.say(str(data))
        tts.runAndWait()
    else:
        msg = "Este idioma no es compatible con la síntesis"
        mb.showerror("Error", msg)
window = Tk()
window.title('Traductor')
window.geometry('950x325')
window ['bg'] = 'gray10'
window.resizable(False, False)
buttonsettings = Button(text = '⚙', command = button_settings)
buttonsettings ['bg'] = 'gray20'
buttonsettings ['fg'] = 'white'
buttonsettings ['font'] = ('Arial', 15, 'bold')
buttonsettings ['relief'] = 'raised'
buttonsettings.place(x = 10, y = 10, width = 30, height = 30)
input_label = Label(text = 'Ingrese texto:')
input_label ['bg'] = 'gray10'
input_label ['fg'] = 'white'
input_label ['font'] = ('Arial', 10, 'bold')
input_label ['justify'] = 'center'
input_label.place(x = 50, y = 25, width = 100, height = 25)
input_languages = Combobox(window)
input_languages['values'] = ('Definir idioma', 'Alemán', 'Árabe', 'Armenio', 'Bielorruso', 'Búlgaro', 'Checo', 'Chino', 'Coreano', 'Croata', 'Danés', 'Eslovaco', 'Esloveno', 'Español', 'Estonio', 'Finlandés', 'Francés', 'Griego', 'Hebreo', 'Hindi', 'Holandés', 'Inglés', 'Italiano', 'Japonés', 'Kazajo', 'Letón', 'Lituano', 'Noruego', 'Polaco', 'Portugués', 'Ruso', 'Serbio', 'Sueco', 'Ucranio')
input_languages.current(13)
input_languages.place(x = 155, y = 25, width = 110, height = 25)
buttoninputsound = Button(text = '📢', command = button_input_sound)
buttoninputsound ['bg'] = 'gray20'
buttoninputsound ['fg'] = 'white'
buttoninputsound ['font'] = ('Arial', 10, 'bold')
buttoninputsound ['relief'] = 'raised'
buttoninputsound.place(x = 275, y = 25, width = 25, height = 25)
input_box = scrolledtext.ScrolledText()
input_box ['bg'] = 'gray20'
input_box ['fg'] = 'white'
input_box ['font'] = ('Arial', 10, 'bold')
input_box ['relief'] = 'flat'
input_box.place(x = 50, y = 75, width = 400, height = 88)
input_transliteration_label = Label(text = 'Transcripción:')
input_transliteration_label ['bg'] = 'gray10'
input_transliteration_label ['fg'] = 'white'
input_transliteration_label ['font'] = ('Arial', 10, 'bold')
input_transliteration_label ['justify'] = 'center'
input_transliteration_label.place(x = 50, y = 163, width = 125, height = 25)
input_transliteration_box = scrolledtext.ScrolledText(state = 'disabled')
input_transliteration_box ['bg'] = 'gray20'
input_transliteration_box ['fg'] = 'white'
input_transliteration_box ['font'] = ('Arial', 10, 'bold')
input_transliteration_box ['relief'] = 'flat'
input_transliteration_box.place(x = 50, y = 188, width = 400, height = 88)
translate_label = Label(text = 'Traducción:')
translate_label ['bg'] = 'gray10'
translate_label ['fg'] = 'white'
translate_label ['font'] = ('Arial', 10, 'bold')
translate_label ['justify'] = 'center'
translate_label.place(x = 500, y = 25, width = 75, height = 25)
translate_languages = Combobox(window)
translate_languages['values'] = ('Alemán', 'Árabe', 'Armenio', 'Bielorruso', 'Búlgaro', 'Checo', 'Chino', 'Coreano', 'Croata', 'Danés', 'Eslovaco', 'Esloveno', 'Español', 'Estonio', 'Finlandés', 'Francés', 'Griego', 'Hebreo', 'Hindi', 'Holandés', 'Inglés', 'Italiano', 'Japonés', 'Kazajo', 'Letón', 'Lituano', 'Noruego', 'Polaco', 'Portugués', 'Ruso', 'Serbio', 'Sueco', 'Ucranio')
translate_languages.current(20)
translate_languages.place(x = 580, y = 25, width = 110, height = 25)
buttontranslatesound = Button(text = '📢', command = button_translate_sound)
buttontranslatesound ['bg'] = 'gray20'
buttontranslatesound ['fg'] = 'white'
buttontranslatesound ['font'] = ('Arial', 10, 'bold')
buttontranslatesound ['relief'] = 'raised'
buttontranslatesound.place(x = 705, y = 25, width = 25, height = 25)
translate_box = scrolledtext.ScrolledText(state = 'disabled')
translate_box ['bg'] = 'gray20'
translate_box ['fg'] = 'white'
translate_box ['font'] = ('Arial', 10, 'bold')
translate_box ['relief'] = 'flat'
translate_box.place(x = 500, y = 75, width = 400, height = 88)
transliteration_label = Label(text = 'Transcripción:')
transliteration_label ['bg'] = 'gray10'
transliteration_label ['fg'] = 'white'
transliteration_label ['font'] = ('Arial', 10, 'bold')
transliteration_label ['justify'] = 'center'
transliteration_label.place(x = 500, y = 163, width = 125, height = 25)
transliteration_box = scrolledtext.ScrolledText(state = 'disabled')
transliteration_box ['bg'] = 'gray20'
transliteration_box ['fg'] = 'white'
transliteration_box ['font'] = ('Arial', 10, 'bold')
transliteration_box ['relief'] = 'flat'
transliteration_box.place(x = 500, y = 188, width = 400, height = 88)
t1 = threading.Thread(target = translate, args = ())
t1.start()
window.mainloop()