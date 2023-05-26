from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import requests
import json
import threading
import os
import subprocess

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
        input_transliteration_label ['bg'] = 'gray10'
        input_transliteration_label ['fg'] = 'white'
        input_transliteration_box ['bg'] = 'gray20'
        input_transliteration_box ['fg'] = 'white'
        translate_label ['bg'] = 'gray10'
        translate_label ['fg'] = 'white'
        translate_box ['bg'] = 'gray20'
        translate_box ['fg'] = 'white'
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
        input_transliteration_label ['bg'] = 'gray90'
        input_transliteration_label ['fg'] = 'black'
        input_transliteration_box ['bg'] = 'white'
        input_transliteration_box ['fg'] = 'black'
        translate_label ['bg'] = 'gray90'
        translate_label ['fg'] = 'black'
        translate_box ['bg'] = 'white'
        translate_box ['fg'] = 'black'
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
        if language == 'Русский':
            window1.destroy()
        elif language == 'Беларуская':
            window1.destroy()
            window.destroy()
            os.system('be.exe')
            os.kill('cmd.exe')

        elif language == 'Български':
            window1.destroy()
            window.destroy()
            os.system('bg.exe')
        elif language == 'Қазақ':
            window1.destroy()
            window.destroy()
            os.system('kk.exe')
        elif language == 'Српски':
            window1.destroy()
            window.destroy()
            os.system('sr.exe')
        elif language == 'Українська':
            window1.destroy()
            window.destroy()
            os.system('uk.exe')
        elif language == 'Čeština':
            window1.destroy()
            window.destroy()
            os.system('cs.exe')
        elif language == 'Dansk':
            window1.destroy()
            window.destroy()
            os.system('de.exe')
        elif language == 'Deutsch':
            window1.destroy()
            window.destroy()
            os.system('de.exe')
        elif language == 'Eesti':
            window1.destroy()
            window.destroy()
            os.system('et.exe')
        elif language == 'English':
            window1.destroy()
            window.destroy()
            subprocess.Popen(['en.exe'], shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
            
            
            
        elif language == 'Español':
            window1.destroy()
            window.destroy()
            os.system('es.exe')
        elif language == 'Français':
            window1.destroy()
            window.destroy()
            os.system('fr.exe')
        elif language == 'Hrvatski':
            window1.destroy()
            window.destroy()
            os.system('hr.exe')
        elif language == 'Italiano':
            window1.destroy()
            window.destroy()
            os.system('it.exe')
        elif language == 'Latviešu':
            window1.destroy()
            window.destroy()
            os.system('lv.exe')
        elif language == 'Lietuvių':
            window1.destroy()
            window.destroy()
            os.system('lt.exe')
        elif language == 'Nederlands':
            window1.destroy()
            window.destroy()
            os.system('nl.exe')
        elif language == 'Norsk':
            window1.destroy()
            window.destroy()
            os.system('no.exe')
        elif language == 'Português':
            window1.destroy()
            window.destroy()
            os.system('pt.exe')
        elif language == 'Polski':
            window1.destroy()
            window.destroy()
            os.system('pl.exe')
        elif language == 'Slovenčina':
            window1.destroy()
            window.destroy()
            os.system('sk.exe')
        elif language == 'Slovenščina':
            window1.destroy()
            window.destroy()
            os.system('sl.exe')
        elif language == 'Suomi':
            window1.destroy()
            window.destroy()
            os.system('fi.exe')
        elif language == 'Svenska':
            window1.destroy()
            window.destroy()
            os.system('sv.exe')
        elif language == 'Ελληνικά':
            window1.destroy()
            window.destroy()
            os.system('el.exe')
        elif language == 'Հայերեն':
            window1.destroy()
            window.destroy()
            os.system('hy.exe')
        elif language == 'עִבְרִית':
            window1.destroy()
            window.destroy()
            os.system('he.exe')
        elif language == 'اَلْعَرَبِيَّةُ':
            window1.destroy()
            window.destroy()
            os.system('ar.exe')
        elif language == 'हिंदी':
            window1.destroy()
            window.destroy()
            os.system('hi.exe')
        elif language == '中文':
            window1.destroy()
            window.destroy()
            os.system('zh.exe')
        elif language == '日本語':
            window1.destroy()
            window.destroy()
            os.system('ja.exe')
        elif language == '한국어':
            window1.destroy()
            window.destroy()
            os.system('ko.exe')
    if light == False:
        window1 = Tk()
        window1.title('Настройки')
        window1.geometry('305x105')
        window1 ['bg'] = 'gray20'
        label_languages = Label(window1, text = 'Основой язык:')
        label_languages ['bg'] = 'gray20'
        label_languages ['fg'] = 'white'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ( 'Русский', 'Беларуская', 'Български', 'Қазақ', 'Српски', 'Українська', 'Čeština', 'Dansk', 'Deutsch', 'Eesti', 'English', 'Español', 'Français', 'Hrvatski', 'Italiano', 'Latviešu', 'Lietuvių', 'Nederlands', 'Norsk', 'Português', 'Polski', 'Slovenčina', 'Slovenščina', 'Suomi', 'Svenska', 'Ελληνικά', 'Հայերեն', 'עִבְרִית', 'اَلْعَرَبِيَّةُ', 'हिंदी', '中文', '日本語', '한국어')  
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Основая тема:')
        label_themes ['bg'] = 'gray20'
        label_themes ['fg'] = 'white'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Тёмная', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'gray20'
        theme_dark ['fg'] = 'white'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Светлая', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'gray20'
        theme_light ['fg'] = 'white'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'Применить', command = button_apply)
        applybutton ['bg'] = 'gray20'
        applybutton ['fg'] = 'white'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 105, y = 70, width = 100, height = 25)
    else:
        window1 = Tk()
        window1.title('Настройки')
        window1.geometry('305x105')
        window1 ['bg'] = 'white'
        label_languages = Label(window1, text = 'Основой язык:')
        label_languages ['bg'] = 'white'
        label_languages ['fg'] = 'black'
        label_languages ['font'] = ('Arial', 10, 'bold')
        label_languages.place(x = 10, y = 10, width = 125, height = 25)
        set_languages = Combobox(window1, width = 10, height = 25)
        set_languages['values'] = ( 'Русский', 'Беларуская', 'Български', 'Қазақ', 'Српски', 'Українська', 'Čeština', 'Dansk', 'Deutsch', 'Eesti', 'English', 'Español', 'Français', 'Hrvatski', 'Italiano', 'Latviešu', 'Lietuvių', 'Nederlands', 'Norsk', 'Português', 'Polski', 'Slovenčina', 'Slovenščina', 'Suomi', 'Svenska', 'Ελληνικά', 'Հայերեն', 'עִבְרִית', 'اَلْعَرَبِيَّةُ', 'हिंदी', '中文', '日本語', '한국어')  
        set_languages.current(0)
        set_languages.place(x = 135, y = 10, width = 100, height = 25)
        label_themes = Label(window1, text = 'Основая тема:')
        label_themes ['bg'] = 'white'
        label_themes ['fg'] = 'black'
        label_themes ['font'] = ('Arial', 10, 'bold')
        label_themes.place(x = 10, y = 35, width = 125, height = 25)
        theme_dark = Radiobutton(window1, text = 'Тёмная', value = 0, command = button_dark_theme)
        theme_dark ['bg'] = 'white'
        theme_dark ['fg'] = 'black'
        theme_dark ['font'] = ('Arial', 10, 'bold')
        theme_dark.place(x = 135, y = 35, width = 75, height = 25)
        theme_light = Radiobutton(window1, text = 'Светлая', value = 1, command = button_light_theme)
        theme_light ['bg'] = 'white'
        theme_light ['fg'] = 'black'
        theme_light ['font'] = ('Arial', 10, 'bold')
        theme_light.place(x = 210, y = 35, width = 75, height = 25)
        applybutton = Button(window1, text = 'Применить', command = button_apply)
        applybutton ['bg'] = 'white'
        applybutton ['fg'] = 'black'
        applybutton ['font'] = ('Arial', 10, 'bold')
        applybutton ['relief'] = 'raised'
        applybutton.place(x = 105, y = 70, width = 100, height = 25)
def translate_button():
    while True:
        global check_from
        input_text = input_box.get('1.0', 'end')
        input_language = input_languages.get()
        translate_language = translate_languages.get()
        if input_language == 'Определить язык':
            check_from = False
        elif input_language == 'Английский':
            input_language = 'en'
        elif input_language == 'Арабский':
            input_language = 'ar'
        elif input_language == 'Армняский':
            input_language = 'hy'
        elif input_language == 'Белорусский':
            input_language = 'be'
        elif input_language == 'Болгарский':
            input_language = 'bg'
        elif input_language == 'Греческий':
            input_language = 'el'
        elif input_language == 'Датский':
            input_language = 'da'
        elif input_language == 'Иврит':
            input_language = 'he'
        elif input_language == 'Испанский':
            input_language = 'es'
        elif input_language == 'Итальянский':
            input_language = 'it'
        elif input_language == 'Казахский':
            input_language = 'kk'
        elif input_language == 'Китайский':
            input_language = 'zh-Hans'
        elif input_language == 'Корейский':
            input_language = 'ko'
        elif input_language == 'Латышский':
            input_language = 'lv'
        elif input_language == 'Литовский':
            input_language = 'lt'
        elif input_language == 'Немецкий':
            input_language = 'de'
        elif input_language == 'Нидерландский':
            input_language = 'nl'
        elif input_language == 'Норвежский':
            input_language = 'no'
        elif input_language == 'Польский':
            input_language = 'pl'
        elif input_language == 'Португальский':
            input_language = 'pt'
        elif input_language == 'Русский':
            input_language = 'ru'
        elif input_language == 'Сербский':
            input_language = 'sr-Cyrl'
        elif input_language == 'Словацкий':
            input_language = 'sk'
        elif input_language == 'Словенский':
            input_language = 'sl'
        elif input_language == 'Украинский':
            input_language = 'uk'
        elif input_language == 'Финский':
            input_language = 'fi'
        elif input_language == 'Французский':
            input_language = 'fr'
        elif input_language == 'Хинди':
            input_language = 'hi'
        elif input_language == 'Хорватский':
            input_language = 'hr'
        elif input_language == 'Чешский':
            input_language = 'cs'
        elif input_language == 'Шведский':
            input_language = 'sv'
        elif input_language == 'Эстонский':
            input_language = 'et'
        elif input_language == 'Японский':
            input_language = 'ja'
        if translate_language == 'Английский':
            translate_language = 'en'
        elif translate_language == 'Арабский':
            translate_language = 'ar'
        elif translate_language == 'Армняский':
            translate_language = 'hy'
        elif translate_language == 'Белорусский':
            translate_language = 'be'
        elif translate_language == 'Болгарский':
            translate_language = 'bg'
        elif translate_language == 'Греческий':
            translate_language = 'el'
        elif translate_language == 'Датский':
            translate_language = 'da'
        elif translate_language == 'Иврит':
            translate_language = 'he'
        elif translate_language == 'Испанский':
            translate_language = 'es'
        elif translate_language == 'Итальянский':
            translate_language = 'it'
        elif translate_language == 'Казахский':
            translate_language = 'kk'
        elif translate_language == 'Китайский':
            translate_language = 'zh-Hans'
        elif translate_language == 'Корейский':
            translate_language = 'ko'
        elif translate_language == 'Латышский':
            translate_language = 'lv'
        elif translate_language == 'Литовский':
            translate_language = 'lt'
        elif translate_language == 'Немецкий':
            translate_language = 'de'
        elif translate_language == 'Нидерландский':
            translate_language = 'nl'
        elif translate_language == 'Норвежский':
            translate_language = 'no'
        elif translate_language == 'Польский':
            translate_language = 'pl'
        elif translate_language == 'Португальский':
            translate_language = 'pt'
        elif translate_language == 'Русский':
            translate_language = 'ru'
        elif translate_language == 'Сербский':
            translate_language = 'sr-Cyrl'
        elif translate_language == 'Словацкий':
            translate_language = 'sk'
        elif translate_language == 'Словенский':
            translate_language = 'sl'
        elif translate_language == 'Украинский':
            translate_language = 'uk'
        elif translate_language == 'Финский':
            translate_language = 'fi'
        elif translate_language == 'Французский':
            translate_language = 'fr'
        elif translate_language == 'Хинди':
            translate_language = 'hi'
        elif translate_language == 'Хорватский':
            translate_language = 'hr'
        elif translate_language == 'Чешский':
            translate_language = 'cs'
        elif translate_language == 'Шведский':
            translate_language = 'sv'
        elif translate_language == 'Эстонский':
            translate_language = 'et'
        elif translate_language == 'Японский':
            translate_language = 'ja'
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
window = Tk()
window.title('Переводчик')
window.geometry('950x325')
window ['bg'] = 'gray10'
buttonsettings = Button(text = '⚙', command = button_settings)
buttonsettings ['bg'] = 'gray20'
buttonsettings ['fg'] = 'white'
buttonsettings ['font'] = ('Arial', 15, 'bold')
buttonsettings ['relief'] = 'raised'
buttonsettings.place(x = 10, y = 10, width = 30, height = 30)
input_label = Label(text = 'Введите текст:')
input_label ['bg'] = 'gray10'
input_label ['fg'] = 'white'
input_label ['font'] = ('Arial', 10, 'bold')
input_label ['justify'] = 'center'
input_label.place(x = 50, y = 25, width = 110, height = 25)
input_languages = Combobox(window)
input_languages['values'] = ('Определить язык', 'Английский', 'Арабский', 'Армняский', 'Белорусский', 'Болгарский', 'Греческий', 'Датский', 'Иврит', 'Испанский', 'Итальянский', 'Казахский', 'Китайский', 'Корейский', 'Латышский', 'Литовский', 'Немецкий', 'Нидерландский', 'Норвежский', 'Польский', 'Португальский', 'Русский', 'Сербский', 'Словацкий', 'Словенский', 'Украинский', 'Финский', 'Французский', 'Хинди', 'Хорватский', 'Чешский', 'Шведский', 'Эстонский', 'Японский')
input_languages.current(21)
input_languages.place(x = 160, y = 25, width = 120, height = 25)
input_box = scrolledtext.ScrolledText()
input_box ['bg'] = 'gray20'
input_box ['fg'] = 'white'
input_box ['font'] = ('Arial', 10, 'bold')
input_box ['relief'] = 'flat'
input_box.place(x = 50, y = 75, width = 400, height = 88)
input_transliteration_label = Label(text = 'Транслитерация:')
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
translate_label = Label(text = 'Перевод:')
translate_label ['bg'] = 'gray10'
translate_label ['fg'] = 'white'
translate_label ['font'] = ('Arial', 10, 'bold')
translate_label ['justify'] = 'center'
translate_label.place(x = 500, y = 25, width = 75, height = 25)
translate_languages = Combobox(window)
translate_languages['values'] = ('Английский', 'Арабский', 'Армняский', 'Белорусский', 'Болгарский', 'Греческий', 'Датский', 'Иврит', 'Испанский', 'Итальянский', 'Казахский', 'Китайский', 'Корейский', 'Латышский', 'Литовский', 'Немецкий', 'Нидерландский', 'Норвежский', 'Польский', 'Португальский', 'Русский', 'Сербский', 'Словацкий', 'Словенский', 'Украинский', 'Финский', 'Французский', 'Хинди', 'Хорватский', 'Чешский', 'Шведский', 'Эстонский', 'Японский')
translate_languages.current(0)
translate_languages.place(x = 575, y = 25, width = 120, height = 25)
translate_box = scrolledtext.ScrolledText(state = 'disabled')
translate_box ['bg'] = 'gray20'
translate_box ['fg'] = 'white'
translate_box ['font'] = ('Arial', 10, 'bold')
translate_box ['relief'] = 'flat'
translate_box.place(x = 500, y = 75, width = 400, height = 88)
transliteration_label = Label(text = 'Транслитерация:')
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
t1 = threading.Thread(target=translate_button, args=())
t1.start()
window.mainloop()