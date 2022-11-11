import vk_api
import yandex_music
from time import sleep

VK = VKTOKENENV

Yandex = YANDEXTOKENENV

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
        print("Cannot catch track_ID.\n\n")
        return 0

def catch_label():
    try:
        track = catch_track()
        artists = ', '.join(track.artists_name())
        title = track.title
        return f"{artists} - {title}"
    except Exception as e:
        return 'Unknown track'

    
current = catch_label()
        
        
def set_status():
    api.status.set(text="Translation from Yandex Music: "+catch_label()+"\n\nGitHub: https://github.com/Kelthic/yandex-music-to-vkontakte-status")
    sleep(60)

while True:
   if catch_label() != current: 
        set_status()