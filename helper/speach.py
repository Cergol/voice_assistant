import os
import time
import winsound
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'ru.dic')
)

#def which_word(word)
print("Say something!")

winsound.Beep(2500,200)

i=0
word=[]

time.sleep(1)

for phrase in speech:
    print(phrase)
    word.append(str(phrase))
    #word.append(' ')
    i=i+1
    print(i)
    
    a=len(word)
    if str(word[a-1])== "пока":
        break
    time.sleep(0.1)

print(word)
