# 🧠🎲 Projeto - CashClash

Este projeto é um jogo interativo desenvolvido para auxiliar crianças e adolescentes a aprenderem conceitos de matemática financeira de forma divertida e progressiva.

## 📚 Objetivo

O jogador percorre um tabuleiro com 10 casas, respondendo a desafios matemáticos a cada passo. Com apenas 3 vidas disponíveis, ele deve usar o raciocínio lógico e conhecimento financeiro para chegar ao final e conquistar seu emblema de vitória!

## ✨ Funcionalidades

- 🎯 **Desafios Progressivos:** As perguntas aumentam de dificuldade conforme o jogador avança.  
- 💡 **Feedback Educacional:** Cada resposta correta vem acompanhada de uma explicação simples do conceito.  
- 🏅 **Sistema de Pontuação e Recompensas:** Avance, acerte e ganhe um emblema no final!  
- 🔁 **Reinício Inteligente:** Perdeu todas as vidas? O jogo recomeça automaticamente.  
- 📱 **Interface Intuitiva e Colorida:** Feita especialmente para o público jovem.

## 🔧 Tecnologias utilizadas

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Node.js ou Django  
- **Banco de Dados:** PostgreSQL ou Firebase

## 💡 Como rodar o projeto
1.  **Clone este repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/seu-repositorio.git](https://github.com/SEU-USUARIO/seu-repositorio.git)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd nome-do-projeto
    ```
    (Substitua `nome-do-projeto` pelo nome real da pasta raiz do seu projeto Django, por exemplo, `CashClash`)

3.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    # Para Windows:
    .\venv\Scripts\activate
    # Para macOS/Linux:
    source venv/bin/activate
    ```

4.  **Instale as dependências:**
    (Assumindo que você tem um `requirements.txt` com `Django` e outras bibliotecas necessárias. Se não tiver, use `pip install Django` primeiro e depois `pip freeze > requirements.txt`)
    ```bash
    pip install -r requirements.txt
    ```

5.  **Aplique as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  **Acesse o projeto no navegador:**
    Abra seu navegador e vá para: [http://127.0.0.1:8000/](http://127.00.0.1:8000/)

## 🌐 Visão de Arquitetura

- **Visão de Desenvolvimento:** Código organizado em pacotes como `jogo`, `usuario`, `perguntas`, `feedback`.  
- **Visão Física:** Aplicação web acessada por navegador, com servidor responsável pela lógica e banco de dados para armazenar perguntas e pontuações.

## 👩‍💻 Equipe

<div align="center">

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Larissa-Kailane">
        <img src="https://avatars.githubusercontent.com/Larissa-Kailane" width="100px;" alt="Larissa Kailane"/><br />
        <sub><b>Larissa Kailane</b></sub>
    </td>
    <td align="center">
      <a href="https://github.com/lucianaliebl">
        <img src="https://avatars.githubusercontent.com/lucianaliebl" width="100px;" alt="Luciana Liebl"/><br />
        <sub><b>Luciana Liebl</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Mariacmv">
        <img src="https://avatars.githubusercontent.com/Mariacmv" width="100px;" alt="Maria Clara Guerreira"/><br />
        <sub><b>Maria Clara</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/RafaPrattes">
        <img src="https://avatars.githubusercontent.com/RafaPrattes" width="100px;" alt="Rafaela Prates"/><br />
        <sub><b>Rafaela Prates</b></sub>
      </a>
    </td>
  </tr>
</table>

</div>


