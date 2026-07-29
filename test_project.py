import pytest
from project import check_validation,get_user_data,choose_function
from calorie_calculator import CALculator
from create_user import User

def main():
    test_get_user_data()
    test_check_validation()
    test_choose_function()


def test_check_validation():
    assert check_validation({"age":[int, "25"]}) == {"age":25}
    assert check_validation({"sex": [str, "male"]}) == {"sex":"male"}
    with pytest.raises(ValueError):
        check_validation({"sex": [str, "cat"]})
    with pytest.raises(ValueError):
        check_validation({"activity":[int, "8"]})

def test_choose_function(monkeypatch):
    user = User(
        name="Ink",
        age=27,
        weight=68,
        height=151,
        sex="female",
        activity=2,
        goal=1,
        target=0.3
    )

    calculator = CALculator(user)
    monkeypatch.setattr("builtins.input", lambda _: "1")
    assert choose_function(calculator) == calculator.bmr

def test_get_user_data(monkeypatch):
    answers = iter([
    "Alice",
    "25",
    "68",
    "151",
    "female",
    "2",
    "1",
    "0.5"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    result = get_user_data()

    assert result["name"] == [str, "Alice"]
    assert result["age"] == [int, "25"]
    assert result["weight"] == [int, "68"]

if __name__ == "__main__":
    main()