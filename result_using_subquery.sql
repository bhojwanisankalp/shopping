select user.id, user.name, role.name as role_name, department.name as department_name
from user
    inner join (select user_id, role_id from user_role_map) as user_role
        on user_role.user_id = user.id
    inner join role
        on role.id = user_role.role_id
    inner join department
        on department.id = role.department_id order by user.id