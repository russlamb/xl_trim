import pandas as _pandas
import sys as _sys
	
def trim_data_rows(in_file, rows_to_trim, out_file):
	xl_input=_pandas.read_excel(in_file,0)
	xl_output=xl_input[rows_to_trim:]
	xl_writer=_pandas.ExcelWriter(out_file)
	xl_output.to_excel(xl_writer,'Sheet1', index=False)
	xl_writer.save()

def trim_header_rows(in_file, rows_to_trim, out_file):
	xl_input=_pandas.read_excel(in_file,0,skiprows=rows_to_trim)
	xl_output=xl_input[:]
	xl_writer=_pandas.ExcelWriter(out_file)
	xl_output.to_excel(xl_writer,'Sheet1', index=False)
	xl_writer.save()

def _usage():
	print("""\
	Usage: module input_file, number_of_rows, output_file
	""")
	
if __name__ == "__main__":
	trim_header_rows(str(_sys.argv[1]),int(_sys.argv[2]),str(_sys.argv[3]))
	
