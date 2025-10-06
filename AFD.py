# ========================================================
# 1. Representação do AFD em Python
# ========================================================

transicoes = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q2', 'b': 'q3'},
    'q2': {'a': 'q4', 'b': 'q5'},
    'q3': {'a': 'q6', 'b': 'q7'},
    'q4': {'a': 'q4', 'b': 'q5'},
    'q5': {'a': 'q6', 'b': 'q7'},
    'q6': {'a': 'q2', 'b': 'q3'},
    'q7': {'a': 'q1', 'b': 'q0'}
}

estado_inicial = 'q0'

estados_finais = {'q4', 'q5', 'q6', 'q7'}

# ========================================================
# 2. A Função de Transição Estendida Recursiva
# ========================================================

def funcao_transicao_estendida_recursiva(estado_atual, palavra):


    if not palavra:
        # Caso base: Se a palavra estiver vazia, retornamos o estado atual.
        return estado_atual
    else:
       
        x = palavra[:-1]
        a = palavra[-1]

        # Chamamos a função recursivamente para processar a parte inicial da palavra
        estado_intermediario = funcao_transicao_estendida_recursiva(estado_atual, x)

        return transicoes[estado_intermediario][a]
    
# ========================================================
# 3. Demonstração 
# ========================================================

def testar_palavra(palavra_a_testar):
    print(f"Testando a palavra: '{palavra_a_testar}'")

    # Chamamos nossa função recursiva para que ela faça todo o trabalho
    estado_final_calculado = funcao_transicao_estendida_recursiva(estado_inicial, palavra_a_testar)

    print(f"  -> O processamento terminou no estado: '{estado_final_calculado}'")


    if estado_final_calculado in estados_finais:
        print(f"  -> Resultado: ACEITA")
    else:
        print(f"  -> Resultado: REJEITA")
    print("-" * 30) 

# --- Chamando a função de teste com exemplos ---
testar_palavra("babaaab")
testar_palavra("aabba")