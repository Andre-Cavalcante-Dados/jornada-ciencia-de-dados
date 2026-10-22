# Registro de aprendizagem

Data: 2026-10-22

Fase: 01. Pensamento analítico e fundamentos

Assunto estudado:

# 1. O que estudei?
Hoje eu reaprendi a pensar como um cientista de dados antes de sair escrevendo código. Utilizei o chat gpt como guia e me ajudou na condução de alguns exercicios.


# 2. O que aprendi?
Aprendi que devo realizar mais perguntas no sentido de ter mais hipóteses. Essas peguntas devem ser acompanhadas por análises e tempo de entendimento.


# 3. Como apliquei?
O problema é algo simples, mas é possível obter vários insights

_______________________________________________________________________________________________________________________________
Problema: 
Empresa X que tem o seguinte os seguintes dados:

Indicador|        Mês anterior|      Mês atual|

Faturamento|        R$ 100.000|      R$ 85.000|

Pedidos realizados|        200|            170|

Vendedores|                 10|             10|
_______________________________________________________________________________________________________________________________
Pergunta 1) Qual é o fato comprovado pelos dados apresentados?	
A) Os vendedores estão trabalhando menos.

B) O faturamento e o número de pedidos diminuíram 15%.

C) Os clientes estão insatisfeitos.

D) A empresa precisa contratar mais vendedores

Respondi a opção B (acertei)

Comentários da IA: 
"Um detalhe importante: a quantidade de vendedores permaneceu constante, mas isso não comprova que a composição da equipe foi a mesma. Você percebeu essa distinção na questão 4, e ela é relevante.
Conceito aprendido: observar uma mudança não significa conhecer sua causa."

_______________________________________________________________________________________________________________________________
Pergunta 2) Escreva uma pergunta que ajudaria a investigar a causa da queda nas vendas.
Resposta:
Houve mudança na política de preço? (fui objetivo e literal na resposta)

Comentários da IA:
"Você identificou uma variável que pode afetar o comportamento comercial: preço.
Entretanto, existe uma diferença entre perguntar se a política mudou e investigar se essa mudança explica a queda.
Uma política de preços pode ter mudado sem afetar negativamente as vendas. Também é possível que os preços tenham permanecido iguais, mas os descontos tenham diminuído, alterando a conversão comercial.

Eu refinaria sua pergunta para:
A variação dos preços praticados e dos descontos concedidos contribuiu para a redução da quantidade de pedidos e do faturamento?

Essa formulação é melhor porque conecta a hipótese ao fenômeno que queremos explicar.

Para investigá-la, eu buscaria:
- Preço médio praticado por produto nos dois meses.
- Descontos concedidos.
- Quantidade de oportunidades comerciais.
- Taxa de conversão de oportunidades em pedidos.
- Quantidade vendida por produto.
A melhoria principal: uma pergunta analítica não deve apenas identificar algo que mudou. Ela deve ajudar a descobrir se essa mudança tem relação com o problema observado."

_______________________________________________________________________________________________________________________________
Pergunta 3) Cite duas hipóteses possíveis para explicar a queda no faturamento.
Resposta:
- Possível aumento na política de preços
- Redução na quantidade de produtos do portifólio (Duas hipóteses plausíveis.)

Comentários da IA:
" São hipóteses plausíveis.

Hipótese 1: aumento de preços
O que faz sentido: preços mais altos podem reduzir a demanda ou a conversão, dependendo do mercado e do comportamento dos clientes.

O que precisa melhorar: o aumento de preços, sozinho, não explica necessariamente uma queda no faturamento. Se os preços subirem e a quantidade vendida permanecer constante, o faturamento poderá aumentar.

Como testar: comparar preços e descontos por produto, quantidade vendida e taxa de conversão entre os períodos.

Hipótese 2: redução do portfólio
O que faz sentido: menos produtos disponíveis podem significar menos opções de compra, perda de vendas ou substituição por produtos de menor valor.

O que precisa melhorar: é necessário distinguir a quantidade de produtos cadastrados da quantidade de produtos efetivamente disponíveis para venda.

Como testar: comparar produtos ativos, produtos disponíveis em estoque, rupturas de estoque, vendas por SKU e participação de cada produto no faturamento.

Há um refinamento adicional que vale guardar: suas duas hipóteses são possíveis causas comerciais, mas outras categorias também precisam ser consideradas, como demanda, disponibilidade de produtos, carteira de clientes e produtividade da equipe.

Não precisamos listar todas as possibilidades do universo. Precisamos construir hipóteses relevantes, priorizá-las e testar as mais promissoras."

_______________________________________________________________________________________________________________________________
- Pergunta 4) Quais dados adicionais você buscaria para descobrir a causa da queda?
Resposta:
- Avaliaria se os 20 vendedores são os mesmos, pois poderia ter uma mudança no headcount e isso impactaria no treinamento de vendas (se tratando de um curto período de tempo)
- Analisar o histórico de vendas para identificar sazonalidade ou ciclo de vendas
- Se for um ramo de serviços, avaliaria se teve algum problema de reclamação da empresa que justificasse a queda. Se for um ramo de produtos acabados, avaliaria se houve algum problema de logística.
- O ticket médio é o mesmo do mês anterior, isso pode indicar que são produtos recorrentes, mas mesmo assim, avaliaria se os produtos são os mesmos

Comentários da IA:

"1. Mudança na equipe e treinamento
Você escreveu que avaliaria se os vendedores eram os mesmos, porque uma mudança no quadro poderia afetar o treinamento.

Avaliação: boa hipótese, com uma ressalva.

O total de vendedores ativos permaneceu em 10 no cenário apresentado. Entretanto, podem ter ocorrido substituições, afastamentos, mudanças de carteira ou diferenças no tempo de experiência.

Para testar sua hipótese, eu avaliaria:
- Admissões e desligamentos no período.
- Tempo de experiência dos vendedores.
- Vendas por vendedor, considerando a carteira atendida.
- Dias efetivamente trabalhados.
- Conversão comercial por vendedor.
Um cuidado: não atribua uma queda à equipe apenas porque houve substituições. É necessário verificar se elas realmente ajudam a explicar o resultado.
2. Histórico de vendas, sazonalidade e ciclos
Avaliação: excelente.

Você reconheceu que comparar somente dois meses pode levar a conclusões equivocadas.

Uma queda em relação ao mês anterior pode ser normal em determinados períodos. Por exemplo, alguns segmentos apresentam maior demanda em datas comemorativas, épocas de orçamento ou períodos específicos do ano.

Eu acrescentaria três comparações:
- Mês atual versus mês anterior.
- Mês atual versus o mesmo mês do ano anterior.
- Resultado observado versus meta ou previsão comercial.
Sempre que possível, utilizaria uma série histórica mais longa e consideraria diferenças no número de dias úteis.
3. Reclamações e problemas logísticos
Avaliação: muito boa visão de negócio.

Você percebeu que a causa pode estar fora do departamento comercial. Essa é uma distinção importante.

Um produto pode ter demanda, preço competitivo e vendedores preparados, mas não gerar pedidos ou faturamento porque está indisponível ou porque os clientes perderam confiança no fornecedor.

Para transformar essas ideias em testes, eu procuraria:
- Volume e gravidade das reclamações.
- Cancelamentos e devoluções.
- Pedidos atrasados ou não entregues.
- Rupturas de estoque.
- Prazo médio de entrega.
- Perdas de clientes e motivos registrados no CRM.
Sua distinção entre empresas de serviços e empresas de produtos acabados faz sentido como ponto de partida. Só não a trataria como uma divisão absoluta: empresas de serviços também enfrentam problemas de capacidade operacional, enquanto empresas de produtos podem sofrer com qualidade, atendimento e retenção de clientes.
4. Ticket médio e recorrência
Você observou que o ticket médio parece ser o mesmo e levantou a possibilidade de vendas recorrentes.

Aqui temos um ponto matemático importante.

Sua observação sobre o ticket médio está correta. Porém, a recorrência ainda não pode ser inferida desses dados.

Um ticket médio constante não significa necessariamente que os mesmos produtos foram vendidos, que os mesmos clientes compraram ou que houve recorrência. Composições diferentes de produtos podem gerar o mesmo valor médio.

Para investigar isso, eu verificaria:
- Quantidade de clientes compradores em cada período.
- Clientes que compraram nos dois meses.
- Produtos vendidos e respectivos volumes.
- Frequência de compra por cliente.
- Ticket médio por cliente e por produto.
Isso permite separar três fenômenos distintos: perda de clientes, redução da frequência de compra e mudanças na composição dos pedidos."
_______________________________________________________________________________________________________________________________

# 4. Onde tive dificuldade?

Acredito que as minhas respostas foram limitadas em alguns momentos. Entendi a importância de realizar as "hipóteses mais relevantes".
Tem uma frase que fez sentido na minha avaliação "explicar matematicamente como o indicador mudou não é o mesmo que descobrir a causa do problema."

# 5. Como melhorei meu raciocínio?

Analisando as respostas, pude ver que preciso pensar mais em outras possibilidas
O próximo passo é disciplinar esse raciocínio: definir indicadores, procurar evidências que possam contrariar suas próprias hipóteses e evitar conclusões precipitadas.

$ 6. Próximo passo

Acredito que preciso formular mais perguntas e definir métricas que permitam respondê-las.

Autoavaliação:
(sim)_Consigo explicar o conceito com minhas palavras.
(parcialmente)_Consigo resolver um exercício sem consultar a solução.
(sim)_Consigo aplicar o conceito em um problema diferente.
