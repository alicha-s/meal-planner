import pytest
from create_user import User

def main():
    test_success()

def test_success():
    user = User("Enzo",24,56,176,"male",1,3,0.3)
    assert user.weightgain_tdee() == 2184

if __name__ == "__main__":
    main()