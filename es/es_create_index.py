# coding=UTF-8
'''
@Author: xiaoyichao
LastEditors: xiaoyichao
@Date: 2020-01-02 16:55:23
LastEditTime: 2020-08-12 18:41:05
@Description: 

'''
from es_operate import ESCURD
from elasticsearch import Elasticsearch
import os
import configparser


dir_name = os.path.abspath(os.path.dirname(__file__))
es_config = configparser.ConfigParser()
es_config.read(os.path.join(dir_name, "es.ini"))
es_server_ip_port = es_config["ServerAddress"]["es_server_ip_port"]

# 使用配置文件中的index_name，也可以自己命名，创建其他名称的索引
index_name_1 = es_config["ServerInfo"]["index_name_1"]
index_name_2 = es_config["ServerInfo"]["index_name_2"]

http_auth_user_name = es_config["ServerAddress"]["http_auth_user_name"]
http_auth_password = es_config["ServerAddress"]["http_auth_password"]

es_connect = Elasticsearch(
    es_server_ip_port, http_auth=(http_auth_user_name, http_auth_password))
es_faq = ESCURD(es_connect)

if __name__ == "__main__":
    es_faq.create_index(index_name=index_name_1)
    # es_faq.create_index(index_name=index_name_2)
