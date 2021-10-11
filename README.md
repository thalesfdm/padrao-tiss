# padrao-tiss
Aplicação que busca e salva um determinado arquivo **.pdf** referente à versão mais recente do Padrão TISS, utilizando técnicas de *web scraping*.
Após baixar o arquivo, a aplicação processa as tabelas contidas nas páginas que foram especificadas, transformando as tabelas em arquivos **.csv**
estruturados e salvando os mesmos em um arquivo **.zip**.

## Requisitos
- [Git](https://git-scm.com)
- [Python 3](https://www.python.org/)
- [pip](https://pypi.org/project/pip/)

## Instruções
Recomenda-se utilizar um ambiente virtual, como o `virtualenv`, para mais informações acessar [este link](https://virtualenv.pypa.io/en/latest/).

Caso esteja utilizando o `virtualenv`:
```bash
# criar o ambiente virtual
virtualenv venv

# ativar o ambiente virtual no linux (para outros sistemas consultar a documentação)
source venv/bin/activate
```

Com o ambiente virtual ativado, instalar as dependências do projeto:
```
pip install -r requirements.txt
```

Para rodar a aplicação, deve-se passar as páginas que serão processadas:

> Quadro 30, página 108
> 
> Quadro 31, páginas 109 a 114
> 
> Quadro 32, página 114
```bash
# exemplo:
# "108" e "114" para processar quadros individuais nas páginas 108 e 114
# "109-114" para processar um quadro que inicia na página 109 e termina na página 114
python3 run.py 108 109-114 114
```
