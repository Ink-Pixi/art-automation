import os
import sys
import ctypes
from data import inkpixi_products_data as ip_data
from ui.main import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QCompleter, QMessageBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
from image_viewer.iviewer import ImageViewer

class InkPixiProducts(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(InkPixiProducts, self).__init__()

        self.setupUi(self)
        
        self.sku_completer()
        self.garm_types()
        
        self.cbox_garm_types.currentIndexChanged.connect(self.change_garment)
        self.btn_test.clicked.connect(self.btn_get_clicked)
        self.le_search_sku.returnPressed.connect(self.btn_get_clicked)
        
        self.btn_update.clicked.connect(self.update_print_info)
        
        
    def garm_types(self):
        garm_types = ip_data.get_garm_types()
        
        for gt in range(len(garm_types)):
            self.cbox_garm_types.addItem(garm_types[gt][1], garm_types[gt][0])
    
    
    def sku_completer(self):

        # grab skus information from comapny.
        root_skus = ip_data.get_sku_names()
        
        # set up an auto complete for the sku line edit box
        rsku_completer = QCompleter(root_skus)
        rsku_completer.setCompletionMode(QCompleter.InlineCompletion)
        rsku_completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        rsku_completer.setCaseSensitivity(Qt.CaseInsensitive)       
        
        self.le_search_sku.setCompleter(rsku_completer) 
        
    def btn_get_clicked(self):
        
        self.sku_text = self.le_search_sku.text().split('-')[0].strip()
        
        self.get_print_info(1)
        
        self.le_search_sku.clear()
        
    def update_print_info(self):
        ip_data.update_print_info(
            self.row_id,
            self.sku_text, 
            self.cbox_garm_types.itemData(self.cbox_garm_types.currentIndex()), 
            150, #untill the dropdown box is down. 
            self.chk_active.isChecked(), 
            self.chk_alt_sweat.isChecked(), 
            self.sbox_variables.getValue(), 
            self.cbox_ink_type.itemData(self.cbox_ink_type.currentIndex()), 
            self.chk_active.isChecked())

    def get_print_info(self, garm_id):
        img_path = ''
        ink_types = ip_data.get_ink_types()

        for it in range(len(ink_types)):
            self.cbox_ink_type.addItem(ink_types[it][1], ink_types[it][0])
            # retrive data with self.cbox_ink_type.itemData(self.comboBox.currentIndex())
            
        
        lst_sku_info = ip_data.get_print_sku_info(self.sku_text, garm_id)
        
        if lst_sku_info:
            self.row_id = lst_sku_info[0]
            self.le_root_sku.setText(lst_sku_info[1])
            self.le_root_sku_name.setText(lst_sku_info[1])
            self.le_root_color.setText(lst_sku_info[2])
            self.sbox_variables.setValue(int(lst_sku_info[3]))
            self.chk_active.setChecked(lst_sku_info[4])            
            self.chk_alt_sweat.setChecked(lst_sku_info[5])
            self.sbox_highlight.setValue(lst_sku_info[7])
            self.sbox_mask.setValue(lst_sku_info[8])
            self.chk_background.setChecked(lst_sku_info[9])
            self.chk_multi_pass.setChecked(lst_sku_info[10])
            self.sbox_ink_vol.setValue(lst_sku_info[11])
            self.sbox_dbl_print.setValue(lst_sku_info[12])
            self.chk_transparent.setChecked(lst_sku_info[13])
            img_path = self.get_img_path(
                lst_sku_info[2],
                lst_sku_info[1], 
                garm_id)     
        else:
            QMessageBox.warning(self, 
                                'Sku Error', 
                                'No data found for this sku/garment combo.')

            img_path = self.get_img_path('', '', 1)
        
   
        self.set_image(img_path)

       
    def change_garment(self): 
        garm_id = self.cbox_garm_types.itemData(
            self.cbox_garm_types.currentIndex())
        self.get_print_info(garm_id)
        
    def set_image(self, img_path):    
        if os.path.exists(img_path):
            self.btn_img.setIcon(QIcon(img_path))
            self.btn_img.setIconSize(QSize(90, 120))
        else:   
            self.btn_img.setIcon(QIcon(':/images/images/red-x.png'))
            self.btn_img.setIconSize(QSize(90, 120))
            
        self.btn_img.clicked.connect(self.image_viewer)         
        
    def get_img_path(self, color, name, garm_type):
        
        if garm_type == 1:
            img_type = '-personalized-tshirt-sm.jpg'        
        elif garm_type == 2:
            img_type = '-personalized-sweatshirt-sm.jpg'
        elif garm_type == 3:
            img_type = '-personalized-apron-sm.jpg'


       
        img_name = color +'-'+ name + img_type
        img_name = str.replace(img_name, ' ', '-')
        img_path = os.path.join('\\\\inkpixi\inkpixi-dev\data\store', img_name)
        
        self.iv = ImageViewer(img_path)
        
        return img_path
    
    def image_viewer(self):
        self.iv.show()

if __name__ == '__main__':
    my_app_id = 'Products'
    # Windows 7 or x64 only
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
        
    app = QApplication(sys.argv)
    ip = InkPixiProducts()
    ip.show()
    
    sys.exit(app.exec_())