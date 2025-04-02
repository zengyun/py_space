import akshare as ak
stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
#stock_zh_a_spot_em_df = ak.stock_zh_a_spot()
stock_zh_a_spot_em_df.to_json("all_items.json",orient="records", force_ascii=False, indent=4)
stock_zh_a_spot_em_df.to_excel("all_items.xls",index=False,sheet_name="1",engine="openpyxl")
print(stock_zh_a_spot_em_df)