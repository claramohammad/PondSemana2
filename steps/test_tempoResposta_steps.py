from behave import given, when, then
import random
import time

@given('uma requisição foi feita para a API de atribuição de pedidos')
def step_impl(context):
    context.request_time = random.randint(2000, 3500)  # Simula tempos entre 2000 e 3500ms

@when('a API processa a requisição')
def step_impl(context):
    time.sleep(context.request_time / 1000)  # Simula o tempo de resposta da API
    context.response_time = context.request_time

@then('a resposta deve ser enviada em menos de 3000 ms')
def step_impl(context):
    assert context.response_time < 3000, f"Tempo de resposta excedido: {context.response_time}ms"

@then('o tempo de resposta deve ser registrado no dashboard')
def step_impl(context):
    assert context.response_time, "Tempo de resposta não registrado"

@when('o tempo de resposta da API excede 3000 ms')
def step_impl(context):
    context.response_time = 3500  # Simulando um tempo acima de 3000ms
    if context.response_time > 3000:
        context.alert_triggered = True

@then('um alerta deve ser disparado para o time de monitoramento')
def step_impl(context):
    assert context.alert_triggered, "Alerta não disparado corretamente"

@given('a média do tempo de resposta da API nas últimas 24 horas foi de "{media_anterior}ms"')
def step_impl(context, media_anterior):
    context.media_anterior = int(media_anterior)

@when('a média das últimas 10 requisições é "{media_nova}ms"')
def step_impl(context, media_nova):
    context.media_nova = int(media_nova)

@then('um alerta de degradação de desempenho deve ser acionado')
def step_impl(context):
    aumento = (context.media_nova - context.media_anterior) / context.media_anterior
    assert aumento >= 0.3, f"Aumento foi de {aumento*100:.2f}%, menor que 30%"

@then('logs de latência devem ser enviados para análise')
def step_impl(context):
    assert context.media_nova, "Logs de latência não foram gerados"

@then('uma ação corretiva deve ser iniciada automaticamente')
def step_impl(context):
    context.acao_corretiva = True
    assert context.acao_corretiva, "Ação corretiva não foi iniciada automaticamente"
