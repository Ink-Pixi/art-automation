import mysql.connector
import json
from contextlib import closing
from PyQt5.QtWidgets import QMessageBox


def connect_mysql():
    # dev = 0
    # live = 1
    stage = 0
    
    with open('data/config.json', 'r') as f:
        config = json.load(f)

    conn = mysql.connector.connect(user=config['user'], password=config['password'], host=config['host'],
                                   database=config['database'][stage], raise_on_warnings=True)
    
    return conn 


def get_sku_names():
    con = connect_mysql()
    cur = con.cursor()
    lst_results = []
    
    with closing(cur) as db:
        db.callproc('get_skus_names')
        for result in db.stored_results():
            results = result.fetchall()
        
    for result in results:
        lst_results.append(result[0]) 
    return lst_results 


def get_print_sku_info(sku, garm_type):
    con = connect_mysql()
    cur = con.cursor()
    with closing(cur) as db:
        db.callproc('get_sku_print_info', [sku, garm_type])
        for result in db.stored_results():
            results = result.fetchall()
            
    lst_print_info = []
    for r in results:
        lst_print_info.append(r)
    if lst_print_info:
        return lst_print_info[0]
        
def get_ink_types():
    con = connect_mysql()
    cur = con.cursor()
    with closing(cur) as db:
        db.callproc('get_ink_types')
        for result in db.stored_results():
            return result.fetchall()
        
def get_garm_types():
    con = connect_mysql()
    cur = con.cursor()
    with closing(cur) as db:
        db.callproc('get_garm_types')
        for result in db.stored_results():
            return result.fetchall()
        
def update_print_info(row_id, sku, garm_id, color, active, alt, var_count, ink_type, hightlight):
    con = connect_mysql()
    cur = con.cursor()
    with closing(cur) as db:
        db.callproc('upsert_print_info', [row_id, sku, garm_id, color, active, alt, var_count, ink_type, hightlight])
        db.commit()
        
def throw_db_error(error):
    ErrorMessage(error)
    
    
class ErrorMessage(QMessageBox):
    def __init__(self, error):
        super(ErrorMessage, self).__init__()
        QMessageBox.critical(self, 'A database error has occured.', str(error))

