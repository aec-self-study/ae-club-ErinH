{% test email_format(model, column_name) %}
    select *
    from {{ model }} 
    where {{ column_name }} not like '%@%.%'
 {% endtest %}