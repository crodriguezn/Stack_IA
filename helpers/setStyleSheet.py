# -*- coding: utf-8 

"""
Created on '05/03/2017'
@author: Luis Rodriguez 
Computer __author__ = 'Desarrollador' 
"""

def btn_default():
    css = ("""
            QPushButton {
                            text-align: center;font-weight: bold;
                            background-color:#ffffff;
                            border: 2px solid #ffffff;
                            padding-top: 5px;padding-right: 12px;padding-bottom: 5px;padding-left: 12px;
                            padding:5px 6px 6px"
                          }
            QPushButton:hover {
                                color:#333;
                                background-color:#fafafa;
                                border-color: #fafafa;
                              }
            QPushButton:focus {
                                color:#333;
                                background-color:#fafafa;
                                border-color: #fafafa;
                              }
            QPushButton:pressed {
                                    background-color: #B7B7B7;
                                    border-color: #B7B7B7;
                                  }
            """)
    return css

def btn_primary():
    css = ("QPushButton {"
                        "color: #fff; text-align: center;font-weight: bold;"
                        "background-color:#546672;"
                        "border: 2px solid #546672;"
                        "padding-top: 5px;padding-right: 12px;padding-bottom: 5px;padding-left: 12px;"
                      "}"
          "QPushButton:hover { "
                                "background-color:#657580;"
                                "border-color: #657580;"
                              "}"
          "QPushButton:focus { "
                                "background-color:#657580;"
                                "border-color: #657580;"
                              "}"
          "QPushButton:pressed { "
                                    "background-color: #4C5B66;"
                                    "border-color: #4C5B66;"
                              "}")
    return css

def btn_success():
    css = ("QPushButton {"
                            "color: #fff; text-align: center;font-weight: bold;"
                            "background-color: #65B688;"
                            "border: 2px solid #65B688;"
                            "padding-top: 5px;padding-right: 12px;padding-bottom: 5px;padding-left: 12px;"
                        "}"
          "QPushButton:hover { "
                                  "background-color: #74bd94;"
                                  "border-color: #74bd94;"
                              "}"
          "QPushButton:focus { "
                                  "background-color: #74bd94;"
                                  "border-color: #74bd94;"
                              "}"
          "QPushButton:pressed { "
                                  "background-color: #59A87B;"
                                  "border-color: #59A87B; "
                              "}")
    return css

def btn_warning():
    css = ("QPushButton {"
                            "color: #fff; text-align: center;font-weight: bold;"
                            "background-color: #E48561;"
                            "border: 2px solid #E48561;"
                            "padding-top: 5px;padding-right: 12px;padding-bottom: 5px;padding-left: 12px;"
                        "}"
          "QPushButton:hover { "
                                  "background-color: #e69171;"
                                  "border-color: #e69171;"
                              "}"
          "QPushButton:focus { "
                                  "background-color: #e69171;"
                                  "border-color: #e69171;"
                              "}"
          "QPushButton:pressed { "
                                  "background-color: #DB805D;"
                                  "border-color: #DB805D; "
                              "}")
    return css

def btn_danger():
    css = ("QPushButton {"
                            "color: #fff; text-align: center;font-weight: bold;"
                            "background-color: #D65C4F;"
                            "border: 2px solid #D65C4F;"
                            "padding-top: 5px;padding-right: 12px;padding-bottom: 5px;padding-left: 12px;"
                        "}"
              "QPushButton:hover { "
                                      "background-color: #da6c61;"
                                      "border-color: #da6c61;"
                                  "}"
              "QPushButton:focus { "
                                      "background-color: #da6c61;"
                                      "border-color: #da6c61;"
                                  "}"
              "QPushButton:pressed { "
                                      "background-color: #C75549;"
                                      "border-color: #C75549; "
                                  "}")
    return css

def btn_info():
    css = ("QPushButton {"
                            "color: #fff; text-align: center;font-weight: bold;"
                            "background-color: #50ABC2;"
                            "border: 2px solid #50ABC2;"
                            "padding-top: 5px;padding-right: 12px;padding-bottom: 5px;padding-left: 12px;"
                        "}"
                  "QPushButton:hover { "
                                          "background-color: #61b3c8;"
                                          "border-color: #61b3c8;"
                                      "}"
                  "QPushButton:focus { "
                                          "background-color: #61b3c8;"
                                          "border-color: #61b3c8;"
                                      "}"
                  "QPushButton:pressed { "
                                          "background-color: #4DA2B8;"
                                          "border-color: #4DA2B8; "
                                      "}")
    return css

def table_view():
    css =("""
            QTableWidget
                        {
                            border: 2px groove #96A8A8;
                            border-radius: 3px;
                            selection-background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                     stop: 0 #65B688, stop: 0.4 #CEECF0,
                                                     stop: 0.6 #C5E4E8, stop: 1.0 #65B688);
                            selection-color:black;
                        }
            QTableWidget QHeaderView::section
                                            {
                                                border-bottom:0px groove #8BA6D9;
                                                border-left:0px groove #8BA6D9;
                                                border-right:2px groove #8BA6D9;
                                                border-top:0px;
                                                padding:5px;
                                                background:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                                         stop: 0 #F8FCFE, stop: 0.4 #EBEEF2,
                                                                         stop: 0.5 #E0E5EA, stop: 1.0 #DADEEA);


                                                color:black;
                                                outline:0px;
                                            }
            QTableWidget::item
                            {
                                padding:2px;
                                outline:0px;
                            }
            """)
    return css