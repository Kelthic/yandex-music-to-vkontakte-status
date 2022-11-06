import vk_api
import yandex_music
from time import sleep
import datetime 

VK = 'pasteyourtoken'

Yandex = 'pasteyourtoken'

client = yandex_music.Client(Yandex).init()

api = vk_api.VkApi(token=VK).get_api()

def catch_track():
    try:
        queues = client.queues_list()
        last_queue = client.queue(queues[0].id)
        track_id = last_queue.get_current_track()
        track = track_id.fetch_track()
        return track
    except Exception as e:
        print("Cannot catch trackID. Restart programm.\n\n")
        return 0

def catch_label():
    try:
        track = catch_track()
        artists = ', '.join(track.artists_name())
        title = track.title
        return f"{artists} - {title}"
    except Exception as e:
        return 'No track'

    
current = catch_label()
        

while True:
    if catch_label() != current: 
        api.status.set(text="Translation from Yandex Music: "+catch_label())
        sleep(20)
