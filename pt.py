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
def button_Configurações():
    global light
    def button_dark_theme():
        global light
        light = False
        window ['bg'] = 'gray10'
        buttonConfigurações ['bg'] = 'gray20'
        buttonConfigurações ['fg'] = 'white'
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
        buttonConfigurações ['bg'] = 'white'
        buttonConfigurações ['fg'] = 'black'
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
        if language == 'English':
            window1.destroy()
        elif language == 'Čeština':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['cs.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Dansk':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['da.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Deutsch':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['de.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Eesti':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['et.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Español':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['es.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Français':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['fr.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Hrvatski':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['hr.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Italiano':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['it.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Latviešu':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['lv.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Lietuvių':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['lt.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Nederlands':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['ne.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Norsk':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['no.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Português':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['pt.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Polski':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['pl.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Slovenčina':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['sk.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Slovenščina':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['sl.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Suomi':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['fi.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Svenska':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['sv.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
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
        elif language == 'Ελληνικά':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['el.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'Հայերեն':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['hy.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'עִבְרִית':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['he.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'اَلْعَرَبِيَّةُ':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['ar.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == 'हिंदी':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['hi.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == '中文':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['zh.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == '日本語':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['ja.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
        elif language == '한국어':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['ko.exe'], shell = True, creationflags = subprocess.CREATE_NEW_CONSOLE)
    if light == False:
        window1 = Tk()
        window1.title('Configurações')
        window1.geometry('305x105')
        window1 ['bg'] = 'gray20'
        label_languages = Label(window1, text = 'Idioma principal:')
        label_languages ['bg'] = 'gray20'
        label_languages ['fg'] = 'white'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ('English', 'Čeština', 'Dansk', 'Deutsch', 'Eesti', 'Español', 'Français', 'Hrvatski', 'Italiano', 'Latviešu', 'Lietuvių', 'Nederlands', 'Norsk', 'Português', 'Polski', 'Slovenčina', 'Slovenščina', 'Suomi', 'Svenska', 'Беларуская', 'Български', 'Қазақ', 'Русский', 'Српски', 'Українська', 'Ελληνικά', 'Հայերեն', 'עִבְרִית', 'اَلْعَرَبِيَّةُ', 'हिंदी', '中文', '日本語', '한국어')  
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Tema principal:')
        label_themes ['bg'] = 'gray20'
        label_themes ['fg'] = 'white'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Escuro', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'gray20'
        theme_dark ['fg'] = 'white'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Luz', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'gray20'
        theme_light ['fg'] = 'white'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'aplicar', command = button_apply)
        applybutton ['bg'] = 'gray20'
        applybutton ['fg'] = 'white'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 105, y = 70, width = 100, height = 25)
    else:
        window1 = Tk()
        window1.title('Configurações')
        window1.geometry('305x105')
        window1 ['bg'] = 'white'
        label_languages = Label(window1, text = 'Idioma principal:')
        label_languages ['bg'] = 'white'
        label_languages ['fg'] = 'black'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ('English', 'Čeština', 'Dansk', 'Deutsch', 'Eesti', 'Español', 'Français', 'Hrvatski', 'Italiano', 'Latviešu', 'Lietuvių', 'Nederlands', 'Norsk', 'Português', 'Polski', 'Slovenčina', 'Slovenščina', 'Suomi', 'Svenska', 'Беларуская', 'Български', 'Қазақ', 'Русский', 'Српски', 'Українська', 'Ελληνικά', 'Հայերեն', 'עִבְרִית', 'اَلْعَرَبِيَّةُ', 'हिंदी', '中文', '日本語', '한국어')
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Tema principal:')
        label_themes ['bg'] = 'white'
        label_themes ['fg'] = 'black'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Escuro', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'white'
        theme_dark ['fg'] = 'black'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Luz', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'white'
        theme_light ['fg'] = 'black'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'aplicar', command = button_apply)
        applybutton ['bg'] = 'white'
        applybutton ['fg'] = 'black'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 105, y = 70, width = 100, height = 25)
def translate():
    while True:
        global check_from
        input_text = input_box.get('1.0', 'end')
        input_language = input_languages.get()
        translate_language = translate_languages.get()
        if input_language == 'Define language':
            check_from = False
        elif input_language == 'Arabic':
            input_language = 'ar'
        elif input_language == 'Armenian':
            input_language = 'hy'
        elif input_language == 'Belarusian':
            input_language = 'be'
        elif input_language == 'Bulgarian':
            input_language = 'bg'
        elif input_language == 'Chinese':
            input_language = 'zh-Hans'
        elif input_language == 'Croatian':
            input_language = 'hr'
        elif input_language == 'Czech':
            input_language = 'cs'
        elif input_language == 'Danish':
            input_language = 'da'
        elif input_language == 'Dutch':
            input_language = 'nl'
        elif input_language == 'English':
            input_language = 'en'
        elif input_language == 'Estonian':
            input_language = 'et'
        elif input_language == 'Finnish':
            input_language = 'fi'
        elif input_language == 'French':
            input_language = 'fr'
        elif input_language == 'German':
            input_language = 'de'
        elif input_language == 'Greek':
            input_language = 'el'
        elif input_language == 'Hebrew':
            input_language = 'he'
        elif input_language == 'Hindi':
            input_language = 'hi'
        elif input_language == 'Italian':
            input_language = 'it'
        elif input_language == 'Japanese':
            input_language = 'ja'
        elif input_language == 'Kazakh':
            input_language = 'kk'
        elif input_language == 'Korean':
            input_language = 'ko'
        elif input_language == 'Latvian':
            input_language = 'lv'
        elif input_language == 'Lithuanian':
            input_language = 'lt'
        elif input_language == 'Norwegian':
            input_language = 'no'
        elif input_language == 'Polish':
            input_language = 'pl'
        elif input_language == 'Portuguese':
            input_language = 'pt'
        elif input_language == 'Russian':
            input_language = 'ru'
        elif input_language == 'Serbian':
            input_language = 'sr-Cyrl'
        elif input_language == 'Slovak':
            input_language = 'sk'
        elif input_language == 'Slovenian':
            input_language = 'sl'
        elif input_language == 'Spanish':
            input_language = 'es'
        elif input_language == 'Swedish':
            input_language = 'sv'
        elif input_language == 'Ukranian':
            input_language = 'uk'
        if translate_language == 'Arabic':
            translate_language = 'ar'
        elif translate_language == 'Armenian':
            translate_language = 'hy'
        elif translate_language == 'Belarusian':
            translate_language = 'be'
        elif translate_language == 'Bulgarian':
            translate_language = 'bg'
        elif translate_language == 'Chinese':
            translate_language = 'zh-Hans'
        elif translate_language == 'Croatian':
            translate_language = 'hr'
        elif translate_language == 'Czech':
            translate_language = 'cs'
        elif translate_language == 'Danish':
            translate_language = 'da'
        elif translate_language == 'Dutch':
            translate_language = 'nl'
        elif translate_language == 'English':
            translate_language = 'en'
        elif translate_language == 'Estonian':
            translate_language = 'et'
        elif translate_language == 'Finnish':
            translate_language = 'fi'
        elif translate_language == 'French':
            translate_language = 'fr'
        elif translate_language == 'German':
            translate_language = 'de'
        elif translate_language == 'Greek':
            translate_language = 'el'
        elif translate_language == 'Hebrew':
            translate_language = 'he'
        elif translate_language == 'Hindi':
            translate_language = 'hi'
        elif translate_language == 'Italian':
            translate_language = 'it'
        elif translate_language == 'Japanese':
            translate_language = 'ja'
        elif translate_language == 'Kazakh':
            translate_language = 'kk'
        elif translate_language == 'Korean':
            translate_language = 'ko'
        elif translate_language == 'Latvian':
            translate_language = 'lv'
        elif translate_language == 'Lithuanian':
            translate_language = 'lt'
        elif translate_language == 'Norwegian':
            translate_language = 'no'
        elif translate_language == 'Polish':
            translate_language = 'pl'
        elif translate_language == 'Portuguese':
            translate_language = 'pt'
        elif translate_language == 'Russian':
            translate_language = 'ru'
        elif translate_language == 'Serbian':
            translate_language = 'sr-Cyrl'
        elif translate_language == 'Slovak':
            translate_language = 'sk'
        elif translate_language == 'Slovenian':
            translate_language = 'sl'
        elif translate_language == 'Spanish':
            translate_language = 'es'
        elif translate_language == 'Swedish':
            translate_language = 'sv'
        elif translate_language == 'Ukranian':
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
        msg = " Este idioma não é compatível com síntese"
        mb.showerror("Erro", msg)
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
        msg = "Este idioma não é compatível com síntese"
        mb.showerror("Erro", msg)
window = Tk()
window.title('Tradutor')
window.geometry('950x325')
window ['bg'] = 'gray10'
buttonConfigurações = Button(text = '⚙', command = button_Configurações)
buttonConfigurações ['bg'] = 'gray20'
buttonConfigurações ['fg'] = 'white'
buttonConfigurações ['font'] = ('Arial', 15, 'bold')
buttonConfigurações ['relief'] = 'raised'
buttonConfigurações.place(x = 10, y = 10, width = 30, height = 30)
input_label = Label(text = 'Digite o texto:')
input_label ['bg'] = 'gray10'
input_label ['fg'] = 'white'
input_label ['font'] = ('Arial', 10, 'bold')
input_label ['justify'] = 'center'
input_label.place(x = 50, y = 25, width = 75, height = 25)
input_languages = Combobox(window)
input_languages['values'] = ('Define language', 'Arabic', 'Armenian', 'Belarusian', 'Bulgarian', 'Chinese', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Finnish', 'French', 'German', 'Greek', 'Hebrew', 'Hindi', 'Italian', 'Japanese', 'Kazakh', 'Korean', 'Latvian', 'Lithuanian', 'Norwegian', 'Polish', 'Portuguese', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swedish', 'Ukranian')
input_languages.current(10)
input_languages.place(x = 130, y = 25, width = 110, height = 25)
buttoninputsound = Button(text = '📢', command = button_input_sound)
buttoninputsound ['bg'] = 'gray20'
buttoninputsound ['fg'] = 'white'
buttoninputsound ['font'] = ('Arial', 10, 'bold')
buttoninputsound ['relief'] = 'raised'
buttoninputsound.place(x = 250, y = 25, width = 25, height = 25)
input_box = scrolledtext.ScrolledText()
input_box ['bg'] = 'gray20'
input_box ['fg'] = 'white'
input_box ['font'] = ('Arial', 10, 'bold')
input_box ['relief'] = 'flat'
input_box.place(x = 50, y = 75, width = 400, height = 88)
input_transliteration_label = Label(text = 'Transliteração:')
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
translate_label = Label(text = 'Tradução:')
translate_label ['bg'] = 'gray10'
translate_label ['fg'] = 'white'
translate_label ['font'] = ('Arial', 10, 'bold')
translate_label ['justify'] = 'center'
translate_label.place(x = 500, y = 25, width = 75, height = 25)
translate_languages = Combobox(window)
translate_languages['values'] = ('Arabic', 'Armenian', 'Belarusian', 'Bulgarian', 'Chinese', 'Croatian', 'Czech', 'Danish', 'Dutch', 'English', 'Estonian', 'Finnish', 'French', 'German', 'Greek', 'Hebrew', 'Hindi', 'Italian', 'Japanese', 'Kazakh', 'Korean', 'Latvian', 'Lithuanian', 'Norwegian', 'Polish', 'Portuguese', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swedish', 'Ukranian')
translate_languages.current(30)
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
transliteration_label = Label(text = 'Transliteração:')
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