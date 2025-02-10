Feature: Tempo de Resposta da Plataforma

  Como sistema da plataforma Rappi
  Quero garantir tempos de resposta adequados
  Para que os entregadores tenham uma experiência fluida e sem atrasos.

  Scenario: Responder chamadas de API dentro do SLA
    Given uma requisição foi feita para a API de atribuição de pedidos
    When a API processa a requisição
    Then a resposta deve ser enviada em menos de 3000 ms
    And o tempo de resposta deve ser registrado no dashboard

  Scenario: Tempo de resposta superior ao limite estabelecido
    Given uma requisição foi feita para a API de atribuição de pedidos
    When o tempo de resposta da API excede 3000 ms
    Then um alerta deve ser disparado para o time de monitoramento
    And uma ação corretiva deve ser iniciada automaticamente

  Scenario: Aumento de 30% no tempo médio de resposta
    Given a média do tempo de resposta da API nas últimas 24 horas foi de "2800ms"
    When a média das últimas 10 requisições é "3640ms"
    Then um alerta de degradação de desempenho deve ser acionado
    And logs de latência devem ser enviados para análise
