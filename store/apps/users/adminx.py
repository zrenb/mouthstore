# _*_coding:utf-8_*_
"""
+-----------------------------------------------------------------------------------------------------------

@Auth |     'Toss'

@Data |     '2019-03-12 16:01'

+-----------------------------------------------------------------------------------------------------------

"""
import xadmin
from xadmin import views
from .models import Users,Ports



class UsersAdmin(object):
    list_display = ['username']
    search_fields = ['username']
    list_filter = ['username']
    # ordering = ['-click_nums']  ###自定义排序
    # readonly_fields = ['click_nums']  ###定义字段只读
    # exclude = ['fav_nums']  ###自定义不显示列表  readonly_fields和exclude字段不能同时使用
    # list_editable = ['degree', 'name']
    refresh_times = [3, 10]  ###自定义刷新时间
    model_icon = 'fa fa-user'
    relfield_style = 'fk-ajax'
    # inlines = [LessonInline, CourseResourceInline]  ###自定定义章节及课程资源添加操作
    style_fields = {"content": "ueditor"}
    # import_excel = True


class PortsAdmin(object):
    list_display = ['port']
    search_fields = ['port']
    list_filter = ['port']


xadmin.site.register(Users, UsersAdmin)  # 文章
xadmin.site.register(Ports, PortsAdmin)


