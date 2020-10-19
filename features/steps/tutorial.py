from behave import *

@given('tenemos behave instalado')
def step_impl(context):
    pass

@when('implementamos una prueba')
def step_impl(context):
    assert True is not False

@then('behave va a testearla por nosotros!')
def step_impl(context):
    assert context.failed is False
