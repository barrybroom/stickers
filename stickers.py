import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import BooleanProperty

root = {}
sticker_number = 0
stickers_in_use = {}
sticker_moving_id = ''

class Sticker(Image):
  is_moving = BooleanProperty()

  def __init__(self, **kwargs):
    super(Sticker, self).__init__(**kwargs)
    self.height = 200
    self.width = 200

  def on_touch_down(self, touch):
    global sticker_moving_id

    if 'pos' in touch.profile:
      if self.collide_point(*touch.pos):
        self.is_moving = True
        sticker_moving_id = self.id
        return True
      return super(Sticker, self).on_touch_down(touch)

  def on_touch_move(self, touch):
    if self.is_moving:
      self.x = touch.x - (self.width / 2)
      self.y = touch.y - (self.height / 2)

  def on_touch_up(self, touch):
    if 'pos' in touch.profile:
      if self.collide_point(*touch.pos):
        self.is_moving = False
        return True
      return super(Sticker, self).on_touch_down(touch)
    

class StickerBookBarButton(Image):
  sticker_source = StringProperty()
  pressed = ListProperty([0,0])    

  def on_touch_down(self, touch):
    if self.collide_point(*touch.pos):
      self.pressed = touch.pos
      print 'Pressed sticker book bar button'
      return True
    return super(StickerBookBarButton, self).on_touch_down(touch)

  def on_pressed(self, instance, pos):
    global sticker_number, stickers_in_use
    sticker_number = sticker_number + 1
    sticker_id = 'sticker_' + str(sticker_number)
    s = Sticker(id = sticker_id, source = self.sticker_source)
    stickers_in_use[sticker_id] = s
    root.add_widget(s)
    print 'Added ' + sticker_id
    print stickers_in_use


class StickerBookBar(BoxLayout):
  def __init__(self, **kwargs):
    super(StickerBookBar, self).__init__(**kwargs)
    self.orientation = 'vertical'
    self.spacing = 20
    self.padding = 5
    self.add_widget(StickerBookBarButton(id='btn01', source='anna-2.png', sticker_source='anna-2.png'))
    self.add_widget(StickerBookBarButton(id='btn02', source='elsa.png', sticker_source='elsa.png'))
    self.add_widget(StickerBookBarButton(id='btn03', source='kristoff.png', sticker_source='kristoff.png'))
    self.add_widget(StickerBookBarButton(id='btn04', source='olaf.png', sticker_source='olaf.png'))


class MenuButton(Widget):
  def on_touch_move(self, touch):
    global sticker_moving_id, stickers_in_use
    if 'pos' in touch.profile:
      if self.collide_point(*touch.pos):
        if len(sticker_moving_id) > 0:
          print 'Delete ' + sticker_moving_id
          root.remove_widget(stickers_in_use[sticker_moving_id])
          stickers_in_use.pop(sticker_moving_id)
          sticker_moving_id = ''
          return True
      return super(MenuButton, self).on_touch_move(touch)

class GameMenu(Widget):
  pass

class GameLayout(FloatLayout):
  pass


class stickersApp(App):

  def build(self):
    global root
    root =  GameLayout()
    return root

if __name__ == '__main__':
  stickersApp().run()
