# Fluxo da conversa com o Bot

Inicialmente será pensado um fluxo sem o LLM, para que posteriormente seja implementado o LLM e pontencialize a comunicação do Bot com o usuário.

Usuário envia qualquer mensagem (ex: “oi”)
📍 Bot responde:
    "Olá! Bem-vindo ao atendimento psicológico automatizado.
    Sou o assistente virtual da clínica.
    Você deseja: 
    1️⃣ Agendar uma consulta
    2️⃣ Iniciar sua anamnese"


```
Entrada → [MENU PRINCIPAL]
           ├── Novo Agendamento
           │    ├── Agendar Consulta
           │    │     ├── Perguntar dados
           │    │     │   ├── Nome completo
           │    │     │   ├── CPF
           │    │     │   ├── Endereço
           │    │     │   └── Telefone (Com DDD)
           │    │     ├── Perguntar dia
           │    │     ├── Perguntar horário
           │    │     ├── Confirmar agendamento
           │    │     └── Perguntar de deseja voltar ao menu inicial
           ├── Alterar Agendamento
           │    ├── Perguntar Nome Completo
           │    ├── Perguntar CPF
           │    ├── Perguntar motivo da alteração
           │    ├── Perguntar novo dia
           │    ├── Perguntar novo horário
           │    ├── Verificar se está disponível
           │    │     ├── Se sim: Confirmar agendamento e perguntar se deseja voltar ao menu incial
           │    └──   └── Se não: Explicar motivo e retornar a etapa de perguntar um novo dia ou horário
           ├── Cancelar Agendamento
           │    ├── Perguntar Nome Completo
           │    ├── Perguntar CPF
           │    ├── Perguntar motivo do cancelamento
           │    ├── Confirmar cancelamento
           │    │     ├── Se sim: Excluir agendamento
           │    └──   └── Se não: Confirmar que o agedamento se mantém e perguntar se deseja voltar ao menu principal
           └── Iniciar Anamnese
                ├── Confirmar se já tem consulta agendada
                │   ├── Caso sim: Vai para as perguntas
                │   ├── Caso não: Pede que primeiro agende uma consulta e que ela seja confirmada
                ├── Pergunta 1
                ├── Pergunta 2
                ├── ...
                ├── Confirmar envio
                └── Perguntar de deseja voltar ao menu inicial
                 
```

