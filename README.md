# Real-Time System Simulator

Este projeto é uma simulação de um sistema de tempo real, desenvolvido em Python, que resolve exercícios baseados em tarefas concorrentes e programação paralela. Ele abrange a implementação de tarefas simples, produtores e um sistema embarcado para um computador de bicicleta, integrando conceitos de concorrência e sincronização.

---

## Estrutura do Projeto

```plaintext
real_time_system/
├── core/                           # Código principal
│   ├── __init__.py
│   ├── hello_task.py               # Implementação da Tarefa Hello_Task
│   ├── producer.py                 # Implementação da Tarefa Producer
│   ├── bike_computer.py            # Simulação do computador de bicicleta
│   ├── utils.py                    # Funções auxiliares
│
├── config/                         # Configurações globais
│   ├── __init__.py
│   └── config.py                   # Parâmetros gerais e constantes
│
├── tests/                          # Testes unitários e integração
│   ├── __init__.py
│   ├── test_hello_task.py
│   ├── test_producer.py
│   ├── test_bike_computer.py
│   └── test_utils.py
│
├── main.py                         # Arquivo principal para iniciar o sistema
├── requirements.txt                # Dependências do projeto
├── README.md                       # Documentação
└── .gitignore                      # Arquivos a serem ignorados
```

---

## Funcionalidades

### 1. **Tarefa Hello_Task**
- Imprime mensagens customizadas no console.
- Permite configurar a quantidade de mensagens e um tempo de retardo entre elas.
- Exemplo:
  ```plaintext
  Hello, I am Task A
  Hello, I am Task A
  ```

### 2. **Tarefa Producer**
- Imprime caracteres no console com configurações flexíveis:
  - Caracter a ser impresso.
  - Número de repetições.
  - Retardo entre cada impressão.
- Permite controle externo para terminar a tarefa.
- Exemplo:
  ```plaintext
  AAAAAA
  ```

### 3. **Sistema Embarcado de Bicicleta**
- Simula um computador de bicicleta com os seguintes modos:
  - **Viagem**: Mostra a quilometragem da viagem atual.
  - **Velocidade**: Mostra a velocidade atual.
  - **Total**: Mostra a quilometragem total de todas as viagens.
  - **Tempo**: Mostra a duração total da viagem.
- Alterna entre modos ao pressionar "botões" simulados.

---

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone git@github.com:raulbatalha/ativiade_4_ufam.git
   cd ativiade_4_ufam
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/Mac
   venv\Scripts\activate          # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Como Executar

1. **Executar o Sistema Principal**:
   ```bash
   python main.py
   ```

2. **Executar os Testes**:
   ```bash
   python -m unittest discover -s tests
   ```

3. **Executar somente os testes isolados com Pytest**:
 - Deve ser instalado o `Pytest` caso não tenha na sua máquina:
 ```bash
 sudo apt install python3-pytest
  ```
  - Depois do `Pytest` instalado na sua máqui é hora de executar os teste do projeto: 
   ```bash
   pytest tests/
   ```
---

## Exemplos de Saída

### Tarefa Hello_Task
```plaintext
Hello, I am Task A
Hello, I am Task A
Hello, I am Task A
```

### Tarefa Producer
```plaintext
BBBBB
```

### Sistema de Bicicleta
```plaintext
Trip Distance: 5.00 km
Speed: 28.30 km/h
Total Distance: 12.00 km
Time: 120 s
```

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Threading**: Para gerenciar tarefas concorrentes.
- **Unittest**: Para testes unitários.

---

## Próximos Passos

- Adicionar suporte a persistência de dados para a quilometragem total.
- Criar uma interface gráfica para o computador de bicicleta.
- Melhorar os testes unitários com mais casos de borda.

---

## Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o repositório.
2. Crie uma branch com sua funcionalidade ou correção.
   ```bash
   git checkout -b minha-nova-funcionalidade
   ```
3. Faça o commit das alterações.
   ```bash
   git commit -m "Minha nova funcionalidade"
   ```
4. Envie para o repositório remoto.
   ```bash
   git push origin minha-nova-funcionalidade
   ```
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

## Contato

Para dúvidas ou sugestões, entre em contato:
- **E-mail**: raulbatalh@gmail.com
- **GitHub**: [Raul Batalh](https://github.com/raulbatalha)
