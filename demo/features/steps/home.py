from behave import given, when


@given('the User is on Football Reference')
def step_impl(context):
    context.driver.get(context.URL)
