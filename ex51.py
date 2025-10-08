import pprint
from pypdf import PdfReader

pdf_file_name = "Statistical_Report_Beer_December_2021_revised.pdf"

def get_data_from_pdf(pdf_file_name)->dict[str, str|int]:
    with PdfReader(pdf_file_name) as reader:
        number_of_pages = len(reader.pages)
        page = reader.pages[0]
        text = page.extract_text()

        reporting_period_index = text.find("Reporting Period")
        if reporting_period_index == -1:
            ValueError("Reporting Period not found")
        reporting_period = text[reporting_period_index:].split("\n")[0].strip()
        
        report_date_index = text.find("Report Date")
        if report_date_index == -1:
            ValueError("Report Date not found")
        report_date = text[report_date_index:].split("\n")[0].strip()
        
        # production for current month, prior year, cumulative to date
        production_for_current_month_index = text.find("Production Production Production")
        if production_for_current_month_index == -1:
            ValueError("Production for current month not found")
        production_for_current_month, production_for_prior_year_current_month, production_for_current_yearcumulative_to_date, production_for_prior_year_cumulative_to_date = text[production_for_current_month_index:].split("\n")[1].strip().split(" ")
        
        stocks_on_hand_end_of_month_for_current_month_index = text.find("Stocks On Hand End-of-Month")
        if stocks_on_hand_end_of_month_for_current_month_index == -1:
            ValueError("Stocks On Hand End-of-Month not found")
        stocks_on_hand_end_of_month_for_current_month, stocks_on_hand_end_of_month_for_prior_year_current_month = text[stocks_on_hand_end_of_month_for_current_month_index:].split("\n")[1].strip().split(" ")
        # Convert string values to integers (or floats if needed) before subtraction
        try:
            stocks_on_hand_end_of_month_for_prior_year_current_month_num = int(stocks_on_hand_end_of_month_for_prior_year_current_month.replace(',', ''))
            stocks_on_hand_end_of_month_for_current_month_num = int(stocks_on_hand_end_of_month_for_current_month.replace(',', ''))
        except ValueError:
            print("Error converting stocks on hand end of month for prior year current month to number")
            exit()
        the_difference_between_stock_on_hand_for_prior_year_current_month_and_current_month = stocks_on_hand_end_of_month_for_prior_year_current_month_num - stocks_on_hand_end_of_month_for_current_month_num
    return {
        "reporting_period": reporting_period.split(":")[1].strip(),
        "report_date": report_date.split(":")[1].strip(),
        "production_for_current_month": production_for_current_month,
        "production_for_prior_year_current_month": production_for_prior_year_current_month,
        "production_for_current_yearcumulative_to_date": production_for_current_yearcumulative_to_date,
        "production_for_prior_year_cumulative_to_date": production_for_prior_year_cumulative_to_date,
        "stocks_on_hand_end_of_month_for_current_month": stocks_on_hand_end_of_month_for_current_month,
        "stocks_on_hand_end_of_month_for_prior_year_current_month": stocks_on_hand_end_of_month_for_prior_year_current_month,
        "the_difference_between_stock_on_hand_for_prior_year_current_month_and_current_month": the_difference_between_stock_on_hand_for_prior_year_current_month_and_current_month
    }

if __name__ == "__main__":
    pprint.pprint(get_data_from_pdf(pdf_file_name))
