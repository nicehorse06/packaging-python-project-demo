# Example Package

## 問題
* 目前執行測試會因為沒有django settings而報錯
```
raise ImproperlyConfigured(
django.core.exceptions.ImproperlyConfigured: Requested settings, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
```
* 如何像django-rest-framework這種django套件一樣，引入`from django.conf import settings`使用，並且測試不報錯
    * 
    * [django-rest-framework的使用場景](https://github.com/encode/django-rest-framework/blob/71e6c30034a1dd35a39ca74f86c371713e762c79/rest_framework/settings.py)
    * [django-rest-framework的測試](https://github.com/encode/django-rest-framework/blob/71e6c30034a1dd35a39ca74f86c371713e762c79/tests/test_settings.py)



## 執行流程
* `pip install -r requirements.txt`，install requirements.txt 
* `python -m unittest tests/test_*`，run test

## project build
This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

```shell
python -m pip install --upgrade build
python -m build
```