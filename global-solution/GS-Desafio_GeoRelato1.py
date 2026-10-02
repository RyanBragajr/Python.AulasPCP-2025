#!/usr/bin/env python3

import math
from datetime import datetime
import sys

def haversine(lat1, lon1, lat2, lon2):
    # Calcula a distância do grande círculo entre dois pontos na terra (especificados em graus decimais)
    R = 6371  # Raio da terra em quilômetros
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c  # em quilômetros

PONTO_DE_REFERENCIA = (0, 0)  # ponto de referência padrão (latitude, longitude), o usuário pode mudar

# Estruturas de dados:
# relatores: dicionário com chave pelo número do documento para unicidade
# relatos: lista de dicionários com informações do relato. Também manter um dicionário por tipo para busca rápida por tipo.

relatores = {}
relatos = []
relatos_por_tipo = {}

def input_non_empty(prompt):
    while True:
        inp = input(prompt).strip()
        if inp:
            return inp
        print("A entrada não pode estar vazia. Por favor, tente novamente.")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Número inválido. Por favor, tente novamente.")

def input_date(prompt):
    while True:
        inp = input(prompt).strip()
        try:
            return datetime.strptime(inp, "%Y-%m-%d").date()
        except ValueError:
            print("Formato de data inválido. Por favor, insira no formato AAAA-MM-DD.")

def input_time(prompt):
    while True:
        inp = input(prompt).strip()
        try:
            return datetime.strptime(inp, "%H:%M").time()
        except ValueError:
            print("Formato de hora inválido. Por favor, insira no formato HH:MM (24h).")

def register_reporter():
    print("\n--- Registrar um novo relator ---")
    nome = input_non_empty("Nome completo: ")
    documento = input_non_empty("Documento (ID único): ")
    if documento in relatores:
        print("Este documento já está registrado.")
        return
    email = input_non_empty("E-mail: ")
    telefone = input_non_empty("Telefone: ")
    print("Insira a localização aproximada do relator:")
    lat = input_float("Latitude (-90 a 90): ")
    lon = input_float("Longitude (-180 a 180): ")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        print("Coordenadas inválidas.")
        return
    relatores[documento] = {
        'nome': nome,
        'documento': documento,
        'email': email,
        'telefone': telefone,
        'localizacao': (lat, lon)
    }
    print("Relator registrado com sucesso.\n")

def register_report():
    print("\n--- Registrar um novo relato de desastre ---")
    documento = input_non_empty("Insira o documento do relator (deve estar registrado): ")
    if documento not in relatores:
        print("Relator não encontrado. Por favor, registre primeiro.")
        return
    tipos_de_desastre = ['enchente', 'incendio', 'deslizamento']
    print("Tipos de desastre:", ", ".join(tipos_de_desastre))
    tipo = input_non_empty("Tipo de catástrofe: ").lower()
    if tipo not in tipos_de_desastre:
        print("Tipo de desastre inválido. Use um dos tipos pré-definidos.")
        return
    descricao = input_non_empty("Descrição: ")
    data = input_date("Data (AAAA-MM-DD): ")
    hora = input_time("Hora (HH:MM 24h): ")
    print("Insira a localização precisa do relato de desastre:")
    lat = input_float("Latitude (-90 a 90): ")
    lon = input_float("Longitude (-180 a 180): ")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        print("Coordenadas inválidas.")
        return

    dist = haversine(lat, lon, PONTO_DE_REFERENCIA[0], PONTO_DE_REFERENCIA[1])
    if dist > 10:
        print(f"A localização do relato está a {dist:.2f} km do ponto de referência, o que excede o limite de 10 km.")
        return

    relato = {
        'documento_relator': documento,
        'tipo': tipo,
        'descricao': descricao,
        'data': data,
        'hora': hora,
        'localizacao': (lat, lon)
    }
    relatos.append(relato)
    if tipo not in relatos_por_tipo:
        relatos_por_tipo[tipo] = []
    relatos_por_tipo[tipo].append(relato)
    print("Relato de desastre registrado com sucesso.\n")

def list_reports():
    if not relatos:
        print("Nenhum relato registrado.")
        return
    print("\n--- Listando todos os relatos de desastre ---")
    for idx, r in enumerate(relatos, 1):
        print_report(r, idx)
    print("Fim dos relatos.\n")

def print_report(relato, idx=None):
    prefixo = f"{idx}. " if idx else ""
    rep = relatores.get(relato['documento_relator'], None)
    nome_relator = rep['nome'] if rep else "Desconhecido"
    print(f"{prefixo}Tipo: {relato['tipo'].capitalize()}, Data: {relato['data']} {relato['hora']}, Localização: {relato['localizacao']}")
    print(f"   Descrição: {relato['descricao']}")
    print(f"   Relator: {nome_relator} (Documento: {relato['documento_relator']})")

def search_reports():
    print("\n--- Buscar relatos de desastres ---")
    print("Buscar por (pressione Enter para pular o critério):")
    tipo = input("Tipo (enchente, incendio, deslizamento): ").strip().lower()
    lat = input("Latitude central para filtro de localização (vazio para pular): ").strip()
    lon = input("Longitude central para filtro de localização (vazio para pular): ").strip()
    raio_km = None
    if lat and lon:
        try:
            lat = float(lat)
            lon = float(lon)
            raio_km = float(input("Raio em km: ").strip())
            if raio_km < 0:
                print("O raio deve ser positivo.")
                return
        except ValueError:
            print("Entrada de localização ou raio inválida.")
            return
    data_de_str = input("Data de (AAAA-MM-DD, vazio para pular): ").strip()
    data_ate_str = input("Data até (AAAA-MM-DD, vazio para pular): ").strip()
    data_de = None
    data_ate = None
    try:
        if data_de_str:
            data_de = datetime.strptime(data_de_str, "%Y-%m-%d").date()
        if data_ate_str:
            data_ate = datetime.strptime(data_ate_str, "%Y-%m-%d").date()
    except ValueError:
        print("Formato de data inválido.")
        return

    # Filtrar relatos
    filtrados = relatos
    if tipo in relatos_por_tipo:
        filtrados = relatos_por_tipo[tipo]
    elif tipo:
        # Se tipo inserido mas sem relatos para esse tipo
        filtrados = []

    def matches(r):
        if data_de and r['data'] < data_de:
            return False
        if data_ate and r['data'] > data_ate:
            return False
        if raio_km is not None:
            d = haversine(r['localizacao'][0], r['localizacao'][1], lat, lon)
            if d > raio_km:
                return False
        return True

    resultados = [r for r in filtrados if matches(r)]

    if not resultados:
        print("Nenhum relato encontrado que corresponda aos critérios.")
    else:
        print(f"\nEncontrados {len(resultados)} relato(s):")
        for idx, r in enumerate(resultados, 1):
            print_report(r, idx)
    print()

def set_reference_point():
    print("\n--- Definir Ponto de Referência para Raio de 10km ---")
    lat = input_float("Insira a latitude de referência (-90 a 90): ")
    lon = input_float("Insira a longitude de referência (-180 a 180): ")
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        print("Coordenadas inválidas, ponto de referência não alterado.")
        return None
    return (lat, lon)

def main_menu():
    global PONTO_DE_REFERENCIA
    print("\n=== CLI de Relato de Desastres ===")
    print(f"Ponto de referência atual para relatos: Latitude {PONTO_DE_REFERENCIA[0]}, Longitude {PONTO_DE_REFERENCIA[1]}")
    print("1. Definir ponto de referência")
    print("2. Registrar um novo relator")
    print("3. Registrar um novo relato de desastre")
    print("4. Listar todos os relatos")
    print("5. Buscar relatos")
    print("6. Sair")
    escolha = input("Escolha uma opção (1-6): ").strip()
    return escolha

def main():
    global PONTO_DE_REFERENCIA
    # Ao iniciar, pergunte ao usuário se deseja definir o ponto de referência ou usar o padrão (0,0)
    print("Bem-vindo ao CLI de Relato de Desastres.")
    print("Por padrão, o ponto de referência para validação de distância está na latitude 0, longitude 0.")
    ans = input("Você gostaria de definir um ponto de referência personalizado agora? (s/n) ").strip().lower()
    if ans == 's':
        ponto = set_reference_point()
        if ponto:
            PONTO_DE_REFERENCIA = ponto
    while True:
        escolha = main_menu()
        if escolha == '1':
            ponto = set_reference_point()
            if ponto:
                PONTO_DE_REFERENCIA = ponto
                print(f"Ponto de referência atualizado para: {PONTO_DE_REFERENCIA}\n")
        elif escolha == '2':
            register_reporter()
        elif escolha == '3':
            register_report()
        elif escolha == '4':
            list_reports()
        elif escolha == '5':
            search_reports()
        elif escolha == '6':
            print("Saindo. Até logo!")
            sys.exit(0)
        else:
            print("Escolha inválida, por favor, tente novamente.")

if __name__ == "__main__":
    main()
