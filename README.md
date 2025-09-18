<p align='center'>
    <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=300&section=header&text=A%20viagem&fontSize=90&animation=fadeIn&fontAlignY=30&desc=%20Cada%20destino%20começa%20com%20uma%20boa%20modelagem!&descAlignY=51&descAlign=62"/>
</p>

# 🧳 Projeto Viagem

Este repositório contém o projeto **Viagem**, desenvolvido com base na **Programação Orientada a Objetos (POO)** e no padrão arquitetural **MVC (Model-View-Controller)**.  
O sistema foi modelado para representar um **gerenciamento de viagens**, contemplando passageiros, destinos, itinerários, meios de transporte e pagamentos.

---

## 📌 Objetivo

O projeto tem como objetivo aplicar conceitos de **POO e modelagem UML**, simulando um sistema de viagens realista, com funcionalidades de compra de passagens, organização de itinerários e controle de pagamentos.

---

## 📂 Estrutura de Classes

O sistema é composto por diversas classes, modeladas conforme o diagrama UML abaixo:

- **Pessoa**: Representa o passageiro.  
- **Viagem**: Agrega informações do itinerário, meio de transporte e passagem.  
- **Itinerário**: Controla os destinos e passageiros.  
- **Destino**: Representa a localização da viagem.  
- **Passagem**: Contém número, assento, data e validade.  
- **Pagamento** (classe abstrata): Superclasse para formas de pagamento.  
  - **Cartão**  
  - **Pix**  
  - **Cédulas**  
- **MeioDeTransporte**: Representa ônibus, avião, navio etc.  
- **EmpresaTransporte**: Relacionada aos meios de transporte.  
- **Parada**: Define locais de parada durante a viagem.  

📌 O diagrama UML está disponível em `/docs/modelagemufsc.drawio.png`.  

---

## 🛠️ Tecnologias Utilizadas

- **Python** (linguagem principal)  
- **UML (diagramação com Draw.io)**  
- Git e GitHub para versionamento  

---

## 🚀 Funcionalidades

- Cadastro de passageiros e itinerários  
- Criação de destinos e paradas  
- Emissão e validação de passagens  
- Associação de meios de transporte às empresas  
- Diferentes formas de pagamento (Cartão, Pix, Cédulas)  
- Cálculo de preço e disponibilidade da viagem  

---

## 📂 Estrutura do Repositório


