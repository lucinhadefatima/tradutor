import os
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="auto",target="pt")

if __name__== "__main__":
    while True:
        try:
            print("1 - traduzir texto")
            print("2 - sair do programa.")

            opcao = input("opcao desejada:")

            os.system("cls")

            match  opcao:
                case  "1":
                    texto_original = input("digite o texto a ser traduzido:")
                    texto_traduzido = tradutor.translate(texto_original)

                    print("\nTRADUCAO:\n")
                    print(f"{texto_traduzido}\n")
                    continue
                 
                case "2":
                    break
                case _:
                      print("opcao invalida.")
                      continue
            
        except Exception as e:
            print (f"nao foi possivel traduzir texto.{e}.")