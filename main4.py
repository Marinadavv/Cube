import speech_recognition as speech


x = input('Нажмите q чтобы начать ')


if x == 'q':
    r = speech.Recognizer() 
    
    micr = speech.Microphone() 
    speech.LANGUAGE = 'ru-Ru'


    with micr as source:
        
        r.adjust_for_ambient_noise(source)
    
        print('Запись началась')
        
        audio = r.listen(source)
    
    text = r.recognize_google(audio, language='ru-Ru')

    print(f'Вы сказали: {text}')
    
else:
    print('Такой команды нет!')
