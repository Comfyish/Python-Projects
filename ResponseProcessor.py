'''Processes responses from intake google form excel sheet and
    outputs a PDF file with the responses
    '''
import gspread
import pypdf

# read  the .json key and access the google sheet through gspread API
client = gspread.service_account(
    filename= 'key\project-intake-processor-780ca6b9d94c.json')
response_sheet =  client.open_by_key(
    '1RuQ53RA1H86tdmi97Iab6i8-XGDlt-pU8ZWfxbUBe2s'
    ).sheet1

def intake_fill(cx_name='blank'):
    intake_path = r"data\blank_intake.pdf"
    output_path = r'New Intakes\NewIntake.PDF'
    intake = pypdf.PdfReader(open(intake_path, 'rb'))
    writer = pypdf.PdfWriter()
    intake_page = intake._get_page(0)
    fields = intake.get_fields()
    print (fields)
    for page in range(36):
        intake_page = intake._get_page(page)
    with open(output_path, 'wb') as intake_completed:
        writer.write(intake_completed)

response_data = response_sheet.get('A2') # writes values as a 2D list
intake_fill()
print ('were all good')