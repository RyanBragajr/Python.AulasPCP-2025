import math
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Localizacao:
    latitude: float
    longitude: float

@dataclass
class Relator:
    nome_completo: str
    documento_id: str
    email: str
    telefone: str
    localizacao: Localizacao

@dataclass
class Relato:
    relator: Relator
    tipo_desastre: str
    descricao: str
    data: datetime
    localizacao: Localizacao

class CLI_RelatoDesastre:
    def __init__(self):
        # Ponto de referência padrão (latitude, longitude) - pode ser alterado pelo usuário
        self.ponto_referencia = Localizacao(latitude=0.0, longitude=0.0)
        self.relatos: List[Relato] = []

    @staticmethod
    def distancia_haversine(loc1: Localizacao, loc2: Localizacao) -> float:
        # Calcula a distância do grande círculo entre dois pontos na superfície da Terra.
        R = 6371.0  # Raio da Terra em quilômetros
        lat1_rad = math.radians(loc1.latitude)
        lat2_rad = math.radians(loc2.latitude)
        delta_lat = math.radians(loc2.latitude - loc1.latitude)
        delta_lon = math.radians(loc2.longitude - loc1.longitude)

        a = math.sin(delta_lat / 2)**2 + \
            math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distancia = R * c
        return distancia

    def esta_dentro_do_raio(self, loc: Localizacao, raio_km=10.0) -> bool:
        distancia = self.distancia_haversine(self.ponto_referencia, loc)
        return distancia <= raio_km

    def input_localizacao(self, prompt_prefix="") -> Optional[Localizacao]:
        try:
            lat_str = input(f"{prompt_prefix}Latitude (graus decimais): ").strip()
            lon_str = input(f"{prompt_prefix}Longitude (graus decimais): ").strip()
            latitude = float(lat_str)
            longitude = float(lon_str)
            if not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
                print("Valores de latitude ou longitude inválidos.")
                return None
            return Localizacao(latitude, longitude)
        except ValueError:
            print("Entrada inválida para latitude ou longitude.")
            return None

    def input_data_hora(self) -> Optional[datetime]:
        try:
            data_str = input("Data (DD-MM-AAAA): ").strip()
            hora_str = input("Hora (HH:MM, formato 24h): ").strip()
            dt_str = f"{data_str} {hora_str}"
            dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
            return dt
        except ValueError:
            print("Formato de data ou hora inválido.")
            return None

    def adicionar_relato(self):
        print("\nInsira as informações do relator:")
        nome_completo = input("Nome completo: ").strip()
        documento_id = input("ID do documento: ").strip()
        email = input("E-mail: ").strip()
        telefone = input("Telefone: ").strip()
        print("Localização do relator:")
        localizacao_relator = self.input_localizacao("  ")
        if localizacao_relator is None:
            print("Falha ao inserir uma localização válida do relator. Criação do relato abortada.")
            return

        relator = Relator(
            nome_completo=nome_completo,
            documento_id=documento_id,
            email=email,
            telefone=telefone,
            localizacao=localizacao_relator
        )

        print("\nInsira os detalhes do relato de desastre:")
        tipo_desastre = input("Tipo de desastre (ex: enchente, incêndio, deslizamento): ").strip().lower()
        descricao = input("Descrição: ").strip()
        dt = self.input_data_hora()
        if dt is None:
            print("Falha ao inserir uma data/hora válida. Criação do relato abortada.")
            return
        print("Localização do relato:")
        localizacao_relato = self.input_localizacao("  ")
        if localizacao_relato is None:
            print("Falha ao inserir uma localização válida do relato. Criação do relato abortada.")
            return

        if not self.esta_dentro_do_raio(localizacao_relato):
            print(f"A localização do relato NÃO está dentro do raio de 10 km do ponto de referência.")
            return
        else:
            print("Localização do relato validada dentro do raio de 10 km.")

        relato = Relato(
            relator=relator,
            tipo_desastre=tipo_desastre,
            descricao=descricao,
            data=dt,
            localizacao=localizacao_relato
        )
        self.relatos.append(relato)
        print("Relato adicionado com sucesso!")

    def listar_relatos(self, relatos_filtrados: Optional[List[Relato]] = None):
        relatorios_a_mostrar = relatos_filtrados if relatos_filtrados is not None else self.relatos
        if not relatorios_a_mostrar:
            print("\nNenhum relato encontrado.")
            return

        print(f"\nListando {len(relatorios_a_mostrar)} relato(s):")
        for i, r in enumerate(relatorios_a_mostrar, start=1):
            print(f"\nRelato #{i}:")
            print(f"  Relator: {r.relator.nome_completo} (Documento: {r.relator.documento_id})")
            print(f"  Contato: E-mail: {r.relator.email}, Telefone: {r.relator.telefone}")
            print(f"  Localização do Relator: ({r.relator.localizacao.latitude}, {r.relator.localizacao.longitude})")
            print(f"  Tipo de Desastre: {r.tipo_desastre.capitalize()}")
            print(f"  Descrição: {r.descricao}")
            print(f"  Data e Hora: {r.data.strftime('%Y-%m-%d %H:%M')}")
            print(f"  Localização do Relato: ({r.localizacao.latitude}, {r.localizacao.longitude})")
            dist = self.distancia_haversine(self.ponto_referencia, r.localizacao)
            print(f"  Distância do ponto de referência: {dist:.2f} km")

    def buscar_relatos(self):
        print("\nBuscar relatos por:")
        print("1 - Tipo de desastre")
        print("2 - Raio de localização")
        print("3 - Período de datas")
        escolha = input("Escolha a opção (1-3): ").strip()
        if escolha == "1":
            tipo = input("Digite o tipo de desastre para buscar (insensível a maiúsculas): ").strip().lower()
            filtrados = [r for r in self.relatos if r.tipo_desastre == tipo]
            self.listar_relatos(filtrados)
        elif escolha == "2":
            loc = self.input_localizacao("Centro da busca ")
            if loc is None:
                print("Localização inválida. Busca abortada.")
                return
            try:
                raio_str = input("Digite o raio em km (máx 10 km): ").strip()
                raio = float(raio_str)
                if not (0 < raio <= 10):
                    print("O raio deve estar entre 0 e 10 km.")
                    return
            except ValueError:
                print("Valor de raio inválido.")
                return
            filtrados = [r for r in self.relatos if self.distancia_haversine(loc, r.localizacao) <= raio]
            self.listar_relatos(filtrados)
        elif escolha == "3":
            formato_data = "%d-%m-%a"
            inicio_str = input("Data de início (DD-MM-AAAA): ").strip()
            fim_str = input("Data de fim (DD-MM-AAAA): ").strip()
            try:
                data_inicio = datetime.strptime(inicio_str, formato_data)
                data_fim = datetime.strptime(fim_str, formato_data)
                if data_fim < data_inicio:
                    print("A data de fim deve ser igual ou posterior à data de início.")
                    return
            except ValueError:
                print("Formato de data inválido.")
                return
            filtrados = [r for r in self.relatos if data_inicio <= r.data.date() <= data_fim]
            self.listar_relatos(filtrados)
        else:
            print("Escolha inválida.")

    def definir_ponto_referencia(self):
        print("\nDefina o ponto de referência para cálculos de distância (padrão é 0.0, 0.0):")
        loc = self.input_localizacao()
        if loc:
            self.ponto_referencia = loc
            print(f"Ponto de referência definido para ({loc.latitude}, {loc.longitude})")
        else:
            print("Falha ao definir o ponto de referência.")

    def executar(self):
        print("=== CLI de Relato de Desastres Naturais ===")
        while True:
            print("\nComandos:")
            print("  1 - Adicionar novo relato")
            print("  2 - Listar todos os relatos")
            print("  3 - Buscar relatos")
            print("  4 - Definir ponto de referência")
            print("  0 - Sair")
            cmd = input("Digite o número do comando: ").strip()
            if cmd == "1":
                self.adicionar_relato()
            elif cmd == "2":
                self.listar_relatos()
            elif cmd == "3":
                self.buscar_relatos()
            elif cmd == "4":
                self.definir_ponto_referencia()
            elif cmd == "0":
                print("Saindo. Até logo!")
                break
            else:
                print("Comando desconhecido. Por favor, tente novamente.")

if __name__ == "__main__":
    cli = CLI_RelatoDesastre()
    cli.executar()
