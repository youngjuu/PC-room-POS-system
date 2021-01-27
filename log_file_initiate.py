# 이주연
# 결제 로그 파일 생성

from openpyxl import Workbook

def log_file_initiate():
    table_attribute = ['','결제시간','사용자','충전한 시간','상품재고','시간판매금액','상품판매금액','선택한 좌석']

    wb= Workbook()
    ws1 = wb.active #sheet 활성화
    ws1.title = '결제로그' #시트 ws1의 이름을 지정

    for c in range(1,8): 
        ws1.cell(row=1, column = c, value = table_attribute[c]) #릴레이션의 속성 지정    
    
    wb.save('결제로그.xlsx')

log_file_initiate()
