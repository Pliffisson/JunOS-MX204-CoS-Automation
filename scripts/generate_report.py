import sys
from fpdf import FPDF
import datetime
import os

class ISPReport(FPDF):
    def header(self):
        # Header background
        self.set_fill_color(0, 51, 102)  # Dark Blue
        self.rect(0, 0, 210, 30, 'F')
        
        self.set_font("helvetica", 'B', 16)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, "Relatório de Configuração de Cliente - ISP", 0, 1, 'C')
        self.set_font("helvetica", 'I', 10)
        self.cell(0, 5, "Automação Juniper MX204", 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Página {self.page_no()} | Comprovante Técnico Gerado via Ansible", 0, 0, 'C')

def generate_report(client_name, vlan_id, bandwidth, ipv4, ipv6, status):
    pdf = ISPReport()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.ln(20) # Space for header
    
    # Metadata
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", '', 10)
    pdf.cell(0, 10, f"Data da Geração: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'R')
    pdf.ln(5)
    
    # Client Info Section
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("helvetica", 'B', 12)
    pdf.cell(0, 10, "  Dados do Cliente", 0, 1, 'L', fill=True)
    pdf.set_font("helvetica", '', 11)
    
    # Create Table-like structure
    fields = [
        ("NOME DO CLIENTE", client_name),
        ("VLAN ID", str(vlan_id)),
        ("PLANO DE BANDA", bandwidth),
        ("VALOR DO SHAPING / POLICER", bandwidth),
        ("IPv4 WAN", ipv4),
        ("IPv6 WAN", ipv6),
        ("STATUS DA OPERAÇÃO", status.upper())
    ]
    
    for label, val in fields:
        pdf.set_font("helvetica", 'B', 10)
        pdf.cell(60, 10, f" {label}:", 1, 0, 'L')
        pdf.set_font("helvetica", '', 10)
        pdf.cell(130, 10, f" {val}", 1, 1, 'L')
    
    pdf.ln(10)
    
    # Technical Summary
    pdf.set_font("helvetica", 'B', 12)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(0, 10, "  Resumo Técnico da Configuração", 0, 1, 'L', fill=True)
    pdf.set_font("helvetica", '', 10)
    
    summary = (
        "O provisionamento foi realizado com sucesso no roteador de borda MX204.\n\n"
        "Componentes Aplicados:\n"
        "1. Interface Lógica: ae0.{} (VLAN-ID {})\n"
        "2. Qualidade de Serviço (CoS): Traffic Control Profile (TCP) vinculado para controle de download.\n"
        "3. Filtros de Segurança: Firewall Filter ativado com anti-spoofing (RPF Check).\n"
        "4. Controle de Upload: Policer específico vinculado via firewall filter.\n"
        "5. Classificação: Mapeamento DSCP (IPv4) e DSCP-IPv6 (IPv6) padrão ISP."
    ).format(vlan_id, vlan_id)
    
    pdf.multi_cell(0, 8, summary, border=1)
    
    # Path logic
    output_dir = "reports"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    output_filename = f"{output_dir}/REPORTE_VLAN_{vlan_id}.pdf"
    pdf.output(output_filename)
    return output_filename

if __name__ == "__main__":
    if len(sys.argv) < 7:
        print("Uso: python3 generate_report.py 'Nome' 'VLAN' 'Banda' 'IPv4' 'IPv6' 'Status'")
        sys.exit(1)
    
    r_file = generate_report(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    print(f"Relatório gerado com sucesso: {r_file}")
