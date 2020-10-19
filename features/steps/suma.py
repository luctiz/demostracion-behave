from behave import *

@when(u'hacemos 2+2')
def step_impl(context):
    context.resultado = 2+2


@then(u'obtenemos 4')
def step_impl(context):
    assert context.resultado == 4


@given('x vale 2 e y vale 3')
def step_impl(context):
    context.x=2
    context.y=3

@when('hacemos x+y')
def step_impl(context):
    context.resultado = (context.x + context.y)

@then('obtenemos 5')
def step_impl(context):
    assert context.resultado == 5


@given(u'x vale 2, y vale 2, z vale -4')
def step_impl(context):
    context.x=2
    context.y=2
    context.z=-4


@when(u'hacemos x+y+z')
def step_impl(context):
    context.resultado = context.x + context.y + context.z


@then(u'obtenemos 0')
def step_impl(context):
    assert context.resultado == 0

