select user.id, user.name, role.name as role_name, department.name as department_name
from user
    join user_role_map
        on user_role_map.user_id = user.id
    join role
        on role.id = user_role_map.role_id
    join department
        on department.id = role.department_id order by user.id