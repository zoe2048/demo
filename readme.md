### 实现内容
参照网站 http://quotes.toscrape.com/，使用django框架实现搭建一个一样的网站


### 数据来源
网站中呈现的数据使用scrapy事先爬取存储至mysql数据库


### 注意事项
- 可能出现的问题：若直接clone代码到本地，运行服务（python manage.py runserver)出现数据库等相关错误，
尝试执行（python manage.py inspectdb > quotes/models.py），检测已有数据库自动创建models.py内的数据模型内容。
- clone代码到本地后，先修改settings.py的数据库设置