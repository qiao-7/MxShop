from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = '用户管理'

    def ready(self):
        import users.signals

        # AppConfig自定义的函数，会在django启动时被运行
        # 现在添加用户的时候，密码就会自动加密存储了