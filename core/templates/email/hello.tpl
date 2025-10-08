{% extends "mail_templated/base.tpl" %}

{% block subject %}

{% endblock %}

{% block html %}
{{token}}
{% endblock %}