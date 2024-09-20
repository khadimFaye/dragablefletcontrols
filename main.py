from flet import Column, Page, GestureDetector, Image, Colors, Row, Text, MainAxisAlignment, DragUpdateEvent


def main(psge:Page):
  
  def makeMagic(DragUpdateEvent, control):
    if control.spacing1!=-5:
      control.spacing=-5
    else:
      control.spacing=5
    control.update()
    page.update()
    

  row_image = Row(alignment = MainAxisAlignment.CENTER, spacing = 1)
  gsdetector = GestureDetector(content = row_image, on_pan_update = lambda DragUpdateEvent :makeMagic(DragUpdateEvent, row_image)
  
  layout1 = Column(controls=[
    Row(alignment= MainAxisAlignment.CENTER, controls=[ Text(value = 'pizzica per vedere la magia ;)',weight = 'w700',size = 20, expand = True),
    gsdetector                                              
                                                       
  ]
                  )
  page.add(layout1)
  page.update()
