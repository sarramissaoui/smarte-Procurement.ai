from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Image
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from datetime import datetime
import os

# Inetum Brand Colors
INETUM_DARK = HexColor("#1C2B4A")
INETUM_TEAL = HexColor("#1ABC9C")
INETUM_LIGHT = HexColor("#ECF0F1")
INETUM_TEXT = HexColor("#2C3E50")
INETUM_ACCENT = HexColor("#0E9B7E")
SUCCESS_COLOR = HexColor("#27AE60")
WARNING_COLOR = HexColor("#E67E22")
DANGER_COLOR = HexColor("#C0392B")

class InetumPDFReporter:
    def __init__(self, output_folder="reports_stylish"):
        self.output_folder = output_folder
        os.makedirs(output_folder, exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        
        self.styles.add(ParagraphStyle(
            name='InetumTitle',
            parent=self.styles['Heading1'],
            fontSize=32,
            textColor=INETUM_DARK,
            spaceAfter=6,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold',
            letterSpacing=1.5
        ))

        self.styles.add(ParagraphStyle(
            name='Subtitle',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=INETUM_TEAL,
            spaceAfter=12,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))

        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=INETUM_DARK,
            spaceAfter=10,
            spaceBefore=12,
            fontName='Helvetica-Bold',
            borderColor=INETUM_TEAL,
            borderPadding=8,
            borderWidth=2,
            borderRadius=4
        ))

       
        self.styles['BodyText'].fontSize = 10
        self.styles['BodyText'].textColor = INETUM_TEXT
        self.styles['BodyText'].spaceAfter = 8
        self.styles['BodyText'].alignment = TA_JUSTIFY
        self.styles['BodyText'].leading = 14

        self.styles.add(ParagraphStyle(
            name='SmallText',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=HexColor("#999999"),
            spaceAfter=4
        ))

    def _create_header(self):
        
        logo_path = "INETUM_LOGO.png"
        logo = None
        
        if os.path.exists(logo_path):
            try:
                
                logo_width = 2.0 * inch
                logo_height = (850 / 2929) * logo_width
                logo = Image(logo_path, width=logo_width, height=logo_height)
            except:
                logo = None
        
        
        header_data = []
        
        
        if logo:
            header_data.append([logo])
        
        
        header_data.append([
            Paragraph(
                "<b>SmartTender AI for Inetum</b><br/><font size=12>Intelligent CV-to-Tender Matching</font>",
                self.styles['InetumTitle']
            )
        ])
        
        colWidths = [7.5*inch]
        
        header_table = Table(header_data, colWidths=colWidths)
        table_style = [
            ('TEXTCOLOR', (0, 0), (-1, -1), INETUM_DARK),
            ('VALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
            ('BORDER', (0, 0), (-1, -1), 0),
        ]
        header_table.setStyle(TableStyle(table_style))
        return header_table

    def _create_match_score_visualization(self, score):
        
        
        filled = int(round(score / 10))
        empty = 10 - filled
        
        if score >= 75:
            color = SUCCESS_COLOR
            status = "EXCELLENT MATCH"
            background = HexColor("#E8F8F5")
        elif score >= 50:
            color = WARNING_COLOR
            status = "GOOD MATCH"
            background = HexColor("#FEF5E7")
        else:
            color = DANGER_COLOR
            status = "NEEDS IMPROVEMENT"
            background = HexColor("#FADBD8")

        
        filled_bar = "█" * filled
        empty_bar = "░" * empty
        
        
        data = [
            [
                Paragraph(
                    f"<para alignment='center'><font size=48 color='{color.hexval()}'><b>{score}%</b></font></para>",
                    self.styles['Normal']
                ),
                Paragraph(
                    f"<para alignment='left'><font size=16 color='{color.hexval()}'><b>{status}</b></font></para>",
                    self.styles['Normal']
                )
            ],
            [
                "",  
                Paragraph(
                    f"<para alignment='left'><font size=20 color='{color.hexval()}'><b>{filled_bar}</b></font>"
                    f"<font size=20 color='#CCCCCC'><b>{empty_bar}</b></font></para>",
                    self.styles['Normal']
                )
            ]
        ]
        

        score_table = Table(data, colWidths=[2.5*inch, 5.0*inch])
        score_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), background),
            ('SPAN', (0, 0), (0, 1)),  # Merge the two left cells vertically
            ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ('ALIGN', (1, 0), (1, 0), 'LEFT'),
            ('ALIGN', (1, 1), (1, 1), 'LEFT'),
            ('VALIGN', (0, 0), (0, -1), 'MIDDLE'),
            ('VALIGN', (1, 0), (1, 0), 'BOTTOM'),
            ('VALIGN', (1, 1), (1, 1), 'TOP'),
            ('LEFTPADDING', (0, 0), (0, -1), 20),
            ('RIGHTPADDING', (0, 0), (0, -1), 10),
            ('LEFTPADDING', (1, 0), (1, -1), 20),
            ('RIGHTPADDING', (1, 0), (1, -1), 20),
            ('TOPPADDING', (0, 0), (-1, -1), 15),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
            ('BOX', (0, 0), (-1, -1), 2, color),
        ]))
        
        return score_table

    def _create_skills_table(self, matched, missing, extra):
        
        max_rows = max(len(matched) if matched else 0, 
                      len(missing) if missing else 0, 
                      len(extra) if extra else 0)
        
        matched = (matched or []) + [""] * (max_rows - len(matched or []))
        missing = (missing or []) + [""] * (max_rows - len(missing or []))
        extra = (extra or []) + [""] * (max_rows - len(extra or []))

        data = [
            [
                Paragraph("<b style='font-size:12'>✓ Matched Skills</b>", 
                         ParagraphStyle('header', parent=self.styles['Normal'], 
                                      textColor=white, fontSize=12, fontName='Helvetica-Bold')),
                Paragraph("<b style='font-size:12'>✗ Missing Skills</b>", 
                         ParagraphStyle('header', parent=self.styles['Normal'], 
                                      textColor=white, fontSize=12, fontName='Helvetica-Bold')),
                Paragraph("<b style='font-size:12'>+ Extra Skills</b>", 
                         ParagraphStyle('header', parent=self.styles['Normal'], 
                                      textColor=white, fontSize=12, fontName='Helvetica-Bold')),
            ]
        ]

        for m, miss, ex in zip(matched, missing, extra):
            data.append([
                Paragraph(f"<font color={SUCCESS_COLOR.hexval()} size=10><b>• {m}</b></font>" if m else "",
                         self.styles['BodyText']),
                Paragraph(f"<font color={DANGER_COLOR.hexval()} size=10><b>• {miss}</b></font>" if miss else "",
                         self.styles['BodyText']),
                Paragraph(f"<font color={INETUM_TEAL.hexval()} size=10><b>• {ex}</b></font>" if ex else "",
                         self.styles['BodyText']),
            ])

        skills_table = Table(data, colWidths=[2.35*inch, 2.35*inch, 2.35*inch])
        skills_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), SUCCESS_COLOR),
            ('BACKGROUND', (1, 0), (1, 0), DANGER_COLOR),
            ('BACKGROUND', (2, 0), (2, 0), INETUM_TEAL),
            ('TEXTCOLOR', (0, 0), (-1, 0), white),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('LEFTPADDING', (0, 0), (-1, -1), 14),
            ('RIGHTPADDING', (0, 0), (-1, -1), 14),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, HexColor("#DCDDE1")),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [white, HexColor("#F9F9F9")]),
            ('BORDER', (0, 0), (-1, -1), 1),
            ('BORDERCOLOR', (0, 0), (-1, -1), HexColor("#BDC3C7")),
        ]))
        return skills_table

    def _create_recommendations(self, score, missing):
        
        recommendations = []
        rec_color = INETUM_DARK
        
        if score >= 80:
            recommendations.append("✓ Excellent fit! This candidate meets the majority of requirements.")
            rec_color = SUCCESS_COLOR
        elif score >= 60:
            recommendations.append("◐ Strong candidate. Training in missing areas could close the gap.")
            rec_color = WARNING_COLOR
        elif score >= 40:
            recommendations.append("△ Fair match. Consider additional screening and skill development plans.")
            rec_color = WARNING_COLOR
        else:
            recommendations.append("✗ Limited match. Consider alternative candidates or intensive training programs.")
            rec_color = DANGER_COLOR

        if missing and len(missing) > 0:
            recommendations.append(f"• Priority: Develop expertise in {', '.join(missing[:3])}")

        if len(recommendations) < 3:
            recommendations.append("• Recommend scheduling a detailed technical interview for validation.")

        rec_data = [[Paragraph(f"<font color={rec_color.hexval()} size=10><b>{rec}</b></font>", 
                              self.styles['BodyText'])] for rec in recommendations]
        
        rec_table = Table(rec_data, colWidths=[7*inch])
        rec_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), HexColor("#F8FBFF")),
            ('TEXTCOLOR', (0, 0), (-1, -1), INETUM_TEXT),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 18),
            ('RIGHTPADDING', (0, 0), (-1, -1), 18),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('BORDER', (0, 0), (-1, -1), 2),
            ('BORDERCOLOR', (0, 0), (-1, -1), rec_color),
        ]))
        return rec_table

    def _create_footer(self, cv_name, tender_name):
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        clean_cv = cv_name.replace('.pdf', '').replace('.PDF', '')
        clean_tender = tender_name.replace('.pdf', '').replace('.PDF', '')
        footer_text = f"Report: {clean_cv} → {clean_tender} | Generated: {timestamp} | SmartTender AI by Inetum"
        
        return Paragraph(
            f"<font size=8 color={INETUM_ACCENT.hexval()}><i>{footer_text}</i></font>",
            ParagraphStyle('footer', parent=self.styles['Normal'], alignment=TA_CENTER)
        )

    def generate_report(self, cv_name, tender_name, match_score, missing, extra):
       
        safe_cv = cv_name.replace(" ", "_").replace(".pdf", "")
        safe_tender = tender_name.replace(" ", "_").replace(".pdf", "")
        pdf_filename = os.path.join(self.output_folder, f"{safe_cv}_vs_{safe_tender}_REPORT.pdf")

        doc = SimpleDocTemplate(
            pdf_filename,
            pagesize=A4,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )

     
        story = []

  
        story.append(self._create_header())
        story.append(Spacer(1, 0.25*inch))

    
        clean_cv = cv_name.replace('.pdf', '').replace('.PDF', '')
        clean_tender = tender_name.replace('.pdf', '').replace('.PDF', '')
        
        info_data = [
            [
                Paragraph("<b>👤 Candidate:</b>", self.styles['BodyText']),
                Paragraph(f"<font color={INETUM_DARK.hexval()}><b>{clean_cv}</b></font>", 
                         self.styles['BodyText'])
            ],
            [
                Paragraph("<b>📋 Position:</b>", self.styles['BodyText']),
                Paragraph(f"<font color={INETUM_DARK.hexval()}><b>{clean_tender}</b></font>",
                         self.styles['BodyText'])
            ],
        ]
        
        info_table = Table(info_data, colWidths=[1.8*inch, 5.2*inch])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), HexColor("#E8F4F8")),
            ('TEXTCOLOR', (0, 0), (-1, -1), INETUM_TEXT),
            ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
            ('ALIGN', (1, 0), (1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('LEFTPADDING', (0, 0), (-1, -1), 14),
            ('RIGHTPADDING', (0, 0), (-1, -1), 14),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('BORDER', (0, 0), (-1, -1), 1),
            ('BORDERCOLOR', (0, 0), (-1, -1), INETUM_TEAL),
        ]))
        story.append(info_table)
        story.append(Spacer(1, 0.3*inch))

        
        story.append(Paragraph("<b>COMPATIBILITY SCORE</b>", self.styles['SectionHeader']))
        story.append(Spacer(1, 0.1*inch))
        story.append(self._create_match_score_visualization(match_score))
        story.append(Spacer(1, 0.35*inch))

  
        story.append(Paragraph("<b>SKILLS ANALYSIS</b>", self.styles['SectionHeader']))
        story.append(Spacer(1, 0.1*inch))
        
 
        cv_set = set(extra) if extra else set()
        tender_set = set(missing) if missing else set()
        matched_skills = list(cv_set.union(tender_set) - tender_set) if extra and missing else extra or []
        
        story.append(self._create_skills_table(matched_skills, missing, extra))
        story.append(Spacer(1, 0.3*inch))

 
        story.append(Paragraph("<b>RECOMMENDATIONS</b>", self.styles['SectionHeader']))
        story.append(Spacer(1, 0.1*inch))
        story.append(self._create_recommendations(match_score, missing))
        story.append(Spacer(1, 0.35*inch))

        
        metrics_text = f"Total Required Skills: {len(set(missing or [])) + len(set(extra or []))} | Matched: {len(set(extra or []))} | Missing: {len(set(missing or []))}"
        story.append(Paragraph(
            f"<font size=9 color={INETUM_ACCENT.hexval()}><b>{metrics_text}</b></font>",
            ParagraphStyle('metrics', parent=self.styles['Normal'], alignment=TA_CENTER)
        ))
        story.append(Spacer(1, 0.1*inch))
        story.append(self._create_footer(cv_name, tender_name))

     
        doc.build(story)
        print(f"Report generated: {pdf_filename}")
        return pdf_filename


def generate_report(cv_name, tender_name, match_score, missing, extra):

    reporter = InetumPDFReporter()
    return reporter.generate_report(cv_name, tender_name, match_score, missing, extra)
