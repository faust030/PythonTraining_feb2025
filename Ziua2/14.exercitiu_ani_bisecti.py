
import numpy as np

start_date = 990
end_date = 2010

arr = np.arange(start_date, end_date)
arr_2 = arr[((arr % 4 == 0) & (arr % 100 != 0)) | (arr % 400 == 0)]

print(arr_2)