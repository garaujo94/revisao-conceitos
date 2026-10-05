import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Revisão de Estatística
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. Probabilidade
    2. Distribuições
    3. Estimadores
    4. Intervalos de Confiança
    5. Testes de Hipótese
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Probabilidade Básica

    - **Experimento aleatório:** Experimentos que não somos capazes de assegurar ou controlar o valor de certas variáveis, o que faz o resultado variar entre um experimento e outo, embora a maioria das condições sejam as mesmas
    - **Espaço amostral:** Um **conjunto S** de todos os resultados possíveis de um **experimento aleatório**, onde cada resultado é chamado de ponto amostral. Pode haver mais de um espaço amostral que descreve os resultados de um experimento
    - **Evento:** É um **subconjunto A** de um **espaço amostral S**

    ## Conceito
    Em qualquer **experimento aleatório** existe sempre uma incerteza se um **evento** em particular irá ocorrer ou não. Como medida de chance ou *probabilidade* é conveniente designar um número entre 0 e 1, sendo 1 certeza que irá acontecer e 0 o contrário.
    1. Abordagem Clássica: Se um **evento** ocorre de *h* hormas diferentes em um total de *n* formas possíveis, todas sendo igualmente prováveis, então a probabilidade do **evento** é *h/n*
    2. Abordagem Frequencial: se após *n* repetições de um **experimento**, onde *n* é muito grande, um evento ocorre *h* vezes, então a probabilidade do **evento** é *h/n*

    ## Axiomas
    Num **espaço amostral S**, para da **evento A**, temos *P* como função de probabilidade e *P(A)* como probabilidade do evento A
    1. Para cada evento A: <BR>P(A) >= 0
    2. Para o evento certo ou garantido S: <BR>P(S) = 1
    3. Para qualquer número de eventos mutuamente exclusivos A<sub>1</sub>, A<sub>2</sub>,... então:<BR>
        P($A_{1} \cup A_{2} \cup A_{3} \cup ...$) = P($A_{1}$) + P($A_{2}$) + P($A_{3}$) + ...

    ##
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Probabilidade Condicional
    "Probabilidade do evento B, dado que o evento A aconteceu"<br>
    $P(B|A) = \frac{P(A \cap B)}{P(A)} \to P(A \cap B)=P(B|A)P(A)$

    ## Eventos Independentes
    Eventos onde um não interfere no outro <br>
    $P(A \cap B) = P(A)P(B)$

    ## Teorema de Bayes
    Onde $A_{1}, A_{2}, A_{3}..., A_{n}$ eventos mutuamente exclusivos, cuja união é o espaço amostral S, isto é, um dos eventos deve acontecer. Então, se A é um evento, temos o seguinte:<br><br>
    $P(A_{k}|A) = \frac{P(A_{k})P(A|A_{k})}{\sum_{j=1}^{n}P(A_{j})P(A|A_{j})}$<br><br>
    Exemplo: "Dado que um e-mail pode ser spam ou não spam (eventos $A_{1}, A_{2}$), qual a probabilidade de um evento ser um spam ($A_{1}$) dado que ele contém a palavra 'dinheiro' (evento $A$)."
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Permutações
    "Eu tenho N elementos e quero combinar eles em um grupo de tamanho R"<br>
    "Suponha que temos N elementos distintos e gostaríamos de dispor R destes objetos numa linha"<br>
    Quantas disposições diferentes eu poderia ter? Sabendo que a ordem importa, ou seja, $(A, B)$ é diferente de $(B, A)$<br>

    $\frac{N!}{(N-R)!}$

    ## Combinações
    Eu quero fazer uma permutação, contudo a ordem dos elementos não importa de forma que $(A, B)$ é igual de $(B, A)$<br>

    $\binom{N}{R} = \frac{N!}{R!(N-R)!}$
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
