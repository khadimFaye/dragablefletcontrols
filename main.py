from flet import Column, Page, GestureDetector, Image, Row, Text, MainAxisAlignment, DragUpdateEvent, app, Container


def main(page:Page):
  
  def makeMagic(e:DragUpdateEvent, control):
    print('chiamato')
    print(e.delta_x)
    if control.spacing!=-5 and e.delta_x <0.7:
      control.spacing=-5
    elif control.spacing==-5 and e.delta_x >-0.7:
      control.spacing=5
    control.update()
    page.update()
  
  def test(e:DragUpdateEvent):
    print(e.delta_x)
    

  row_image = Row(alignment = MainAxisAlignment.CENTER, spacing = 1, controls = [Container(width = 50, height = 50, bgcolor = 'blue'), Container(width = 50, height = 50, bgcolor = 'red')])
  gsdetector = GestureDetector(content = row_image, on_pan_update = lambda DragUpdateEvent :makeMagic(DragUpdateEvent, row_image), multi_tap_touches = lambda DragUpdateEvent : test(DragUpdateEvent))
  
  layout1 = Column(controls=[
    Row(alignment= MainAxisAlignment.CENTER, controls=[ Text(value = 'pizzica per vedere la magia ;)',weight = 'w700',size = 20, expand = False)]),
    gsdetector                                              
                                                       
  ]
                  )
  page.add(layout1)
  page.update()

app(target = main)

