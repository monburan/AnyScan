# -*- coding: utf-8 -*-

"""
 * Copyright(C) Anyuntec 2017.
 *
 * poc执行
 *
 * @author margin 2017/03/12.
 *
 * @version V1.00.
 *
 * 更新履历： V1.00 2017/03/12 margin 创建.
 *
 """

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json,traceback,uuid,datetime,sys
from AnyScanUI.epoc.ExecPoc import ExecPoc

@method_decorator(csrf_exempt)
def exe_poc(req):
    """
    poc执行
    :param req:
    :return:
    """
    data=json.loads(req.body)
    targets = data.get("targets").encode("utf-8")
    threads = 10
    payload = data.get("payload").encode("utf-8")
    commond = data.get("commond").encode("utf-8")

    result = {"status":True,"msg":"成功","data":"","id":[]}
    try:

        exe = ExecPoc(targets,payload,threads,commond)
        result["id"] = exe.start()

    except Exception:
        result = {"status":False,"msg":"POC执行异常","data":traceback.format_exc()}
        print traceback.format_exc()
    return HttpResponse(json.dumps(result, ensure_ascii=False))