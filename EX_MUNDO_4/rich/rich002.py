from rich import print
from rich.panel import Panel

caixa = Panel("[white]Esse aqui é um exemplo de painel[/]:+1:", title="Mensagem", style="red", width=38)

print(caixa)