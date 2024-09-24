import android
from pelican import pelicans
from pelicandb import Pelican,DBSession,feed
import json
import struct
from decimal import Decimal
from ru.travelfood.simple_ui import SimpleSQLProvider as sqlClass
import random
import base64
from ru.travelfood.simple_ui import SimpleUtilites as suClass
import os
from ru.travelfood.simple_ui import NoSQL as noClass

db = pelicans["TA_WMS"]

# при старте экрана Отбор 
def py_OnStartOrder(hashMap, _files=None, _data=None):
    # android.stop()
    if hashMap.containsKey("НомерЗаказа") and hashMap.get("НомерЗаказа") != "":
        py_LoadGoods(hashMap)
    Display_Elrment(hashMap)
    return hashMap

# загрузка товаров
def py_LoadGoods(hashMap):
    # android.stop()
    j = {
        "customcards":  {
            "options":  {
                "search_enabled": True,
                "save_position": True
            },
            "layout":   { #корневой контейнер
                "type": "LinearLayout",
                "orientation": "vertical",
                "height": "match_parent",
                "width": "match_parent",
                "weight": "0",
                "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "Elements": [
                            {   #Карточка товара
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "5",
                                "Elements": [
                                    { #Контейнер Производитель
                                        "type": "LinearLayout",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "0",
                                        "Value": "",
                                        "Variable": "",
                                        "orientation": "horizontal",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "3",
                                                "Value": "Производитель:",
                                                "Variable": "",
                                                "gravity_horizontal": "right",
                                                "TextSize": "16",
                                                # "TextBold": True,
                                                # "BackgroundColor": "#A9A9A9",
                                                # "TextColor": "#DB7093"
                                            },
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "2",
                                                "Value": "@Производитель",
                                                "Variable": "",
                                                "gravity_horizontal": "left",
                                                "TextSize": "16",
                                                "TextBold": True,
                                                # "BackgroundColor": "#A9A9A9",
                                                # "TextColor": "#DB7093"
                                            }
                                        ]
                                    },
                                    { #Контейнер Артикул
                                        "type": "LinearLayout",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "0",
                                        "Value": "",
                                        "Variable": "",
                                        "orientation": "horizontal",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "3",
                                                "Value": "№ по каталогу:",
                                                "Variable": "",
                                                "gravity_horizontal": "right",
                                                "TextSize": "16",
                                                # "TextBold": True,
                                                # "BackgroundColor": "#A9A9A9",
                                                # "TextColor": "#DB7093"
                                            },
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "2",
                                                "Value": "@Артикул",
                                                "Variable": "",
                                                "gravity_horizontal": "left",
                                                "TextSize": "16",
                                                "TextBold": True,
                                                # "BackgroundColor": "#A9A9A9",
                                                # "TextColor": "#DB7093"
                                            }
                                        ]
                                    },
                                    { #Контейнер Наименование
                                        "type": "LinearLayout",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "0",
                                        "Value": "",
                                        "Variable": "",
                                        "orientation": "horizontal",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "3",
                                                "Value": "Наименование:",
                                                "Variable": "",
                                                "gravity_horizontal": "right",
                                                "TextSize": "16",
                                                # "TextBold": True,
                                                # "TextColor": "#DB7093"
                                            },
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "2",
                                                "Value": "@Номенклатура",
                                                "Variable": "",
                                                "gravity_horizontal": "left",
                                                "TextSize": "16",
                                                "TextBold": True,
                                                # "TextColor": "#DB7093"
                                            }
                                        ]
                                    },
                                    { #Контейнер Св.остаток
                                        "type": "LinearLayout",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "0",
                                        "Value": "",
                                        "Variable": "",
                                        "orientation": "horizontal",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "1",
                                                "Value": "Св.остаток:",
                                                "Variable": "",
                                                "TextSize": "16",
                                                "gravity_horizontal": "right",
                                                "TextBold": True,
                                                # "TextColor": "#DB7093"
                                            },
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "1",
                                                "Value": "@СвободныйОстаток",
                                                "Variable": "",
                                                "TextSize": "16",
                                                "TextBold": True,
                                                # "TextColor": "#DB7093"
                                            }
                                        ]
                                    },
                                    { #Контейнер Заказано/Отобрано
                                        "type": "LinearLayout",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "0",
                                        "Value": "",
                                        "Variable": "",
                                        "orientation": "horizontal",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "1",
                                                "Value": "Отобрано/Заказано:",
                                                "Variable": "",
                                                "TextSize": "16",
                                                "gravity_horizontal": "right",
                                                "TextBold": True,
                                                # "TextColor": "#DB7093"
                                            },
                                            {
                                                "type": "TextView",
                                                "height": "wrap_content",
                                                "width": "match_parent",
                                                "weight": "1",
                                                "Value": "@ЗаказаноОтобрано",
                                                "Variable": "",
                                                "TextSize": "16",
                                                "TextBold": True,
                                                # "TextColor": "#DB7093"
                                            }
                                        ]
                                    }#,
                                    # {  # Кнопка ШК
                                    #     "type": "LinearLayout",
                                    #     "height": "wrap_content",
                                    #     "width": "match_parent",
                                    #     "weight": "0",
                                    #     "Value": "",
                                    #     "Variable": "",
                                    #     "orientation": "horizontal",
                                    #     # "Padding": "10",
                                    #     "Elements": [
                                    #         {
                                    #             "type": "Button",
                                    #             "show_by_condition": False,
                                    #             "Value": "@НадписьКнРучВвод",
                                    #             "Variable": "btn_manual",
                                    #             "NoRefresh": False,
                                    #             "document_type": "",
                                    #             "mask": "",
                                    #             "TextSize": "-1",
                                    #             "TextColor": "#6F9393",
                                    #             "width": "wrap_content",
                                    #             "height": "wrap_content",
                                    #             "weight": "1"
                                    #         }
                                    #     ],
                                    # }  # ,
                                ]
                            },
                            {  # Меню карточки
                                "type": "PopupMenuButton",
                                "show_by_condition": "",
                                "Value": "@ListCardMenu",
                                "NoRefresh": False,
                                "document_type": "",
                                "mask": "",
                                "Variable": "menu_card"
                            }  # ,
                        ]
                    }# ,
                    # {
                    #     "type": "TextView",
                    #     "show_by_condition": "",
                    #     "Value": "@descr",
                    #     "NoRefresh": False,
                    #     "document_type": "",
                    #     "mask": "",
                    #     "Variable": "",
                    #     "TextSize": "-1",
                    #     "TextColor": "#6F9393",
                    #     "gravity_horizontal": "left",
                    #     "gravity_vertical": "center",
                    #     "TextBold": False,
                    #     "TextItalic": True,
                    #     "BackgroundColor": "",
                    #     "width": "wrap_content",
                    #     "height": "wrap_content",
                    #     "weight": "3"
                    # }
                ]
            }
        }
    }

    # j = {
    #     "customcards":  {
    #         "options":  {
    #             "search_enabled": True,
    #             "save_position": True
    #         },
    #         "layout":   { #корневой контейнер
    #             "type": "LinearLayout",
    #             "orientation": "vertical",
    #             "height": "match_parent",
    #             "width": "match_parent",
    #             "weight": "0",
    #             "Elements": [
    #                 {
    #                     "type": "LinearLayout",
    #                     "orientation": "vertical",
    #                     "height": "wrap_content",
    #                     "width": "match_parent",
    #                     "weight": "0",
    #                     "Elements": [
    #                         {
    #                             "type": "LinearLayout",
    #                             "orientation": "vertical",
    #                             "height": "wrap_content",
    #                             "width": "match_parent",
    #                             "weight": "5",
    #                             "Elements": [
    #                                 {
    #                                     "type": "TextView",
    #                                     "show_by_condition": "",
    #                                     "Value": "@Номенклатура",
    #                                     "width": "match_parent",
    #                                     "gravity_horizontal": "center",
    #                                     "NoRefresh": False,
    #                                     "document_type": "",
    #                                     "mask": "",
    #                                     "Variable": ""
    #                                 },
    #                                 {
    #                                     "type": "TextView",
    #                                     "show_by_condition": "",
    #                                     "Value": "@Артикул",
    #                                     "width": "match_parent",
    #                                     "gravity_horizontal": "center",
    #                                     "NoRefresh": False,
    #                                     "document_type": "",
    #                                     "mask": "",
    #                                     "Variable": ""
    #                                 },
    #                                 {
    #                                     "type": "TextView",
    #                                     "show_by_condition": "",
    #                                     "Value": "@Производитель",
    #                                     "width": "match_parent",
    #                                     "gravity_horizontal": "center",
    #                                     "NoRefresh": False,
    #                                     "document_type": "",
    #                                     "mask": "",
    #                                     "Variable": ""
    #                                 }
    #                             ]
    #                         },
    #                         {
    #                             "type": "LinearLayout",
    #                             "orientation": "vertical",
    #                             "height": "wrap_content",
    #                             "width": "match_parent",
    #                             "weight": "2",
    #                             "Elements": [
    #                                 {
    #                                     "type": "LinearLayout",
    #                                     "height": "wrap_content",
    #                                     "width": "wrap_content",
    #                                     "weight": "0",
    #                                     "Value": "",
    #                                     "Variable": "",
    #                                     "orientation": "horizontal",
    #                                     "Elements": [
    #                                         {
    #                                             "type": "TextView",
    #                                             "height": "wrap_content",
    #                                             "width": "wrap_content",
    #                                             "weight": "0",
    #                                             "Value": "Заказано:",
    #                                             "Variable": "",
    #                                             "TextSize": "16",
    #                                             "TextBold": True,
    #                                             "TextColor": "#DB7093"
    #                                         },
    #                                         {
    #                                             "type": "TextView",
    #                                             "height": "wrap_content",
    #                                             "width": "wrap_content",
    #                                             "weight": "0",
    #                                             "Value": "@КОтбору",
    #                                             "Variable": "",
    #                                             "TextSize": "16",
    #                                             "TextBold": True,
    #                                             "TextColor": "#DB7093"
    #                                         }
    #                                     ]
    #                                 },
    #                                 {
    #                                     "type": "LinearLayout",
    #                                     "height": "wrap_content",
    #                                     "width": "wrap_content",
    #                                     "weight": "0",
    #                                     "Value": "",
    #                                     "Variable": "",
    #                                     "orientation": "horizontal",
    #                                     "Elements": [
    #                                         {
    #                                             "type": "TextView",
    #                                             "height": "wrap_content",
    #                                             "width": "wrap_content",
    #                                             "weight": "0",
    #                                             "Value": "Отобрано:",
    #                                             "Variable": "",
    #                                             "TextSize": "16",
    #                                             "TextBold": True,
    #                                             "TextColor": "#DB7093"
    #                                         },
    #                                         {
    #                                             "type": "TextView",
    #                                             "height": "wrap_content",
    #                                             "width": "wrap_content",
    #                                             "weight": "0",
    #                                             "Value": "@Отобрано",
    #                                             "Variable": "",
    #                                             "TextSize": "16",
    #                                             "TextBold": True,
    #                                             "TextColor": "#DB7093"
    #                                         }
    #                                     ]
    #                                 },
    #                                 {
    #                                     "type": "LinearLayout",
    #                                     "height": "wrap_content",
    #                                     "width": "wrap_content",
    #                                     "weight": "0",
    #                                     "Value": "",
    #                                     "Variable": "",
    #                                     "orientation": "horizontal",
    #                                     "Elements": [
    #                                         {
    #                                             "type": "TextView",
    #                                             "height": "wrap_content",
    #                                             "width": "wrap_content",
    #                                             "weight": "0",
    #                                             "Value": "Св.остаток:",
    #                                             "Variable": "",
    #                                             "TextSize": "16",
    #                                             "TextBold": True,
    #                                             "TextColor": "#DB7093"
    #                                         },
    #                                         {
    #                                             "type": "TextView",
    #                                             "height": "wrap_content",
    #                                             "width": "wrap_content",
    #                                             "weight": "0",
    #                                             "Value": "@СвободныйОстаток",
    #                                             "Variable": "",
    #                                             "TextSize": "16",
    #                                             "TextBold": True,
    #                                             "TextColor": "#DB7093"
    #                                         }
    #                                     ]
    #                                 }
    #                             ]
    #                         }
    #                     ]
    #                 },
    #                 {
    #                     "type": "TextView",
    #                     "show_by_condition": "",
    #                     "Value": "@descr",
    #                     "NoRefresh": False,
    #                     "document_type": "",
    #                     "mask": "",
    #                     "Variable": "",
    #                     "TextSize": "-1",
    #                     "TextColor": "#6F9393",
    #                     "gravity_horizontal": "left",
    #                     "gravity_vertical": "center",
    #                     "TextBold": False,
    #                     "TextItalic": True,
    #                     "BackgroundColor": "",
    #                     "width": "wrap_content",
    #                     "height": "wrap_content",
    #                     "weight": "3"
    #                 }
    #             ]
    #         }
    #     }
    # }

    j["customcards"]["cardsdata"] = []

    # db = pelicans["TA_WMS"]
    records = db["GoodsForSelection"].find({"$and": [{"ВидЗаказа": hashMap.get("ВидЗаказа")},
                                                     {"НомерЗаказа": hashMap.get("НомерЗаказа")}]})
    if len(records) > 0:
        hashMap.put("OrderCollected", False)    
        i = 1
        for record in records:
            if (record['КОтбору'] == record['Отобрано']):
                continue
            
            # list_btn_Goods = "Подтвердить отбор" if record['ШтрихКод'] == "Нет штрихкода" else "Ручной ввод ШК" + ";Ввести количество" if record['КОтбору'] > 1 else ""
            
            # if record['ШтрихКод'] == "Нет штрихкода":
            c = {
                "key": record['Код'],
                "ЗаказаноОтобрано": "<font color=#F08080>"+str(record['Отобрано'])+"/"+str(record['КОтбору'])+" "+ record['ЕдиницаИзмерения']+"</font>",
                "СвободныйОстаток": record['СвободныйОстаток'] + " " + record['ЕдиницаИзмерения'],
                "Код": record['Код'],
                "Номенклатура": record['Номенклатура'],
                "Артикул": record['Артикул'],
                "Производитель": record['Производитель'],
                "ШтрихКод": record['ШтрихКод'],
                "Отобрано": record['Отобрано'],
                "ListCardMenu": "Подтвердить отбор;Ввести количество" if record['ШтрихКод'] == "Нет штрихкода" else "Ручной ввод ШК;Ввести количество"
                # "_layout": { #корневой контейнер
                #         "type": "LinearLayout",
                #         "orientation": "vertical",
                #         "height": "match_parent",
                #         "width": "match_parent",
                #         "weight": "0",
                #         "Elements": [
                #             {
                #                 "type": "LinearLayout",
                #                 "orientation": "vertical",
                #                 "height": "wrap_content",
                #                 "width": "match_parent",
                #                 "weight": "0",
                #                 "Elements": [
                #                     {
                #                         "type": "LinearLayout",
                #                         "orientation": "vertical",
                #                         "height": "wrap_content",
                #                         "width": "match_parent",
                #                         "weight": "5",
                #                         "Elements": [
                #                             { #Контейнер Производитель
                #                                 "type": "LinearLayout",
                #                                 "height": "wrap_content",
                #                                 "width": "match_parent",
                #                                 "weight": "0",
                #                                 "Value": "",
                #                                 "Variable": "",
                #                                 "orientation": "horizontal",
                #                                 "Elements": [
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "3",
                #                                         "Value": "Производитель:",
                #                                         "Variable": "",
                #                                         "gravity_horizontal": "right",
                #                                         "TextSize": "16",
                #                                         # "TextBold": True,
                #                                         # "BackgroundColor": "#A9A9A9",
                #                                         # "TextColor": "#DB7093"
                #                                     },
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "2",
                #                                         "Value": "@Производитель",
                #                                         "Variable": "",
                #                                         "gravity_horizontal": "left",
                #                                         "TextSize": "16",
                #                                         "TextBold": True,
                #                                         # "BackgroundColor": "#A9A9A9",
                #                                         # "TextColor": "#DB7093"
                #                                     }
                #                                 ]
                #                             },
                #                             { #Контейнер Артикул
                #                                 "type": "LinearLayout",
                #                                 "height": "wrap_content",
                #                                 "width": "match_parent",
                #                                 "weight": "0",
                #                                 "Value": "",
                #                                 "Variable": "",
                #                                 "orientation": "horizontal",
                #                                 "Elements": [
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "3",
                #                                         "Value": "№ по каталогу:",
                #                                         "Variable": "",
                #                                         "gravity_horizontal": "right",
                #                                         "TextSize": "16",
                #                                         # "TextBold": True,
                #                                         # "BackgroundColor": "#A9A9A9",
                #                                         # "TextColor": "#DB7093"
                #                                     },
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "2",
                #                                         "Value": "@Артикул",
                #                                         "Variable": "",
                #                                         "gravity_horizontal": "left",
                #                                         "TextSize": "16",
                #                                         "TextBold": True,
                #                                         # "BackgroundColor": "#A9A9A9",
                #                                         # "TextColor": "#DB7093"
                #                                     }
                #                                 ]
                #                             },
                #                             { #Контейнер Наименование
                #                                 "type": "LinearLayout",
                #                                 "height": "wrap_content",
                #                                 "width": "match_parent",
                #                                 "weight": "0",
                #                                 "Value": "",
                #                                 "Variable": "",
                #                                 "orientation": "horizontal",
                #                                 "Elements": [
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "3",
                #                                         "Value": "Наименование:",
                #                                         "Variable": "",
                #                                         "gravity_horizontal": "right",
                #                                         "TextSize": "16",
                #                                         # "TextBold": True,
                #                                         # "TextColor": "#DB7093"
                #                                     },
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "2",
                #                                         "Value": "@Номенклатура",
                #                                         "Variable": "",
                #                                         "gravity_horizontal": "left",
                #                                         "TextSize": "16",
                #                                         "TextBold": True,
                #                                         # "TextColor": "#DB7093"
                #                                     }
                #                                 ]
                #                             },
                #                             { #Контейнер Св.остаток
                #                                 "type": "LinearLayout",
                #                                 "height": "wrap_content",
                #                                 "width": "match_parent",
                #                                 "weight": "0",
                #                                 "Value": "",
                #                                 "Variable": "",
                #                                 "orientation": "horizontal",
                #                                 "Elements": [
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "1",
                #                                         "Value": "Св.остаток:",
                #                                         "Variable": "",
                #                                         "TextSize": "16",
                #                                         "gravity_horizontal": "right",
                #                                         "TextBold": True,
                #                                         # "TextColor": "#DB7093"
                #                                     },
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "1",
                #                                         "Value": "@СвободныйОстаток",
                #                                         "Variable": "",
                #                                         "TextSize": "16",
                #                                         "TextBold": True,
                #                                         # "TextColor": "#DB7093"
                #                                     }
                #                                 ]
                #                             },
                #                             { #Контейнер Заказано/Отобрано
                #                                 "type": "LinearLayout",
                #                                 "height": "wrap_content",
                #                                 "width": "match_parent",
                #                                 "weight": "0",
                #                                 "Value": "",
                #                                 "Variable": "",
                #                                 "orientation": "horizontal",
                #                                 "Elements": [
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "1",
                #                                         "Value": "Отобрано/Заказано:",
                #                                         "Variable": "",
                #                                         "TextSize": "16",
                #                                         "gravity_horizontal": "right",
                #                                         "TextBold": True,
                #                                         # "TextColor": "#DB7093"
                #                                     },
                #                                     {
                #                                         "type": "TextView",
                #                                         "height": "wrap_content",
                #                                         "width": "match_parent",
                #                                         "weight": "1",
                #                                         "Value": "@ЗаказаноОтобрано",
                #                                         "Variable": "",
                #                                         "TextSize": "16",
                #                                         "TextBold": True,
                #                                         # "TextColor": "#DB7093"
                #                                     }
                #                                 ]
                #                             },
                #                             { #Кнопка ШК
                #                                 "type": "LinearLayout",
                #                                 "height": "wrap_content",
                #                                 "width": "match_parent",
                #                                 "weight": "0",
                #                                 "Value": "",
                #                                 "Variable": "",
                #                                 "orientation": "horizontal",
                #                                 # "Padding": "10",
                #                                 "Elements": [
                #                                     {
                #                                         "type": "Button",
                #                                         "show_by_condition": False,
                #                                         "Value": "@НадписьКнРучВвод", 
                #                                         "Variable": "btn_manual",
                #                                         "NoRefresh": False,
                #                                         "document_type": "",
                #                                         "mask": "",
                #                                         "TextSize": "-1",
                #                                         "TextColor": "#6F9393",
                #                                         "width": "wrap_content",
                #                                         "height": "wrap_content",
                #                                         "weight": "1"
                #                                     }
                #                                 ],
                #                             },
                #                             { # Кнопка ввод количества
                #                                 "type": "Button",
                #                                 "show_by_condition": "",
                #                                 "Value": "Ввод количества", 
                #                                 "Variable": "btn_q",
                #                                 "NoRefresh": False,
                #                                 "document_type": "",
                #                                 "mask": "",
                #                                 "TextSize": "-1",
                #                                 "TextColor": "#6F9393",
                #                                 "width": "wrap_content",
                #                                 "height": "wrap_content",
                #                                 "weight": "1"
                #                             }   
                #                         ]
                #                     }
                #                 ]
                #             }
                #         ]
                # }

                }
            # else:        
                # c = {
                #     "key": record['Код'],
                #     # "descr": "Pos. "+str(i)+". "+record['Код'],
                #     "ЗаказаноОтобрано": "<font color=#F08080>"+str(record['Отобрано'])+"/"+str(record['КОтбору'])+" "+ record['ЕдиницаИзмерения']+"</font>",
                #     # "ЗаказаноОтобрано": "<font color=#F08080>" if record['КОтбору']>record['Отобрано'] else "<font color=#32CD32>" + str(record['КОтбору'])+"/"+str(record['Отобрано'])+" "+ record['ЕдиницаИзмерения']+"</font>",
                #     # "КОтбору": record['КОтбору'],
                #     # "Отобрано": record['Отобрано'],
                #     "СвободныйОстаток": record['СвободныйОстаток'] + " " + record['ЕдиницаИзмерения'],
                #     "Код": record['Код'],
                #     "Номенклатура": record['Номенклатура'],
                #     "Артикул": record['Артикул'],
                #     "Производитель": record['Производитель'],
                #     "ШтрихКод": record['ШтрихКод'],
                #     # "list_btn_Goods": list_btn_Goods

                #     "НадписьКнРучВвод": "Подтвердить отбор" if record['ШтрихКод'] == "Нет штрихкода" else "Ручной ввод ШК"
                #     # "ЕдиницаИзмерения": record['ЕдиницаИзмерения']
                #     # "НомерЗаказа": record['НомерЗаказа'],
                #     # "Получатель": record['Получатель'],
                #     # "ВидЗаказа": record['ВидЗаказа']
                # }

            j["customcards"]["cardsdata"].append(c)
            i += 1
        hashMap.put("CardsGoods", json.dumps(j, ensure_ascii=False).encode('utf8').decode())
        hashMap.put("OrderCollected", "False")    

    else:
        Set_Order_Collected(hashMap)
        hashMap.put("OrderCollected", "True")    

    return hashMap

# Установка признака собранного заказа
def Set_Order_Collected(hashMap):

    db["OrdersForSelection"].update({"$and": [{"ВидЗаказа": hashMap.get('ВидЗаказа')},
                                             {"НомерЗаказа": hashMap.get('НомерЗаказа')}]},
                                   {"ЗаказСобран": True})
    return hashMap

# отображение элементов экрана Отбор
def Display_Elrment(hashMap):
    OrderIsSelect = hashMap.containsKey("НомерЗаказа") and hashMap.get("НомерЗаказа") != ""
    # OrderCollected = eval(hashMap.get("OrderCollected") if hashMap.containsKey("OrderCollected") else "False")
    
    hashMap.put("Заголовок", hashMap.get("ВидЗаказа").upper() if OrderIsSelect else "ВЫБЕРИТЕ ЗАКАЗ")
    hashMap.put("Show_Контейнер_Получатель", "1" if OrderIsSelect else "-1")
    hashMap.put("Show_Контейнер_ВремяОстатков", "1" if OrderIsSelect else "-1")
    hashMap.put("Show_Контейнер_Товар", "1" if OrderIsSelect else "-1")
    # hashMap.put("Show_TextOrderCollected", "1" if OrderCollected else "-1")
    android.stop(hashMap)
    return hashMap

# при вводе в экране Отбор
def py_select_on_input(hashMap, _files=None, _data=None): 

    # android.stop(hashMap)

    if hashMap.get("listener") == 'barcode': #сканирование

        b = hashMap.get('barcode')
        hashMap.put('barcode', '')
        
        records = db["GoodsForSelection"].find({"$and": [{"ШтрихКод": b},{"НомерЗаказа": hashMap.get('НомерЗаказа')}]})
        if len(records) == 0:
            hashMap.put("beep", "15")
            hashMap.put("ShowDialog", "Ошибка")
            hashMap.put("ShowDialogStyle", "{'title': 'Товара с таким штрихкодом нет в заказе!',   'yes': '',   'no': 'OK' }")
        elif len(records) == 1:
            kodItem = records[0]['Код']
            goods_in_order = json.loads(hashMap.get('CardsGoods'))["customcards"]["cardsdata"]
            # search by barcode value
            card_of_goods = next((item for item in goods_in_order if item["key"] == kodItem), None)
            if card_of_goods == None:
                hashMap.put("beep", "15")
                hashMap.put("ShowDialog", "Ошибка")
                hashMap.put("ShowDialogStyle", "{'title': 'Товара с таким штрихкодом нет в заказе!',   'yes': '',   'no': 'OK' }")
            else:
                Update_Qty_Goods(hashMap, card_of_goods)
        else:
            hashMap.put("beep", "15")
            hashMap.put("ShowDialog", "Ошибка")
            hashMap.put("ShowDialogStyle", "{'title': 'Более 1-го товара с таким штрихкодом!',   'yes': '',   'no': 'OK' }")

    elif hashMap.get("listener") == "LayoutAction" and hashMap.get("layout_listener") == "Ручной ввод ШК":
    
        hashMap.put("ShowDialog", "ДиалогВводШК")
        hashMap.put("ShowDialogStyle", json.dumps({"title": "Введите штрихкод:", "yes": "ОК",   "no": "Отмена"}))
    
    elif hashMap.get("listener") == "LayoutAction" and hashMap.get("layout_listener") == "Подтвердить отбор":
        card_data = json.loads(hashMap.get('card_data'))
        Update_Qty_Goods(hashMap, card_data)

    elif hashMap.get("listener") == "LayoutAction" and hashMap.get("layout_listener") == "Ввести количество":
        
        hashMap.put("ShowDialog", "Ввод количества")
        hashMap.put("ShowDialogStyle", json.dumps({"title": "", "yes": "ОК",   "no": "Отмена"}))

    elif hashMap.get("event") == "onResultPositive" and hashMap.get("layout_listener") == "Ручной ввод ШК":

        b = hashMap.get('barcode')
        hashMap.put('barcode', '')

        # records = db["GoodsForSelection"].find({"ШтрихКод":b})
        card_data = json.loads(hashMap.get('card_data'))

        if card_data['ШтрихКод'] == b:
            Update_Qty_Goods(hashMap, card_data)
        else:
            hashMap.put("beep", "15")
            hashMap.put("ShowDialog", "Ошибка")
            hashMap.put("ShowDialogStyle", "{'title': 'Введен неверный штрихкод!',   'yes': '',   'no': 'OK' }")

    elif hashMap.get("event") == "onResultPositive" and hashMap.get("layout_listener") == "Ввести количество":

        
        # hashMap.put('barcode', '')

        # records = db["GoodsForSelection"].find({"ШтрихКод":b})
        card_data = json.loads(hashMap.get('card_data'))

        # if card_data['ШтрихКод'] == b:
        Update_Qty_Goods(hashMap, card_data, int(hashMap.get('qty')))
        # else:
        #     hashMap.put("beep", "15")
        #     hashMap.put("ShowDialog", "Ошибка")
        #     hashMap.put("ShowDialogStyle", "{'title': 'Введен неверный штрихкод!',   'yes': '',   'no': 'OK' }")

        # if len(records) == 0:
        #     hashMap.put("beep", "15")
        #     hashMap.put("ShowDialog", "Ошибка")
        #     hashMap.put("ShowDialogStyle", "{'title': 'Товара с таким штрихкодом нет в заказе!',   'yes': '',   'no': 'OK' }")
        # elif len(records) == 1:
        #     kodItem = records[0]['Код']
        #     hashMap.put('VAR_DEBUG', kodItem)
        #     android.stop(hashMap)
        #     if hashMap.get('selected_card_key') == kodItem:
        #         hashMap.put('VAR_DEBUG', "Точка 4")
        #         android.stop(hashMap)
        #         dict_selected_card = json.loads(hashMap.get('selected_card_data'))
        #         hashMap.put('VAR_DEBUG', "Точка 5")
        #         android.stop(hashMap)
        #         Update_Qty_Goods(hashMap, dict_selected_card)
        #     else:
        #         hashMap.put("beep", "15")
        #         hashMap.put("ShowDialog", "Ошибка")
        #         hashMap.put("ShowDialogStyle", "{'title': 'Введен неверный штрихкод!',   'yes': '',   'no': 'OK' }")

        #     goods_in_order = json.loads(hashMap.get('CardsGoods'))["customcards"]["cardsdata"]
        #     # search by barcode value
        #     card_of_goods = next((item for item in goods_in_order if item["key"] == kodItem), None)
        #     if card_of_goods == None:
        #         hashMap.put("beep", "15")
        #         hashMap.put("ShowDialog", "Ошибка")
        #         hashMap.put("ShowDialogStyle", "{'title': 'Товара с таким штрихкодом нет в заказе!',   'yes': '',   'no': 'OK' }")
        #     else:
        #         Update_Qty_Goods(hashMap, card_of_goods)
        # else:
        #     hashMap.put("beep", "15")
        #     hashMap.put("ShowDialog", "Ошибка")
        #     hashMap.put("ShowDialogStyle", "{'title': 'Более 1-го товара с таким штрихкодом!',   'yes': '',   'no': 'OK' }")

    # elif hashMap.get("listener") == 'CardsClick': #тап по карточке 
        # android.stop(hashMap)
        
        # hashMap.put("ShowDialog", "ДиалогВводШК")
        # hashMap.put("ShowDialogStyle", json.dumps({"title": "Введите штрихкод:", "yes": "ОК",   "no": "Отмена"}))


    return hashMap

# обновление количества отобранного товара в БД
def Update_Qty_Goods(hashMap, card_of_goods, qty=1):
    # db = pelicans["TA_WMS"]
    # hashMap.put('VAR_DEBUG', "Точка 3")
    # android.stop(hashMap)

    db["GoodsForSelection"].update({"$and": [{"ВидЗаказа": hashMap.get('ВидЗаказа')},
                                             {"НомерЗаказа": hashMap.get('НомерЗаказа')},
                                             {"Код": card_of_goods['Код']}]},
                                   {"Отобрано": card_of_goods['Отобрано']+qty})
    return hashMap

# при старте экрана выбора заказа
def py_OrderList_OnStart(hashMap, _files=None, _data=None):

    hashMap.put("SetTitle", "ВЫБОР ЗАКАЗА")

    db = pelicans["TA_WMS"]
    recordsZP = db["OrdersForSelection"].find({"ВидЗаказа": "Заказ покупателя"})
    recordsVZ = db["OrdersForSelection"].find({"ВидЗаказа": "Внутренний заказ"})

    if not hashMap.containsKey("btn_z"):
        list_btn = "Заказы покупателя("+str(len(recordsZP))+")"
        list_btn = list_btn + ";Внутренние заказы("+str(len(recordsVZ))+")"
        hashMap.put("list_btn", list_btn)
        return hashMap
    
    # android.stop(hashMap)
        
    
    j = {"customcards": {
                        "options": {
                            # "search_enabled": True,
                            # "save_position": True
                        },
                        "layout": { #Корневой котейнер
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "match_parent",
                            "width": "match_parent",
                            "weight": "0",
                            "Elements": [
                                    { #Надпись ЗаголовокЗаказа
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@ЗаголовокЗаказа",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": "",
                                        "TextSize": "-1",
                                        "TextColor": "#6F9393",
                                        "TextBold": False,
                                        "TextItalic": True,
                                        "gravity_horizontal": "left",
                                        "BackgroundColor": "",
                                        "width": "wrap_content",
                                        "height": "wrap_content",
                                        "weight": 0
                                    },
                                    { #Контейнер Получатель
                                        "type": "LinearLayout",
                                        "orientation": "horizontal",
                                        "height": "wrap_content",
                                        "width": "match_parent",
                                        "weight": "0",
                                        "Elements": [
                                            {
                                                "type": "TextView",
                                                "show_by_condition": "",
                                                "Value": "@ПолучательНадпись",
                                                "NoRefresh": False,
                                                "document_type": "",
                                                "mask": "",
                                                "Variable": "",
                                                "TextSize": "16",
                                                # "TextColor": "#DB7093",
                                                # "TextBold": True,
                                                # "TextItalic": False,
                                                "BackgroundColor": "",
                                                "width": 200, #"match_parent",
                                                "height": "wrap_content",
                                                "weight": 1
                                            },
                                            { 
                                                "type": "TextView",
                                                "show_by_condition": "",
                                                "Value": "@Получатель",
                                                "NoRefresh": False,
                                                "document_type": "",
                                                "mask": "",
                                                "Variable": "",
                                                "TextSize": "16",
                                                # "TextColor": "#DB7093",
                                                "TextBold": True,
                                                "TextItalic": False,
                                                "gravity_horizontal": "left",
                                                "BackgroundColor": "",
                                                "width": "match_parent",
                                                "height": "wrap_content",
                                                "weight": 1
                                            }#,
                                            # {
                                            #     "type": "LinearLayout",
                                            #     "orientation": "vertical",
                                            #     "height": "wrap_content",
                                            #     "width": "match_parent",
                                            #     "weight": "1",
                                            #     "Elements": [
                                            #             { #Надпись Получатель
                                            #                 "type": "TextView",
                                            #                 "show_by_condition": "",
                                            #                 "Value": "@Получатель",
                                            #                 "NoRefresh": False,
                                            #                 "document_type": "",
                                            #                 "mask": "",
                                            #                 "Variable": ""
                                            #             }
                                            #     ]
                                            # },
                                            # { #Надпись НомерЗаказа
                                            #     "type": "TextView",
                                            #     "show_by_condition": "",
                                            #     "Value": "@НомерЗаказа",
                                            #     "NoRefresh": False,
                                            #     "document_type": "",
                                            #     "mask": "",
                                            #     "Variable": "",
                                            #     "TextSize": "16",
                                            #     "TextColor": "#DB7093",
                                            #     "TextBold": True,
                                            #     "TextItalic": False,
                                            #     "BackgroundColor": "",
                                            #     "width": "match_parent",
                                            #     "height": "wrap_content",
                                            #     "weight": 2
                                            # }
                                        ]
                                    }
                            ]
                        }
                    }
    }

    j["customcards"]["cardsdata"] = []
    # hashMap.put("structcards", str(j))
    # android.stop(hashMap)
    ZP = True if hashMap.get("btn_z")[:6] == "Заказы" else False
        
    if ZP:
        i = 0
        if len(recordsZP) > 0:
            i = 1
            # c = {"group": "Заказы покупателя"}
            # j["customcards"]["cardsdata"].append(c)
            for record in recordsZP:
                # OrderHeader = ""
                OrderHeader = "<font color=#000000><b>"+record['Заказ']+"</b></font><br>"
                OrderHeader = OrderHeader + "Статус: " +record['Статус']
                OrderHeader = OrderHeader if record['Доставка'] == "" else OrderHeader + "<br>"+record['Доставка']
                OrderHeader = OrderHeader if record['Комментарий'] == "" else OrderHeader + "<br><font color=#DB7093>"+record['Комментарий']+"</font>"
                # OrderHeader = OrderHeader if record['Доставка'] == "" else "<p align=left>"+record['Доставка'] + "</p>"
                # OrderHeader = OrderHeader if record['Комментарий'] == "" else OrderHeader +"<p align=left><font color=#DB7093>"+record['Комментарий']+"</font></p>"
                # OrderHeader = OrderHeader +"<p align=left><font color=#2E8B57>"+record['Заказ']+"</font><br>"
                # OrderHeader = OrderHeader +"<font color=#000000>Статус: "+record['Статус']+"</font></p>"
                c = {
                    "key": record['НомерЗаказа'],
                    "ЗаголовокЗаказа": OrderHeader,	
                    "НомерЗаказа": record['НомерЗаказа'],
                    "Получатель": "<b>"+record['Получатель']+"</b>",
                    "ПолучательНадпись": "Покупатель: ",
                    "ВремяОстатков": record['ВремяОстатков'],
                    "ВидЗаказа": record['ВидЗаказа']
                }

                j["customcards"]["cardsdata"].append(c)
                i += 1
    else:
        i = 0
        if len(recordsVZ) > 0:
            i = 1
            # c = {"group": "Внутренние заказы"}
            # j["customcards"]["cardsdata"].append(c)
            for record in recordsVZ:
                OrderHeader = "<font color=#000000><b>"+record['Заказ']+"</b></font><br>"
                OrderHeader = OrderHeader + "Статус: " +record['Статус']
                OrderHeader = OrderHeader if record['Доставка'] == "" else OrderHeader + "<br>"+record['Доставка']
                OrderHeader = OrderHeader if record['Комментарий'] == "" else OrderHeader + "<br><font color=#DB7093>"+record['Комментарий']+"</font>"

                # OrderHeader = ""
                # OrderHeader = OrderHeader if record['Доставка'] == "" else "<p align=left>"+record['Доставка'] + "</p>"
                # OrderHeader = OrderHeader if record['Комментарий'] == "" else OrderHeader +"<p align=left><font color=#DB7093>"+record['Комментарий']+"</font></p>"
                # OrderHeader = OrderHeader +"<p align=left><font color=#2E8B57>"+record['Заказ']+"</font></p>"
                # OrderHeader = OrderHeader +"<p align=left><font color=#000000>Статус:"+record['Статус']+"</font></p>"
                c = {
                    "key": record['НомерЗаказа'],
                    "ЗаголовокЗаказа": OrderHeader,
                    "НомерЗаказа": record['НомерЗаказа'],
                    "ПолучательНадпись": "Получатель: ",
                    "Получатель": record['Получатель'],
                    "ВремяОстатков": record['ВремяОстатков'],
                    "ВидЗаказа": record['ВидЗаказа']
                }

                j["customcards"]["cardsdata"].append(c)
                i += 1

    # if not hashMap.containsKey("cards"):
    hashMap.put("cards", json.dumps(j, ensure_ascii=False).encode('utf8').decode())

    return hashMap

# при выборе карточки заказа на экране выбора заказа
def py_SelectionOrder(hashMap, _files=None, _data=None):
    Sel_card = json.loads(hashMap.get("selected_card_data"))
    hashMap.put("Получатель", Sel_card['Получатель'])
    hashMap.put("ВидЗаказа", Sel_card['ВидЗаказа'])
    hashMap.put("ВремяОстатков", Sel_card['ВремяОстатков'])
    hashMap.put(hashMap.get("field"), hashMap.get("selected_card_key"))
    hashMap.put("BackScreen", "")
    # @field=@selected_card_key; BackScreen
    return hashMap

# Функция для поиска собранных позиций зказов 
def check_order_position(document): 
    if document.get("Отобрано") == document.get("КОтбору"):
        return True
    else:
        return False

# нажатие кнопки Выгрузить основного меню
def py_UploadOrders(hashMap, _files=None, _data=None):
    #Использование функции для поиска, вместо условий
    #передаем функцию как параметр, она работает с документом
    records = db['GoodsForSelection'].find([check_order_position])
    hashMap.put("ТоварыВыгрузить",json.dumps(records))
    # hashMap.put('VAR_DEBUG', "Точка 3")
    # android.stop(hashMap)
    return hashMap

def PeriodicLoadOrder(hashMap, _files=None, _data=None):

    hashMap.put("RunEvent",json.dumps([{"action": "runasync", 
                                        "type": "online", 
                                        "method": "ЗагрузитьДанные",
                                        "postExecute": '[{"action": "run","type": "python","method": "py_InsertRecords"}]'}]))
                                    #,
                                    #    {"action": "run", "type": "pythonscript", "method": "ZnJvbSBnZW5lcmFsIGltcG9ydCAqCgojYW5kcm9pZC5zdG9wKCkKICAgCtCX0LDQutCw0LfRi9CX0LDQs9GA0YPQt9C40YLRjD1qc29uLmxvYWRzKGhhc2hNYXAuZ2V0KCLQl9Cw0LrQsNC30YvQl9Cw0LPRgNGD0LfQuNGC0YwiKSkK0JfQsNCz0YDRg9C20LXQvdC+0JfQsNC60LDQt9C+0LIgPSBkYlsiT3JkZXJzRm9yU2VsZWN0aW9uIl0uaW5zZXJ0KNCX0LDQutCw0LfRi9CX0LDQs9GA0YPQt9C40YLRjCwgdXBzZXJ0PVRydWUpCgrQotC+0LLQsNGA0YvQl9Cw0LPRgNGD0LfQuNGC0Yw9anNvbi5sb2FkcyhoYXNoTWFwLmdldCgi0KLQvtCy0LDRgNGL0JfQsNCz0YDRg9C30LjRgtGMIikpCtCX0LDQs9GA0YPQttC10L3QvtCi0L7QstCw0YDQvtCyID0gZGJbIkdvb2RzRm9yU2VsZWN0aW9uIl0uaW5zZXJ0KNCi0L7QstCw0YDRi9CX0LDQs9GA0YPQt9C40YLRjCwgdXBzZXJ0PVRydWUpCg=="},
                                    #    {"action":"run","type":"set","method":"speak=Загружены новые заказы"}])) 
    return hashMap

# нажатие кнопки Закгрузить основного меню (после отработки обработчика 1С)
def py_InsertRecords(hashMap, _files=None, _data=None):
    if hashMap.containsKey("ЗаказыЗагрузить") and hashMap.containsKey("ТоварыЗагрузить"):
        try:
            with DBSession(db) as s:
                
                ЗаказыЗагрузить=json.loads(hashMap.get("ЗаказыЗагрузить"))
                ЗагруженоЗаказов = db["OrdersForSelection"].insert(ЗаказыЗагрузить, upsert=True, session=s)

                ТоварыЗагрузить=json.loads(hashMap.get("ТоварыЗагрузить"))
                ЗагруженоТоваров = db["GoodsForSelection"].insert(ТоварыЗагрузить, upsert=True, session=s)
                
                if len(ЗагруженоЗаказов) == int(hashMap.get("ЗагруженоЗаказов")) and len(ЗагруженоТоваров) == int(hashMap.get("ЗагруженоТоваров")):
                    #Надо сообщить об этом 1С
                    # android.stop(hashMap)
                    hashMap.put("RunEvent",json.dumps([{"action": "runasync", 
                                                            "type": "online", 
                                                            "method": "ДанныеВТСДЗагружены"}]))                    
                
        except Exception as e:
            hashMap.put("ErrorMessage ","Транзакция не записана:" + str(e))  

        # hashMap.put("_ZZ", str(len(ЗагруженоЗаказов)))
        # hashMap.put("_ZT", str(len(ЗагруженоТоваров)))
        # if len(ЗагруженоЗаказов) > 0 and len(ЗагруженоТоваров) > 0:
        # hashMap.put("Toast", "Загружено")#+str(len(ЗагруженоЗаказов))+" заказов из "+str(len(ЗагруженоТоваров))+ " товаров")
        # import requests
        # from requests.auth import HTTPBasicAuth

        # mainURL = "http://10.4.27.33/test/hs/simpleui"

        # url = mainURL+"/get_orderlist/"
        # data = {'user': 'user', 'password': 'password'}
        # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        # r = requests.post(url, data=json.dumps(data), headers=headers,
        #                   auth=HTTPBasicAuth('Белый'.encode('utf-8'), '20052019SO'))
        # hashMap.put("toast", str(r.status_code))

        # hashMap.put("toast","PeriodicLoadOrder")
    
    return hashMap
    






# -------------------
def init_on_start(hashMap, _files=None, _data=None):

    hashMap.put("SQLConnectDatabase", "")
    # hashMap.put("toast","init_on_start")

    # hashMap.put("getJSONConfiguration", "")
    # hashMap.put("ПервыйЗапуск", "1")
    # hashMap.put("_Debug_var", "") #Для отладки

    # if hashMap.containsKey("toast"):
    #     text1 = hashMap.get("toast")
    #     text1 = text1 + ",2"
    #     hashMap.put("toast",text1)
    # else:
    #     hashMap.put("toast","1")
    return hashMap


def py_OnStartMainMenu(hashMap, _files=None, _data=None):

    # hashMap.put("toast","py_OnStartMainMenu")

    sql = sqlClass()
    success = sql.SQLExec(
        "CREATE TABLE IF NOT EXISTS OrdersForSelection(ВидЗаказа text, НомерЗаказа text, Получатель text)", "")
    text_Err = ""
    if not success:
        text_Err = text_Err+'Не создана таблица заказов для отбора. '

    # success = sql.SQLExec("CREATE TABLE IF NOT EXISTS GoodsImg(Код text, ФотоТовара text, ИДФото text)","")
    # text_Err = ""
    # if not success:
    #     text_Err = text_Err+'Не создана таблица фотографий товара. '

    success = sql.SQLExec("CREATE TABLE IF NOT EXISTS GoodsForSelection(ВидЗаказа text,\
                                                                        НомерЗаказа text,\
                                                                        Получатель text,\
                                                                        Номенклатура text,\
                                                                        Код text,\
                                                                        Артикул text,\
                                                                        Производитель text,\
                                                                        ФотоТовара text,\
                                                                        Штрихкод text,\
                                                                        КоличествоСпланировано decimal(15,3),\
                                                                        КоличествоОтобрано decimal(15,3))","")
    if not success:
        text_Err = text_Err+'Не создана таблица товаров для отбора.'

    if text_Err != "":
        hashMap.put("beep", "")
        hashMap.put("ShowDialog", "Ошибка")
        hashMap.put("ShowDialogStyle",
                    "{'title': "+text_Err+",   'yes': '',   'no': 'OK' }")

    hashMap.put("backup_sql", "")

    return Update_central_table(hashMap, _files)
    # return hashMap


def py_LoadData(hashMap, _files=None, _data=None):

    sql = sqlClass()

    ЗаказыЗагрузить = json.loads(hashMap.get("ЗаказыЗагрузить"))
    success = sql.SQLExecMany(
        ЗаказыЗагрузить["query"], json.dumps(ЗаказыЗагрузить["params"]))

    ТоварыВЗаказахЗагрузить = json.loads(
        hashMap.get("ТоварыВЗаказахЗагрузить"))
    success = success and sql.SQLExecMany(
        ТоварыВЗаказахЗагрузить["query"], json.dumps(ТоварыВЗаказахЗагрузить["params"]))

    # ФотоТоваровЗагрузить=json.loads(hashMap.get("ФотоТоваровЗагрузить"))
    # success = sql.SQLExecMany(ФотоТоваровЗагрузить["query"],json.dumps(ФотоТоваровЗагрузить["params"]))

    if not success:
        hashMap.put("beep", "")
        hashMap.put("ShowDialog", "Ошибка загрузки")
        hashMap.put("ShowDialogStyle",
                    "{'title': 'Произошла ошибка загрузки.',   'yes': '',   'no': 'OK' }")

    # hashMap.put("toast","py_LoadData")

    # hashMap.put("toast",json.dumps(_files))

    res = sql.SQLQuery("select ИДФото,ФотоТовара from GoodsImg", "")

    records = json.loads(res)
    PathApp = suClass.get_temp_dir()
    # hashMap.put("toast",str(type(_files)))
    for record in records:
        # try:
        # hashMap.put("toast",'Проход '+str(i)+' '+ str(type(record['ФотоТовара'])))
        # i+=1
        image_64_decode = base64.b64decode(record['ФотоТовара'])

        # except Exception:

        Full_Name_File = PathApp+'/'+record['ИДФото']+'.jpg'
        # try:
        # создание изображения, доступного для записи, и запись результата декодирования
        image_result = open(Full_Name_File, 'wb')
        # except Exception:
        # hashMap.put("toast",str(type(image_result)))

        image_result.write(image_64_decode)
        # try:
        #     image_result.write(image_64_decode)
        # except Exception:
        #     hashMap.put("toast","image_result2")

        # _files.append({'id':record["ИДФото"],'path': Full_Name_File})
        # try:
        #     _files.append({'id':record["ИДФото"],'path': Full_Name_File})
        # except Exception:
        #     hashMap.put("toast","append")
        hashMap.put("addfile_"+record["ИДФото"], Full_Name_File)

        # for record in _files:
        # hashMap.put("toast",record['id']+record['path'])
        # hashMap.put("getfiles","")

        # rows.append({"ВидЗаказа":record['ВидЗаказа'],"НомерЗаказа":record['НомерЗаказа'],"Получатель":record['Получатель']})

        # success=sql.SQLExec("update GoodsImg set ФотоТовара=? where ИДФото=?",Full_Name_File+','+record['ИДФото'])
        # if  not success:
        #     hashMap.put("beep","15")
        #     hashMap.put("ShowDialog","Ошибка")
        #     hashMap.put("ShowDialogStyle","{'title': 'Ошибка записи в базу данных',   'yes': '',   'no': 'OK' }");
        # hashMap.put("toast",str(len(_files)))

        # hashMap.put("_files",json.dumps(_files))
    return hashMap


def py_DelTable(hashMap, _files=None, _data=None):

    sql = sqlClass()
    success = sql.SQLExec("DROP TABLE IF EXISTS OrdersForSelection", "")
    text_Err = ""
    if not success:
        text_Err = text_Err+'Не удалена таблица заказов для отбора. '

    success = sql.SQLExec("DROP TABLE IF EXISTS GoodsForSelection", "")
    if not success:
        text_Err = text_Err+'Не удалена таблица товаров для отбора.'

    res = sql.SQLQuery("select ИДФото,ФотоТовара from GoodsImg", "")
    records = json.loads(res)
    PathApp = suClass.get_temp_dir()
    for record in records:
        Full_Name_File = PathApp+'/'+record['ИДФото']+'.jpg'
        if os.path.isfile(Full_Name_File):
            os.remove(Full_Name_File)
            # hashMap.put("delfile_"+record["ИДФото"],"")
            # idx_del = -1
            # for jf in _files:
            #         if jf['id']==record['ИДФото']:
            #             idx_del = _files.index(jf)
            #             break
            # if idx_del>-1:
            #     # del A[X]
            #     _files.remove(jf)

    success = sql.SQLExec("DROP TABLE IF EXISTS GoodsImg", "")
    if not success:
        text_Err = text_Err+'Не удалена таблица фотографий товаров.'

    if text_Err != "":
        hashMap.put("beep", "")
        hashMap.put("ShowDialog", "Ошибка")
        hashMap.put("ShowDialogStyle",
                    "{'title': "+text_Err+",   'yes': '',   'no': 'OK' }")

    # hashMap.put("putfiles","")
    # hashMap.put("toast", str(len(_files)))
    return Update_central_table(hashMap, _files)


def Update_central_table(hashMap, _files):

    rows = []

    table = {
        "type": "table",
        "textsize": "10",

        "columns": [
            {
                "name": "ВидЗаказа",
                "header": "Вид заказа",
                "weight": "1"
            },
            {
                "name": "НомерЗаказа",
                "header": "№ заказа",
                "weight": "1"
            },
            {
                "name": "Получатель",
                "header": "Получатель",
                "weight": "2"
            }
        ]
    }

    try:
        for record in _files:
            rows.append(
                {"ВидЗаказа": record['id'], "НомерЗаказа": record['path'], "Получатель": record['path']})

        table['rows'] = rows

    except Exception:
        hashMap.put("toast", "Ошибка Update_central_table")
    finally:
        hashMap.put("central_table", json.dumps(table))

    # sql = sqlClass()
    # try:
    #     res = sql.SQLQuery("select ВидЗаказа,НомерЗаказа,Получатель from OrdersForSelection order by ВидЗаказа desc,Получатель","")

    #     records = json.loads(res)
    #     for record in records:
    #         rows.append({"ВидЗаказа":record['ВидЗаказа'],"НомерЗаказа":record['НомерЗаказа'],"Получатель":record['Получатель']})

    #     table['rows'] =rows

    # except Exception:
    #     hashMap.put("toast","Ошибка Update_central_table")
    # finally:
    #     hashMap.put("central_table",json.dumps(table))

    return hashMap


def py_Input(hashMap, _files=None, _data=None):
    fruits = ['apple', 'banana', 'cherry']
    fruits.append('orange')
    print(fruits)
    # if hashMap.get('listener')=='btn_start_log':
    #     hashMap.put('start_sys_log','')
    # elif hashMap.get('listener')=='btn_stop_log':
    #     hashMap.put('stop_sys_log','')
    # elif hashMap.get('listener')=='btn_send_log':
    #     hashMap.put('send_sys_log','http://192.168.1.143:2312/ui2/hs/simplewms/set_logmessages')
    # elif hashMap.get('listener')=='btn_clear_log':
    #     hashMap.put('clear_sys_log','')

    # hashMap.put("toast","Питон Input Экран")
    return hashMap


# +++ Область для офф-лайн работы

# Основное меню
def py_Selection(hashMap, _files=None, _data=None):

    # hashMap.put("НадписьЗаголовок_ВидЗаказа", "Выберите вид заказа")
    hashMap.put("ShowScreen", "Отбор")
    # hashMap.put("ТипЗадачи", "Перемещение")
    # hashMap.put("ШагОкна", "Ячейка")

    # hashMap = get_Task_Moving(hashMap)
    # success=sql.SQLExec("update goods set nom=? where id=1","Periodic -"+str(random.randint(10, 10000)))
    # res = sql.SQLQuery("select * from goods where id=1","")
    # if success:

    # hashMap.put("beep","15")
    return hashMap


def get_Task_Moving1(hashMap):  # Получим задачи перемещения
    sql = sqlClass()
    res = json.loads(sql.SQLQuery(
        "select * from tasks where ШагОперации = 0 and ТипЗадачи = 'Перемещение' order by ОбходПриОтборе limit 1", ""))
    if res == []:
        res = json.loads(sql.SQLQuery(
            "select * from tasks where ШагОперации = 1 and ТипЗадачи = 'Перемещение' order by ОбходПриРазмещении limit 1", ""))

    if res == []:
        hashMap.put("beep", "")
        hashMap.put("ShowDialog", "НетЗадач")
        hashMap.put("ShowDialogStyle",
                    "{'title': 'Не найдено задание. Выберите другую операцию или рабочий поток, или повторите попытку поиска задания позже.',   'yes': '',   'no': 'OK' }")
        hashMap.put("ShowScreen", "Основное меню")
    else:
        hashMap = Set_Vars(hashMap, res)
    return hashMap


# --------------------------------------------------------
def py_Moving(hashMap, _files=None, _data=None):

    hashMap.put("НадписьЗаголовок_ТипЗадачи", "ПЕРЕМЕЩЕНИЕ ТОВАРА")
    hashMap.put("ShowScreen", "Перемещение")
    # hashMap.put("ТипЗадачи", "Перемещение")
    hashMap.put("ШагОкна", "Ячейка")

    hashMap = get_Task_Moving(hashMap)
    # success=sql.SQLExec("update goods set nom=? where id=1","Periodic -"+str(random.randint(10, 10000)))
    # res = sql.SQLQuery("select * from goods where id=1","")
    # if success:

    # hashMap.put("beep","15")
    return hashMap


def get_Task_Moving(hashMap):  # Получим задачи перемещения
    sql = sqlClass()
    res = json.loads(sql.SQLQuery(
        "select * from tasks where ШагОперации = 0 and ТипЗадачи = 'Перемещение' order by ОбходПриОтборе limit 1", ""))
    if res == []:
        res = json.loads(sql.SQLQuery(
            "select * from tasks where ШагОперации = 1 and ТипЗадачи = 'Перемещение' order by ОбходПриРазмещении limit 1", ""))

    if res == []:
        hashMap.put("beep", "")
        hashMap.put("ShowDialog", "НетЗадач")
        hashMap.put("ShowDialogStyle",
                    "{'title': 'Не найдено задание. Выберите другую операцию или рабочий поток, или повторите попытку поиска задания позже.',   'yes': '',   'no': 'OK' }")
        hashMap.put("ShowScreen", "Основное меню")
    else:
        hashMap = Set_Vars(hashMap, res)
    return hashMap


def py_Placement(hashMap, _files=None, _data=None):

    hashMap.put("ШагОкна", "Контейнер")
    hashMap.put("НадписьЗаголовок_ТипЗадачи", "РАЗМЕЩЕНИЕ ТОВАРА")
    hashMap.put("ShowScreen", "Перемещение")
    # hashMap.put("ТипЗадачи", "Размещение")
    hashMap = get_Task_Placement(hashMap)
    # success=sql.SQLExec("update goods set nom=? where id=1","Periodic -"+str(random.randint(10, 10000)))
    # res = sql.SQLQuery("select * from goods where id=1","")
    # if success:

    # hashMap.put("beep","15")
    return hashMap


def get_Task_Placement(hashMap):  # Получим задачи размещения
    sql = sqlClass()
    res = json.loads(sql.SQLQuery(
        "select * from tasks_container where ШагОперации = 0 and ТипЗадачи = 'Размещение' order by ОбходПриОтборе limit 1", ""))
    if res == []:
        hashMap.put("ШагОкна", "Ячейка")
        res = json.loads(sql.SQLQuery(
            "select * from tasks where ШагОперации = 1 and ТипЗадачи = 'Размещение' order by ОбходПриРазмещении limit 1", ""))
    if res == []:
        hashMap.put("beep", "")
        hashMap.put("ShowDialog", "НетЗадач")
        hashMap.put("ShowDialogStyle",
                    "{'title': 'Не найдено задание. Выберите другую операцию или рабочий поток, или повторите попытку поиска задания позже.',   'yes': '',   'no': 'OK' }")
        hashMap.put("ShowScreen", "Основное меню")
    else:
        hashMap = Set_Vars(hashMap, res)
    return hashMap


def Set_Vars(hashMap, res):  # Заполним переменные
    for key, val in res[0].items():
        hashMap.put(key, str(val))
        if key == "ШагОперации":
            StepOperation = val
    if StepOperation == 0:
        hashMap.put("НадписьЗаголовок_Операция", "ВЗЯТЬ")
        hashMap.put("Ячейка", res[0]['ТекущаяЯчейка'])
    elif StepOperation == 1:
        hashMap.put("НадписьЗаголовок_Операция", "ПОЛОЖИТЬ")
        hashMap.put("Ячейка", res[0]['КонечнаяЯчейка'])
    return hashMap


def py_OnStartMoving(hashMap, _files=None, _data=None):

    # Видимость элементов
    if hashMap.get("ШагОкна") == "Ячейка":
        hashMap = Display_Elrment(hashMap, "Ячейка")
        hashMap = Display_Elrment(hashMap, "Контейнер", False, False)
        hashMap = Display_Elrment(hashMap, "Товар", True, False)
        hashMap = Display_Elrment(hashMap, "План", False, False)
        hashMap = Display_Elrment(hashMap, "Количество", True, False)
        hashMap.put("Show_barcode", "1")
    elif hashMap.get("ШагОкна") == "Товар":
        hashMap = Display_Elrment(hashMap, "Ячейка", True, False)
        hashMap = Display_Elrment(hashMap, "Контейнер", False, False)
        hashMap = Display_Elrment(hashMap, "Товар")
        hashMap = Display_Elrment(hashMap, "План", False, False)
        hashMap = Display_Elrment(hashMap, "Количество", True, False)
        hashMap.put("Show_barcode", "1")
    elif hashMap.get("ШагОкна") == "Количество":
        hashMap = Display_Elrment(hashMap, "Ячейка", True, False)
        hashMap = Display_Elrment(hashMap, "Контейнер", False, False)
        hashMap = Display_Elrment(hashMap, "Товар", True, False)
        hashMap = Display_Elrment(hashMap, "План", True, False)
        hashMap = Display_Elrment(hashMap, "Количество")
        hashMap.put("Show_barcode", "-1")
    elif hashMap.get("ШагОкна") == "Контейнер":
        hashMap = Display_Elrment(hashMap, "Ячейка", True, False)
        hashMap = Display_Elrment(hashMap, "Контейнер")
        hashMap = Display_Elrment(hashMap, "Товар", False, False)
        hashMap = Display_Elrment(hashMap, "Упаковка", False, False)
        hashMap = Display_Elrment(hashMap, "СтатусНоменклатуры", False, False)
        hashMap = Display_Elrment(hashMap, "ПартияНоменклатуры", False, False)
        hashMap = Display_Elrment(hashMap, "План", False, False)
        hashMap = Display_Elrment(hashMap, "Количество", False, False)
        hashMap.put("Show_barcode", "1")

    return Update_central_table(hashMap)


def py_OnInputMoving(hashMap, _files=None, _data=None):

    StepScreen = hashMap.get("ШагОкна")
    # hashMap.put("toast",hashMap.get("listener"))

    if hashMap.get("listener") == "barcode":  # Сканирование
        barcode = hashMap.get("barcode")
        if StepScreen == "Ячейка":
            hashMap.put("ПолеВвода_Ячейка", barcode)
        elif StepScreen == "Товар":
            hashMap.put("ПолеВвода_Товар", barcode)
        return Update_ScreenMoving(hashMap, StepScreen)
    elif hashMap.get("listener") is None:  # Кнопка вперед
        return Update_ScreenMoving(hashMap, StepScreen)
    elif hashMap.get("listener") == "BACK_BUTTON":  # Кнопка назад
        if StepScreen == "Ячейка":
            hashMap.put("ShowScreen", "Основное меню")
        elif StepScreen == "Товар":
            hashMap.put("ШагОкна", "Ячейка")
        elif StepScreen == "Количество":
            hashMap.put("ШагОкна", "Товар")
        return hashMap
    elif hashMap.get("listener") == "Положить":
        hashMap.put("ShowScreen", "Основное меню")
    elif hashMap.get("listener") == "Пропустить задачу":
        hashMap.put("ShowScreen", "Основное меню")
    elif hashMap.get("listener") == "Отменить задачу":
        hashMap.put("ShowScreen", "Основное меню")
    elif hashMap.get("listener") == "Заблокировать задачу":
        hashMap.put("ShowScreen", "Основное меню")
    elif hashMap.get("listener") == "Вернуться в меню":
        hashMap.put("ShowScreen", "Основное меню")
    else:
        return hashMap
    # StepScreen = hashMap.get("ШагОкна")
    # barcode = hashMap.get("barcode")
    # if StepScreen=="Ячейка":
    #     hashMap.put("ПолеВвода_Ячейка",barcode)
    # elif StepScreen=="Товар":
    #     hashMap.put("ПолеВвода_Товар",barcode)

    # return py_OnInputMovingForvard(hashMap)


def Update_ScreenMoving(hashMap, StepScreen):
    # def py_OnInputMovingForvard(hashMap,_files=None,_data=None):
    TypeTask = hashMap.get("ТипЗадачи")
    # if TypeTask == "Перемещение":

    StepScreen = hashMap.get("ШагОкна")
    if StepScreen == "Ячейка":
        if hashMap.get("ШагОперации") == "0":
            CurCell = hashMap.get("ТекущаяЯчейкаШтрихкод")
        elif hashMap.get("ШагОперации") == "1":
            CurCell = hashMap.get("КонечнаяЯчейкаШтрихкод")

        if hashMap.get("ПолеВвода_Ячейка") == CurCell:
            hashMap.put("ШагОкна", "Товар")
        else:
            hashMap.put("beep", "")
            hashMap.put("ShowDialog", "ОшибкаЯчейка")
            hashMap.put(
                "ShowDialogStyle", "{'title': 'Не найдена ячейка или задача',   'yes': '',   'no': 'OK' }")
    elif StepScreen == "Товар":
        if hashMap.get("ПолеВвода_Товар") == hashMap.get("Штрихкод") or hashMap.get("ПолеВвода_Товар") == hashMap.get("Артикул"):
            hashMap.put("ШагОкна", "Количество")
        else:
            hashMap.put("beep", "")
            hashMap.put("ShowDialog", "ОшибкаТовар")
            hashMap.put(
                "ShowDialogStyle", "{'title': 'Не верный штрихкод или артикул',   'yes': '',   'no': 'OK' }")
    elif StepScreen == "Количество":
        Kol = hashMap.get("ПолеВвода_Количество")
        Kol = "0" if Kol == "" else Kol
        if float(Kol) == float(hashMap.get("Количество")):
            if hashMap.get("ШагОперации") == "0":
                StepOperation = "1"
            elif hashMap.get("ШагОперации") == "1":
                StepOperation = "2"
            sql = sqlClass()
            success = sql.SQLExec("update tasks set ШагОперации=? where НомерДокумента=?",
                                  StepOperation+','+hashMap.get("НомерДокумента"))
            if success:
                hashMap.put("ШагОкна", "Ячейка")
                if TypeTask == "Перемещение":
                    hashMap = get_Task_Moving(hashMap)
                elif TypeTask == "Размещение":
                    hashMap = get_Task_Placement(hashMap)
            else:
                hashMap.put("beep", "15")
                hashMap.put("ShowDialog", "ОшибкаКоличество")
                hashMap.put(
                    "ShowDialogStyle", "{'title': 'Ошибка записи в базу данных',   'yes': '',   'no': 'OK' }")
        elif float(Kol) > float(hashMap.get("Количество")):
            hashMap.put("beep", "")
            hashMap.put("ShowDialog", "ОшибкаКоличество")
            hashMap.put(
                "ShowDialogStyle", "{'title': 'Превышено количество по задаче',   'yes': '',   'no': 'OK' }")
            hashMap.put("ПолеВвода_Количество", "0")
        elif float(Kol) == 0:
            hashMap.put("beep", "")
            hashMap.put("ShowDialog", "ОшибкаКоличество")
            hashMap.put(
                "ShowDialogStyle", "{'title': 'Количество не может быть равно нулю',   'yes': '',   'no': 'OK' }")
            hashMap.put("ПолеВвода_Количество", "0")
    elif StepScreen == "Контейнер" and TypeTask == "Размещение":
        if hashMap.get("ПолеВвода_Контейнер") == hashMap.get("Штрихкод") or hashMap.get("ПолеВвода_Контейнер") == hashMap.get("Контейнер"):
            if hashMap.get("ШагОперации") == "0":
                StepOperation = "1"
            elif hashMap.get("ШагОперации") == "1":
                StepOperation = "2"
            sql = sqlClass()
            success = sql.SQLExec("update Tasks_container set ШагОперации=? where НомерДокумента=?",
                                  StepOperation+','+hashMap.get("НомерДокумента"))
            if success:
                success = sql.SQLExec("update tasks set ШагОперации=? where ПеремещениеКонтейнера=? and ТипЗадачи = 'Размещение'",
                                      StepOperation+','+hashMap.get("НомерДокумента"))
                # hashMap.put("ШагОкна","Ячейка")
                hashMap = get_Task_Placement(hashMap)
            else:
                hashMap.put("beep", "15")
                hashMap.put("ShowDialog", "ОшибкаКоличество")
                hashMap.put(
                    "ShowDialogStyle", "{'title': 'Ошибка записи в базу данных',   'yes': '',   'no': 'OK' }")
        else:
            hashMap.put("beep", "")
            hashMap.put("ShowDialog", "ОшибкаКонтейнер")
            hashMap.put(
                "ShowDialogStyle", "{'title': 'Контейнер не найден',   'yes': '',   'no': 'OK' }")

    return hashMap


def py_test(hashMap, _files=None, _data=None):

    import requests
    from requests.auth import HTTPBasicAuth

    mainURL = "http://10.4.27.33/test/hs/simpleui"

    url = mainURL+"/get_orderlist/"
    data = {'user': 'user', 'password': 'password'}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    r = requests.post(url, data=json.dumps(data), headers=headers,
                      auth=HTTPBasicAuth('Белый'.encode('utf-8'), '20052019SO'))
    hashMap.put("toast", str(r.status_code))
#    if r.status_code==200:

#     response = r.json()

#     if response.get("status")==0:
#       connection_settings = {
#          "OnlineSplitMode":True,
#          "onlineURLListener":mainURL,
#          "OnlineSplitMode ":True,
#          "onlineUserListener":user,
#          "onlinePassListener":password
#       }

#       hashMap.put("SetSettingsJSON",json.dumps(connection_settings,ensure_ascii=False))

#       ncl = noClass("pure_settings")
#       ncl.put("pure_db",user,True)
#       ncl.put("pure_password",password,True)
#       ncl.put("pure_qr",json.dumps(connection_settings,ensure_ascii=False),True)

#       hashMap.put("_master_registration","")
#       hashMap.put("RunNewProcess","Раздача")

#       hashMap.put("toast","Успешная авторизация")

#       hashMap.put("RunEvent",json.dumps([{"action": "run","type": "online","method": "update_menu", "postExecute": "" }]))

#     elif response.get("status")==-1:
#       hashMap.put("toast","Неправильные учетные данные")
#    else:
#       hashMap.put("toast","Ошибка подключения")

    return hashMap


# --- Область для офф-лайн работы


# hashMap.get("ЗадачиПермещенияКонтейнеров")

# def py_onInputCell(hashMap,_files=None,_data=None):
#     if hashMap.get("ПолеВвода_Ячека")==hashMap.get("ТекущаяЯчейкаШтрихкод"):
#         hashMap.put("Show_Надпись_Ячейка","1")
#         hashMap.put("Show_НадписьНад_Ячейка","-1")
#         hashMap.put("Show_ПолеВвода_Ячека","-1")
#         hashMap.put("Show_НадписьКомментарий_Ячека","-1")
#         hashMap.put("Show_НадписьНад_Товар","1")
#         hashMap.put("Show_Надпись_Товар","-1")
#         hashMap.put("Show_ПолеВвода_Товар","1")
#         hashMap.put("Show_НадписьКомментарий_Товар","1")
#     else:
#         hashMap.put("beep","")
#         hashMap.put("ShowDialog","ОшибкаЯчейка")
#         hashMap.put("ShowDialogStyle","{'title': 'Не найдена ячейка или задача',   'yes': '',   'no': 'OK' }");

#     return hashMap

# def py_onInputGoods(hashMap,_files=None,_data=None):
#     if hashMap.get("ПолеВвода_Товар")==hashMap.get("Штрихкод") or hashMap.get("ПолеВвода_Товар")==hashMap.get("Артикул"):
#         hashMap.put("Show_НадписьНад_Товар","-1")
#         hashMap.put("Show_Надпись_Товар","1")
#         hashMap.put("Show_ПолеВвода_Товар","-1")
#         hashMap.put("Show_НадписьКомментарий_Товар","-1")
#         hashMap.put("Show_Контейнер_План","1")
#         hashMap.put("Show_ПолеВвода_Количество","1")
#         hashMap.put("Show_Надпись_Количество","-1")
#         hashMap.put("Show_НадписьКомментарий_Количество","1")
#     else:
#         hashMap.put("beep","")
#         hashMap.put("ShowDialog","ОшибкаТовар")
#         hashMap.put("ShowDialogStyle","{'title': 'Не верный штрихкод или артикул',   'yes': '',   'no': 'OK' }");

#     return hashMap

# def py_OnInputKol(hashMap,_files=None,_data=None):
#     if float(hashMap.get("ПолеВвода_Количество"))==float(hashMap.get("Количество")):
#         hashMap.put("Show_НадписьНад_Товар","-1")
#         hashMap.put("Show_Надпись_Товар","1")
#         hashMap.put("Show_НадписьКомментарий_Товар","-1")
#         hashMap.put("Show_Контейнер_План","1")
#         hashMap.put("Show_ПолеВвода_Количество","1")
#         hashMap.put("Show_Надпись_Количество","-1")
#         hashMap.put("Show_НадписьКомментарий_Количество","1")
#     elif float(hashMap.get("ПолеВвода_Количество")) > float(hashMap.get("Количество")):
#         hashMap.put("beep","")
#         hashMap.put("ShowDialog","ОшибкаКоличество")
#         hashMap.put("ShowDialogStyle","{'title': 'Превышено количество по задаче',   'yes': '',   'no': 'OK' }");

#     return hashMap

    # sql = sqlClass()

    # success=sql.SQLExec("update goods set nom=? where id=1","Periodic -"+str(random.randint(10, 10000)))
    # res = sql.SQLQuery("select * from goods where id=1","")
    # if success:

    #     hashMap.put("beep","15")
