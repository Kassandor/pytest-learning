def test_admin_settings(admin_user):
    if admin_user.is_admin():
        print('Доступ разрешен')
    assert admin_user.is_admin() == True
