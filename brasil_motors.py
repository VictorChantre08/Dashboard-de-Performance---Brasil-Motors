import pandas as pd
import os

# 1. Configurações Iniciais
arquivo_origem = "BrasilMotors_Planilha (1).xlsx"
abas_para_processar = ['VENDEDORES', 'CLIENTES', 'ESTOQUE', 'VENDAS']
pasta_saida = 'dados_limpos'

# Cria uma pasta para organizar os arquivos finais, caso ela não exista
if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

print("Iniciando o Pipeline de Extração e Limpeza...\n" + "-"*40)

# 2. Laço de repetição: Extrai, Transforma e Carrega (ETL)
for aba in abas_para_processar:
    try:
        print(f"Processando a tabela: {aba}...")
        
        # Extração
        df = pd.read_excel(arquivo_origem, sheet_name=aba)
        
        # Transformação (Padronização das colunas)
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Carga (Exportando para CSV dentro da pasta dados_limpos)
        nome_arquivo_saida = f"{pasta_saida}/dados_limpos_{aba.lower()}.csv"
        df.to_csv(nome_arquivo_saida, index=False)
        
        print(f"-> Sucesso! Arquivo gerado: {nome_arquivo_saida}\n")
        
    except Exception as e:
        print(f"Erro ao processar a aba {aba}: {e}\n")

print("-" * 40 + "\nPipeline finalizado com sucesso! Arquivos prontos para o Power BI.")