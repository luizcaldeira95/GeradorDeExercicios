def EntradaDeDados():
    ajuda = {
        "P": "Projeto - Define o nome do projeto gerado e seu propósito geral.",
        "F": "Ferramenta/Framework - Especifique uma ferramenta útil ou um framework relevante para o projeto.",
        "M": "Matéria - Adicione uma disciplina ou conceito relacionado ao estudo, como Estrutura de Dados ou Segurança da Informação.",
        "C": "Cor - Escolha uma cor predominante para o projeto, útil para design e identidade visual.",
        "T": "Tema - Defina o tema geral do projeto, como Esportes, Música, Tecnologia, ou Ficção Científica.",
        "E": "Estilo - Determine o estilo do projeto, como Minimalista, Retrô, Futurista ou Cartoon.",
        "A": "Aplicação - Informe o tipo de aplicação que será gerada, como Site, App Mobile, API ou Automação.",
        "G": "Gênero - Escolha um gênero, como Jogo, Sistema de Gestão, Chatbot ou E-commerce.",
        "L": "Linguagem de Programação - Especifique a linguagem principal do projeto, como Python, JavaScript ou C#.",
        "I": "Inspiração/Referência - Adicione uma referência ou projeto similar para se basear.",
        "U": "Usuário-alvo - Defina para quem o projeto será feito, como estudantes, empresas ou desenvolvedores iniciantes."
    }

    opcao = input(
        """O que você deseja adicionar?  

        [P] Projeto   
        [M] Matéria  
        [C] Cor  
        [T] Tema  
        [E] Estilo  
        [A] Aplicação  
        [G] Gênero  
        [L] Linguagem de Programação  
        [F] Framework/Biblioteca  
        [I] Inspiração/Referência  
        [U] Usuário-alvo  

        [Ajuda] Mostrar informações detalhadas sobre cada item.

        Escolha uma opção: """
    ).strip().upper()  # Remove espaços extras e transforma em maiúsculas

    if opcao == "AJUDA":
        print("\nLista de opções disponíveis:\n")
        for chave, descricao in ajuda.items():
            print(f"[{chave}] {descricao}")
    elif opcao in ajuda:
        print(f"\nOpção escolhida: {ajuda[opcao]}")
    else:
        print("\nOpção inválida. Use um dos códigos da lista.")

EntradaDeDados()
