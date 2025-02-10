Feature: Eficiência na Distribuição de Pedidos

  Como sistema de distribuição do Rappi
  Quero atribuir pedidos aos entregadores de forma otimizada
  Para garantir eficiência e cumprir o SLA estabelecido.

  Scenario: Atribuir pedido a um entregador disponível em menos de 2 minutos
    Given um pedido foi criado com peso "2kg", custo "10.00", tipo de transporte "moto", urgência "alta"
    And existem entregadores disponíveis próximos ao local
    When o sistema processa a atribuição do pedido
    Then o pedido deve ser atribuído a um entregador em até 120 segundos
    And os logs de distribuição devem registrar o tempo de resposta

  Scenario: Nenhum entregador disponível no momento da atribuição
    Given um pedido foi criado com urgência "alta"
    And não há entregadores disponíveis na região
    When o sistema tenta atribuir o pedido
    Then o pedido deve ser escalonado para supervisão manual
    And um alerta deve ser gerado no dashboard de monitoramento

  Scenario: Reatribuição de pedido recusado por entregador
    Given um pedido foi atribuído a um entregador
    And o entregador recusou a entrega
    When o sistema tenta reatribuir o pedido
    Then outro entregador disponível deve ser selecionado
    And a reatribuição deve ocorrer em menos de 60 segundos
