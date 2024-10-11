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
                                                     {"НомерЗаказа": hashMap.get("НомерЗаказа")},
                                                     {"ПозицияСобрана": False}]})
    if len(records) > 0:
        # hashMap.put("Records", json.dumps(records))
        # hashMap.put("ДляОтладки", "Количество найденых записей >0")
        # android.stop(hashMap)
        i = 1
        for record in records:
            # if (record['КОтбору'] == record['Отобрано']):
            #     continue
            
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
                "КОтбору": record['КОтбору'],
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
        hashMap.remove("CardsGoods")
        hashMap.put("OrderCollected", "True")    
        Set_Order_Collected(hashMap)

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
    OrderCollected = eval(hashMap.get("OrderCollected") if hashMap.containsKey("OrderCollected") else "False")
    
    hashMap.put("Заголовок", hashMap.get("ВидЗаказа").upper() if OrderIsSelect else "ВЫБЕРИТЕ ЗАКАЗ")
    hashMap.put("Show_Контейнер_Получатель", "1" if OrderIsSelect else "-1")
    hashMap.put("Show_Контейнер_ВремяОстатков", "1" if OrderIsSelect and not OrderCollected else "-1")
    hashMap.put("Show_Контейнер_Товар", "1" if OrderIsSelect and not OrderCollected else "-1")
    hashMap.put("Show_TextOrderCollected", "1" if OrderCollected and OrderIsSelect else "-1")
    # hashMap.put("VarOrderCollected", str(OrderCollected))
    # android.stop(hashMap)
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
    NewSelQty = card_of_goods['Отобрано']+qty
    if card_of_goods['КОтбору'] > NewSelQty:
        db["GoodsForSelection"].update({"$and": [{"ВидЗаказа": hashMap.get('ВидЗаказа')},
                                                {"НомерЗаказа": hashMap.get('НомерЗаказа')},
                                                {"Код": card_of_goods['Код']}]},
                                    {"Отобрано": NewSelQty})
    elif card_of_goods['КОтбору'] == NewSelQty:
        db["GoodsForSelection"].update({"$and": [{"ВидЗаказа": hashMap.get('ВидЗаказа')},
                                                {"НомерЗаказа": hashMap.get('НомерЗаказа')},
                                                {"Код": card_of_goods['Код']}]},
                                    {"Отобрано": NewSelQty, "ПозицияСобрана": True})
    else:
        hashMap.put("beep", "15")
        hashMap.put("ShowDialog", "Внимание!")
        hashMap.put("ShowDialogStyle", "{'title': 'Превышение количества!',   'yes': '',   'no': 'OK' }")
        
        
    return hashMap

# при старте экрана выбора заказа
def py_OrderList_OnStart(hashMap, _files=None, _data=None):

    hashMap.put("SetTitle", "ВЫБОР ЗАКАЗА")

    db = pelicans["TA_WMS"]
    recordsZP = db["OrdersForSelection"].find({"ВидЗаказа": "Заказ покупателя"})
    recordsVZ = db["OrdersForSelection"].find({"ВидЗаказа": "Внутренний заказ"})

    list_btn = "Заказы покупателя("+str(len(recordsZP))+")"
    list_btn = list_btn + ";Внутренние заказы("+str(len(recordsVZ))+")"
    hashMap.put("list_btn", list_btn)
    if not hashMap.containsKey("btn_z"):
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
    # Пока собранные товары не буду выгржать, только собранные заказы
    #Использование функции для поиска, вместо условий
    #передаем функцию как параметр, она работает с документом
    # records = db['GoodsForSelection'].find([check_order_position])
    # hashMap.put("ТоварыВыгрузить",json.dumps(records))

    Orders = db['OrdersForSelection'].find({"ЗаказСобран":True})
    Goods = db['GoodsForSelection'].find({"ПозицияСобрана":True})
    if len(Orders)>0 and len(Goods)>0:
        hashMap.put("ЗаказыСобранные",json.dumps(Orders))
        hashMap.put("ТоварыСобранные",json.dumps(Goods))
        hashMap.put("RunEvent",json.dumps([{"action": "run", 
                                            "type": "online", 
                                            "method": "ВыгрузитьДанные"}]))
    
    else: 
        hashMap.remove("ЗаказыСобранные")
        hashMap.remove("ТоварыСобранные")
        hashMap.put("toast","Нет данных для выгрузки")
    
    # Для отладки
    # hashMap.put('VAR_DEBUG', "Точка 3")
    # android.stop(hashMap)
    return hashMap

# удаляем выгруженные в 1С заказы (после отработки обработчика 1С)
def py_DeleteRecords(hashMap, _files=None, _data=None):
    # Для отладки
    hashMap.put('VAR_DEBUG', 'py_DeleteRecords')
    android.stop(hashMap)

    # dbmap = {"TA_WMS":db}
    # res = feed(dbmap,json.loads(hashMap.get("стрДляFeedPelican")))
    
    # hashMap.put('VAR_DEBUG', 'feed')
    # android.stop(hashMap)
    # if hashMap.containsKey("ЗаказыСобранные"):
    #     # recordsZS=json.loads(hashMap.get("ЗаказыСобранные"))
    #     # hashMap.put('VAR_DEBUG', "Точка 2")
    #     # hashMap.put('VAR_recordsZS', json.dumps(recordsZS))
    #     # android.stop(hashMap)
    #     # for record in recordsZS:
    #         # hashMap.put('VAR_DEBUG', "Точка 3")
    #         # hashMap.put("Удаляемая запись", record["ВидЗаказа"]+record["НомерЗаказа"])
    #         # android.stop(hashMap)
    #         # pelicans["TA_WMS"]["OrdersForSelection"].delete([record["_id"]])

    #         # db["OrdersForSelection"].delete({"$and": [{"ВидЗаказа": record["ВидЗаказа"]},
    #         #                                     {"НомерЗаказа": record["НомерЗаказа"]}]})
    #         # db["OrdersForSelection"].shrink()
            
    #         # db["GoodsForSelection"].delete({"$and": [{"ВидЗаказа": record["ВидЗаказа"]},
    #         #                                     {"НомерЗаказа": record["НомерЗаказа"]}]})
    #         # db["GoodsForSelection"].shrink()
            
    #         # db = pelicans["TA_WMS"]
            
    #         # hashMap.put('ЗаказКУдалению', json.dumps(pelicans["TA_WMS"]["OrdersForSelection"].find({"$and": [{"ВидЗаказа": record["ВидЗаказа"]},
    #         #                                                                         {"НомерЗаказа": record["НомерЗаказа"]}]})))
    #         # hashMap.put('ТоварыКУдалению', json.dumps(pelicans["TA_WMS"]["GoodsForSelection"].find({"$and": [{"ВидЗаказа": record["ВидЗаказа"]},
    #         #                                                                         {"НомерЗаказа": record["НомерЗаказа"]}]})))
    #         # hashMap.put('VAR_DEBUG', record["_id"]+" "+record["ВидЗаказа"]+" "+record["НомерЗаказа"])
    #         # android.stop(hashMap)
            
    #         # hashMap.put('ЗаказКУдалению',"")    
    #         # hashMap.put('ТоварыКУдалению', "")
    #     try:
    #         with DBSession(db) as s:
                
    #             db["OrdersForSelection"].delete({"ЗаказСобран":True})
    #             db["GoodsForSelection"].delete({"ПозицияСобрана": True})

    #             # db["OrdersForSelection"].shrink()
    #             # db["GoodsForSelection"].shrink()
    #             # recordsZS=json.loads(hashMap.get("ЗаказыСобранные"))
    #             # for record in recordsZS:
    #                 # db["OrdersForSelection"].delete({"$and": [{"ВидЗаказа": record["ВидЗаказа"]},
    #                 #                                  {"НомерЗаказа": record["НомерЗаказа"]}]}, session=s)
                    
    #                 # db["GoodsForSelection"].delete({"$and": [{"ВидЗаказа": record["ВидЗаказа"]},
    #                 #                                  {"НомерЗаказа": record["НомерЗаказа"]}]}, session=s)
                
    #     except Exception as e:
    #         hashMap.put("ErrorMessage ","Транзакция не записана:" + str(e))  

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
            # hashMap.remove("ЗаказыЗагрузить")    
            # hashMap.remove("ТоварыЗагрузить")    
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
    

