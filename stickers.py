import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image

class Sticker(Image):
  def on_touch_move(self, touch):
    if 'pos' in touch.profile:
      self.x = touch.x - (self.width / 2)
      self.y = touch.y - (self.height / 2)

class StickerBookBarButton(Widget):
  pass

class StickerBookBar(BoxLayout):
  pass

class GameMenu(Widget):
  pass

class GameLayout(FloatLayout):
  pass


class stickersApp(App):

  def build(self):
    return GameLayout()

if __name__ == '__main__':
  stickersApp().run()
