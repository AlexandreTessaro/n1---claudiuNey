from src.leitura_dados import ler_conexoes, ler_entregas
from src.leilao_basico import calcular_lucro_basico
from src.leilao_otimizado import calcular_lucro_otimizado
from src.comparar_desempenho import comparar_desempenho
from src.simulated_annealing import calcular_lucro_simulated_annealing 
from src.swarm import calcular_lucro_swarm  

def main():
    destinos, conexoes = ler_conexoes()
    entregas = ler_entregas()

    print("Executando Leilão de Entregas - Versão Básica")
    entregas_realizadas_basico, lucro_basico = calcular_lucro_basico(destinos, conexoes, entregas)
    
    print("Entregas realizadas (básico):")
    for entrega in entregas_realizadas_basico:
        tempo_inicio, destino, bonus = entrega
        print(f"({tempo_inicio}, {destino}; {bonus})")
    
    print(f"Lucro esperado (básico): {lucro_basico}")

    print("\nExecutando Leilão de Entregas - Versão Otimizada")
    entregas_realizadas_otimizado, lucro_otimizado = calcular_lucro_otimizado(destinos, conexoes, entregas)
    
    print("Entregas realizadas (otimizado):")
    for entrega in entregas_realizadas_otimizado:
        tempo_inicio, destino, bonus = entrega
        print(f"({tempo_inicio}, {destino}; {bonus})")
    
    print(f"Lucro esperado (otimizado): {lucro_otimizado}")

    print("\nExecutando Leilão de Entregas - Versão Simulated Annealing")
    entregas_realizadas_sa, lucro_sa = calcular_lucro_simulated_annealing(destinos, conexoes, entregas)
    
    print("Entregas realizadas (Simulated Annealing):")
    for entrega in entregas_realizadas_sa:
        tempo_inicio, destino, bonus = entrega
        print(f"({tempo_inicio}, {destino}; {bonus})")
    
    print(f"Lucro esperado (Simulated Annealing): {lucro_sa}")

    print("\nExecutando Leilão de Entregas - Versão Swarm Optimization")
    entregas_realizadas_swarm, lucro_swarm = calcular_lucro_swarm(destinos, conexoes, entregas)
    
    print("Entregas realizadas (Swarm Optimization):")
    for entrega in entregas_realizadas_swarm:
        tempo_inicio, destino, bonus = entrega
        print(f"({tempo_inicio}, {destino}; {bonus})")
    
    print(f"Lucro esperado (Swarm Optimization): {lucro_swarm}")

    comparar_desempenho(destinos, conexoes, entregas)

if __name__ == "__main__":
    main()
