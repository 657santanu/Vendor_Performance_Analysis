import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s-%(levelname)s-%(message)s",
    filemode="a"
)

def create_vendor_summary(conn):
    ''' This function will merge the different tables to get the overall vendor summary and adding new columns in the resultant data '''
    vendor_sales_summary=pd.read_sql_query("""with FreightSummary as  (
    select VendorNumber,sum(Freight) as FreightCost 
    from vendor_invoice
    group by VendorNumber
    ),

   PurchaseSummary as (
   select p.VendorNumber,
   p.VendorName,
   p.Brand,
   p.Description,
   p.PurchasePrice,
   pp.Price as ActualPrice,
   pp.Volume,
   sum(p.Quantity) as TotalPurchaseQuantity,
   sum(p.Dollars) as TotalPurchaseDollars
   from purchases p
   join purchase_prices pp
   on p.Brand=pp.Brand
   where p.PurchasePrice > 0 
   group by p.VendorNumber,p.VendorName,p.Brand,p.Description,p.PurchasePrice,pp.Price,pp.Volume
   ),

   SalesSummary as (
   select VendorNo,
   Brand,
   sum(SalesQuantity) as TotalSalesQuantity,
   sum(SalesDollars) as TotalSalesDollars,
   sum(SalesPrice) as TotalSalesPrice,
   sum(ExciseTax) as TotalExciseTax
   from sales
   group by VendorNo,Brand
   )

   select ps.VendorNumber,
   ps.VendorName,
   ps.Brand,
   ps.Description,
   ps.PurchasePrice,
   ps.ActualPrice,
   ps.Volume,
   ps.TotalPurchaseQuantity,
   ps.TotalPurchaseDollars,
   ss.TotalSalesQuantity,
   ss.TotalSalesDollars,
   ss.TotalSalesPrice,
   ss.TotalExciseTax,
   fs.FreightCost
   from PurchaseSummary ps
   left join SalesSummary ss
   on ps.VendorNumber=ss.VendorNo
   and ps.Brand=ss.Brand
   left join FreightSummary fs
   on ps.VendorNumber=fs.VendorNumber
   order by ps.TotalPurchaseDollars DESC""",conn)

   return vendor_sales_summary


def clean_data(df):
    '''This Function will clean the data'''

    df['Volume']=df['Volume'].astype('float64')
    df.fillna(0,inplace=True)
    df['VendorName']=df['VendorName'].str.strip()
    df['Description']=df['Description'].str.strip()


    vendor_sales_summary['GrossProfit']=vendor_sales_summary['TotalSalesDollars']-vendor_sales_summary['TotalPurchaseDollars']
    vendor_sales_summary['ProfitMargin']=(vendor_sales_summary['GrossProfit']/vendor_sales_summary['TotalSalesDollars'])*100
    vendor_sales_summary['StockTurnover']=vendor_sales_summary['TotalSalesQuantity']/vendor_sales_summary['TotalPurchaseQuantity']
    vendor_sales_summary['SalestoPurchaseRatio']=vendor_sales_summary['TotalSalesDollars']/vendor_sales_summary['TotalPurchaseDollars']

    return df

if __name=='__main__':
    conn=sqlite3.connect('inventory.db')
    
    logging.info('Creating Vendor Summary Table.....')
    summary_df=create_vendor_summary(conn)
    logging.info(summary_df.head())

    logging.info('Cleanin data........')
    clean_df=clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data.......')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')