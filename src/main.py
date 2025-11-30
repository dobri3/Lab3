import typer
from src.router import router


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    while (f := input("Choose function (type 'quit', 'q', 'exit' or 'e' to stop): ")) not in ["quit", "q", "exit", "e"]:
        router(f)

if __name__ == "__main__":
    typer.run(main)
