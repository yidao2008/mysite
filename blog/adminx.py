import xadmin

from .models import Post



class BlogAdmin(object):
    list_display = ['title', 'slug', 'created', 'author', 'status']

    # 搜索
    search_fields = ['title', 'slug', 'created', 'author']

    # 过滤
    list_filter = ['created','publish']

    # 小图标
    model_icon = 'fa fa-th-list'

    # 只读字段
    #readonly_fields = ['user', 'pay_status', 'pay_time', 'add_time', 'total_amount', 'order_no', 'trade_no',
                       # 'receive_way', 'order_id', 'pay_url']
    # 每页显示几条
    list_per_page = 10

    # list_editable 设置默认可编辑字段
    list_editable = ['title', 'slug']

    style_fields = {'content':'ueditor'}

    # fk_fields 设置显示外键字段
    # fk_fields = ('machine_room_id',)
xadmin.site.register(Post,BlogAdmin)