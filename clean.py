import numpy as np
import pandas as pd
from sklearn import preprocessing, impute
data = pd.read_csv("C:/Users/ACER/Downloads/honda_sell_data.csv", index_col=None, encoding='cp1252')
data_fix = np.array(data['Consumer_Rating']).reshape((len(data['Consumer_Rating']),1))

#Thêm cột giá trị gán nhãn
def fix_2():
    danh_gia = ["Kém", "Trung bình", "Khá", "Tốt"]
    dk = [0, 2, 3, 4, 5]
    data["Xếp loại"] = pd.cut(data["Consumer_Rating"], bins=dk, labels=danh_gia)
    data.to_csv('D:/data/preprocessing.csv',mode='a', index=False)

#Xóa cột giá trị thiếu quá nhiều và nhiều giá trị lỗi
def fix_3():
    data_fix = data.drop('MPG', axis=1)
    data_fix.to_csv('D:/data/preprocessing.csv',mode='a', index=False)

#chỉnh sửa Exterior_Styling_Rating
def fix_1():
    data_fix = np.array(data['Exterior_Styling_Rating']).reshape((len(data['Exterior_Styling_Rating']),1))
    imp = impute.SimpleImputer(strategy='mean')
    imp.fit(data_fix)
    fixed_data = imp.transform(data_fix)
    data['Exterior_Styling_Rating'] = np.array(fixed_data)
    round(data['Exterior_Styling_Rating'],2)
    data.to_csv('D:/data/preprocessing.csv',mode='a', index=False)
#chỉnh sửa Mileage
def fix_mileage_1():
    data_new = data[data['Condition']=='New']
    data_new = data_new.replace('â€“', np.nan)
    data_new = data_new.replace('USB', np.nan)
    data_new = data_new.replace('BluetoothUSB', np.nan)
    data_fix = np.array(data_new['Mileage']).reshape((len(data_new['Mileage']),1))
    imp = impute.SimpleImputer(strategy='median')
    imp.fit(data_fix)
    fixed_data = imp.transform(data_fix)
    data_new['Mileage'] = np.array(fixed_data)
    print(data_new['Mileage'])
    data_new.to_csv('D:/data/preprocessing.csv',mode='a', index=False)

def fix_mileage_2():
    data_new = data[data['Condition'] == 'Used']
    data_new = data_new.replace('â€“', np.nan)
    data_new = data_new.replace('USB', np.nan)
    data_new = data_new.replace('BluetoothUSB', np.nan)
    data_new = data_new.replace('Premium', np.nan)
    data_new = data_new.replace('HomeLinkRear', np.nan)
    data_new = data_new.replace('Alloy', np.nan)
    data_new = data_new.replace('Apple', np.nan)
    data_fix = np.array(data_new['Mileage']).reshape((len(data_new['Mileage']), 1))
    imp = impute.SimpleImputer(strategy='median')
    imp.fit(data_fix)
    fixed_data = imp.transform(data_fix)
    data_new['Mileage'] = np.array(fixed_data)
    data_new.to_csv('D:/data/preprocessing.csv',mode='a', index=False)

def fix_mileage_3():
    data_new = data[data['Condition'] == 'Honda Certified']
    data_new = data_new.replace('â€“', np.nan)
    data_new = data_new.replace('USB', np.nan)
    data_new = data_new.replace('BluetoothUSB', np.nan)
    data_new = data_new.replace('HomeLinkRear', np.nan)
    data_fix = np.array(data_new['Mileage']).reshape((len(data_new['Mileage']), 1))
    imp = impute.SimpleImputer(strategy='median')
    imp.fit(data_fix)
    fixed_data = imp.transform(data_fix)
    data_new['Mileage'] = np.array(fixed_data)
    data_new.to_csv('D:/data/preprocessing.csv', mode='a', index=False)


fix_mileage_1()
fix_mileage_2()
fix_mileage_3()
fix_1()
fix_2()
fix_3()
import pandas as pd

# Đọc dữ liệu từ file Excel
doc_file = pd.read_csv(
    r"C:/Users/ACER/Desktop/STUDY/hoc_may_1/honda_sell_data.csv", encoding="cp1252")

def excelRepalce(doc, column_replace,error, replace_text):
    df = doc
    column_name = column_replace
    # Thay thế kí tự "â€“" bằng kí tự mới
    replacement_character = replace_text
    df[column_name] = df[column_name].replace(error, replacement_character)

    # Hiển thị DataFrame sau khi thay thế giá trị
    print("DataFrame sau khi thay thế giá trị:")
    print(df)
    # Ghi DataFrame sau khi thay thế vào file Excel mới nếu cần
    excel_replace = "C:/Users/ACER/Desktop/STUDY/hoc_may_1/excel_replace.csv"
    df.to_csv(excel_replace, index=False)
    print("\nDữ liệu đã được xử lý và lưu vào:", excel_replace)

excelRepalce(doc=doc_file, column_replace="Interior_Color", error ="â€“", replace_text="unknown_color")
excelRepalce(doc=doc_file, column_replace="Interior_Color", error =".", replace_text="unknown_color")
#cot Exterior Color thay the ki tu â€“ bang unknown_color
excelRepalce(doc=doc_file, column_replace="Exterior_Color", error ="â€“", replace_text="unknown_color")

#them vao o trong ki tu unknown
def insertExcel(doc,column_replace,new_value):
    df = doc
    # Chọn cột cần thêm giá trị
    column_name = column_replace
    # Thêm giá trị "unknown" vào các ô có giá trị trống
    df[column_name].fillna(new_value, inplace=True)
    # Hiển thị DataFrame sau khi thêm giá trị
    print("DataFrame sau khi thêm giá trị {new_value}:")
    print(df)
    # Ghi DataFrame sau khi thay thế vào file Excel mới nếu cần
    excel_replace = "C:/Users/ACER/Desktop/STUDY/hoc_may_1/excel_replace.csv"
    df.to_csv(excel_replace, index=False)
    print("\nDữ liệu đã được xử lý và lưu vào:", excel_replace)

insertExcel(doc=doc_file, column_replace="Interior_Color",new_value="unknown_color")
insertExcel(doc=doc_file, column_replace="Exterior_Color",new_value="unknown_color")
# data.to_csv('D:/data/preprocessing.csv', index=False)
insertExcel(doc=doc_file, column_replace="Fuel_Type",new_value="unknown")
insertExcel(doc=doc_file, column_replace="Transmission",new_value="unknown")
excelRepalce(doc=doc_file, column_replace="Transmission", error ="â€“", replace_text="unknown")
insertExcel(doc=doc_file, column_replace="Stock_#",new_value="unknown")