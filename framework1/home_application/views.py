# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""
import json

import requests
from requests import request
from conf.default import *
from common.log import logger

logger.debug("debug日志信息")
logger.info("info日志信息")
logger.error("info日志信息")
from common.mymako import render_mako_context, render_json


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def demo(request):
    """
    联系我们
    """
    print request.POST.dict()
    return render_mako_context(request, '/home_application/business.html')

def dataTest(request):
    """
    联系我们
    """
    print request.POST.dict()
    print request.GET.dict()
    return render_json({'result':'true'})

from common.log import logger

def getBusiness(req):
    """
    联系我们
    """
    data ={
       "bk_app_code": APP_ID,
       "bk_app_secret": APP_TOKEN,
       "bk_username": "admin",
    }
    url = "http://paas.bkds.com/api/c/compapi/v2/cc/search_business/"
    res = requests.post(url,json=data)
    print(res.content)
    print(json.loads(res.content).data.info.bk_biz_id)
    return render_json(json.loads(res.content))

def getHosts(req):
    """
    联系我们
    """
    data ={
       "bk_app_code": APP_ID,
       "bk_app_secret": APP_TOKEN,
       "bk_username": "admin",
    }
    url = "http://paas.bkds.com/api/c/compapi/v2/cc/search_host/"
    res = requests.post(url,json=data)
    print(res.content)
    print(json.loads(res.content))
    return render_json(json.loads(res.content))

def executeResult(req):
    """
    联系我们
    """
    data ={
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_token": "20e75720-86f5-4936-b384-8974d09c66dd",
        "bk_biz_id": 2,
        "script_id": 6,
        "script_content": "ZWNobyAkMQ==",
        "script_param": "aGVsbG8=",
        "script_timeout": 1000,
        "account": "root",
        "script_type": 1,
        "is_param_sensitive": 0,
        "ip_list": [
            {
                "bk_cloud_id": 0,
                "ip": "192.168.3.213"
            }
        ]
    }
    url = "http://paas.bkds.com/api/c/compapi/v2/job/fast_execute_script/"
    res = requests.post(url,json=data)
    print(res.content)
    print(json.loads(res.content))
    return render_json(json.loads(res.content))
