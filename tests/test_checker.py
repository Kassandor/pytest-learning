from app.checker import check_sign


def test_check_sign_positive():
    assert check_sign(10) == "positive"
    assert check_sign(-10) == "zero or negative"
