from my_package import *
from fpdf import FPDF

username = 'admin'
password = 'password'    
conn = create_db_connection("localhost", username, password)

def execute_query(query):
    conn = create_db_connection("localhost", username, password, "hospital")
    Connector.execute_query(conn, query)
    
def disp(query):
    conn = create_db_connection("localhost", username, password,"hospital")
    return Connector.disp(conn, query)

def incr(look = True):
    incr_index = disp(" Select AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'hospital' AND TABLE_NAME = 'patient'")
    # print(incr_index,type(incr_index))
    if(look):
        print("LOOKING",'delete from patient where p_id = '+str(incr_index[0][0]+1))
        insert_patient('password','name','b',0,'g',0,0,999999999,'NULL')
        execute_query('delete from patient where p_id = '+str(incr_index[0][0]+1))
        
    return incr_index[0][0]    

def init():   

    conn = create_db_connection("localhost", username, password)
    check = Connector.disp(conn,"SHOW DATABASES LIKE 'hospital'")
    if len(check) == 0:    
        Connector.create_database(conn, "hospital")
        Connector.execute_query(conn,"use hospital")
        maketables(conn)
        relate(conn)
        dept,doc = loadbasicdata()
        for elem in dept:
            execute_query(elem)
        for elem in doc:
            execute_query(elem)
            
        print("Hospital database created")
    else: 
        print("Connection to hospital established")
        execute_query("use hospital")
    
def make_page(pdf,report = "expense"):
    try:
        get_header = disp("desc " + report)
        heads = []
        fields = 0
        for tup in get_header:
            if (tup[0] != 'Password' ):
                heads.append(tup[0])
            fields += 1
        result = disp("select * from " + report)
        pdf.add_page()

        page_width = pdf.w - 2 * pdf.l_margin 

        pdf.set_font('Times','B',24.0) 
        pdf.cell(page_width, 0.0, report.upper()+' Report', align='C')
        pdf.ln(10)

        col_width = page_width/(fields)

        pdf.ln(1)

        th = pdf.font_size
        
        # max_cell_length = col_width
        # for row in result:
        #     for el in row:
        #         cell_len = col_width if 2*len(str(el)) < col_width else 2*len(str(el))
        #         #max_cell_length = cell_len if cell_len > max_cell_length else max_cell_length
        
        pdf.set_font('Times', 'B', 11.0)
        for head in heads[:-1]:
            pdf.cell(col_width, 2*th, head, border=1)
        if(report == 'doctor'):
            pdf.cell(col_width*2, 2*th, heads[-1], border=1)
        else:
            pdf.cell(col_width, 2*th, heads[-1], border=1)            
        
        pdf.ln(2*th) 
        
        pdf.set_font('Courier', '', 9)
        for row in result:
            pdf.cell(col_width, th, str(row[0]), border=1)
            if(report == 'expense'):
                pdf.cell(col_width, th, str(row[1]), border=1)    
            for el in row[2:-1]:
                pdf.cell(col_width, th, str(el), border=1)
            if(report == 'doctor'):
                pdf.cell(col_width*2, th, row[-1], border=1)
            else:
                pdf.cell(col_width, th, row[-1], border=1)
            pdf.ln(th)
        
        pdf.ln(10)

        pdf.set_font('Times','',10.0) 
        pdf.cell(page_width, 0.0, '- end of ' + report + ' report -', align='C')
        return pdf #Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=Expense_report.pdf'})    
    except Exception as e:
        print(e)
