import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random
import os
import pygame

pygame.init()

background_music = None
sound_channel = None

photo = None

def get_random_image_from_api():
    url = "https://nekos.best/api/v2/neko"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        if "results" in data and data["results"]:
            return data["results"][0]["url"]  
        else:
            print("No image URL found in API response")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request Exception: {e}")
        return None
    except ValueError as e:
        print(f"JSON Decode Error: {e}")
        return None

def play_background_music():
    global background_music
    if background_music is None:
        background_music = pygame.mixer.Sound("Bg/loop.mp3")  
        background_music.set_volume(0.62)  
        background_music.play(loops=-1)  

def play_random_sound():
    sounds_folder = "Sounds"
    sound_files = os.listdir(sounds_folder)
    if sound_files:
        random_sound = random.choice(sound_files)
        sound_path = os.path.join(sounds_folder, random_sound)
        sound = pygame.mixer.Sound(sound_path)
        sound.set_volume(1.0)  
        sound.play()


def display_random_image_from_api():
    global photo  
    
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.overrideredirect(True) 

    image_width = 700
    image_height = 450

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    def update_image_from_api():
        global photo  
        
        image_url = get_random_image_from_api()
        if image_url:
            try:

                response = requests.get(image_url)
                response.raise_for_status()  
                image_data = response.content  
                image = Image.open(BytesIO(image_data))

                image = image.resize((image_width, image_height), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)

                label.configure(image=photo)
                label.image = photo  

                new_x = random.randint(0, screen_width - image_width)
                new_y = random.randint(0, screen_height - image_height)
                root.geometry(f"{image_width}x{image_height}+{new_x}+{new_y}")

                play_random_sound()

                root.after(7500, update_image_from_api)
            except requests.exceptions.RequestException as e:
                print(f"Request Exception: {e}")
                root.after(7500, update_image_from_api)  
        else:
            print("No image URL received from API. Retrying in 15 seconds...")
            root.after(7500, update_image_from_api)

    label = tk.Label(root)
    label.pack()

    update_image_from_api()

    play_background_music()

    root.mainloop()

display_random_image_from_api()