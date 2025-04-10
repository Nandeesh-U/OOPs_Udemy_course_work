from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO


Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def google_image_search(self):
        query = self.manager.current_screen.ids.search_input.text
        search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Find image URLs
        image_tags = soup.find_all("img")
        image_urls = [img["src"] for img in image_tags if img["src"].startswith("http")]

        return image_urls[0]  # Return top image URL

    def download_image(self):
        response = requests.get(self.google_image_search())
        image = Image.open(BytesIO(response.content))
        file_name = "files/google_searched_image.jpg"
        image.save(file_name)
        return file_name
    
    def set_image(self):
        self.manager.current_screen.ids.img_1.source = self.download_image()

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()
    

MainApp().run()