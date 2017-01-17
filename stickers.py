import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class Sticker(Image):
  def on_touch_move(self, touch):
    if 'pos' in touch.profile:
      self.x = touch.x - (self.width / 2)
      self.y = touch.y - (self.height / 2)

class StickerBookBarButton(Button):
  def on_touch_down(self, touch):
    self.add_widget(Sticker())

class StickerBookBar(BoxLayout):
  def __init__(self, **kwargs):
    super(StickerBookBar, self).__init__(**kwargs)
    self.orientation = 'vertical'
    self.add_widget(StickerBookBarButton(text='A'))
    self.add_widget(StickerBookBarButton(text='B'))
    self.add_widget(StickerBookBarButton(text='C'))
    self.add_widget(StickerBookBarButton(text='D'))
    self.add_widget(StickerBookBarButton(text='E'))


class GameMenu(Widget):
  pass

class GameLayout(FloatLayout):
  pass


class stickersApp(App):

  def build(self):
    return GameLayout()

if __name__ == '__main__':
  stickersApp().run()
