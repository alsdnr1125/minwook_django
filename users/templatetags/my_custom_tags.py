from django import template

register = template.Library()


@register.simple_tag
def my_tag():
	exec(open("C:/Users/user/PycharmProjects/Empyhsema_code/Emphysema_detection.py", encoding='UTF8').read())
	return "Hello World"