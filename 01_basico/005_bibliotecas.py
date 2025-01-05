"""
Bibliotecas 

Bibliotecas são um conjunto de funções, classes e modulos que estão prontos para uso e que ajudam a resolver problemas ou implementar funcionalidades no desenvolvimento do codigo sem precisar desenvolver a roda novamente.

Temos dois tipos de bibliotecas:

Bibliotecas built-in (nativas) ja fazem parte do python e não precisam ser instaladas basta importalas com "import"
Exemplos:
math: Fornece funções matemáticas (ex.: sqrt, sin, cos).
random: Gera números aleatórios (ex.: randint, choice).
datetime: Trabalha com datas e horários.
os: Manipula o sistema operacional (ex.: caminhos de arquivos, ambiente).
json: Trabalha com dados no formato JSON.
"""
import math # Importamos a biblioteca math

print(math.sqrt(16)) # usamos uma função da biblioteca para descobrirmos a raiz quadrada de 16

"""
Bibliotecas externas são criadas por terceiros seja empresas ou comunidade e precisam ser instaladas com gerenciador de pacotes como o pip que ja vem quando voce instala o python.
É interessante sempre independente se for Externa ou Built-in voce pesquisar a documentação da biblioteca, isso vai melhorar seu conhecimento e seu desenvolvimento de codigo.

Exemplos:
numpy: Para cálculos numéricos e álgebra linear.
pandas: Para manipulação e análise de dados.
requests: Para trabalhar com requisições HTTP.
flask: Para desenvolvimento web.
tensorflow: Para machine learning e IA.

Vamos usar a biblioteca requests como exemplo, então primeiro olhe a documentação dela e depois execute o comando abaixo no terminal do projeto ou do python geral.

pip install requests
"""

import requests
resposta = requests.get("https://api.github.com")
print(resposta.status_code) #Aqui usamos um dos atributos da biblioteca para sabermos o codigo de status da requisição
