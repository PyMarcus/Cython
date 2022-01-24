from cumprimenta import cumprimenta


def intro() -> None:
    nome: str = input('Qual seu nome? ')
    cumprimenta(nome)


if __name__ == '__main__':
    intro()
