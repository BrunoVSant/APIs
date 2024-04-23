import requests


class Asaas:
    def __init__(self) -> None:
        self.chave = 'Insira a chave'
    
    def puxar_dados_clientes(self, CNPJ):
        try:
            url = f'https://sandbox.asaas.com/api/v3/customers?cpfCnpj={CNPJ}'

            headers = {
                "accept": "application/json",
                "access_token": self.chave
            }

            response = requests.get(url, headers=headers)
            return response.text
        except Exception as e:
            print(e)
            return None
        
    def cri_cont(self, usu, valor, desc, venc):
        try:
            url = "https://api.asaas.com/v3/payments"
            usuario = str(usu)
            venci = str(venc)
            desc = str(desc)
            print(venci)
            payload = {
                "billingType": "BOLETO",
                "customer": usuario,
                "dueDate": venci,#qual dia ficará os vencimentos dos boletos
                "description": desc,
                "value": str(valor)
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "access_token": self.chave
            }

            response = requests.post(url, json=payload, headers=headers)
            return response.text
        except Exception as e:
            print(e)
            return None
        
        
    def ger_nf(self, payment, customer, value, date):
        try:
            url = "https://api.asaas.com/v3/invoices"
            payload = {
                "taxes": {
                    "retainIss": True,#Retem ISS?
                    "iss": 1,#valor ISS
                    "cofins": 1,#valor COFINS
                    "inss": 1,#valor INSS
                    "ir": 1,#valor IR
                    "pis": 1,#valor PIS
                    "csll": 1#valor CSLL
                },
                "updatePayment": True,
                "municipalServiceCode": "17.12",
                "effectiveDate": f'{date}',#Data 
                "deductions": 1,#oque teremos
                "value": 1,#Puxar do main.py
                "observations": "Tera alguma coisa?",#Devemos informar algo?
                "serviceDescription": "Rede de beneficios",
                "customer": "buscar da requisição", #puxar identificador de cliente do main.py
                "payment": "pay_9469558531261802" #puxar identificador de pagamento do main.py
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "access_token": self.chave
            }

            response = requests.post(url, json=payload, headers=headers)

            return response
        except Exception as e:
            print(e)
            return None

    def moni_pag(self, date):
        try:
            url = f'https://api.asaas.com/v3/payments?paymentDate={date}&&limit=100'
            headers = {
                "accept": "application/json",
                "access_token": self.chave
            }
            resp = requests.get(url, headers=headers)
            resp_json = resp.json()['data']
            return resp_json
        except Exception as e:
            print(e)
            return None
    