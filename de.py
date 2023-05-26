from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
def button_settings():
    def button_dark_theme():
        window ['bg'] = 'gray10'
        buttonsettings ['bg'] = 'gray20'
        buttonsettings ['fg'] = 'white'
        input_label ['bg'] = 'gray10'
        input_label ['fg'] = 'white'
        input_box ['bg'] = 'gray20'
        input_box ['fg'] = 'white'
        translate_label ['bg'] = 'gray10'
        translate_label ['fg'] = 'white'
        translate_box ['bg'] = 'gray20'
        translate_box ['fg'] = 'white'
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
        window ['bg'] = 'gray90'
        buttonsettings ['bg'] = 'white'
        buttonsettings ['fg'] = 'black'
        input_label ['bg'] = 'gray90'
        input_label ['fg'] = 'black'
        input_box ['bg'] = 'white'
        input_box ['fg'] = 'black'
        translate_label ['bg'] = 'gray90'
        translate_label ['fg'] = 'black'
        translate_box ['bg'] = 'white'
        translate_box ['fg'] = 'black'
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
        print()
    window1 = Tk()
    window1.title('Einstellungen')
    window1.geometry('305x105')
    window1 ['bg'] = 'gray20'
    label_languages = Label(window1, text = 'Hauptsprache:')
    label_languages ['bg'] = 'gray20'
    label_languages ['fg'] = 'white'
    label_languages ['font'] = ('Arial', 10, 'bold')
    label_languages.place(x = 10, y = 10, width = 125, height = 25)
    set_languages = Combobox(window1, width = 10, height = 25)
    set_languages['values'] = ('Deutsch', 'English', 'Español', 'Français', 'Italiano', 'Polski', 'Suomi', 'Беларуская', 'Русский', 'Ελληνικά', 'Հայերեն', 'עִבְרִית', 'اَلْعَرَبِيَّةُ', '中文', '日本語')  
    set_languages.current(0)
    set_languages.place(x = 135, y = 10, width = 100, height = 25)
    label_themes = Label(window1, text = 'Hauptthema:')
    label_themes ['bg'] = 'gray20'
    label_themes ['fg'] = 'white'
    label_themes ['font'] = ('Arial', 10, 'bold')
    label_themes.place(x = 10, y = 35, width = 125, height = 25)
    theme_dark = Radiobutton(window1, text = 'Dunkles', value = 0, command = button_dark_theme)
    theme_dark ['bg'] = 'gray20'
    theme_dark ['fg'] = 'white'
    theme_dark ['font'] = ('Arial', 10, 'bold')
    theme_dark.place(x = 135, y = 35, width = 75, height = 25)
    theme_light = Radiobutton(window1, text = 'Licht', value = 1, command = button_light_theme)
    theme_light ['bg'] = 'gray20'
    theme_light ['fg'] = 'white'
    theme_light ['font'] = ('Arial', 10, 'bold')
    theme_light.place(x = 210, y = 35, width = 75, height = 25)
    applybutton = Button(window1, text = 'Anwenden', command = button_apply)
    applybutton ['bg'] = 'gray20'
    applybutton ['fg'] = 'white'
    applybutton ['font'] = ('Arial', 10, 'bold')
    applybutton ['relief'] = 'raised'
    applybutton.place(x = 105, y = 70, width = 100, height = 25)
window = Tk()
window.title('Übersetzer')
window.geometry('950x325')
window ['bg'] = 'gray10'
buttonsettings = Button(text = '⚙', command = button_settings)
buttonsettings ['bg'] = 'gray20'
buttonsettings ['fg'] = 'white'
buttonsettings ['font'] = ('Arial', 15, 'bold')
buttonsettings ['relief'] = 'raised'
buttonsettings.place(x = 10, y = 10, width = 30, height = 30)
input_label = Label(text = 'Text eingeben:')
input_label ['bg'] = 'gray10'
input_label ['fg'] = 'white'
input_label ['font'] = ('Arial', 10, 'bold')
input_label ['justify'] = 'center'
input_label.place(x = 50, y = 25, width = 110, height = 25)
input_languages = Combobox(window)
input_languages['values'] = ('Arabisch', 'Armenisch', 'Belarussisch', 'Chinesisch', 'Deutsch', 'Englisch', 'Finnisch', 'Französisch', 'Griechisch', 'Hebräisch', 'Italienisch', 'Japanisch', 'Polieren', 'Russisch', 'Spanisch')  
input_languages.current(4)
input_languages.place(x = 160, y = 25, width = 100, height = 25)
input_box = scrolledtext.ScrolledText()
input_box ['bg'] = 'gray20'
input_box ['fg'] = 'white'
input_box ['font'] = ('Arial', 10, 'bold')
input_box ['relief'] = 'flat'
input_box.place(x = 50, y = 75, width = 400, height = 200)
translate_label = Label(text = 'Übersetzerung:')
translate_label ['bg'] = 'gray10'
translate_label ['fg'] = 'white'
translate_label ['font'] = ('Arial', 10, 'bold')
translate_label ['justify'] = 'center'
translate_label.place(x = 500, y = 25, width = 110, height = 25)
translate_languages = Combobox(window)
translate_languages['values'] = ('Arabisch', 'Armenisch', 'Belarussisch', 'Chinesisch', 'Deutsch', 'Englisch', 'Finnisch', 'Französisch', 'Griechisch', 'Hebräisch', 'Italienisch', 'Japanisch', 'Polieren', 'Russisch', 'Spanisch')    
translate_languages.current(5)
translate_languages.place(x = 610, y = 25, width = 100, height = 25)
translate_box = scrolledtext.ScrolledText()
translate_box ['bg'] = 'gray20'
translate_box ['fg'] = 'white'
translate_box ['font'] = ('Arial', 10, 'bold')
translate_box ['relief'] = 'flat'
translate_box.place(x = 500, y = 75, width = 400, height = 200)
window.mainloop()