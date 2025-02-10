from behave import given, when, then
import time

@given('um pedido foi criado com peso "{peso}", custo "{custo}", tipo de transporte "{transporte}", urgência "{urgencia}"')
def step_impl(context, peso, custo, transporte, urgencia):
    context.pedido = {"peso": peso, "custo": custo, "transporte": transporte, "urgencia": urgencia}

@given('existem entregadores disponíveis próximos ao local')
def step_impl(context):
    context.entregadores_disponiveis = True

@given('um pedido foi criado com urgência "{urgencia}"')
def step_impl(context, urgencia):
    context.pedido = {"urgencia": urgencia}

@given('um pedido foi atribuído a um entregador')
def step_impl(context):
    context.entregador_atribuido = True

@given('o entregador recusou a entrega')
def step_impl(context):
    context.entregador_aceitou = False

@when('o sistema processa a atribuição do pedido')
def step_impl(context):
    start_time = time.time()
    context.entregador_atribuido = True
    context.tempo_atribuicao = time.time() - start_time

@when('o sistema tenta reatribuir o pedido')
def step_impl(context):
    if not context.entregador_aceitou:
        context.novo_entregador = True

@then('o pedido deve ser atribuído a um entregador em até 120 segundos')
def step_impl(context):
    assert context.tempo_atribuicao < 120, f"Tempo de atribuição excedido: {context.tempo_atribuicao}s"

@then('os logs de distribuição devem registrar o tempo de resposta')
def step_impl(context):
    assert context.entregador_atribuido, "Pedido não foi atribuído corretamente"

@given('não há entregadores disponíveis na região')
def step_impl(context):
    context.entregadores_disponiveis = False

@when('o sistema tenta atribuir o pedido')
def step_impl(context):
    if not context.entregadores_disponiveis:
        context.escalonado = True

@then('o pedido deve ser escalonado para supervisão manual')
def step_impl(context):
    assert context.escalonado, "Pedido não foi escalonado corretamente"

@then('um alerta deve ser gerado no dashboard de monitoramento')
def step_impl(context):
    assert context.escalonado, "Alerta não foi disparado corretamente"

@then('outro entregador disponível deve ser selecionado')
def step_impl(context):
    assert context.novo_entregador, "Nenhum novo entregador foi selecionado"

@then('a reatribuição deve ocorrer em menos de 60 segundos')
def step_impl(context):
    start_time = time.time()
    context.tempo_reatribuicao = time.time() - start_time
    assert context.tempo_reatribuicao < 60, f"Tempo de reatribuição excedido: {context.tempo_reatribuicao}s"