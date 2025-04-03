# Auralyx - Web Player

A **Auralyx** é uma aplicação web simples que permite pesquisar e reproduzir áudio do YouTube diretamente no navegador. Utilizando Flask para o backend, SQLAlchemy para o gerenciamento de banco de dados e yt_dlp para extração de áudio, o projeto oferece uma interface intuitiva com funcionalidades modernas, como barra de progresso e controles de áudio.

## Funcionalidades

- **Pesquisa de Áudio no YouTube:** Utiliza yt_dlp para buscar os 10 melhores resultados de áudio a partir de uma consulta do usuário.
- **Reprodução de Áudio:** Ao selecionar um resultado da pesquisa, o áudio é carregado e reproduzido com controles de progresso.
- **Banco de Dados com SQLAlchemy:** Inclui um modelo de usuário simples para armazenar informações como nome de usuário e e-mail.
- **Interface Responsiva:** Design moderno e adaptável para diferentes dispositivos com foco na experiência do usuário.

## Tecnologias Utilizadas

- **Python 3**
- **Flask** – Micro framework web
- **Flask_SQLAlchemy** – ORM para gerenciamento de banco de dados SQLite
- **yt_dlp** – Extração e processamento de áudio do YouTube
- **HTML5, CSS3 e JavaScript** – Para a interface e interatividade

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/auralyx.git
   cd auralyx
   ```

2. **Crie um Ambiente Virtual e Ative-o:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows utilize: venv\Scripts\activate
   ```

3. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```

   > Certifique-se de que o arquivo `requirements.txt` contenha as seguintes bibliotecas (ou instale manualmente):
   > - Flask
   > - Flask_SQLAlchemy
   > - yt_dlp

4. **Configuração do Banco de Dados:**

   O projeto utiliza SQLite por padrão. Ao executar a aplicação, o banco de dados `auralyx.db` será criado automaticamente se ainda não existir.

## Uso

1. **Inicie a Aplicação:**

   ```bash
   python app.py
   ```

2. **Acesse a Aplicação:**

   Abra o navegador e acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. **Pesquisa e Reprodução:**

   - Utilize a barra de pesquisa para procurar áudios.
   - Clique em um dos resultados para iniciar a reprodução.
   - Controle a reprodução e visualize o progresso com a barra interativa.

## Estrutura do Projeto

- **app.py:** Arquivo principal que contém as rotas, configuração do Flask e funções de pesquisa/reprodução de áudio.
- **templates/index.html:** Arquivo de template HTML que define a interface do usuário.
- **static/** (opcional): Pasta para armazenar arquivos estáticos, como CSS ou JavaScript adicionais.
- **auralyx.db:** Banco de dados SQLite criado automaticamente para armazenamento de informações dos usuários.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, por favor, abra uma issue ou envie um pull request.

## Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Desenvolvido por [Yuki](https://t.me/yukiiiasahina)
Sinta-se à vontade para entrar em contato ou deixar seu feedback.
