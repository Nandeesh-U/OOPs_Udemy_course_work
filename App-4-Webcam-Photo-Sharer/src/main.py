from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from fileshare import FileSharer
import time
from kivy.core.clipboard import Clipboard
import webbrowser

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
        def start(self):
            self.ids.camera.opacity=1
            self.ids.camera.play = True
            self.ids.camera_button.text = "Stop Camera"

        def stop(self):
            self.ids.camera.play = False
            self.ids.camera.opacity=0
            self.ids.camera_button.text = "Start Camera"

        def capture(self):
            self.filepath = f'files/{time.strftime('%Y%m%d-%H%M%S')}.png'
            self.ids.camera.export_to_png(self.filepath)
            self.manager.current = 'image_screen'
            self.manager.current_screen.ids.img.source = self.filepath

class ImageScreen(Screen):
    def create_link(self):
        filepath_forlink = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(filepath=filepath_forlink)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
            self.ids.link.text = "Link copied to clipboard!"
        except:
            self.ids.link.text = "Please create a link first!"
    
    def open_link(self):
        try:
            webbrowser.open(self.url)
            self.ids.link.text = "Link opened in browser!"
        except:
            self.ids.link.text = "Please create a link first!"

class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()