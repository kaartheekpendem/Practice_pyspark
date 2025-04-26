from behave import given, when, then
from primenumbers import primenums  # Replace 'your_function_file' with the actual file name

@given('the input number {num:d}')
def given_input_number(context, num):
    context.num = num

@when('the function is executed')
def execute_function(context):
    context.output = primenums(context.num)

@then('the output type should be {expected_type}')
def validate_output_type(context, expected_type):
    # Compare output type with the expected type
    assert str(type(context.output)) == expected_type, f"Expected {expected_type}, but got {type(context.output)}"