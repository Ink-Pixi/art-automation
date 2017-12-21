import os
from ui.iviewer import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap

class ImageViewer(QWidget, Ui_Form):
    
    def __init__(self, path):
        super(ImageViewer, self).__init__()
        self.setupUi(self)
        
        if os.path.exists(path):
            self.lbl_img.setPixmap(QPixmap(path))
        else:
            self.lbl_img.setPixmap(QPixmap(':/images/images/thumbs-down.png'))

        

    