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
        if language == 'Italiano':
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
        elif language == 'Español':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['es.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
    if light == False:
        window1 = Tk()
        window1.title('Impostazioni')
        window1.geometry('305x105')
        window1 ['bg'] = 'gray20'
        window1.resizable(False, False)
        label_languages = Label(window1, text = 'Lingua principale:')
        label_languages ['bg'] = 'gray20'
        label_languages ['fg'] = 'white'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ('Italiano', 'Беларуская', 'Български', 'Қазақ', 'Русский', 'Српски', 'Українська', 'Deutsch', 'English', 'Español')  
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Tema principale:')
        label_themes ['bg'] = 'gray20'
        label_themes ['fg'] = 'white'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Scuro', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'gray20'
        theme_dark ['fg'] = 'white'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Leggero', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'gray20'
        theme_light ['fg'] = 'white'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'Fare domanda a', command = button_apply)
        applybutton ['bg'] = 'gray20'
        applybutton ['fg'] = 'white'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 100, y = 70, width = 110, height = 25)
    else:
        window1 = Tk()
        window1.title('Impostazioni')
        window1.geometry('305x105')
        window1 ['bg'] = 'white'
        window1.resizable(False, False)
        label_languages = Label(window1, text = 'Lingua principale:')
        label_languages ['bg'] = 'white'
        label_languages ['fg'] = 'black'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ('Italiano', 'Беларуская', 'Български', 'Қазақ', 'Русский', 'Српски', 'Українська', 'Deutsch', 'English', 'Español')
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Tema principale:')
        label_themes ['bg'] = 'white'
        label_themes ['fg'] = 'black'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Scuro', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'white'
        theme_dark ['fg'] = 'black'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Leggero', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'white'
        theme_light ['fg'] = 'black'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'Fare domanda a', command = button_apply)
        applybutton ['bg'] = 'white'
        applybutton ['fg'] = 'black'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 100, y = 70, width = 110, height = 25)
def translate():
    while True:
        global translate_language, input_text, input_language, data
        global check_from
        input_text = input_box.get('1.0', 'end')
        input_language = input_languages.get()
        translate_language = translate_languages.get()
        if input_language == 'Definire la lingua':
            check_from = False
        elif input_language == 'Arabo':
            input_language = 'ar'
        elif input_language == 'Armeno': 
            input_language = 'hy'
        elif input_language == 'Bielorusso':
            input_language = 'be'
        elif input_language == 'Bulgaro':
            input_language = 'bg'
        elif input_language == 'Cinese':
            input_language = 'zh-Hans'
        elif input_language == 'Croato':
            input_language = 'hr'
        elif input_language == 'Ceco':
            input_language = 'cs'
        elif input_language == 'Danese':
            input_language = 'da' 
        elif input_language == 'Olandese':
            input_language = 'nl'
        elif input_language == 'Inglese':
            input_language = 'en'
        elif input_language == 'Estone':
            input_language = 'et'
        elif input_language == 'Finlandese':
            input_language = 'fi'
        elif input_language == 'Francese':
            input_language = 'fr'
        elif input_language == 'Tedesco':
            input_language = 'de'
        elif input_language == 'Greco':
            input_language = 'el'
        elif input_language == 'Ebraico':
            input_language = 'he'
        elif input_language == 'Hindi':
            input_language = 'hi'
        elif input_language == 'Italiano':
            input_language = 'it'
        elif input_language == 'Giapponese':
            input_language = 'ja'
        elif input_language == 'Kazako':
            input_language = 'kk'
        elif input_language == 'Coreano':
            input_language = 'ko'
        elif input_language == 'Lettone':
            input_language = 'lv'
        elif input_language == 'Lituano':
            input_language = 'lt'
        elif input_language == 'Norvegese':
            input_language = 'no'
        elif input_language == 'Polacco':
            input_language = 'pl'
        elif input_language == 'Portoghese':
            input_language = 'pt'
        elif input_language == 'Russo':
            input_language = 'ru'
        elif input_language == 'Serbo':
            input_language = 'sr-Cyrl'
        elif input_language == 'Slovacco':
            input_language = 'sk'
        elif input_language == 'Sloveno':
            input_language = 'sl'
        elif input_language == 'Spagnolo':
            input_language = 'es'
        elif input_language == 'Svedese':
            input_language = 'sv'
        elif input_language == 'Ucraino':
            input_language = 'uk'
        if translate_language == 'Arabo':
            translate_language = 'ar'
        elif translate_language == 'Armeno':
            translate_language = 'hy'
        elif translate_language == 'Bielorusso':
            translate_language = 'be'
        elif translate_language == 'Bulgaro':
            translate_language = 'bg'
        elif translate_language == 'Cinese':
            translate_language = 'zh-Hans'
        elif translate_language == 'Croato':
            translate_language = 'hr'
        elif translate_language == 'Ceco':
            translate_language = 'cs'
        elif translate_language == 'Danese':
            translate_language = 'da'
        elif translate_language == 'Olandese':
            translate_language = 'nl'
        elif translate_language == 'Inglese':
            translate_language = 'en'
        elif translate_language == 'Estone':
            translate_language = 'et'
        elif translate_language == 'Finlandese':
            translate_language = 'fi'
        elif translate_language == 'Francese':
            translate_language = 'fr'
        elif translate_language == 'Tedesco':
            translate_language = 'de'
        elif translate_language == 'Greco':
            translate_language = 'el'
        elif translate_language == 'Ebraico':
            translate_language = 'he'
        elif translate_language == 'Hindi':
            translate_language = 'hi'
        elif translate_language == 'Italiano':
            translate_language = 'it'
        elif translate_language == 'Giapponese':
            translate_language = 'ja'
        elif translate_language == 'Kazako':
            translate_language = 'kk'
        elif translate_language == 'Coreano':
            translate_language = 'ko'
        elif translate_language == 'Lettone':
            translate_language = 'lv'
        elif translate_language == 'Lituano':
            translate_language = 'lt'
        elif translate_language == 'Norvegese':
            translate_language = 'no'
        elif translate_language == 'Polacco':
            translate_language = 'pl'
        elif translate_language == 'Portoghese':
            translate_language = 'pt'
        elif translate_language == 'Russo':
            translate_language = 'ru'
        elif translate_language == 'Serbo':
            translate_language = 'sr-Cyrl'
        elif translate_language == 'Slovacco':
            translate_language = 'sk'
        elif translate_language == 'Sloveno':
            translate_language = 'sl'
        elif translate_language == 'Spagnolo':
            translate_language = 'es'
        elif translate_language == 'Svedese':
            translate_language = 'sv'
        elif translate_language == 'Ucraino':
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
        msg = "Questo linguaggio non è supportato dalla sintesi"
        mb.showerror("Errore", msg)
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
        msg = "Questo linguaggio non è supportato dalla sintesi"
        mb.showerror("Errore", msg)
window = Tk()
window.title('Traduttore')
window.geometry('950x325')
window ['bg'] = 'gray10'
window.resizable(False, False)
buttonsettings = Button(text = '⚙', command = button_settings)
buttonsettings ['bg'] = 'gray20'
buttonsettings ['fg'] = 'white'
buttonsettings ['font'] = ('Arial', 15, 'bold')
buttonsettings ['relief'] = 'raised'
buttonsettings.place(x = 10, y = 10, width = 30, height = 30)
input_label = Label(text = 'Inserire il testo:')
input_label ['bg'] = 'gray10'
input_label ['fg'] = 'white'
input_label ['font'] = ('Arial', 10, 'bold')
input_label ['justify'] = 'center'
input_label.place(x = 50, y = 25, width = 100, height = 25)
input_languages = Combobox(window)
input_languages['values'] = ('Definire la lingua', 'Arabo', 'Armeno', 'Bielorusso', 'Bulgaro', 'Ceco', 'Cinese', 'Coreano', 'Croato', 'Danese', 'Ebraico', 'Estone', 'Finlandese', 'Francese' , 'Giapponese', 'Greco', 'Hindi', 'Inglese', 'Italiano', 'Kazako', 'Lettone', 'Lituano', 'Norvegese', 'Olandese', 'Polacco', 'Portoghese', 'Russo', 'Serbo', 'Slovacco', 'Sloveno', 'Spagnolo', 'Svedese', 'Tedesco', 'Ucraino')
input_languages.current(18)
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
input_transliteration_label = Label(text = 'Traslitterazione:')
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
translate_label = Label(text = 'Traduzione:')
translate_label ['bg'] = 'gray10'
translate_label ['fg'] = 'white'
translate_label ['font'] = ('Arial', 10, 'bold')
translate_label ['justify'] = 'center'
translate_label.place(x = 500, y = 25, width = 75, height = 25)
translate_languages = Combobox(window)
translate_languages['values'] = ('Arabo', 'Armeno', 'Bielorusso', 'Bulgaro', 'Ceco', 'Cinese', 'Coreano', 'Croato', 'Danese', 'Ebraico', 'Estone', 'Finlandese', 'Francese' , 'Giapponese', 'Greco', 'Hindi', 'Inglese', 'Italiano', 'Kazako', 'Lettone', 'Lituano', 'Norvegese', 'Olandese', 'Polacco', 'Portoghese', 'Russo', 'Serbo', 'Slovacco', 'Sloveno', 'Spagnolo', 'Svedese', 'Tedesco', 'Ucraino')
translate_languages.current(16)
translate_languages.place(x = 580, y = 25, width = 110, height = 25)
buttontranslatesound = Button(text = '📢', command = button_translate_sound)
buttontranslatesound ['bg'] = 'gray20'
buttontranslatesound ['fg'] = 'white'
buttontranslatesound ['font'] = ('Arial', 10, 'bold')
buttontranslatesound ['relief'] = 'raised'
buttontranslatesound.place(x = 700, y = 25, width = 25, height = 25)
translate_box = scrolledtext.ScrolledText(state = 'disabled')
translate_box ['bg'] = 'gray20'
translate_box ['fg'] = 'white'
translate_box ['font'] = ('Arial', 10, 'bold')
translate_box ['relief'] = 'flat'
translate_box.place(x = 500, y = 75, width = 400, height = 88)
transliteration_label = Label(text = 'Traslitterazione:')
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