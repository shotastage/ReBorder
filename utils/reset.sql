/*
THIS QUERY WILL DELETE ALL USER INFORMATION IN MOMENT.
DO NOT EXECUTE THIS IF YOU RUN SFCOIN ON PRODUCT ENV.
DO NOT EXECUTE THIS IF YOU STORE IMPORTANT DATA BEFORE YOU BACKUP IT.
DO NOT EXECUTE THIS IF YOU DELETE SPECIFIC USERS INFORMATION. ANOTHER WAY IS AVAILABLE.
*/
/* Reset DataBase crealy */
DROP TABLE IF EXISTS
auth_group, auth_groups, auth_group_permissions,
auth_permission, auth_user,
auth_user_groups, auth_user_user_permissions,
django_admin_log, django_content_type,
django_migrations, django_session
CASCADE;
DROP TABLE IF EXISTS
research
CASCADE;
