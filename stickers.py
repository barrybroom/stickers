import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty

class Sticker(Image):
  def __init__(self, **kwargs):
    super(Sticker, self).__init__(**kwargs)
    self.height = 300
    self.width = 300

  def on_touch_move(self, touch):
    if 'pos' in touch.profile:
      if self.collide_point(*touch.pos):
        self.x = touch.x - (self.width / 2)
        self.y = touch.y - (self.height / 2)
        return True

class StickerBookBarButton(Button):
  sticker_source = StringProperty()
  pressed = ListProperty([0,0])    

  def on_touch_down(self, touch):
    if self.collide_point(*touch.pos):
      self.pressed = touch.pos
      return True
    return super(StickerBookBarButton, self).on_touch_down(touch)

  def on_pressed(self, instance, pos):
    self.add_widget(Sticker(source = self.sticker_source))

class StickerBookBar(BoxLayout):
  def __init__(self, **kwargs):
    super(StickerBookBar, self).__init__(**kwargs)
    self.orientation = 'vertical'
    self.add_widget(StickerBookBarButton(id='btn01', text='A', sticker_source='monster01.png'))
    self.add_widget(StickerBookBarButton(id='btn02', text='B', sticker_source='monster02.png'))
    self.add_widget(StickerBookBarButton(id='btn03', text='C', sticker_source='monster03.png'))


class GameMenu(Widget):
  pass

class GameLayout(FloatLayout):
  pass


class stickersApp(App):

  def build(self):
    return GameLayout()

if __name__ == '__main__':
  stickersApp().run()
