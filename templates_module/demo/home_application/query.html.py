# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1565505799.898
_enable_loop = True
_template_filename = 'E:/python/framework/templates/home_application/query.html'
_template_uri = '/home_application/query.html'
_source_encoding = 'utf-8'
_exports = [u'content', u'footerline']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def footerline():
            return render_footerline(context._locals(__M_locals))
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footerline'):
            context['self'].footerline(**pageargs)
        

        __M_writer(u'\r\n<script>\r\n    $("#check").click(\r\n    function(){\r\n    $.ajax({\r\n      url:"/search/",\r\n      type:\'post\',\r\n      data:{"name":"asdafafd"},\r\n      success:function(res){\r\n        console.log(res)\r\n        alert(res);\r\n      }\r\n    })\r\n    }\r\n    )\r\n\r\n    function query(){\r\n        $.ajax({\r\n          url:"/search/",\r\n          type:\'post\',\r\n          dataType : "JSON",\r\n          data:{"aaaa":121221},\r\n          success:function(res){\r\n            console.log(res)\r\n          }\r\n        })\r\n    }\r\n</script>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n    <style type="text/css">\r\n        #footer{\r\n            position: relative;\r\n            bottom: -40px;\r\n        }\r\n    </style>\r\n      <div class="page-contactus">\r\n          <button type="button" id="check" name="check" onclick = "query()" value="\u53c2\u6570">\u53c2\u6570</button>\r\n          <a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'contactus" target="_blank">\u70b9\u51fb\u4e0b\u8f7d</a>\r\n      </div>\r\n    <div class="col-sm-6">\r\n        <div class="king-block king-block-bordered">\r\n            <div class="king-block-content clearfix">\r\n                <div class="plugin3_demo" id="plugin3_demo3" style="display:inline-block;">\r\n                    <tx>\r\n                        <td>\u4e1a\u52a1</td>\r\n\u3000                    \u3000<td>\r\n                           <select id="businessSelect">\r\n\u3000                     \u3000\u3000\u3000 <option>\u9009\u62e9A</option>\r\n\u3000\u3000\u3000\u3000                      <option>\u9009\u62e9B</option>\r\n\u3000\u3000\u3000\u3000                      <option>\u9009\u62e9C</option>\r\n\u3000\u3000                      </select>\r\n                        </td>\r\n                    </tx>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footerline(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footerline():
            return render_footerline(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n    <hr class="guide-cutting-line">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"68": 33, "37": 1, "42": 32, "47": 35, "80": 74, "74": 33, "53": 2, "27": 0, "60": 2, "61": 11, "62": 11}, "uri": "/home_application/query.html", "filename": "E:/python/framework/templates/home_application/query.html"}
__M_END_METADATA
"""
