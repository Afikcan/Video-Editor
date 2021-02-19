import pandas as pd
from moviepy.editor import *


data = pd.read_json(r'1610015685_output_3270.json')

pd_items = {}
pd_items['start_time'] = []
pd_items['end_time'] = []
pd_items['content'] = []
pd_items['type'] = []
for i in range(len(data['results']['items'])):
    # print(i, data['results']['items'][i], '\n')
    if data['results']['items'][i]['type'] == 'pronunciation':
        pd_items['start_time'].append(data['results']['items'][i]['start_time'])
        pd_items['end_time'].append(data['results']['items'][i]['end_time'])
        pd_items['content'].append(data['results']['items'][i]['alternatives'][0]['content'])
        pd_items['type'].append(data['results']['items'][i]['type'])
    elif data['results']['items'][i]['type'] == 'punctuation':
        pd_items['start_time'].append(None)
        pd_items['end_time'].append(None)
        pd_items['content'].append(data['results']['items'][i]['alternatives'][0]['content'])
        pd_items['type'].append(data['results']['items'][i]['type'])
    else:
        pass

pd_items = pd.DataFrame(pd_items)
print(pd_items)


pd_items_words ={}
pd_items_words['start_time'] = []
pd_items_words['end_time'] = []
pd_items_words['content'] = []
pd_items_words['type'] = []

pd_items_puncs ={}
pd_items_puncs['start_time'] = []
pd_items_puncs['end_time'] = []
pd_items_puncs['content'] = []
pd_items_puncs['type'] = []

for i in range(len(data['results']['items'])):
    #print(i, data['results']['items'][i], '\n')
    if data['results']['items'][i]['type'] == 'pronunciation':
        pd_items_words['start_time'].append(data['results']['items'][i]['start_time'])
        pd_items_words['end_time'].append(data['results']['items'][i]['end_time'])
        pd_items_words['content'].append(data['results']['items'][i]['alternatives'][0]['content'])
        pd_items_words['type'].append(data['results']['items'][i]['type'])
    elif data['results']['items'][i]['type'] == 'punctuation':
        pd_items_puncs['start_time'].append(None)
        pd_items_puncs['end_time'].append(None)
        pd_items_puncs['content'].append(data['results']['items'][i]['alternatives'][0]['content'])
        pd_items_puncs['type'].append(data['results']['items'][i]['type'])
    else:
        pass

pd_items_words = pd.DataFrame(pd_items_words)
#print(pd_items_words.to_string())

for i in range(len(pd_items_words)):
    pd_items_words.loc[i]['end_time'] = float(pd_items_words.loc[i]['end_time']) - 5
    pd_items_words.loc[i]['start_time'] = float(pd_items_words.loc[i]['start_time']) - 5

for i in range(len(pd_items_words)):
    if float(pd_items_words.loc[i]['end_time']) < 300:
        print(pd_items_words.loc[i])

clip = VideoFileClip("scripted_video.mp4")

for i in range(len(pd_items_words)):
    if float(pd_items_words.loc[i]['end_time']) < 300:
        if pd_items_words.loc[i]['content'] == "so" or pd_items_words.loc[i]['content'] == "So" or pd_items_words.loc[i]['content'] == "um" or pd_items_words.loc[i]['content'] == "Um" or pd_items_words.loc[i]['content'] == "okey" or pd_items_words.loc[i]['content'] == "Okey":
            star_time_tmp = pd_items_words.loc[i]['start_time']
            end_time_tmp = pd_items_words.loc[i]['end_time']
            clip = clip.cutout(star_time_tmp, end_time_tmp)
            print(i)

#"ah" or "uh" or "um" or "like" or "you know" or "I mean" or "okay" or "so" or "actually" or "basically" or "right"

clip.write_videofile("test.mp4")



#print(pd_items_puncs)






















