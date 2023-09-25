import pandas as pd
from twilio.rest import Client
import os

# Your Account SID from twilio.com/console
account_sid = "ACdad4cb380c29f06f190fff73ca1cfb88"
# Your Auth Token from twilio.com/console
auth_token = "b9b9ed55fefc6a1cc98bb009c54ccd84"  # token changes all days #
client = Client(account_sid, auth_token)

myDir = os.getcwd()

# to access 6 excel excel
lista_meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{myDir}/excel/{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5561981868451",
            from_="+16189958380",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)
