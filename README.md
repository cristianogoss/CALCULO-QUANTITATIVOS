# Cálculo de Quantitativos

## Site da aplicação web: 
https://calculoquantitativos-yagy7xcdd3p3nyunow6pkn.streamlit.app/

## Descrição

Esta aplicação web, desenvolvida com Streamlit, permite calcular quantitativos de materiais e serviços necessários para a execução de uma obra. 
Utilizando dados fornecidos pelos projetos arquitetônicos e de engenharia, o sistema calcula as quantidades de cada item, como concreto e tijolos.

## Estrutura do Projeto

- **/src**: Contém o código-fonte da aplicação.
  - **/components**: Componentes reutilizáveis da interface.
  - **/pages**: Páginas individuais da aplicação.
  - **/utils**: Funções utilitárias e helpers.
- **/data**: Contém os arquivos de entrada com os dados dos projetos.
- **/docs**: Contém a documentação do projeto.
- **/tests**: Contém os testes unitários e de integração.
- **/output**: Diretório onde os resultados são armazenados.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/calculo-quantitativos.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd calculo-quantitativos
    ```
3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```
4. Ative o ambiente virtual:
    - No Windows:
        ```bash
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Coloque os arquivos de entrada no diretório `/data`.
2. Execute a aplicação:
    ```bash
    streamlit run app.py
    ```
3. Acesse a aplicação no navegador através do endereço fornecido pelo Streamlit.

## Funcionalidades

- **Cálculo de Materiais**: Calcula a quantidade de materiais necessários com base nos dados fornecidos.
- **Interface Intuitiva**: Interface amigável e fácil de usar desenvolvida com Streamlit.

## Estrutura do Código

- **Home.py**: Arquivo principal que inicia a aplicação Streamlit.
- **/src/components**: Contém componentes reutilizáveis como botões, tabelas e gráficos.
- **/src/pages**: Contém as diferentes páginas da aplicação, como a página de upload de dados e a página de resultados.
- **/src/utils**: Funções auxiliares para manipulação de dados e cálculos.
- **/tests**: Contém testes para garantir a qualidade e funcionamento correto da aplicação.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma nova branch:
    ```bash
    git checkout -b minha-nova-feature
    ```
3. Faça suas alterações e commit:
    ```bash
    git commit -m 'Adiciona nova feature'
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin minha-nova-feature
    ```
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.





