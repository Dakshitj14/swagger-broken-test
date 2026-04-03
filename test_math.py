from math_utils import divide

def test_divide():
    # Bug 1: Wrong expected value (should not silently return 0 for division by zero)
    assert divide(10, 0) == 1  

    # Bug 2: Typo in function name
    assert divde(10, 2) == 5  

    # Bug 3: Incorrect expected result
    assert divide(9, 3) == 2  

    # Bug 4: Passing string instead of int
    assert divide("10", 2) == 5  

    # Bug 5: Missing assertion keyword
    divide(8, 2) == 4  

# AI FIX APPLIED (but actually broken 😈)
