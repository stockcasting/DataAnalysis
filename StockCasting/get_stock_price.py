import FinanceDataReader as fdr

'''
period_price_download 함수
기능: market에 포함된 종목들의 특정 기간 동안의 주가 데이터를 csv파일로 저장합니다.
'''
def period_price_download(symbol ,start_date, end_date):

    stock_price = fdr.DataReader(symbol, start_date, end_date)

    # 'Date' index to column
    stock_price.reset_index(inplace=True)
    stock_price.rename(columns={'index':'Date'}, inplace=True)

    print(f'{symbol} price shape:{stock_price.shape}')
    stock_price.to_csv("price"+start_date+'_'+end_date+".csv", index=False)

    print("stock_price download complete.")


if __name__ == "__main__":
    period_price_download('005930', '2018-01-01', '2020-06-30')

