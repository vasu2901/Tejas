import asyncio
import getpass
import os
import random
import smtplib
import subprocess
import webbrowser
from datetime import datetime
import bluetooth

import PyDictionary
import cv2
import language_tool_python
import python_weather
import python_weather.response
import pyttsx3
import pywhatkit
import qrcode
import screen_brightness_control
import speech_recognition as sr
import wikipedia
import winshell

listener = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.runAndWait()


def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


talk('Hello Sir. What can I do for you?')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            engine.runAndWait()
            return command
    except:
        pass


date = datetime.now()
print(date)


def run_tejas():
    user_name = getpass.getuser()
    v = take_command()
    print(v)
    if "tejas goodbye" in v:
        talk('goodbye sir')
        quit()
    else:
        # for doing generous calculation.
        if 'add' in v:
            t = v.split('add')[-1]
            k = t.split('and')
            sum = 0
            for i in range(len(k)):
                sum += int(k[i])
            talk(sum)
        elif 'subtract' in v:
            t = v.split('subtract')[-1]
            k = t.split('from')
            minus = int(k[0])
            for i in range(1, len(k)):
                minus -= int(k[i])
            talk(minus)
        elif 'multiply' in v:
            t = v.split('multiply')[-1]
            k = t.split('and')
            multiply = 1
            for i in range(len(k)):
                multiply = multiply * int(k[i])
            talk(multiply)
        elif 'divide' in v:
            t = v.split('divide')[-1]
            k = t.split('by')
            talk(int(k[0]) / int(k[1]))
        elif 'calculate percentage' in v:
            t = v.split('calculate percentage of')[1]
            k = t.split('in')
            x = (int(k[0]) / int(k[1])) * 100
            talk(x)
        elif 'create' in v:
            if 'new' in v:
                x = v.split("new ")[1]
                if 'excel' in x:
                    talk('please type name of file')
                    talk("please say after listening appears")
                    name = take_command()
                    z = "C:\\Users\\{}\\OneDrive\\Desktop\\{}.csv".format(user_name, name)
                    open(z, "a")
                    talk("opening {}.xlsx".format(name))
                    os.system("start {}".format(z))
                elif 'word' in v:
                    talk('please type name of file')
                    talk("please say after listening appears")
                    name = take_command()
                    z = "C:\\Users\\{}\\OneDrive\\Desktop\\{}.docx".format(user_name, name)
                    open(z, "a")
                    talk("opening {}.docx".format(name))
                    os.system("start {}".format(z))
                elif 'power point' or 'powerpoint' in v:
                    talk('please type name of file')
                    talk("please say after listening appears")
                    name = take_command()
                    z = "C:\\Users\\{}\\OneDrive\\Desktop\\{}.pptx".format(user_name, name)
                    open(z, "a")
                    talk("opening {}.pptx".format(name))
                    os.system("start {}".format(z))
                elif 'onenote' in v:
                    talk('please type name of file')
                    talk("please say after listening appears")
                    name = take_command()
                    z = "C:\\Users\\{}\\OneDrive\\Desktop\\{}.one".format(user_name, name)
                    open(z, "a")
                    talk("opening {}.one".format(name))
                    os.system("start {}".format(z))
                elif 'notepad' in v:
                    talk('please type name of file')
                    talk("please say after listening appears")
                    name = take_command()
                    z = "C:\\Users\\{}\\OneDrive\\Desktop\\{}.txt".format(user_name, name)
                    open(z, 'w')
                    talk("opening {}.txt".format(name))
                    os.system("start {}".format(z))
                else:
                    talk("Sorry but couldn't process it.")
        # for playing songs and movies
        elif 'play' in v:
            t = v.split('play song')[-1]
            talk('playing sir')
            pywhatkit.playonyt(t)
        elif 'tell me' in v:
            if 'about' in v:
                if 'yourself' in v:
                    talk('Namaste. Mera Naam Tejaas hai. Aapse Milkaar khushi huee.')
                elif 'weather' in v:
                    talk('please type your current location')
                    location = input('enter your location>>> ')
                    if "today's weather" in v:
                        async def getweather():
                            # declare the client. format defaults to metric system (celcius, km/h, etc.)
                            client = python_weather.Client(format=python_weather.IMPERIAL)

                            # fetch a weather forecast from a city
                            weather = await client.find(location)

                            # returns the current day's forecast temperature (int)
                            if weather.current.sky_text[-1] == 'g':
                                talk('It will be {}gy today'.format(weather.current.sky_text))
                            elif weather.current.sky_text[-1] == 'n':
                                talk('It will be {}ny today'.format(weather.current.sky_text))
                            else:
                                talk('It will be {} today'.format(weather.current.sky_text))
                            # get the weather forecast for a few days
                            # close the wrapper once done
                            await client.close()

                        if __name__ == "__main__":
                            loop = asyncio.get_event_loop()
                            loop.run_until_complete(getweather())
                    else:
                        async def getweather():
                            # declare the client. format defaults to metric system (celcius, km/h, etc.)
                            client = python_weather.Client(format=python_weather.IMPERIAL)

                            # fetch a weather forecast from a city
                            weather = await client.find(location)

                            # returns the current day's forecast temperature (int)
                            talk('please refer to the data given below')

                            # get the weather forecast for a few days
                            for forecast in weather.forecasts:
                                talk(str(forecast.date), forecast.sky_text, forecast.temperature)

                            # close the wrapper once done
                            await client.close()

                        if __name__ == "__main__":
                            loop = asyncio.get_event_loop()
                            loop.run_until_complete(getweather())
                else:
                    s = v.split('tell me about')[-1]
                    talk('here it is')
                    talk(wikipedia.summary(s, 3))
            elif 'meaning' in v:
                s = v.split(" of ")[1]
                x = PyDictionary.PyDictionary.meaning(s)
                talk(x)
            elif "synonyms" or 'synonym' in v:
                from nltk.corpus import wordnet
                word = v.split(" of ")[1]
                synonyms = list()
                for syn in wordnet.synsets(word):
                    for l in syn.lemmas():
                        synonyms.append(l.name())
                synonym = list(set(synonyms))
                print(synonym)
                for i in range(len(synonym[:5])):
                    talk(synonym[i])
            elif 'antonyms' or 'antonym' in v:
                from nltk.corpus import wordnet
                word = v.split(" of ")[1]
                antonyms = list()
                for syn in wordnet.synsets(word):
                    for l in syn.lemmas():
                        antonyms.append(l.name())
                antonyms = list(set(antonyms))
                for i in range(len(antonyms[:5])):
                    talk(antonyms[i])
            elif 'time' in v:
                time0 = datetime.now()
                time = time0.strftime("%H:%M:%S")
                talk(time)
            else:
                talk('this is what I found out.')
                webbrowser.open('https://www.google.com/search?q={}'.format(v))
        elif 'who is' in v:
            s = v.split('who is')[-1]
            talk('here it is')
            talk(wikipedia.summary(s, 2))
        elif 'who are' in v:
            s = v.split('who are')[-1]
            talk('here it is')
            talk(wikipedia.summary(s, 2))
        elif 'what' in v:
            if 'is' or 'are' in v:
                try:
                    if 'time' in v:
                        time0 = datetime.now()
                        time = time0.strftime("%H:%M:%S")
                        talk(time)
                    elif 'date' in v:
                        date2 = datetime.now()
                        talk("today's date is {}".format(date2))
                    elif 'meaning' in v:
                        s = v.split(" of ")[1]
                        x = PyDictionary.PyDictionary.meaning(s)
                        talk(x)
                    elif "synonyms" or 'synonym' in v:
                        from nltk.corpus import wordnet
                        word = v.split(" of ")[1]
                        synonyms = list()
                        for syn in wordnet.synsets(word):
                            for l in syn.lemmas():
                                synonyms.append(l.name())
                        synonym = list(set(synonyms))
                        print(synonym)
                        for i in range(len(synonym[:5])):
                            talk(synonym[i])
                    elif 'antonyms' or 'antonym' in v:
                        from nltk.corpus import wordnet
                        word = v.split(" of ")[1]
                        antonyms = list()
                        for syn in wordnet.synsets(word):
                            for l in syn.lemmas():
                                antonyms.append(l.name())
                        antonyms = list(set(antonyms))
                        for i in range(len(antonyms[:5])):
                            talk(antonyms[i])
                except:
                    s = v.split('what is')[-1]
                    talk('here it is')
                    wikipedia.summary(s, 5)
                    talk(wikipedia.summary(s, 5))
            elif 'will be' in v:
                if "today's temperature" in v:
                    talk('please type your current location')
                    location = input('enter your location>>>')

                    async def getweather():
                        # declare the client. format defaults to metric system (celcius, km/h, etc.)
                        client = python_weather.Client(format=python_weather.IMPERIAL)

                        # fetch a weather forecast from a city
                        weather = await client.find(location)

                        # returns the current day's forecast temperature (int)
                        talk("today's temperature will be {} degree fahrenheit.".format(weather.current.temperature))
                        # close the wrapper once done
                        await client.close()

                    if __name__ == "__main__":
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(getweather())
                else:
                    talk('please refer to the data given below')

                    # import the module

                    async def getweather():
                        # declare the client. format defaults to metric system (celcius, km/h, etc.)
                        client = python_weather.Client(format=python_weather.IMPERIAL)

                        # fetch a weather forecast from a city
                        weather = await client.find("Meerut")
                        # get the weather forecast for a few days
                        for forecast in weather.forecasts:
                            talk(str(forecast.date), forecast.sky_text, forecast.temperature)

                        # close the wrapper once done
                        await client.close()

                    if __name__ == "__main__":
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(getweather())
        elif 'will' in v:
            if 'you' in v:
                if 'marry me' or 'love me' or 'hate me' in v:
                    talk('Ummmm I will think about this later. What else can I do for you?')
                elif 'be my friend' in v:
                    talk("Yes I'm your friend.")
                elif 'help me' in v:
                    webbrowser.open("https://www.google.com/search?q={}".format(v))
            elif 'rainy' or 'sunny' or 'windy' or 'cold' or 'haze' or ' fog' or 'raining' in v:

                talk('please type your current location')
                location = input('enter your location>>> ')

                async def getweather():
                    client = python_weather.Client(format=python_weather.IMPERIAL)

                    # fetch a weather forecast from a city
                    weather = await client.find(location)

                    # returns the current day's forecast temperature (int)
                    if weather.current.sky_text[-1] == 'g':
                        talk('It will be {}gy today'.format(weather.current.sky_text))
                    elif weather.current.sky_text[-1] == 'n':
                        talk('It will be {}ny today'.format(weather.current.sky_text))
                    else:
                        talk('It will be {} today'.format(weather.current.sky_text))
                    # get the weather forecast for a few days
                    # close the wrapper once done
                    await client.close()

                if __name__ == "__main__":
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(getweather())
        # for counting back
        elif 'countdown' in v:
            time = int(v.split(" to ")[1])
            print(time)
            while time > 0:
                talk(time)
                time = time - 1
        # for opening files and applications.
        elif 'start' in v:
            x = v.split('start')[-1]
            app_name = x.title()
            try:
                os.system("start {}.exe".format(app_name))
            except:
                talk('sorry but could not open')
        elif 'open' in v:
            print(user_name)
            if 'file' in v:
                import win32api
                drives = win32api.GetLogicalDriveStrings()
                drives = drives.split('\000')[::-1]
                x = drives[1:]
                result = []
                talk("Enter the name of file with its domain name like.xlsx for excel etc")
                file_name = input("Enter the name of file with its domain name like.xlsx for excel etc.-->")
                try:
                    for root, dir, files in os.walk(x[0]):
                        if file_name in files:
                            talk("File found.")
                            result.append(os.path.join(root, file_name))
                            os.system("start {}".format(result[0]))
                            break
                except:
                    for root, dir, files in os.walk(x[1]):
                        if file_name in files:
                            result.append(os.path.join(root, file_name))
                            talk("File found.")
                            os.system("start {}".format(result[0]))
                            break
                try:
                    for root, dir, files in os.walk(x[-1]):
                        if file_name in files:
                            result.append(os.path.join(root, file_name))
                            talk("File found.")
                            os.system("start {}".format(result[0]))
                            break
                except:
                    talk("File not found.")
            elif 'folder' in v:
                talk('please type the name of folder and its sub folder if any')
                folder = input("enter the name of folder")
                sub_folder = input('enter the name of sub folder')
                if sub_folder == "No":
                    try:
                        os.system("start C:\\Users\\Vighneshvats\\OneDrive\\Desktop\\{}".format(folder))
                    except:
                        talk('Sorry I could not find your folder')
                else:
                    try:
                        os.system("start C:\\Users\\Vighneshvats\\OneDrive\\Desktop\\{}\\{}".format(folder, sub_folder))
                    except:
                        talk('Sorry I could not find your folder')
            elif 'microsoft' or 'ms' in v:
                if 'microsoft' in v:
                    talk('here it is')
                    if 'excel' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                    elif 'word' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                    elif 'teams' in v:
                        subprocess.call(
                            'C:\\Users\\' + user_name + '\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"')
                    elif 'one note' or 'onenote' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")
                    elif 'power point' or 'powerpoint' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                    elif 'edge' in v:
                        subprocess.call('"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"')
                elif 'ms' in v:
                    talk('here it is')
                    if 'excel' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
                    elif 'word' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
                    elif 'powerpoint' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
                    elif 'teams' in v:
                        subprocess.call(
                            'C:\\Users\\' + user_name + '\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"')
                    elif 'edge' in v:
                        subprocess.call('"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"')
                    elif 'one note' or 'onenote' in v:
                        subprocess.call("C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE")
            elif 'settings' in v:
                os.system("start ms-settings:")
            elif 'file explorer' in v:
                subprocess.call("explorer-")
            elif 'camera' in v:
                os.system("start microsoft.windows.camera:")
            else:
                x = v.split(" open ")[0]
                os.system("start {}.exe".format(x))
        elif 'brightness' in v:
            s = v.split('to')[-1]
            if '2' not in s:
                talk('setting brightness to {}'.format(s))
                screen_brightness_control.set_brightness(int(s))
            elif "2" in v:
                s = v.split('brightness')[1]
                s = int(s) - 200
                talk('setting brightness to {}'.format(s))
                screen_brightness_control.set_brightness(int(s))
        elif 'game' in v:
            if 'tic tac toe' in v:
                player1 = input("enter player 1 name>>>")
                sign1 = input("enter player 1 sign>>>")
                player2 = 'tejas'
                turns = 9
                l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                l = ["_", "_", "_",
                     "_", "_", "_",
                     "_", "_", "_"]
                print(l[0], l[1], l[2])
                print(l[3], l[4], l[5])
                print(l[6], l[7], l[8])
                talk("Let's play tic tac toe game {}".format(player1))
                engine.runAndWait()
                if sign1 == 'x':
                    sign2 = 'o'
                else:
                    sign2 = 'x'
                for i in range(turns):
                    if i % 2 != 0:
                        with sr.Microphone() as source3:
                            print('say now>>>')
                            voice3 = listener.listen(source3)
                            n = listener.recognize_google(voice3)
                        n = int(n)
                        if n in l2:
                            l2.remove(n)
                            l[n - 1] = sign1
                            print("columns remaining", l2, "\n")
                            print(l[0], l[1], l[2])
                            print(l[3], l[4], l[5])
                            print(l[6], l[7], l[8])
                            if l[0] == l[1] == l[2]:
                                if l[0] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[0] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[3] == l[4] == l[5]:
                                if l[3] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[3] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[6] == l[7] == l[8]:
                                if l[6] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[6] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[0] == l[3] == l[6]:
                                if l[0] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[0] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[1] == l[4] == l[7]:
                                if l[1] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[1] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[2] == l[5] == l[8]:
                                if l[2] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[2] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[0] == l[4] == l[8]:
                                if l[0] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[0] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[2] == l[4] == l[6]:
                                if l[2] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[2] == sign2:
                                    talk(player2 + "wins")
                                    break
                    elif i % 2 == 0:
                        n = int(random.choice(l2))
                        talk(n)
                        if n in l2:
                            l2.remove(n)
                            l[n - 1] = sign2
                            print("columns remaining", l2, "\n")
                            print()
                            print(l[0], l[1], l[2])
                            print(l[3], l[4], l[5])
                            print(l[6], l[7], l[8])
                            if l[0] == l[1] == l[2]:
                                if l[0] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[0] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[3] == l[4] == l[5]:
                                if l[3] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[3] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[6] == l[7] == l[8]:
                                if l[6] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[6] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[0] == l[3] == l[6]:
                                if l[0] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[0] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[1] == l[4] == l[7]:
                                if l[1] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[1] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[2] == l[5] == l[8]:
                                if l[2] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[2] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[0] == l[4] == l[8]:
                                if l[0] == sign1:
                                    talk(player1 + "wins")
                                    break
                                elif l[0] == sign2:
                                    talk(player2 + "wins")
                                    break
                            elif l[2] == l[4] == l[6]:
                                if l[2] == sign1:
                                    talk(player1 + "wins")
                                    break
                                else:
                                    talk(player2 + "wins")
                                    break
                    if not l2:
                        talk("draw")
            elif 'rock paper scissor' or 'rock paper scissors ' in v:
                word = ["scissor", "rock", "paper"]
                talk('please choose a word')
                with sr.Microphone() as source2:
                    print('Say Now!!!')
                    voice1 = listener.listen(source2)
                    word2 = listener.recognize_google(voice1)
                word2 = word2.lower()
                word1 = random.choice(word)
                print(word1)
                if word1 == "rock":
                    if word2 == "paper":
                        talk("you win")
                    elif word2 == "scissor":
                        talk("you lost. Try again")
                    else:
                        talk("It's a draw")
                elif word1 == "paper":
                    if word2 == "scissor":
                        talk("you win")
                    elif word2 == "rock":
                        talk("you lost")
                    else:
                        talk("It's a draw")
                elif word1 == "scissor":
                    if word2 == "paper":
                        talk("you lost")
                    elif word2 == "rock":
                        talk("you win")
                    else:
                        talk("It's a draw")
        # for general communication
        elif 'i am fine' in v:
            talk('Good to hear that.What can I do for you?')
        elif 'when' in v:
            if 'did' in v:
                s = v.split('when did')[-1]
                talk('here it is')
                webbrowser.open("https://www.google.com/search?q={}".format(s))
        elif 'send an email' in v:
            talk("please check whether you have allowed less security app access for your gmail account")
            option = take_command().lower()
            if "yes" in option:
                talk("please type your email id, your password, receiver's address and message.")
                sender_address = input("enter your id>>>")
                password = input("enter your password")
                receiver_address = input("enter receiver's id>>>")
                talk("please say your message after Listening appears")
                message = take_command()
                talk("your message is : {}".format(message))
                talk('is this right?')
                x = input("please type Yes or No")
                if x == "Yes":
                    server = smtplib.SMTP("smtp.gmail.com", 587)
                    server.starttls()
                    server.login(sender_address, password)
                    server.sendmail(sender_address, receiver_address, message)
                    talk("message sent")
                else:
                    talk("please pardon your message.")
                    message = input("enter your message")
                    talk("your message is : {}".format(message))
                    talk('is this right?')
                    x = input("please type Yes or No")
                    if x == "Yes":
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender_address, password)
                        server.sendmail(sender_address, receiver_address, message)
                        talk("message sent")
            elif "no" in option:
                talk("please follow the instructions")
                for i in range(5):
                    engine.runAndWait()
                talk("please go to your gmail account setting.")
                for i in range(5):
                    engine.runAndWait()
                talk('after opening settings go to your security tab and turn of 2-step verification.')
                for i in range(5):
                    engine.runAndWait()
                talk("after doing so scroll down and you will find less security app access. Please turn it on.")
                for i in range(5):
                    engine.runAndWait()
                try:
                    talk("please provide us your email id, your password, receiver's address and message.")
                    sender_address = input("enter your id>>>")
                    password = input("enter your password")
                    receiver_address = input("enter receiver's id>>>")
                    talk("please say your message after Listening appears")
                    engine.runAndWait()
                    message = take_command()
                    talk("your message is : {}".format(message))
                    talk('is this right?')
                    x = input("please type Yes or No")
                    if x == "Yes":
                        server = smtplib.SMTP("smtp.gmail.com", 587)
                        server.starttls()
                        server.login(sender_address, password)
                        server.sendmail(sender_address, receiver_address, message)
                        talk("message sent")
                    else:
                        talk("please pardon your message.")
                        message = input("enter your message")
                        talk("your message is : {}".format(message))
                        talk('is this right?')
                        x = input("please type Yes or No")
                        if x == "Yes":
                            server = smtplib.SMTP("smtp.gmail.com", 587)
                            server.starttls()
                            server.login(sender_address, password)
                            server.sendmail(sender_address, receiver_address, message)
                            talk("message sent")
                except:
                    talk("sorry I am not able to do so.")
                    webbrowser.open("https://mail.google.com/mail/u/0/#inbox?compose=new")
        elif 'search' in v:
            r = v.split('search')[-1]
            webbrowser.open("https://www.google.com/search?q={}".format(r))
        elif 'close' in v:
            t = v.split('close')[-1]
            if t != 'word' or 'power point' or 'power point':
                os.system("TASKKILL /F /IM {}.EXE".format(t))
                talk('{} closed'.format(t))
            elif t == 'word':
                os.system("TASKKILL /F /IM Winword.exe")
                talk('{} closed'.format(t))
            elif t == 'power point' or 'powerpoint':
                os.system("TASKKILL /F /IM POWERPNT.EXE")
                talk('{} closed'.format(t))
        elif 'how' in v:
            if 'to' in v:
                s = v.split('how to')
                if 'reach' in v:
                    s = v.split('how to reach')[-1]
                    t = s.split('from')
                    talk('here it is')
                    webbrowser.open("https://www.google.com/maps/dir/{}/{}".format(t[1], t[0]))
                else:
                    talk('here it is')
                    webbrowser.open("https://www.google.com/search?q={}".format(s))
            elif 'are you' in v:
                talk('I am fine. Thank you. What about you?')

                # for closing a program
            # for scheduling special events on specific dates
            elif 'date' in v:
                date2 = datetime.now()
                if '01-29' in date2:
                    talk('happy birthday sir')
                elif '02-20' in date2:
                    talk('happy wedding anniversary mom and dad')
                elif '09-22' in date2:
                    talk('happy birthday papa')
                elif '10-16' in date2:
                    talk('happy birthday gauri')
                elif '11-16' in date2:
                    talk('happy birthday mom')
            elif 'time' in v:
                time0 = datetime.now()
                time = time0.strftime("%H:%M:%S")
                talk("current time is {}".format(time))
        elif 'greet everyone' in v:
            talk('Hello Everyone. My name is Tejas')
        elif 'introduce yourself' in v:
            talk('Hello Everyone. My name is Tejas. I am created by Vighnesh Vasu Vats. Nice to meet you.')
        elif 'empty recycle bin' in v or 'empty recycle bin' in v:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            talk("Recycle Bin Emptied")
        # for generating passwords, otp,  and qr codes.
        elif 'generate' in v:
            t = int(v.split('length')[1])
            if 'password' in v:
                n = t
                x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
                                                                            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                     'v',
                     'w', 'x', 'y', 'z']
                s = ['@', "#", "$", "%", "&", "*", "^"]
                if n % 2 == 0:
                    if n % 4 == 0:
                        for i in range(0, round(n / 4)):
                            v = random.choice(x)
                            y = random.choice(x).upper()
                            talk(v, y, end=" ")
                        for i in range(round(n / 2) - 1):
                            z = random.randint(0, 9)
                            talk(z, end=" ")
                        talk(random.choice(s))
                    else:
                        for i in range(0, int(n / 4)):
                            v = random.choice(x)
                            y = random.choice(x).upper()
                            talk(v, y, end=" ")
                        for i in range(round(n / 2)):
                            z = random.randint(0, 9)
                            talk(z, end=" ")
                        talk(random.choice(s))
                else:
                    if '.25' in str(n / 4):
                        for i in range(0, round(n / 4)):
                            v = random.choice(x)
                            y = random.choice(x).upper()
                            talk(v, y, end=" ")
                        for i in range(round(n / 2)):
                            z = random.randint(0, 9)
                            talk(z, end=" ")
                        talk(random.choice(s))
                    else:
                        for i in range(0, round(n / 4) - 1):
                            v = random.choice(x)
                            y = random.choice(x).upper()
                            talk(v, y, end=" ")
                        for i in range(round(n / 2)):
                            z = random.randint(0, 9)
                            talk(z, end=" ")
                        talk(random.choice(s))
            elif 'otp' in v:
                l = list()
                for i in range(t):
                    x = random.randint(0, 9)
                    l.append(x)
                print(l)
                talk(l)
            elif 'qr code' or 'qrcode' in v:
                y2 = input("enter the code")
                x2 = input("enter the name") + ".jpg"
                v = qrcode.make(y2)
                v.save(x2)
        elif 'check grammar' in v:
            text = v.split("check grammar in ")[1]
            tool = language_tool_python.LanguageTool('en-US')
            matches = tool.check(text)
            print(matches)
        elif 'connect to ' in v:
            if 'bluetooth device' in v:
                talk("opening bluetooth")
                try:
                    z = bluetooth.pair_device("GIZMO402", 2)
                    print(z)
                except:
                    os.system("start ms-settings-bluetooth:")
            elif 'wifi' or 'wi-fi' in v:
                # function to establish a new connection
                def createNewConnection(name2, SSID, password1):
                    config = """<?xml version=\"1.0\"?>
                <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
                	<name>""" + name2 + """</name>
                	<SSIDConfig>
                		<SSID>
                			<name>""" + SSID + """</name>
                		</SSID>
                	</SSIDConfig>
                	<connectionType>ESS</connectionType>
                	<connectionMode>auto</connectionMode>
                	<MSM>
                		<security>
                			<authEncryption>
                				<authentication>WPA2PSK</authentication>
                				<encryption>AES</encryption>
                				<useOneX>false</useOneX>
                			</authEncryption>
                			<sharedKey>
                				<keyType>passPhrase</keyType>
                				<protected>false</protected>
                				<keyMaterial>""" + password1 + """</keyMaterial>
                			</sharedKey>
                		</security>
                	</MSM>
                </WLANProfile>"""
                    command = "netsh wlan add profile filename=\"" + name2 + ".xml\"" + " interface=Wi-Fi"
                    with open(name2 + ".xml", 'w') as file1:
                        file1.write(config)
                    os.system(command)

                # function to connect to a network
                def connect(name1, SSID):
                    command = "netsh wlan connect name=\"" + name1 + "\" ssid=\"" + SSID + "\" interface=Wi-Fi"
                    os.system(command)

                # function to display available Wi-Fi networks
                def displayAvailableNetworks():
                    command = "netsh wlan show networks interface=Wi-Fi"
                    os.system(command)

                # display available networks
                displayAvailableNetworks()

                # input Wi-Fi name and password
                name = input("Name of Wi-Fi: ")
                password = input("Password: ")

                # establish new connection
                createNewConnection(name, name, password)

                # connect to the Wi-Fi network
                connect(name, name)
                talk("If you aren't connected to this network, try connecting with the correct password!")
        elif 'meaning' in v:
            s = v.split(" of ")[1]
            x = PyDictionary.PyDictionary.meaning(s)
            talk(x)
        elif "synonyms" or 'synonym' in v:
            from nltk.corpus import wordnet
            word = v.split(" of ")[1]
            synonyms = list()
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    synonyms.append(l.name())
            synonym = list(set(synonyms))
            print(synonym)
            for i in range(len(synonym[:5])):
                talk(synonym[i])
        elif 'antonyms' or 'antonym' in v:
            from nltk.corpus import wordnet
            word = v.split(" of ")[1]
            antonyms = list()
            for syn in wordnet.synsets(word):
                for l in syn.lemmas():
                    antonyms.append(l.name())
            antonyms = list(set(antonyms))
            for i in range(len(antonyms[:5])):
                talk(antonyms[i])
        elif "alarm" in v:
            alarm_hour = int(input("enter the hour in 24 hour format ->>"))
            alarm_minute = int(input("enter the minutes in two integer format ->>"))
            if alarm_hour > 12:
                if alarm_minute == 00:
                    talk("setting an alarm for {} pm".format(alarm_hour - 12))
                else:
                    talk("setting an alarm for {}:{} pm".format(alarm_hour - 12, alarm_minute))
            elif alarm_hour == 12:
                if alarm_minute == 00:
                    talk("setting an alarm for {} noon".format(alarm_hour))
                else:
                    talk("setting an alarm for {}:{} pm".format(alarm_hour - 12, alarm_minute))
            elif alarm_hour == 00 or alarm_hour == 24:
                if alarm_minute == 00:
                    talk("setting an alarm for Midnight ")
                else:
                    talk("setting an alarm for 00:{} am".format(alarm_minute))
            else:
                if alarm_minute == 00:
                    talk("setting an alarm for {} am".format(alarm_hour))
                else:
                    talk("setting an alarm for {}:{} am".format(alarm_hour, alarm_minute))
            while 1:
                time = datetime.now()
                current_hour = int(time.strftime("%H"))
                current_minute = int(time.strftime("%M"))
                while alarm_minute != current_minute and alarm_hour != current_hour:
                    continue
                pywhatkit.playonyt("Hawayein")
                break
        elif 'shutdown' in v:
            os.system("Shutdown -s")
        elif 'restart' in v:
            os.system("Shutdown -R")
        elif 'log off' or 'logoff' or 'lockwindow' or 'lock window' in v:
            talk("logging off")
            os.system("Shutdown -L")
        elif 'click a photo' or 'camera' or 'take a photo' or 'capture a photo' in v:
            video_capture_object = cv2.VideoCapture(0)
            x = str(datetime.now())
            print(x)
            result = True
            while result:
                ret, frame = video_capture_object.read()
                cv2.imwrite("x.jpg", frame)
                result = False
            video_capture_object.release()
            cv2.destroyAllWindows()
            os.system("x.jpg")
        elif 'cancel' or 'abort' or 'stop' in v:
            os.system("Shutdown -A")
            talk("Aborted")
        # for reading qr code.
        elif 'read qrcode' or 'read qr code' in v:
            x2 = input("enter the name") + ".jpg"
            d = cv2.QRCodeDetector()
            val, _, _ = d.detectAndDecode(cv2.imread(x2))
            talk("Decoded text is:{}".format(val))
        else:
            talk("Here it is")
            webbrowser.open("https://www.google.com/search?q={}".format(v))


while True:
    run_tejas()
