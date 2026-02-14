import tabula
pdf_path = r"C:\Users\pende\OneDrive\Desktop\Desktop\pyspark_data\ast_sci_data_tables_sample.pdf"

dfs = tabula.read_pdf(pdf_path,pages='all')

for i in range(len(dfs)):
    dfs[i].to_csv(i)
