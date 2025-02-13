from EntradaDeDados import EntradaDeDados

def BoasVindas():

    print("""
    ░██████╗░███████╗██████╗░░█████╗░██████╗░░█████╗░██████╗░  ██████╗░███████╗
    ██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
    ██║░░██╗░█████╗░░██████╔╝███████║██║░░██║██║░░██║██████╔╝  ██║░░██║█████╗░░
    ██║░░╚██╗██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔══██╗  ██║░░██║██╔══╝░░
    ╚██████╔╝███████╗██║░░██║██║░░██║██████╔╝╚█████╔╝██║░░██║  ██████╔╝███████╗
    ░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

    ██████╗░██████╗░░█████╗░░░░░░██╗███████╗████████╗░█████╗░░██████╗
    ██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝
    ██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░░░░██║░░░██║░░██║╚█████╗░
    ██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░░░░██║░░░██║░░██║░╚═══██╗
    ██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗░░░██║░░░╚█████╔╝██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░░░╚═╝░░░░╚════╝░╚═════╝░""")

    print("""



    """)

    print("""            Bem-vindo ao Gerador de Projetos!

    Está sem ideias para o seu próximo projeto de estudo? 
    Este programa te ajuda a criar sugestões personalizadas com 
    base nas tecnologias e características que você escolher!
    Basta inserir algumas informações, como linguagem de programação, 
    temas, cores e outros detalhes, e clicar no botão "Gerar". 
    Em instantes, você receberá um nome de projeto único para usar como inspiração!
    Explore novas possibilidades e desafie suas habilidades com ideias criativas.         

    """)


def Gerador():
    from EntradaDeDados import EntradaDeDados

    escolha = input("""Vamos começar? 
[1] Gerar Projeto
[2] Adicionar itens 🚀
 """)

    if escolha == "1":
        print("Gerar")
    elif escolha == "2":
        EntradaDeDados()
    else:
        print("Opção inválida. Tente novamente.")
        Gerador()


def editar():
    print("Editar")

BoasVindas()
Gerador()
