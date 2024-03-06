select  *
  from  {{ source('coffee_shop','customers') }} c
