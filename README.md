# Junos MX204 CoS Automation 🚀

![Ansible](https://img.shields.io/badge/Ansible-E00?style=for-the-badge&logo=ansible&logoColor=white)
![Juniper](https://img.shields.io/badge/Juniper-CC0000?style=for-the-badge&logo=junipernetworks&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Network Automation](https://img.shields.io/badge/Focus-Network_Automation-blue?style=for-the-badge)

Este projeto automatiza a gestão de **Class of Service (CoS)** e **Filtros de Firewall** para roteadores Juniper **MX204** (chipset Trio), garantindo uma configuração padronizada e segura para links dedicados de ISP.

## 🌟 Funcionalidades Principais

- **Ciclo de Vida Iterativo (C/E/D/S)**: O script verifica a existência do cliente e oferece opções para **C**riar, **E**ditar, **D**eletar ou **S**aír.
- **Visualização de Auditoria**: Novo roteiro para consultar configurações atuais (IPv4, IPv6, Firewall, CoS) e gerar relatórios Markdown.
- **Relatório em PDF**: Geração automática de relatórios técnicos profissionais para cada cliente (Criação/Edição).
- **Segurança com Ansible Vault**: Proteção de credenciais de rede através de criptografia.
- **Dual-Stack nativo**: Suporte completo a IPv4 e IPv6 com classificadores independentes.
- **Conectividade Flexível**: Suporte a portas SSH customizadas (ex: 60002).

## 📂 Estrutura do Projeto

- `manage_clients.yml`: Playbook principal interativo (Gestão).
- `view_client.yml`: Playbook de visualização e auditoria (Consulta).
- `reports/`: Pasta centralizada onde todos os relatórios (.pdf e .md) são salvos.
- `inventory.yml`: Inventário com definições de host e porta.
- `templates/cos_config.j2`: Modelo Jinja2 para a configuração Junos.
- `templates/client_report.md.j2`: Modelo Markdown para relatórios de consulta.
- `scripts/generate_report.py`: Script Python para geração de relatórios PDF.
- `group_vars/all/vault.yml`: Arquivo encriptado para senhas.

## 🛠️ Instalação e Preparação

### 1. Requisitos
- Ansible instalado.
- Coleção Juniper instalada: `ansible-galaxy collection install junipernetworks.junos`
- Python 3.12+ com biblioteca `fpdf2`.
- Antes da primeira conexão, confira a fingerprint do roteador por um canal confiável e registre a chave no `known_hosts` do operador. Não desative `host_key_checking` em ambientes de produção.

### 2. Segurança (Ansible Vault)
O arquivo [vault.yml](group_vars/all/vault.yml) já está criptografado com Ansible Vault. Edite-o com a senha do Vault e defina `router_password` para o seu ambiente:
```bash
ansible-vault edit group_vars/all/vault.yml
```
Não publique senhas nem arquivos Vault descriptografados.

## 🚀 Como Usar

Execute o playbook principal passando a flag do Vault:

```bash
ansible-playbook -i inventory.yml manage_clients.yml --ask-vault-pass
```

### 🔍 Visualizar Configurações (Audit)
Para consultar a situação técnica de um cliente e gerar um relatório formatado em Markdown:

```bash
ansible-playbook -i inventory.yml view_client.yml --ask-vault-pass
```
O arquivo será salvo automaticamente na pasta `reports/` como `REPORT_CLIENTE_VLAN_<ID>.md`.

### Comandos de Operação (Interativo)
- **VLAN ID**: Digite o ID do cliente.
- **Branching**: Se o cliente já existir, selecione `e` (Edit), `d` (Delete) ou `s` (Skip).
- **Dados**: Para novos clientes, insira os dados separados por vírgula conforme solicitado.

## 📊 Relatórios
Todos os relatórios (PDF e Markdown) são salvos na pasta `reports/` seguindo o padrão:
- **PDF**: `REPORTE_VLAN_<ID>.pdf` (Gerado na Criação/Edição)
- **Markdown**: `REPORT_CLIENTE_VLAN_<ID>.md` (Gerado na Consulta)

### 🖥️ Como visualizar os relatórios
Para abrir os relatórios PDF diretamente pelo terminal Linux:
```bash
evince reports/REPORTE_VLAN_<ID>.pdf
```
Ou abra manualmente a pasta `reports/` e utilize o seu leitor de PDF preferido.

---
**Consultoría ISP/NOC - Automação Juniper MX204**
