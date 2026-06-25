# Análise — as 3 responsabilidades da classe `Academia` (v1.0)

**Sua tarefa (Parte 2 da atividade, 0,3):** responder com **suas palavras**
(2–4 frases por item), olhando o arquivo `academia.py` da pasta da aula.
Substitua cada `...` pela sua resposta.

---

## 1. Quais são as 3 responsabilidades grudadas na classe `Academia`?
Escreva no formato "a classe faz **X** e **Y** e **Z**":

> A partir da observação e análise da classe Academia, podemos afirmar 
que ela faz três coisas ao mesmo tempo: ela cuida das regras da academia, 
como calcular o valor do plano e registrar check-ins; também conversa com
o usuário pela tela usando input e print; e ainda envia notificações 
simuladas pelo WhatsApp.

## 2. Aponte, no código, **uma linha** de cada responsabilidade
(diga o número da linha e cole o trecho)

Quanto à responsabilidade de regra de negócio, ela aparece, 
por exemplo, na linha 22 (valor = 100.0), onde o sistema define 
o valor da mensalidade de acordo com o plano escolhido. Já quanto 
à responsabilidade de interface com o usuário, ela aparece 
na linha 16 (nome = input("Nome do aluno: ")), que lê informações 
digitadas pelo usuário. E a responsabilidade de notificação aparece 
na linha 36 (print(f"[WhatsApp para {nome}] ...")), que simula 
o envio de uma mensagem para o aluno.

## 3. Como o SRP separa essas responsabilidades?
Diga **em qual componente** cada responsabilidade passa a morar:

> A responsabilidade de enviar notificações ao aluno passa a morar 
no componente Notificador, no arquivo notificador.py. Assim, a classe 
Academia deixa de cuidar do aviso de boas-vindas e da confirmação 
de check-in, ficando focada apenas nas regras e operações da academia.

## 4. Por que ficou melhor? Cite **um** RNF
(manutenibilidade, testabilidade **ou** extensibilidade — veja `docs/requisitos.md`)
e explique em 1–2 frases:

> O RNF que mais melhora é a manutenibilidade. Com cada responsabilidade 
separada em sua própria classe, fica mais fácil alterar uma parte do sistema 
sem correr o risco de quebrar as outras. Além disso, o código fica mais 
organizado e mais fácil de entender. Além disso, o sistema fica mais fácil 
de manter, porque qualquer mudança nas mensagens ou no canal de envio pode 
ser feita em um único lugar, sem alterar a lógica de matrícula, listagem 
ou check-in da classe Academia. Um outro ponto de melhora é quanto à testabilidade, 
com a notificação separada em um componente próprio, fica mais fácil testar a 
classe Academia sem depender das mensagens enviadas ao aluno. Também fica mais 
simples testar o Notificador isoladamente, verificando se ele envia a mensagem 
correta em cada situação.