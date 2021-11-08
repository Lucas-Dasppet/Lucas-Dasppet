import os
import pandas as pd


caminho_in = r'G:\ECOMMERCE'
extensoes = ['.png', '.jpg', '.jpeg', '.bmp', '.pdf', '.webp', '.eps']
lista_arquivos_sem_imagem = []
lista_arquivos_com_imagem = []

def adiciona_lista_sem_imagem(sku, marca):
    lista_arquivos_sem_imagem.append([sku, marca])


def adiciona_lista_com_imagem(sku, marca):
    lista_arquivos_com_imagem.append([sku, marca])


def verifica_arquivo(caminho_completo, sku, marca):
    for _, _, files in os.walk(caminho_completo):
        verificador = False
        for file in files:
            _, extensao = os.path.splitext(f'{caminho_completo}\{file}')
            if extensao in extensoes:
                verificador = True
                adiciona_lista_com_imagem(sku, marca)
                break
        if verificador == False:
            adiciona_lista_sem_imagem(sku, marca)


def verifica_diretorio(caminho, marca):
    for roots, dirs, files in os.walk(caminho):
        for dir in dirs:
            verficador = False
            caminho_completo = f'{caminho}\{dir}'
            if os.path.getsize(caminho_completo) != 0:
                adiciona_lista_sem_imagem(dir, marca)
                continue
            verifica_arquivo(caminho_completo, dir, marca)


for dir in next(os.walk(caminho_in))[1]:
    verifica_diretorio(f'{caminho_in}\{dir}', dir)
print(f'COM IMAGENS: {len(lista_arquivos_com_imagem)}, SEM IMAGENS: {len(lista_arquivos_sem_imagem)}')
    
planilha = pd.DataFrame(data=lista_arquivos_sem_imagem)
colunas = {
    0: 'SKU',
    1: 'MARCA'
}
planilha.rename(columns=colunas, inplace=True)
planilha.to_excel(r'C:\Users\lucas.borges\Documents\Pessoal2\Relatório.xlsx', index=False)
print('FEITO!!!')
