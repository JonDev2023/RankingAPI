from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RankingAPI(App):
  def __init__(self, json):
    self.json = json
  def build(self):
    box = BoxLayout(orientation='vertical')
    i = 1
    while i < 5:
      str_i = str(i)
      json_i = json[i]
      TopLabel = Label(text=f'Top {str_i}: {json_i}')
      box.add_widget(TopLabel)
      i += 1
    return box

def run(json):
  ranking = RankingAPI(json)
  if_loop = True
  while if_loop:
    if __name__ == '__main__':
      ranking.run()
      if_loop = False
    else:
      if_loop = True
