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

import pandas as pd
import numpy as np


def handle_outliers(data):
    try:
        # Kiểm tra xem DataFrame có dữ liệu hay không
        if data.empty:
            raise ValueError("Dữ liệu trống. Không thể xử lý giá trị ngoại lệ.")

        # Lấy danh sách các cột chứa dữ liệu là số
        numeric_columns = data.select_dtypes(include=[np.number]).columns

        # Kiểm tra xem có dữ liệu số để xử lý không
        if not numeric_columns.empty:
            # Khởi tạo biến đếm cho giá trị ngoại lệ
            total_outliers_before = 0
            total_outliers_after = 0

            # Duyệt qua từng cột số để xử lý giá trị ngoại lệ
            for col in numeric_columns:
                # Kiểm tra xem có đủ dữ liệu để tính toán không
                if len(data[col]) < 2:
                    raise ValueError(f"Cột '{col}' không có đủ dữ liệu để xử lý giá trị ngoại lệ.")

                # Xác định ngưỡng trên và dưới dựa trên quantiles
                Q1 = data[col].quantile(0.25)
                Q3 = data[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                # Đếm số lượng giá trị ngoại lệ trước khi xử lý
                total_outliers_before += data[col][(data[col] < lower_bound) | (data[col] > upper_bound)].count()

                # Xử lý giá trị ngoại lệ bằng cách thay thế chúng bằng giá trị trung bình
                data[col] = np.where((data[col] < lower_bound) | (data[col] > upper_bound), data[col].mean(), data[col])

                # Đếm số lượng giá trị ngoại lệ sau khi xử lý
                total_outliers_after += data[col][(data[col] < lower_bound) | (data[col] > upper_bound)].count()

            # In kết quả tổng số lượng giá trị ngoại lệ trước và sau khi xử lý
            print(f'Tổng số lượng giá trị ngoại lệ trước khi xử lý: {total_outliers_before}')
            print(f'Tổng số lượng giá trị ngoại lệ sau khi xử lý: {total_outliers_after}')

            # Lưu dữ liệu mới vào file CSV
            output_file = "data/outliers_data_processed.csv"
            data.to_csv(output_file, index=False)
            print(f"Dữ liệu đã được lưu vào '{output_file}'.")

            return data

        else:
            raise ValueError("Không có cột nào chứa dữ liệu là số.")

    except Exception as e:
        error_message = f"Lỗi xảy ra: {str(e)}"
        print(error_message)
        # Ghi log lỗi vào một file hoặc hệ thống log
        with open("error_log.txt", "a") as log_file:
            log_file.write(error_message + "\n")
        return None


# Đọc dữ liệu từ file hoặc nguồn dữ liệu khác
data = pd.read_csv("C:/ML/ML1/Honda/data/honda_sell_data.csv")

# Xử lý giá trị ngoại lệ
handled_data = handle_outliers(data)

# Kiểm tra xem có lỗi xảy ra không trước khi hiển thị dữ liệu
if handled_data is not None:
    # Hiển thị dữ liệu sau khi xử lý
    print(handled_data)
# Chế Linh

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Không tìm thấy file {file_path}. Vui lòng kiểm tra lại đường dẫn.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"File {file_path} không chứa dữ liệu.")
    except pd.errors.ParserError:
        raise ValueError(f"Không thể đọc dữ liệu từ file {file_path}. Định dạng không hợp lệ.")

def display_missing_values(df, message="Số liệu thiếu:"):
    missing_values = df.isnull().sum()
    print(f"{message}")
    print(missing_values)

def handle_numeric_missing_values(df):
    try:
        numeric_columns = df.select_dtypes(include=['number']).columns
        numeric_imputer = SimpleImputer(strategy='mean')
        df[numeric_columns] = numeric_imputer.fit_transform(df[numeric_columns])
        return round(df, 1)
    except Exception as e:
        raise Exception(f"Lỗi xử lý dữ liệu số thiếu: {str(e)}")

def handle_string_missing_values(df):
    try:
        string_columns = df.select_dtypes(include=['object']).columns
        string_imputer = SimpleImputer(strategy='constant', fill_value=0)
        df[string_columns] = string_imputer.fit_transform(df[string_columns])
        return df
    except Exception as e:
        raise Exception(f"Lỗi xử lý dữ liệu chuỗi thiếu: {str(e)}")

def handle_missing_values(df):
    try:
        df_before = df.copy()  # Sao chép DataFrame trước khi xử lý
        df = handle_numeric_missing_values(df)
        df = handle_string_missing_values(df)
        return df_before, df
    except Exception as e:
        raise Exception(f"Lỗi xử lý dữ liệu thiếu: {str(e)}")

def save_processed_data(df, output_file_path="C:/ML/ML1/Honda/data/missing_data_processed.csv"):
    try:
        df.to_csv(output_file_path, index=False)
        print(f"Dữ liệu đã xử lý được lưu vào file: {output_file_path}")
    except Exception as e:
        raise Exception(f"Lỗi khi lưu dữ liệu đã xử lý: {str(e)}")

def main():
    try:
        file_path = "C:/ML/ML1/Honda/data/honda_sell_data.csv"  # Thay tên file thực tế của bạn
        df = load_data(file_path)

        print("*--------- DỮ LIỆU TRƯỚC KHI XỬ LÝ: ---------*")
        display_missing_values(df, message="Số liệu thiếu ban đầu:")

        df_before, df_after = handle_missing_values(df)

        print("*--------- DỮ LIỆU SAU KHI ĐƯỢC XỬ LÝ: ---------*")
        display_missing_values(df_after, message="Số liệu thiếu sau khi xử lý:")

        save_processed_data(df_after)

    except FileNotFoundError as e:
        print(f"Lỗi: {str(e)}")
    except pd.errors.EmptyDataError as e:
        print(f"Lỗi: {str(e)}")
    except ValueError as e:
        print(f"Lỗi: {str(e)}")
    except Exception as e:
        print(f"Lỗi chương trình chính: {str(e)}")


if __name__ == "__main__":
    main()
