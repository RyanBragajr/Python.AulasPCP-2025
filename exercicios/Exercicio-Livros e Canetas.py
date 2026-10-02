quantidade_livros = int(input("Quantos livros você comprou:"))
quantidade_canetas = int(input("Quantas canetas você comprou:"))

preco_livro = 25
preco_caneta = 5

total_livros = preco_livro * quantidade_livros
total_canetas = preco_caneta * quantidade_canetas
total_gasto = total_livros + total_canetas

print(f"O total gasto foi: $ {total_gasto:.2f}")