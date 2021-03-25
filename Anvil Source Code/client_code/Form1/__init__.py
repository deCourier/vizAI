from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.
    self.initialiser()
    
  def initialiser(self):
    anvil.server.call('clearVars')
  
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_1.enabled = True
    link = anvil.server.call('returnWeb')
    self.link_1.url = str(link)
    self.link_1.text = "Open Dashboard in New Tab"
   

  def file_loader_1_change(self, file, **event_args):
    anvil.server.call('uploadModel', file, file.name)
    self.label_1.text = "Model uploaded"
    self.checkFiles()

  def file_loader_2_change(self, file, **event_args):
    anvil.server.call('uploadX_train', file, file.name)
    self.label_2.text = "X_train uploaded"
    self.checkFiles()
   
  def file_loader_3_change(self, file, **event_args):
    anvil.server.call('uploadX_test', file, file.name)
    self.label_4.text = "X_test uploaded"
    self.checkFiles()
    
  def file_loader_4_change(self, file, **event_args):
    anvil.server.call('uploadY_train', file, file.name)
    self.label_5.text = "y_train uploaded"
    self.checkFiles()
     
  def file_loader_5_change(self, file, **event_args):
    anvil.server.call('uploadY_test', file, file.name)
    self.label_6.text = "y_test uploaded"
    self.checkFiles()
    
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('resetFeatures')
    self.label_3.text = ""

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    anvil.server.call('setFeatures', self.text_box_1.text)
    self.label_3.text = "Data labels uploaded"


  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.initialiser()
    self.file_loader_1.clear()
    self.file_loader_2.clear()
    self.file_loader_3.clear()
    self.file_loader_4.clear()
    self.file_loader_5.clear()
    self.link_1.text = ""
    self.checkFiles()
    anvil.server.call('resetFeatures')
    self.label_3.text = ""
    self.label_1.text = ""
    self.label_2.text = ""
    self.label_4.text = ""
    self.label_5.text = ""
    self.label_6.text = ""
    
  def checkFiles(self):
    files = [self.file_loader_1.file, self.file_loader_2.file, self.file_loader_3.file, self.file_loader_4.file, self.file_loader_5.file]
    self.button_1.enabled = False
    if not(None in files):
      self.button_1.enabled = True




